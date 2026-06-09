# Bulk User/ Event API

- URL: https://docs.webengage.com/docs/bulk-user-api
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

REST API
Bulk User/ Event API
When you have a record of thousands of data then, parsing data one by one can be time-consuming. Hence,
Bulk APIs
are used to process a large amount of data in batches, reducing the time and cost involved.
To know more about how WebEngage tracks users and events, kindly refer to
Tracking Users
and
Tracking Events
documentation.
Sending Bulk Users
METHOD:
POST
URL STRUCTURE:
curl -X POST <HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/bulk-users
AUTHENTICATION:
Bearer <YOUR_API_KEY>
Content-Type:
application/json
🚧
Find your
WebEngage License Code and API Key
Example
cURL
{
 "users": [
 {
 "userId": "johndoe",
 "firstName": "John",
 "lastName": "Doe",
 "birthDate": "1986-08-19T15:45:00-0800",
 "gender": "male",
 "email": "
[email protected]
",
 "phone": "+551155256325",
 "company": "Alphabet Inc.",
 "attributes": {
 "Age": "31",
 "Twitter username": "@origjohndoe86",
 "Dollars spent": 461.93,
 "Points earned": 78732
 }
 },
 {
 "userId": "johndoe",
 "firstName": "John",
 "lastName": "Doe",
 "birthDate": "1986-08-19T15:45:00-0800",
 "gender": "male",
 "email": "
[email protected]
",
 "phone": "+551155256325",
 "company": "Alphabet Inc.",
 "attributes": {
 "Age": "31",
 "Twitter username": "@origjohndoe86",
 "Dollars spent": 461.93,
 "Points earned": 78732
 }
 }
 ]
}
Parameters
Here's a list of all the parameters that can be updated through the API:
Parameter
Type
Description
Is mandatory
userId
String
Identifier for known user.
Either one of
userId
or
anonymousId
is mandatory.
User ID or Anonymous ID can be found on the respective user's profile screen on WebEngage dashboard.
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
will be ignored.
User ID or Anonymous ID can be found on the respective user's profile screen on WebEngage dashboard.
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
Gender of the user.
Can be one of
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
emailOptIn
Boolean
Email subscription preference of the user.
Users who are opted out of this will not receive any communication over email. Users are by default opted in to email.
No
smsOptIn
Boolean
SMS subscription preference the user. Users who are opted out of this will not receive any communication over SMS. Users are by default opted in to SMS.
No
whatsappOptIn
Boolean
WhatsApp subscription preference of the user.
Users who are opted out of this will not receive any communication over WhatsApp. The WhatsApp opt-in is
false
by default and you need to explicitly set it to
true
once you have received the opt-in permission from the user.
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
Custom attributes of the user as key-value pairs. For example:\
{ "isPaidUser": true, "userPlan": "Premium" }
\ These data types are allowed for custom attributes:
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
Return
JSON
{
 "response": {
 "status": "queued"
 }
}
Errors
List of API Error Codes
Sending Bulk Events
METHOD:
POST
URL STRUCTURE:
curl -X POST <HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/bulk-events
AUTHENTICATION:
Bearer <YOUR_API_KEY>
Content-Type:
application/json
Example:
cURL
{
 "events": [
 {
 "userId": "johndoe",
 "eventName": "Added to Cart",
 "eventTime": "2018-09-15T18:29:00-0800",
 "eventData": {
 "Product ID": 1337,
 "Price": 39.8,
 "Quantity": 1,
 "Product": "Givenchy Pour Homme Cologne",
 "Category": "Fragrance",
 "Currency": "USD"
 }
 },
 {
 "userId": "johndoe",
 "eventName": "Added to Cart",
 "eventTime": "2018-09-15T18:29:00-0800",
 "eventData": {
 "Product ID": 1337,
 "Price": 39.8,
 "Quantity": 1,
 "Product": "Givenchy Pour Homme Cologne",
 "Category": "Fragrance",
 "Currency": "USD"
 }
 }
 ]
}
Parameters
Here's a list of all the parameters that can be updated through the API:
Parameter
Type
Description
Is mandatory
userId
String
Identifier for known user.
Either one of
userId
or
anonymousId
is mandatory.
User ID or Anonymous ID can be found on the respective user's profile screen on WebEngage dashboard.
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
will be ignored.
User ID or Anonymous ID can be found on the respective user's profile screen on WebEngage dashboard.
Constraint:
anonymousId
can be of maximum 100 characters.
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
Event attributes as key-value pairs. For example:\
{ "Product ID": 1337, "Category": "Fragrance" }
\ These data types are allowed for custom attributes:
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
Rate Limiting
To prevent abuse and ensure fair usage, the Bulk Event Creation and Update API have a limit of 25 users/events per API call and the rate limit is 500 requests per minute.
Errors
List of API error status codes.
Please feel free to drop in a few lines at
[email protected]
or get in touch with your
Onboarding Manager
if you have any further queries. We're always just an email away!
Updated
7 months ago
GET Survey Responses
Catalog Upload via REST API
Copy Page
