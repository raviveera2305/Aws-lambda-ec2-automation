🚀 AWS Lambda Automation Using Boto3


Serverless AWS automation projects using AWS Lambda, Python Boto3, Amazon EC2, Amazon S3, IAM, and CloudWatch.

This repository contains hands-on AWS automation assignments focused on reducing manual cloud operations through serverless automation.

==========================================================

📌 Assignment 1: AWS Lambda EC2 Instance Automation


Automating Amazon EC2 instance management using AWS Lambda and Python Boto3 based on EC2 resource tags.

==========================================================

📌 Project Overview


This project demonstrates a serverless automation solution using AWS Lambda and Boto3.

The Lambda function automatically identifies EC2 instances based on predefined tags and performs the appropriate action:

•	Stops instances tagged with Action=Auto-Stop

•	Starts instances tagged with Action=Auto-Start

This approach helps automate operational tasks and reduces manual intervention in managing cloud resources.

==========================================================

🎯 Assignment Objective


Gain hands-on experience with:

•	AWS Lambda

•	Amazon EC2

•	AWS IAM

•	Python Boto3 SDK

•	Amazon CloudWatch

•	Serverless Automation

==========================================================

🏗️ Architecture


                    ┌──────────────────────┐
                    │      AWS Lambda      │
                    │   EC2TagAutomation   │
                    │      Python/Boto3    │
                    └──────────┬───────────┘
                               
                               │

                       EC2 API Operations

                               │

                ┌──────────────┴──────────────┐
                
                │                             │

                ▼                             ▼

       ┌─────────────────┐           ┌─────────────────┐
       │                 |           |                 |
       | AutoStop-       │           │ AutoStart-      │
       │                 |           |                 |
       | Instance        │           │ Instance        │
       │                 |           |                 |
       | Action=         │           | Action=         │
       │                 |           |                 |
       | Auto-Stop       │           │ Auto-Start      |
       |                 │           |                 |
       └─────────────────┘           └─────────────────┘
                
                │                             │

                └──────────────┬──────────────┘

                               ▼

                    ┌──────────────────────┐
                    │                      |
                    |   Amazon CloudWatch  │
                    │                      |
                    |         Logs         |
                    |                      │
                    └──────────────────────┘

==========================================================

☁️ AWS Services Used

•	AWS Lambda

•	Amazon EC2

•	AWS IAM

•	Amazon CloudWatch Logs

•	Boto3 SDK for Python

==========================================================

🖥️ EC2 Configuration

AutoStop Instance

•	Name    : AutoStop-Instance

•	Tag Key : Action

•	Value   : Auto-Stop

AutoStart Instance

•	Name    : AutoStart-Instance

•	Tag Key : Action

•	Value   : Auto-Start

==========================================================

🔐 IAM Configuration

IAM Role

LambdaEC2ManagementRole

Attached Policy

AmazonEC2FullAccess

==========================================================

⚡ Lambda Function Details


•	Function Name- EC2TagAutomation

•	Runtime- Python 3.14

Responsibilities

•	Discover EC2 instances using tags

•	Stop Auto-Stop instances

•	Start Auto-Start instances

•	Generate execution logs

==========================================================

🧪 Testing Performed


Before Lambda Execution

•	AutoStop-Instance  → Running

•	AutoStart-Instance → Stopped

After Lambda Execution

•	AutoStop-Instance  → Stopped

•	AutoStart-Instance → Running

==========================================================

✅ Assignment 1 Results


The Lambda function successfully:

•	Identified EC2 instances using tags

•	Stopped instances tagged as Auto-Stop

•	Started instances tagged as Auto-Start

•	Logged execution details in CloudWatch

The automation worked as expected and fulfilled the assignment requirements.

==========================================================

🗄️ Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

Automating the deletion of Amazon S3 objects older than 30 days using AWS Lambda and Python Boto3.

==========================================================

📌 Project Overview

•	This project demonstrates a serverless S3 cleanup solution using AWS Lambda and Boto3.

•	The Lambda function evaluates objects stored in an Amazon S3 bucket using their Last Modified timestamp.

•	Objects older than the configured 30-day retention period are automatically deleted, while newer objects are retained.

•	The solution eliminates the need for manual cleanup and demonstrates practical serverless cloud automation.

==========================================================

🎯 Assignment Objective

Gain hands-on experience with:

•	AWS Lambda

•	Amazon S3

•	AWS IAM

•	Python Boto3 SDK

•	Amazon CloudWatch Logs

•	Serverless Automation

•	S3 Object Lifecycle Management

==========================================================

