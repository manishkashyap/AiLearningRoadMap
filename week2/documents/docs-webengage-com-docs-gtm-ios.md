# iOS

- URL: https://docs.webengage.com/docs/gtm-ios
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Partners Integrations
Google Tag Manager
iOS
🚧
Pre-requisites to getting started:
Step 1:
Integrate WebEngage iOS SDK
.
Step 2:
Set up and configure
Google Tag Manager and Firebase
.
1. Install WebEngage's GTM Pod
Update the
Podfile
(in the WebEngage SDK integration) to remove existing WebEngage SDK and include WebEngage's GTM library, as shown below.
Ruby
#Only WebEngageGTM should be added, remove WebEngage from Podfile

target 'MyApp' do
 #pod 'WebEngage'
 pod 'WebEngageGTM'
end
2. User Login and Attributes Setup
🚧
Must Read
We recommend that you get yourself acquainted with all the concepts related to
Users
and
User Attributes
before proceeding. Doing so will help you understand the workings of this section, better.
Here's how you can go about it:
Step 1:
Create a new Tag under
Tags
section and provide a name.
Step 2:
Click on
Tag Configuration
and under
Choose tag type
select
Function Call
.
Step 3:
Provide
WEGSetUserAttributeTag
under
Class Path
section.
Step 4:
Expand
ADD ARGUMENT
section and provide user's system attributes and custom attributes.
List of System User Attributes Defined by WebEngage
Name
Type
Description
we_user_id
String
Unique user identifier
we_first_name
String
User's first name
we_last_name
String
User's last name
we_email
String
User's email address
we_birth_date
String
User’s birth date in
yyyy-mm-dd
format
we_phone
String
User’s phone number in
E.164
format
eg.
+551155256325
we_gender
String
User’s gender (values can only be
male
,
female
or
other
)
we_company
String
User’s company
we_hashed_email
String
Encrypted email address
we_hashed_phone
String
Encrypted phone number
we_push_opt_in
Boolean
if set to
false
, user will not receive push notification on any of his/her device.
we_sms_opt_in
Boolean
If set to
false
, users will be excluded from promotional SMS campaigns.
we_email_opt_in
Boolean
If set to
false
, users will be excluded from promotional email campaigns
Step 5:
Click on
Triggering
section and choose your appropriate trigger on which this Tag should fire.
Click to enlarge
Guidelines for Tracking Custom User Attributes
Here are a few things to keep in mind:
User Attribute
names are case sensitive and must be less than 50 characters long.
String
attribute values must be less than 1000 characters long. Additional characters will be truncated.
You can create a maximum of 25
Custom User Attributes
of each data type.
userAttributeName
must not start with
we_
. Names starting with
we_
are reserved exclusively for internal use at WebEngage. Thus, to avoid data contamination for your account, such data will be ignored if used for your
Custom User Attributes.
The first datapoint synced to WebEngage defines the data type for that user attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Users Attribute
data will stop flowing to your WebEngage dashboard.
3. Event Tracking Setup
🚧
Must Read
We recommend that you get yourself acquainted with the concept of
System Events
,
Custom Events
and their attributes before proceeding. Doing so will help you better understand the workings of this section.
Here are a few
Custom Event Templates
to help you get started
.
Here's how you can go about it:
Step 1:
Create a new Tag under
Tags
section of your GTM account and provide a name.
Step 2:
Click on
Tag Configuration
and under
Tag type
select
Function Call
.
Step 3:
Provide
WEGEventTag
under
Class Path
section.
Step 4:
Expand
ADD ARGUMENT
section and provide key as
event_name
with value being the default built in
Event Name
variable.
Step 5:
Provide rest of the event attributes as arguments to function calls with appropriate data types.
Step 6:
Click on
Triggering
section and choose your appropriate trigger on which this Tag should fire.
Click to enlarge
Guidelines for Tracking Custom Events & Event Attributes
WebEngage sends all events data periodically in batches to minimize network usage and maximize mobile battery life for your users.
Custom Event
and
Custom Event Attribute
names are case sensitive and must be less than 50 characters long.
String
attribute values must be less than 1000 characters long.
eventName
or
eventAttributeName
must not start with
we_
. Names starting with
we_
are reserved exclusively for internal use at WebEngage. Thus, to avoid data contamination for your account, such data will be ignored if used for your
Custom Events.
Custom Event Attributes
can be of these data types:
NSString
,
NSNumber
,
NSDate
,
NSArray
. You can also add
Boolean
attributes since its wrapped type is
NSNumber
.
You can create a maximum of 25
Event Attributes
of each data type for a
Custom Event.
If an
Event Attribute
value is
NSArray
or
NSDictionary
, then it cannot be used to create segments. It can only be used to personalize campaigns.
The first datapoint synced to WebEngage defines the data type for that event attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Event Attribute
data will stop flowing to your WebEngage dashboard.
4. Screen Tracking Setup
Screens are the mobile equivalent of the pages of a website. We highly recommend that you track all the sections of your app as screens to enable contextual
In-app Message targeting.
Further, you can also choose to track specific app-user interactions as
Screen Data
to engage users with an In-app Message whenever they perform a specific action on any app screen.
(
Detailed read
)
Here's how you can go about it:
Step 1:
Create a new tag under
Tags
section and provide a name.
Step 2:
Click on
Tag Configuration
and under
Tag Type
select
Function Call.
Step 3:
Provide
WEGScreenTag
under the section,
Class Path.
Expand the
ADD ARGUMENT
section and add
screen_name
as the
Key
with the
Value
being your custom screen variable.
Repeat these steps to add all your other Key-Value pairs for tracking screen data.
Click to enlarge
🚧
Related Read
Follow this guide to configure advanced integrations
like callbacks and manual push registration for your iOS app.
5. Data Types
WebEngage allows you to track event and user attribute values with different data types. This is similar to Firebase but with a few differences like:
Firebase event parameters don't have a Date data type.
Firebase user properties are always Strings.
To overcome the limitations of Firebase types, WebEngage allows you to change the data type of the argument value before it is tracked to WebEngage. There are no code changes required and you can achieve this by just appending one of the below suffixes in your argument key. WebEngage first tries to convert the value associated with the key to its proper data type (depending on the suffix of the key on the Tag configuration) and then removes the suffix before it is tracked.
👍
For Example
Suppose you have defined a GTM variable
UserAge
of type Event Parameter (or Firebase user property).
Now to track an attribute
age
to WebEngage with data type of Number you need to provide argument key as
age_$number
(see image below)
and the value being the
UserAge
GTM variable.
Click to enlarge
Suffix
Description
_$string
Converts the data type of the value to its appropriate String representation.
For example:
id_$string
_$number
Converts the data type of the value to Number.
For example:
age_$number
passed as "30" will be converted to 30 and
price_$number
passed as "1999.99" will be converted to the number 1999.99
_$boolean
Converts "true" string to true Boolean. Any other string will be converted to false.
For example: "false" -> false
"true" -> true
"False" -> false
"TRUE" -> false
"blah" -> false
_$date
If the value is a String, it is expected to be in ISO date string format
yyyy-MM-ddTHH:mm:ss.SSSZ
for conversion to Date object. For example: "2017-06-01T00:00:00.000Z" will be converted to its appropriate Date type value.
If the value is a Number, it is interpreted as the epoch value in milliseconds. For example: A value of 0 will correspond to the timestamp of midnight 1 January 1970, GMT.
Please feel free to drop in a few lines at
[email protected]
in case you have any queries or feedback. We're always just an email away!
Updated
7 months ago
So, what's next?
Complete the one-time integration to start engaging users!
Push
In-app
SMS
On-site
Web Push
Email
WhatsApp
Facebook
Copy Page
