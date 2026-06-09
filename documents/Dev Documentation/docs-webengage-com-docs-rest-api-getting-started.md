# Getting Started

- URL: https://docs.webengage.com/docs/rest-api-getting-started
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

REST API
Getting Started
REST API allows you to programmatically transfer information over the internet using a predefined schema. WebEngage offers endpoints with specific requirements that perform actions and return data.
🚧
Support for Personal API Keys will be discontinued soon. We recommend migrating to Service Accounts for continued API access.
Know more about
Service Accounts
.
With the WebEngage APIs you can:
Track each user's preferences and their actions as
User Attributes
and
Events
,
respectively.
Get
survey data
from WebEngage.
Pass data to WebEngage from third-party platforms like
LeadSquare, Salesforce,
or any other
CRM/Lead Management system
you're using.
Trigger highly personalized
Transactional campaigns
through
Push, SMS, Web Push, and Email
in your dashboard.
(How it works)
Personalize a
Journey campaign
with real-time data from your servers OR update user details as per their journey experience.
(How it works)
Send
Business Events
data to build
Relays
that enables you to automate product/platform communication.
(How it works)
And much more!
Let's walk you through the basics:
User Authentication
🚧
Important!
REST API calls can be authenticated by using the
key
of only those
Admins_who have _Account Management
and
Update Data
permissions. Please check with the account owner if your API requests return the error,
Unauthorized
.
WebEngage follows
Bearer Authentication Scheme
for API access.
A unique REST API key is automatically created for each
WebEngage Account Admin.
Your
key
acts as the authorization bearer token and must be passed in the header of each API call. The token is valid for the entire lifetime of an Account Admin.
In case your
API key
is accidentally compromised or shared with a third-party, a new key can be requested from your
Customer Success Manager
or by dropping us an email at
[email protected]
.
Getting Your Credentials
As shown below, navigate to
Data Paltform> Integrations > REST API
in your dashboard to access your unique
REST API Key
and
WebEngage Account License Code.
Click to enlarge
License Code:
Replace the placeholder,
YOUR_WEBENGAGE_LICENSE_CODE
in all API calls to build the API endpoint URL for your account. Adding the incorrect code will cause the API call to fail
(indicated by
error code 404
in response).
API Key:
Add it to the
Authorization: Bearer <YOUR_API_KEY>
header (by replacing the placeholder) in all API calls to authenticate the request. Adding the incorrect key or not adding one will cause the call to fail
(indicated by
error code 401
in response).
Example
In the below code snippet, we're calling the
/user
API
to update the
unique User ID, First Name, and Last Name
for a user in WebEngage from an external source.
/user API Sample Request
curl -X POST <HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/users 
 --header 'Authorization: Bearer <YOUR_API_KEY>' 
 --header 'Content-Type: application/json' 
 --data '{
 "userId": "johndoe21#",
 "firstName": "John",
 "lastName": "Doe"
 }'
Thus, we will:
Replace
<HOST>
with the applicable host mentioned
here
to build the resource endpoint URL.
Replace
<YOUR_WEBENGAGE_LICENSE_CODE>
with the respective
account's license code
to build the API resource endpoint.
Replace
<YOUR_API_KEY>
with our
unique API key
to authenticate the API call.
This is what the actual POST API call will look like:
Building /user API Request with Actual API Key, License Code & Host URL
curl -X POST https://api.webengage.com/v1/accounts/va1w264d/users 
 --header 'Authorization: Bearer f414139-3cb9-4ed2-8od3-b8bbae8e7f8xY' 
 --header 'Content-Type: application/json' 
 --data '{
 "userId": "johndoe21#",
 "firstName": "John",
 "lastName": "Doe"
 }'
