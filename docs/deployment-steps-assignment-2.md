### \# Assignment 2: Deployment Steps



#### \## Step 1: Create S3 Bucket



1\. Open the AWS Management Console.

2\. Navigate to Amazon S3.

3\. Create a new S3 bucket.

4\. Use the bucket name:



`s3-cleanup-raviveera`



5\. Keep the remaining settings at their default values.

6\. Create the bucket.



Screenshot: `12-S3-Bucket-Creation.png`



#### \## Step 2: Upload Test Files



1\. Open the newly created S3 bucket.

2\. Upload multiple test files.

3\. Verify that the uploaded objects are visible in the Objects tab.



Screenshot: `13-S3-Bucket-Details.png`



Screenshot: `14-Test-Files-Uploaded.png`



#### \## Step 3: Create IAM Role



1\. Open IAM.

2\. Navigate to Roles.

3\. Create a role for the Lambda service.

4\. Select Lambda as the trusted service.

5\. Attach `AmazonS3FullAccess`.

6\. Create the role with the name:



`LambdaS3CleanupRole`



Screenshot: `15-IAM-Role-and-Permissions.png`



#### \## Step 4: Create Lambda Function



1\. Open AWS Lambda.

2\. Select Create Function.

3\. Choose Author from scratch.

4\. Function name:



`S3CleanupFunction`



5\. Select Python as the runtime.

6\. Select `LambdaS3CleanupRole` as the execution role.

7\. Create the function.



###### Screenshots:



\* `16-Lambda-Function-Created.png`

\* `17-Lambda-Execution-Role.png`



#### \## Step 5: Configure Lambda Code



1\. Open the Lambda Code tab.

2\. Replace the default code with the S3 cleanup Python code.

3\. Configure the S3 bucket name.

4\. Set the default retention period to 30 days.

5\. Deploy the function.



###### Screenshots:



\* `18-Lambda-Code-Editor.png`

\* `19-Lambda-Deploy-Success.png`



#### \## Step 6: Create Test Event



###### Create a Lambda test event named:



`S3CleanupTest`



The test event was initially configured for controlled testing.



###### Screenshot:



`20-Test-Event-Creation.png`



#### \## Step 7: Test Lambda



Invoke the Lambda function using the configured test event.



The function evaluates the S3 objects and deletes objects that meet the test retention criteria.



##### Screenshot:



`21-Lambda-Test-Execution.png`



#### \## Step 8: Verify S3 Cleanup



Open the S3 bucket and verify that the cleanup has occurred.



The newer object remained in the bucket after the cleanup test.



###### Screenshot:



`22-S3-Bucket-After-Cleanup.png`



#### \## Step 9: Verify CloudWatch Logs



1\. Open Amazon CloudWatch.

2\. Navigate to Logs.

3\. Open the Lambda log group.

4\. Open the latest log stream.

5\. Verify the cleanup messages and deleted object information.



###### Screenshot:



`23-CloudWatch-Logs.png`



#### \## Step 10: Restore Final Configuration



After testing, the Lambda function was restored to the required production configuration.



###### The final retention period is:



`30 days`



The temporary testing logic was removed.



###### Screenshot:



`24-Final-Lambda-30-Day-Configuration.png`



#### \## Final Result



The S3 cleanup Lambda function was successfully implemented and tested. The final configuration automatically evaluates S3 objects and deletes objects older than 30 days while recording execution details in CloudWatch Logs.

