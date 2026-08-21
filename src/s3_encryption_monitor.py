import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3")


def lambda_handler(event, context):

    print("Starting S3 encryption monitoring...")

    response = s3.list_buckets()

    buckets = response.get("Buckets", [])

    unencrypted_buckets = []

    print(f"Total S3 buckets found: {len(buckets)}")

    for bucket in buckets:

        bucket_name = bucket["Name"]

        try:
            encryption = s3.get_bucket_encryption(
                Bucket=bucket_name
            )

            rules = encryption.get(
                "ServerSideEncryptionConfiguration", {}
            ).get("Rules", [])

            if rules:
                print(f"ENCRYPTED: {bucket_name}")
            else:
                print(f"UNENCRYPTED: {bucket_name}")
                unencrypted_buckets.append(bucket_name)

        except ClientError as error:

            error_code = error.response["Error"]["Code"]

            if error_code == "ServerSideEncryptionConfigurationNotFoundError":
                print(f"UNENCRYPTED: {bucket_name}")
                unencrypted_buckets.append(bucket_name)

            else:
                print(
                    f"ERROR checking {bucket_name}: "
                    f"{error_code}"
                )

    print("S3 encryption monitoring completed.")

    if unencrypted_buckets:

        print("Unencrypted S3 buckets detected:")

        for bucket_name in unencrypted_buckets:
            print(f"- {bucket_name}")

    else:
        print("No unencrypted S3 buckets detected.")

    return {
        "statusCode": 200,
        "unencrypted_buckets": unencrypted_buckets
    }