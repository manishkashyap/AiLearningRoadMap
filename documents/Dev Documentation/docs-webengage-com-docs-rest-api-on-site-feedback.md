# GET Feedback Responses

- URL: https://docs.webengage.com/docs/rest-api-on-site-feedback
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

GET Feedback Responses
🚧
Please make sure that you replace
HOST
in all the code snippets below with the host mentioned
here
.
WebEngage offers APIs for querying the feedback responses generated via WebEngage
on-site feedback widget
. These APIs also let you query replies on a particular feedback thread or even a specific reply.
/feedback/
<FeedbackId>
METHOD:
GET
DESCRIPTION:
Get feedback data for specific feedback identified by
FeedbackId
.
URL STRUCTURE:
<HOST>/v1/feedback/<FeedbackId>
AUTHENTICATION:
Bearer Authentication Scheme
EXAMPLE
cURL
curl -X GET <HOST>/v1/feedback/<FeedbackId> \
 --header 'Authorization: Bearer <YOUR_API_KEY>' \
 --header 'Content-Type: application/json'
Returns
JSON
{
 "response": {
 "data": {
 "licenseCode": "311c48b3",
 "fields": [{
 "id": "1fcdjgf",
 "label": "Name",
 "type": "default",
 "value": {
 "@class": "name",
 "text": "John"
 }
 }, {
 "id": "ah1ihjd",
 "label": "Email",
 "type": "default",
 "value": {
 "@class": "email",
 "text": "
[email protected]
"
 }
 }, {
 "id": "cci1868",
 "label": "Category",
 "type": "default",
 "value": {
 "@class": "category",
 "text": "Suggestion"
 }
 }, {
 "id": "~78me196",
 "label": "Message",
 "type": "default",
 "value": {
 "@class": "message",
 "text": "Thank you very much for this awesome service!"
 }
 }, {
 "id": "~5d68amb",
 "label": "Attach a screenshot of this page",
 "type": "default",
 "value": {
 "@class": "snapshot",
 "thumbnailImageUrl": ""
 }
 }, {
 "id": "n283q0",
 "label": "Enter your mobile number",
 "type": "custom",
 "value": {
 "@class": "text",
 "text": "9988776655"
 }
 }, {
 "id": "pp3j84",
 "label": "Your Bio",
 "type": "custom",
 "value": {
 "@class": "text",
 "text": "I am an early beta user of this product."
 }
 }, {
 "id": "19jb68o",
 "label": "Which countries you have been to?",
 "type": "custom",
 "value": {
 "@class": "list",
 "values": ["US", "Mexico"]
 }
 }, {
 "id": "1cc6lks",
 "label": "Rate our website",
 "type": "custom",
 "value": {
 "@class": "matrix",
 "values": {
 "Experience": ["Good"],
 "Content": ["Good"],
 "Design": ["Poor"]
 }
 }
 }, {
 "id": "sht4k8",
 "label": "Upload your resume",
 "type": "custom",
 "value": {
 "@class": "file",
 "fileName": "android_sdk_developing.pdf",
 "fileSize": 1919972,
 "fileAccessUrl": "<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/feedback-responses/ofq4jy/download",
 "fileType": "pdf"
 }
 }, {
 "id": "16qfkqk",
 "label": "What is your favourite color?",
 "type": "custom",
 "value": {
 "@class": "list",
 "values": ["Red"]
 }
 }, {
 "id": "16qhkqk",
 "label": "How likely is it that you would recommend WebEngage to a colleague?",
 "type": "custom",
 "value": {
 "@class": "score",
 "value": 10
 }
 }],
 "customData": {
 "userName": ["john"],
 "gender": ["male"],
 "customerType": ["Gold"],
 "jsessionid": ["CB300FEC898236FF9E5A181E468CA6BC"]
 },
 "replies": [{
 "repliedByEmail": "
[email protected]
",
 "repliedByName": "Mike",
 "repliedOn": "2013-02-11T08:27+0000",
 "repliedText": "Thanks for your feedback Joe. Your feature request is under development and planned for this weekend's release.\r\n\r\nRegards,\r\nMike",
 "attachments": [],
 "replyType": "ADMIN",
 "id": "8bea242d"
 }, {
 "repliedByEmail": "
[email protected]
",
 "repliedByName": "john",
 "repliedOn": "2013-02-11T08:37+0000",
 "repliedText": "Thanks! looking forward for the release.",
 "attachments": [],
 "replyType": "USER",
 "id": "a5828a9e"
 }, {
 "repliedByEmail": "
[email protected]
",
 "repliedByName": "Mike",
 "repliedOn": "2013-02-11T08:39+0000",
 "repliedText": "Sure. Meanwhile, take a look at the attached screenshot of the first draft. ",
 "attachments": [{
 "fileName": "git.from.bottom.up.pdf",
 "fileSize": 811094,
 "fileAccessUrl": "<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/feedback-reply-attachments/76178a43a/download",
 "fileType": "pdf"
 }],
 "replyType": "ADMIN",
 "id": "be1a0220"
 }],
 "id": "has7e2",
 "activity": {
 "pageUrl": "http://webengage.net/publisher/feedback-configuration/fields/311c48b3",
 "pageTitle": "Feedback Configuration - WebEngage",
 "ip": "127.0.0.1",
 "city": "Mumbai",
 "country": "India",
 "browser": "Firefox",
 "browserVersion": "18",
 "platform": "Linux",
 "activityOn": "2013-02-11T08:09+0000"
 }
 },
 "message": "success",
 "status": "success"
 }
}
The containers received in this response are described below:
activity
: Details of the user giving feedback on your website.
fields
: The responses of feedback form fields are in the
fields
container.
id
: Specifies the field ID.
type
: Could be either
default
or
custom
.
default
fields are the ones present by default in the WebEngage feedback form and
custom
fields are the ones added by you.
class
: Indicates the type of field. Examples of each class are listed below.
Default Fields
There are 5 types of default fields:
name
,
email
,
category
,
message
, and
snapshot
.
name
field
JSON
{
 "id": "1fcdjgf",
 "label": "Name",
 "type": "default",
 "value": {
 "@class": "name",
 "text": "John"
 }
}
email
field
JSON
{
 "id": "ah1ihjd",
 "label": "Email",
 "type": "default",
 "value": {
 "@class": "email",
 "text": "
[email protected]
"
 }
}
category
field
JSON
{
 "id": "cci1868",
 "label": "Category",
 "type": "default",
 "value": {
 "@class": "category",
 "text": "Suggestion"
 }
}
message
field
JSON
{
 "id": "~78me196",
 "label": "Message",
 "type": "default",
 "value": {
 "@class": "message",
 "text": "Thank you very much for this awesome service!"
 }
 }
