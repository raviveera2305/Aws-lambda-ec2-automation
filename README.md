🚀 AWS Lambda EC2 Instance Automation Using Boto3

Automating Amazon EC2 instance management using AWS Lambda and Python Boto3 based on EC2 resource tags.
________________________________________

📌 Project Overview

This project demonstrates a serverless automation solution using AWS Lambda and Boto3.

The Lambda function automatically identifies EC2 instances based on predefined tags and performs the appropriate action:

•	Stops instances tagged with Action=Auto-Stop

•	Starts instances tagged with Action=Auto-Start

This approach helps automate operational tasks and reduces manual intervention in managing cloud resources.

________________________________________

🎯 Assignment Objective

Gain hands-on experience with:

•	AWS Lambda

•	Amazon EC2

•	AWS IAM

•	Python Boto3 SDK

•	Serverless Automation
________________________________________
🏗️ Architecture
 
 <img width="213" height="358" alt="image" src="https://github.com/user-attachments/assets/10607852-8b96-4acf-9689-2652153d27e6" />

________________________________________

☁️ AWS Services Used

•	AWS Lambda

•	Amazon EC2

•	AWS IAM

•	Amazon CloudWatch logs

•	Boto3 SDK for Python
________________________________________

🖥️ EC2 Configuration

AutoStop Instance

Name   : AutoStop-Instance

Tag Key: Action


Value  : Auto-Stop

AutoStart Instance

Name   : AutoStart-Instance

Tag Key: Action

Value  : Auto-Start

________________________________________

🔐 IAM Configuration

IAM Role

LambdaEC2ManagementRole

Attached Policy

AmazonEC2FullAccess

________________________________________

⚡ Lambda Function Details

Function Name

EC2TagAutomation

Runtime

Python 3.14

Responsibilities

•	Discover EC2 instances using tags

•	Stop Auto-Stop instances

•	Start Auto-Start instances

•	Generate execution logs

________________________________________

📂 Repository Structure

Assignment-1-Lambda-EC2-Automation

│

├── src

│   └── lambda_function.py

│

├── Documentation

│

├── Screenshots

│   ├── 01-AutoStop-Instance-Running.png

│   ├── 02-AutoStart-Instance-Running.png

│   ├── 03-Both-Instances-Created.png

│   ├── 04-Lambda-IAM-Role.png

│   ├── 05-Lambda-Function-Created.png

│   ├── 06-Lambda-Code-Deployed.png

│   ├── 07-Pre-Test-Instance-State.png

│   ├── 08-Lambda-Test-Success.png

│   └── 09-Post-Test-Instance-State.png

│

└── README.md

________________________________________

🧪 Testing Performed

Before Lambda Execution

•	AutoStop-Instance -> Running

•	AutoStart-Instance -> Stopped

After Lambda Execution

•	AutoStop-Instance -> Stopped

•	AutoStart-Instance -> Running

________________________________________

✅ Results

The Lambda function successfully:

•	Identified EC2 instances using tags

•	Stopped instances tagged as Auto-Stop

•	Started instances tagged as Auto-Start

•	Logged execution details in CloudWatch

The automation worked as expected and fulfilled all assignment requirements.

________________________________________




