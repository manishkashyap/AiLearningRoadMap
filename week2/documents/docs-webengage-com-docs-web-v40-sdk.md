# Legacy SDK v4

- URL: https://docs.webengage.com/docs/web-v40-sdk
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

SDK Changelogs
Web SDK
Legacy SDK v4
JavaScript API (Version 4.0)
Once you sign-up and integrate
Webengage Widget Code
on your web-site, you can use this Javascript API to change the default behaviour of how the Surveys, Feedback and Notifications work on your site to suit your needs.
Integration Code and API
Default Integration Code
Following is the default
one time integration code
snippet -
HTML
<script id="_webengage_script_tag" type="text/javascript">
 var _weq = _weq || {
 'webengage.licenseCode' : '_LICENSE_CODE_'
 };
 (function(d){
 var _we = d.createElement('script');
 _we.type = 'text/javascript';
 _we.async = true;
 _we.src = (d.location.protocol == 'https:' ? _WIDGET_SSL_DOMAIN_ : _WIDGET_DOMAIN_ ) + "/js/widget/webengage-min-v-4.0.js";
 var _sNode = d.getElementById('_webengage_script_tag');
 _sNode.parentNode.insertBefore(_we, _sNode);
 })(document);
</script>
This code loads and initializes WebEngage Widget asynchronously, so it does not block loading of your web page. This is cautiously done to not impact page load time on your website. The URLs in the above code are
protocol relative
. This lets the browser to load the widget over the same protocol (HTTP or HTTPS) as the containing page, which will prevent "Insecure Content" warnings.
Initialization
All widget configuration parameters are set in a global JavaScript object called
_weq
. Once the WebEngage Widget JavaScript loads, it initialises the widget based on
_weq
map properties. The default shipped integration code sets the
licenseCode
key in the
_weq
map. Similarly, you can set other widget properties and callback functions in the
_weq
map.
Global Configuration (_weq Map)
All global and static configuration either at the widget level or individual product (Feedback, Survey or Notification) level are set in a global map named
_weq
. This configuration includes set of properties as well as callback event handlers (functions). The complete set of keys supported in the
_weq
are listed in the tables below:
Widget Settings
Widget Configuration Properties
Property
Type
Description
Default
licenseCode*
String
Registered license code for the website. You can get it from your Webengage dashboard if registered, otherwise
signup
to get your licenseCode.
N/A
language*
String
Specify your widget language here. The static messages present in your feedback/survey form will appear in the language specified here.
As per settings in the dashboard
delay*
number
Delays API initialization for the time specified (in milliseconds).
0
defaultRender
boolean
If set to false, then by default on widget initialization, none of the products (feedback, survey and notification) appears. To stop rendering selective products from rendering, set the
defaultRender
at the product level configuration properties.
true
customData
object
Specify your custom data here in proper JSON format to submit along with every survey / feedback submission and notification click
null
ruleData
object
Specify your rule data here in proper JSON format. The keys should match with the values used in Targeting rules section for the corresponding Survey or Notification
null
tokens
object
Specify your tokens data here in proper JSON format
null
enableCallbacks
boolean
If set to true, will enable callbacks for all the events of feedback, survey and notificaton
true
*
Property used only at the init time, changing this property later will have no effect
Examples of using Widget Configuration Properties
1. Load WebEngage widget after 5 seconds
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.delay'] = 5;
2. Pass your own custom/business data for tracking (e.g. userId, email, sessionId etc.)
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.customData'] = { 'userId' : '2947APW09', 'age' : 21, 'isPaidCust' : false };
This data will be passed to all the activated products Survey,Feedback and Notification unless their own specific custom data (eg. webengage.feedback.customData ) is provided.
3. Hide WebEngage by default on mobile and tablets
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';

var isMobile = {
 Android: function() {
 return navigator.userAgent.match(/Android/i);
 },
 BlackBerry: function() {
 return navigator.userAgent.match(/BlackBerry/i);
 },
 iOS: function() {
 return navigator.userAgent.match(/iPhone|iPad|iPod/i);
 },
 Opera: function() {
 return navigator.userAgent.match(/Opera Mini/i);
 },
 Windows: function() {
 return navigator.userAgent.match(/IEMobile/i);
 },
 any: function() {
 return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
 }
};

