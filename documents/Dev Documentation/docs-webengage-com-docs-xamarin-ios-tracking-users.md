# Tracking Users

- URL: https://docs.webengage.com/docs/xamarin-ios-tracking-users
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.iOS
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
All user related APIs are part of WebEngage Xamarin.iOS SDK's
WEGUser
object. You get an instance of WebEngage
WEGUser
object as follows.
C#
// Import WebEngage SDK
using WebEngageXamariniOS;

// Get an instance of 'User' object
User weUser = WebEngage.SharedInstance().User;
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
is called, all of this stored information is attributed to the identified user.
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
type attributes must be less than 1000 characters long. Additional characters will be truncated.
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
Opt In Status
You can set the subscription preference of your users for
SMS, Web Push, Email and WhatsApp
using
weUser.SetOptInStatusForChannel
as shown below.
C#
weUser.SetOptInStatusForChannel(WEGEngagementChannel.Push, true);
WEGEngagementChannel
is an
enum
and can have four values:
Push
,
InApp
,
Sms
,
Email
. Setting
SetOptInStatusForChannel
to
false
for a particular channel opts the user out of that channel.
By default, all users who have shared their email address and phone number are opted in to
Email
and
SMS,
respectively. All users who have downloaded your app are opted-in to
Push
and
In-app.
WhatsApp opt-in is set to
false
by default. You will need to explicitly set it to
true
as and when users opt into the channel.
(Detailed Read)
Users who have opted out of a particular channel will not receive any communication through it.
Location
If
auto location tracking
is enabled, WebEngage SDK will manage location updates on its own. However, you can call this method to set user location if you have disabled auto location tracking, or to set it manually.
C#
NSNumber latitude = 72.5;
NSNumber longitude = 120.5;
weUser.SetUserLocation(latitude, longitude);
Setting Custom Attributes
You can use
SetAttribute
to attach custom attributes to the user, as illustrated in following sections.
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
NSString
,
NSNumber
and
NSDate
are called simple custom user attributes. They can be used to create segments and personalize campaigns.
1. String Attribute
C#
weUser.SetAttribute("Twitter username", "@origjohndoe86");
2. Number Attribute
C#
weUser.SetAttribute("Age", 31);
3. Boolean Attribute
C#
weUser.SetAttribute("Subscribed to email", true);
4. Date Attribute
C#
NSDateComponents dateComponents = new NSDateComponents
 {
 Day = 29,
 Month = 4,
 Year = 2001
 };
NSCalendar calendar = NSCalendar.CurrentCalendar;
NSDate date = calendar.DateFromComponents(dateComponents);
weUser.SetAttribute("Last order date", date);
Complex Custom User Attributes
User attributes of
NSObject
and
NSDictionary
data types are called complex custom user attributes. As shown below, you can use this data to personalize your campaigns. However, you will not be able to use these data types for creating segments.
Click to enalrge
1. NSObject Attribute
NSObject
values must be one of the
simple
or
complex
attribute types.
C#
NSObject[] brandAffinity = { new NSString("Hugo Boss"), new NSString("Armani Exchange"), new NSString("GAS"), new NSString("Brooks Brothers") };
weUser.SetAttribute("Brand affinity", brandAffinity);
2. NSDictionary Attribute
Values in the
NSDictionary
must be one of the
simple
or
complex
attribute types.
C#
NSDictionary<NSString, NSObject> address = new NSDictionary<NSString, NSObject>();
address.SetValueForKey(new NSString("Z-62"), new NSString("Flat"));
address.SetValueForKey(new NSString("Pennant Court"), new NSString("Building"));
address.SetValueForKey(new NSString("Penn Road"), new NSString("Locality"));
address.SetValueForKey(new NSString("West Midlands"), new NSString("State"));
address.SetValueForKey(new NSString("WV30DT"), new NSString("PIN"));
weUser.SetAttribute("Address", address);
Deleting Custom User Attributes
You can easily delete existing
Custom User Attributes
if you no longer need them. Here's how you can go about it:
C#
weUser.DeleteAttribute("Points earned");
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
