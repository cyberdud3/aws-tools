import logging
import boto3
from botocore.exceptions import ClientError
import os


# ---------------- CONSTANTS ----------------
AWS_ACCESS = '< Replace with AWS_ACCESS >'
AWS_SECRET = '< Replace with AWS_SECRET >'
BUCKET_NAME = '< Replace with BUCKET_NAME >'


def list_s3_files_using_client(bucket_name: str) -> bool:
    """_summary_: This functions list all files in s3 bucket.

    Args:
        bucket_name (str): Bucket to upload to

    Returns:
        bool: True if file list was available, else False
    """

    s3_client = boto3.client('s3',
        aws_access_key_id = AWS_ACCESS,
        aws_secret_access_key = AWS_SECRET)

    response = s3_client.list_objects_v2(Bucket=bucket_name)
    files = response.get("Contents")
    
    for file in files:
        print(f"file_name: {file['Key']}, size: {file['Size']}")


if __name__ == "__main__":
    list_s3_files_using_client(BUCKET_NAME)
