Deployment Guide

Prerequisites

Before starting the implementation, ensure the following prerequisites are available:

•	Active AWS Account

•	Access to EC2, IAM, and Lambda services

•	Basic understanding of AWS Console navigation

•	Two EC2 instances running in the same AWS region

________________________________________

Step 1: Create EC2 Instances

Two Ubuntu EC2 instances were created in the Asia Pacific (Mumbai) region.

Instance 1

•	Name: AutoStop-Instance

•	Instance Type: t2.micro

•	Operating System: Ubuntu Server

•	Purpose: Automatically stopped by Lambda

Instance 2

•	Name: AutoStart-Instance

•	Instance Type: t2.micro

•	Operating System: Ubuntu Server

•	Purpose: Automatically started by Lambda

________________________________________

Step 2: Configure EC2 Tags- The automation logic relies on EC2 tags.


AutoStop Instance

•	Tag Key: Action

•	Tag Value: Auto-Stop

AutoStart Instance

•	Tag Key: Action

•	Tag Value: Auto-Start

These tags are used by the Lambda function to identify which action should be performed on each instance.

________________________________________

Step 3: Create IAM Role

An IAM role was created to allow Lambda to interact with EC2 resources.

Role Details

•	Role Name: LambdaEC2ManagementRole


Attached Policy

•	AmazonEC2FullAccess

This permission allows the Lambda function to:

•	Describe EC2 instances

•	Start EC2 instances

•	Stop EC2 instances

________________________________________

Step 4: Create Lambda Function

A Lambda function was created using Python runtime.

Configuration

•	Function Name: EC2TagAutomation

•	Runtime: Python 3.14

•	Execution Role: LambdaEC2ManagementRole

The function was configured to execute on demand through manual invocation.

________________________________________

Step 5: Deploy Python Code

The Lambda function uses the Boto3 SDK to:

•	Discover instances tagged with Action=Auto-Stop

•	Stop matching instances

•	Discover instances tagged with Action=Auto-Start

•	Start matching instances

•	Log affected instance IDs

The source code is available in:

src/lambda_function.py

________________________________________





Step 6: Test the Lambda Function

Before execution:

•	AutoStop-Instance was in Running state

•	AutoStart-Instance was manually stopped

A Lambda test event was created and executed manually.

Test Event

{}

Execution completed successfully without errors.

________________________________________

Validation Results

After Lambda execution:

•	AutoStop-Instance changed from Running to Stopped

•	AutoStart-Instance changed from Stopped to Running

The result confirmed that the Lambda function correctly identified EC2 instances using tags and executed the appropriate actions.

________________________________________

Conclusion

The objective of the assignment was successfully achieved by implementing a serverless automation solution using AWS Lambda and Boto3.

The solution automatically manages EC2 instances based on resource tags, reducing manual administrative effort and demonstrating practical AWS automation capabilities.














