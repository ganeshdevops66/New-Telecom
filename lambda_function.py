import json
import boto3
import os
import uuid

s3 = boto3.client('s3')

BUCKET = os.environ['BUCKET']

def lambda_handler(event, context):
    print("Event Received:", event)

    for record in event['Records']:
        body = json.loads(record['body'])

        file_name = f"telecom_{uuid.uuid4()}.json"

        s3.put_object(
            Bucket=BUCKET,
            Key=file_name,
            Body=json.dumps(body)
        )

        print(f"Stored in S3: {file_name}")

    return {
        "statusCode": 200,
        "body": "Success"
    }