snapshot
field
JSON
{
 "id": "~5d68amb",
 "label": "Attach a screenshot of this page",
 "type": "default",
 "value": {
 "@class": "snapshot",
 "thumbnailImageUrl": "http://s3-ap-southeast-1.amazonaws.com/wk-static-files/feedback/82617417/1358664682292-095c-ed2f-06bb-thumb-small.jpg",
 "fullImageUrl": "http://s3-ap-southeast-1.amazonaws.com/wk-static-files/feedback/82617417/1358664682292-095c-ed2f-06bb-full.jpg"
 }
}
🚧
thumbnailImageUrl
and
fullImageUrl
are public URLs of the screenshot of the page on which feedback was submitted.
Custom Form Fields
There are 4 types of default fields:
text
,
matrix
,
file
and
text
.
text
field
JSON
{
 "id": "pp3j84",
 "label": "Your Bio",
 "type": "custom",
 "value": {
 "@class": "text",
 "text": "I am an early beta user of this product."
 }
 }
list
field
Single option (radio and single-select drop-down) fields
JSON
{
 "id": "16qfkqk",
 "label": "What is your favourite color?",
 "type": "custom",
 "value": {
 "@class": "list",
 "values": ["Red"]
 }
}
List of multi-option (radio and multi-select drop-down) fields
JSON
{
 "id": "19jb68o",
 "label": "Which countries you have been to?",
 "type": "custom",
 "value": {
 "@class": "list",
 "values": ["US", "Mexico"]
 }
}
matrix
field
Values for matrix type questions
JSON
{
 "id": "1cc6lks",
 "label": "Rate our website",
 "type": "custom",
 "value": {
 "@class": "matrix",
 "values": {
 "Experience": ["Good"],
 "Content": ["Good"],
 "Design": ["Poor"]
 }
 }
}
file
field
Values for file uploads
JSON
{
 "id": "sht4k8",
 "label": "Upload your resume",
 "type": "custom",
 "value": {
 "@class": "file",
 "fileName": "android_sdk_developing.pdf",
 "fileSize": 1919972,
 "fileAccessUrl": "<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/feedback-responses/ofq4jy/download",
 "fileType": "pdf"
 }
}
🚧
Files can be downloaded by accessing the
fileAccessUrl
with your API credentials.
You can use the
fileName
value to save the downloaded file as illustrated below.
cURL
curl -H "Authorization: bearer your_api_token" -o android_sdk_developing.pdf <HOST>/v1/accounts/311c48b3/feedback-responses/ofq4jy/download
Custom Data
These are the custom data fields that are submitted along with the feedback on your site.
JSON
{
 "userName": ["john"],
 "gender": ["male"],
 "customerType": ["Gold"],
 "jsessionid": ["CB300FEC898236FF9E5A181E468CA6BC"]
}
/feedback/
<FeedbackId>
/replies
METHOD:
GET
DESCRIPTION:
Get the replies of a specific feedback thread identified by
FeedbackId
. This includes all the data related to a particular reply including all the attachments.
URL STRUCTURE:
<HOST>/v1/feedback/<FeedbackId>/replies
AUTHENTICATION:
User Authentication
EXAMPLE
cURL
curl -X GET <HOST>/v1/feedback/<FeedbackId>/replies \
 --header 'Authorization: Bearer <YOUR_API_KEY>' \
 --header 'Content-Type: application/json'
