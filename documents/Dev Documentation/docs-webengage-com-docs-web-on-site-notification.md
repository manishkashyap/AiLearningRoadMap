# On-site Notification

- URL: https://docs.webengage.com/docs/web-on-site-notification
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Website
On-site Notification
Notification Properties
Configuration
You can configure the on-site notification properties as described below.
Property
Type
Description
Default value
notificationId
String
Identify a specific notification using its
notificationId
.
null
skipRules
Boolean
If set to true, targeting rules specified in the dashboard for the active notifications are not executed. Thus, all the active notifications, unless
notificationId
is specified, become eligible to be shown.
false
forcedRender
Boolean
If set to true, the clicked or closed notifications also become eligible to be shown.
false
delay
Number
Time delay, in milliseconds, to show a survey on a page. This overrides the time delay specified on the dashboard while creating the notification.
null
defaultRender
Boolean
If set to
false
, the eligible notification is not displayed by default.
true
customData
Object
Specify your custom data for notification here in
JSON
format to submit along with every notification click. If not set then
webengage.customData
is referred.
null
ruleData
Object
Specify your rule data here in
JSON
format to filter your audience, with the keys you specified on WebEngage dashboard while editing rules for the corresponding notification. If not specified,
webengage.ruleData
is referred.
null
tokens
Object
Specify your tokens data here in
JSON
format. If not specified,
webengage.tokens
is referred.
null
Usage examples
Delay the rendering time of a particular notification.
JavaScript
webengage.notification.options({
 'delay' : 5,
 'notificationId' : '_NOTIFICATION_ID_'
});
Skip rules on a page for notifications.
JavaScript
webengage.notification.options('skipRules', true);
Show a "We are offline" notification every Sunday.
JavaScript
var daysInWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
webengage.notification.options('ruleData', {day : daysInWeek[(new Date()).getDay()]});
🚧
In custom rules section on the targeting page of WebEngage dashboard, you can use the "day" variable to create targeting rules. For example, if the day is "Sunday", you can display a notification on your contact page that your support team is currently offline.
Notification Methods
webengage.notification.render()
This method allows you to override notification settings as configured on WebEngage dashboard. It also overrides any provided
global configuration properties
on the page. This method accepts all
notification configuration properties
.
Usage Examples
Open a notification on click of a button.
JavaScript
webengage.notification.options('defaultRender', false);
webengage.onReady(function(){
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.notification.render();
 };
});
Open a notification on page scroll (down).
JavaScript
webengage.notification.options('defaultRender', false);
var getScrollPercentage = function () {
 var documentHeight = $(document).height();
 var viewPortHeight = $(window).height();
 var verticlePageOffset = $(document).scrollTop();
 return Math.round(100* (viewPortHeight+verticlePageOffset)/documentHeight);
}
var notificationDisplayed = false;
webengage.onReady(function(){
 window.onscroll = function (event) {
 if (!notificationDisplayed && getScrollPercentage() >= 70) {
 webengage.notification.render({ notificationId : '_NOTIFICATION_ID_' }); // invoking webengage.notification.render with specific notification id
 notificationDisplayed = true;
 }
 };
});
🚧
Please scroll down a bit to see this in effect.
Also, note that we are calling
webengage.notification.render
by passing it
notificationId
option
.
Pass custom data / rule data.
JavaScript
webengage.notification.options('defaultRender', false);
webengage.notification.options('ruleData', { 'categoryCode' '_CATEGORY_CODE_', 'paidCustomer' : true });
webengage.onReady(function(){
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.notification.render({
 'customData' : { 'userId' : '_USER_ID_', 'age' : _AGE_ }
 });
 };
});
Pop an alert on closing a notification.
JavaScript
webengage.notification.options('defaultRender', false);
webengage.onReady(function(){
 document.getElementById("_BUTTON_ID_").onclick = function(){
 webengage.notification.onClose(function(){
 alert("You have closed the notification");
 });
 webengage.notification.render();
 };
});
webengage.notification.clear()
This method clears any rendered notification.
Usage Example
Clear a notification on click of a button.
JavaScript
webengage.notification.options('defaultRender', false);
webengage.onReady(function(){
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.notification.clear();
 };
});
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Web Push
On-site Survey
Copy Page
