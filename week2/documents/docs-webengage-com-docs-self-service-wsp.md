# WhatsApp Service Provider

- URL: https://docs.webengage.com/docs/self-service-wsp
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Service Partner Integration
WhatsApp Service Provider
Welcome to WebEngage's Developer Hub!
Adding your WhatsApp Service Provider (WSP) to WebEngage enables you to extend your services to over 40,000 global users and makes it easier for your existing clients to start using your services through their WebEngage dashboard.
How to Initiate WSP Integration
We'd love to add you to our Service Partner Network! Please feel free to initiate a conversation by dropping an email at
[email protected]
with the following details:
Your test credentials. For example, you could share a username-password OR API Key and an API endpoint where we can
POST
requests.
A logo of the service provider with a minimum width of 370 px in PNG/JPEG format.
A static endpoint URL that listens to incoming HTTPS
POST
requests and adheres to the specified schema for sending WhatsApp messages.
Please note that this needs to be a single static endpoint. If you have multiple endpoints dedicated to various geographies and so on, then you will need to accept WebEngage requests on a single endpoint and route them accordingly for delivery.
The request authentication method (Basic authentication or Bearer authentication).
Input fields to be shown to the client on WebEngage dashboard. For example: API Key or Username and Password.
In case of API Key, the
POST
request will contain the header
Authorization: Bearer API_KEY
.
In case of Username and Password, the POST request will contain the header
Authorization: Basic BASE_64(USERNAME:PASSWORD)
.
For example, if your username is 'webengage' and password is 'admin' then the Authorization header will be
Basic d2ViZW5nYWdlOmFkbWlu
. The string d2ViZW5nYWdlOmFkbWlu is the Base64 encoded version of the string
webengage:admin
.
WebEngage comes with three servers: Indian, Saudi Arabia and US servers, and it is necessary that the DSN is configured for both servers.
You can find the DSN tracking link
below
. The DSN Token will be provided once the integration and testing are done by the WebEngage team.
Our support team will process your request if a mutual client agrees to test your WSP in private beta mode on our dashboard before we make it available for all our clients.
Section 1: The flow of the message will be as follows:
WebEngage will send message to the WhatsApp Service Provider (WSP) and WSP will reply synchronously to the message received with respective Status Codes given in the last section of this documentation.
WSP will reply back to WebEngage webhook (i.e. static endpoint which can be found on WebEngage dashboard following:
Data Platform > Integrations > WhatsApp Setup (Configure) > ACTIONS (WSP) > View Webhook URL
.) for the delivery report (i.e. Delivery Status Notification (DSN)) asynchronously.
1. WebEngage WhatsApp Request to WSP
As depicted in SECTION 1 point 1, WebEngage will send WhatsApp messages to
WSP
in the following given payload format and WSP needs to reply synchronously to the message with Status Codes provided in the last section of this documentation.
Key points for API request from WebEngage to WSP:
At the time of integration, WebEngage allows WSP to either accept message or templateVariables in the payload request from WebEngage to WSP. templateVariables is a list of string of template variables provided by user as per template and message is the actual generalization of the user’s template with the given template variables.
e.g. if the template is: hello {{1}}, welcome to new {{2}} and template variables i.e. {{1}} and {{2}} are john and world, then the actual generalized message will be: hello john, welcome to the new world and templateVariables will be: ["john", "world"].
templateData
provided in the given below payload will only contain either message or
templateVariables
as per WSP’s choice at the time of integration. WSP will never receive both messages as well as
templateVariables
.
The
Content-Type
header will always be application/json. We’ll also provide support for adding custom headers (specific to individual WSP) while the user creates WhatsApp WSP configuration on WebEngage dashboard.
In case of Carousel only one dynamic url button is allowed, also copy code is not applicable currently and no change in the payload for buttons like Quick Reply, Phone number, Static Url button.
Please note entire message will not be sent from our end this needs to be handled by WSPs.
Request format of payload from WebEngage to WSP
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
Key
Description
version
Indicates the payload contract. If there is any change in the payload structure in future, the version will be updated.
toNumber
The recipient’s encoded phone number along with prefixed country code.
fromNumber
The WhatsApp Business Number you are using to send the campaign.
templateName
Name of the whitelisted template being used by you.
message
message to be delivered to user (generalised message as per template and template variables). It will be provided if you accept this in place of templateVariables.
templateVariables
List of string values of template variables in exact sequence as per template. It will be provided if you accept this in place of message
This key is included in the payload only if you select
Send Personalization Variables against Request Type
during configuration.
language
Message template language supported by WhatsApp
buttonUrlParam
Indicates the Dynamic call to Action placeholder value
This key is included in the payload only if Dynamic CTA buttons are added in the WhatsApp template
buttonUrlDynamicParam
Indicates second Dynamic call to Action placeholder value
This key is included in the payload only if 2 Dynamic CTA buttons are added in the WhatsApp template
copyCodeText
Indicates copy offer code call to Action placeholder value
This key is included in the payload only if copy offer code buttons are added in the WhatsApp template
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
Keys
Description
campaignType
The value this key in the payload can be either PROMOTIONAL or TRANSACTIONAL as selected by the user creating campaign on WebEngage dashboard.
timestamp
The time when the message was triggered from the WebEngage system. This follows the ISO date format: yyyy-MM-ddTHH:mm:ss±hhmm.
messageId
Unique ID assigned to the message which should be used in further Delivery Status Notifications to identify a message uniquely.
Example curl Request for Request Type: Send Personalization Variables
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
 "header": "",
 "footer": "",
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
Example curl Request for Request Type: Send Entire Message
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
 "buttonUrlContent": "home/orderid"
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
 "buttonUrlContent": "https://www.google.com"
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
curl --location --request POST '<WSP-API-END-POINT>' \
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
Examples for synchronous response for above payloads from WSP to WebEngage:
Example 1: Message Accepted Successfully
JSON
HTTP 200 OK
{
 "status" : "whatsapp_accepted",
 "statusCode": 0
}
Example 2: Message Cannot be Sent further
NOTE: If the status code is not 0, send message property too.
JSON
HTTP 200 OK
{
 "status": "whatsapp_rejected",
 "statusCode": 2000,
 "message": "Not enough credit to send message"
}
Example 3: Payload Not Acceptable
NOTE: In case there is mismatch in payload version of API contract (current is 1.0).
JSON
HTTP 400 BAD REQUEST
{
 "status" : "whatsapp_rejected",
 "statusCode" : 2010,
 "message" : "Version not supported",
 "supportedVersion" : "2.0" // Mandatory in case of statusCode 2010
}
2. Delivery Status Notification (DSN) from WSP to WebEngage
Delivery report of each message forwarded by WSP to WebEngage is called as Delivery Status Notification (DSN). It helps our clients to track their campaign's performance in their WebEngage dashboard.
As depicted in SECTION 1 point 2, DSNs are asynchronous updates to messages (e.g. WhatsApp message delivered, expired, rejected etc.) that WSP sends to WebEngage webhook.
Key points for DSN from WSP to WebEngage:
WSP is required to
POST DSN
i.e. WhatsApp message sent, failed, etc. on the static endpoint which can be found on WebEngage dashboard following:
Data Platform > Integrations > WhatsApp Setup (Configure) > ACTIONS (WSP) > View Webhook URL
.
WebEngage comes with three servers: Saudi Arabia, India and US servers, and it is necessary that the DSN is configured for all servers.
You can find the DSN tracking link below. The DSN Token will be provided once the integration and testing are done by the WebEngage team.
The service provider is required to
POST Delivery Status Notifications (DSNs)
i.e. WhatsApp Message sent, failed, etc. on the static endpoint.
For US Server
<https://wt.webengage.com/tracking/events>
For IN Server
<https://wt.in.webengage.com/tracking/events>
For KSA Server
<https://wt.ksa.webengage.com/tracking/events>
WSP will be provided with:
Auth token - which needs to be included as an Authorization header in the POST request of DSNs.
e.g. Authorization: Bearer
<Auth token>
. This token will remain the same and should not be shared to ensure security. In case there is a need to change the token, WSP should reach out to WebEngage Support to get a new token.
Content-Type Header for the DSN request should be application/json.
WebEngage will respond to the DSN request with an HTTP 2XX response code.
Request format of DSN payload from WSP to WebEngage
JSON
{
 "version": "1.0",
 "messageId" : "webengage-message-id",
 "toNumber" : "919999999999",
 "status": "whatsapp_sent",
 "statusCode" : 0,
 "reason": "FAILED WHILE TRANSMISSION",
 "timestamp": "2018-01-25T10:24:16+0000"
}
Key
Description
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
Status code of this DSN. This must be one of the status codes described below.
reason
It is an optional field (must be given when
statusCode
doesn’t fulfill failed reason, or when
statusCode
is 9988).
timestamp
The time when the message was triggered from the WebEngage system. This follows the ISO date format:
yyyy-MM-ddTHH:mm:ss±hhmm.
Example curl Request of DSN with Auth token Passed as Header for Authorization
JSON
curl --location --request POST '<STATIC-DSN-END-POINT-OF-WEBENGAGE>' \
--header 'Authorization: Bearer <AUTH-TOKEN-PROVIDED-BY-WEBENGAGE>' \
--header 'Content-Type: application/json' \
--data-raw '{
 "version": "1.0",
 "messageId" : "webengage-message-id",
 "toNumber" : "919999999999",
 "status": "whatsapp_sent",
 "statusCode" : 0,
 "reason": "sent successfully to user",
 "timestamp": "2018-01-25T10:24:16+0000"
}'
Status Code
These status codes are to be used both for synchronous responses and DSN. Refer to the Description column below for more details about the respective status. Make sure that you send the appropriate HTTP status corresponding to the status codes.
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
WebEngage uses auto-scaling to handle high traffic, which may occasionally trigger rate limits on your end. For throttled requests, return this status code so WebEngage can recognize the signal and retry delivery at a later time.
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
9988
For outcomes not covered above. Include the appropriate error description in the "message" field of the response
200
Updated
4 months ago
Email Service Provider
RCS Service Provider
Copy Page
