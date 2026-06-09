# Legacy SDK v3

- URL: https://docs.webengage.com/docs/web-v30-sdk
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

SDK Changelogs
Web SDK
Legacy SDK v3
JavaScript API (Version 3.0)
The WebEngage JavaScript API provides interface to WebEngage JavaScript widget sitting on your website and thus allows you to customize its configuration and behaviour. Look at few examples mentioned below -
Overview
WebEngage JavaScript API has two main components. One is at the top widget level and other is at the individual product level.
Widget
- Widget Level Customization - examples of using JavaScript API
Hide WebEngage widget on certain pages of your website
Load the entire widget after a certain time delay
Feedback
- WebEngage Feedback - examples of using JavaScript API
Customize the style and alignment of the feedback tab
Show a different feedback form based on sections of your website
Pre-populate name and email in the feedback form for your signed-in users
Pass your own custom/business data (your user identifier) along with each feedback
many more..
Survey
- WebEngage Survey - examples of using JavaScript API
Show a survey on click of a button
Show a survey when a page is scrolled down to the bottom
Show a survey for visitors who have spent more than 5 minutes on your website
Pass data for custom targeting rules
Pass your own custom/business data (your user identifier) along with survey response for tracking
many more..
Notification
- WebEngage Notification - examples of using JavaScript API
Show a notification on click of a button
Show a notification when a page is scrolled down to the bottom
Show a notification with 50% chances of appearing on a page
Pass data for custom targeting rules
Pass your own custom/business data (your user identifier) along with survey response for tracking
many more..
Widget API
The API must be initialized before making any calls. You will need your WebEngage registered website's licenseCode to initialize the API. If you haven't registered your website, you can
register here
. On successful registration, you will be provided a
one time integration code
which you can place anywhere inside the website's html markup. The best place to put this code is right before the closing body tag
</body>
.
Loading And Initialization
The
one time integration code
will load and initialize the JavaScript API with the available initialization options.
Following is the default
one time integration code
snippet for example.
HTML
<script id="_webengage_script_tag" type="text/javascript">
 /**
 * You can define window.webengageWidgetInit to override code
 * that comes by default with the integration code.
 */
 window.webengageWidgetInit = window.webengageWidgetInit || function(){
 webengage.init( {
 licenseCode : '_LICENSE_CODE_'
 }).onReady(function() {
 webengage.render();
 });
 };
 (function(d){
 var _we = d.createElement('script');
 _we.type = 'text/javascript';
 _we.async = true;
 _we.src = (d.location.protocol == 'https:' ? 'https://ssl.widgets.webengage.com' : 'http://cdn.widgets.webengage.com') + "/js/widget/webengage-min-v-3.0.js";
 var _sNode = d.getElementById('_webengage_script_tag');
 _sNode.parentNode.insertBefore(_we, _sNode);
 })(document);
