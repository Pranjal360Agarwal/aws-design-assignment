import boto3
import base64

s3 = boto3.client('s3')
BUCKET_NAME = 'your-bucket-name'

def lambda_handler(event, context):
    file_content = base64.b64decode(event['fileContent'])
    file_name = event['fileName']
    
    s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)
    
    return {
        'statusCode': 200,
        'body': f"File {file_name} uploaded successfully to {BUCKET_NAME}"
    }
