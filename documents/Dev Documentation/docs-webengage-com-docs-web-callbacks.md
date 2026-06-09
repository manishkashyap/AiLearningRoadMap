# Callbacks

- URL: https://docs.webengage.com/docs/web-callbacks
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Website
Callbacks
Callbacks are useful for understanding the lifecycle stages of WebEngage messages. All WebEngage callbacks are called on the main thread.
New Session Started
This callback is invoked when a new session is started by our web SDK.
JavaScript
webengage.onSessionStarted(function(){
 //CALLBACK LOGIC GOES HERE
})
On-site Notification Callbacks
Notification Opened
This callback is invoked when the on-site notification is opened.
JavaScript
webengage.notification.onOpen(function (data) {
 if (data.notificationId === '_NOTIFICATION_ID_') {
 //CALLBACK LOGIC GOES HERE
 }
});
The callback
data
Object in the above call looks like below.
JSON
{
 "notificationId": "173049892",
 "licenseCode": "311c48b3",
 "type": "notification",
 "title": "Check out the new pricing",
 "event": "open",
 "activity": {
 "pageUrl": "http://example.com/",
 "pageTitle": "Example Title",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "United States",
 "region": "Texas",
 "city": "Dallas",
 "ip": "127.0.0.1"
 },
 "customData": {
 "userName" : [ "johndoe" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Notification closed
This callback is invoked when the on-site notification is closed.
JavaScript
webengage.notification.onClose(function (data) {
 if (data.notificationId === '_NOTIFICATION_ID_') {
 //CALLBACK LOGIC GOES HERE
 }
});
The callback
data
Object in the above call looks like below.
JSON
{
 "notificationId": "173049892",
 "licenseCode": "311c48b3",
 "type": "notification",
 "title": "Checkout the new pricing",
 "event": "click",
 "actionLink": "http://example.com/pricing",
 "actionText": "Check out",
 "activity": {
 "pageUrl": "http://example.com/",
 "pageTitle": "Example Title",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "United States",
 "region": "Texas",
 "city": "Dallas",
 "ip": "127.0.0.1"
 },
 "customData": {
 "userName" : [ "johndoe" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
🚧
The callback data for Close event will be the same as the last event (Open or Click) for that notification.
Notification Clicked
JavaScript
webengage.notification.onClick(function (data) {
 if (data.notificationId === '_NOTIFICATION_ID_') {
 //CALLBACK LOGIC GOES HERE
 }
});
The callback
data
Object in the above call looks like below.
JSON
{
 "notificationId": "173049892",
 "licenseCode": "311c48b3",
 "type": "notification",
 "title": "Checkout the new pricing",
 "event": "click",
 "actionLink": "http://example.com/pricing",
 "actionText": "Check out",
 "activity": {
 "pageUrl": "http://example.com/",
 "pageTitle": "Example Title",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "United States",
 "region": "Texas",
 "city": "Dallas",
 "ip": "127.0.0.1"
 },
 "customData": {
 "userName" : [ "johndoe" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
On-site Survey Callbacks
Survey Opened
This callback is invoked when the on-site survey is opened.
JavaScript
webengage.survey.onOpen(function (data) {
 if (data.surveyId === '_SURVEY_ID_') {
 //CALLBACK LOGIC GOES HERE
 }
});
The callback
data
Object in the above call looks like below.
JSON
{
 "surveyId": "~5g1c4fd",
 "licenseCode": "311c48b3",
 "activity": {
 "pageUrl": "http://example.com/",
 "pageTitle": "Example Title",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "United States",
 "region": "Texas",
 "city": "Dallas",
 "ip": "127.0.0.1"
 },
 "type": "survey",
 "title": "Survey #1",
 "totalQuestions": 6,
 "customData": {
 "userName" : [ "johndoe" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Survey Closed
This callback is invoked when the on-site survey is closed.
JavaScript
webengage.survey.onClose(function (data) {
 if (data.surveyId === '_SURVEY_ID_') {
 //CALLBACK LOGIC GOES HERE
 }
});
The callback
data
Object in the above call looks like below.
JSON
{
 "surveyId": "~5g1c4fd",
 "licenseCode": "311c48b3",
 "activity": {
 "pageUrl": "http://example.com/",
 "pageTitle": "Example Title",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "United States",
 "region": "Texas",
 "city": "Dallas",
 "ip": "127.0.0.1"
 },
 "type": "survey",
 "title": "Survey #1",
 "totalQuestions": 6,
 "customData": {
 "userName" : [ "johndoe" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
🚧
The callback data for Close event will be the same as the last event (Open or Click) for that survey.
Survey Submit
This callback is invoked when a question is answered.
JavaScript
webengage.survey.onSubmit(function (data) {
 if (data.surveyId === '_SURVEY_ID_') {
 //CALLBACK LOGIC GOES HERE
 }
});
The callback
data
Object in the above call looks like below.
JSON
{
 "surveyId": "~5g1c4fd",
 "licenseCode": "311c48b3",
 "activity": {
 "pageUrl": "http://example.com/",
 "pageTitle": "Example Title",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "United States",
 "region": "Texas",
 "city": "Dallas",
 "ip": "127.0.0.1"
 },
 "type": "survey",
 "title": "Survey #1",
 "totalQuestions": 6,
 "customData": {
 "userName" : [ "johndoe" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 },
 "questionResponses": [{
 "questionId": "~1fstl7a",
 "questionText": "What is your favourite color?",
 "value": {
 "@class": "list",
 "values": ["Red"]
 }
 }]
}
Survey Complete
This callback is invoked when the on-site survey is completed.
JavaScript
webengage.survey.onComplete(function (data) {
 if (data.surveyId === '_SURVEY_ID_') {
 //CALLBACK LOGIC GOES HERE
 }
});
The callback
data
Object in the above call looks like below.
JSON
{
 "surveyId": "~5g1c4fd",
 "licenseCode": "311c48b3",
 "activity": {
 "pageUrl": "http://example.com/",
 "pageTitle": "Example Title",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "United States",
 "region": "Texas",
 "city": "Dallas",
 "ip": "127.0.0.1"
 },
 "type": "survey",
 "title": "Survey #1",
 "totalQuestions": 6,
 "customData": {
 "userName" : [ "johndoe" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 },
 "questionResponses": [
 {
 "questionId": "~1fstl7a",
 "questionText": "Your name?",
 "value": {
 "@class": "map",
 "values": {
 "First name": "John",
 "Last name": "Doe"
 }
 }
 },
 {
 "questionId": "~1asf233",
 "questionText": "Enter your mobile number?",
 "value": {
 "@class": "text",
 "text": "+14155552671"
 }
 },
 {
 "questionId": "we2e4545",
 "questionText": "Your Bio?",
 "value": {
 "@class": "text",
 "text" : "I am an early beta user of this product."
 }
 },
 {
 "questionId": "324saf3w",
 "questionText": "What is your favourite color?",
 "value": {
 "@class": "list",
 "values": ["Red"]
 }
 },
 {
 "questionId": "~213wrw43s",
 "questionText": "Which countries you have been to?",
 "value": {
 "@class": "list",
 "values": [ "US", "Mexico" ]
 }
 },
 {
 "questionId": "~ew347fev"
 "questionText": "Rate our website",
 "value": {
 "@class" : "matrix",
 "values" : {
 "Experience" : [ "Good" ],
 "Content" : [ "Good" ],
 "Design" : [ "Poor" ]
 }
 }
 },
 {
 "questionId": "sht4k8",
 "questionText": "Upload your resume",
 "value": {
 "@class" : "file",
 "fileName" : "john_doe_resume.pdf",
 "fileSize" : 1919972,
 "fileAccessUrl" : "https://api.webengage.com/v1/download/feedback/response/ofq4jy",
 "fileType" : "pdf"
 }
 }]
}
Usage Examples
Close survey after response of a particular question is submitted
Java
webengage.init('_LICENSE_CODE_');
webengage.survey.onSubmit(function (data) {
 var surveyInstance = this;
 if(data !== undefined && data.questionResponses !== undefined && data.questionResponses.length > 0) {
 for(var i=0; i < data.questionResponses.length; i++) {
 var question = data.questionResponses[i];
 if(question["questionId"] === "324saf3w") {
 var questionResponse = question["value"];
 var values = questionResponse["values"];
 if(values !== 'undefined' && values.length > 0){
 for(var k=0; k < values.length; k++) {
 if(values[k] === 'RED') {
 surveyInstance.close();
 break;
 }
 }
 }
 break;
 }
 }
 }
});
Redirect a user on survey completion
JavaScript
webengage.survey.onComplete(function () {
 window.location.href='/newletter/subscribe.html';
});
On-site Feedback Callbacks (Deprecated)
Feedback Opened
This callback is invoked when the on-site feedback widget is opened.
JavaScript
webengage.feedback.onOpen(function (data) {
 //CALLBACK LOGIC GOES HERE
});
The callback
data
Object in the above call looks like below.
JSON
{
 "licenseCode": "311c48b3",
 "type": "feedback",
 "activity": {
 "pageUrl": "http://example.com/page",
 "pageTitle": "Example Title",
 "ip": "127.0.0.1",
 "city": "Dallas",
 "country": "United States",
 "browser": "Firefox",
 "browserVersion": "18",
 "platform": "Linux",
 "activityOn": "2013-02-11T08:09+0000"
 },
 "customData": {
 "userName" : [ "johndoe" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Feedback Closed
This callback is invoked when the on-site feedback widget is closed.
JavaScript
webengage.feedback.onClose(function (data) {
 //CALLBACK LOGIC GOES HERE
});
The callback
data
Object in the above call looks like below.
JSON
{
 "licenseCode": "311c48b3",
 "type": "feedback",
 "activity": {
 "pageUrl": "http://example.com/page",
 "pageTitle": "Example Title",
 "ip": "127.0.0.1",
 "city": "Dallas",
 "country": "United States",
 "browser": "Firefox",
 "browserVersion": "18",
 "platform": "Linux",
 "activityOn": "2013-02-11T08:09+0000"
 },
 "customData": {
 "userName" : [ "johndoe" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
🚧
The callback data for Close event will be the same as the last event (Open or Click) for that feedback.
Feedback Submitted
This callback is invoked when the on-site feedback is submitted.
JavaScript
webengage.feedback.onSubmit(function (data) {
 //CALLBACK LOGIC GOES HERE
});
The callback
data
Object in the above call looks like below.
JSON
{
 "id": "has7e2",
 "licenseCode": "311c48b3",
 "type": "feedback",
 "fields": [{
 "id": "1fcdjgf",
 "label": "Name",
 "type": "default",
 "value": {
 "@class": "name",
 "text": "John Doe"
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
 "text": "+14155552671"
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
 "fileName": "john_doe_resume.pdf",
 "fileSize": 1919972,
 "fileAccessUrl": "https://api.webengage.com/v1/download/feedback/response/ofq4jy",
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
 }],
 "activity": {
 "pageUrl": "http://example.com/page",
 "pageTitle": "Example Title",
 "ip": "127.0.0.1",
 "city": "Dallas",
 "country": "United States",
 "browser": "Firefox",
 "browserVersion": "18",
 "platform": "Linux",
 "activityOn": "2013-02-11T08:09+0000"
 },
 "customData": {
 "userName" : [ "johndoe" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Usage Examples
Close the feedback window 5 seconds after user submits feedback
JavaScript
webengage.feedback.onSubmit(function (data) {
 var feedbackInstance = this;
 setTimeout(function(){
 feedbackInstance.close();
 }, 5000);
});
Web Push Callbacks
Web Push Notification Permission Prompt Viewed
For both 1-step opt-in and 2-step opt-in, this callback is invoked when browser prompts the notification permission to the user.
JavaScript
webengage.options('webpush.onWindowViewed', function () {
// Callback logic goes here.
});
Web Push Notification Permission Granted
For 1-step opt-in, this callback is invoked when the user grants permission for Web Push. For 2-step opt-in, it is invoked when the custom permission prompt window closes after the user grants permission for Web Push.
JavaScript
webengage.options('webpush.onWindowAllowed', function () {
// Callback logic goes here.
});
Web Push Notification Permission Denied
For 1-step opt-in, this callback is invoked when the user denies permission for Web Push. For 2-step opt-in, it is invoked when the custom permission prompt window closes after the user denies permission for Web Push.
JavaScript
webengage.options('webpush.onWindowDenied', function () {
// Callback logic goes here.
});
Web Push Notification Permission Granted First Time
For 1-step opt-in, this callback is invoked when the user grants permission for Web Push for the first time. For 2-step opt-in, it is invoked when the custom permission prompt window closes after the user grants permission for Web Push for the first time.
JavaScript
webengage.options('webpush.onPushRegistered', function () {
// Callback logic goes here.
});
Web Push Notification Permission Revoked
For 1-step opt-in, this callback is invoked when the user revokes permission for Web Push after having granted it before. This callback is not available for 2-step opt-in.
JavaScript
webengage.options('webpush.onPushUnregistered', function () {
// Callback logic goes here.
});
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Copy Push to Web Inbox
Advanced
Copy Page