</script>
This code loads the API asynchronously, so it does not block loading of your web page. This is cautiously done to not impact page load time on your website.
The URLs in the above code are protocol relative. This lets the browser load the API over the same protocol (HTTP or HTTPS) as the parent webpage.
The function assigned to
window.webengageWidgetInit
will run as soon as the API is loaded. All the widget initialization options should be passed in
webengage.init
. Any code, that you want to run after the API is loaded, should be placed within the
webengage.onReady
.
See the
webengage.init
documentation for a complete list of available initialization options.
Methods
webengage.init
The
webengage.init
function initializes the API with the passed initialization options.
Note:
The API must be initialized atleast with the registered license code before making any API call against it.
Example Code:
JavaScript
webengage.init({
 // Specify license code of your domain
 licenseCode : '_LICENSE_CODE_'

 // Delay the API initialization by the time specified here in miliseconds.
 delay : '_TIME_IN_MILI_SEC_'
})
Parameters
Name
Type
Description
initOptions
Object
API Initialization options
Initialization Options
Property
Type
Description
Required
Default
licenseCode
String
Registered license code for the website. You can get it from your WebEngage dashboard if the website registered or register it
here
right now
Yes
null
delay
Number
Delays API initialization with the time specified here in miliseconds
No
0
webengage.onReady
The
webengage.onReady
function ensures the successful initialization of the API. The code that you would like to execute after the API initialization must go inside this function.
Default code:
JavaScript
webengage.onReady(function() {

 // This callback function is executed as soon as the API is initialized.
 // This is the default implementation and it internally invokes rendering
 // of feedback tab, surveys and notification if applicable.
 webengage.render();

});
Parameters
Name
Type
Description
funcToCallOnReady
Function
Function to be executed on API ready
webengage.render
The
webengage.render
method internally invokes rendering of feedback tab, surveys and notification if applicable.
In case of any customization that you would like to do with the Feedback, Surveys or Notifications, there are separate APIs available for individual products - feedback, survey and notification.
See the
feedback
,
survey
and
notification
API documentation for the complete list of available customization options.
Examples
Hide WebEngage widget on certain pages of your website
JavaScript
window.webengageWidgetInit = window.webengageWidgetInit || function(){
 webengage.init( {
 licenseCode : '_LICENSE_CODE_'
 }).onReady(function() {
 var pageUrl = document.location.href;
 //hide widget on Terms and Services page
 if(pageUrl != 'http://www.mywebsite.com/terms'){
 webengage.render();
 }
 });
};
Load the entire widget 4 seconds after the page loads
JavaScript
window.webengageWidgetInit = window.webengageWidgetInit || function(){
 webengage.init( {
 licenseCode : '_LICENSE_CODE_',
 delay : 4000
 }).onReady(function() {
 webengage.render();
 });
};
Feedback API (Deprecated)
The core object of the Feedback API is
webengage.feedback
. Using its API methods, one can render feedback tab with custom style, open the feedback form on click of your own button, render feedback forms based on the feedback category, pass custom data along with each feedback submitted and also allows you to remove the feedback tab if needed. Many more such use cases can be addressed using the below mentioned API methods.
Methods
webengage.feedback.render
This methods creates feedback tab. Also shows feedback form, if needed.
Parameters
Name
Type
Description
options
Object
Feedback customization options
Feedback Customization Options
Property
Type
Description
Default
feedbackButtonAlignment
String
Shows the feedback tab on the left/right side of the webpage. The possible value that you can specify here is
left
or
right
As specified in feedback tab configuration
feedbackButtonTextColor
String
Renders feedback tab text with the specified color. Specify here the hex code of the feedback tab text color you desired. For example pass in hex code
#0000ff
to display feedback tab text in blue color
As specified in feedback tab configuration
feedbackButtonBorderColor
String
Renders feedback tab with the specified border color
As specified in feedback tab configuration
feedbackButtonBackgroundColor
String
Renders feedback tab with the specified background color
As specified in feedback tab configuration
defaultFeedbackCategory
Renders the feedback form based on the feedback category specified here
As specified in feedback category configuration
showAllFeedbackCategories
Boolean
If set to
true
Feedback API renders feedback form with feedback category dropdown menu to let the end users to submit contextual feedbacks. If set to
false
, Feedback API renders feedback form based on the default feedback category specified without any feedback category dropdown menu
true
data
Object
Specify your custom data here in proper JSON format to be submitted along with feedback
null
webengage.feedback.clear
This function removes the feedback tab and form, if shown, from the webpage. It takes no parameters.
Examples
Listing below few common usages of WebEngage Feedback JavaScript API
Customize the style and alignment of the feedback tab
Makes feedback tab appear on the left hand side of the page with colors defined in the arguments.
HTML
<script type="text/javascript">// <![CDATA[
 webengage.onReady(function(){
 //call default renderers for survey and notification
 webengage.survey.render();
 webengage.notification.render();

 //render the feedback tab using following colors
 webengage.feedback.render({
 feedbackButtonAlignment:"left",
 feedbackButtonTextColor:"#FFE4B5",
 feedbackButtonBackgroundColor:"#DEB887",
 feedbackButtonBorderColor:"#8B4513"
 });
 });
// ]]>
</script>
Show a feedback form on click of a button on your page
Instead of using the default feedback tab, you can make the feedback form appear on click of a button/link on your webpage.
HTML
<script type="text/javascript">// <![CDATA[
 webengage.onReady(function(){
 //call default renderers for survey and notification
 webengage.survey.render();
 webengage.notification.render();
 $("button#help-support").click(function(){
 //render the feedback tab as well as form
 webengage.feedback.render({
 showFeedbackForm:true //opens the form
 });
 });
 });
