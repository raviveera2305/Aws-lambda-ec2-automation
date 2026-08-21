# Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3


## 📌 Objective


The objective of this assignment is to create an AWS Lambda function that checks S3 buckets and identifies buckets without server-side encryption.

===============================================================

## 🏗️ Architecture

Amazon S3

    |

    | List Buckets

    v

AWS Lambda

S3EncryptionMonitor

    |

    | Check Encryption

    v

Encryption Status

    |

    +---- Encrypted ------> Secure

    |

    +---- Not Encrypted --> Security Finding

    |

    v

CloudWatch Logs

===============================================================

☁️ AWS Services Used

Amazon S3

AWS Lambda

AWS IAM

Amazon CloudWatch Logs

Python Boto3

===============================================================

🪣 Amazon S3

Three S3 buckets were created for testing the monitoring solution.

Example:

s3-encryption-monitor-raviveera-01

s3-encryption-monitor-raviveera-02

s3-encryption-monitor-raviveera-03

The bucket encryption configuration was checked during the setup.

===============================================================

🔐 IAM Configuration

The Lambda function uses the following IAM role:

LambdaS3EncryptionMonitorRole

Policies attached:

AmazonS3ReadOnlyAccess

AWSLambdaBasicExecutionRole

Purpose

AmazonS3ReadOnlyAccess allows Lambda to read S3 bucket information and encryption configuration.

AWSLambdaBasicExecutionRole allows Lambda to write execution logs to CloudWatch.

===============================================================

⚡ Lambda Function

Function Name

S3EncryptionMonitor

Runtime

Python 3.14

Source File

src/s3_encryption_monitor.py

===============================================================

🐍 Lambda Function Workflow

The Lambda function performs the following steps:

Creates a Boto3 S3 client.

Lists all S3 buckets.

Checks the encryption configuration of each bucket.

Identifies buckets without encryption configuration.

Prints the bucket names and encryption status.

Sends the execution output to CloudWatch Logs.

===============================================================

📊 CloudWatch Logs

CloudWatch Logs are used to review the Lambda execution.

The logs show:

Number of S3 buckets checked

Encryption status of each bucket

Names of any unencrypted buckets

Final scan result

Example:

ENCRYPTED: s3-encryption-monitor-raviveera-01

ENCRYPTED: s3-encryption-monitor-raviveera-02

ENCRYPTED: s3-encryption-monitor-raviveera-03

No unencrypted S3 buckets detected.

===============================================================

📌 Test Result

The Lambda function was manually invoked using the test event:

S3EncryptionMonitorTest

The function successfully scanned the available S3 buckets and reported their encryption status.

No unencrypted buckets were detected in the current test environment.