if (isMobile.any()) {
 _weq['webengage.defaultRender'] = false; 
}
Widget Callbacks
Callback
Type
Description
Default
onReady
Function
Any code that you want to run after the API is loaded and initialized should be placed within the
webengage.onReady
null
Examples of using Widget Callback
1. Show a survey on click of a button instead of default rendering
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
//default rendering is disabled
_weq['webengage.survey.defaultRender'] = false;
_weq['webengage.onReady'] = function(){
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.survey.render();
 };
};
Global Methods
webengage.track
This method allows you to pass business events to WebEngage for analytics or to trigger surveys/notifications.
All passed events are captured in the event analytics screen (coming soon)
Parameters
Name
Type
Description
eventName
String
Name of the event that occurred
eventData
Object
Data to associate with the event. Pass a simple object with only strings, numbers, booleans and dates as property values
Example of a webengage.track call
1. Let WebEngage know when a visitor leaves a cart before checkout
JavaScript
webengage.track('cartAbandoned', { userID: 1337, country: 'India' });
Survey Settings
Survey Configuration Properties
Property
Type
Description
Default
surveyId
String
To show a specific survey, specify the surveyId
null
skipRules
Boolean
If set to true, targeting rules specified in the dashboard for the active surveys are not executed. Thus, all the active surveys, unless surveyId is specified, become eligible to be shown.
false
forcedRender
Boolean
If set to true, the submitted or closed surveys also become elgible to be shown.
false
defaultRender
Boolean
If set to false, the eligible survey is not displayed by default.
true
delay
Number
Time delay, in miliseconds, to show a survey on a page. It overrides the time delay specified in the dashboard.
As set in the dashboard
scope
String/Object
A visitor life cycle depends on a long term cookie installed for your site in a browser. Lifecyle of a survey depends on the scope of a visitor. If a survey is closed, it doesn't appear for the visitor in the same browser session. If a survey is submitted, then it doesn't appear for the same visitor at all. If you want a survey to appear in every new browser session irrespective of the survey being taken in a past session, you can define your own scope. In this case, specify scope as SESSION_ID and the lifecycle of a survey remains within the scope of a session id. See examples below -
null
scopeType
String
By defining custom scope, you can make a survey submitted once in that scope. By specifying the scopeType as 'session', you can narrow a scope within that session, making a possibility of a survey appearing multiple times to a visitor per each scope. By specifying the scopeType as 'global', you can make a survey submitted once per each scope value across different browser sessions/visitors.
session
customData
Object
Specify your custom data for survey in proper JSON format to submit along with every survey submission. If not set then webengage.customData is referred
null
ruleData
Object
Specify your rule data here in proper JSON format to filter you audience, with the keys you specified in the WebEngage Dashboard while editing rule for the corresponding Survey. If not specified webengage.ruleData is refered
null
enableCallbacks
Boolean
If set to true, will enable callbacks for all the survey events.
false
Examples of using Survey Properties
1. Pass business data for custom rules
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.survey.ruleData'] = {
 'itemsInCart' : 3,
 'cartAmount' : 1288,
 'customerType' : 'gold'
};
2. Show surveys to a visitor everytime a new browser session starts
By specifying a session_id (some unique identifier for a browser session) as the survey scope with scopeType as 'session', one can make a survey re-appear to a visitor, even if (s)he has closed or submitted it in a previous browser session.
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.survey.scope'] = "_USER_SESSION_ID_";
_weq['webengage.survey.scopeType'] = "session";
3. Show a survey to a visitor every day irrespective (s)he has closed/submitted the same survey.
By specifying a today's date as the survey scope, one can make a survey re-appear to a visitor each day even if he has closed or submitted it.
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
var today = new Date();
_weq['webengage.survey.scope'] = {
 'scope' : (today.getDate()+"-"+today.getMonth()+"-"+today.getYear()),
 'scopeType' : 'session',
 'surveyIds' : ["~29aj48l"]
};
4. Show a survey once to a logged in user from differernt browsers
If one wants a survey to be submitted once per logged in user irrespective of different browser sessions, then specify logged in user's email or userId as the scope with scopeType as 'global'.
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.survey.scope'] = '_USER_EMAIL_';
_weq['webengage.survey.scopeType'] = 'global';
Survey Callbacks
Callback
Description
Callback data
onOpen
invoked on survey open
Object
onClose
invoked when a survey is closed
Object
onSubmit
invoked when a question is answered
Object
onComplete
invoked when the thank you message is displayed in the end
Object
Survey onOpen callback data (JSON)
JSON
{
 "surveyId": "~5g1c4fd",
 "licenseCode": "311c48b3",
 "activity": {
 "pageUrl": "http://webengage.net/",
 "pageTitle": "In-site customer Feedback, targeted Surveys & push Notifications for Websites - WebEngage",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "India",
 "region": "Maharashtra",
 "city": "Mumbai",
 "ip": "127.0.0.1"
 },
 "type": "survey",
 "title": "Survey #1",
 "totalQuestions": 6,
 "customData": {
 "userName" : [ "john" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Survey onSubmit callback data (JSON)
JSON
{
 "surveyId": "~5g1c4fd",
 "licenseCode": "311c48b3",
 "activity": {
 "pageUrl": "http://webengage.net/",
 "pageTitle": "In-site customer Feedback, targeted Surveys & push Notifications for Websites - WebEngage",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "India",
 "region": "Maharashtra",
 "city": "Mumbai",
 "ip": "127.0.0.1"
 },
 "type": "survey",
 "title": "Survey #1",
 "totalQuestions": 6,
 "customData": {
 "userName" : [ "john" ],
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
Survey onComplete callback data (JSON)
JSON
{
 "surveyId": "~5g1c4fd",
 "licenseCode": "311c48b3",
 "activity": {
 "pageUrl": "http://webengage.net/",
 "pageTitle": "In-site customer Feedback, targeted Surveys & push Notifications for Websites - WebEngage",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "India",
 "region": "Maharashtra",
 "city": "Mumbai",
 "ip": "127.0.0.1"
 },
 "type": "survey",
 "title": "Survey #1",
 "totalQuestions": 6,
 "customData": {
 "userName" : [ "john" ],
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
 "First name": "ABC",
 "Last name": "EFG"
 }
 }
 },
 {
 "questionId": "~1asf233",
 "questionText": "Enter your mobile number?",
 "value": {
 "@class": "text",
 "text": "9988776655"
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
 "questionText": "Rate out website?",
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
 "questionText": "Upload your resume?",
 "value": {
 "@class" : "file",
 "fileName" : "android_sdk_developing.pdf",
 "fileSize" : 1919972,
 "fileAccessUrl" : "https://api.webengage.com/v1/download/feedback/response/ofq4jy",
 "fileType" : "pdf"
 }
 }]
}
Survey onClose callback data (JSON)
On survey close the callback data for close event handlers will the latest event's (Open, Submit or Complete) callback data that happened before close.
Lets say if you close a survey after it opens the callback data for close event would same as the onOpen callback data as mentioned above.
JSON
{
 "surveyId": "~5g1c4fd",
 "licenseCode": "311c48b3",
 "activity": {
 "pageUrl": "http://webengage.net/",
 "pageTitle": "In-site customer Feedback, targeted Surveys & push Notifications for Websites - WebEngage",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "India",
 "region": "Maharashtra",
 "city": "Mumbai",
 "ip": "127.0.0.1"
 },
 "type": "survey",
 "title": "Survey #1",
 "totalQuestions": 6,
 "customData": {
 "userName" : [ "john" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Examples of using Survey Callbacks
1. Close survey after certain response of a particular question
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.enableCallbacks'] = true;
_weq['webengage.survey.onSubmit'] = function (data) {
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
};
2. Redirect a user on survey completion
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.survey.onComplete'] = function () {
 window.location.href='/newletter/subscribe.html';
};
Survey Methods
1. webengage.survey.render
This method allows you to overwrite the dashboard settings. It also overwrites the settings provided in
_weq
in the widget code. This method accepts all the
_weq survey configuration properties
and
_weq callbacks
.
Name
Type
Description
options
Object
Survey configuration properties
callbacks
Examples of Render Method
1. Open a survey on click of a button
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.survey.surveyId'] = '_SURVEY_ID_'; // survey id to be rendered ... note : it is optional
_weq['webengage.survey.defaultRender'] = false;
_weq['webengage.onReady'] = function () {
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.survey.render();
 };
};
2. Open a survey on page scroll (down)
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.onReady'] = function () {
 var getScrollPercentage = function () {
 var documentHeight = $(document).height();
 var viewPortHeight = $(window).height();
 var verticlePageOffset = $(document).scrollTop();
 return Math.round(100* (viewPortHeight+verticlePageOffset)/documentHeight);
 }
 var surveyDisplayed = false;
 window.onscroll = function (event) {
 if (!surveyDisplayed && getScrollPercentage() >= 70) {
 webengage.survey.render({ surveyId : '_SURVEY_ID_' }); // invoking webengage.survey.render with specific survey id
 surveyDisplayed = true;
 }
 }
};
Please scroll down, till the end to see this in effect.
Also, notice that we are calling
webengage.survey.render
by passing it surveyId option.
3. Passing Custom Data / Rule Data
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.survey.ruleData'] = { 'categoryCode' '_CATEGORY_CODE_', 'paidCustomer' : true };
_weq['webengage.onReady'] = function () {
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.survey.render({
 'customData' : { 'userId' : '_USER_ID_', 'age' : _AGE_ }
 });
 };
};
4. Tracking survey view in console
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.onReady'] = function(){
 document.getElementById("_BUTTON_ID_").onclick = function(){
 webengage.survey.render().onView( function(){
 console.log("survey open");
 });
 };
};
2. webengage.survey.clear
Clears rendered survey.
Examples of Clear Method
1. Clear a survey on click of a button
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.onReady'] = function () {
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.survey.clear();
 };
};
Feedback Settings
Feedback Configuration Properties
Property
Type
Description
Default
delay
Number
Time delay, in milliseconds, to show the feedback tab on a page.
null
formData
Array of
Object
Specify values in the feedback form for the pre-population of the fields.
example
null
alignment
string
Shows the feedback tab on the left/right side of the webpage. The possible value that you can specify here is
left
or
right
.
As specified in feedback tab configuration
borderColor
string
Renders feedback tab with the specified border color
As specified in feedback tab configuration
backgroundColor
string
Renders feedback tab with the specified background color
As specified in feedback tab configuration
defaultCategory
string
Shows the feedback form based on the feedback category specified here.
As specified in feedback tab configuration
showAllCategories
boolean
If set to
true
, the feedback form appears with feedback category drop down menu to let the end users to submit contextual feedbacks. If set to
false
, the feedback form appears based on the default feedback category specified without any feedback category dropdown menu.
true
showForm
boolean
If set to
true
, feedback form slides out, on page load, by default.
false
defaultRender
boolean
If set to false, the feedback tab is not displayed by default.
true
customData
object
Specify your custom data here in proper JSON format to submit along with every feedback got submitted, if not specified
webengage.data
is referred.
null
enableCallbacks
boolean
If set to true, will enable callbacks for all the feedback events.
false
formData Object
Property
Type
Description
name
String
Label of the field in the feedback form which you want to prepopulate data or want to hide or make it mandatory
value
String
Specify the value of the field
mode
String
Specify if the field should be hidden, read only or default (no-change). So values only supported are
hidden
and
readOnly
and
default
isMandatory
Boolean
Specify if the field should be mandatory or not
options
String Array
Applicable only in case of ‘Category’ field. Specify in case you want to show specific values in the category dropdown
NOTE
: To see the example code click
here
Examples of using Feedback Properties
1. Set feedbackTab alignment to right
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.feedback.alignment'] = 'right';
2. Set feedback tab background colours and border colours
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.feedback.backgroundColor'] = '#ff9';
_weq['webengage.feedback.borderColor'] = '#f99';
3. Prepopulate email and keep it readonly, hide message, specific options for category drop-down
// Values int the category drop-down 'Like' & 'Question'
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.feedback.formData'] = [
 {
 'name' : 'email',
 'value' : '_EMAIL_VALUE_',
 'mode' : 'readOnly'
 }, {
 'name' : 'message',
 'mode' : 'hidden'
 }, {
 'name' : 'category',
 'isMandatory' : false, 
 'value' : 'like',
 'options' : ['Like', 'Question'] // make sure you send right category lables
 }
];
Feedback Callbacks
Callback
Description
Callback data
onOpen
invoked on feedback form open
Object
onClose
invoked when feedback form is closed
Object
onSubmit
invoked when a feedback is submitted
Object
Feedback onOpen callback data (JSON)
JSON
{
 "licenseCode": "311c48b3",
 "type": "feedback",
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
 },
 "customData": {
 "userName" : [ "john" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Feedback onSubmit callback data (JSON)
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
 "pageUrl": "http://webengage.net/publisher/feedback-configuration/fields/311c48b3",
 "pageTitle": "Feedback Configuration - WebEngage",
 "ip": "127.0.0.1",
 "city": "Mumbai",
 "country": "India",
 "browser": "Firefox",
 "browserVersion": "18",
 "platform": "Linux",
 "activityOn": "2013-02-11T08:09+0000"
 },
 "customData": {
 "userName" : [ "john" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Feedback onClose callback data (JSON)
On feedback close the callback data for close event handlers will the latest event's (Open or Submit) callback data that happened before close.
Lets say if you close feedback window after it opens the callback data for close event would same as the onOpen callback data as mentioned above.
JSON
{
 "licenseCode": "311c48b3",
 "type": "feedback",
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
 },
 "customData": {
 "userName" : [ "john" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Examples of using Feedback Callbacks
1. Close the feedback window in 5 second just after someone submits feedback.
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.enableCallbacks'] = true;
_weq['webengage.feedback.onSubmit'] = function () {
 var feedbackInstance = this;
 setTimeout(function(){
 feedbackInstance.close();
 }, 5000);
};
Feedback Methods
1. webengage.feedback.render
This method allows you to overwrite the dashboard settings. It also overwrites the settings provided in
_weq
in the widget code. This method accepts all the
_weq feedback configuration properties
and
_weq callbacks
.
Name
Type
Description
options
Object
Feedback Configuration Properties
&
callbacks
Examples for Render Method
1. Show a feedback on click of a button
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.onReady'] = function () {
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.feedback.render({ 'showForm' : true });
 };
};
2. webengage.feedback.clear
Example of clear Method
1. Clear a feedback on click of a button
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.onReady'] = function () {
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.feedback.clear();
 };
};
Notification Settings
Notification Configuration Properties
Property
Type
Description
Default
notificationId
String
To show a specific notification, specify the notificationId
null
skipRules
Boolean
If set to true, targeting rules specified in the dashboard for the active notifications are not executed. Thus, all the active notifications, unless notificationId is specified, become eligible to be shown
false
forcedRender
Boolean
If set to true, the clicked or closed notifications also become elgible to be shown
false
delay
Number
Time delay, in miliseconds, to show a survey on a page. It overrides the time delay specified in the dashboard
null
defaultRender
Boolean
If set to false, the eligible notification is not displayed by default
true
customData
Object
Specify your custom data for notification here in proper JSON format to submit along with every notification click. If not set then
webengage.customData
is referred
null
ruleData
Object
Specify your rule data here in proper JSON format to filter you audience, with the keys you specified in the WebEngage Dashboard while editing rule for the corresponding Notification. If not specified
webengage.ruleData
is refered
null
tokens
Object
Specify your tokens data here in proper JSON format. If not specified
webengage.tokens
is refered
null
enableCallbacks
Boolean
If set to true, will enable callbacks for all the notification events
false
Examples of using Notification Properties
1. Delay a particular notification rendering
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.notification.delay'] = 5;
_weq['webengage.notification.notificationId'] = _NOTIFICATION_ID_;
Note
: If you have already set the time-delay in the notification rule while creating it,
webengage.notification.delay
will overwrite it.
2. Skip rules on a page for notifications
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.notification.skipRules'] = true;
3. Custom rules - showing a "we are offline" notification every Sunday
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
var daysInWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
_weq['webengage.notification.ruleData'] = {day : daysInWeek[new Date().getDay()]};
Note
: In custom rules section, on the targeting page, you can use the "day" variable to create targeting rules. For example, if the day is "Sunday", display a notification on your contact page that your support team is currently offline.
Notification Callbacks
Callback
Description
Callback data
onOpen
invoked on notification open
Object
onClose
invoked when a notification is closed
Object
onClick
invoked when a notification is clicked
Object
Notification onOpen callback data (JSON)
JSON
{
 "notificationId": "173049892",
 "licenseCode": "311c48b3",
 "type": "notification",
 "title": "Checkout the new pricing",
 "event": "open",
 "activity": {
 "pageUrl": "http://webengage.net/",
 "pageTitle": "In-site customer Feedback, targeted Surveys & push Notifications for Websites - WebEngage",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "India",
 "region": "Maharashtra",
 "city": "Mumbai",
 "ip": "127.0.0.1"
 },
 "customData": {
 "userName" : [ "john" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Notification onClick callback data (JSON)
JSON
{
 "notificationId": "173049892",
 "licenseCode": "311c48b3",
 "type": "notification",
 "title": "Checkout the new pricing",
 "event": "click",
 "actionLink": "http://webengage.com/pricing",
 "actionText": "Check out",
 "activity": {
 "pageUrl": "http://webengage.net/",
 "pageTitle": "In-site customer Feedback, targeted Surveys & push Notifications for Websites - WebEngage",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "India",
 "region": "Maharashtra",
 "city": "Mumbai",
 "ip": "127.0.0.1"
 },
 "customData": {
 "userName" : [ "john" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Notification onClose callback data (JSON)
On notification close the callback data for close event handlers will the latest event's (Open or Click) callback data that happened before close.
Lets say if you close a notification after it opens the callback data for close event would same as the onOpen callback data as mentioned above.
JSON
{
 "notificationId": "173049892",
 "licenseCode": "311c48b3",
 "type": "notification",
 "title": "Checkout the new pricing",
 "event": "click",
 "actionLink": "http://webengage.com/pricing",
 "actionText": "Check out",
 "activity": {
 "pageUrl": "http://webengage.net/",
 "pageTitle": "In-site customer Feedback, targeted Surveys & push Notifications for Websites - WebEngage",
 "referrer": "",
 "browser": "Chrome",
 "version": 27,
 "OS": "Windows",
 "country": "India",
 "region": "Maharashtra",
 "city": "Mumbai",
 "ip": "127.0.0.1"
 },
 "customData": {
 "userName" : [ "john" ],
 "gender" : [ "male" ],
 "customerType" : [ "Gold" ],
 "jsessionid" : [ "CB300FEC898236FF9E5A181E468CA6BC" ]
 }
}
Examples of using Notification Callbacks
1. Callback handler when a notification is closed
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.notification.onClose'] = function () {
 var r=confirm("Do you realy want to miss this offer");
 if (r==false){
 return false;
 }
};
Notification Methods
1. webengage.notification.render
This method allows you to overwrite the dashboard settings. It also overwrites the settings provided in
_weq
in the widget code. This method accepts all the
_weq notification configuration properties
and
_weq callbacks
.
Name
Type
Description
options
Object
Notification configuration properties
callbacks
Examples of Render Method
1. Open a notification on click of a button
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.notification.defaultRender'] = false;
_weq['webengage.onReady'] = function () {
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.notification.render();
 };
};
2. Open a notification on page scroll (down)
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.notification.defaultRender'] = false;
_weq['webengage.onReady'] = function () {
 var getScrollPercentage = function () {
 var documentHeight = $(document).height();
 var viewPortHeight = $(window).height();
 var verticlePageOffset = $(document).scrollTop();
 return Math.round(100* (viewPortHeight+verticlePageOffset)/documentHeight);
 }
 var notificationDisplayed = false;
 window.onscroll = function (event) {
 if (!notificationDisplayed && getScrollPercentage() >= 70) {
 webengage.notification.render({ notificationId : '_NOTIFICATION_ID_' }); // invoking webengage.notification.render with specific notification id
 notificationDisplayed = true;
 }
 }
};
Also, notice that we are calling
webengage.notification.render
by passing it notificationId option.
3. Passing Custom Data / Rule Data
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.notification.ruleData'] = { 'categoryCode' '_CATEGORY_CODE_', 'paidCustomer' : true };
_weq['webengage.onReady'] = function () {
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.notification.render({
 'customData' : { 'userId' : '_USER_ID_', 'age' : _AGE_ }
 });
 };
};
4. Popping an alert onClose of a notification
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.onReady'] = function(){
 document.getElementById("_BUTTON_ID_").onclick = function(){
 webengage.notification.render().onClose( function(){
 alert("You have closed the notification");
 });
 };
};
2.
webengage.notification.clear
Clears rendered notification.
Examples of Clear Method
1. Clear a notification on click of a button
JavaScript
var _weq = _weq || {};
_weq['webengage.licenseCode'] = '_LICENSE_CODE_';
_weq['webengage.onReady'] = function () {
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.notification.clear();
 };
};
Updated
7 months ago
Legacy SDK v3
Android SDK
Copy Page