// ]]>
</script>
Show a different feedback form based on sections of your website
One can pre-populate feedback category and show the feedback form loaded with its custom fields. On different section of your website, you can pass default category -
HTML
<script type="text/javascript">// <![CDATA[
webengage.onReady(function(){
 //render the feedback (tab), survey (if any) and notification (if any) by default
 webengage.render();

 //Demo 1: bind the click event of sales-related-query button
 $("button#sales-related-query").click(function(){
 //render the feedback tab
 webengage.feedback.render({
 feedbackButtonTextColor:"#FFFFFF",
 feedbackButtonBackgroundColor:"#87CEEB",
 feedbackButtonBorderColor:"#191970",
 defaultFeedbackCategory:"Sales/pricing related query",
 showAllFeedbackCategories:true,
 showFeedbackForm:true //open the tab
 });
 });

 //Demo 2: bind the click event of apply-for-job button
 $("button#apply-for-job").click(function(){
 webengage.feedback.render({
 feedbackButtonTextColor:"#FFE4B5",
 feedbackButtonBackgroundColor:"#DEB887",
 feedbackButtonBorderColor:"#8B4513",
 defaultFeedbackCategory:"Jobs and hiring",
 showAllFeedbackCategories:false, //don't show the category drop-down
 showFeedbackForm:true
 });
 });
});
//]]></script>
Pre-populate name and email in the feedback form for your signed-in users
HTML
<script type="text/javascript">// <![CDATA[
webengage.onReady(function(){
 // call default renderers for survey and notification
 webengage.survey.render();
 webengage.notification.render();

 // pass name and email fields to feedback.
 // The keys used in the data JSON object should match exactly with your feedback field labels
 webengage.feedback.render({
 data: {
 "Name" : "<?php echo $userName; ?>",
 "Email" : "<?php echo $userEmail; ?>"
 }
 });
 });
// ]]></script>
Pass your own custom/business data (your user identifier) along with each feedback
HTML
<script type="text/javascript">// <![CDATA[
webengage.onReady(function(){
 //call default renderers for survey and notification
 webengage.survey.render();
 webengage.notification.render();

 //render the feedback tab using following colors
 webengage.feedback.render({
 data: {
 userId: <?php echo $userId; ?>,
 category: "<?php echo $userCategory; ?>"
 }
 });
});
// ]]></script>
Survey API
The core object of the Survey API is
webengage.survey
. Using its API methods, one can show a specific survey on click of a button, change survey theme real-time, pass custom data along with each survey response submitted, pass rules data for custom targeting (e.g. shopping cart abandonment) and one can use custom logic to show a survey.
Methods
webengage.survey.render
This method checks the applicable survey on a webpage and shows as per defined configuration - time delay, theme and alignment. The method provides hooks and options to override the default behaviour. One can
pop-up a specific survey
skip the rules defined in the dashboard for a survey
show a survey irrespective whether it has been taken or closed by the site's visitor
render a survey after a time delay different than the configured one
pass custom/business data along with each survey got submitted
pass rule data for custom rules specified in targeting
Parameters
Name
Type
Description
options
Object
Survey customization options
Survey Customization Options
Property
Type
Description
Default
surveyId
String
Renders the survey with the specified surveyId. Checks for its applicability based on the rules defined for this survey
Applicability check is performed based on rules defined
skipRuleExecution
Boolean
If set to
true
, rules defined for the survey are skipped
false
showAllClosedAndTakenSurveys
Boolean
If set to
true
, it shows surveys that have already been taken or closed by the website visitor
false
delay
Number
Delays the survey rendering by the time specified here in miliseconds. It overrides the delay time configured in the targeting rules section for that survey
As specified in the survey rules configuration
data
Object
Specify your custom data in proper JSON format to be submitted along with individual survey response
null
scope
String/Object
A visitor life cycle depends on a long term cookie installed for your site in a browser. Lifecyle of a survey depends on the scope of a visitor. If a survey is closed, it doesn't appear for the visitor in the same browser session. If a survey is submitted, then it doesn't appear for the same visitor at all. If you want a survey to appear in every new browser session irrespective of the survey being taken in a past session, you can define your own scope. In this case, specify scope as SESSION_ID and the lifecycle of a survey remains within the scope of a session id. See examples below -
null
scopeType
String
By defining custom scope, you can make a survey submitted once in that scope. By specifying the scopeType as 'session', you can narrow a scope within that session, making a possibility of a survey appearing multiple times to a visitor per each scope. By specifying the scopeType as 'global', you can make a survey submitted once per each scope value across different browser sessions/visitors
session
webengage.survey.clear
This function can be used to remove the survey pop-up window from a Webpage. It takes no parameters.
Examples
Listing below few common usages of WebEngage Survey JavaScript API
Show a survey on click of a button
Show a survey as pop-up on your website on click of a button/link
HTML
<script type="text/javascript">// <![CDATA[
 webengage.onReady(function(){
 //render the feedback (tab) and survey (if any) by default
 webengage.render();

 //Take Survey: bind the click event of a button to trigger a lead generation survey
 document.getElementById("take-survey").onclick = function(){
 //call the survey renderer
 webengage.survey.render({

 //the survey to invoke
 surveyId:"_LEAD_GENERATION_SURVEY_ID_",

 //ignore targeting-rules for the survey
 skipRuleExecution:true,

 //once a visitor has taken a survey or closed it on your site
 //it doesn't appear again for the same visitor.
 //to make this survey appear irrespective, we can override this behavior by setting "true"
 showAllClosedAndTakenSurveys:true,

 //to keep the user experience intact on your site, WebEngage
 //let's you time-delay the survey. this works great in
 //auto mode. however, while using the API, you'd want the survey
 //to immediately pop upon some user action.
 // "delay" is your friend
 delay:0
 });
 };
 });
