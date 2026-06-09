# Tracking Users

- URL: https://docs.webengage.com/docs/ios-tracking-users
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
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
integrate your platforms
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
All user related APIs are part of WebEngage iOS SDK's
WEGUser
object. You get an instance of WebEngage
WEGUser
object as follows:
Swift
Objective-C
let weUser: WEGUser = WebEngage.sharedInstance().user
WEGUser* weUser = [WebEngage sharedInstance].user;
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
Swift
Objective-C
weUser.login("9SBOkLVMWvPX")
[weUser login:@"9SBOkLVMWvPX"];
On Logout
Make sure you call
logout
when the logged-in user logs out, or you do not want to attach any future event, session or user data with this user, until
login
is called again.
Swift
Objective-C
weUser.logout()
//Available >= 3.4.12
[weUser logout];

//Deprecated >= 3.4.12, use login instead
[weUser loggedout];
User Attributes
Several addtional details like a user's name. email address, location and so on can be associated with their user profile. All such details are referred to as
User Attributes
which can be of 2 types -
System User Attributes
and
Custom User Attributes. (All user attributes are tracked for both, anonymous and known users.)
WebEngage provides setters for assigning values against each attribute for your users. These attributes can be used to segment users, configure campaign targeting and personalize messages sent through each channel of engagement.
Each session has its own user attributes that get copied from one session to the next. This is in contrast to event parameters, which may take on different values in each session. For this reason, we recommend that you use user attributes for recording details that don't change with each session or details with which you want to entire session to be associated.
Setting System User Attributes
Please note that the value of
NSString
type attributes vmust be less than 1000 characters long. Additional characters will be truncated.
Email
Swift
Objective-C
weUser.setEmail("
[email protected]
")
[weUser setEmail:@"
[email protected]
"];
Hashed Email
Many businesses are averse to sharing contact details of their users with third-party platforms like WebEngage. This is why, we've made it possible for you to pass encrypted email IDs of your users as the system user attribute
we_hashed_email
.
Swift
Objective-C
weUser.setHashedEmail("144e0424883546e07dcd727057fd3b62")
//(Available >= 3.4.2)
[weUser setHashedEmail:@"144e0424883546e07dcd727057fd3b62"];
You can set up a
private ESP API endpoint
at your end to decrypt the email addresses and pass the data on to your
ESP
for final delivery.
Birth Date
Swift
Objective-C
var comps = DateComponents()
comps.day = 19
comps.month = 08
comps.year = 1996

let date: Date? = Calendar.current.date(from: comps)
weUser.setBirthDate(date)
//(Available >= 3.4.14, use setBirthDate for < 3.4.14)

NSDateComponents *comps = [[NSDateComponents alloc] init];
[comps setDay:19];
[comps setMonth:08];
[comps setYear:1996];

NSDate *date = [[NSCalendar currentCalendar] dateFromComponents:comps];
[weUser setBirthDate:date];
Birth Date in
yyyy-mm-dd
Format
Swift
Objective-C
weUser.setBirthDateString("1986-08-19")
[weUser setBirthDateString:@"1986-08-19"]; //yyyy-mm-dd
Phone Number
Swift
Objective-C
weUser.setPhone("+551155256325")
[weUser setPhone:@"+551155256325"];
🚧
The
NSString
phone
must be in E.164 format, eg. +551155256325, +917850009678.
Hashed Phone Number
Many businesses are averse to sharing contact details of their users with third-party platforms like WebEngage. This is why, we've made it possible for you to pass encrypted phone numbers of your users as the system user attribute
we_hashed_phone
.
Swift
Objective-C
weUser.setHashedPhone("e0ec043b3f9e198ec09041687e4d4e8d")
//(Available >= 3.4.2)
[weUser setHashedPhone:@"e0ec043b3f9e198ec09041687e4d4e8d"];
You can set up a
private SSP API endpoint
at your end to decrypt the phone numbers and pass the data on to your
SSP
for final delivery.
Gender
Swift
Objective-C
weUser.setGender("male")
[weUser setGender:@"male"];
First Name
Swift
Objective-C
weUser.setFirstName("John")
[weUser setFirstName:@"John"];
Last Name
Swift
Objective-C
weUser.setLastName("Doe")
[weUser setLastName:@"Doe"];
Company
Swift
Objective-C
weUser.setCompany("Alphabet Inc.")
[weUser setCompany:@"Alphabet Inc."];
Opt In Status
You can set the subscription preference of your users for
SMS, Web Push, Email and WhatsApp
using
setOptInStatusForChannel
, as shown below.
Swift
Objective-C
weUser.setOptInStatusFor(WEGEngagementChannel.push, status: true)
[weUser setOptInStatusForChannel:WEGEngagementChannelPush status:YES];
WEGEngagementChannel
is an
enum
and can have the following values:
WEGEngagementChannelPush
WEGEngagementChannelInApp
WEGEngagementChannelSMS
WEGEngagementChannelEmail
WEGEngagementChannelWhatsapp
Setting
setOptInStatusForChannel
to false for a particular channel opts the user out of that channel, preventing them from receiving further messages through it.
By default, all users who have shared their email address and phone number are opted in to
Email
and
SMS,
respectively.
WhatsApp opt-in is set to
false
by default. You will need to explicitly set it to
true
as and when users opt into the channel.
(Detailed Read)
Location
To set user location manually, use this method. If
auto location tracking
is enabled, WebEngage SDK will manage location updates on its own. However, you can call this method to set user location if you have disabled auto location tracking, or to manually set the location.
Swift
Objective-C
weUser.setUserLocationWithLatitude(19.0822, andLongitude: 72.8417)
[weUser setUserLocationWithLatitude:@19.0822 andLongitude:@72.8417];
Deleting System User Attributes
You can easily delete
System User Attributes
if you no longer need them. Here's how you can go about it:
Swift
Objective-C
weUser.deleteAttribute("email")
[weUser deleteAttribute:@"email"];
WEGUserProfileAttribute
is an
enum
and can have following values:
User Profile Attribute
Description
WEGUserProfileAttributeEmail
Email
WEGUserProfileAttributeBirthDate
Date of birth
WEGUserProfileAttributeGender
Gender
WEGUserProfileAttributeFirstName
First name
WEGUserProfileAttributeLastName
Last name
WEGUserProfileAttributeCompany
Organization
Setting Custom User Attributes
You can use the
weUser.setAttribute
method of our iOS SDK to track custom attributes for a user.
Guidelines for Tracking User Attributes
Here are a few things to keep in mind:
User Attribute
names are case sensitive and must be less than 50 characters long.
NSString
type attribute values must be less than 1000 characters long. Additional characters will be truncated.
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
are called simple custom user attributes. They can be used to both create user segments as well as to personalize campaigns.
1. NSString Attribute
Swift
Objective-C
weUser.setAttribute("Twitter username", withStringValue: "origjohndoe86")
[weUser setAttribute:@"Twitter username" withStringValue:@"@origjohndoe86"];
2. NSNumber Attribute
Swift
Objective-C
weUser.setAttribute("Points earned", withValue: 78732)
[weUser setAttribute:@"Points earned" withValue:[NSNumber numberWithInteger:78732]];
3. Boolean Attribute
Swift
Objective-C
weUser.setAttribute("Subscribed to email", withValue: true)
[weUser setAttribute:@"Subscribed to email" withValue:[NSNumber numberWithBool:YES]];
4. NSDate Attribute
Swift
Objective-C
var comps = DateComponents()
comps.day = 19
comps.month = 8
comps.year = 1996

let date: Date? = Calendar.current.date(from: comps)
weUser.setAttribute("Last order date", withDateValue: date)
NSDateComponents *comps = [[NSDateComponents alloc] init];
[comps setDay:19];
[comps setMonth:8];
[comps setYear:1996];

NSDate *date = [[NSCalendar currentCalendar] dateFromComponents:comps];
[weUser setAttribute:@"Last order date" withDateValue:date];
Complex Custom User Attributes
User attributes of
NSArray
and
NSDictionary
data types are called complex custom user attributes. As shown below, you can use this data to personalize your campaigns. However, you will not be able to use these data types for creating segments.
Click to enlarge
1. NSArray Attribute
NSArray
values must be one of the
simple
or
complex
attribute types.
Swift
Objective-C
weUser.setAttribute("Brand affinity", withArrayValue: ["Hugo Boss","Armani Exchange", "GAS", "Brooks Brothers"])
[weUser setAttribute:@"Brand affinity" withArrayValue:@[@"Hugo Boss",@"Armani Exchange", @"GAS", @"Brooks Brothers"]];
2. NSDictionary Attribute
Values in the
NSDictionary
must be one of the
simple
or
complex
attribute types.
Swift
Objective-C
let userAddress = ["Flat": "Z-62", "Building": "Pennant Court", "Locality": "Penn Road", "City": "Wolverhampton", "State": "West Midlands", "PIN": "WV30DT"]

weUser.setAttribute("Address", withDictionaryValue: userAddress)
NSDictionary *userAddress=@{
 @"Flat":@"Z-62",
 @"Building":@"Pennant Court",
 @"Locality":@"Penn Road",
 @"City":@"Wolverhampton",
 @"State":@"West Midlands",
 @"PIN":@"WV30DT"
};

[weUser setAttribute:@"Address" withDictionaryValue:userAddress];
Deleting Custom User Attributes
You can easily delete existing
Custom User Attributes
if you no longer need them. Here's how you can go about it:
Swift
Objective-C
weUser.deleteAttribute("Points earned")
weUser.deleteAttributes(["Twitter username", "Subscribed to email", "Points earned"])
[weUser deleteAttribute:@"Points earned"];
[weUser deleteAttributes:@[@"Twitter username", @"Subscribed to email", @"Points earned"]];
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
