import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('the_table')

def handler(event, context):
    try:
        response = table.get_item(
            Key={
                'id': event['pathParameters']['id']
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps(response.get('Item', {}))
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