//]]></script>
Show a survey on custom/business rules
To show a survey only to repeat customers who signs in to your website after 2 months, you just need to pass these 2 metrics and create a custom rule in the Targeting Rules section of the survey.
HTML
<script type="text/javascript">// <![CDATA[
 webengage.onReady(function(){
 webengage.feedback.render();
 webengage.notification.render();

 //pass business data for custom rules set in targeting section
 webengage.survey.render({
 ruleData: {
 "daysAfterSignedIn" : <?php echo $daysAfterUserLoggedIn; ?>,
 "customerType" : "<?php echo $customerGroup; ?>"
 } 
 });
 });
// ]]></script>
Pass your custom/business data along with individual survey response
You can pass your own business data to identify a survey response and tie it with your own database user. Moreover, you can pass more context to understand user behaviour on your site.
HTML
<script type="text/javascript">// <![CDATA[
 webengage.onReady(function(){
 webengage.feedback.render();
 webengage.notification.render();

 //pass business data for custom rules set in targeting section
 webengage.survey.render({
 data: {
 'userId' : <?php echo $myUserId; ?>,
 'customerType' : '<?php echo $customerGroup; ?>',
 'searchQuery' : '<?php echo ".$_REQUEST['term']." ?>'
 } 
 });
 });
// ]]></script>
Show surveys to a visitor everytime a new browser session starts
By specifying a session_id (some unique identifier for a browser session) as the survey scope with scopeType as 'session', one can make a survey re-appear to a visitor, even if (s)he has closed or submitted it in a previous browser session.
HTML
<script type="text/javascript">// <![CDATA[
 webengage.onReady(function(){
 webengage.feedback.render();
 webengage.notification.render();

 //set custom scope for surveys
 webengage.survey.render({
 'scope' : '_USER_SESSION_ID_',
 'scopeType' : 'session'
 });
 });
// ]]></script>
Show a survey to a visitor every day irrespective (s)he has closed/submitted the same survey.
By specifying a today's date as the survey scope, one can make a survey re-appear to a visitor each day even if he has closed or submitted it.
HTML
<script type="text/javascript">// <![CDATA[
 webengage.onReady(function(){
 webengage.feedback.render();
 webengage.notification.render();

 var today = new Date();
 //set custom scope for surveys
 webengage.survey.render({
 'scope' : {
 'scope' : (today.getDate()+"-"+today.getMonth()+"-"+today.getYear()),
 'scopeType' : 'session',
 'surveyIds' : ["~29aj48l"]
 }
 });
 });
// ]]></script>
Show a survey once to a logged in user from differernt browsers
If one wants a survey to be submitted once per logged in user irrespective of different browser sessions, then specify logged in user's email or userId as the scope with scopeType as 'global'.
HTML
<script type="text/javascript">// <![CDATA[
 webengage.onReady(function(){
 webengage.feedback.render();
 webengage.notification.render();

 //set custom scope for surveys
 webengage.survey.render({
 'scope' : '_USER_EMAIL_',
 'scopeType' : 'global'
 });
 });
