# Private RSP

- URL: https://docs.webengage.com/docs/private-rsp
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Private RSP
Private RCS Service Provider Basics
A private RSP is an API endpoint that you expose for WebEngage to call, that acts as a proxy between WebEngage and your actual RCS service provider.
WebEngage hits your Private RSP endpoint with a payload containing the phone identifiers, the message body and some other data.
WebEngage expects a JSON response at that instance denoting synchronous result (request success / failure).
WebEngage also subscribes to your Webhooks and expects later hits, passing the subsequent Delivery Status Notifications (DSNs): delivery (delivered, read or failed).
Here's how this works:
WebEngage
POSTs
to an API endpoint URL you provide us.
A unique ID
UUID
will always be passed in
messageId
in the payload to uniquely identify RCS message.
Body of the
POST
request will be in
JSON
format.
Synchronous response for the message request should be passed in the predefined format shown in following step.
You can configure Private RSP on WebEngage dashboard with following data:
Property
Remark
Mandatory
Configuration Name
Name for your configuration
Yes
Business Number
Business number for sending message
Yes
URL
Private RSP API Endpoint
Yes
Request Type
This dropdown list contains two properties, please choose accordingly:
Send personalization variables
- If you want to accept list of string values of template variables (in sequence) from WebEngage instead of entire generalized message
Yes
Custom Headers
If you want to pass custom data (key-value pair in headers), you can configure Custom Headers. It can be used to pass Authorization Headers.
Note: WebEngage will put
ContentType:
application/json
as default header in POST Request to Private RSP API. Putting Custom Headers will not override the default header.
No
SECTION 1: The flow of message will be as follows:
WebEngage will send message to you, and you will reply synchronously to the message received with respective
Status Codes
given in the last section of this documentation.
You will also reply back to WebEngage webhook (i.e. static endpoint which can be found on WebEngage dashboard following:
Integrations > Channels > RCS > ACTIONS (RSP) > View Webhook URL.
for delivery report (i.e. Delivery Status Notification (DSN)) asynchronously.
1. WebEngage RCS Request to you
As depicted in SECTION 1 point 1, WebEngage will send RCS message to you in the following given payload format and you will reply synchronously to the message with
Status Codes
provided in the last section of this documentation.
Key points for API request from WebEngage to you:
At the time of adding configuration for your Private RSP (Request Type property), WebEngage allows you to accept
parameters
in the payload request from WebEngage.
parameters
is a map of key - value pair of template variables provided by user as per template.
e.g. if the template is:
hello {{1}}, welcome to new {{2}}
and template variables i.e.
{{1}}
and
{{2}}
are
john
and
world
, then the parameters will be:
{"key1":"john", "key2":"world"}
.
templateData
provided in given below payload will only contain parameters as per your choice.
The
Content-Type
header will always be
application/json
. We’ll also provide support for adding custom headers (specific to individual you) while user creates your Private RSP configuration on WebEngage dashboard.
Request format of payload for Text/ Rich Card/ Rich Carousel from WebEngage to you
JSON
{
 "version": "1.0",
 "rcsData": {
 "toNumber": "+919999999999",
 "sender": "<senderId>",
 "templateData": {
 "templateName": "templateName",
 "parameters": {
 "paramkey1": "paramValue1",
 "paramkey2": "paramValue2"
 }
 },
 "customData": {
 "customkey1": "customValue1",
 "customkey2": "customValue2"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timeStamp": "2024-12-20T12:00:21+0000",
 "messageId": "<messageId>"
 }
}
Key
Description
version
Indicates the payload contract. If there is any change in the payload structure in future, the version will be updated.
toNumber
The recipient’s phone number along with country code as prefix.
sender
The RCS SenderID you are using to send the campaign.
templateName
Name of template used
parameters
Template variables with the exact name and sequence as added in dashboard.
language
Message template language supported by RCS
timestamp
The time when the message was triggered from the WebEngage system. This follows the ISO date format:
yyyy-MM-ddTHH:mm:ss±hhmm
.
messageId
Unique ID assigned to the message which should be used in further Delivery Status Notifications to identify a message uniquely.
campaignType
PROMOTIONAL
customData
In this section , you can pass extra data (in Key-value pair format from the dashboard) in the payload. This is mainly used by partners if they require some custom integrations to be done for their internal systems or for particular clients.
Example curl request with
parameters
and headers provided by you:
cURL
curl --location --request POST '<PRIVATE-RSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "rcsData": {
 "toNumber": "+919999999999",
 "sender": "<senderId>",
 "templateData": {
 "templateName": "templateName",
 "parameters": {
 "paramkey1": "paramValue1",
 "paramkey2": "paramValue2"
 }
 },
 "customData": {
 "customkey1": "customValue1",
 "customkey2": "customValue2"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timeStamp": "2024-12-20T12:00:21+0000",
 "messageId": "<messageId>"
 }
}'
Examples for synchronous response for above payloads by you to WebEngage:
Example 1: Message Accepted Successfully
JSON
HTTP 200 OK
{
 "status" : "rcs_accepted",
 "statusCode": 0
}
Example 2: Message Cannot be Sent further
NOTE: If the status code is not
0
, send
message
property too.
JSON
HTTP 200 OK
{
 "status": "rcs_rejected",
 "statusCode": 2000,
 "message": "Not enough credit to send message"
}
Example 3: Payload Not Acceptable
NOTE: In case there is mismatch in payload version of API contract (current is 1.0).
JSON
HTTP 400 BAD REQUEST
{
 "status" : "rcs_rejected",
 "statusCode" : 2010,
 "message" : "Version not supported",
 "supportedVersion" : "1.0" // Mandatory in case of statusCode 2010
}
2. Delivery Status Notification (DSN) by you to WebEngage
Delivery report of each message forwarded by you to WebEngage is called as Delivery Status Notification (DSN). It helps our clients to track their campaign's performance in their WebEngage dashboard.
As depicted in SECTION 1 point 2, DSNs are asynchronous updates to messages (e.g. RCS message delivered, expired, rejected etc.) that you sends to WebEngage webhook.
Key points for DSN by you to WebEngage:
You are required to
POST
DSN i.e. RCS message sent, failed, etc. on the static endpoint which can be found on WebEngage dashboard following:
Integrations > Channels > RCS > ACTIONS (RSP) > View Webhook URL
.
You will be provided with:
Auth token
- which needs to be included as an Authorization header in the POST request of DSNs.
e.g.
Authorization: Bearer <Auth token>
. This token will remain the same and should not be shared to ensure security. In case there is a need to change the token, You should reach out to WebEngage Support to get a new token.
Content-Type
Header for the DSN request should be
application/json
.
WebEngage will respond to the DSN request with an
HTTP 2XX
response code.
Request format of DSN payload by you to WebEngage
JSON
{
 "version": "1.0",
 "messageId" : "webengage-message-id",
 "toNumber" : "+919999999999",
 "sender" : "<senderId>",
 "status": "rcs_delivered",
 "statusCode" : 0,
 "reason": "Success",
 "timestamp": "2024-08-12T14:57:16+0000"
}
Key
Description
version
This indicates the payload contract of the request. If there is any change in the payload structure in future, the version will be updated.
messageId
This is the unique ID assigned to the message which is used to identify a message uniquely.
This is received by the service provider in the request body. The length of this string can be up to 500 characters. The
messageId
provided in DSNs must be the same as that received from WebEngage in the request. You must not modify it.
toNumber
The message recipient’s phone number along with country code as prefix.
sender
The RCS SenderID you are using to send the campaign.
status
The message status being reported by this DSN. This can be either
rcs_delivered
,
rcs_failed
or
rcs_read
.
statusCode
Status code of this DSN. This must be one of the status codes described below.
reason
It is an optional field (must be given when
statusCode
doesn’t fulfill failed reason, or when
statusCode
is 9988).
timestamp
The time when the message was triggered from the WebEngage system. This follows the ISO date format:
yyyy-MM-ddTHH:mm:ss±hhmm.
Example curl request of
DSN
with Auth token for authentication as header:
JSON
curl --location --request POST '<STATIC-DSN-END-POINT-OF-WEBENGAGE>' \
--header 'Authorization: Bearer <AUTH-TOKEN-PROVIDED-BY-WEBENGAGE>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "messageId": "webengage-message-id",
 "toNumber": "+919999999999",
 "sender": "<senderId>",
 "status": "rcs_delivered",
 "statusCode": 0,
 "reason": "sent successfully to user",
 "timestamp": "2018-01-25T10:24:16+0000"
}'
Status Codes
These status codes are to be used both for synchronous responses and Delivery Status Notifications. Refer to the Description column below for more details about the respective status. Make sure that you send the appropriate HTTP status corresponding to the status codes.
Status Code
Description
HTTP Status
0
To be sent in case of success
200
1000
Insufficient credit balance
200
1001
Number is RCS Disabled
200
1002
Entity was not found
401
1003
Template code with bot doesn’t exist
400
9988
For outcomes not covered, include the appropriate error description in the "message" field of the response
400
2019
Credit Insufficient
400
2020
Message Empty
403
2021
Mobile Number Invalid
200
2022
Sender Id is Invalid
413
2005
Authorization failure
401
2006
Exceeding max length
200
2007
Expired
400
2008
Undelivered
401
2009
Version Unsupported
200
2017
Invalid Message Format
429
2011
Others
200
2012
DND Time
400
2013
Maximum Retries Exhausted
400
2014
Rate Limit Exceeded
400
2015
TTL Expired
200
2016
Retries Expired
200
2023
Template Missing
200
2024
Template Paramenter Format Mismatch
200
2025
User not Opted in or Inactive
200
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
6 months ago
Getting Started
Copy Page
