# Tracking Users

- URL: https://docs.webengage.com/docs/xamarin-android-tracking-users
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.Android
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
All user related APIs are part of WebEngage Xamarin.Android SDK's
User
object. You get an instance of the WebEngage
User
object as follows.
C#
// Import WebEngage SDK
using Com.Webengage.Sdk.Android;

// Get an instance of 'User' object
User weUser = WebEngage.Get().User();
An ID can have of maximum 100 characters.
Once assigned, a user ID cannot be changed.
Although ID can be any
String
that uniquely identifies users in your system, we recommend using system generated user IDs from your database instead of information that can change over time such as email addresses, usernames or phone numbers.
On Login
You can assign an ID by calling the
Login
method. All attributes, events and session information accumulated before this API has been called get associated to an anonymous user created by default.
Once
Login
is called, all of this stored information is attributed to this identified user.
Make sure you call
Login
as soon as the user logs in to your application, or whenever earliest you are able to identify the user.
C#
weUser.Login("9SBOkLVMWvPX");
On Logout
Make sure you call
Logout
when the logged-in user logs out, or you do not want to attach any future event, session or user data with this user, until
Login
is called again.
C#
weUser.Logout();
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
type attribute values must be less than 1000 characters long. Additional characters will be truncated.
Email
C#
weUser.SetEmail("
[email protected]
");
Hashed Email
Many businesses are averse to sharing contact details of their users with third-party platforms like WebEngage. This is why, we've made it possible for you to pass encrypted email IDs of your users as the system user attribute
we_hashed_email
.
C#
weUser.SetHashedEmail("144e0424883546e07dcd727057fd3b62");
You can set up an
API endpoint
at your end to decrypt the email addresses and pass the data on to your
Email Service Provider (ESP)
for final delivery.
Birth Date in
yyyy-mm-dd
Format
C#
weUser.SetBirthDate("1986-08-19");
Phone Number
C#
weUser.SetPhoneNumber("+551155256325");
🚧
The phone number must be passed in E.164 format, eg. +551155256325, +917850009678.
Hashed Phone Number
Many businesses are averse to sharing contact details of their users with third-party platforms like WebEngage. This is why, we've made it possible for you to pass encrypted phone numbers of your users as the system user attribute
we_hashed_phone
.
C#
weUser.SetHashedPhoneNumber("e0ec043b3f9e198ec09041687e4d4e8d");
You can set up an
API endpoint
at your end to decrypt the phone numbers and pass the data on to your
SMS Service Provider (SSP)
for final delivery.
Gender
C#
weUser.SetGender(Gender.Male);
🚧
Gender value can be one of
Gender.Male
,
Gender.Female
or
Gender.Other
.
First Name
C#
weUser.SetFirstName("John");
Last Name
C#
weUser.SetLastName("Doe");
Company
C#
weUser.SetCompany("Alphabet Inc.");
Setting Custom Attributes
You can use
SetAttribute
to track custom attributes for a user.
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
User attributes of
String
,
Java.Lang.Boolean
,
Java.Util.Date
and
Java.Lang.Number
data types are called simple custom user attributes. They can be used to create segments and personalize campaigns.
1. String Attribute
C#
weUser.SetAttribute("Twitter username", "@origjohndoe86");
2. Number Attribute
C#
using Java.Lang;
...

weUser.SetAttribute("Age", (Integer)31);
3. Boolean Attribute
C#
using Java.Lang;
...

weUser.SetAttribute("Subscribed to email", (Boolean)true);
4. Date Attribute
C#
using Java.Lang;
...

weUser.SetAttribute("Last order date", new Date("21-07-2018"));
Complex Custom User Attributes
User attributes of
IList
and
IDictionary
data types are called complex custom user attributes. As shown below, you can use this data to personalize your campaigns. However, you will not be able to use these data types for creating segments.
Click to enlarge
1. IList Attribute
IList
values must be one of the
simple
or
complex
attribute types.
C#
using Java.Lang;
using System.Collections.Generic;
...
 
IList<Object> brandAffinity = new List<Object>
 {
 "Hugo Boss",
 "Armani Exchange",
 "GAS",
 "Brooks Brothers"
 };
weUser.SetAttribute("Brand affinity", brandAffinity);
2. IDictionary Attribute
You can define multiple user attributes in one go using
IDictionary
. The keys of this
IDictionary
will be attribute names and values will be respective attribute values. These attribute values must be one of the
simple
or
complex
attribute types.
Example 1
C#
using System.Collections.Generic;
using Java.Lang;
using Android.Runtime;
...

JavaDictionary<string, Object> address = new JavaDictionary<string, Object>
{
 { "Flat", "Z-62" },
 { "Building", "Pennant Court" },
 { "Locality", "Penn Road" },
 { "City", "Wolverhampton" },
 { "State", "West Midlands" },
 { "PIN", "WV30DT" }
};
IDictionary<string, Object> customAttributes = new Dictionary<string, Object>();
customAttributes.Add("Address", address);

weUser.SetAttributes(customAttributes);
Example 2
C#
using Com.Webengage.Sdk.Android;
...

weUser.DeleteAttribute("Points earned");
Deleting Custom User Attributes
You can easily delete existing
Custom User Attributes
if you no longer need them. Here's how you can go about it:
C#
IDictionary<string, Object> customAttributes = new Dictionary<string, Object>();
customAttributes.Add("Age", 31);
customAttributes.Add("Twitter username", "@origjohndoe86";
customAttributes.Add("Subscribed to email", true);
customAttributes.Add("Dollars spent", 461.93);
customAttributes.Add("Points earned", 78732);
customAttributes.Add("Contact Number 1", "+44628976359");
customAttributes.Add("Contact Number 2", "+44776977507");
customAttributes.Add("Address Flat", "Z-62");
customAttributes.Add("Address Building", "Pennant Court");
customAttributes.Add("Address Locality", "Penn Road");
customAttributes.Add("Address City", "Wolverhampton");
customAttributes.Add("Address State", "West Midlands");
customAttributes.Add("Address PIN", "WV30DT");

weUser.SetAttributes(customAttributes);
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