Returns
First reply added by site owner (Mike).
JSON
{
 "response": {
 "data": [{
 "repliedByEmail": "
[email protected]
",
 "repliedByName": "Mike",
 "repliedOn": "2013-02-11T08:27+0000",
 "repliedText": "Thanks for your feedback Joe. Your feature request is under development and planned for this weekend's release.\r\n\r\nRegards,\r\nMike",
 "attachments": [],
 "replyType": "ADMIN",
 "id": "8bea242d"
 }]
 }
}
Subsequent reply from John gets appended in the same return object.
JSON
{
 "response": {
 "data": [{
 "repliedByEmail": "
[email protected]
",
 "repliedByName": "Mike",
 "repliedOn": "2013-02-11T08:27+0000",
 "repliedText": "Thanks for your feedback Joe. Your feature request is under development and planned for this weekend's release.\r\n\r\nRegards,\r\nMike",
 "attachments": [],
 "replyType": "ADMIN",
 "id": "8bea242d"
 }, {
 "repliedByEmail": "
[email protected]
",
 "repliedByName": "john",
 "repliedOn": "2013-02-11T08:37+0000",
 "repliedText": "Thanks! looking forward for the release.",
 "attachments": [{
 "fileName": "pic-feautre-beta.jpg",
 "fileSize": 811094,
 "fileAccessUrl": "<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/feedback-reply-attachments/76178a43a/download",
 "fileType": "jpg"
 }],
 "replyType": "USER",
 "id": "a5828a9e"
 }]
 }
}
🚧
Attachments can be downloaded by accessing the
fileAccessUrl
with your API credentials.
You can use the
fileName
value to save the downloaded file as illustrated below.
cURL
curl -H "Authorization: bearer your_api_token" -o pic-feautre-beta.jpg <HOST>/v1/accounts/311c48b3/feedback-reply-attachments/76178a43a/download
/feedback/
<FeedbackId>
/reply/
<ReplyId>
METHOD:
GET
DESCRIPTION:
Get a specific reply of a feedback thread identified by
ReplyId
.
URL STRUCTURE:
<HOST>/v1/feedback/<FeedbackId>/reply/<ReplyId>
AUTHENTICATION:
User Authentication
EXAMPLE
cURL
curl -X GET <HOST>/v1/feedback/<FeedbackId>/reply/<ReplyId> \
 --header 'Authorization: Bearer <YOUR_API_KEY>' \
 --header 'Content-Type: application/json'
