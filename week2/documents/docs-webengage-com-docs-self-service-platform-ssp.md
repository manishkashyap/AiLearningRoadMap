# SMS Service Provider

- URL: https://docs.webengage.com/docs/self-service-platform-ssp
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Service Partner Integration
SMS Service Provider
How an SSP can integrate their platform with the WebEngage Marketing Automation Suite
Adding your SSP to WebEngage enables you to extend your services to over 40,000 global users and makes it easier for your existing clients to start using your services through their WebEngage dashboard.
How to Initiate SSP Integration
We'd love to add you to our Service Partner Network! Please feel free to initiate a conversation by dropping an email at
[email protected]
with the following details:
Service provider's test credentials.
A logo of the service provider with a minimum width of 370 px in PNG/JPEG format.
A static endpoint that listens to incoming
HTTPS
POST
requests and adheres to the specified schema for sending SMS. Note that this needs to be a single static endpoint. If you have multiple such endpoints based on, for example, geography, you will have to accept WebEngage requests on a single endpoint and then route them accordingly.
The request authentication method (Basic authentication or Bearer authentication).
Input fields to be shown to the client on the WebEngage dashboard. For example: API Key or Username and Password.
In the case of API Key, the
POST
request will contain the header
Authorization: Bearer API_KEY
.
In the case of Username and Password, the
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
If your clients will be sending SMS to Indian consumers, kindly let us know so that we enable PEID and TemplateID fields for your configurations and share details accordingly.
Status code
management.
WebEngage comes with three servers: Saudi Arabia, Indian and US servers, and it is necessary that the DSN is configured for both servers.
You can find the DSN tracking link below. The
DSN Token
will be provided once the integration and testing are done by the WebEngage team.
Configuring Delivery Status Notifications
WebEngage provides an endpoint security token for Delivery Status Notifications (DSN) that makes it easier for our clients to track their campaign's performance in their WebEngage dashboard.
What are Delivery Status Notifications?
Delivery Status Notifications are asynchronous updates to messages (for example, SMS Delivered, Bounced, Rejected etc.) that the service provider sends to WebEngage. This is shown in the flowchart below.
WebEngage Support will then process the request if there is a mutual client willing to try out the integration and add the service provider in private beta mode on WebEngage dashboard.
The service provider is required to
POST
Delivery Status Notifications (DSNs) i.e. SMS sent, SMS failed, etc. on the static endpoint.
For US Server
https://st.webengage.com/tracking/events
For IN Server
https://st.in.webengage.com/tracking/events
For KSA Server
https://st.ksa.webengage.com/tracking/events
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
 "version": "1.0",
 "messageId": "webengage-message-id",
 "toNumber": "919999999999",
 "status": "sms_sent",
 "statusCode": 0,
 //newly added field
 "smsCount":1
}
Key
Description
version
This indicates the payload contract of the
request
. If there is any change in the payload structure in future, the version will be updated.
messageId
This is the unique ID assigned to the message which is used to identify a message uniquely.
This is received by the service provider in the
request body
. The length of this string can be up to 500 characters. The
messageId
provided in DSNs must be the same as that received from WebEngage in the request. You must not modify it.
toNumber
The message recipient’s phone number along with country code as prefix.
status
The message status being reported by this DSN. This can be either
sms_sent
or
sms_failed
.
statusCode
Status code of this DSN. This must be one of the status codes described
below
.
smsCount
Number of SMS units consumed for this message. Required for accurate billing and reporting.
WebEngage will respond to the
Delivery Status Notification (DSN)
with an
HTTP 2XX
response code and will enqueue the event to process it.
🚧
Skip to:
List of DSN Status Codes
Testing Integration
You can test your integration using
Postman
. Here's how you can configure the
Postman Test Environment:
Step 1:
Import the
collection of APIs
which will help you test several use-cases.
Step 2:
Configure the Postman environment with your account data.
Environments
are a group of variables & values, that allow you to quickly switch the context for your requests and collections. Here's how you can go about it:
Step 1:
Click on the settings button next to the environment selector dropdown on the top right.
Step 2:
Select
WebEngage SMS SSP Test Environment
. In doing so, you will see the following keys. Edit their values as per your test environment.
a.
test-phone
: Phone number on which you want to receive test messages
b.
sender-id
: Phone number from which you want to send test messages.
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
Step 3:
Once you have set up the environment, you are ready to test your integration. Here's how you can go about it:
Step 1:
Open Postman Collection Runner by clicking on Runner button on the top of Postman window.
Step 2:
Select the Collection with the name
WebEngage SMS SSP Test Suite
and Environment with the name
WebEngage SMS SSP Test Environment
.
Step 3:
Click the
Run
button. Postman will then start testing your APIs and will show you the report.
On completion of the above steps, the service provider will continue to function in private beta mode for mutual clients and will be later made public after ensuring the QoS and functionality tests.
Request
The service provider should accept the following payload as a part of the request to send SMS.
The
Content-Type
header will always be
application/json
.
Version 1
Version 2
{
 "version": "1.0",

 "smsData": {
 "toNumber": "919999999999",
 "fromNumber": "PAXXXN",
 "body": "Text message body"
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id",
 "custom": {
 "key1": "val1",
 "key2": "val2"
 }
 }
}
{
 "version": "2.0",
 "smsData": {
 "toNumber": "919999999999",
 "fromNumber": "PAXXXN",
 "body": "Text message body"
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id",
 "custom": {
 "key1": "val1",
 "key2": "val2"
 },
 "indiaDLT": {
 "contentTemplateId": "xyz",
 "principalEntityId": "abc",
 "telemarketerId": "tm1"
 }
 }
}
Key
Description
version
​
Indicates the payload contract. If there is any change in the payload structure in future, the version will be updated.
campaignType
​
The value this key in the payload can be either
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
toNumber
​
The recipient’s phone number along with country code as prefix.
metadata
This can contain additional fields. Service provider's integration should be able to ignore these additional fields passed as metadata.
contentTemplateId
(specific to Version 2 payload)
Registered Templated ID for your SMS content. Added for version 2 payload and mandatory to sending SMS to Indian consumers
principalEntityId
(specific to Version 2 payload)
Entity unique ID received from DLT after Entity registration is approved. Added for version 2 payload and mandatory to sending SMS to Indian consumers
telemarketerId
(specific to Version 2 payload)
tm1
would be WebEngage's Telemarketer Aggregator ID, which is added by Principal Entity to PE-TM chain binding on DLT portal.
🚧
About Link Wrapping
If you are performing additional link wrapping on the links already wrapped by WebEngage (original URL) anywhere in the request payload, the wrapped domain must ask the caller to follow the original URL-encoded location.
For example, let's assume that the SMS has the following hyperlink:
<a href=“https://google.co.in/?param=%3D%3D%2B%20%20abcd”> Link </a>
We have a parameter named
param
with a value of
==+ abcd
here.
If you are further wrapping this link, then the wrapped domain must ask the caller to follow the URL-encoded location (
https://google.co.in/?param=%3D%3D%2B%20%20abcd
),
not
the decoded one (
https://google.co.in/?param===+ abcd
).
Response
The service provider must synchronously respond with the
appropriate
statusCode
. Also, the message status must be included, whether it is
SUCCESS
or
ERROR
. Refer to the examples below. If there is an asynchronous update to the message later (SMS Delivered, Bounced, Rejected etc.), that should be sent as a
Delivery Status Notification
.
🚧
Skip to:
List of Response Status Codes
Example 1: Message Sent Successfully
HTTP
HTTP 200 OK
{
 "status" : "sms_accepted"
}
Example 2: Message Cannot be Sent
HTTP
HTTP 200 OK
{
 "status": "sms_rejected",
 "statusCode": 2000,
 "message": "Not enough credit to send message"
}
Example 3: Payload Not Acceptable
HTTP
HTTP 400 BAD REQUEST
{
 "status" : "sms_rejected",
 "statusCode" : 2010,
 "message" : "Version not supported",
 "supportedVersion" : "2.0" // Mandatory in case of statusCode 2010
}
Example 3: Payload for Message Failed
HTTP
{
 "version": "1.0",// Mandatory key, value can be 1.0 or 2.0
 "messageId" : "XXXXXXXXXXXX",
 "toNumber" : "abc12345",
 "status" : "sms_failed",
 "statusCode" : 2007, // Mandatory
 "message" : "EXCEEDING MAX LENGTH"
}
Example 4: Message Count
HTTP
{
 "version": "1.0",
 "messageId": "webengage-message-id",
 "toNumber": "919999999999",
 "status": "sms_sent",
 "statusCode": 0,
 //newly added field
 "smsCount":1
}
Status Codes
These status codes are to be used both for
synchronous responses
and
Delivery Status Notifications
. Refer to the
Description
column below for more details about the respective status. Make sure that you send the appropriate HTTP status corresponding to the status codes.
Status Code
Description
HTTP Status
0
To be sent in case of success
200
2000
Insufficient credit balance
200
2001
The IP has not been whitelisted
401
2002
Empty message body
400
2003
Invalid mobile number
400
2004
Invalid Sender ID
400
2005
Authorization failure
403
2006
User under DND
403
2007
Maximum length of the message body has been exceeded
413
2008
The message has been expired
200
2009
The message was not delivered by the operator
200
2010
Payload version unsupported.
In this case the
supportedVersion
is to be sent mandatorily, i.e., the version supported by the service provider. For example:\
HTTP 400 BAD REQUEST
{
 "status" : "sms_rejected",
 "statusCode" : 2010,
 "message" : "Version not supported",
 "supportedVersion" : "2.0"
}
400
2011
Authentication failure
401
2015
Throttling error.
WebEngage uses auto-scaling to handle high traffic, which may occasionally trigger rate limits on your end. For throttled requests, return this status code so WebEngage can recognize the signal and retry delivery at a later time.
Note:
WebEngage will retry sending the message 10 times if this status is received.
Time interval between retries follows binary exponential backoff: 0ms, 200ms, 400ms, 800ms...
429
3000
Recipient Blacklisted
You can choose to blacklist users when:
A user opt-outs of your channel and you'd like to maintain a record for opted-out users with your SSP.
(In addition to maintaining this data with WebEngage)
A user's directly reaches out to your SSP to stop receiving messages from your brand.
403
9988
For outcomes not covered above. Include the appropriate error description in the "message" field of the response
200
India DLT specific Delivery Status Codes
Status Code
Description
HTTP Status
2022
Message blocked by
DLT scrubbing
(applicable only if users are located in India)
Can happen if:
You have not registered your business on a
DLT Portal.
Your PEID & Template ID were not added/ added incorrectly while creating the campaign
403
2023
Timeout while performing
DLT scrubbing
(applicable only if users are located in India)
200
2024
Sender blocked by
DLT scrubbing
(applicable only if users are located in India)
403
2025
Entity blocked by
DLT scrubbing
(applicable only if users are located in India)
403
2026
Template blocked by
DLT scrubbing
(applicable only if users are located in India)
403
2027
Variable length exceeded the max configured length
400
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
4 months ago
Getting Started
Email Service Provider
Copy Page
