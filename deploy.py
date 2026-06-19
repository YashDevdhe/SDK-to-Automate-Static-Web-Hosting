
import boto3
import os
import json
from botocore.exceptions import ClientError

# Change this bucket name to something unique
BUCKET_NAME = "yash-static-site-demo-2026"
REGION = "ap-south-1"

s3 = boto3.client("s3", region_name=REGION)

# Create bucket only if it doesn't exist
try:
    s3.head_bucket(Bucket=BUCKET_NAME)
    print(f"Bucket '{BUCKET_NAME}' already exists.")

except ClientError:
    print("Creating bucket...")

    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={
            "LocationConstraint": REGION
        }
    )

    print("Bucket created successfully.")

# Upload website files
website_folder = "website"

print("Uploading files...")

for file in os.listdir(website_folder):

    file_path = os.path.join(website_folder, file)

    if os.path.isfile(file_path):

        if file.endswith(".html"):
            content_type = "text/html"

        elif file.endswith(".css"):
            content_type = "text/css"

        elif file.endswith(".js"):
            content_type = "application/javascript"

        elif file.endswith(".png"):
            content_type = "image/png"

        elif file.endswith(".jpg") or file.endswith(".jpeg"):
            content_type = "image/jpeg"

        else:
            content_type = "binary/octet-stream"

        s3.upload_file(
            file_path,
            BUCKET_NAME,
            file,
            ExtraArgs={
                "ContentType": content_type
            }
        )

        print(f"Uploaded: {file}")

# Enable static website hosting
s3.put_bucket_website(
    Bucket=BUCKET_NAME,
    WebsiteConfiguration={
        "IndexDocument": {
            "Suffix": "index.html"
        }
    }
)

print("Static website hosting enabled.")

# Public bucket policy
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*"
        }
    ]
}

s3.put_bucket_policy(
    Bucket=BUCKET_NAME,
    Policy=json.dumps(policy)
)

print("Public access policy applied.")

# Website URL
website_url = (
    f"http://{BUCKET_NAME}.s3-website-{REGION}.amazonaws.com"
)

print("\nDeployment Successful!")
print("Website URL:")
print(website_url)