# How to Configure

- URL: https://docs.webengage.com/docs/webhook-configuration
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Webhooks
How to Configure
You will be able to configure URLs for different events from the
Data Platform > Integrations > Webhooks
section of your WebEngage dashboard. Following are the webhooks you can configure.
Feedback Webhook
Triggers on feedback submission. To add a webhook specific to
FEEDBACK_SUBMIT
event, you need to configure this webhook by specifying the
postURL
and the response format (
XML
JSON
). Feedback data will be the same as that received from
/feedback/<FeedbackId> API call
.
Feedback Reply Webhook
Triggers when a reply is posted to an existing feedback thread. To add a webhook specific to
FEEDBACK_REPLY_SUBMIT
event, you need to configure this webhook by specifying the
postURL
and the response format (
XML
or
JSON
). Feedback reply data will be the same as that received from
/feedback/<FeedbackId>/replies API call
.
Survey Response Webhook
Triggers when survey response is submitted. To add a webhook specific to
SURVEY_RESPONSE_SUBMIT
event, you need to configure this webhook by specifying the
postURL
and the response format (
XML
or
JSON
).
Survey response data will be the same as that received from
/survey/response/<ResponseId> API call
.
Events Webhook
Triggers when the specified event gets logged into the system. To add a webhook specific to an event, you need to configure this webhook by specifying the event's name and the
postURL
. Currently, only
JSON
response format is supported.
Below is an example of how the event data for
push_notification_accepted
event looks like
JSON
{
 "event_data": {
 "result": "SUCCESS"
 },
 "system_data": {
 "variation_id": "1if30if",
 "sdk": "ANDROID",
 "scope": "~7l798ci",
 "id": "20hlgbg",
 "push_notification_content": "{\"identifier\":\"1if30if\",\"experimentId\":\"20hlgbg\",\"packageName\":null,\"title\":\"Master App\",\"message\":\"How are you today ?\",\"image\":null,\"cta\":{\"id\":\"3d7630c9\",\"type\":\"DEEP_LINK\",\"actionLink\":\"webengage://com.webengage.testapp1/start_activity/com.webenagege.testapp1.Activity1\",\"actionText\":null,\"templateId\":null},\"custom\":[{\"key\":\"theKey\",\"value\":\"whatIsKey\"}],\"expandableDetails\":{\"title\":null,\"image\":\"https://webengage.net/wk-test-static-files/~99199077/6313a242-91a5-46b8-96b5-1598365a509a.jpg\",\"message\":null,\"cta1\":null,\"cta2\":null,\"cta3\":null,\"style\":\"BIG_PICTURE\",\"category\":null},\"tokens\":null}"
 },
 "event_time": "2016-06-01T15:53:59+0000",
 "event_name": "push_notification_accepted",
 "license_code": "~99199077",
 "category": "system",
 "user_id": "
[email protected]
",
 "anonymous_id": "0000014a-a2da-cfd3-91c7-0252d7df1a4c"
}
Below is an example of how the event data for
push_notification_rejected
event looks like
JSON
{
 "event_data": {
 "result": "UNAVAILABLE"
 },
 "system_data": {
 "variation_id": "1if30if",
 "sdk": "ANDROID",
 "scope":"~7l799ci",
 "id": "20hlgbg",
 "push_notification_content": "GCM_ERROR"
 },
 "event_time": "2016-06-01T15:53:58+0000",
 "event_name": "push_notification_rejected",
 "license_code": "~99199077",
 "category": "system",
 "user_id": "
[email protected]
",
 "anonymous_id": "0000014a-a2da-cfd3-91c7-0252d7df1a4c"
 }