🏗️ Architecture


                    ┌──────────────────────┐
                    │                      |
                    |      Amazon S3       │
                    │                      |
                    | s3-cleanup-raviveera |
                    │                      |
                    └──────────┬───────────┘

                               │

                         List Objects

                               │

                               ▼

                    ┌──────────────────────┐
                    │                      |
                    |      AWS Lambda      |
                    │                      |
                    │   S3CleanupFunction  │
                    │                      |
                    |     Python/Boto3     │
                    |                      |
                    └──────────┬───────────┘

                               │

                       Check Last Modified

                               │

                               ▼

                    ┌──────────────────────┐
                    │  Older than 30 days? │
                    └──────────┬───────────┘

                               │

                    ┌──────────┴──────────┐

                    │                     │

                   YES                    NO

                    │                     │

                    ▼                     ▼
          ┌─────────────────┐    ┌─────────────────┐
          │  Delete Object  │    │  Keep Object    │
          └────────┬────────┘    └─────────────────┘

                   │

                   ▼

          ┌─────────────────────┐
          │ Amazon CloudWatch   │
          │       Logs          │         
          └─────────────────────┘

==========================================================

☁️ AWS Services Used

AWS Service-	Purpose

•	🪣 Amazon S3- Stores objects targeted for cleanup

•	⚡ AWS Lambda- Executes the automated cleanup

•	🔐 AWS IAM- Provides required Lambda permissions

•	📊 Amazon CloudWatch- Stores execution and deletion logs

•	🐍 Boto3-	Python SDK used to interact with AWS

==========================================================

🪣 S3 Configuration

Bucket

s3-cleanup-raviveera

Purpose

•	The S3 bucket contains objects that are evaluated by the Lambda function.

•	The Lambda function checks the Last Modified timestamp of each object and compares it against the configured retention period.

==========================================================

🔐 IAM Configuration

IAM Role- LambdaS3CleanupRole

Attached Policies

AmazonS3FullAccess

AWSLambdaBasicExecutionRole

Policy Responsibilities- AmazonS3FullAccess

Provides the Lambda function with access to S3 objects required for the cleanup operation.

AWSLambdaBasicExecutionRole

Provides the Lambda function with permission to write execution logs to Amazon CloudWatch Logs.

==========================================================

⚡ Lambda Function Details


•	Function Name- S3CleanupFunction

•	Runtime- Python 3.14

•	Execution Role- LambdaS3CleanupRole

•	Default Retention Period- 30 Days


Responsibilities


•	Connect to Amazon S3 using Boto3

•	List objects in the configured bucket

•	Read each object's LastModified timestamp

•	Calculate the 30-day cutoff date

•	Delete objects older than 30 days

•	Log deleted object names

•	Report the total number of deleted objects

==========================================================

🐍 Boto3 Implementation


The Lambda function uses the Boto3 S3 client and an S3 paginator to process objects.

The paginator was used so that the implementation can handle buckets containing more than 1,000 objects.

The cleanup workflow is:

Initialize Boto3 S3 Client

        ↓

Calculate 30-Day Cutoff Date

        ↓

List S3 Objects

        ↓

Read Last Modified Timestamp

        ↓

Compare Object Age

        ↓

Older Than 30 Days?

        ↓

   ┌────┴────┐

  YES        NO

   ↓          ↓

Delete       Keep

   ↓

Log Object

==========================================================

🧪 Testing Performed


A controlled test was performed using a temporary short retention period to validate the deletion functionality without waiting 30 days.

The Lambda successfully:


•	Identified eligible S3 objects

•	Deleted the objects matching the test condition

•	Logged the deleted object names

•	Retained the newer object during the cleanup verification


After successful testing, the Lambda function was restored to the required 30-day retention configuration.

==========================================================

📊 Test Result


Lambda Execution

Test retention period- 1 minute

Objects deleted- 6


S3 Verification


After the cleanup operation, the S3 bucket contained the newer test object:

•	new-test-file.txt

This verified that the cleanup logic was able to remove eligible objects while retaining a newer object.

==========================================================

📈 CloudWatch Monitoring


AWS Lambda execution logs were verified using Amazon CloudWatch Logs.

The logs provide information including:


•	Bucket being processed

•	Retention period

•	Cutoff timestamp

•	Deleted object names

•	Total number of deleted objects

•	Lambda execution status


Example:


TEST MODE: Retention period = 1 minute(s)

Checking bucket: s3-cleanup-raviveera

Deleted: <object-name>

Cleanup completed. Total objects deleted: 6

==========================================================

📌 Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3

Automating the detection of S3 buckets without server-side encryption using AWS Lambda and Python Boto3.

==========================================================

📌 Project Overview

This project demonstrates a serverless S3 security monitoring solution using AWS Lambda and Boto3.

The Lambda function:

• Lists all S3 buckets

• Checks the server-side encryption configuration of each bucket

• Identifies buckets without encryption configuration

