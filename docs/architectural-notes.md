Architecture Notes

Solution Overview
This project uses AWS Lambda and Boto3 to automate EC2 instance management based on EC2 tags.

Components
•	Amazon EC2
•	AWS Lambda
•	AWS IAM
•	Boto3 SDK

Workflow
1.	Lambda function is invoked manually.
2.	Boto3 identifies EC2 instances tagged with Action=Auto-Stop.
3.	Matching instances are stopped.
4.	Boto3 identifies EC2 instances tagged with Action=Auto-Start.
5.	Matching instances are started.
6.	Results are logged to CloudWatch.

Architecture Diagram
Refer to:
docs/architecture-diagram.png