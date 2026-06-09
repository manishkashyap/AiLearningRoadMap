# On-site Feedback (Deprecated)

- URL: https://docs.webengage.com/docs/web-on-site-feedback
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

On-site Feedback (Deprecated)
Feedback Properties
Configuration
You can configure the on-site feedback properties as described below.
Property
Type
Description
Default value
delay
Number
Time delay, in milliseconds, to show the feedback tab on a page.
null
defaultRender
Boolean
If set to
false
, the feedback tab is not displayed by default.
true
customData
Object
Specify your custom data for feedback here in
JSON
format to submit along with every feedback that gets submitted. If not set then
webengage.customData
is referred.
null
formData
Array of
Object
Specify values in the feedback form for pre-population of the fields. This is illustrated in the examples below.
null
alignment
String
Shows the feedback tab on the left/right side of the webpage. The possible value that you can specify here is
left
or
right
.
As specified in feedback tab configuration on dashboard.
borderColor
String
Renders feedback tab with the specified border color.
As specified in feedback tab configuration on dashboard.
backgroundColor
String
Renders feedback tab with the specified background color.
As specified in feedback tab configuration on dashboard.
defaultCategory
String
Shows the feedback form based on the feedback category specified here.
As specified in feedback tab configuration on dashboard.
showAllCategories
Boolean
If set to
true
, the feedback form appears with feedback category dropdown menu to let the end users submit contextual feedbacks. If set to
false
, the feedback form appears based on the default feedback category specified without any feedback category dropdown menu.
true
showForm
Boolean
If set to
true
, feedback form slides out on page load by default.
false
formData Object
Property
Type
Description
name
String
Label of the field in the feedback form which you want to pre-populate with data, or want to hide, or make it mandatory.
value
String
Specify the value of the field.
mode
String
Specify if the field should be hidden, read-only or default (no-change). Supported values are
hidden
,
readOnly
and
default
.
isMandatory
Boolean
Specify if the field should be mandatory or not.
options
Array of
String
Applicable only in case of ‘Category’ field. Specify in case you want to show specific values in the category dropdown.
Usage examples
Align feedback tab to the right.
JavaScript
webengage.feedback.options('alignment', 'right');
Set feedback tab background and border colors.
JavaScript
webengage.feedback.options({
 'backgroundColor' : '#ff9',
 'borderColor' : '#f99'
});
Pre-populate email field and keep it read-only, hide message and specific options for category drop-down.
JavaScript
// Values in the category drop-down 'Like' & 'Question'

webengage.feedback.options('formData', [
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
]);
Feedback Methods
webengage.feedback.render()
This method allows you to override feedback settings as configured on WebEngage dashboard. It also overrides any provided
global configuration properties
on the page. This method accepts all
feedback configuration properties
.
Usage examples
Show a feedback on click of a button.
JavaScript
webengage.onReady(function(){
 document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.feedback.render({ 'showForm' : true });
 };
});
webengage.feedback.clear()
This method clears any rendered feedback.
Usage Example
Clear a feedback on click of a button.
JavaScript
document.getElementById("_BUTTON_ID_").onclick = function () {
 webengage.feedback.clear();
};
Showing Feedback Widget on Select Pages
You can add the following code snippet to the WebEngage Website SDK to prevent the feedback widget from displaying on select pages.
HTML
<script type="text/javascript">
 var _weq = _weq || {};
 _weq['webengage.onReady'] = function(){
 webengage.notification.render();
 webengage.survey.render();
 var pageUrl = document.location.href;
 //Hide widget on /terms page
 if(pageUrl != 'http://www.mywebsite.com/terms'){
 webengage.feedback.render();
 }
 };
</script>
In the script above, the feedback widget has been disabled for the URL
http://www.mywebsite.com/terms
. Simply replace this URL with links of the pages you would like to disable the feedback widget for, on your website.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Getting Started
Copy Page
