import json
import base64
from slack import WebClient
from slack.errors import SlackApiError


def notify_slack(data, context):
    ACCESS_TOKEN = 'xxxxxxxxxxxxxxxx'
    CHANNEL_ID = 'xxxxxx'
    client = WebClient(token=ACCESS_TOKEN)

    try:
        notification_data = base64.b64decode(data['data']).decode('utf-8')
        notification_data = json.loads(notification_data)
        budget_notification_text = '予算額：{0} ({1})\n利用料金：{2} ({1})\n利用開始日時：{3}'.format(
            notification_data.get('budgetAmount'),
            notification_data.get('currencyCode'),
            notification_data.get('costAmount'),
            notification_data.get(
                'costIntervalStart'))
        response = client.chat_postMessage(
            channel=CHANNEL_ID,
            text=budget_notification_text)
        assert response['message']['text'] == budget_notification_text

    except SlackApiError as e:
        assert e.response['ok'] is False
        assert e.response['error']
        print(f"Got an error: {e.response['error']}")
