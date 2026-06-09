# FAQ

- URL: https://knowledgebase.webengage.com/docs/sms-faq
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

FAQ
Commonly asked questions related to SMS Marketing
Campaign Creation
Your dashboard comes with a highly-intuitive
6-step campaign creation interface
that enables you to customize, personalize and test your messages with great ease. Here are a few questions that are frequently asked by WebEngage users:
1. Can I send SMS campaigns to encrypted phone numbers?
Yes, this can be achieved by setting up a
Private SSP
at your end. You can think of a Private SSP as a middle layer between WebEngage and your SSP (SMS Service Provider) that enables you to decrypt the encrypted phone numbers shared with your WebEngage account. This is a great way to maintain your user's privacy and protect their
Personally Identifiable Information (PII Data).
(In case you're wondering - a Private SSP setup works for sending all types of campaigns, including transactional messages.)
Here's how it works:👇
Step 1:
Create and launch your SMS campaign.
(
Step-by-step guide
)
Once launched, we will send the messages to the endpoint URL specified as the Private SSP under Integrations < Channels <
SMS section
in your dashboard.
Step 2:
Your Private SSP receives the messages and decrypts phone numbers of your target audience.
Step 3:
The Private SSP forwards the
SMS campaign
with the real phone numbers to the
SSP (SMS Service Provider)
you're using to deliver the messages to users.
Step 4:
The SSP receives the campaign and starts delivering the messages to the specified phone numbers.
Step 5:
Users included within the campaign's target audience receive the message and start interacting with it!
All interactions can be analyzed in real-time through the
SMS Campaign's Overview section
.
Step 6:
The SSP pings back your
Private SSP (Decryption Layer)
with the delivery status of each message which could be any of:
Failed
Delivered
Queued
Step 7:
Your decryption layer forwards the delivery status for each user to your WebEngage dashboard through a
Webhook
.
Step 8:
As soon as we receive data, it starts reflecting under the
SMS Campaign's Overview section
.
🚧
Detailed Read
How to Send Encrypted Phone Numbers to WebEngage
Integrating a Private SSP with WebEngage
2. Can the URLs in an SMS campaign have a custom domain?
Yes! Here's how you can go about it:
Step 1:
Create a custom domain that will exclusively be used to add links in your campaigns.
Step 2:
Add a CNAME entry for the custom domain and point it to
weurl.co
with a TTL (
time to live
) of 30 minutes in your DNS (Domain Name System) zone file. Doing so will ensure that your domain name is not replaced with
weurl.co
when the link is shortened.
Step 3:
Add the domain to your dashboard under
Settings > Campaign Custom Domain
, as shown below.
Click to enlarge
And you're all set!
(
Detailed read
)
3. How can I send geo-targeted text messages?
Geotargeted messages can be sent through the
Journeys section
in your dashboard. You can easily leverage the
Geofence Trigger block
to start a
Journey experience
for users who enter/exit the fence and engage them with highly personalized text messages in real-time!
(
Step-by-step Guide
)
4. How can I engage users in multiple segments through SMS?
You can easily combine multiple segments under
Step 1: Audience
while creating a campaign.
Click to enlarge
As highlighted above:
Step 1:
Select
Send to users in multiple segments and/or...
against the field,
Audience Type
Step 2:
Select the logic by which you'd like to combine the segments:
Send to only those users who are included in ALL Segments
OR
Send to users in ANY of the selected Segments
Step 3:
Continue building your campaign
5. How can I schedule my campaign for delivery in the user's timezone?
You can easily schedule a text message for delivery in your user's timezone by selecting
One-time
as the
Campaign Type
at
Step 2: When
while creating the campaign.
Click to enlarge
As highlighted above:
Step 1:
Select
Later
against
Delivery Time
Step 2:
Specify the delivery date-time, select
In User's timezone
from the last dropdown and you're all set!
Step 3:
Continue building your campaign.
Campaign Delivery, Failures & Queueing
Here are a few questions that are frequently asked by WebEngage users:
1. What happens when SMS is sent to a user who is out of network coverage / has switched off their phone?
All SMS campaigns are sent to an
SSP (SMS Service Provider)
intergated with your WebEngage account. So, both cases, the SSP will continue to attempt delivery for the
Queueing Duration
specified while creating the campaign.
In cases where the queueing duration expires before the user can be reached, the message is dropped by the SSP.
If you have disabled
Queueing
while creating the campaign, then the message will be dropped immediately by the SSP after attempting delivery for the first time.
In all cases, since the SMS was successfully delivered to the SSP, the message will be counted towards the performance indicator,
Sent
for the campaign.
If a user is sent multiple messages when they're out of network coverage/ their phone is switched off:
All messages will be delivered back-to-back as soon the user is reachable
(only if their queueing duration hasn't expired).
2. Why do messages fail to get delivered to some users?
SMS campaigns may fail to get delivered to a few users for various reasons like,
incorrect phone number, user is out of coverage area, SSP's monthly quota has expired
and so on.
🚧
Detailed Read
SMS Delivery Failure Reasons
Analyzing Failures for an SMS Campaign
3. Why do messages get queued for some users?
The term,
Queued
indicates the number of messages that have been sent to a campaign's target audience but are currently lined up for delayed delivery. It usually happens when
DND Hours
or
Frequency Capping settings
are applicable for a user.
🚧
Detailed Read
How Delivery Time is Determined for Queued Messages
Analyzing Queued Messages for an SMS Campaign
4. Why have my SMS clicks suddenly increased?
Some devices or apps automatically preview links in SMS messages to check safety or generate a preview. These background previews can register as clicks, which may increase your click numbers even when users have not clicked the link themselves.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries or feedback. We're always just an email away!
5. What is SMS Count?
SMS messages have a character limit (160 characters for standard encoding, 70 for Unicode). When a message exceeds this limit, it is split into parts, even if this is seen as one SMS for the end user, each transmitted and billed separately by the SSP.
The SMS Part Count card in the Campaign Overview shows the total number of parts across all messages for the campaign, aggregated from delivery confirmations received from your SSPs. This gives a more accurate picture of actual transmission volume and cost than the message count alone.
6. Why is my SMS Count lower than my Delivered Count?
The Delivered count is a derived metric, calculated as:
Delivered = Total Sent - Failed - Rejected - Queued
Because SSPs do not confirm every delivery back to WebEngage, this figure is an estimate and will trend higher than actual confirmed deliveries. SMS Part Count is built only from confirmed delivery receipts from SSPs. When Part Count is lower than Delivered, it is expected behavior - it means Delivered is overcounting, and Part Count is the accurate signal.
7. Why does my SMS Count card show "Incompatible SSP. Count Not Available"?
This appears when the SSP connected to your campaign does not share part count data with WebEngage. This can happen with SSPs that do not include part count in their delivery reports. In these cases, the card cannot display a value and will show this message instead. To resolve this, check with your SSP provider on whether part count reporting can be enabled on their end. Refer to the
SMS Integrations
page to check how to send SMS Counts.
Updated
27 days ago
Analyzing SMS Overview
RCS
Copy Page
