import boto3
import json
from botocore.exceptions import NoCredentialsError
from app.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET_NAME # noqa

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)


def upload_student(student_id: str, student_data: dict):
    """Uploads student data to S3"""
    try:
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=f"students/{student_id}.json",
            Body=json.dumps(student_data),
            ContentType="application/json"
        )
        return {"message": "Student data uploaded successfully"}
    except NoCredentialsError:
        return {"error": "Invalid AWS Credentials"}


def get_student(student_id: str):
    """Retrieves student data from S3"""
    try:
        response = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key=f"students/{student_id}.json") # noqa
        student_data = json.loads(response["Body"].read().decode("utf-8"))
        return student_data
    except s3_client.exceptions.NoSuchKey:
        return {"error": "Student not found"}