Returns
JSON
{
 "response": {
 "data": {
 "repliedByEmail": "
[email protected]
",
 "repliedByName": "Mike",
 "repliedOn": "2013-02-11T08:27+0000",
 "repliedText": "Thanks for your feedback Joe. Your feature request is under development and planned for this weekend's release.\r\n\r\nRegards,\r\nMike",
 "attachments": [],
 "replyType": "ADMIN",
 "id": "8bea242d"
 },
 "message": "success",
 "status": "success"
 }
}
/feedbacks/searches
METHOD:
POST
DESCRIPTION:
Search for feedback(s).
URL STRUCTURE:
<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/feedbacks/searches
AUTHENTICATION:
User Authentication
EXAMPLE
cURL
curl -X POST <HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/feedbacks/searches \
 --header 'Authorization: Bearer <YOUR_API_KEY>' \
 --header 'Content-Type: application/json' \
 --data '{
 "pageNo" : "1",
 "pageSize" : "5",
 "filter" : {
 "feedback_id": "~12l3ohu",
 "action": "unread", //Status
 "activity_type": "Question", //Category 
 "email": "
[email protected]
", //Email 
 "content": "hi", //Message
 "url": "https://dashboard.webengage.net/accounts/311c48b3/web/feedback-configuration/fields", //PageURL
 "ip": "192.168.1.1", //IP
 "browser":"Firefox", //Browser
 "browser_version": "51", // Browser version
 "to": "2013-02-11T08:25+0800", //To date
 "from": "2016-01-11T08:25+0800", // From date
 "country": "India", //Country
 "city": "mumbai", //City
 "tags":["ignore","test"] //Tags array
 "client_data": {
 "package": "Free 12k"
 }
}'
Parameters
JSON
{
 "pageNo" : "1",
 "pageSize" : "5",
 "filter" : {
 "feedback_id": "~12l3ohu",
 "action": "unread", //Status
 "activity_type": "Question", //Category 
 "email": "
[email protected]
", //Email 
 "content": "hi", //Message
 "url": "https://dashboard.webengage.net/accounts/311c48b3/web/feedback-configuration/fields", //PageURL
 "ip": "192.168.1.1", //IP
 "browser":"Firefox", //Browser
 "browser_version": "51", // Browser version
 "to": "2013-02-11T08:25+0800", //To date
 "from": "2016-01-11T08:25+0800", // From date
 "country": "India", //Country
 "city": "mumbai", //City
 "tags":["ignore","test"] //Tags array
 "client_data": {
 "package": "Free 12k"
 }
}
Parameter
Type
Description
feedback_id
String
Unique ID for the feedback
action
String
Status of feedback (read/unread/done)
activity_type
String
Category of feedback (Like/Question/Suggestion/Problem)
email
String
Email ID of the user submitting the feedback
content
String
Feedback message
url
String
Page URL
ip
String
IP address of the user submitting the feedback
browser
String
Browser through which feedback was submitted
browser_version
String
Browser version
tags
String Array
Feedback tags
Note: WebEngage will consider AND of all tags as the criteria
country
String
Country in which feedback was submitted
city
String
City in which feedback was submitted
client_data
Object
{"key","value"}
Client data passed from publisher
pageNo
String
Page number
pageSize
String
Page size
from
String
From date for search in ISO format: "yyyy-MM-dd'T'HH:mm:ss±hhmm"
to
String
To date for search in ISO format: "yyyy-MM-dd'T'HH:mm:ss±hhmm"
Returns
With reference to the below code snippet,
response
contains the list of feedback with following information:
1. Feedback Fields with Values:
Includes all the feedback fields, default and custom, with the response submitted.
2. Client Data/ Custom Data:
Details about the custom data passed from publisher.
3. Replies:
Details of replies in feedback thread including any attachments.
4. User Information:
The information of the user who has submitted the feedback.
Page Information:** Since the response can be large, it is divided into pages. This includes total page count and size of each page.
JSON
{
 "response": {
 "data": {
 "pageNo": 1,
 "contents": [
 {
 "licenseCode": "311c48b3",
 "fields": [
 {
 "id": "1fcdjgf",
 "label": "Name",
 "type": "NAME",
 "value": {
 "@class": "name",
 "text": "David"
 }
 },
 {
 "id": "ah1ihjd",
 "label": "Email",
 "type": "EMAIL",
 "value": {
 "@class": "email",
 "text": "
[email protected]
"
 }
 },
 {
 "id": "cci1868",
 "label": "Category",
 "type": "CATEGORY",
 "value": {
 "@class": "category",
 "text": "Like"
 }
 },
 {
 "id": "~78me196",
 "label": "Message",
 "type": "MESSAGE",
 "value": {
 "@class": "message",
 "text": "Splendid Experience, Thank you!"
 }
 },
 {
 "id": "~5d68amb",
 "label": "Attach a screenshot of this page",
 "type": "SCREENSHOT",
 "value": {
 "@class": "snapshot",
 "thumbnailImageUrl": "",
 "fullImageUrl": ""
 }
 },
 {
 "id": "~33egg4",
 "label": "Your Bio",
 "type": "TEXT",
 "value": {
 "@class": "text",
 "text": "I am an early beta user of this product."
 }
 },
 {
 "id": "~1ljk72m",
 "label": "Rate our website",
 "type": "RATING",
 "value": {
 "@class": "list",
 "values": [
 "4"
 ]
 }
 }
 ],
 "customData": {
 "package": [
 "Lite Package Usage"
 ],
 "user_id": [
 1736491
 ]
 },
 "replies": [
 {
 "repliedByEmail": "
[email protected]
",
 "repliedByName": "michael",
 "repliedOn": "2016-07-26T14:46:54+0000",
 "repliedText": "Thank you for the feedback!",
 "replyType": "ADMIN",
 "id": "27aa6849"
 },
 {
 "repliedByEmail": "
[email protected]
",
 "repliedByName": "david",
 "repliedOn": "2016-07-26T14:29:28+0000",
 "repliedText": "Thanks! looking forward for the release.",
 "attachments": [
 {
 "fileName": "thanks.jpg",
 "fileSize": 79418,
 "fileAccessUrl": "webengage/311c48b3/attachment/thanks_1469543364679.jpg",
 "fileType": "jpg"
 }
 ],
 "replyType": "USER",
 "id": "e2301c8"
 }
 ],
 "tags": [
 "test",
 "ignore"
 ],
 "id": "~12l3ohu",
 "activity": {
 "pageUrl": "https://dashboard.webengage.net/accounts/311c48b3/web/feedback-configuration/fields",
 "pageTitle": "Feedback Configuration - WebEngage",
 "ip": "127.0.0.1",
 "city": "Mumbai",
 "country": "India",
 "browser": "Chrome",
 "browserVersion": "51",
 "platform": "Mac",
 "activityOn": "2016-07-26T11:18:58+0000"
 }
 }
 ],
 "totalCount": 1,
 "numberOfPages": 1,
 "ascending": false,
 "pageSize": 25
 },
 "message": "success",
 "status": "success"
 }
}
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
On-site survey
Copy Page
