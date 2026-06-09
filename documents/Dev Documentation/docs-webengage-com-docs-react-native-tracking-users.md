# Tracking Users

- URL: https://docs.webengage.com/docs/react-native-tracking-users
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
React Native
Tracking Users
🚧
Must Read
We recommend that you get yourself acquainted with all the concepts related to
Users
and
Events
before proceeding. Doing so will help you understand the workings of this section, better.
Identifying Users
At WebEngage we start detecting users as soon as you
integrate your platform
through our SDKs. Each time a user visits your website, the WebEngage SDK automatically creates a unique ID (LUID) for them. This helps us record users in our backend and create an anonymous profile. All their behavioral data and session data
(
System Events
,
Custom Events
,
System User Attributes
and
Custom User Attributes
)
are stored under the anonymous profile.
You can assign a unique ID (CUID) to each user to identify them. We recommend that you assign a CUID at any of the following moments in their lifeycle:
On signup.
On login.
On page views where user's identity becomes known.
When the user context changes.
Whenever a CUID is assigned to a user it means that:
The user is identified (they become
Known Users
in your dashboard).
A new,
Known User Profile
is created for them that contains all their data.
All their previous anonymous profiles are merged with the new
Known User Profile
to create a single unified view of your users.
(This means that data from their first visit to your website to their latest interactions can all be found under a single user profile!)
👍
How User Profiles are Merged When User is Identified (assigned a CUID by you)
Let's assume that
User A
visits your website a few times before signing up.
User A visits your website on Day 1:
WebEngage assigns them an LUID and automatically creates an anonymous user profile containing all their data
(Anonymous Profile 1).
User A revisits your website on Day 3:
WebEngage assigns them an LUID and creates another anonymous profile to record all their data
(Anonymous Profile 2).
User A revisits your website on Day 7 and creates an account:
On account creation, you can choose to assign the user a CUID. This will lead to the creation of a new user profile.
As soon as the
Known User Profile
is created, WebEngage will run a quick check in it's backend to identify all the existing anonymous user profiles of the user that were created on their previous visits.
In this case,
Anonymous Profile 1
and
Anonymous Profile 2
will be merged with the final profile of
User A
to provide a unified view of their preferences and behavioral history.
Guidelines
Here are a few things to keep in mind when assigning a unique ID (CUID) to identify your users:
All user related APIs are part of WebEngage React Native SDK's
user
object.
An ID can have of maximum 100 characters.
A user ID cannot be changed once it has been assigned.
Although ID can be any
String
that uniquely identifies users in your system, we recommend using system generated user IDs from your database instead of information that can change over time such as email addresses, usernames or phone numbers.
On Login
You can assign an ID by calling the
login
method. All attributes, events and session information accumulated before this API has been called get associated to an anonymous user created by default.
Once
login
is called, all of this stored information is attributed to this identified user.
Make sure you call
login
as soon as the user logs in to your application, or whenever earliest you are able to identify the user.
JavaScript
webengage.user.login('9SBOkLVMWvPX');
On Logout
Make sure you call
logout
when the logged-in user logs out, or you do not want to attach any future event, session or user data with this user, until
login
is called again.
JavaScript
webengage.user.logout();
User Attributes
Several addtional details like a user's name. email address, location and so on can be associated with their user profile. All such details are referred to as
User Attributes
which can be of 2 types -
System User Attributes
and
Custom User Attributes. (All user attributes are tracked for both, anonymous and known users.)
WebEngage provides setters for assigning values against each attribute for your users. These attributes can be used to segment users, configure campaign targeting and personalize messages sent through each channel of engagement.
Each session has its own user attributes that get copied from one session to the next. This is in contrast to event parameters, which may take on different values in each session. For this reason, we recommend that you use user attributes for recording details that don't change with each session or details with which you want to entire session to be associated.
Setting System Attributes
Please note that the value of
String
type attributes must be less than 1000 characters long. Additional characters will be truncated.
Email
JavaScript
webengage.user.setEmail('
[email protected]
');
Hashed Email
Many businesses are averse to sharing contact details of their users with third-party platforms like WebEngage. This is why, we've made it possible for you to pass encrypted email IDs of your users as the system user attribute
we_hashed_email
.
JavaScript
webengage.user.setHashedEmail('144e0424883546e07dcd727057fd3b62');
You can set up a
private ESP API endpoint
at your end to decrypt the email addresses and pass the data on to your
ESP
for final delivery.
Birth Date in
yyyy-mm-dd
Format
JavaScript
webengage.user.setBirthDateString('1986-08-19');
Phone Number
JavaScript
webengage.user.setPhone('+551155256325');
🚧
The
String
we_phone
must be in E.164 format, eg. +551155256325, +917850009678.
Hashed Phone Number
Many businesses are averse to sharing contact details of their users with third-party platforms like WebEngage. This is why, we've made it possible for you to pass encrypted phone numbers of your users as the system user attribute
we_hashed_phone
.
JavaScript
webengage.user.setHashedPhone('e0ec043b3f9e198ec09041687e4d4e8d');
You can set up a
private SSP API endpoint
at your end to decrypt the phone numbers and pass the data on to your
SSP
for final delivery.
Gender
JavaScript
webengage.user.setGender('male');
🚧
Gender values can be one of
male
,
female
or
other
.
First Name
JavaScript
webengage.user.setFirstName('John');
Last Name
JavaScript
webengage.user.setLastName('Doe');
Company
JavaScript
webengage.user.setCompany('Alphabet Inc.');
Opt In Status
You can set the subscription preference of your users for
SMS, Web Push, Email,
and
WhatsApp
using
setOptIn
, as shown below.
JavaScript
webengage.user.setOptIn("push", true);
webengage.user.setOptIn("in_app", true);
webengage.user.setOptIn("email", false);
webengage.user.setOptIn("sms", true);
webengage.user.setOptIn("whatsapp", false);
Setting Custom Attributes
You can use
setAttribute
to track custom attributes for all your users through the WebEngage React Native SDK.
Guidelines for Tracking User Attributes
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
Simple Custom User Attributes
User attributes of the data types
String
,
Number
,
Boolean
and
Date
are called simple custom user attributes. They can be used to both create user segments as well as to personalize campaigns.
1. String Attribute
JavaScript
webengage.user.setAttribute("Category", "GOLD");
2. Number Attribute
JavaScript
webengage.user.setAttribute("Value Index", 5.06);
3. Boolean Attribute
JavaScript
webengage.user.setAttribute("Inactive", false);
4. Date Attribute
JavaScript
webengage.user.setAttribute("Registered On", new Date("1995-12-17T03:24:00").toISOString());
Complex Custom User Attributes
User attributes of
Array
and
Object
data types are called complex custom user attributes. As shown below, you can use this data to personalize your campaigns. However, you will not be able to use these data types for creating segments.
Click to enlarge
1. Array Attribute
Array
values must be one of the
simple
or
complex
attribute types.
JavaScript
webengage.user.setAttribute("Brand affinity", [
 "Hugo Boss",
 "Armani Exchange",
 "GAS",
 "Brooks Brothers"
]);
2. Object Attribute
You can define multiple user attributes in one go using JavaScript
Object
. The keys of this
Object
will be attribute names and values will be respective the attribute values. These attribute values must be one of the
simple
or
complex
attribute types.
Example 1
JavaScript
webengage.user.setAttribute("Address", {
 "Flat" : "Z-62",
 "Building" : "Pennant Court",
 "Locality" : "Penn Road",
 "City" : "Wolverhampton",
 "State" : "West Midlands",
 "PIN" : "WV30DT"
});
Please feel free to drop in a few lines at
[email protected]
or get in touch with your
Onboarding Manager
in case you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
Tracking events
Copy Page
