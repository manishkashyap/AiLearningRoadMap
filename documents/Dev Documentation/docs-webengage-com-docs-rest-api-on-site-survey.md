# GET Survey Responses

- URL: https://docs.webengage.com/docs/rest-api-on-site-survey
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

REST API
GET Survey Responses
📘
Make sure you replace
HOST
in all the code snippets below with the host mentioned
here
.
WebEngage offers API for querying the survey responses generated via WebEngage on-site survey widget.
/survey/response/<ResponseId>
METHOD:
GET
DESCRIPTION:
Get survey response data identified by
ResponseId
.
URL STRUCTURE:
<HOST>/v1/survey/response/<ResponseId>
AUTHENTICATION:
User Authentication
EXAMPLE
cURL
curl -X GET <HOST>/v1/survey/response/<ResponseId> \
 --header 'Authorization: Bearer <YOUR_API_KEY>' \
 --header 'Content-Type: application/json'
🚧
Make sure you replace
ResponseId
with the survey response ID and
YOUR_API_KEY
with your
WebEngage API key
.
Returns
JSON
{
 "response": {
 "data": {
 "surveyId": "7djl637",
 "title": "Customer Satisfaction Survey",
 "licenseCode": "311c48b3",
 "questionResponses": [{
 "id": "~11uth8m",
 "questionId": "6f51d6",
 "questionText": "Which countries you have been to?",
 "value": {
 "@class": "list",
 "values": ["Mexico"]
 }
 }, {
 "id": "~vqxl96",
 "questionId": "980gpa",
 "questionText": "Rate our website",
 "value": {
 "@class": "matrix",
 "values": {
 "Experience": ["Good"],
 "Content": ["Poor"],
 "Design": ["Good"]
 }
 }
 }, {
 "id": "~67j6bv",
 "questionId": "2i98bsk",
 "questionText": "Upload Product Image",
 "value": {
 "@class": "file",
 "fileName": "shoes-for-men-by-tzaro.jpg",
 "fileSize": 33731,
 "fileAccessUrl": "<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/survey-responses/~67j6bv/download",
 "fileType": "jpg"
 }
 }, {
 "id": "~13nacf",
 "questionId": "2l23rao",
 "questionText": "What is your favourite color?",
 "value": {
 "@class": "list",
 "values": ["Red", "Blue"]
 }
 }, {
 "id": "~gfaxas",
 "questionId": "2notcms",
 "questionText": "Your profile",
 "value": {
 "@class": "map",
 "values": {
 "Name": "jhon",
 "Qualification": "",
 "Age": "24"
 }
 }
 }],
 "customData": {
 "customerType": ["Gold"],
 "productCategory": ["Footwear"],
 "jsessionid": ["CDB300FEF898236FF9E5A181E468CA6BCD"]
 },
 "id": "1kfrn7c",
 "activity": {
 "pageUrl": "http://webengage.net/",
 "pageTitle": "In-site customer Feedback, targeted Surveys & push Notifications for Websites - WebEngage",
 "ip": "127.0.0.1",
 "city": "Mumbai",
 "country": "India",
 "browser": "Chrome",
 "browserVersion": "26",
 "platform": "Linux",
 "activityOn": "2013-05-08T10:34:33+0000"
 }
 },
 "message": "success",
 "status": "success"
 }
 }
The containers received in this response are described below:
activity
: Details of the user giving survey on your website.
questionResponses
: The responses of survey questions are in the
questionResponses
container.
id
: Specifies the question response ID.
type
: There are 5 types of questions:
list
,
matrix
,
file
,
text
and
map
.
@class
: Indicates the type of question. Examples of each class are listed below.
text
question response
JSON
{
 "id": "~gfaxas",
 "questionId": "2notcms",
 "questionText": "Your profile",
 "value": {
 "@class": "map",
 "values": {
 "Name": "jhon",
 "Qualification": "",
 "Age": "24"
 }
 }
}
list
question response
Single option (radio and single-select drop-down) questions
JSON
{
 "id": "~11uth8m",
 "questionId": "6f51d6",
 "questionText": "Which countries you have been to?",
 "value": {
 "@class": "list",
 "values": ["Mexico"]
 }
}
List of multi-option (radio and multi-select drop-down) questions
JSON
{
 "id": "~13nacf",
 "questionId": "2l23rao",
 "questionText": "What is your favourite color?",
 "value": {
 "@class": "list",
 "values": ["Red", "Blue"]
 }
}
NPS question response
JSON
{
 "questionId": "16qfkqk",
 "questionText": "How likely is it that you would recommend WebEngage to a colleague?",
 "value": {
 "@class": "score",
 "value": 10
 }
}
matrix
question response
JSON
{
 "id": "~vqxl96",
 "questionId": "980gpa",
 "questionText": "Rate our website",
 "value": {
 "@class": "matrix",
 "values": {
 "Experience": ["Good"],
 "Content": ["Poor"],
 "Design": ["Good"]
 }
 }
}
file
question response
JSON
{
 "id": "~67j6bv",
 "questionId": "2i98bsk",
 "questionText": "Upload Product Image",
 "value": {
 "@class": "file",
 "fileName": "shoes-for-men-by-tzaro.jpg",
 "fileSize": 33731,
 "fileAccessUrl": "<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/survey-responses/~67j6bv/download",
 "fileType": "jpg"
 }
}
📘
Files can be downloaded by accessing the
fileAccessUrl
with your API credentials.
You can use the
fileName
value to save the downloaded file as illustrated below.
cURL
curl -H "Authorization: bearer your_api_token" -o shoes-for-men-by-tzaro.jpg <HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/survey-responses/~67j6bv/download
Custom Data
These are the custom data fields that are submitted along with the survey on your site.
JSON
{
 "customerType": ["Gold"],
 "productCategory": ["Footwear"],
 "jsessionid": ["CDB300FEF898236FF9E5A181E468CA6BCD"]
}
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Transactional Campaign API
Bulk User/ Event API
Copy Page
