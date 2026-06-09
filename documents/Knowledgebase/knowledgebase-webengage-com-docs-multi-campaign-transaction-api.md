# Multi-Campaign Transaction API

- URL: https://knowledgebase.webengage.com/docs/multi-campaign-transaction-api
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Multi-Campaign Transaction API
The Multi-Campaign Transaction API lets you trigger multiple transactional campaigns in a single request, with control over how they execute. Beyond message delivery, a single call can also emit a tracking event and create or update a user profile.
This is useful when you want to:
Send a message across multiple channels (SMS, Email, WhatsApp, etc.)
Define fallback communication logic based on delivery outcome
Improve delivery reliability
Track the transaction as an event in the user's profile
Create or update user profile attributes at the time of sending
Reduce multiple API calls into a single transaction
🚧
Keep in Mind
All campaigns included in the request must be in
Running
state before triggering this API.
Setup Modes
Broadcast
— All campaigns run simultaneously, across channels.
Fallback
— Campaigns execute sequentially. The next campaign triggers only if the previous one fails. You can control whether fallback is based on a failed send attempt or a failed delivery.
When Should You Use This?
1. Multi-Channel Broadcast
Send the same order confirmation simultaneously through SMS, Email, and Push.
Use
Broadcast
mode.
2. Channel Fallback Strategy
Try WhatsApp first → if it fails, try SMS → if that fails, try Email.
Use
Fallback
mode. This ensures users receive communication even if one channel fails.
3. Track the Transaction as an Event
Automatically emit a named event (e.g.
order_confirmed
) when the transaction is triggered — useful for downstream journeys, segment membership, or analytics.
4. Create or Update a User Profile
Pass user attributes (name, email, custom fields) in the same call so the profile is created or updated at the time of sending — no separate API call needed.
Execution Modes
Broadcast Mode
All campaigns are triggered independently. Success or failure of one does not affect others.
Use when you want to maximize reach across channels simultaneously — for example, parallel notifications or cross-channel A/B testing.
Fallback Mode
Campaigns execute one after another in the order you define. If one channel fails, the next one is automatically tried — continuing until a message gets through or all options are exhausted.
You can configure when the fallback triggers: either as soon as a send attempt fails, or only after a delivery failure is confirmed.
📘
Want to understand the difference?
See the
Developer Guide
for a technical breakdown of both fallback variants.
Event Tracking
When configured, the API emits a tracking event as part of the transaction — without blocking or affecting delivery or fallback logic.
The event automatically captures transaction context, including the transaction ID, personalization tokens, and contact details from the request.
If event tracking is not configured, no event is emitted and the transaction proceeds normally.
User Profile Upsert
When configured, the API creates or updates the user's profile as part of the same transaction call.
If the user doesn't exist → a new profile is created
If the user exists → only the fields you provide are updated; everything else stays unchanged
Custom attributes are merged; existing keys are overwritten if re-provided
The profile update runs
once per request
, independent of fallback campaign execution
If not configured, no profile operation is performed.
Execution Order
Campaigns always execute in the exact order in which they are passed. This order is strictly preserved and is not affected by retries or internal processing.
If order matters to your communication strategy, ensure campaign IDs are passed in the correct priority sequence.
📘
Need Technical Details?
For the complete implementation — endpoint, request parameters, authentication, rate limits, and sample API calls — refer to the
Multi-Campaign Transaction API – Developer Guide
.
Updated
about 2 months ago
Engagement Score
Catalogs and Recommendations
Copy Page
