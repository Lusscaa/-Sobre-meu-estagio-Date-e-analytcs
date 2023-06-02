import boto3
from botocore.exceptions import ClientError
import os


idpadrao = "AKIAZTNN5SJXGDHX7XNC"
idboladao = "Xk+1Zzj675TwRz4yotlf4KQMT4u52W3uSqYPgTGh"
region_s3 = "us-east-1"


def upload_file(file_name, bucket, folder_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param folder_name: Folder name in the S3 bucket. If not specified, the file will be uploaded to the bucket root.
    :return: True if file was uploaded, else False
    """

    # If folder_name is specified, append it to the object_name
    if folder_name is not None:
        object_name = os.path.join(folder_name, os.path.basename(file_name))
    else:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3', aws_access_key_id=idpadrao, aws_secret_access_key=idboladao, region_name=region_s3)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
upload_file('movies.csv', 'lucasricardo2', 'Raw/Local/CSV/Movies/2023/05/26/')
upload_file('series.csv', 'lucasricardo2', 'Raw/Local/CSV/Series/2023/05/26/')



