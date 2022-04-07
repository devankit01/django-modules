import logging
import boto3
from botocore.exceptions import ClientError
import os

print(os.path.join(os.path.dirname(__file__)))
def upload_file(file_name, bucket):

    if object_name is None:
        object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True