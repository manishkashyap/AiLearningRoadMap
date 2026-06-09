# Throttling (Message Rate-Limiting)

- URL: https://knowledgebase.webengage.com/docs/throttling-messages
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Throttling (Message Rate-Limiting)
Control the number of messages sent through each campaign & channel to avoid system overload
What is Throttling?
As marketers, we want our messages to reach all our users as soon as possible. But for apps and websites that have a significantly large userbase, this tendency increases the risk of server overload.
Let's assume a scenario where you've sent a
Push Notification
to all your users (1M+) who click on it to open your app around the same time. Such a sudden surge in traffic can raise the risk of overload on your backend system. And even for highly prepared businesses, the unanticipated load may cause server slowdown or outage (in extreme cases).
Such situations are a great inconvenience as they disrupt your user experience and are a source of frustration for your fellow teammates.
The solution?
Throttle your messages.
📘
Throttling allows you to limit the number of messages that can be sent to a particular endpoint, enabling you to maximize user outreach without taking unnecessary risks.
Thus, while sending a
Push Notification, SMS, Web Push Notification, Email, or WhatsApp message
, you can control the number of messages sent from your dashboard to your service providers
(FCM, APNs, SSP, ESP, WSP).
Doing so helps:
Reduce server resource consumption and maintain a consistent performance of your platforms.
Avoid unwanted system load caused by a surge in platform engagement.
Build domain authority for the IP address to send marketing email campaigns (as large volumes are often suspected to be spam).
How It Works
Message throttling can be set at two levels in your dashboard:
For a Channel
(
How to configure
)
For a Campaign
(
How to configure
)
Once you specify a rate limit for a channel under
Configurations > Throttling,
messages will be throttled by default for all its campaigns.
You can choose to disable throttling for a campaign or specify a different (lower) throttle limit while creating it.
If a campaign is being sent to multiple platforms (like
Android & iOS for Push
or
Firefox & Chrome for Web Push),
then the throttle limit will be divided equally amongst the platforms.
For example, if you've specified a throttle limit of 10K for a
Push campaign,
then 5K messages per minute will be sent to
Android users
and
iOS users,
each.
🚧
Please Note: Transactional Campaigns Cannot be Throttled
Given the urgent nature of
Transactional Campaigns
,
such messages are sent to your users as soon as a specific scenario occurs in their lifecycle. Channel-level throttle limits are not applied.
Specifying Custom Throttle Limit for a Campaign
You can choose to alter the message throttling rate for each campaign while creating it by:
Disabling throttling.
Specifying a lower, custom throttle limit.
Click to enlarge
You can adjust the limit based on the available server capacity and the expected popularity of each campaign. For example:
If you're
sending a campaign during a high traffic period on your platforms,
then you can lower the number of messages sent per minute to manage better your server bandwidth (so that it can comfortably cater to the additional traffic).
If you're
sending a campaign that requires your team to answer calls/ respond to user queries,
then you can set a limit that can help your team balance out the workload.
If you're
sending a campaign that promotes an ongoing offer/coupon code,
then you can lower the throttle limit to reduce the number of users redeeming the offer at the same time (to balance daily marketing spends).
If you're
sending a campaign that conveys an urgent message, you can disable throttling for the campaign.
It will ensure that the message is delivered immediately to the entire target audience!
Throttling Journey Campaigns
By default, messages sent through
Journey campaigns
are throttled as per the channel-level limits set by you. However, you can choose to specify a custom throttle limit for a
Journey campaign
while creating it. (as shown below)
Click to enlarge
How Throttling, DND & Queueing Work Together
(To help you optimize user experiences!)
By limiting the number of messages sent per minute, a few users will receive the message a few hours after the campaign is triggered/launched. This raises the risk of engaging users during odd hours, such as when users may be asleep.
You can easily tackle such situations by:
Step 1:
Configuring
DND Hours
for your account.
(
step-by-step guide
)
Step 2:
Enabling
DND Hours
for all messages sent with
Message Throttling
enabled.
Step 3:
Specifying a sufficient
Queueing Duration
to ensure that the message is delivered as soon as
DND Hours
pass for a user.
Thus, as per your settings, we will attempt delivery as soon as a delivery window opens up. However, if the queueing duration expires before we can deliver the message, it'll be counted towards the Campaign's Failure stats with the reason,
DND Queue Drop. (You can analyze it under the Campaign's Overview).
As shown below, you can configure these settings while creating the campaign.
Click to enlarge
🚧
Related Read
How Delivery Window is Determined for Queued Messages
We hope this provides you a detailed understanding of how throttling works in your dashboard. Please feel to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away :)
Updated
7 months ago
Queueing
Send Intelligently
Copy Page