// ]]></script>
Notification API
The core object of the Notification API is
webengage.notification
. Using its API methods, one can show a specific notificaton on click of a button, change notification theme real-time, pass custom data along with each notification click that gets recorded, pass rules data for custom targeting (e.g. shopping cart abandonment) and one can use custom logic to show a notification.
Methods
webengage.notification.render
This method checks the applicable notification on a webpage and shows as per defined configuration - time delay, theme and alignment. The method provides hooks and options to override the default behaviour. One can
pop a specific notification
skip the rules defined in the dashboard for a notification
render a notification after a time delay different than the configured one
pass custom/business data along with each notification click
pass rule data for custom rules specified in targeting
Parameters
Name
Type
Description
options
Object
Notification customization options
Notification Customization Options
Property
Type
Description
Default
notificationId
String
Renders the notification with the specified notificationId. Checks for its applicability based on the rules defined for this notification
Applicability check is performed based on rules defined
skipRuleExecution
Boolean
If set to
true
, rules defined for the notification are skipped
false
delay
Number
Delays the notification rendering by the time specified here in miliseconds. It overrides the delay time configured in the targeting rules section for that notification
As specified in the notification rules configuration
data
Object
Specify your custom data in proper JSON format to be recorded along with each notification click
null
webengage.notification.clear
This function removes the notification pop-up window from a Webpage. It takes no parameters.
Examples
Listing below few common usages of WebEngage Notification JavaScript API
Show a notification on click of a button
Pop a notification on your website on click of a button/link
HTML
<script type="text/javascript">// <![CDATA[
webengage.onReady(function(){
 //render the feedback (tab) and notification (if any) by default
 webengage.render();

 //Demo 5: bind the click event of a button to trigger a promotional notification
 document.getElementById("take-lead-notification").onclick = function(){
 //call the notification renderer
 webengage.notification.render({
 //the notification to invoke
 notificationId:"_PROMOTION_NOTIFICATION_ID_",
 //don't worry about targeting-rules for the notification
 //more on what is targeting and why should you use it -
 // http://webengage.com/notification
 skipRuleExecution:true,
 //to keep the user experience intact on your site, WebEngage
 //let's you time-delay the notification. this works great in
 //auto mode. however, while using the API, you'd want the notification
 //to immediately pop upon some user action.
 // "delay" is your friend
 delay:0
 });
 };

 //Demo 6: bind the click event to a button button to pop a system alert notification
 document.getElementById("take-notification").onclick = function(){
 //call the notification renderer
 webengage.notification.render({
 notificationId:"_SYSTEM_ALERT_NOTIFICATION_ID_",
 skipRuleExecution:true,
 delay:0
 });
 };
});
// ]]></script>
Show a notification with 50% chances of appearing on a page
Show a notification with 50% probability of it appearing on a page
HTML
<script type="text/javascript">// <![CDATA[
webengage.onReady(function(){
 //render the feedback (tab) and notification (if any) by default
 webengage.feedback.render();
 webengage.survey.render();
 // range (1 - 100) specifies probability of displaying notification
 var percentChances = 50;
 var randomNumber = Math.floor((Math.random()*(100/percentChances)));
 if (randomNumber === 0) {
 webengage.notification.render();
 }
});
// ]]></script>
Pass your own custom/business data (your user identifier) along with survey response for tracking
You can pass your own business data to identify a visitor who clicked on the notification. Along with your user identifier, you can pass more context to understand user behaviour on your site.
HTML
<script type="text/javascript">// <![CDATA[
 webengage.onReady(function(){
 webengage.feedback.render();
 webengage.survey.render();
 //pass business data for custom rules set in targeting section
 webengage.notification.render({
 data: {
 'userId' : <?php echo $myUserId; ?>,
 'customerType' : '<?php echo $customerGroup; ?>',
 'searchQuery' : '<?php echo ".$_REQUEST['term']." ?>'
 }
 });
 });
// ]]></script>
Pass data for custom targeting rules
To show a notification with discount offer to customers who have more than 2 items in the cart worth more than $100 and haven't yet made a purchase after spending 5 minutes on the page, you just need to pass these two metrics and create a custom rule in the Targeting Rules section of the notification.
HTML
<script type="text/javascript">// <![CDATA[
 webengage.onReady(function(){
 webengage.feedback.render();
 webengage.survey.render();

 //pass business data for custom rules set in targeting section
 webengage.notification.render({
 ruleData: {
 "itemsInCart" : <?php echo $itemsInCart; ?>,
 "cartAmount" : <?php echo $totalCartValue; ?>
 }
 });
 });
// ]]></script>
Updated
7 months ago
Web SDK
Legacy SDK v4
Copy Page
