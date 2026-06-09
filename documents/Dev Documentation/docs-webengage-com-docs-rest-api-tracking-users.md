# Tracking Users

- URL: https://docs.webengage.com/docs/rest-api-tracking-users
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

REST API
Tracking Users
Learn how to use WebEngage's REST API to create and update user profiles, set user attributes, and track user data effectively.
WebEngage offers APIs for creating and updating users. Both of these operations can be performed using the
/users
endpoint described below
.
🚧
Must Read
We recommend that you get yourself acquainted with all the concepts related to
Users
and
Events
before proceeding. Doing so will help you understand the workings of this section, better.
Identifying Users
At WebEngage we start detecting users as soon as you integrate your platforms through our SDK. Each time a user visits your website, the WebEngage SDK automatically creates a unique ID (Anonymous ID) for them. This helps us record users in our backend and create an anonymous profile. All their behavioral data and session data
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
🚧
You can assign:
Anonymous ID by passing the parameter,
anonymousID
in the request body
described below
.
CUID by passing the parameter,
userId
in the request body
described below
.
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
WebEngage assigns them an anonymous ID and automatically creates an anonymous user profile containing all their data
(Anonymous Profile 1).
User A revisits your website on Day 3:
WebEngage assigns them an anonymous ID and creates another anonymous profile to record all their data
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
that uniquely identifies users in your system, we recommend using system-generated user IDs from your database instead of information that can change over time such as email addresses, usernames, or phone numbers.
User Attributes
Several details like a user's name, email address, location, and so on can be associated with their user profile. All such details are referred to as
User Attributes
which can be of 2 types -
System User Attributes
and
Custom User Attributes. (All user attributes are tracked for both, anonymous and known users.)
WebEngage provides setters for assigning values against each attribute for your users. These attributes can be used to segment users, configure campaign targeting, and personalize messages sent through each channel of engagement.
Each session has its own user attributes that get copied from one session to the next. This is in contrast to event parameters, which may take on different values in each session. For this reason, we recommend that you use user attributes for recording details that don't change with each session or details with which you want the entire session to be associated.
Setting System Attributes
You can set system attributes by passing them as parameters in the request body
described below
.
Setting Custom Attributes
You can set the value of Custom Attributes by passing them as key-value pairs in the
attributes
parameter in the request body
described below
.
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
If the attribute value is
JSON Object
, it cannot be used to create user segments. It can only be used to personalize campaigns.
The first datapoint synced to WebEngage defines the data type for that user attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Users Attribute
data will stop flowing to your WebEngage dashboard.
/users
METHOD:
POST
URL STRUCTURE:
<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/users
AUTHENTICATION:
Bearer Authentication Scheme
DEFAULT API CALL RATE LIMIT:
5,000 per minute
Headers
Name
Description
x-request-id:{HEX_STRING}
Replace
{HEX_STRING}
with a unique random hex string. If API re-attempts are being made, this tag stops propagation of duplicate events within a 4 hour window. Events with same ID re-attempted within 4 hours won't get duplicated if the previous
HTTP
request was able to ingest the event.
EXAMPLE
cURL
curl -X POST <HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/users \
 --header 'Authorization: Bearer <YOUR_API_KEY>' \
 --header 'Content-Type: application/json' \
 --data '{
 "userId": "johndoe",
 "firstName": "John",
 "lastName": "Doe",
 "birthDate": "1986-08-19T15:45:00-0800",
 "gender":"male",
 "email":"
[email protected]
",
 "phone":"+551155256325",
 "company":"Alphabet Inc.",
 "attributes": {
 "Age":"31",
 "Twitter username": "@origjohndoe86",
 "Dollars spent": 461.93,
 "Points earned": 78732
 }
 }'
▶ Run in Postman
🚧
Please ensure that you:
Replace
HOST
with the applicable host mentioned
here
Replace
YOUR_WEBENGAGE_LICENSE_CODE
with your
WebEngage license code
Replace
YOUR_API_KEY
with your
WebEngage API key
Parameters
Here's a list of all the parameters that can be updated through the API:
Parameter
Type
Description
Is mandatory
userId
String
Identifier for known user. Either one of
userId
or
anonymousId
is mandatory. User ID or Anonymous ID can be found on the respective user's profile screen on WebEngage dashboard.
Constraint:
userId
can be of maximum 100 characters.
No
anonymousId
String
Identifier for anonymous user. Either one of
userId
or
anonymousId
is mandatory. In case both IDs are sent,
anonymousId
will be ignored. User ID or Anonymous ID can be found on the respective user's profile screen on WebEngage dashboard.
Constraint:
anonymousId
can be of maximum 100 characters.
No
firstName
String
First name of the user.
No
lastName
String
Last name of the user.
No
birthDate
String
Birth date of the user in ISO format:
yyyy-MM-ddTHH:mm:ss±hhmm
.
No
gender
String
Gender of the user. Can be one of
male
,
female
or
other
.
No
email
String
Email address of the user.
No
phone
String
Phone number of the user.
phone
must be in E.164 format, eg. +551155256325, +917850009678.
No
emailOptIn
Boolean
Email subscription preference of the user. Users who are opted out of this will not receive any communication over email. Users are by default opted in to email.
No
smsOptIn
Boolean
SMS subscription preference the user. Users who are opted out of this will not receive any communication over SMS. Users are by default opted in to SMS.
No
whatsappOptIn
Boolean
WhatsApp subscription preference of the user. Users who are opted out of this will not receive any communication over WhatsApp. The WhatsApp opt-in is
false
by default and you need to explicitly set it to
true
once you have received the opt-in permission from the user.
No
rcsOptIn
Boolean
RCS subscription preference the user. Users who are opted out of this will not receive any communication over RCS. Users are by default opted in to RCS.
No
company
String
Name of the company the user works for.
No
hashedEmail
String
Encrypted email address for use with a private Email Service Provider.
No
hashedPhone
String
Encrypted phone number for use with a private SMS Service Provider.
No
attributes
Object
Custom attributes of the user as key-value pairs. For example:
{ "isPaidUser": true, "userPlan": "Premium" }
These data types are allowed for custom attributes:
String
,
Number
,
Boolean
,
Date
,
JSON Array
JSON Object
.
JSON Object
can contain one of these data types.
No
Returns
JSON
{
 "response": {
 "status": "queued"
 }
}
Errors
List of API error status codes.
JSON
Example: `userId` & `anonymousID` are Missing
{
 "response": {
 "message":"Error: userId and anonymousId cannot be empty.",
 "status":"error"
 }
}
Please feel free to drop in a few lines at
[email protected]
or get in touch with your
Onboarding Manager
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Getting Started
Tracking Events
Copy Page
