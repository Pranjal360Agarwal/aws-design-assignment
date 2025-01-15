# AWS Tasks Assignment

## **Overview**
This repository contains the solution for two AWS tasks:
1. **AWS Lambda Function to Add Two Numbers:** A Lambda function that takes two numbers as input, adds them, and returns the result.
2. **AWS Lambda Function to Store a Document in an S3 Bucket:** A Lambda function that uploads a document or PDF file to an S3 bucket.

---

## **Features**
- **Lambda Function for Addition:** Simple AWS Lambda function that performs addition of two numbers.
- **Lambda Function for S3 Upload:** Lambda function that stores a document or PDF file in an AWS S3 bucket.
  
---

## **Tech Stack**
- **AWS Lambda:** A serverless compute service to run code without provisioning or managing servers.
- **AWS S3:** A scalable object storage service to store documents, images, and other file types.

---

## **Setup Instructions**

### **Prerequisites**
- AWS account
- AWS CLI installed and configured
- IAM role with permissions to execute Lambda functions and interact with S3.

### **Steps to Deploy the Lambda Functions**

#### 1. **Lambda Function to Add Two Numbers**
   - **Create the Lambda Function:**
     1. Go to the AWS Lambda console.
     2. Click **Create function** and choose **Author from Scratch**.
     3. Set the runtime to **Node.js** or **Python** (as per your preferred language).
     4. Paste the Lambda function code from the `add-numbers.js` or `add-numbers.py` file into the inline editor.
     5. Set up the **IAM Role** with the necessary permissions.

   - **Test the Function:**
     1. In the Lambda console, click on **Test**.
     2. Provide sample input (e.g., `{ "num1": 5, "num2": 3 }`).
     3. Click **Test** again, and the output should show the sum of the two numbers.

#### 2. **Lambda Function to Store a Document in S3**
   - **Create the Lambda Function:**
     1. Go to the AWS Lambda console.
     2. Click **Create function** and choose **Author from Scratch**.
     3. Set the runtime to **Node.js** or **Python**.
     4. Paste the Lambda function code from the `upload-s3.js` or `upload-s3.py` file into the inline editor.
     5. Set up the **IAM Role** with permissions to interact with S3.

   - **Test the Function:**
     1. In the Lambda console, click on **Test**.
     2. Provide a sample event with the document path.
     3. Click **Test** again, and verify that the document is uploaded to the specified S3 bucket.

---

## **Project Structure**

The project consists of the following files:

1. `add-numbers.js` / `add-numbers.py`: AWS Lambda function that adds two numbers.
2. `upload-s3.js` / `upload-s3.py`: AWS Lambda function to upload a file to S3.
3. `README.md`: Instructions for setting up and running the Lambda functions.

---

## **Usage Instructions**

1. Deploy the Lambda functions to your AWS account using the steps above.
2. Test the Lambda functions using the AWS Lambda console by providing sample input data.

---

# Made with ❤ by [Pranjal Agarwal](https://github.com/Pranjal360Agarwal).
