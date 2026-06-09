# Private WSP

- URL: https://docs.webengage.com/docs/private-wsp
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
WhatsApp
Private WSP
Deliver highly personalize WhatsApp messages to encrypted phone numbers with great ease!
Many businesses are averse to sharing the contact details of their users with third-party platforms like WebEngage.
We understand your concerns.
This is why, we've made it possible for you to leverage a user's
PII (Personally Identifiable Information)
for sending WhatsApp campaigns without actually sharing their phone numbers! This can be achieved by setting up a
Private WSP API
endpoint at your end.
Private WhatsApp Service Provider Basics
You can think of Private WSP as a proxy layer that decrypts phone numbers of a WhatsApp campaign's target audience before sending it to your WSP for delivery to your users. All you need to do is:
Step 1:
Pass hashed PII data to WebEngage
from your servers.
Step 2:
Set up a
Private WSP API
endpoint to decrypt hashed phone numbers and
integrate with WebEngage
.
Step 3:
Configure
Webhooks
to ensure that the delivery status notifications
(Sent, Delivered, Read, Failed)
are relayed for each message from your
WSP --> Decryption Layer --> WebEngage dashboard.
Step 4:
Select
Private WSP
as the preferred WSP while creating the WhatsApp campaign.
PII Hashing
At WebEngage, we refer to
User Attributes
such as
phone
and
email
as
PII (Personally Identifiable Information)
, which can be encrypted to safeguard your user's privacy.
Thus, the term
PII Hashing
refers to the encryption of these details. If you opt to do so, then instead of passing actual data against the attributes mentioned above, you will need to pass the hashed values against the attributes,
hashed_phone
and
hashed_email
, respectively.
Passing Hashed PII Values
All our platform integration SDKs enable you to pass hashed phone numbers and email addresses for each user. Here are a few examples to help you get started:
Website
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
Start Here!
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
How to Configure Private WSP
Now that you're sending us encrypted user data, let's show you how you can leverage it to engage users
(while keeping their identity a top-secret!)
Click to enlarge
As shown above:
Step 1: Access
Integrations > Channels > WhatsApp
Click on
Add WhatsApp Service Provider
to get started.
In doing so, you will be prompted by a pop-up. Click the first dropdown and select Private WSP.
Step 2: Add Business Number
Add the registered phone number through which users will receive your WhatsApp messages.
(
Here are a few best practices to help you get started
.)
Step 3: Add URL
As shown above, Add the endpoint URL of your Private WSP layer.
Each time you launch a campaign, where Private WSP is selected as the preferred WSP, we will
POST
an API call to this URL in
JSON
.
Step 4: Specify Request Type
Before configuring this field, please check with your WSP about the type of data they are willing to ingest from your Private WSP endpoint. While some WSPs prefer to ingest the entire message (containing the whitelisted template's text and values of personalization variables) in the message payload, others prefer to receive only the personalization tokens.
Click to enlarge
As shown above:
Select
Send Entire Message
to pass the template's text and personalization variables from WebEngage to your Private WSP layer.
(Sample Request Payload)
Select
Send Personalization Variables
to pass only values of the personalization variables from WebEngage to your Private WSP layer.
This way, your WSP will populate the selected message template (that has been whitelisted by them) with only the personalization variables for each user before delivery.
(Sample Request Payload)
👍
Understanding Request Type
For example, let's assume that your template is:
Hey
{{1}}
, we're delighted to have you aboard! Here's your code,
{{2}}
to help you get started!
Where,
Variable
{{1}}
= Name
Variable
{{2}}
= Unique Password
Then the WhatsApp message received by the user, Sophie would be:
Hey
Sophie
, we're delighted to have you aboard! Here's your code,
Sph512X
to help you get started!
Thus, if you've selected
Send Entire Message
against
Request Type
, then you will receive the above message in the payload.
However, if you select
Send Personalization Variables
against
Request Type
, then you will receive only values of the template variables - [
Sophie
,
Sph512X
] in the message payload.
Step 5 (Optional): Add Custom Headers
Click to enlarge
You can choose to pass custom data as key-value pairs by adding them here in
JSON
. This field can also be used to pass
Authorization Headers.
Click
Add Headers
to continue adding custom data.
Click
Add WSP
to save the details.
Step 6: Add WebEngage Webhook URL to Private WSP
Adding the WebEngage Webhook to your decryption layer will enable us to receive
Delivery Status Notifications (DSNs)
for each user. This includes
campaign performance indicators
like
message delivered, failed, and queued.
Here's how you can go about it:
Click to enlarge
Step 6.1.:
As shown above, you will find the integrated
Private WSP
under the section,
Your WhatsApp Service Provider List.
Click the
Actions overflow menu
on the right-side.
Step 6.2:
Click
View Webhook URL.
In doing so, a pop-up containing the static endpoint URL will appear on the screen.
Copy the URL and configure it as the WebEngage endpoint for sending
POST API response containing the DSN
.
Step 6.3:
Request your Onboarding Manager for a security token (Auth Token/ API Key). This must be added to your DSN request as an authorization header, for example:
Authorization: Bearer <Security Token>
. You can also drop in a message at
[email protected]
to get your
Auth Token.
(How it works)
👍
Congratulations!
You have successfully integrated your Private WSP with WebEngage.
You can test the integration by creating a campaign targeting opted-in internal users (aka your teammates) to ensure everything's running smoothly.
Request
🚧
About Link Wrapping/Shortening in Message
If your Private WSP is performing additional link wrapping on the links already wrapped by WebEngage (original URL) anywhere in the request payload, then the wrapped domain must ask the caller to follow the original URL-encoded location.
For example, let's assume that the message has the following hyperlink:
<a href=“https://google.co.in/?param=%3D%3D%2B%20%20abcd”> Link </a>
We have a parameter named
param
with a value of
==+ abcd
here.
Thus, if you are further wrapping this link, then the wrapped domain must ask the caller to follow the URL-encoded location
(https://google.co.in/?param=%3D%3D%2B%20%20abcd)
, and
not
the decoded one
(https://google.co.in/?param===+ abcd)
.
Sample POST Request
Here's a sample code snippet to help you understand the format in which you will receive the payload from WebEngage:
Text
Video
Image
Document
Location
Carousel
{
"version": "1.0",
"whatsAppData": {
 "toNumber": "91902867XXXX",
 "fromNumber": "91334180XXXX",
 "templateData": {
 "templateName": "templatexyz",
 "templateVariables": [
"test" ],
 "language": "en",
 "type": "TEXT",
 "buttonUrlParam": "test", // In the case of dynamic CallToAction
 "buttonUrlDynamicParam": "test", // In the case of two dynamic CallToAction
 "copyCodeText": "TESTCODE", // In the case of copy offer code button
 },
 "customData": {
 "key": "value"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2024-07-03T05:13:15+0000",
 "messageId": "ed70a6d4-431c-4d18-a062-a4d0a6c68153"
 }
}
{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "91902867XXXX",
 "fromNumber": "91334180XXXX",
 "templateData": {
 "templateName": "templatexyzVIDEO",
 "message": "hello john, welcome to new world",
 "templateVariables": ["john", "world"],
 "type" : "VIDEO",
 "mediaUrl":"https://www.webenagege.com/webengage-logo.png",
 "buttonUrlParam": "test", // In the case of dynamic CallToAction
 "buttonUrlDynamicParam": "test", // In the case of two dynamic CallToAction
 "copyCodeText": "TESTCODE", // In the case of copy offer code button
 "language": "en"
 },
 "customData": {
 "key1": "value1",
 "key": "value"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id"
 }
}
{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "91902867XXXX",
 "fromNumber": "91334180XXXX",
 "templateData": {
 "templateName": "templatexyzIMAGE",
 "message": "hello john, welcome to new world",
 "templateVariables": ["john", "world"],
 "type" : "IMAGE",
 "mediaUrl":"https://www.webenagege.com/webengage-logo.png",
 "buttonUrlParam": "test", // In the case of dynamic CallToAction
 "buttonUrlDynamicParam": "test", // In the case of two dynamic CallToAction
 "copyCodeText": "TESTCODE", // In the case of copy offer code button
 "language": "en"
 },
 "customData": {
 "key1": "value1",
 "key": "value"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id"
 }
}
{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "91902867XXXX",
 "fromNumber": "91334180XXXX",
 "templateData": {
 "templateName": "templatexyzDOC",
 "message": "hello john, welcome to new world",
 "templateVariables": ["john", "world"],
 "type" : "DOCUMENT",
 "mediaUrl":"https://www.webenagege.com/webengage-logo.png",
 "fileName": "<file-name if added>",
 "buttonUrlParam": "test", // In the case of dynamic CallToAction
 "buttonUrlDynamicParam": "test", // In the case of two dynamic CallToAction
 "copyCodeText": "TESTCODE", // In the case of copy offer code button
 "language": "en"
 },
 "customData": {
 "key1": "value1",
 "key": "value"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id"
 }
}
{ 
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "91902867XXXX",
 "fromNumber": "91334180XXXX",
 "templateData": {
 "templateName": "templatexyzDOC",
 "message": "hello john, welcome to new world",
 "templateVariables": ["john", "world"],
 "type" : "LOCATION",
 "longitude":15.946519,
 "latitude":45.946519,
 "locationName":"Name of the location", 
 "locationAddress":"Address",
 "buttonUrlParam": "test", // In the case of dynamic CallToAction
 "buttonUrlDynamicParam": "test", // In the case of two dynamic CallToAction
 "copyCodeText": "TESTCODE", // In the case of copy offer code button
 "language": "en"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id"
 }
}
{
"version": "1.0",
"whatsAppData": {
 "toNumber": "919028670XXXX",
 "fromNumber": "91334180XXXX",
 "templateData": {
 "templateName": "carousel cards image",
 "templateVariables": ["john"],
 "language": "en",
 "type": "CAROUSEL",
 "carousel": {
"cards": [ {
 "header": {
 "type": "IMAGE/VIDEO",
 "mediaUrl": "mediaurl"
 },
 "placeholders": ["test"],
 "buttonUrlParam": "test"// In the case of dynamic CallToAction 
 },
 {
 "header": {
 "type": "IMAGE/VIDEO",
 "mediaUrl": "mediaurl2"
 },
 "placeholders": ["test"],
 "buttonUrlParam": "test"// In the case of dynamic CallToAction 
 }
 ] }
 },
 "customData": {
 "key": "value"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2024-07-03T05:17:21+0000",
 "messageId": "75200558-d23b-49a9-886e-cf0a8d8d6a5e"
} }
Location:
<PRIVATE-WSP-API-END-POINT>
will be replaced with the
URL provided during configuration
.
Headers:
WebEngage will add
“Content-Type”: “application/json”
by default as a header in the
POST
call. All other
custom headers specified during configuration
will also be included here.
Let's break down each parameter included in the
whatsAppData
container:
Key
What It Means
version
Indicates the payload contract. If there is any change in the payload structure in future, the version will be updated.
toNumber
The recipient’s encoded phone number along with prefixed country code.
fromNumber
The WhatsApp Business Number you are using to send the campaign.
templateName
Name of the whitelisted template being used by you.
message
Indicates the exact message that needs to be delivered to a user (as per the template and template variables populated at
Step 3: Message
while creating the WhatsApp campaign).
This key is included in the payload only if you select
Send Entire Message against Request Type
during configuration.
templateVariables
Indicates string values of all personalization variables, in the exact sequence, as per the template selected at Step 3: Message while creating the WhatsApp campaign.
This key is included in the payload only if you select
Send Personalization Variables against Request Type
during configuration.
language
Indicates the language in which the WhatsApp Message template was created in WebEngage.
buttonUrlParam
Indicates the Dynamic call to Action placeholder value
This key is included in the payload only if Dynamic CTA buttons are added in the WhatsApp template
buttonUrlDynamicParam
Indicates second Dynamic call to Action placeholder value
This key is included in the payload only if 2 Dynamic CTA buttons are added in the WhatsApp template
type
Indicates the WhatsApp media template type
This key is included in the payload only for media templates:
TEXT, VIDEO, IMAGE, DOCUMENT, LOCATION
,
CAROUSEL
mediaUrl
Resource URL link which is to be sent
This key is included for
VIDEO, IMAGE, DOCUMENT
,
CAROUSEL
media templates
customData
(Optional)
In this section , you can pass extra data (in Key-value pair format from the dashboard) in the payload.
This is mainly used by partners if they require some custom integrations to be done for their internal systems or for particular clients.
longitude
Longitude value
This key is included for
LOCATION
template only
latitude
Latitude value
This key is included for
LOCATION
template only
locationName
Name of the location
This key is included for
LOCATION
template only
locationAddress
Address of the location
This key is included for
LOCATION
template only
Here's what each parameter included in the
metadata
container denotes:
Key
What It Means
campaignType
The value of this key can be either
PROMOTIONAL
or
TRANSACTIONAL
, as selected at
Step 1: Audience
while creating the WhatsApp campaign in your dashboard.
timestamp
Indicates the time at which the message was sent from WebEngage to your Private SSP. It follows the ISO date format:
yyyy-MM-ddTHH:mm:ss±hhmm
.
messageId
A unique ID assigned to each message sent from your campaign. Please ensure that this ID is specified in each
Delivery Status Notification sent in Response
from your Private WSP.
Request Containing Only Personalization Variables in Payload
Here's a sample
cURL
POST API request sent from WebEngage to your
Private WSP
for
Request Type: Send Personalization Variables
.
Text
Video
Image
Document
Location
Carousel
curl --location --request POST '<WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "919999999999",
 "fromNumber": "44000000099",
 "templateData": {
 "templateName": "templatexyz",
 "templateVariables": ["john", "world"],
 "type" : "TEXT",
 "buttonUrlParam" : "XYZ.pdf", // In the case of dynamic CallToAction 
 "language": "en"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id"
 }
}
curl --location --request POST '<WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "919999999999",
 "fromNumber": "44000000099",
 "templateData": {
 "templateName": "templatexyzVIDEO",
 "templateVariables": ["john", "world"],
 "type" : "VIDEO",
 "mediaUrl":"https://www.webenagege.com/webengage-logo.png",
 "buttonUrlParam" : "XYZ.pdf", // In the case of dynamic CallToAction
 "language": "en"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id"
 }
}
curl --location --request POST '<WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "919999999999",
 "fromNumber": "44000000099",
 "templateData": {
 "templateName": "templatexyzIMAGE",
 "templateVariables": ["john", "world"],
 "type" : "IMAGE",
 "mediaUrl":"https://www.webenagege.com/webengage-logo.png",
 "buttonUrlParam" : "XYZ.pdf", // In the case of dynamic CallToAction
 "language": "en"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id"
 }
}
curl --location --request POST '<WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "919999999999",
 "fromNumber": "44000000099",
 "templateData": {
 "templateName": "templatexyzDOC",
 "templateVariables": ["john", "world"],
 "type" : "DOCUMENT",
 "mediaUrl":"https://www.webenagege.com/webengage-logo.png",
 "fileName": "<file-name if added>",
 "buttonUrlParam" : "XYZ.pdf", // In the case of dynamic CallToAction
 "language": "en"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id"
 }
}
curl --location --request POST '<WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{ 
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "919999999999",
 "fromNumber": "44000000099",
 "templateData": {
 "templateName": "templatexyzDOC",
 "templateVariables": ["john", "world"],
 "type" : "LOCATION",
 "longitude":15.946519,
 "latitude":45.946519,
 "locationName":"Name of the location", 
 "locationAddress":"Address",
 "buttonUrlParam" : "XYZ.pdf", // In the case of dynamic CallToAction
 "language": "en"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2018-01-25T10:24:16+0000",
 "messageId": "webengage-message-id"
 }
}
{
"version": "1.0",
"whatsAppData": {
 "toNumber": "919028670XXXX",
 "fromNumber": "91334180XXXX",
 "templateData": {
 "templateName": "carousel cards image",
 "templateVariables": ["john"],
 "language": "en",
 "type": "CAROUSEL",
 "carousel": {
"cards": [ {
 "header": {
 "type": "IMAGE/VIDEO",
 "mediaUrl": "mediaurl"
 },
 "placeholders": ["test"],
 "buttonUrlParam": "XYZ.pdf"// In the case of dynamic CallToAction 
 },
 {
 "header": {
 "type": "IMAGE/VIDEO",
 "mediaUrl": "mediaurl2"
 },
 "placeholders": ["test"],
 "buttonUrlParam": "XYZ.pdf"// In the case of dynamic CallToAction 
 }
 ] }
 },
 "customData": {
 "key": "value"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2024-07-03T05:17:21+0000",
 "messageId": "75200558-d23b-49a9-886e-cf0a8d8d6a5e"
} }
Request Containing Entire Message in Payload
Here's a sample
cURL
POST API request sent from WebEngage to your
Private WSP
for
Request Type: Send Entire Message
.
Text
Video
Image
Document
Location
Carousel
curl --location --request POST '<WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "+919999999999",
 "fromNumber": "99999999999",
 "templateData": {
 "templateName": "text_template",
 "message": "hello john, welcome to new world",
 "header": "Header",
 "footer": "Footer",
 "language": "en",
 "type": "TEXT",
 "buttonUrlParam": "/home",
 "copyCodeText": "1234",
 "buttons": [
 {
 "templateButtonType": "CALL_TO_ACTION",
 "buttons": [
 {
 "templateButtonActionType": "VISIT_WEBSITE",
 "buttonText": "Visit Website",
 "templateButtonUrlType": "STATIC"
 },
 {
 "templateButtonActionType": "VISIT_WEBSITE",
 "buttonText": "Check blog",
 "templateButtonUrlType": "DYNAMIC",
 "buttonUrlContent": "/home"
 },
 {
 "templateButtonActionType": "CALL_PHONE_NUMBER",
 "buttonText": "Call Us"
 },
 {
 "templateButtonActionType": "COPY_CODE",
 "buttonText": "copy code",
 "copyCodeText": "1234"
 }
 ]
 },
 {
 "templateButtonType": "QUICK_REPLY",
 "buttons": [
 {
 "buttonText": "Yes"
 },
 {
 "buttonText": "No"
 },
 {
 "buttonText": "May be"
 }
 ]
 }
 ]
 },
 "customData": {
 "key1": "value1",
 "key2": "value2"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2025-01-28T08:42:22+0000",
 "messageId": "d9672b7d-a20f-48ee-a0bc-c9ef532b318b"
 }
}
curl --location --request POST '<WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "+919999999999",
 "fromNumber": "99999999999",
 "templateData": {
 "templateName": "Video_template",
 "message": "hello john, welcome to new world",
 "header": "",
 "footer": "Footer",
 "language": "en",
 "type": "VIDEO",
 "mediaUrl": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
 "buttonUrlParam": "www.google.com",
 "buttons": [
 {
 "templateButtonType": "QUICK_REPLY",
 "buttons": [
 {
 "buttonText": "Yes"
 },
 {
 "buttonText": "No"
 }
 ]
 },
 {
 "templateButtonType": "CALL_TO_ACTION",
 "buttons": [
 {
 "templateButtonActionType": "CALL_PHONE_NUMBER",
 "buttonText": "Call Us"
 },
 {
 "templateButtonActionType": "VISIT_WEBSITE",
 "buttonText": "Visit Website",
 "templateButtonUrlType": "DYNAMIC",
 "buttonUrlContent": "www.google.com"
 }
 ]
 }
 ]
 },
 "customData": {
 "key1": "value1",
 "key2": "value2"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2025-01-28T10:30:17+0000",
 "messageId": "99df3b19-4d23-4944-a688-6bc616f43c3c"
 }
}
curl --location --request POST '<WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "+919999999999",
 "fromNumber": "99999999999",
 "templateData": {
 "templateName": "image_template",
 "message": "hello john, welcome to new world",
 "header": "",
 "footer": "Footer",
 "language": "en",
 "type": "IMAGE",
 "mediaUrl": "https://afiles.webengage.com/aa131d2c/f181dbb6-7aa1-4924-94dd-416d09eb425e.jpg",
 "buttons": [
 {
 "templateButtonType": "CALL_TO_ACTION",
 "buttons": [
 {
 "templateButtonActionType": "VISIT_WEBSITE",
 "buttonText": "Visit Website",
 "templateButtonUrlType": "STATIC"
 }
 ]
 },
 {
 "templateButtonType": "QUICK_REPLY",
 "buttons": [
 {
 "buttonText": "Interested"
 },
 {
 "buttonText": "Not Interested"
 }
 ]
 }
 ]
 },
 "customData": {
 "key1": "value1",
 "key2": "value2"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2025-01-28T14:54:22+0000",
 "messageId": "5d49d79a-c154-42e6-bf63-1f78abad7561"
 }
}
curl --location --request POST '<PRIVATE-WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "+919999999999",
 "fromNumber": "99999999999",
 "templateData": {
 "templateName": "document_template",
 "message": "hello john, welcome to new world",
 "header": "",
 "footer": "Footer",
 "language": "en",
 "type": "DOCUMENT",
 "mediaUrl": "https://afiles.webengage.com/aa131d2c/a53c8262-63ea-46f8-892e-0273ce18554a.pdf",
 "fileName": "Itinerary",
 "buttons": [
 {
 "templateButtonType": "QUICK_REPLY",
 "buttons": [
 {
 "buttonText": "Get More Details"
 },
 {
 "buttonText": "Not Interested"
 }
 ]
 },
 {
 "templateButtonType": "CALL_TO_ACTION",
 "buttons": [
 {
 "templateButtonActionType": "CALL_PHONE_NUMBER",
 "buttonText": "Call Us"
 }
 ]
 }
 ]
 },
 "customData": {
 "key1": "value1",
 "key2": "value2"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2025-01-28T15:08:22+0000",
 "messageId": "ee558056-2bd8-4e1b-9d0a-09211b2f0193"
 }
}
curl --location --request POST '<WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "+919999999999",
 "fromNumber": "99999999999",
 "templateData": {
 "templateName": "location_template",
 "message": "hello john, welcome to new world",
 "header": "",
 "footer": "",
 "language": "en",
 "type": "LOCATION",
 "latitude": "45.946519",
 "longitude": "15.946519",
 "locationName": "Name of the location",
 "locationAddress": "Address",
 "copyCodeText": "123456",
 "buttons": [
 {
 "templateButtonType": "CALL_TO_ACTION",
 "buttons": [
 {
 "templateButtonActionType": "COPY_CODE",
 "buttonText": "copy code",
 "copyCodeText": "123456"
 }
 ]
 },
 {
 "templateButtonType": "QUICK_REPLY",
 "buttons": [
 {
 "buttonText": "Yes"
 },
 {
 "buttonText": "No"
 }
 ]
 }
 ]
 },
 "customData": {
 "key1": "value1",
 "key2": "value2"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2025-01-28T15:16:21+0000",
 "messageId": "4427f430-7ad1-459b-a29c-c1c8e645b5f2"
 }
}
curl --location --request POST '<WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "+919999999999",
 "fromNumber": "99999999999",
 "templateData": {
 "templateName": "carousel_template",
 "message": "hello john, welcome to new world",
 "header": "",
 "language": "en",
 "type": "CAROUSEL",
 "carousel": {
 "cards": [
 {
 "header": {
 "type": "IMAGE",
 "mediaUrl": "https://i.pinimg.com/236x/11/dc/9a/11dc9ae1696e7843d998f6f3e10a9125.jpg"
 },
 "message": "hello john, This is Card 1 text",
 "placeholders": [],
 "buttonUrlParam": "jMro3y",
 "buttons": [
 {
 "templateButtonType": "CALL_TO_ACTION",
 "buttons": [
 {
 "templateButtonActionType": "VISIT_WEBSITE",
 "buttonText": "Visit Website",
 "templateButtonUrlType": "DYNAMIC",
 "buttonUrlContent": "jMro3y"
 },
 {
 "templateButtonActionType": "CALL_PHONE_NUMBER",
 "buttonText": "Call Us"
 }
 ]
 }
 ]
 },
 {
 "header": {
 "type": "IMAGE",
 "mediaUrl": "https://afiles.webengage.com/aa131d2c/47891647-c5b3-4943-a5de-023ddf54666d.png"
 },
 "message": "hello john, This is Card 2 text",
 "placeholders": [],
 "buttons": [
 {
 "templateButtonType": "CALL_TO_ACTION",
 "buttons": [
 {
 "templateButtonActionType": "VISIT_WEBSITE",
 "buttonText": "Visit Website",
 "templateButtonUrlType": "STATIC"
 },
 {
 "templateButtonActionType": "CALL_PHONE_NUMBER",
 "buttonText": "Call Us"
 }
 ]
 }
 ]
 },
 {
 "header": {
 "type": "IMAGE",
 "mediaUrl": "https://afiles.webengage.com/aa131d2c/4444723b-591e-4659-ac8a-484b19a83fea.jpg"
 },
 "message": "hello john, This is Card 3 text",
 "placeholders": [],
 "buttonUrlParam": "category/blogid",
 "buttons": [
 {
 "templateButtonType": "CALL_TO_ACTION",
 "buttons": [
 {
 "templateButtonActionType": "VISIT_WEBSITE",
 "buttonText": "Check Blog",
 "templateButtonUrlType": "DYNAMIC",
 "buttonUrlContent": "category/blogid"
 },
 {
 "templateButtonActionType": "CALL_PHONE_NUMBER",
 "buttonText": "Contact Us"
 }
 ]
 }
 ]
 }
 ]
 }
 },
 "customData": {
 "key1": "value1",
 "key2": "value2"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2025-01-28T15:33:21+0000",
 "messageId": "04ac98c7-0214-4a30-b010-d4959e97282e"
 }
}
Request Containing Key-Value Pairs in Payload
🚧
Must Read
Leveraging Key-Value Pairs to Send Additional User Data to Your Servers & Personalize User Experience
You can choose to pass additional data in the message payload to your
Private WSP
by adding
Key-Value Pairs at Step 3: Message,
while creating the
WhatsApp campaign.
This comes in handy when for various custom requirements, for example: passing specific user data to your servers through Key-Value pairs like promo code/ offer type included in WhatsApp message, user type, details of the product purchased, and so on.
As shown below, all
Keys
and their corresponding
Values
are included in the
customdata
container in the message payload sent from WebEngage.
Sample API Request containing Key-Value Pairs as Custom data
curl --location --request POST '<PRIVATE-WSP-API-END-POINT>' \
--header '<HEADERS-PROVIDED-BY-YOU-IN-CONFIGURATION>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "whatsAppData": {
 "toNumber": "+919167714989",
 "fromNumber": "9167714989",
 "templateData": {
 "templateName": "Hello Test",
 "message": "This is a test template",
 "language": "en",
 "type": "TEXT"
 },
 "customData": {
 "Key 1": "Value 1",
 "Key2": "Value 2",
 "Name": "Rajesh"
 }
 },
 "metadata": {
 "campaignType": "PROMOTIONAL",
 "timestamp": "2020-11-20T10:52:57+0000",
 "messageId": "c5d5457e-6c43-41a0-8f02-35d6957d92a0"
 }
}'
🚧
Please Note
All personalization variables are supported in
customdata
.
While you can add links in
customdata
, link wrapping is not supported. Thus, clicks will not be tracked in your dashboard for links specified in Key-Value pairs.
Response (Delivery Status Notification)
For each message forwarded to your
Private WSP
, we expect a response containing a
Delivery Status Notification (DSN).
These are asynchronous updates
like
message delivered, expired, rejected
and so on. It enables you to analyze your campaign's performance against several
performance indicators
in your dashboard.
DSNs
can be sent as
POST
API requests to the
WebEngage Webhook URL added to your Private WSP during configuration
.
Here's a sample DSN response containing the unique Auth Token provided specifically for DSN authorization by the WebEngage support team:
Sample DSN Response with Auth Token
curl --location --request POST '<STATIC-DSN-END-POINT-OF-WEBENGAGE>' \
--header 'Authorization: Bearer <AUTH-TOKEN-PROVIDED-BY-WEBENGAGE>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "messageId" : "webengage-message-id",
 "toNumber" : "ENCODEDXYZ123PHONENUMBER",
 "status": "whatsapp_sent",
 "statusCode" : 0,
 "reason": "sent successfully to user",
 "timestamp": "2018-01-25T10:24:16+0000"
}'
DSN parameters must include the
messageId
previously passed in
metadata
so that we're able to map it to a specific message.
WebEngage will respond to the API call with an HTTP 2XX response code and will enqueue the event to process it.
Here's what each parameter in the above code snippet denotes:
Key
What It Means
version
This indicates the payload contract of the request. If there is any change in the payload structure in future, the version will be updated.
messageId
This is the unique ID assigned to the message which is used to identify a message uniquely.
This is received by the service provider in the request body. The length of this string can be up to 500 characters. The
messageId
provided in DSNs must be the same as that received from WebEngage in the request. You must not modify it.
toNumber
The message recipient’s phone number along with prefixed country code.
status
The message status being reported by this DSN. This can be either
whatsapp_sent,whatsapp_failed
or
whatsapp_read
.
statusCode
Status code of this DSN. This must be one of the
status codes listed here
.
reason
It is an optional field (must be given when
statusCode
doesn’t fulfill failed reason, or when
statusCode
is 9988).
timestamp
The time when the message was triggered from the WebEngage system. This follows the ISO date format:
yyyy-MM-ddTHH:mm:ss±hhmm.
Synchronous Response Examples
Example 1: Message Accepted Successfully
JSON
HTTP 200 OK
{
 "status" : "whatsapp_accepted",
 "statusCode": 0
}
Example 2: Message Cannot Be Sent Further
NOTE: If the status code is not 0, then please send the message property too.
JSON
HTTP 200 OK
{
 "status": "whatsapp_rejected",
 "statusCode": 2000,
 "message": "Not enough credit to send message"
}
Example 3: Payload Not Acceptable
The following snippet depicts a scenario where there is a mismatch in the payload version of the API contract (currently we're using v1.0).
JSON
HTTP 400 BAD REQUEST
{
 "status" : "whatsapp_rejected",
 "statusCode" : 2010,
 "message" : "Version not supported",
 "supportedVersion" : "2.0" // Mandatory in case of statusCode 2010
}
Status Codes
These status codes are to be used for both, synchronous responses and asynchronous
Delivery Status Notifications (DSNs).
Please ensure that you send the appropriate HTTP status corresponding to the status codes.
Status Code
Description
HTTP Status
0
Message delivery is successful!
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
Invalid Business Number
400
2005
Authorization failure
403
2006
User blocked the Business Number
200
2007
Maximum length of the message body has been exceeded
413
2008
The message has expired
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
Authentication failure (e.g. mobile number might be unverified)
401
2014
Maximum number of retries to send the message have been exhausted.
200
2015
Throttling error.
To handle the loads with an increasing customer base, WebEngage has introduced autoscaling which can occasionally result in higher call rates. WebEngage supports throttling from the WSP's end to handle such cases. Sending this status code will activate throttling for that request and WebEngage will send that request at a later time.
Note:
WebEngage will retry sending the message 10 times if this status is received.
The time intervals between retries would be in the following order (in mins): 3 + 6 + 9 + 12 + 15 + 15 + 15 + 15 + 15
429
2019
The message format is invalid
400
2021
Template Missing
400
2022
Template Parameter Format Mismatch
400
2023
Template did not match
400
2024
User isn't opted in for template message
200
2025
User is not Opted in and is inactive
200
2026
Meta Frequency Cap
9988
For outcomes not covered above. Include the appropriate error description in the "message" field of the response
200
We hope this has enabled you to set up a decryption layer for sending WhatsApp campaigns to encrypted phone numbers. Please feel free to drop in a few lines at
[email protected]
in case you have further queries. We're always just an email away!
Updated
1 day ago
TrustSignal
RCS
Copy Page
