# Private SSP

- URL: https://docs.webengage.com/docs/private-ssp
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
SMS
Private SSP
Deliver highly personalized messages to encrypted phone numbers with great ease!
Many businesses are averse to sharing the contact details of their users with third-party platforms like WebEngage.
We understand your concerns.
This is why we've made it possible for you to leverage a user's PII
(Personally Identifiable Information)
for sending SMS campaigns without actually sharing their phone numbers! This can be achieved by setting up a
Private SSP API endpoint
at your end.
Private SSP Basics
A
Private SSP
is an API endpoint that you expose for WebEngage to call. You can think of it as a proxy layer that decrypts the phone numbers of an SMS campaign's target audience before sending it to your SSP for delivery to your users. All you need to do is:
Step 1:
Pass hashed PII data to WebEngage
from your servers.
Step 2:
Set up a Private SSP API endpoint
to decrypt hashed phone numbers.
Step 3:
Connect
Private SSP
with WebEngage
. And add WebEngage Webhook URL to decryption layer to ensure that the delivery status of each message is relayed back from your
SSP --> Decryption Layer --> WebEngage dashboard.
Step 4:
Select
Private SSP
as the preferred
SSP
at
Step 3: Message while creating the SMS campaign.
In doing so, we'll send all the messages to the specified endpoint (where you can decrypt the phone numbers and pass them to your preferred SSP).
The message payload will contain the hashed phone identifiers, message body, and some more associated data.
WebEngage expects a JSON response at that instance denoting synchronous result (request success/failure).
How Private SSP Setup enables you to send SMS campaigns to encrypted phone numbers
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
hashed_phone
must be encrypted in a format that you can decrypt later through the Private SSP.
The encrypted value can be a maximum of 512 characters. Additional characters will be truncated.
Please ensure that the actual phone number is never passed through this method.
🚧
Start Here
Website
Android
iOS
React Native
Cordova/ Phone Gap/ Ionic
Xamarin.Android
Xamarin.iOS
Unity.Android
Unity.iOS
You can also choose to pass and update hashed PII attributes through the
WebEngage REST API
.
Once you've created a decryption layer at your end, you can add it to WebEngage as a
Private SSP.
How to Configure
Now that you're sending us encrypted user data, let's show you how you can leverage it to engage users
(while keeping their identity a top-secret!)
Click to enlarge
As shown above:
Step 1: Select SSP
Access Data Platform> Integrations > SMS Setup.
Select
Private SSP
from the
List of Available SSPs.
In doing so, you will be prompted by a configuration modal.
Step 2: Name your Configuration
Please add a user-friendly name that enables you to identify the right SSP for a campaign
while creating it.
Step 3: Add URL
Add the
Private SSP API endpoint URL
here.
WebEngage makes a
POST
call in JSON to the URL you provide us.
(as shown here)
Response for the message request should be passed in
this predefined format
.
Step 4: Add Custom Headers (Optional):
This could be used for authenticating API requests from WebEngage and passing any other additional user data, as per your business needs.
“Content-Type”: “application/json”
is a default header present in all WebEngage POST requests to the Private SSP and cannot be overridden by you.
A unique ID will always be passed in custom data as
UUID
for each SMS.
Next, click
Save!
Step 5: Add WebEngage Webhook URL to Private SSP
Adding the WebEngage Webhook to your decryption layer will enable us to receive delivery status notifications for each user. This includes
campaign performance indicators
like
message delivered, failed, and queued.
Here's how you can go about it:
Step 5.1.:
As shown below, you will find the integrated
Private SSP
under the section,
Your SMS Service Provider List.
Click to enlarge
Step 5.2.:
Click the overflow menu placed on the extreme right, click
View Webhook URL,
and copy it.
Step 5.3:
Add it to your decryption layer to communicate DSN for each SMS sent to your users.
🚧
About Link Wrapping/Shortening
If your Private SSP is performing additional link wrapping on the links already wrapped by WebEngage (original URL) anywhere in the request payload, then the wrapped domain must ask the caller to follow the original URL-encoded location.
For example, let's assume that the SMS has the following hyperlink:
<a href=“https://google.co.in/?param=%3D%3D%2B%20%20abcd”> Link </a>
We have a parameter named
param
with a value of
==+ abcd
here.
Thus, if you are further wrapping this link, then the wrapped domain must ask the caller to follow the URL-encoded location (
https://google.co.in/?param=%3D%3D%2B%20%20abcd
) and
not
the decoded one (
https://google.co.in/?param===+ abcd
).
Request
Version 1
Version 2
{
 "version": "1.0",
 "smsData" :{
 "toNumber" : "abc12345",
 "fromNumber": "PAXXXN",
 "body" : "Text message"
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "custom": {
 "key1": "val1",
 "key2": "val2"
 },
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id"
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
 "principalEntityId": "abc"
 }
 }
}
Response (Delivery Status Notification)
Here are a few samples of the delivery status notifications (DSN) we expect to receive (in JSON) for each SMS sent to your Private SSP layer from your WebEngage dashboard.
DSN must include the
UUID
passed from WebEngage.
SMS Sent
SMS Rejected 1
SMS Rejected 2
SMS Failed
SMS Accepted
SMS Count
{
 "version": "1.0",
 "messageId" : "webengage-message-id",
 "toNumber" : "abc12345",
 "status" : "sms_sent",
 "statusCode" : 0
}
{
 "status" : "sms_rejected",
 "statusCode" : 2001, // null in case of SMS_SENT
 "message" : "YOUR IP IS NOT WHITELISTED" // null in case of SMS_SENT
}
{
 "status" : "sms_rejected",
 "statusCode" : 2010, // null in case of SMS_SENT
 "message" : "VERSION NOT SUPPORTED",
 "supportedVersion" : "2.0" // mandatory in case of statusCode 2010
}
{
 "version": "1.0",// Mandatory
 "messageId" : "XXXXXXXXXXXX",
 "toNumber" : "abc12345",
 "status" : "sms_failed",
 "statusCode" : 2007, // Mandatory
 "message" : "EXCEEDING MAX LENGTH"
}
{
 "status" : "sms_accepted"
}
{
 "version": "1.0",
 "messageId": "webengage-message-id",
 "toNumber": "919999999999",
 "status": "sms_sent",
 "statusCode": 0,
 //newly added field
 "smsCount":1
}
Let's walk you through each parameter in the above code snippets:
Key
Description
version
This indicates the payload contract of the
request
. If there is any change in the payload structure in future, the version will be updated.
messageId
The unique ID assigned to the message which is used to identify a message uniquely. This is received by the private SSP in the
request body
.
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
contentTemplateId
(specific to Version 2 payload)
Registered Templated ID for your SMS content. Added for version 2 payload and mandatory to sending SMS to Indian consumers
principalEntityId
(specific to Version 2 payload)
Entity unique ID received from DLT after Entity registration is approved. Added for version 2 payload and mandatory to sending SMS to Indian consumers
Delivery Status Codes
WebEngage will respond to the delivery status notification sent by the service provider with an
HTTP 2XX
response code and will enqueue the event to process it. Here's a list of all the response codes for your reference:
Status Code
Description
HTTP Status
0
Success
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
Phone number is registered in a
National DND List
(applicable only if users are located in US, Canada, UK, Australia, Singapore, India)
403
2007
Maximum length of the message body has been exceeded
413
2008
The message has expired (was dropped by SSP from delivery pipeline)
200
2009
The message was not delivered by the mobile network operator.
200
2010
Unsupported payload version
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
To handle the loads with increasing customer base, WebEngage has introduced autoscaling which can occasionally result in higher call rates. WebEngage supports throttling from SSP end to handle such cases. Sending this status code will activate throttling for that request and WebEngage will send that request at later time.
Please Note:
WebEngage will retry sending the message 10 times if this status is received.
Time interval between retries follows binary exponential backoff: 0ms, 200ms, 400ms, 800ms...
429
3000
Recipient Blacklisted
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
We hope this has enabled you to set up a decryption layer for sending SMS campaigns to encrypted phone numbers. Please feel free to drop in a few lines at
[email protected]
in case you have further queries. We're always just an email away!
Updated
6 months ago
2Factor
SMPP
Copy Page
