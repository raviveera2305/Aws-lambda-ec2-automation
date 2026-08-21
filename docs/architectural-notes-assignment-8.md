# Assignment 8: Analyze Sentiment of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend

==========================================================

📌 Project Overview

This project demonstrates a serverless sentiment analysis solution using AWS Lambda, Python Boto3, and Amazon Comprehend.

The Lambda function receives a user review, sends it to Amazon Comprehend for sentiment analysis, and logs the sentiment result in Amazon CloudWatch Logs.

==========================================================

🎯 Assignment Objective

Gain hands-on experience with:

• AWS Lambda

• Amazon Comprehend

• AWS IAM

• Python Boto3 SDK

• Amazon CloudWatch Logs

• Serverless AI Services

==========================================================

🏗️ Architecture

```text
                 ┌──────────────────────┐
                 |                      |
                 │      AWS Lambda      │
                 |                      | 
                 │  S3SentimentAnalyzer │
                 |                      | 
                 │     Python/Boto3     │
                 |                      |
                 └──────────┬───────────┘

                            │
                 
                       User Review
                 
                            │
                 
                            ▼
                 
                 ┌──────────────────────┐
                 |                      |
                 │  Amazon Comprehend   │
                 │                      │
                 │  Detect Sentiment    │
                 |                      |
                 └──────────┬───────────┘
                 
                            │
                 
                     Sentiment Result
                 
                            │
                 
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

• ⚡ AWS Lambda - Executes the sentiment analysis function

• 🤖 Amazon Comprehend - Analyzes the sentiment of user reviews

• 🔐 AWS IAM - Provides Lambda with required permissions

• 📊 Amazon CloudWatch - Stores execution and sentiment logs

• 🐍 Boto3 - Python SDK used to interact with AWS

==========================================================

🔐 IAM Configuration

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

==========================================================

⚡ Lambda Function Details

• Function Name - S3SentimentAnalyzer

• Runtime - Python 3.14

• Execution Role - LambdaComprehendSentimentRole

Responsibilities

• Extract the user review from the event

• Send the review to Amazon Comprehend

• Analyze the sentiment of the review

• Log the sentiment result

• Return the sentiment information

==========================================================

🐍 Boto3 Implementation

The Lambda function uses the Boto3 Comprehend client to analyze user reviews.

The sentiment analysis workflow is:

Extract User Review

↓

Send Review to Amazon Comprehend

↓

Detect Sentiment

↓

Log Sentiment Result

↓

Return Sentiment Response

The Lambda source file is:

src/sentiment_analysis_lambda.py

==========================================================

🧪 Testing Performed

Manual Lambda test events were created using sample user reviews.

Positive Review

"I absolutely loved this product. The quality is excellent and I am very happy with my purchase!"

Result

• Sentiment → POSITIVE

Negative Review

"I am very disappointed with this product. The quality is terrible and it stopped working after one day."

Result

• Sentiment → NEGATIVE

The Lambda function successfully:

• Extracted the user review

• Sent the review to Amazon Comprehend

• Analyzed the sentiment

• Logged the sentiment result

• Returned the sentiment response

==========================================================

📊 CloudWatch Monitoring

AWS Lambda execution logs were verified using Amazon CloudWatch Logs.

The logs provide information including:

• User review

• Detected sentiment

• Sentiment scores

• Lambda execution status

Example:

Review: I absolutely loved this product...

Sentiment: POSITIVE

==========================================================

✅ Assignment 8 Results

The Lambda function successfully:

• Received user reviews

• Analyzed reviews using Amazon Comprehend

• Identified positive and negative sentiment

• Logged sentiment results in CloudWatch

• Returned the sentiment analysis response

The sentiment analysis worked as expected and fulfilled the assignment requirements.