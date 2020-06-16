import os
import json
import base64
from slack import WebClient


def notify_slack(data, context):
    ACCESS_TOKEN = 'xxxx-xxxx-xxxx-xxxx'
    CHANNEL_ID = 'xxxxxxxxxxx'

    slack_client = WebClient(token=os.environ[ACCESS_TOKEN])

    notification_data = base64.b64decode(data['data']).decode('utf-8')
    notification_data = json.loads(notification_data)
    budget_notification_text = '予算額：{0} ({1})\n利用料金：{2} ({1})\n利用開始日時：{3}'
    budget_notification_text = budget_notification_text.format(notification_data.get('budgetAmount'),
                                                               notification_data.get('currencyCode'),
                                                               notification_data.get('costAmount'),
                                                               notification_data.get('costIntervalStart'))
    slack_client.chat_postMessage(
        'chat.postMessage',
        channel=CHANNEL_ID,
        text=budget_notification_text)
