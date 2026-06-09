# Users

- URL: https://docs.webengage.com/docs/users
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Overview
Users
📘
At WebEngage, anybody who has interacted with your business at least once is called a
User.
Types of Users
At WebEngage, we automatically start detecting the users across your platforms as soon as they're integrated. These visitors are classified as
Unknown Users
and
Known Users.
Let's walk you through this:
Unknown Users
Each time a new user visits your website or downloads your app, they are tracked as anonymous users in your dashboard and an
Unknown User Profile
is created for them.
The WebEngage SDK automatically assigns them a unique ID (
LUID
) and starts populating their user profile with all their data (
System User Attributes
,
Custom User Attributes
,
System Events
,
Custom Events
).
Known Users
As and when the users share details that help you identify them in your platform, you can assign them a unique ID (
CUID
) to track them as
Known Users.
This user is now stored in our database as the ‘Identified/Registered’ ones. A new user profile is created for them that contains all their data from the previous anonymous user profiles, too merged with the new account.
User Attributes
You can think of user attributes as data points that paint a complete picture of who your user is, where they're from, what they do, and much more, depending on your business. Such granular user data enables you to segment them into contextually relevant segments and personalize campaigns sent through all the channels of engagement.
User Attributes
are classified into 2 categories in WebEngage:
System User Attributes
:
Pre-defined by WebEngage, automatically tracked for all users post-integration.
(However, you will need to call setter functions of the WebEngage SDK to indicate when and what value must be passed against each attribute.)
Custom User Attributes
:
Defined by you for each platform (app, website) and tracked through the respective SDKs.
Let's walk you through this.
System Attributes
We have predefined several generic user details that all digital businesses must track for their users. These details are referred to as
System User Attributes
include information like the user's name, location, channel opt-in status, and so on. Here's how you can
set the value of these attributes
for all your users.
Here's a list of all the
System Attributes
:
System Attribute Name
Data Type of Attribute
What It Tracks
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
Gender which can be one of
male
/
female
/
other
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
Phone number, as shared by the user. eg. +551155256325, +917850009678
hashed_email
String
Encrypted email address of a user (as encrypted and sent by you to your WebEngage account).
Here's how it works.
hashed_phone
String
Encrypted phone number of a user (as encrypted and sent by you to your WebEngae account.
Here's how it works.
email_opt_in
Boolean
Tracks channel opt-in preference of a user.
All users that share their email address are automatically opted-in (value equals 'true').
*If set to
false
by you, then the user will be opted-out and will not receive any promotional Emails from you *(transactional Emails are sent to all users irrespective of their opt-in status)._
sms_opt_in
Boolean
Tracks channel opt-in preference of a user.
All users that share their phone number are automatically opted-in (value equals 'true').
If this is set to
false
by you, then the user will be opted-out and will not receive any promotional SMS campaigns _(transactional messages are sent to all users irrespective of their opt-in status).*
push_opt_in
Boolean
Tracks channel opt-in preference of a user.
All users that download your app and have _Push Notifications_ enabled on their device are automatically opted-in (value equals
true
).
If this is set to
false
by you OR if a user disables _Push Notifications
(value is automatically set to
false
) they will be opted-out and will not receive any promotional campaigns
(transactional notifications are sent to all users irrespective of their opt-in status).
whatsapp_opt_in
Boolean
Tracks channel opt-in preference of a user.
As per
Facebook's guidelines
, a user must explicitly opt-in to receive WhatsApp messages from your business. Thus, all users that share their phone number are opted-out of the channel (value equals
false
).
*As soon as you obtain permission from the user you will need to set the value to
true
to start engaging them through WhatsApp. *(
Detailed Read
)_
rcs_opt_in
Boolean
Tracks channel opt-in preference of a user.
All users who have a phone number and have opted in to receive RCS messages their phone number are automatically opted-in (value equals 'true').
If this is set to
false
by you, then the user will be opted-out and will not receive any promotional RCS campaigns.
Custom Attributes
Custom Attributes
are specific user data that you can custom define and track for all your users. These enable you to understand a user's preferences in the context of your business and deliver contextually personalized experiences in real-time.
Depending on your business, these attributes could be anything like:
RFM Score
|
Lead Score
Language
Membership Type
|
Membership Status
|
Subscription Status
Trial Start Date
|
Trial End Date
|
Trial Days
Country Code
Preferred Genre
Offer Type
and so on.
🚧
Skip to:
How to define & track
Custom Attributes
for your users.
Tracking Users: Concepts
Before we dig into the technicalities, let's quickly get you acquainted with a few crucial concepts and terms related to your WebEngage account.
Click to enlarge
Unique Identifiers
A unique identifier is a piece of information, generally shared by the users themselves, or attributed by you to each user, helping you identify them.
For example, if you define an email address as the unique identifier for your account, then all users who have shared their email address on your app/website will become
Known Users
. And users who are yet to share their email address will be treated as
Unknown Users
.
Thus, you can think of the Unique Identifier as a unique tag or piece of information that you can associate with each user. This could be anything like their email address, phone number, platform userID, or an ID generated in your backend. Each time we receive this piece of information from your platforms, we:
Create a Known User Profile for the user and merge all their historical data (from the unknown profile created when they first landed on your platform).
Assign them a unique
CUID
. This enables us to map all their devices and channel-platform interactions to a single profile - providing you with a 360-degree view.
CUID & LUID
LUID
All users who visit your app/website as guests are assigned a unique ID by WebEngage. This enables us to track all their devices, activities, and details under an
Unknown User Profile
. Thus, a user could be assigned multiple LUIDs over their entire lifetime if they log out or interact with your app/website through new devices as guests.
CUID
This is a unique ID that is assigned by you to a user whenever they signup or perform an action that enables you to identify them. Once assigned, the CUID is shown as the default user ID for all
Known Users
across your dashboard and cannot be changed.
Function of CUID & LUID
Every user is assigned a new LUID each time they visit the app/web from a new device. This way, all their activities will be tracked anonymously in a new ‘Unknown User’ profile with all the data tracking points possible at that level.
Now, as soon as the user fulfills that criteria to qualify as a ‘
Known User
’ (by signing up/logging in), they will be assigned a one-time CUID and will then map their LUID to the CUID to make sure all the past data points captured anonymously are now merged to their new ‘Known User’ profile. In doing so, you will be able to pass a Unique Identifier to the user.
Also, note that the user can have several LUIDs in the past, but a CUID is a one-time token and will be only assigned to a ‘Known User’ profile just once in their lifetime.
👍
Let’s understand it through this simple user journey:
Day 1:
The user downloads the app on his phone and starts browsing without logging in or sharing any other details. Then they will be assigned an LUID, and an unknown user profile will be created.
Day 2:
The user comes back on the app, but this time, from their iPad and does not log in or share any other details again. This user will again be assigned with a new LUID.
Day 3:
The user again comes on the app from their iPad and performs a KPI action through which their identity is revealed, like - making a purchase, signing up on the app, or any action that can be essential for their identity to be known. Once the user performs any of these actions, a CUID is immediately assigned to their profile and now is recognized as a ‘Known User’ profile.
On assigning the CUID, WebEngage also passes a one-time Unique Identifier against the user profile which remains constant for that user for a lifetime. Now, with the passing of the CUID, the system will also track the latest LUID attributes assigned to the profile before the CUID was assigned, and hence all past data before that session will be merged and populated against the same ‘Known User’ profile now.
Tracking Users: How It Works
Now let's get you acquainted with all the ways in which you can track the preferences of all your users (Known & Unknown), and assign an identity to all anonymous users as and when they share their personal details!
Identifying Users
You can identify your users by calling the
login
function of the WebEngage platform SDKs and assigning them a unique CUID. Depending on your business, you can choose to call this function in moments where the user's identity becomes known, like Signup, Login, Purchase, and so on.
Here are a few guidelines to help you get started:
An ID can have of maximum 100 characters and cannot be changed once assigned to a user.
Although the ID can be any
String
value that uniquely identifies users in your system, we recommend using system-generated IDs from your database instead of information that can change over time such as email address, username, or phone number.
🚧
Please Refer to the Respective SDK Functions to Identify Your Users
Web
Android
iOS
React Native
Cordova/ Phone Gap/ Ionic
Xamarin.Android
Xamarin.iOS
Unity.Android
Unity.iOS
Setting Attribute Values
You can call certain setter functions of the WebEngage platform SDKs to set the value of
System Attributes
and
Custom Attributes
for each user. This enables you to segment users and deliver contextually personalized messages through all the channels of engagement.
Here are a few guidelines to help you create and track
Custom User Attributes
:
Custom User Attribute
names are case sensitive and must be less than 50 characters long.
String
attribute values must be less than 1000 characters long. Any characters beyond that will be truncated.
Values of attributes can be of one of
Boolean
,
Number
,
String
,
Date
,
Map
and
Array
. You can create a maximum of 25
Custom User Attributes
of each data type.
A user profile can have as many attributes of
Map
and
Array
data types as you would like with the limitation that all the values together occupy a maximum space of 16KB.
Custom User Attribute
names must not start with
we_
. Names starting with
we_
are reserved exclusively for internal use at WebEngage. Thus, to avoid data contamination for your account, such data will be ignored if used for your attributes.
The first datapoint synced to WebEngage defines the data type for that user attribute. Thus, please ensure that the attribute names and data types are consistent across all your different platforms.
For example, if you have defined
score
to be a
Number
attribute, then please ensure that all your sources -
Android, iOS
, and
Website
are sending values of this attribute as a
Number
. If WebEngage receives data in a different data type from what was first defined, then we will not be able to record this data.
🚧
Please Refer to the Respective SDK Functions to Set Values of User Attributes
Web
Android
iOS
React Native
Cordova/ Phone Gap/ Ionic
Xamarin.Android
Xamarin.iOS
Unity.Android
Unity.iOS
(You will need to intergate the respective platforms with WebEngage before you start tracking user attributes.)
Updated
7 months ago
So, what's next?
Let's walk you through behavioral data, aka. Events, and how you can track it.
Events
Copy Page
