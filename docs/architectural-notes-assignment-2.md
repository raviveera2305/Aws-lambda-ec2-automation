### \# Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3



#### \## 1. Objective



The objective of this assignment is to automate the deletion of files older than 30 days from an Amazon S3 bucket using AWS Lambda and the Boto3 Python SDK.



#### \## 2. AWS Services Used



\* Amazon S3 – Stores the files that need to be monitored and cleaned up.

\* AWS Lambda – Executes the cleanup process without requiring a server.

\* AWS IAM – Provides permissions for Lambda to access S3 and write execution logs.

\* Amazon CloudWatch – Stores Lambda execution logs for monitoring and troubleshooting.



#### \## 3. Architecture



###### The solution follows this workflow:



S3 Bucket → AWS Lambda → Boto3 → S3 Object Evaluation → Delete Old Objects → CloudWatch Logs



#### \## 4. S3



An S3 bucket named `s3-cleanup-raviveera` was created to store test objects.



The Lambda function checks the `LastModified` timestamp of objects stored in this bucket.



#### \## 5. AWS Lambda



###### The Lambda function is named:



`S3CleanupFunction`



The function uses Python and the Boto3 SDK to communicate with Amazon S3.



The default retention period is configured as 30 days.



#### \## 6. IAM



###### The Lambda execution role is:



`LambdaS3CleanupRole`



The role provides the permissions required by the Lambda function.



###### Policies used:



\* AmazonS3FullAccess

\* AWSLambdaBasicExecutionRole



`AmazonS3FullAccess` allows the function to access and delete S3 objects.



`AWSLambdaBasicExecutionRole` allows the Lambda function to send execution logs to Amazon CloudWatch Logs.



#### \## 7. Cleanup Logic



The Lambda function calculates a cutoff date based on the current UTC time and the configured 30-day retention period.



###### For each S3 object:



1\. The object's `LastModified` timestamp is retrieved.

2\. The timestamp is compared with the calculated cutoff date.

3\. If the object is older than 30 days, it is deleted.

4\. The deleted object's name is printed to the Lambda logs.



#### \## 8. Pagination



The implementation uses the S3 `list\_objects\_v2` paginator so that the function can process buckets containing more than 1,000 objects.



#### \## 9. Logging and Monitoring



Lambda execution information is written to Amazon CloudWatch Logs.



###### The logs record:



\* Bucket being checked

\* Retention period

\* Cleanup activity

\* Names of deleted objects

\* Total number of deleted objects



#### \## 10. Testing



A controlled test was performed using a temporary short retention period to verify the deletion logic.



The test successfully deleted eligible S3 objects while leaving the newer object in the bucket.



After testing, the Lambda function was restored to the required 30-day retention configuration.



#### \## 11. Final Architecture



###### The final architecture consists of:



\* Amazon S3

\* AWS Lambda

\* AWS IAM

\* Amazon CloudWatch

\* Boto3



The solution provides a serverless approach to automatically managing old S3 objects.



