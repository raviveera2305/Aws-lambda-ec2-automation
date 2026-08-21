# Assignment 8: Analyze Sentiment of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend

==========================================================

📌 Overview

This project demonstrates a serverless sentiment analysis solution using AWS Lambda, Python Boto3, and Amazon Comprehend.

The Lambda function receives a user review, analyzes its sentiment using Amazon Comprehend, and logs the result in Amazon CloudWatch Logs.

==========================================================

🎯 Assignment Objective

Automate the analysis and categorization of user reviews using Amazon Comprehend.

The Lambda function:

• Extracts the user review from the event

• Sends the review to Amazon Comprehend

• Detects the sentiment of the review

• Logs the sentiment result

• Returns the sentiment response

==========================================================

🔐 IAM Role Configuration

A dedicated IAM role was created for the Lambda function.

IAM Role

LambdaComprehendSentimentRole

Attached Policies

• AmazonComprehendFullAccess

• AWSLambdaBasicExecutionRole

Policy Responsibilities

AmazonComprehendFullAccess

• Allows the Lambda function to use Amazon Comprehend for sentiment analysis.

AWSLambdaBasicExecutionRole

• Allows the Lambda function to write execution logs to Amazon CloudWatch Logs.

📸 Screenshot

34-IAM-Comprehend-and-CloudWatch-Permissions.png

==========================================================

⚡ Lambda Function Creation

A new Lambda function was created from scratch.

Function Name

S3SentimentAnalyzer

Runtime

Python 3.14

Execution Role

LambdaComprehendSentimentRole

📸 Screenshot

35-Lambda-Sentiment-Function-Creation.png

==========================================================

🐍 Lambda Function Implementation

The Lambda function was implemented using Python and the Boto3 SDK.

The function performs the following operations:

• Extracts the review from the Lambda event

• Creates an Amazon Comprehend client

• Sends the review to Amazon Comprehend

• Detects the sentiment

• Retrieves the sentiment scores

• Logs the review and sentiment result

• Returns the analysis result

Source File

src/sentiment_analysis_lambda.py

📸 Screenshot

36-Lambda-Sentiment-Analysis-Code.png

==========================================================

🧪 Test Event Creation

A Lambda test event was created to provide a sample user review.

Test Event Name

SentimentPositiveTest

Test Event

```json
{
  "review": "I absolutely loved this product. The quality is excellent and I am very happy with my purchase!"
}

📸 Screenshot

37-Lambda-Sentiment-Test-Event.png

==========================================================

😊 Positive Sentiment Testing

The Lambda function was manually invoked using the positive review test event.

Expected Result

Sentiment → POSITIVE

The Lambda execution successfully analyzed the review using Amazon Comprehend.

📸 Screenshot

38-Lambda-Positive-Sentiment-Execution.png

==========================================================

😞 Negative Sentiment Testing

A second test event was used with a negative review.

Test Event Name

SentimentNegativeTest

Test Event

{

  "review": "I am very disappointed with this product. The quality is terrible and it stopped working after one day."

}

Expected Result

Sentiment → NEGATIVE

The Lambda function successfully identified the negative sentiment.

📸 Screenshot

39-Lambda-Negative-Sentiment-Execution.png

==========================================================

📊 CloudWatch Monitoring

AWS Lambda execution logs were reviewed using Amazon CloudWatch Logs.

The logs provide information including:

• User review

• Detected sentiment

• Sentiment scores

• Lambda execution status

Example:

Review: I absolutely loved this product...

Sentiment: POSITIVE

📸 Screenshot

40-CloudWatch-Sentiment-Analysis-Logs.png