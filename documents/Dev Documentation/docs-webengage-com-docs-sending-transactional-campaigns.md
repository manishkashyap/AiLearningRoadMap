# Transactional Campaign API

- URL: https://docs.webengage.com/docs/sending-transactional-campaigns
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

REST API
Transactional Campaign API
A step-by-step guide to setting up the WebEngage Transactional Campaign API for your business
WebEngage's Transactional Campaign API
enables you to send critical transactional messages to your users such as
order confirmations, shipping details, payment invoices
and so on through the channels of
Push, SMS, Email, Web Push
and
WhatsApp.
(Detailed read on how transactional campaigns work)
​
Please note that this API can be used only for triggering
Transactional
campaigns which are in
Running
state i.e., the campaign needs to be launched on the WebEngage dashboard before you call this API.
Here's a quick overview of how it works:
/transaction
METHOD:
POST
URL STRUCTURE:
<HOST>/v2/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/experiments/<EXPERIMENT_ID>/transaction
AUTHENTICATION:
Bearer Authentication Scheme
DEFAULT API CALL RATE LIMIT:
100 per minute
EXAMPLE
cURL
curl -X POST \
 '<HOST>/v2/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/experiments/<EXPERIMENT_ID>/transaction' \
 -H 'Authorization: Bearer <YOUR_API_KEY>' \
 -H 'Content-Type: application/json' \
 -d '{
 "ttl": 1200,
 "dedupe": {
 "ttl": 1800
 },
 "userId": "peter",
 "overrideData": {
 "context": {
 "token": {
 "name": "Peter",
 "orderId": "ABCD1234"
 }
 }
 }
}'
🚧
Please ensure that you:
Replace
<HOST>
with the host mentioned
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
Replace
<EXPERIMENT_ID>
with the ID of the campaign which you would like to trigger via this API.
Finding a Campaign's ID in Dashboard
Step 1:
Go to the
Channel
& click on the campaign's name in the
List of Campaigns.
Step 2:
Click
Show Details
on the top right of the
Campaign's Overview.
As shown below, you will find the
Campaign ID
amongst other details. Please note that your campaign ID might start with tilde (
~
).
Click to enlarge
Parameters
Here's a list of all the parameters that can be updated through the API:
Parameter
Data Type
Description
Is Mandatory?
userId
String
Identifier for known user. Please note that the length of
userId
can be a maximum of 100 characters.
Yes
ttl
Number
(in seconds)
This parameter specifies the maximum time that WebEngage should take to send your message to the user once the message has been received by WebEngage. Delays can happen sometimes because of infrastructure issues or other errors. In case of any delays, the request will be retried multiple times (in order to send the message) only for the time duration specified in the the
ttl
.\
We use a default
ttl
of 120 seconds in case it is not provided.
No
dedupe.ttl
Number
(in seconds)
Time during which duplicate communication requests will be ignored (Range: 5 – 1800 seconds)
The dedupe window is fixed (not sliding): it applies from T0 to T0 +
dedupe.ttl
, where T0 is the time of the first occurrence.
No
txnId
String
A transaction ID can be provided with each request. If this is not provided then our server will generate a random ID for each request which is also returned in the response.
No
overrideData.email
String
Specify the email ID to whom the email should be sent
Yes (only for Email channel)
overrideData.phone
String
Specify the phone number to whom the SMS should be sent
Yes (only for SMS and WhatsApp channels)
overrideData.context.token
JSON
An object which contains values of personalized tokens which are used in the campaign.
Eg. If the campaign's message contains the following token:
{{token.first_name}}
then the
overrideData
should be:\
"overrideData": {
 "context": {
 "token": {
 "first_name": "Peter"
 }
 }
}
No
Deduplication (Idempotency)
To avoid sending duplicate messages—especially in retry scenarios—you can configure a dedupe window in seconds.
How does it work?
A unique
dedupe key
is generated for each communication.
If the same
dedupe key
appears again within the dedupe TTL window, the message is not resent.
The dedupe window is fixed (not sliding): it applies from T0 to T0 +
dedupe.ttl
, where T0 is the time of the first occurrence.
Note : Add
ttl
and
dedupe.ttl
based on message criticality and retry strategies.
Example Payload
{
 "ttl": 1200,
 "dedupe": {
 "ttl": 1800
 },
 "overrideData": {
 "context": {
 "token": {
 "system": "ll91y0fndbj"
 }
 },
 "phone": "9999999999"
 },
 "userId": "gr7y6a9p3tg"
}
Response
200
- The request has been successfully accepted.
JSON
{
 "response": {
 "data": {
 "txnId": "69b180f6-5731-4c4e-9816-298058f32072",
 "experimentId": "~3ekekrh",
 "userId": "peter",
 "ttl": 30
 }
 }
}
Errors
Response Code
Description
400
The request was not in an acceptable format. Possible reasons are missing parameters, bad structure etc.
404
The request resources do not exist. Possible reasons are user does not exist, invalid campaign ID etc.
408
The TTL of the request expired while calling the WebEngage API.
412
Certain conditional checks failed for this request. One of the reasons can be that user is not reachable on that channel.
5xx
Something went wrong at WebEngage's end. Please reach out to
[email protected]
in case you encounter this issue
Pipeline Latency (Request to Delivery Time)
To help track request to delivery time, i.e., the time between WebEngage received your request and when it delivered to the downstream channel, WE generates the
txnId
which can be used to identify the request-to-delivery time.
UUID Generation for Latency Tracking
If
txnId
is not passed, WebEngage generates a UUID as the txnId whose MSBs are the timestamp when the request is received.
This allows you to estimate the latency from API acceptance to delivery, using downstream delivery event timestamps.
For Advanced Users (Optional)
If you’re exporting data to BigQuery, you can extract the timestamp embedded in the UUID using a custom function like the one below:
SQL
CREATE TEMP FUNCTION
 entry_time(x STRING)
 RETURNS STRING
 LANGUAGE js AS """
 function getMostSignificantBits(s) {
 const sp = s.split("-");
 const msb_s = sp.slice(0, 3).join("");
 let msb = parseInt(msb_s, 16);
 return msb.toString();
 }
 return getMostSignificantBits(x);
""";
You can then compare this timestamp with the message’s actual delivery time to measure pipeline latency.
📘
Tip: For precise SLAs, always define a txnId and set appropriate ttl based on the urgency of your message.
Please feel free to drop in a few lines at
[email protected]
in case you have further queries. We're always just an email away!
Updated
7 months ago
Tracking Events
GET Survey Responses
Copy Page
