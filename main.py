import os
import json
import base64
import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ.get('BOT_ACCESS_TOKEN')
channel_id = os.environ.get('CHANNEL_ID')
slack_client = WebClient(token=slack_token)


def notify_slack(data, ctx):
    try:
        # If you want to easily control the notification time, use datetime.

        # now_hour = datetime.datetime.now().hour
        # if now_hour + 9 == 9:

        notification_data = base64.b64decode(data['data']).decode('utf-8')
        notification_data = json.loads(notification_data)

        budgetAmount = notification_data.get('budgetAmount')
        currencyCode = notification_data.get('currencyCode')
        costAmount = notification_data.get('costAmount')

        budget_notification_text = '設定している予算額：' + str(budgetAmount) + ' (' + str(currencyCode) + ')\n'
        budget_notification_text += '現在の消化予算：' + str(costAmount) + ' (' + str(currencyCode) + ')\n\n'
        budget_notification_text += '詳細内訳レポート\n'
        budget_notification_text += 'https://console.cloud.google.com/billing/xxxxxxxxxx'

        slack_client.chat_postMessage(
            channel=channel_id,
            text=budget_notification_text
        )

    except SlackApiError as e:
        assert e.response['ok'] is False
        assert e.response['error']
        print(f"Got an error: {e.response['error']}")
