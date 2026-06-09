# Private ESP

- URL: https://docs.webengage.com/docs/private-esp
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
Email
Private ESP
Many businesses are averse to sharing contact details of their users with third-party platforms like WebEngage.
We understand your concerns.
This is why we've made it possible for you to leverage a user's PII (Personally Identifiable Information) for sending Email campaigns without actually sharing their email addresses! This can be achieved by setting up a Private ESP API endpoint at your end.
You can think of Private ESP as a proxy layer that decrypts email addresses of an Email campaign's target audience before sending it to your ESP for delivery to your users. All you need to do is:
Step 1:
Pass hashed PII data to WebEngage
from your servers.
Step 2:
Set up a Private ESP API endpoint
to decrypt hashed email addresses.
Step 3:
Configure
Webhooks
to ensure that the delivery status of each message is relayed back from your
ESP --> Decryption Layer --> WebEngage Dashboard.
Step 4:
Select
Private ESP
as the preferred ESP while creating the
Email campaign.
In doing so, we'll send all the messages to the specified endpoint (where you can decrypt the phone numbers and pass them to your preferred ESP).
How Private ESP Setup enables you to send Email campaigns to encrypted email addresses
PII Hashing
Let's get you acquainted with PII hashing or how you can encrypt a user's phone number and pass it to your WebEngage account.
Which Attributes Are PII?
WebEngage recognizes the user attributes,
phone
and
email
as PII (Personally Identifiable Information). Thus, if you opt for PII hashing, then instead of passing the actual data against these attributes, you will need to pass the corresponding hashes values against the attributes,
hashed_phone
and
hashed_email
.
Passing Hashed PII Values
All WebEngage platform integration SDKs enable you to pass hashed phone numbers and email addresses for each user. Here's an example to help you get started:
JavaScript
Android
iOS
webengage.user.setAttribute({
 'we_hashed_phone': 'e0ec043b3f9e198ec09041687e4d4e8d',
 'we_hashed_email': '144e0424883546e07dcd727057fd3b62'
});
weUser.setHashedEmail(String hashedEmail)

weUser.setHashedPhoneNumber(String hashedPhoneNumber)
-(void) setHashedEmail:(NSString*)hasdhedemail;

