
import json
import os
import boto3

print('Loading function')
region_name = os.environ['REGION_NAME']
dynamo = boto3.client('dynamodb')
table_name = os.environ['TABLE_NAME']

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))

    scan_result = dynamo.scan(TableName=table_name)
    print("Scan successful.")
    print(scan_result)
    #print(json.dumps(scan_result, indent=2))
    return respond(None, res=scan_result)