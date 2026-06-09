# On-site Survey

- URL: https://docs.webengage.com/docs/web-on-site-survey
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Website
On-site Survey
Survey Properties
Configuration
You can configure the on-site survey properties as described below.
Property
Type
Description
Default value
surveyId
String
Identify a specific survey using its
surveyId
.
null
skipRules
Boolean
If set to true, targeting rules specified in the dashboard for the active surveys are not executed. Thus, all the active surveys, unless
surveyId
is specified, become eligible to be shown.
false
forcedRender
Boolean
If set to true, the submitted or closed surveys also become eligible to be shown.
false
delay
Number
Time delay, in milliseconds, to show a survey on a page. This overrides the time delay specified on the dashboard while creating the survey.
As set on the dashboard
defaultRender
Boolean
If set to
false
, the eligible survey is not displayed by default.
true
customData
Object
Specify your custom data for survey here in
JSON
format to submit along with every survey submission. If not set then
webengage.customData
is referred.
null
ruleData
Object
Specify your rule data here in
JSON
format to filter your audience, with the keys you specified on WebEngage dashboard while editing rules for the corresponding survey. If not specified,
webengage.ruleData
is referred.
null
scope
String
/
Object
A visitor lifecycle depends on a long term cookie installed for your website on a browser. Lifecycle of a survey depends on the scope of a visitor. If a survey is closed, it doesn't appear for the visitor in the same browser session. If a survey is submitted, then it doesn't appear for the same visitor ever again. If you want a survey to appear in every new browser session irrespective of the survey being submitted in a past session, you can define your own scope. In this case, specify scope as
SESSION_ID
and the lifecycle of a survey remains within the scope of a session ID. Refer examples below.
null
scopeType
String
By defining custom scope, you can ensure that a survey is submitted only once in that scope. By specifying the
scopeType
as
session
, you can narrow a scope within that session, making the possibility of a survey appearing multiple times to a visitor per each scope.
By specifying the
scopeType
as
global
, you can make a survey submitted once per each scope value across different browser sessions/visitors.
session
Usage Examples
Pass business data for custom rules.
JavaScript
webengage.survey.options('ruleData', {
 'itemsInCart' : 3,
 'cartAmount' : 1288,
 'customerType' : 'gold'
});
Show surveys to a visitor everytime a new browser session starts.
By specifying a
session_id
(some unique identifier for a browser session) as the survey scope with
scopeType
as 'session', one can make a survey re-appear to a visitor, even if the visitor has closed or submitted it in a previous browser session.
JavaScript
webengage.survey.options({
 'scope' : '_USER_SESSION_ID_',
 'scopeType' : 'session'
});
Show a survey to a visitor every day irrespective of them closing/submitting the same survey.
By specifying today's date as the survey scope, one can make a survey re-appear to a visitor each day even if the visitor has closed or submitted it.
JavaScript
var today = new Date();
webengage.survey.options('scope', {
 'scope' : (today.getDate()+"-"+today.getMonth()+"-"+today.getYear()),
 'scopeType' : 'session',
 'surveyIds' : ["~29aj48l"]
});
Show a survey once to a user logged in from different browsers.
If you want a survey to be submitted once per logged in user irrespective of different browser sessions, then the specify logged in user's email or
userId
as the scope with
scopeType
as
global
.
JavaScript
webengage.survey.options({
 'scope' : '_USER_EMAIL_',
 'scopeType' : 'global'
});
Survey Methods
webengage.survey.render()
This method allows you to override survey settings as configured on WebEngage dashboard. It also overrides any provided
global configuration properties
on the page. This method accepts all
survey configuration properties
.
Usage Examples
Open a survey on click of a button.
JavaScript
webengage.survey.options({
 'surveyId' : '_SURVEY_ID_', // survey id to be rendered ... note : it is optional
 'defaultRender' : false
});
webengage.onReady(function(){
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.survey.render();
 };
});
Open a survey on page scroll (down).
JavaScript
webengage.survey.options({
 'defaultRender' : false
});
(function () {
 var getScrollPercentage = function () {
 var documentHeight = $(document).height();
 var viewPortHeight = $(window).height();
 var verticlePageOffset = $(document).scrollTop();
 return Math.round(100* (viewPortHeight+verticlePageOffset)/documentHeight);
 }
 var surveyDisplayed = false;
 webengage.onReady(function(){
 window.onscroll = function (event) {
 if (!surveyDisplayed && getScrollPercentage() >= 70) {
 webengage.survey.render({ surveyId : '_SURVEY_ID_' }); // invoking webengage.survey.render with specific survey id
 surveyDisplayed = true;
 }
 }
 });
})();
🚧
Please scroll down a bit to see this in effect.
Also, note that we are calling
webengage.survey.render
by passing it
surveyId
option
.
Pass custom data / rule data.
JavaScript
webengage.survey.options({
 'defaultRender' : false
});
webengage.survey.options('ruleData', { 'categoryCode' '_CATEGORY_CODE_', 'paidCustomer' : true });
webengage.onReady(function(){
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.survey.render({
 'customData' : { 'userId' : '_USER_ID_', 'age' : _AGE_ }
 });
 };
});
Track survey view in console.
JavaScript
webengage.survey.options({
 'defaultRender' : false
});
webengage.onReady(function(){
 document.getElementById("_BUTTON_ID_").onclick = function(){
 webengage.survey.render().onOpen( function(){
 console.log("survey open");
 });
 };
});
webengage.survey.clear()
This method clears any rendered survey.
Usage Example
Clear a survey on click of a button.
JavaScript
webengage.onReady(function(){
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.survey.clear();
 };
});
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
On-site Notification
Copy Push to Web Inbox
Copy Page
