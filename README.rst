==================
My Awesome Project
==================



Install
============


1.Setting budget and alerts with Pub/Sub topics in GCP
-------------------------------------------------------------

https://console.cloud.google.com/billing


2. Creat a slack bot in slack api
-----------------------------------------


1. Access to https://api.slack.com and creat a bot

2. In "App Home" Add, "App Display Name"

3. In "OAuth & Permissions" > "Scopes" > "Bot Token Scopes", set chat:write "Send messages as ~"

4. "Install App to Workspace"

5. Copy "Bot User OAuth Access Token"


3. Deploy main.py to CloudFunction
-------------------------------------------------------------------------------------------

- Change ACCESS_TOKEN, CHANNEL_ID to yours
- Set cloud Pub/Sub topics as a Trigger
