# Tracking Events

- URL: https://docs.webengage.com/docs/rest-api-tracking-events
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

REST API
Tracking Events
Learn how to track custom events through WebEngage's REST API. Create custom events to track crucial user interactions with detailed event attributes for personalized campaigns.
WebEngage offers API for tracking
Custom Events
through the
/events
endpoint described below
.
🚧
Must Read
We recommend that you get yourself acquainted with the concept of
System Events
,
Custom Events
and their attributes before proceeding. Doing so will help you better understand the type of
Events
that can be created through our APIs.
Here are a few
Custom Event Templates
to help you get started
.
WebEngage starts tracking some events as soon as you integrate your platforms through our SDK. These are called
System Events
and track some generic user interactions with your app and campaigns.
You can create
Custom Events
to track any other user interactions that are crucial for your business. Each
Custom Event
can further be defined by
Event Attributes
like
price, quantity, category
and so on. Such granular data enables you to engage users through highly contextual and personalized campaigns through all the
channels of engagement
.
Guidelines for Tracking Custom Events
Here are a few things to keep in mind:
Custom Event
names must be less than 50 characters long.
Custom Event Attribute
names are case sensitive and must be less than 50 characters long.
String
attribute values must be less than 1000 characters long.
These data types are allowed for event attributes:
String
,
Number
,
Boolean
,
Date
,
JSON Array
,
JSON Object
.
JSON Object
can contain only one of these data types.
eventName
or
eventAttributeName
must not start with
we_
. Names starting with
we_
are reserved exclusively for internal use at WebEngage. Thus, to avoid data contamination for your account, such data will be ignored if used for your
Custom Events.
You can create a maximum of 25
Event Attributes
of each data type for a
Custom Event.
If the event attribute value is
JSON Object
, it cannot be used to create user segments. It can only be used to personalize campaigns.
The first datapoint synced to WebEngage defines the data type for that event attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Event Attribute
data will stop flowing to your WebEngage dashboard.
/events
METHOD:
POST
URL STRUCTURE:
<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/events
AUTHENTICATION:
Bearer Authentication Scheme
DEFAULT API CALL RATE LIMIT:
5,000 per minute
You cannot create
System Events
using the WebEngage API.
Here's a list of the
System Events
that are automatically tracked by WebEngage.
Please avoid creating
Custom Events
of the same name as that of
System Events
through the API to avoid confusion.
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
JSON
curl -X POST <HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/events \
 --header 'Authorization: Bearer <YOUR_API_KEY>' \
 --header 'Content-Type: application/json' \
 --data '{
 "userId": "johndoe",
 "eventName": "Added to Cart",
 "eventTime": "2018-09-15T18:29:00-0800",
 "eventData": {
 "Product ID": 1337,
 "Price": 39.80,
 "Quantity": 1,
 "Product": "Givenchy Pour Homme Cologne",
 "Category": "Fragrance",
 "Currency": "USD"
 }
}'
►
Run in Postman
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
Note:
Passing both userId and anonymousId will not merge the unknown user into known user.
No
eventName
String
Name of the event.
Yes
eventTime
String
Date and time when the event occurred in ISO format:
yyyy-MM-ddTHH:mm:ss±hhmm
.
No
eventData
String
Event attributes as key-value pairs. For example:
{"Product ID": 1337, "Category": "Fragrance"}
. These data types are allowed for custom attributes:
String
,
Number
,
Boolean
,
Date
,
JSON Array
,
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
Tracking Users
Transactional Campaign API
Copy Page
