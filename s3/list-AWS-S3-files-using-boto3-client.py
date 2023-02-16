import os
import time
import boto3
from botocore.exceptions import ClientError

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
log_format = '%(asctime)s | %(levelname)s: %(message)s'
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)


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

    file_list_status = {
        "success": False,
        "msg": '',
        "data": ''
    }

    s3_client = boto3.client('s3',
        aws_access_key_id = AWS_ACCESS,
        aws_secret_access_key = AWS_SECRET)

    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        files = response.get("Contents")

        file_list_status["success"] = True
        file_list_status["msg"] = f"SUCCESS: list all files in s3 bucket - {bucket_name}"
        file_list_status["data"] = files

    except ClientError as e:
        logging.error(e)
        file_list_status["msg"] = f"FAIL: list all files in s3 bucket - {bucket_name}"
    
    finally:
        return file_list_status


if __name__ == "__main__":

    begin = time.time()
    
    file_list_status = list_s3_files_using_client(BUCKET_NAME)
    
    if not file_list_status["success"]:
        logger.error(file_list_status["msg"])

    else:
        logger.info(file_list_status["msg"])

        files = file_list_status["data"]
        for file in files:
            logger.info(f"file_name: {file['Key']}, size: {file['Size']}")

    logger.info(f"SUCCESS: list all files in s3 bucket - {BUCKET_NAME} - COMPLETED in {time.time()-begin} seconds.")
