# Email Service Provider

- URL: https://docs.webengage.com/docs/self-service-platform-esp
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Service Partner Integration
Email Service Provider
How an Email Service Provider can integrate its platform with WebEngage
Adding your ESP to WebEngage enables you to extend your services to over 40,000 global users and makes it easier for your existing clients to start using your services through their WebEngage dashboard.
How to Initiate ESP Integration
We'd love to add you to our Service Partner Network! Please feel free to initiate a conversation by dropping an email at
[email protected]
with the following details:
Service provider's test credentials.
A logo of the service provider with a minimum width of 370 px in PNG/JPEG format.
A static endpoint which listens to incoming
HTTPS
POST
requests and adheres to the specified schema for sending email.
Please note that this needs to be a single static endpoint. If you have multiple such endpoints based on, for example, geography, you will have to accept WebEngage requests on a single endpoint and then route them accordingly.
The request authentication method (Basic authentication or Bearer authentication).
Input fields to be shown to the client on WebEngage dashboard. For example: API Key or Username and Password.
In case of API Key, the
POST
request will contain the header
Authorization: Bearer API_KEY
.
In case of Username and Password, the
POST
request will contain the header
Authorization: Basic BASE_64(USERNAME:PASSWORD)
.
For example, if your username is 'webengage' and password is 'admin' then the Authorization header will be
Basic d2ViZW5nYWdlOmFkbWlu
. The string
d2ViZW5nYWdlOmFkbWlu
is the Base64 encoded version of the string
webengage:admin
.
Configuring Delivery Status Notifications
WebEngage provides endpoint security token for Delivery Status Notifications (DSN) that makes it easier for our clients to track their campaign's performance in their WebEngage dashboard.
What are Delivery Status Notifications?
Delivery Status Notifications are asynchronous updates to messages (for example, Email Delivered, Bounced etc.) that the service provider sends to WebEngage. This is shown in the flowchart below.
Click to enlarge
WebEngage Support will process the request if there is a mutual client willing to try out the integration and add the service provider in private beta mode on WebEngage dashboard.
The service provider is required to
POST
Delivery Status Notifications (DSNs) i.e. Email Delivered, Bounced etc. on the static endpoint
https://et.webengage.com/tracking/events
The service provider will be provided with a security token which needs to be included as a Authorization header in the
POST
request of DSNs.
For example:
Authorization: Bearer <Security Token>
. This token will remain the same and should not be shared to ensure security. In case there is a need to change the token, the service provider should reach out to WebEngage Support to get a new token.
Please follow the below format for the
POST
body for DSN:
JSON
{
 "messageId": "webengage-message-id",
 "event": "DELIVERED",
 "timestamp": "2018-01-25T10:24:16+0000",
 "email": "email-id",
 "hashedEmail": "hashed-email-id",
 "statusCode": 1000,,
 "message": "Success",
 "version": "1.0"
}
Key
Description
messageId
This is the unique ID assigned to the message which is used to identify a message uniquely.
This is received by the service provider in the
request body
. The length of this string can be up to 500 characters. The
messageId
provided in DSNs must be the same as that received from WebEngage in the request. You must not modify it.
event
The event being reported by this DSN. This can be one of
SENT
,
DELIVERED
,
BOUNCE
or
UNSUBSCRIBE
.
timestamp
The time when the event that this DSN represents happened. This follows the ISO date format:
yyyy-MM-ddTHH:mm:ss±hhmm
.
email
Email ID of the user for whom this event has happened. Note that either one of
email
or
hashedEmail
is mandatory.
hashedEmail
Hashed email ID of the user for whom this event has happened. Note that either one of
email
or
hashedEmail
is mandatory.
statusCode
Status code of this DSN. This must be one of the status codes described
below
.
message
Use this to describe the status of the DSN.
version
This indicates the payload contract of the
request
. If there is any change in the payload structure in future, the version will be updated.
WebEngage will respond to the
Delivery Status Notification
with an
HTTP 2XX
response code and will enqueue the event to process it.
🚧
Skip to:
List of DNS Status Codes
Testing Integration
You can test your integration using
Postman
. Here's how you can configure the
Postman Test Environment:
Step 1:
Click the button below to import a collection of APIs which will help you test several use-cases.
►
Run in Postman
Step 2:
Configure the Postman environment with your account data.
Environments
are a group of variables & values, that allow you to quickly switch the context for your requests and collections. Here's how you can go about it:
Step 1:
Click on the settings button next to the environment selector dropdown on the top right.
Step 2:
Select
WebEngage Email ESP Test Environment
. In doing so, you will see the following keys. Edit their values as per your test environment.
a.
to-email
: Email ID on which you want to receive test emails.
b.
from-email
: Email ID from which you want to send test emails.
c.
api-end-point
: API endpoint of your integration
d.
username
: Username of your Basic Auth. Leave the value as it is if you're using Bearer Auth.
e.
password
: Password of your Basic Auth. Leave the value as it is if you're using Bearer Auth.
f.
api-key
: API key (token) for Bearer Auth. Leave the value as it is if you're using Basic Auth.
g.
authorization
: Leave as it is.
h.
message-id
: Leave as it is.
Step 3:
Once you have set up the environment, you are ready to test your integration. Here's how you can go about it:
Open Postman Collection Runner by clicking on Runner button on the top of Postman window.
Select the Collection with the name
WebEngage Email ESP Test Suite
and Environment with the name
WebEngage Email ESP Test Environment
.
Click the
Run
button. Postman will then start testing your APIs and will show you the report.
On completion of the above steps, the service provider will continue to function in private beta mode for mutual clients and will be later made public after ensuring the QoS and functionality tests.
Request
The service provider should accept the following payload as a part of the request to send Email.
The
Content-Type
header will always be
application/json
.
Non-AMP Email
AMP Email
{
 "email": {
 "from": "
[email protected]
",
 "fromName": "John Doe",
 "replyTo": [
 "
[email protected]
",
 "
[email protected]
"
 ],
 "subject": "email subject",
 "text": "text body",
 "html": "html body",
 "recipients": {
 "to": [{
 "name": "Recipient1",
 "email": "abc12345"
 }, {
 "name": "Recipient2",
 "email": "
[email protected]
"
 }],
 "cc": [
 "
[email protected]
",
 "
[email protected]
"
 ],
 "bcc": [
 "
[email protected]
",
 "
[email protected]
"
 ]
 },
 "attachments": [{
 "name": "Attachment1",
 "url": "https://link/to/attachment/1"
 },{
 "name": "Attachment2",
 "url": "http://link/to/attachment/2"
 }]
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id",
 "custom" : {
 "key1" : "val1",
 "key2" : "val2"
 }
 },
 "version": "1.0"
}
{
 "email":
 {
 "from": "
[email protected]
",
 "fromName": "John Doe",
 "replyTo":
 [
 "
[email protected]
",
 "
[email protected]
"
 ],
 "subject": "email subject",
 "amp_html": "amp html body",
 "html": "fallback html body",
 "recipients":
 {
 "to":
 [
 {
 "name": "Recipient1",
 "email": "abc12345"
 },
 {
 "name": "Recipient2",
 "email": "
[email protected]
"
 }
 ],
 "cc":
 [
 "
[email protected]
",
 "
[email protected]
"
 ],
 "bcc":
 [
 "
[email protected]
",
 "
[email protected]
"
 ]
 },
 "attachments":
 [
 {
 "name": "Attachment1",
 "url": "https://link/to/attachment/1"
 },
 {
 "name": "Attachment2",
 "url": "http://link/to/attachment/2"
 }
 ]
 },
 "metadata":
 {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id",
 "custom":
 {
 "key1": "val1",
 "key2": "val2"
 }
 },
 "version": "2.0"
}
Key
Description
version
Indicates the payload contract. If there is any change in the payload structure in future, the
version
will be updated.
campaignType
The value of this key can be either
PROMOTIONAL
or
TRANSACTIONAL
as selected by the user creating campaign on WebEngage dashboard.
messageId
Unique ID assigned to the message which should be used in further Delivery Status Notifications to identify a message uniquely.
timestamp
The time when the message was triggered from the WebEngage system. This follows the ISO date format:
yyyy-MM-ddTHH:mm:ss±hhmm
.
metadata
This can contain additional fields. Service provider's integration should be able to ignore these additional fields passed as metadata.
🚧
About Link Wrapping
If you are performing additional link wrapping on links already wrapped by WebEngage (original URL) anywhere in the request payload, the wrapped domain must ask the caller to follow the original URL-encoded location.
For example, let's assume that the email body has the following hyperlink:
https://google.co.in/?param=%3D%3D%2B%20%20abcd
We have a parameter named param with a value of
==+abcd
here.
If you are further wrapping this link, then the wrapped domain must ask the caller to follow the URL-encoded location
(https://google.co.in/?param=%3D%3D%2B%20%20abcd)
and not the decoded one
(https://google.co.in/?param===+ abcd)
Response
The service provider must synchronously respond with the
appropriate
statusCode
. Also, the message status must be included, whether it is
SUCCESS
or
ERROR
. Refer to the examples below. If there is an asynchronous update to the message later (Email Delivered, Bounced, Rejected etc.), that should be sent as a
Delivery Status Notification
.
🚧
Skip to:
List of Response Status Codes
Example 1: Message sent successfully
HTTP
HTTP 200 OK
{
 "status": "SUCCESS",
 "statusCode": 1000,
 "message": "NA"
}
Example 2: Message cannot be sent
HTTP
HTTP 200 OK
{
 "status": "ERROR",
 "statusCode": 9002,
 "message": "Daily email sending quota is over."
}
Example 3: Payload not acceptable
HTTP
HTTP 400 BAD REQUEST
{
 "status": "ERROR",
 "statusCode": 9022,
 "message": "Unsupported version",
 "supportedVersion": "2.0" // Mandatory in case of status code 9022
}
Status Codes
These status codes are to be used both for
synchronous responses
and
Delivery Status Notifications
. Please ensure that the HTTP status and status codes are mapped correctly at your end to avoid any confusion.
Status Code
Description
HTTP Status
1000
Success
200
9001
Throttling error.
WebEngage uses auto-scaling to handle high traffic, which may occasionally trigger rate limits on your end. For throttled requests, return this status code so WebEngage can recognize the signal and retry delivery at a later time.
Note:
WebEngage will retry sending the message 10 times if this status is received.
Time interval between retries follows binary exponential backoff: 0ms, 200ms, 400ms, 800ms...
429
9002
Message sending quota exceeded
200
9003
Authentication failure
403
9004
Recipient address not specified
400
9005
From field missing
400
9006
Soft bounce (temporarily deferred)
200
9007
Hard bounce
200
9008
Email reported as spam
200
9009
Email unsubscribed
200
9010
Email in suppression list
200
9011
Sender address not verified
400
9012
ESP rejected message
200
9013
Request to ESP expired
200
9014
ESP unavailable
500
9015
IP not whitelisted with ESP
401
9016
Subject field empty
400
9017
Invalid sender address
400
9018
Invalid email address
400
9019
Recipient’s mail box is full
200
9020
Error processing email at Private ESP
500
9021
Mailbox was not found on email server
200
9022
Unsupported or unknown version
In this case the
supportedVersion
is to be sent mandatorily, i.e., the version supported by the service provider. For example:\
HTTP 400 BAD REQUEST
{
 "status": "ERROR",
 "statusCode": 9022,
 "message": "Unsupported version",
 "supportedVersion": "2.0"
}
400
9024
Authorization failure
403
9452
Message overloading
200
9512
Host email server not found
200
9988
Unknown error occurred
200
Please feel free to drop in a few lines at
[
[email protected]
](mailto:
[email protected]
)
in case you have any further queries. We're always just an email away!
Updated
4 months ago
SMS Service Provider
WhatsApp Service Provider
Copy Page
