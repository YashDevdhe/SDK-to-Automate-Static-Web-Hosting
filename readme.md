# AWS S3 Static Website Hosting Automation

## Overview

This project automates the deployment of a static website on Amazon S3 using Python and the AWS SDK for Python (boto3).

Instead of manually creating buckets, uploading files, enabling website hosting, and configuring permissions through the AWS Console, this script performs the entire deployment process automatically.

The goal of this project is to demonstrate cloud automation using Python and AWS services.

---

## Project Workflow

1. Create an S3 bucket
2. Upload website files to the bucket
3. Configure static website hosting
4. Apply a public-read bucket policy
5. Generate the website endpoint
6. Access the deployed website from the browser

---

## Architecture

```text
Local Website Files
        │
        ▼
 Python Script (boto3)
        │
        ▼
    Amazon S3
        │
        ▼
 Static Website Hosting
        │
        ▼
 Website Endpoint
```

---

## Technologies Used

* Python
* boto3
* Amazon S3
* AWS CLI

---

## Project Structure

```text
aws-s3-static-website-automation/

├── website/
│   ├── index.html
│   └── style.css
│
├── deploy.py
├── requirements.txt
└── README.md
```

---

## Features

* Automated S3 bucket creation
* Automated website file upload
* Static website hosting configuration
* Public access policy setup
* Website endpoint generation
* Single-command deployment

---

## Prerequisites

Before running the project, make sure you have:

* An AWS account
* Python 3.x installed
* AWS CLI installed and configured
* Required Python dependencies installed

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/aws-s3-static-website-automation.git
cd aws-s3-static-website-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure AWS credentials:

```bash
aws configure
```

---

## Usage

Run the deployment script:

```bash
python deploy.py
```

---

## Sample Output

```text
Creating S3 bucket...
Bucket created successfully.

Uploading website files...
Files uploaded successfully.

Enabling static website hosting...
Website hosting enabled.

Applying bucket policy...
Policy applied successfully.

Deployment completed.

Website URL:
http://your-bucket-name.s3-website-region.amazonaws.com
```

---

## What I Learned

Through this project, I gained hands-on experience with:

* Amazon S3 operations
* AWS SDK for Python (boto3)
* Infrastructure automation
* Static website hosting
* AWS IAM permissions
* Cloud deployment workflows

---

## Future Improvements

* Custom domain integration
* HTTPS using CloudFront
* Automatic bucket name generation
* CI/CD integration using GitHub Actions
* Infrastructure as Code using Terraform

---

## Author

**Yash Devdhe**

AWS Cloud & DevOps Enthusiast

Focused on building cloud-native solutions and automating infrastructure using AWS services and Python.
