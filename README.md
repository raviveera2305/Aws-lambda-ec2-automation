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