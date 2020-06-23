import json
import base64
import datetime
import dateutil.parser
import slack

BOT_ACCESS_TOKEN = 'xxxx-111111111111-abcdefghidklmnopq'
CHANNEL_ID = 'C0XXXXXX'

slack_client = slack.WebClient(token=BOT_ACCESS_TOKEN)


def notify_slack(data, context):
    try:
        notification_data = base64.b64decode(data['data']).decode('utf-8')
        notification_data = json.loads(notification_data)

        today = datetime.datetime.now().day
        first_day = dateutil.parser.parse(notification_data.get('costIntervalStart')).day
        budgetAmount = notification_data.get('budgetAmount')
        currencyCode = notification_data.get('currencyCode')
        costAmount = notification_data.get('costAmount')
        now_pace = costAmount / int(today - first_day)
        schedule_pace = budgetAmount / 30
        if now_pace > schedule_pace:
            # in English
            budget_notification_text = '<!channel> \nBudget consumption rate is too fast.\n\n'
            budget_notification_text += 'BudgetAmount：' + str(budgetAmount) + ' (' + str(currencyCode) + ')\n'
            budget_notification_text += 'CostAmount：' + str(costAmount) + ' (' + str(currencyCode) + ')\n\n'
            budget_notification_text += 'BudgetAmount per day：' + str(round(schedule_pace)) + ' (' + str(
                currencyCode) + ')\n'
            budget_notification_text += 'CostAmount per day：' + str(round(now_pace)) + ' (' + str(
                currencyCode) + ')\n\n'
            budget_notification_text += 'Please check your GCP'

            # in Japanese
            # budget_notification_text = '<!channel> \n予算に対して、1日の利用料金ペースが上回っています！\n\n'
            # budget_notification_text += '設定している予算額：' + str(budgetAmount) + ' (' + str(currencyCode) + ')\n'
            # budget_notification_text += '現在の消化予算：' + str(costAmount) + ' (' + str(currencyCode) + ')\n\n'
            # budget_notification_text += '1日あたり予定予算：' + str(round(schedule_pace)) + ' (' + str(currencyCode) + ')\n'
            # budget_notification_text += '1日あたり消化予算：' + str(round(now_pace)) + ' (' + str(currencyCode) + ')\n\n'
            # budget_notification_text += '念のため確認しておきましょう！'

            response = slack_client.chat_postMessage(
                channel=CHANNEL_ID,
                text=budget_notification_text)
            assert response['message']['text'] == budget_notification_text

    except slack.errors.SlackApiError as e:
        assert e.response['ok'] is False
        assert e.response['error']
        print(f"Got an error: {e.response['error']}")
