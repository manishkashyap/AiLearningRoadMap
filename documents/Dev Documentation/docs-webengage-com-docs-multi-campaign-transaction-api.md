# Multi-Campaign Transaction API & User Profile Upsert

- URL: https://docs.webengage.com/docs/multi-campaign-transaction-api
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

REST API
Multi-Campaign Transaction API & User Profile Upsert
Overview
The Transaction API supports triggering multiple campaigns within a single request, along with optional inline event tracking and user profile upsert. Execution behavior is controlled using the
mode
parameter, enabling:
Parallel broadcast across channels
Sequential fallback on attempt failure
Sequential fallback on delivery failure
Inline event emission via
trackConfig.eventName
User profile create/update via
trackConfig.updateUser
All enhancements are opt-in and fully backward compatible.
Endpoint
POST /v2/accounts/{licenseCode}/transaction
Query Parameters
Parameter
Type
Required
Description
campaignIds
String
Yes
Repeatable. Ordered list of campaign IDs to execute.
mode
String
Yes
Execution strategy:
all
,
fallback_on_attempt_failure
,
fallback_on_delivery_failure
Request Body
JSON
{
 "ttl": 300,
 "userId": "user_123",
 "txnId": "order_12345",
 "overrideData": {
 "context": {
 "token": {}
 },
 "email": "
[email protected]
",
 "phone": "+919876543210"
 },
 "trackConfig": {
 "eventName": "track_txn",
 "updateUser": {
 "firstName": "John",
 "lastName": "Doe",
 "email": "
[email protected]
",
 "attributes": {
 "Points": 100
 }
 }
 }
}
Field
Type
Required
Description
ttl
Integer
No
Time-to-live in seconds for the entire transaction. Remaining campaigns are skipped if TTL expires.
userId
String
Yes
Unique user identifier. Used to resolve the user for profile upsert and event tracking.
txnId
String
No
Client-provided transaction ID for deduplication.
overrideData
Object
Yes
Personalization payload — tokens, phone, email. Shared across all campaigns in the execution chain.
trackConfig
Object
No
Optional. Configuration for event tracking and/or profile upsert.
trackConfig.eventName
String
No
If present, a tracking event with this name is emitted inline during transaction processing.
trackConfig.updateUser
Object
No
If present, performs a user profile create or update. All subfields optional. Supported fields:
firstName
,
lastName
,
birthDate
(ISO-8601),
gender
,
email
,
phone
,
attributes
(key-value map).
Execution Order Guarantee
Campaign execution order strictly follows the sequence in which
campaignIds
are provided. This order is deterministic, persisted internally, and not affected by retries or asynchronous processing.
Execution Modes
Mode
Behavior
Success Condition
Typical Use Cases
all
All campaigns triggered independently. No short-circuiting.
N/A — all run regardless of outcome.
Parallel multi-channel notifications, cross-channel A/B testing
fallback_on_attempt_failure
Sequential. Next campaign triggers if provider rejects synchronously (e.g. invalid phone, provider error).
Provider accepts the request.
Invalid contact handling, fast failover without waiting for delivery reports
fallback_on_delivery_failure
Sequential. Delivery outcome determines fallback.
SENT
/
ACCEPTED
are not treated as success.
Confirmed delivery to end user.
Critical transactional messaging, high delivery assurance, channel escalation
🚧
Important
For
fallback_on_delivery_failure
, intermediate statuses such as
SENT
or
ACCEPTED
are
not
considered successful delivery. Only a confirmed delivery DLR stops the chain.
trackConfig: Event Tracking
When
trackConfig.eventName
is provided, an event is emitted inline during transaction processing. Event emission does not block execution or affect fallback logic.
Event Payload Composition
Field
Source
userId
From transaction request
eventName
From
trackConfig.eventName
txnId
System-generated or client-provided
ttl
From transaction request
phone
From
overrideData.phone
(if present)
email
From
overrideData.email
(if present)
Personalization fields
Flattened one level deep from
overrideData.context.token
Flattening Behavior
Personalization overrides are flattened one level deep
Nested maps are expanded by extracting immediate child key-value pairs
No recursive flattening is performed
Flattening occurs before
phone
/
email
enrichment
Failure Handling
Event emission failures are logged internally. They do not impact campaign execution or profile updates, and no retries are performed.
trackConfig: User Profile Upsert
When
trackConfig.updateUser
is provided, a user profile create or update is performed once per request during initial transaction processing. It is
not
re-executed on each fallback attempt.
updateUser Fields
Field
Type
Required
Description
firstName
String
No
User's first name.
lastName
String
No
User's last name.
email
String
No
User's email address.
phone
String
No
User's phone number.
gender
String
No
User's gender.
birthDate
String
No
User's date of birth in ISO-8601 format (e.g.
1990-05-21
).
attributes
Object
No
Key-value map of custom user attributes (e.g.
{"Points": 100, "Tier": "Gold"}
).
All fields are optional. Only fields present in the payload are written — omitted fields are left unchanged.
Identity Resolution
userId
from the TXN request is used to resolve the user
If user does not exist → new profile is created with the provided fields
If user exists → only the provided fields are updated; all other fields remain unchanged
Attribute Merge Behavior
Custom
attributes
are merged into the existing attribute map
If a key already exists, it is overwritten with the new value
Keys not present in the request are left unchanged
No attribute deletion is supported via this API
Execution Notes
Executed
once per TXN request
, during initial processing
Independent of campaign execution and fallback logic — profile update is not retried or re-run per fallback attempt
Executes regardless of whether campaign delivery succeeds or fails
Failure Handling
Profile update failures are logged internally. They do not block campaign execution or event tracking, and no retries are performed.
Example — updateUser Payload
JSON
{
 "trackConfig": {
 "updateUser": {
 "firstName": "John",
 "lastName": "Doe",
 "email": "
[email protected]
",
 "phone": "+919876543210",
 "birthDate": "1990-05-21",
 "gender": "male",
 "attributes": {
 "Points": 100,
 "Tier": "Gold",
 "PreferredChannel": "whatsapp"
 }
 }
 }
}
Processing Order
Transaction request received and validated
Campaign(s) executed per selected
mode
If
trackConfig.eventName
is present → event emitted
If
trackConfig.updateUser
is present → profile upsert performed
🚧
Note
If campaign validation fails at step 1, neither event emission nor profile update is performed.
Keep In Mind
📘
Things to note
Shared personalization
— A single
overrideData
payload is applied to all campaigns in the execution chain.
TTL scope
— Applies to the entire transaction lifecycle. Campaigns not yet triggered are skipped if TTL expires.
Rate limits
— Fallback campaigns triggered within the same request count toward the Transaction API rate limit.
Backward compatibility
— Existing single-campaign Transaction API behavior is unchanged.
campaignIds
,
mode
, and
trackConfig
are all opt-in.
Example — Fallback on Delivery Failure with Event Tracking and Profile Upsert
Bash
curl -X POST \
 '<HOST>/v2/accounts/<LICENSE_CODE>/transaction?campaignIds=~abc123&campaignIds=~xyz456&mode=fallback_on_delivery_failure' \
 -H 'Authorization: Bearer <YOUR_API_KEY>' \
 -H 'Content-Type: application/json' \
 -d '{
 "ttl": 300,
 "userId": "user_123",
 "txnId": "order_12345",
 "overrideData": {
 "context": {
 "token": {
 "order_id": "ORD-12345"
 }
 },
 "email": "
[email protected]
",
 "phone": "+919876543210"
 },
 "trackConfig": {
 "eventName": "track_txn",
 "updateUser": {
 "firstName": "John",
 "lastName": "Doe",
 "email": "
[email protected]
",
 "attributes": {
 "Points": 100
 }
 }
 }
 }'
cURL
curl -X POST \
'<HOST>/v2/accounts/<YOUR_WEBENGAGE_LICENSE_CODE>/transaction?campaignIds=~abc123&campaignIds=~xyz456&mode=fallback_on_delivery_failure' \
-H 'Authorization: Bearer <YOUR_API_KEY>' \
-H 'Content-Type: application/json' \
-d '{
 "ttl": 600,
 "userId": "peter",
 "txnId": "order_12345",
 "overrideData": {
 "context": {
 "token": {
 "orderId": "ABCD1234"
 }
 },
 "phone": "9999999999"
 }
}'
Updated
about 2 months ago
Custom Recommendation API
How It Works
Copy Page
