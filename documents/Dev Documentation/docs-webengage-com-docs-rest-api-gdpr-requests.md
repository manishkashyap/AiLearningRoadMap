# GDPR Compliance API

- URL: https://docs.webengage.com/docs/rest-api-gdpr-requests
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

GDPR
GDPR Compliance API
How you can honor your users' GDPR related requests through WebEngage's Rest APIs
WebEngage provides APIs which enable you to comply with the GDPR requests of your users. Using these APIs, you can perform the following actions:
Request to export user data, erase user data, restrict data processing or re-enable processing of user data.
Retrieve the status of a particular GDPR request.
Cancel a particular GDPR request in case it is in the
Pending
state.
POST: /opengdpr_requests
METHOD:
POST
DESCRIPTION:
Export user data, erase user data, restrict data processing or re-enable processing of user data.
URL STRUCTURE:
<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/opengdpr_requests
AUTHENTICATION:
User Authentication
📘
Note
Default rate limit for GDPR API is 100 per minute.
Example
cURL
curl -X POST <HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/opengdpr_requests \
 --header 'Authorization: Bearer <YOUR_API_KEY>' \
 --header 'Content-Type: application/json' \
 --data '{
 "subject_request_id":"a7551968-d5d6-44b2-9831-815ac90177879",
 "subject_request_type":"erasure",
 "subject_identities":[{
 "identity_type":"cuid",
 "identity_value":"1519021150"}]
}'
🚧
Please ensure that you:
Replace
<HOST>
in all the code snippets below with the host mentioned
here
.
Replace
<YOUR_WEBENGAGE_LICENSE_CODE>
with your
WebEngage license code
.
Replace
<YOUR_API_KEY>
with your
WebEngage API key
.
Parameters
JSON
{
 "subject_request_id":"a7551968-d5d6-44b2-9831-815ac90177879",
 "subject_request_type":"erasure",
 "subject_identities":[{
 "identity_type":"cuid",
 "identity_value":"1519021150"}]
}
Parameter
Type
Description
Is mandatory
subject_request_id
String
This should be a unique ID for each request.
Yes
subject_request_type
String
This can be one of the following values:
erasure
: If requesting to delete the user profile.
restriction
: If requesting to restrict the processing of the user profile.
re-enable
: If requesting to re-enable the processing of the user profile.
portability
: If requesting to export the user profile.
Yes
subject_identities
Array
Request for only one user can be placed per API call. This array accepts only one value: User ID of known users which can be found on the user profile page.
Yes
🚧
Important!
Erasure CANNOT be undone. It will PERMANENTLY remove users which may cause discrepancies in your data. Data will be permanently deleted within 30 days of the original request.
If you delete a user by mistake, you can
cancel the request
within 7 days (the request remains in
Pending
state for these 7 days).
Returns
201 Created
JSON
{
 "subject_request_id":"a7551968-d5d6-44b2-9831-815ac90177879",
 "subject_request_type":"erasure",
 "message": "erasure request registered"
}
In case the
subject_request_type
is
portability
, the user's profile is embedded in the response body.
Errors
400 Bad request
: If the JSON body is of incorrect format, the
subject_request_id
is not unique or if the
identity_value
in the request is not a known user's ID.
500 Server error
: Unforeseen service issues.
GET: /opengdpr_requests/{requestId}
METHOD:
GET
DESCRIPTION:
Retrieve the status of a particular GDPR request.
URL STRUCTURE:
<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/opengdpr_requests/{requestId}
AUTHENTICATION:
User Authentication
Example
cURL
curl -X GET <HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/opengdpr_requests/{requestId} \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
--header 'Content-Type: application/json'
🚧
Please ensure that you:
Replace
<HOST>
in all the code snippets below with the host mentioned
here
.
Replace
<YOUR_WEBENGAGE_LICENSE_CODE>
with your
WebEngage license code
.
Replace
<YOUR_API_KEY>
with your
WebEngage API key
.
Returns
200 OK
JSON
{
 "subject_request_id":"a7551968-d5d6-44b2-9831-815ac90177879",
 "subject_request_type":"erasure",
 "status": "PENDING"
}
status
can be one of
PENDING
,
PROCESSING
,
DONE
or
CANCELLED
.
Errors
404 Not Found
: GDPR request not found.
500 Server error
: Unforeseen service issues.
DELETE: /opengdpr_requests/{requestId}
METHOD:
DELETE
DESCRIPTION:
Cancel a particular GDPR request. Request can only be cancelled if it is in the
Pending
state.
URL STRUCTURE:
<HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/opengdpr_requests/{requestId}
AUTHENTICATION:
User Authentication
Example
cURL
curl -X DELETE <HOST>/v1/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/opengdpr_requests/{requestId} \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
--header 'Content-Type: application/json'
🚧
Please ensure that you:
Replace
<HOST>
in all the code snippets below with the host mentioned
here
.
Replace
<YOUR_WEBENGAGE_LICENSE_CODE>
with your
WebEngage license code
.
Replace
<YOUR_API_KEY>
with your
WebEngage API key
.
Returns
200 OK
JSON
{
 "subject_request_id":"a7551968-d5d6-44b2-9831-815ac90177879",
 "subject_request_type":"erasure",
 "message": "request cancelled"
}
If the request is already completed, the response body will convey that with appropriate message.
Errors
400 Bad request
: If the request status is not
Pending
.
404 Not Found
: GDPR request not found.
500 Server error
: Unforeseen service issues.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Understanding GDPR
Web SDK
Copy Page