-(void) setHashedPhone:(NSString*)hashedphone;
Please Note:
The values passed against
hashed_email
must be encrypted in a format that you can decrypt later through the Private ESP.
The encrypted value can be a maximum of 512 characters. Additional characters will be truncated.
Please ensure that the actual email address is never passed through this method.
🚧
Start Here
Web SDK
Android SDK
iOS SDK
React Native
Cordova/ Phone Gap/ Ionic
Xamarin.Android
Xamarin.iOS
Unity.Android
Unity.iOS
You can also choose to pass and update hashed PII attributes through the
WebEngage REST API
.
Private Email Service Provider
A private ESP is an API endpoint that you expose for WebEngage to call, which acts as a proxy between WebEngage and your actual Email service provider.
WebEngage hits your Private ESP endpoint with a payload containing the hashed email identifiers, the message body, and some other data.
WebEngage expects a JSON response at that instance denoting synchronous result (request success/failure).
WebEngage also subscribes to your Webhooks and expects later hits, passing the subsequent Delivery Status Notifications: delivery (sent, bounced) and interaction (opened, clicked).
Here's how this works:
WebEngage
POST
s to an API endpoint URL you provide us.
You can configure key-value pairs in the headers section in your dashboard to pass custom data with this
POST
request.
a. Some headers cannot be overridden (e.g.
“Content-Type”: “application/json”
).
b. Custom headers can be used for authentication.
A unique ID will always be passed in custom data:
TrackerId
in case of email.
Body of the
POST
request will be in
JSON
format. AMP emails can also be sent, check the Request format in subsequent section.
Response for the message request should be passed in the predefined format shown below.
Webhook settings:
a. URL to be set on your side for real-time delivery reports. This URL can be accessed on WebEngage dashboard under
Data Platform > Integrations > > Email Setup> Channels
in your ESP list as shown below.
Click to enlarge
b. Delivery Status Notification request to be a
POST
(predefined
JSON
format).
c. Delivery Status Notification parameters must include the previously received
TrackerId
.
d.
errorCode
and
errorMessage
parameters and values in case of failure should be passed in the predefined format shown below.
🚧
About Link Wrapping/Shortening
If your Private ESP is performing additional link wrapping on the links already wrapped by WebEngage (original URL) anywhere in the request payload, the wrapped domain must ask the caller to follow the original URL-encoded location.
For example, let's assume that the email contains the following hyperlink:
<a href=“https://google.co.in/?param=%3D%3D%2B%20%20abcd”> Link </a>
We have a parameter named
param
with a value of
==+ abcd
here.
Thus, if you are further wrapping this link, then the wrapped domain must ask the caller to follow the URL-encoded location (
https://google.co.in/?param=%3D%3D%2B%20%20abcd
), and
not
the decoded one (
https://google.co.in/?param===+ abcd
).
Request (JSON)
Non-AMP email
For AMP email
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
 "email": "abc12345" // Actual EmailIds or Encrypted EmailIds
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
 "url": "http://link/to/attachment/1"
 },{
 "name": "Attachment2",
 "url": "http://link/to/attachment/2"
 }]
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "custom": {
 "key1": "val1",
 "key2": "val2"
 },
 "timestamp": 1521012814,
 "messageId": "webengage-message-id"
 },
 "version": "1.0"
}
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
 "amp_html": "amp html body",
 "html": "fallback html body",
 "recipients": {
 "to": [{
 "name": "Recipient1",
 "email": "abc12345" // Actual EmailIds or Encrypted EmailIds
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
 "url": "http://link/to/attachment/1"
 },{
 "name": "Attachment2",
 "url": "http://link/to/attachment/2"
 }]
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "custom": {
 "key1": "val1",
 "key2": "val2"
 },
 "timestamp": 1521012814,
 "messageId": "webengage-message-id"
 },
 "version": "1.0"
}
Response
JSON
JSON
JSON
200 OK
{
 "status": "SUCCESS",
 "statusCode": 1000,
 "message": "NA"
}
200 OK
{
 "status": "ERROR",
 "statusCode": 9002,
 "message": "Daily email sending quota is over."
}
400 Bad Request
{
 "status": "ERROR",
 "statusCode": 9022,
 "message": "Unsupported version",
 "supportedVersion": "2.0" // Mandatory in case of status code 9022
}
Delivery Status Notification
event
in the below payload can be
SPAM
,
DELIVERED
,
BOUNCE
or
UNSUBSCRIBE
.
JSON
{
 "messageId": "webengage-message-id",
 "event": "DELIVERED",
 "timestamp": 1521012814,
 "email": "email-id",
 "hashedEmail": "hashed-email-id",
 "statusCode": 1000, // Status Code (Integer) (Refer table below),
 "message": "NA / Description",
 "version": "1.0"
}
Key
Description
messageId
The unique ID assigned to the message which is used to identify a message uniquely. This is received by private ESP in the
request body
.
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
The time when the event that this DSN represents happened. This is the time since Unix epoch in seconds.
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
Status codes
WebEngage will respond to the delivery status notification sent by the service provider with an
HTTP 2XX
response code and will enqueue the event to process it. Here's a list of all the response codes for your reference:
Status Code
Description
HTTP Status
1000
Success
200
9001
Throttling error.
To handle the loads with increasing customer base, WebEngage has introduced autoscaling which can occasionally result in higher call rates. WebEngage supports throttling from ESP end to handle such cases. Sending this status code will activate throttling for that request and WebEngage will send that request at later time.
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
Unsupported or unknown version (A)
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
9999
Unknown error occurred
200
We hope this has enabled you to set up a decryption layer for sending Email campaigns to encrypted email addresses. Please feel free to drop in a few lines at
[email protected]
in case you have further queries. We're always just an email away!
Updated
7 months ago
SparkPost
SMTP
Copy Page
