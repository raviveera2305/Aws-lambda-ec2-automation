import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client("s3")

BUCKET_NAME = "s3-cleanup-raviveera"
RETENTION_DAYS = 30


def lambda_handler(event, context):

    cutoff_date = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)

    print(f"Checking bucket: {BUCKET_NAME}")
    print(f"Retention period: {RETENTION_DAYS} days")
    print(f"Deleting objects older than: {cutoff_date}")

    paginator = s3.get_paginator("list_objects_v2")

    deleted_count = 0

    for page in paginator.paginate(Bucket=BUCKET_NAME):

        for obj in page.get("Contents", []):

            if obj["LastModified"] < cutoff_date:

                file_name = obj["Key"]

                s3.delete_object(
                    Bucket=BUCKET_NAME,
                    Key=file_name
                )

                print(f"Deleted: {file_name}")

                deleted_count += 1

    print(f"Cleanup completed. Total objects deleted: {deleted_count}")

    return {
        "statusCode": 200,
        "body": f"Cleanup completed. Deleted {deleted_count} objects."
    }