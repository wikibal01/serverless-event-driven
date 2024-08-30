import boto3
import json
import logging

sns = boto3.client('sns')

def handler(event, context):
    logging.info("Received event: %s", json.dumps(event))
    for alarm in event.get('detail', {}).get('alarmName', []):
        sns.publish(
            TopicArn='arn:aws:sns:us-west-2:123456789012:TheTopic',
            Message=f"Alarm triggered: {alarm}"
        )
        logging.info("Notification sent for alarm: %s", alarm)