Revoking API KEY
Team members with roles
Admin, Manager
or any
Custom Role
with
Update Data Management
permission can choose to revoke API Key permissions of a specific team member. This can be done by:
Deleting the user
Changing their role. For more details on how to change the role of the team member or view the role permissions, kindly refer to
Role-Based Access Control
.
👍
Highly Recommended!
If the respective admin's API Key is being used in active API requests, then we highly recommend that you change the authorization bearer token for all API calls and use your API KEY to authenticate the calls.
Failing to do so will cause API call failure (
unauthorized error
). This could potentially disrupt transactional campaign delivery, message personalization, real-time data sync with WebEngage, and much more (depending on your usage of WebEngage APIs).
API Endpoint
<HOST>
All available resources (
/users
,
/events
,
/transaction
,
/survey/response/
) can be accessed over
HTTPS
via the respective URLs listed below. The host URL serves as the parent link of the actual API resource endpoint and differs, depending on the WebEngage data center you're using for your account.
🚧
Please Note
WebEngage API Endpoint
differs for
updating Business Events
, CSV data uploads, and
making API calls through Journeys
. Please refer to the respective docs for more details.
Global Data Center
If your WebEngage dashboard URL starts with
dashboard.webengage.com
, then it means you're using our
Global Data Center.
Please use the following host to access resources via API:
Global Data Center Host
https://api.webengage.com/
India Data Center
If your WebEngage dashboard URL starts with
dashboard.in.webengage.com
, then it means you're using our
India Data Center.
Please use the following host to access resources via API:
India Data Center Host
https://api.in.webengage.com/
Saudi Arabia Data Center
If your WebEngage dashboard URL starts with
dashboard.ksa.webengage.com
, then it means you're using our
Kingdom of Saudi Arabia Data Center.
Please use the following host to access resources via API:
Saudi Arabia Data Center Host
https://api.ksa.webengage.com/
API Call Rate Limit
The default rate limits for each API endpoint is mentioned in the table below. An HTTP response code of 429 would be sent if you exceed these limits.
Endpoint
Rate Limit
User Data
Update
5,000 per minute
Event Data
Update
5,000 per minute
Creating
Business Events
1 per minute
Transactional Campaign API
Request
100 per minute
You will also get the following headers in the response for you to programmatically keep a track of the limits:
Header Name
What It Means
Sample Value
X-RateLimit-Limit
The per minute API rate limit for that endpoint
5000
X-RateLimit-Remaining
How many more requests you can make in that minute
4990
Response
The data can be sent in either
JSON
or
XML
format. To select this, the
format
parameter can be passed in the URL as
json
or
xml
. Data is sent in
JSON
format by default. Any parameters can be passed as
HTTP
query string parameters in the API URLs.
Date
All timestamps are returned in
yyyy-MM-ddTHH:mm:ssZ
format.
👍
Example:
2013-01-26T07:31+0000
Response Container
JSON
{
 "response" : {
 "data" : {
 ...
 },
 "message" : "success",
 "status" : "success"
 }
}
Each API response is wrapped in the main
response
container. It contains the following properties:
status
- Value can be
success
or
error
, depending on the server response.
message
- Explains the reason for the corresponding
status
.
data
- Contains the data for the requested resource.
Error Status Codes
Errors are returned using standard HTTP error code syntax. The response body is always in JSON.
Code
What It Means
How to Resolve
400
Invalid resource/parameters
*Step 1:** Please cross-check that you're using the correct
License Code
as a path parameter in the API resource endpoint.
*Step 2:** Please cross-check that you're accessing a valid WebEngage resource which can be either of the following:
/users
,
/events
,
/transaction
,
/survey/response/
*Step 2:** Please drop in a few lines at
[email protected]
if the issue persists.
401
Invalid authentication/access | Unauthorized access
*Step 1:** Please reach out to
[email protected]
, mentioning the API Key being used. We will help you identify the
Account Admin
to whom the
API Key
in question, belongs.
*Step 2:** Once Identified, go to
Profile > Account Admins
to cross-check if the respective admin has sufficient access permissions to
Account Management
and
Update Data
to authenticate
REST API calls.
*Step 3 (If the Account Admin doesn't have sufficient permissions):** You can edit their access permissions by clicking
Edit > Selecting Account Management and Update Data > Save.
*Step 3 (If the Account Admin has been remove from your WebEngage dashboard):** Please replace the invalid API Key in all active and future API calls with the Key of an admin that has sufficient permissions to authenticate the call.
404
Invalid URL
*Step 1:** Please cross-check if you're using the correct
host
(
as per your WebEngage data center
)
as the parent URL for building the resource endpoint in your API call.
*Step 2:** Please drop in a few lines at
[email protected]
if the issue persists.
Please feel free to drop in a few lines at
[email protected]
in case you have further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
Let's show you how you can:
Track User Properties as User Attributes
Track User Actions as Events
Access On-site Survey Data
Trigger Transactional Campaigns
Copy Page
