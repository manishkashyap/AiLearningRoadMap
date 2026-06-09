# How It Works

- URL: https://docs.webengage.com/docs/webhooks
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Webhooks
How It Works
WebEngage webhooks let you add an
HTTP
callback to the events happening in WebEngage. By configuring a webhook, WebEngage is triggered to call a script on your web-servers whenever a particular event, for which you want to get real-time data, occurs and use it for internal purposes. You can use webhooks to send information to systems such as Salesforce. You can also use webhooks to send information to your backend systems. For example, you might want to credit your customers' accounts with promotion credits once they’ve performed a custom event a certain number of times.
Webhook Requests
Webhook requests will be posted to a URL configured by you and in the format described
below
. Webhook request method will always be
POST
. There will be additional parameters that will be appended to the
postURL
.
Request Headers
Name
Description
x-request-id:{HEX_STRING}
Used to identify webhook
POST
requests uniquely to achieve events idempotency. {HEX_STRING} will be replaced by a unique, random hex string.
Request Parameters
Name
Description
eventType
Event for which data is being sent
licenseCode
Your WebEngage account license code
secret
This secret key is to be used to identify the webhook
POST
requests from WebEngage. More about request verification
below
.
Request Body
The
Request body
will contain event-specific data and will vary based on the registered webhook.
Response
WebEngage will understand
HTTP Status
, of the response. Responses with
HTTP Status
200 will be treated as successful posts, everything else will be logged as failed webhook posts.
See the section about
error handling and retries
below to understand what happens in case of failures.
Request Verification
You will find
Webhook Secret Key
for your account in the
Data Platform > Integrations > Webhooks
section of WebEngage dashboard. This secret key is to be used to identify the Webhook
POST
requests from WebEngage to your servers. WebEngage appends a parameter named
secret
in the
postURL
. The value of this parameter is the MD5 Hex of the combination of your WebEngage license code and the Webhook Secret Key separated by
:
.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Multi-Campaign Transaction API & User Profile Upsert
How to Configure
Copy Page
