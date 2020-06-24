========================================================================
slack-notifications-for-gcp-billing / salckにGCP消化予算を通知する
========================================================================

.. image::https://user-images.githubusercontent.com/21049958/85386606-c7c05980-b57e-11ea-8ae3-d07a06305c72.png


*********************************************
Getting Started / スタートガイド
*********************************************

Prerequisites / 必要条件
====================================
- GCP
  - Google Cloud Billing
  - Google Cloud Pub/Sub
  - Google Cloud Functions
- Python 3.7.2
- Slack bot


Installing / インストール
====================================


1.Setting budget and alerts with Pub/Sub topics in GCP
-------------------------------------------------------------

`GCP billing <https://console.cloud.google.com/billing>`_


2. Creat a slack bot in slack api
-----------------------------------------


1. Access to `Slack API <https://api.slack.com>`_ and creat a bot


2. In "App Home" Add, "App Display Name"

3. In "OAuth & Permissions" > "Scopes" > "Bot Token Scopes", set chat:write "Send messages as ~"

4. "Install App to Workspace"

5. Copy "Bot User OAuth Access Token"


3. Deploy main.py to CloudFunction
-------------------------------------------------------------------------------------------

- Change ACCESS_TOKEN, CHANNEL_ID to yours
- Set cloud Pub/Sub topics as a Trigger

4. Invite bot to a channel
-------------------------------------------------------------------------------------------

5. Testing in cloud functions
-------------------------------------------------------------------------------------------

complete!!


*********************************************
Authors / 著者
*********************************************
`sakimyto <https://twitter.com/sakimyto>`_

*********************************************
License / ライセンス
*********************************************

This is under `MIT license <https://en.wikipedia.org/wiki/MIT_License>`_ .

*********************************************
Acknowledgments / 謝辞
*********************************************

References / 参考・引用文献
====================================

- `Examples of automated cost control responses | Google Cloud <https://cloud.google.com/billing/docs/how-to/notify>`_
- `GCP予算アラートをSlackに通知する | Qiita <https://qiita.com/takezoux2/items/0cff8a2cc4f900cf1d29>`_


