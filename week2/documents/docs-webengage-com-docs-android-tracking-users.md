# Tracking Users

- URL: https://docs.webengage.com/docs/android-tracking-users
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
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
All user related APIs are part of WebEngage Android SDK's
User
object. You get an instance of WebEngage
User
object as follows.
Java
Kotlin
// Import WebEngage 'User'
import com.webengage.sdk.android.User;

// Get an instance of 'User' object
User weUser = WebEngage.get().user();
// Import WebEngage 'User'
import com.webengage.sdk.android.User;

// Get an instance of 'User' object
val weUser = WebEngage.get().user()
An ID can have of maximum 100 characters.
Once assigned, a user ID cannot be changed.
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
Java
weUser.login("9SBOkLVMWvPX");
On Logout
Make sure that you call
logout
when the user logs out and you don't want to attach any future event, session or user data with this user, until
login
is called again.
Java
weUser.logout();
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
Java
weUser.setEmail("
[email protected]
");
Hashed Email
Many businesses are averse to sharing contact details of their users with third-party platforms like WebEngage. This is why, we've made it possible for you to pass encrypted email IDs of your users as the system user attribute
we_hashed_email
.
Java
weUser.setHashedEmail("144e0424883546e07dcd727057fd3b62");
You can set up an
API endpoint
at your end to decrypt the email addresses and pass the data on to your
Email Service Provider (ESP)
for final delivery.
Birth Date with Year, Month, Day as
Integer
objects
Java
//Deprecated. Use weUser.setBirthDate(String birthDate) instead.
weUser.setBirthDate(1996, 8, 19); // Month is index 1 based: January = 1
Birth Date in
yyyy-mm-dd
Format
Java
weUser.setBirthDate("1986-08-19"); //yyyy-mm-dd
Phone Number
Java
weUser.setPhoneNumber("+551155256325");
🚧
The
String
phoneNumber
must be in E.164 format, eg. +551155256325, +917850009678.
Hashed Phone Number
Many businesses are averse to sharing contact details of their users with third-party platforms like WebEngage. This is why, we've made it possible for you to pass encrypted phone numbers of your users as the system user attribute
we_hashed_phone
.
Java
weUser.setHashedPhoneNumber("e0ec043b3f9e198ec09041687e4d4e8d");
You can set up an
API endpoint
at your end to decrypt the phone numbers and pass the data on to your
SMS Service Provider (SSP)
for final delivery.
Gender
Java
weUser.setGender(Gender.MALE);
🚧
Gender value can be one of
Gender.MALE
,
Gender.FEMALE
or
Gender.OTHER
.
First Name
Java
weUser.setFirstName("John");
Last Name
Java
weUser.setLastName("Doe");
Company
Java
weUser.setCompany("Alphabet Inc.");
Opt In Status
You can set the subscription preference of your users for
SMS, Web Push, Email and WhatsApp
using
setOptIn
, as shown below.
Java
weUser.setOptIn(Channel.PUSH, true);
Channel
is an
enum
and can have four values:
PUSH
,
SMS
,
EMAIL
,
WHATSAPP
. Setting
setOptIn
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
Java
Kotlin
double latitude = 19.0822;
double longitude = 72.8417;
weUser.setLocation(latitude, longitude);
val latitude = 19.0822
val longitude = 72.8417
weUser.setLocation(latitude, longitude)
In addition to these individual setters, you can also set the user profile in one go using Java builder pattern.
Java
Kotlin
weUser.setUserProfile(new UserProfile.Builder()
 .setFirstName("John")
 .setLastName("Doe")
 .setEmail("
[email protected]
")
 .setBirthDate("1986-08-19")
 .setPhoneNumber("+551155256325")
 .setGender(Gender.MALE)
 .setCompany("Alphabet Inc.")
 .setLocation(19.0822, 72.8417)
 .build());
weUser.setUserProfile(
 UserProfile.Builder()
 .setFirstName("John")
 .setLastName("Doe")
 .setEmail("
[email protected]
")
 .setBirthDate("1986-08-19")
 .setPhoneNumber("+551155256325")
 .setGender(Gender.MALE)
 .setCompany("Alphabet Inc.")
 .setLocation(19.0822, 72.8417)
 .build()
 )
Setting Custom Attributes
You can use the
weUser.setAttribute
method of our Android SDK to track custom attributes for a user.
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
Boolean
,
Date
and all subclasses of
Number
are called simple custom user attributes. They can be used to create segments and personalize campaigns.
1. String Attribute
Java
weUser.setAttribute("Twitter username", "@origjohndoe86");
2. Boolean Attribute
Java
weUser.setAttribute("Subscribed to email", true);
3. Long Attribute
Java
weUser.setAttribute("Points earned", 78732);
4. Double Attribute
Java
weUser.setAttribute("Dollars spent", 461.93);
5. Integer Attribute
Java
weUser.setAttribute("Age", 31);
6. Date Attribute
Java
Kotlin
String dateStr = "2017-10-06T09:27:37Z";
SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'");
try {
 Date date = format.parse(dateStr);
 weUser.setAttribute("Last order date", date);
} catch (ParseException e) {
 e.printStackTrace();
}
val format = SimpleDateFormat("yyyy-MM dd'T'HH:mm:ss'Z'")
 try {
 val date: Date = format.parse(dateStr)
 weUser.setAttribute("Last order date", date)
 } catch (e: ParseException) {
 e.printStackTrace()
 }
Complex Custom User Attributes
User attributes of
List
and
Map
data types are called complex custom user attributes. As shown below, you can use this data to personalize your campaigns. However, you will not be able to use these data types for creating segments.
Click to enlarge
1. List Attribute
List
values must be one of the
simple
or
complex
attribute types.
Java
weUser.setAttribute("Brand affinity", Arrays.asList("Hugo Boss", "Armani Exchange", "GAS", "Brooks Brothers"));
2. Map Attribute
You can define multiple user attributes in one go using
Map
. The keys of this
Map
will be attribute names and values will be respective attribute values. These attribute values must be one of the
simple
or
complex
attribute types.
Example 1
Java
Kotlin
Map<String, Object> customAttributes = new HashMap<>();
 customAttributes.put("Age", 31);
 customAttributes.put("Twitter username", "@origjohndoe86";
 customAttributes.put("Subscribed to email", true);
 customAttributes.put("Dollars spent", 461.93);
 customAttributes.put("Points earned", 78732);
 customAttributes.put("Contact Number 1", "+44628976359");
 customAttributes.put("Contact Number 2", "+44776977507");
 customAttributes.put("Address Flat", "Z-62");
 customAttributes.put("Address Building", "Pennant Court");
 customAttributes.put("Address Locality", "Penn Road");
 customAttributes.put("Address City", "Wolverhampton");
 customAttributes.put("Address State", "West Midlands");
 customAttributes.put("Address PIN", "WV30DT");
 
 weUser.setAttributes(customAttributes);
val customAttributes = mutableMapOf<String, Any>()
 customAttributes["Age"] = 31
 customAttributes["Twitter username"] = "@origjohndoe86"
 customAttributes["Subscribed to email"] = true
 customAttributes["Dollars spent"] = 461.93
 customAttributes["Points earned"] = 78732
 customAttributes["Contact Number 1"] = "+44628976359"
 customAttributes["Contact Number 2"] = "+44776977507"
 customAttributes["Address Flat"] = "Z-62"
 customAttributes["Address Building"] = "Pennant Court"
 customAttributes["Address Locality"] = "Penn Road"
 customAttributes["Address City"] = "Wolverhampton"
 customAttributes["Address State"] = "West Midlands"
 customAttributes["Address PIN"] = "WV30DT"
 
 weUser.setAttributes(customAttributes)
Example 2
Java
Kotlin
Map<String, Object> userAddress = new HashMap<>();
userAddress.put("Flat", "Z-62");
userAddress.put("Building","Pennant Court");
userAddress.put("Locality","Penn Road");
userAddress.put("City","Wolverhampton");
userAddress.put("State","West Midlands");
userAddress.put("PIN","WV30DT");

Map<String, Object> customAttributes = new HashMap<>();
customAttributes.put("Address", userAddress);

weUser.setAttributes(customAttributes);
val userAddress: MutableMap<String, Any> = HashMap()
 userAddress["Flat"] = "Z-62"
 userAddress["Building"] = "Pennant Court"
 userAddress["Locality"] = "Penn Road"
 userAddress["City"] = "Wolverhampton"
 userAddress["State"] = "West Midlands"
 userAddress["PIN"] = "WV30DT"

 val customAttributes: MutableMap<String, Any> = HashMap()
 customAttributes["Address"] = userAddress

 weUser.setAttributes(customAttributes)
Deleting Custom User Attributes
You can easily delete existing
Custom User Attributes
if you no longer need them. Here's how you can go about it:
Java
weUser.deleteAttribute("Points earned");
weUser.deleteAttributes(Arrays.asList("Twitter username", "Subscribed to email", "Points earned"));
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
