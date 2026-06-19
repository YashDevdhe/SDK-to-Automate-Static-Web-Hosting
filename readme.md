# AWS S3 Static Website Hosting Automation

## Project Overview

This project automates the deployment of a static website on Amazon S3 using Python and the AWS SDK for Python (boto3).

The script performs the complete deployment process automatically:

* Creates an S3 bucket
* Uploads website files
* Enables static website hosting
* Applies bucket policy
* Generates a website endpoint

## Architecture

Local Website Files → Python Script (boto3) → Amazon S3 → Static Website Hosting

## Technologies Used

* Python
* AWS SDK (boto3)
* Amazon S3
* AWS CLI

## Project Structure

aws-s3-static-website-automation/

├── website/
│   ├── index.html
│   └── style.css
│
├── deploy.py
├── requirements.txt
└── README.md

## Features

* Automated S3 bucket creation
* Automated website file upload
* Static website hosting configuration
* Public access policy configuration
* One-click deployment

## Prerequisites

* AWS Account
* Python 3.x
* AWS CLI configured
* boto3 installed

## Installation

Install dependencies:

pip install -r requirements.txt

Configure AWS credentials:

aws configure

## Run the Project

python deploy.py

## Expected Output

Bucket Created

Files Uploaded

Static Website Hosting Enabled

Public Access Policy Applied

Deployment Successful

## Learning Outcomes

* AWS S3 Operations
* boto3 SDK Usage
* Infrastructure Automation
* Static Website Hosting
* Cloud Deployment Automation

## Author

Yash Devdhe
AWS Cloud & DevOps Enthusiast
