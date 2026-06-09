# Tracking Users

- URL: https://docs.webengage.com/docs/unity-ios-tracking-users
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Unity.iOS
Tracking Users
Tracking your user's details and preferences as Custom User Attributes to better understand their needs
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
through our SDK. Each time a user visits your website, the WebEngage SDK automatically creates a unique ID (LUID) for them. This helps us record users in our backend and create an anonymous profile. All their behavioral data and session data
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
An ID can have of maximum 100 characters.
Once assigned, a user ID cannot be changed.
Although ID can be any
String
that uniquely identifies users in your system, we recommend using system generated user IDs from your database instead of information that can change over time such as email addresses, usernames or phone numbers.
Login & Logout
You can assign an ID by calling the
login
method. All attributes, events, and session information accumulated before this API has been called get associated with an anonymous user created by default.
Once
login
is called, all of this stored information is attributed to this identified user.
Make sure you call
login
as soon as the user logs in to your application, or whenever earliest you are able to identify the user.
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 ...

 // User login
 WebEngage.Login("userId");

 // User logout
 WebEngage.Logout();
}
Make sure you call
logout
when the logged-in user logs out, or you do not want to attach any future event, session, or user data with this user until
login
is called again.
User Attributes
Several details like a user's name, email address, location, and so on can be associated with their user profile. All such details are referred to as
User Attributes
which can be of 2 types -
System User Attributes
and
Custom User Attributes. (All user attributes are tracked for both, anonymous and known users.)
WebEngage provides setters for assigning values against each attribute for your users. These attributes can be used to segment users, configure campaign targeting, and personalize messages sent through each channel of engagement.
Each session has its own user attributes that get copied from one session to the next. This is in contrast to event parameters, which may take on different values in each session. For this reason, we recommend that you use user attributes for recording details that don't change with each session or details with which you want the entire session to be associated.
Setting Value of System User Attributes
Please note that the value of
String
type attributes must be less than 1000 characters long. Additional characters will be truncated.
First Name
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 // Set user first name
 WebEngage.SetFirstName("John");
}
Last Name
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 // Set user last name
 WebEngage.SetLastName("Doe"); 
}
Email
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 // Set user email
 WebEngage.SetEmail("
[email protected]
");
}
Hashed Email
Many businesses are averse to sharing contact details of their users with third-party platforms like WebEngage. This is why we've made it possible for you to pass encrypted email IDs of your users as the system user attribute
we_hashed_email
.
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 // Set user hashed email
 WebEngage.SetHashedEmail("144e0424883546e07dcd727057fd3b62");
}
You can set up a
private ESP API endpoint
at your end to decrypt the email addresses and pass the data on to your
ESP
for final delivery.
Phone Number
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 // Set user phone number
 WebEngage.SetPhoneNumber("+551155256325");
}
Hashed Phone Number
Many businesses are averse to sharing contact details of their users with third-party platforms like WebEngage. This is why we've made it possible for you to pass encrypted phone numbers of your users as the system user attribute
we_hashed_phone
.
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 // Set user hashed phone number
 WebEngage.SetHashedPhoneNumber("e0ec043b3f9e198ec09041687e4d4e8d"); 
}
Gender
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 // Set user gender, allowed values are ['male', 'female', 'other']
 WebEngage.SetGender("male");
}
Channel Opt-in Status
You can set the subscription preference of your users for
SMS, Web Push, Email, and WhatsApp
as shown below.
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 // Set opt-in status, channels: ['push', 'in_app', 'email', 'sms']
 WebEngage.SetOptIn("push", true);
}
Setting
webengage.SetOptIn
to
false
for a particular channel opts the user out of that channel.
By default, all users who have shared their email address and phone number are opted-in to
Email and SMS,
respectively. All users who have downloaded your app are opted-in to
Push
and
In-app.
WhatsApp
opt-in is set to
false
by default. You will need to explicitly set it to true as and when users opt into the channel.
(Detailed Read)
Users who have opted out of a particular channel will not receive any communication through it.
Birth Date in
yyyy-mm-dd
Format
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 // Set user birth-date, supported format: 'yyyy-mm-dd'
 WebEngage.SetBirthDate("1994-04-29");
}
Company
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 // Set user company
 WebEngage.SetCompany("Google");
}
Location
C#
using WebEngageBridge;
...

public class YourScript : MonoBehaviour
{
 // Set user location
 double latitude = 19.0822;
 double longitude = 72.8417;
 WebEngage.SetLocation(latitude, longitude);
}
Seting Value of Custom User Attributes
You can use
WebEngage.setUserAttribute
to track custom attributes for all your users through the
WebEngage Unity.iOS SDK.
C#
using WebEngageBridge;
 ...
 // Set custom user attributes
 WebEngage.SetUserAttribute("age", 25);
 WebEngage.SetUserAttribute("premium", true);

 // Set multiple custom user attributes
 Dictionary<string, object> customAttributes = new Dictionary<string, object>();
 customAttributes.Add("Twitter Email", "
[email protected]
");
 customAttributes.Add("Subscribed", true);
 WebEngage.SetUserAttributes(customAttributes);
Guidelines
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
Deleting Custom User Attributes
You can easily delete existing
Custom User Attributes
if you no longer need them. Here's how you can go about it:
C#
using WebEngageBridge;
 ...
 
 WebEngage.DeleteUserAttribute("age");
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
