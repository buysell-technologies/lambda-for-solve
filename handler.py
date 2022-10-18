import os
import json
from slack_bolt import App

SLACK_BOT_TOKEN=os.getenv('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET=os.getenv('SLACK_SIGNING_SECRET')

app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)

def hello(event, context):
    print(app)
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