• Logs the encryption status of each bucket

• Reports the final security scan result through CloudWatch Logs

This approach helps automate basic S3 security checks and reduces manual monitoring.

==========================================================

🎯 Assignment Objective

Gain hands-on experience with:

• AWS Lambda

• Amazon S3

• AWS IAM

• Python Boto3 SDK

• Amazon CloudWatch Logs

• Serverless Security Monitoring

==========================================================

🏗️ Architecture

                 ┌──────────────────────┐
                 │                      |
                 |      AWS Lambda      |
                 │                      | 
                 │  S3EncryptionMonitor |
                 │                      |
                 │     Python/Boto3     |
                 │                      |
                 └──────────┬───────────┘

                            │
                 
                     List S3 Buckets
                 
                            │
                 
                            ▼
                 
                 ┌──────────────────────┐
                 |                      |
                 │      Amazon S3       │
                 │                      │
                 │  Check Encryption    │
                 |                      |
                 │    Configuration     │
                 |                      | 
                 └──────────┬───────────┘

                            │
                 
                   Encryption Status
                 
                            │
                 
                 ┌──────────┴──────────┐
                 
                 │                     │
                
                YES                    NO
                
                 │                     │
                
                 ▼                     ▼
          ┌──────────────┐      ┌──────────────┐
          |              |      |              |
          │   Encrypted  │      │ Unencrypted  │
          |              |      |              | 
          │    Bucket    │      │    Bucket    │
          |              |      |              |        
          └──────┬───────┘      └──────┬───────┘
          
                 │                     │
          
                 └──────────┬──────────┘
          
                            ▼
          
                 ┌──────────────────────┐
                 |                      |
                 │   Amazon CloudWatch  │
                 |                      |
                 │        Logs          │
                 |                      |
                 └──────────────────────┘

==========================================================

☁️ AWS Services Used

AWS Service - Purpose

• 🪣 Amazon S3 - Provides the buckets being monitored

• ⚡ AWS Lambda - Executes the encryption monitoring function

• 🔐 AWS IAM - Provides Lambda with required permissions

• 📊 Amazon CloudWatch - Stores Lambda execution logs

• 🐍 Boto3 - Python SDK used to interact with AWS

==========================================================

🪣 S3 Configuration

Test Buckets

• s3-encryption-monitor-raviveera-01

• s3-encryption-monitor-raviveera-02

• s3-encryption-monitor-raviveera-03

Purpose

• The buckets were created to test the S3 encryption monitoring function.

• The default encryption configuration of the buckets was reviewed.

==========================================================

🔐 IAM Configuration

IAM Role

LambdaS3EncryptionMonitorRole

Attached Policies

• AmazonS3ReadOnlyAccess

• AWSLambdaBasicExecutionRole

Policy Responsibilities

AmazonS3ReadOnlyAccess

• Allows the Lambda function to read S3 bucket information and encryption configuration.

AWSLambdaBasicExecutionRole

• Allows the Lambda function to write execution logs to Amazon CloudWatch Logs.

==========================================================

⚡ Lambda Function Details

• Function Name - S3EncryptionMonitor

• Runtime - Python 3.14

• Execution Role - LambdaS3EncryptionMonitorRole

Responsibilities

• List all S3 buckets

• Check bucket encryption configuration

• Identify buckets without encryption configuration

• Log encryption status

• Report unencrypted buckets

==========================================================

🐍 Boto3 Implementation

The Lambda function uses the Boto3 S3 client to:

• List S3 buckets

• Check encryption configuration using get_bucket_encryption()

• Detect missing encryption configuration

• Log the results

The Lambda source file is:

src/s3_encryption_monitor.py

==========================================================

🧪 Testing Performed

A manual Lambda test event was created:

Test Event Name

S3EncryptionMonitorTest

Test Event

{}

The Lambda function was manually invoked to verify the S3 encryption monitoring logic.

The function successfully:

• Listed the available S3 buckets

• Checked encryption configuration

• Logged the encryption status

• Completed the security scan

==========================================================

📊 Test Result

The Lambda function successfully completed the S3 encryption scan.

Current AWS S3 configuration resulted in:

• Encrypted buckets detected

• No unencrypted buckets detected

Final result:

No unencrypted S3 buckets detected.

==========================================================

📈 CloudWatch Monitoring

AWS Lambda execution logs were verified using Amazon CloudWatch Logs.

The logs provide information including:

• Total number of S3 buckets checked

• Encryption status of each bucket

• Names of any unencrypted buckets

• Final security scan result

==========================================================

✅ Assignment 3 Results

The Lambda function successfully:

• Discovered S3 buckets

• Checked server-side encryption configuration

• Identified potential encryption gaps

• Generated CloudWatch logs

• Completed the security monitoring scan