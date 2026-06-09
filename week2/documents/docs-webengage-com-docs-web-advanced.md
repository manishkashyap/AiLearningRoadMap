# Advanced

- URL: https://docs.webengage.com/docs/web-advanced
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Website
Advanced
Global On-site Widget Properties
Configuration
You can configure your WebEngage SDK integration at the global level using
webengage.options
method with the properties described below.
Property
Type
Description
Default
language
String
Static messages present in your feedback/survey form will appear in the language specified here.
Should only be set at the time of initializaiton. Changing this property later will have no effect.
As configured on WebEngage dashboard
delay
Number
Delays SDK initialization for the time specified (in miliseconds)
Should only be set at the time of initializaiton. Changing this property later will have no effect.
0
defaultRender
Number
If set to
false
, then by default on initialization, none of the on-site widgets (feedback, survey and notificaton) are enabled and do not appear. To stop rendering selective widgets, set the
defaultRender
option at the respective widget level, for example,
webengage.survey.options('defaultRender', false)
.
true
customData
Object
DEPRECATED
Use
webengage.screen
instead. Specify your custom data here in proper JSON format to submit along with every survey / feedback submission and notification click
null
ruleData
Object
DEPRECATED
Use
webengage.screen
instead. Specify your rule data here in proper JSON format. The keys should match with the values used in Targeting rules section for the corresponding survey or notification
null
tokens
Object
DEPRECATED
Use
webengage.screen
instead. Specify your tokens data here in proper JSON format
null
Usage Examples
Load WebEngage after 5 seconds.
JavaScript
webengage.options('delay', 5000);
Hide WebEngage by default on mobile phones and tablets.
JavaScript
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
 webengage.options('defaultRender', false);
}
WebEngage Methods
webengage.onReady
Any code that you want to run after WebEngage is loaded and initialized should be provided as a callback to
webengage.onReady
.
Usage Example
Show a survey on click of a button instead of default rendering
JavaScript
webengage.survey.options('defaultRender', false);
webengage.onReady(function(){
 document.getElementById('_BUTTON_ID_').onclick = function () {
 webengage.survey.render();
 };
});
webengage.reload
In single-page applications (SPAs) the page does not load often. Instead, a page view change is mimicked either using
history.pushState()
or hash change. Each of these SPA view changes should be ideally thought of as different page views and tracked likewise.
WebEngage automatically initializes and tracks page view on full page loads but not on in-page SPA view changes. You can use
webengage.reload()
to inform the SDK of such view changes.
Usage Example
Reinitialize WebEngage on SPA view changes, assuming the SPA has implemented 'hash change' view changes
JavaScript
function reload () {
 webengage.onReady(function() {
 webengage.reload();
 });
}

if (window.attachEvent) {
 window.attachEvent('onhashchange', function() {
 reload();
 });
} else if (window.addEventListener) {
 window.addEventListener('hashchange', function() {
 reload();
 });
}
webengage.screen
You can use the
screen
method to pass any contextual information on the current page. Both of its two arguments (screen
name
and object of properties,
data
) are optional. This data:
Will be recorded with the submission of a survey or feedback or click activation of a notification.
Can be used in targeting rules.
Can contain personalized values for placeholders (called tokens) in notifications.
JavaScript
webengage.screen([name], [data])
Usage example
Pass your own business data for inclusion in survey reports.
JavaScript
webengage.screen('Dassler Premium Ice-cream', { 'currentProductId' : '2947APW09', 'price' : 210, 'isDiscounted' : false });
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Callbacks
AMP
Copy Page