Activity Events Webhook
If you don’t want to collect data for all the
Custom and Campaign Events
and are looking for a specific set of events, you can specify their name in the
Event Name
box, add the post URL, and click on the Save button.
Here's
a list of all the System Events that are automatically tracked for all your users post-integration.
📘
Please Note
Only one event can be added at a time.
Global System Events Webhook
Used for all the campaign events like
Email Opens
,
Email Clicks
,
Push Notification Impressions
, etc.
The global system events include the campaign events coming from the various channels available on the dashboard. The list of these campaign events is listed at the end.
📘
Please Note
Following system events cannot be passed through Webhook:
App Installed
App Upgraded
App Crashed
App Uninstalled
User Login
User Logout
Session Started
Below is an example of how the event data for
push_notification_accepted
event looks like
JSON
{
 "event_data": {
 "result": "SUCCESS"
 },
 "system_data": {
 "variation_id": "1if30if",
 "sdk": "ANDROID",
 "scope": "~7l798ci",
 "id": "20hlgbg",
 "push_notification_content": "{\"identifier\":\"1if30if\",\"experimentId\":\"20hlgbg\",\"packageName\":null,\"title\":\"Master App\",\"message\":\"How are you today ?\",\"image\":null,\"cta\":{\"id\":\"3d7630c9\",\"type\":\"DEEP_LINK\",\"actionLink\":\"webengage://com.webengage.testapp1/start_activity/com.webenagege.testapp1.Activity1\",\"actionText\":null,\"templateId\":null},\"custom\":[{\"key\":\"theKey\",\"value\":\"whatIsKey\"}],\"expandableDetails\":{\"title\":null,\"image\":\"https://webengage.net/wk-test-static-files/~99199077/6313a242-91a5-46b8-96b5-1598365a509a.jpg\",\"message\":null,\"cta1\":null,\"cta2\":null,\"cta3\":null,\"style\":\"BIG_PICTURE\",\"category\":null},\"tokens\":null}"
 },
 "event_time": "2016-06-01T15:53:59+0000",
 "event_name": "push_notification_accepted",
 "license_code": "~99199077",
 "category": "system",
 "user_id": "
[email protected]
",
 "anonymous_id": "0000014a-a2da-cfd3-91c7-0252d7df1a4c"
}
Below is an example of how the event data for
push_notification_rejected
event looks like
JSON
{
 "event_data": {
 "result": "UNAVAILABLE"
 },
 "system_data": {
 "variation_id": "1if30if",
 "sdk": "ANDROID",
 "scope":"~7l799ci",
 "id": "20hlgbg",
 "push_notification_content": "GCM_ERROR"
 },
 "event_time": "2016-06-01T15:53:58+0000",
 "event_name": "push_notification_rejected",
 "license_code": "~99199077",
 "category": "system",
 "user_id": "
[email protected]
",
 "anonymous_id": "0000014a-a2da-cfd3-91c7-0252d7df1a4c"
 }
Global Application Events Webhook
All the custom events passed to WebEngage Dashboard through
Website, App, and Rest APIs
can be pushed to other third-party tools or systems.
To add a webhook specific to an event, you need to configure this webhook by specifying the event's name and the
postURL
. Currently, only
JSON
response format is supported.
Journey Webhook
Triggers on Journey create, update, publish and delete events. To add a webhook specific to a journey, you need to configure this webhook by specifying the
postURL
. Currently, only
JSON
response format is supported.
Below is an example of how the event data for
journey_activated
event looks like
JSON
{
 "category": "account",
 "resource": "Journey",
 "version": 1,
 "event_name": "journey_activated",
 "event_time": "2017-03-06T11:00:52+0000",
 "license_code": "311c48b3",
 "user_id": "
[email protected]
",
 "event_data": {
 "creationTime": "2017-03-06T11:00:52+0000",
 "createdBy": "
[email protected]
",
 "name": "Repeat Order Journey",
 "id": "abn3jj5",
 "activatedBy": "
[email protected]
",
 "activationTime": "2017-03-06T11:00:52+0000",
 "status": "ACTIVE",
 "tags": ["premium-user"]
 }
}
Please feel free to drop in a few lines at
[email protected]
if you have any further queries. We're always just an email away!
Updated
7 months ago
How It Works
Shopify
Copy Page
