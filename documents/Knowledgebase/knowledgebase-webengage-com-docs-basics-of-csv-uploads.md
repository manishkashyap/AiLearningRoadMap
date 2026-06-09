# Basics of CSV Uploads

- URL: https://knowledgebase.webengage.com/docs/basics-of-csv-uploads
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Basics of CSV Uploads
A comprehensive guide for your CSV file requirements and uploading it to WebEngage
Users
Any user profile data on WebEngage has attributes that define a user, such as
First Name, Last Name, Date of Birth, Gender, Score, Membership Type
and so on.
Among the attributes above, there are certain attributes that are predefined by WebEngage such as
First Name, Last Name
, etc. These are called
System Attributes
.
Another set of attributes that are defined by you, for example,
Score
,
Membership Type
, etc, are called
Custom Attributes
.
Please refer to
Users
for more details on the system and custom attributes.
Any User CSV file that a marketer uploads on WebEngage will be a combination of system and custom attributes that define each user.
Let’s look at a tabular representation of a sample User CSV file. If you notice the first row in the table below, you will see that this CSV file has a mix of system attributes (
user_id
,
email
,
phone
,
first_name
,
last_name
) and custom attributes (
score
,
membership_type
).
user_id
email
phone
first_name
last_name
score
membership_type
2123414
[email protected]
+1 925 336 0294
Adam
Smith
20
Gold
2384708
[email protected]
+65 90391135
John
Knowles
10
Silver
In addition to defining specific user attributes as system attributes, WebEngage also has relevant data types assigned to these system attributes (e.g., system attribute
email
is of
String
data type).
📘
Important
While preparing the CSV file, kindly ensure that you use the same attributes and data types to represent the user data.
Please note that you cannot change the name of these system attributes or the corresponding data types.
Following is the list of system attributes and their data types that have been defined by WebEngage and is available for use in CSV file uploads.
List of System Attributes for Users CSV File Upload
📘
You can now update your users time zone!
You can now set or update a user’s time zone in WebEngage using the two attributes:
tz_name
and
tz_offset
. These attributes help ensure that events, journeys, and time-based campaigns are evaluated and delivered in the user’s local time.
System Attribute Name
Data Type
Description
user_id
String
User ID
first_name
String
First name
last_name
String
Last name
birth_date
Date
Birth date in YYYY-MM-DD format
gender
String
Gender - value can only be one of
male
,
female
,
other
.
company
String
Company
country
String
Country
city
String
City
region
String
Region
locality
String
Locality
postal_code
String
Postal Code
email
String
Email ID
phone
String
Phone number of the user in E.164 format
eg. +551155256325, +917850009678
hashed_email
String
Encrypted email address for use with a private ESP (Email Service Provider). This can be a maximum of 512 characters.
See
PII hashing
for more details.
hashed_phone
String
Encrypted email address for use with a private SSP (SMS Service Provider). This can be a maximum of 512 characters.
See
PII hashing
for more details.
email_opt_in
Boolean
If this is set to
false
, Email campaigns will not be sent to the user.
sms_opt_in
Boolean
If this is set to
false
, SMS campaigns will not be sent to the user.
push_opt_in
Boolean
If this is set to
false
, Push campaigns will not be sent to the user.
whatsapp_opt_in
Boolean
If this is set to
false
, WhatsApp campaigns will not be sent to the user.
tz_name
String
Time zone name of the user in IANA format (for example,
Asia/Kolkata
,
America/New_York
). This is used to process time-based actions and campaigns in the user’s local time.
tz_offset
Number
Time zone offset of the user from UTC, expressed in minutes (for example,
330
for UTC+5:30). This helps accurately align event timestamps and campaign delivery times.
In addition to these system attributes, you can define various custom attributes (and their corresponding data types) representing a user. If you have integrated the WebEngage SDK in your mobile apps or website, you might have already defined these custom attributes.
You can check the custom attributes you have already defined on your WebEngage dashboard under the
Data Management > User attributes list
section.
While preparing the User CSV file, you can choose to use the already existing custom attributes, or you could choose to add new custom attributes. Do note that once these custom attributes are recorded in WebEngage, you will not be able to change their name. Therefore, kindly be careful while adding new custom attributes.
Please take note of the following limitations when creating new custom attributes:
Values of an attribute can only be of one of the following data types:
Boolean
,
Number
,
String
, and
Date
.
Map
and
Array
data types are not allowed for CSV uploads.
A user profile can have a maximum of 25 custom attributes per data type for the following data types:
Boolean
,
Number
,
String
,
Date
(i.e. 25 custom attributes of
Number
data type, 25 custom attributes of
String
data type etc.).
The maximum length of a
String
data type for an attribute is 1000 characters.
The maximum length of an attribute name is 50 characters.
The name of your user attribute should not begin with
we_
.
📘
CSV Uploads Are Only for Known Users
Please note that CSV Uploads for Users can be used only to add or update details of known users. You will not be able to add or update the details of any unknown users through CSV uploads.
Events
Events in WebEngage are of the following types. Kindly refer to
Events
for more details.
System Events:
These events are automatically captured by WebEngage as soon as the SDK integration is done, such as
App Install, App Uninstall
, etc.
Campaign Events:
These events are automatically captured by WebEngage, based on the actions your users perform on the campaigns they receive through WebEngage such as
Email Open, Email Click
, etc.
Custom Events:
These events are sent by you to WebEngage, based on the actions performed by your users on your mobile app and/or website. Some examples of these events are:
Purchased, Searched, Added to Wishlist
and so on. You can check the various custom events you are already sending to WebEngage under the
Data Management > Events
section of your dashboard.
📘
Only CSV Files with Custom Events Can Be Uploaded
Please note that you can upload the Events CSV file for
Custom Events
only. The file can contain data about an already existing custom event or a new custom event. Any new custom events created through CSV files will be visible on your list of events section in the WebEngage dashboard under the
Data Management > Events list
section.
A custom event has attributes that describe the event's details - who did the event, where did the event happen, what time did the event happen, etc. Just like
User
attributes, attributes of a
Custom Event
are of two types:
System Attributes
: WebEngage predefines these, and they automatically capture specific details about the event such as time of the event, who did the event, the location where the event happened, etc.
Custom Attributes
: You define these attributes and their data types. For example, a Purchase event could have custom attributes like
Item ID, Item Price, Item Category
, etc.
Any Events CSV file you upload on WebEngage will have a mix of system and custom attributes that define each custom event. Let’s look at a tabular representation of a sample Events CSV file. If you notice the first row in the table below, you will see that this CSV file has a mix of system attributes (
event_name,
user_id,
event_time
) and custom attributes (
product
,
price
,
category
).
event_name
user_id
event_time
product
price
category
add_to_cart
2123414
2018-01-21 10:23:21
iPhone XS
$800
Phone
add_to_cart
2384708
2018-05-18 22:20:00
Inspiron 6000
$549
Laptop
In addition to defining specific event attributes as system attributes, WebEngage has also assigned the relevant data types to these system attributes (e.g., system attribute
event_name
is of
String
data type). When you prepare your Events CSV file, you need to ensure that you use these same attribute names and data types to represent your data. Note that you cannot change the name of these system attributes or the corresponding data types.
Following is the list of system attributes and their data types that have been defined by WebEngage and have to be mandatorily used in uploads of Events CSV files.
List of System Attributes for Events CSV File Upload
System Attribute Name
Data Type
Description
event_name
String
Name of the event
user_id
String
User ID of the user that performed the event
event_time
Date
Time at which the the event occurred in ISO format
📘
System Attributes Not Included for Events CSV Uploads
There are other system attributes as well such as
Country, City, OS, Browser
etc. These are not covered in the list above because you will not be able to use these system attributes in your CSV files.
In addition to these system attributes, you can define various custom attributes (and their corresponding data types) representing a custom event. If you have integrated the WebEngage SDK in your mobile apps or website, you might have already defined these custom attributes. You can check the custom attributes of the custom event you have already defined on your WebEngage dashboard under the
Data Management > Events
section of your dashboard.
When preparing your Events CSV file, you can choose to use the already existing custom attributes or choose to use new custom attributes. Do note that once these custom attributes are recorded in WebEngage, you will not be able to change their name. Therefore, please be careful whenever you add new custom attributes.
Please take note of the following limitations when you’re creating new custom attributes:
Values of an attribute can only be one of the following data types:
Boolean
,
Number
,
String
, and
Date
.
Map
and
Array
data types are not allowed for CSV uploads.
A custom event can have a maximum of 25 custom attributes per data type for the following data types:
Boolean
,
Number
,
String
,
Date
(i.e. 25 custom attributes of
Number
data type, 25 custom attributes of
String
data type, etc.).
The maximum length of an event name is 50 characters.
The maximum length of a
String
data type for an attribute is 1000 characters.
The maximum length of an attribute name is 50 characters.
The name of your event or event attribute should not begin with
we_
.
Updated
5 months ago
So, what's next?
Upload Process
Copy Page
