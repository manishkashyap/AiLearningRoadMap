# Frequency Capping

- URL: https://knowledgebase.webengage.com/docs/frequency-capping
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Frequency Capping
A detailed explaination of how frequency capping settings work and how they're applied to a campaign and journey
What's worse than engaging users with mass blast campaigns? Inundating them with multiple messages through various channels in a short span of time.
One of the biggest challenges brands face is balancing their user engagement efforts across multiple channels in a way that neither comes across as spam nor as disengaged. At WebEngage, we found the perfect solution to this problem in the form of
Frequency Capping.
📘
Frequency Capping
is a powerful campaign management tool that allows you to control the number of campaigns a user can receive within a day, week and month. Additionally, you can also specify a time gap that needs to be maintained between consecutive messages.
Thus, using this feature, you can adjust and determine the flow of your entire communication and marketing strategy.
How It Works
Frequency Capping (FC)
is automatically applied to all campaigns sent through
Push, SMS, Web Push, Email,
as highlighted below. However, this setting cannot be configured for
On-site
and
In-app.
Given the targeted nature of these channels, messages are sent to your users only in the context of their behavior in real-time, rendering such channel restrictions unnecessary.
Applying Frequency Capping (FC) to a campaign at Step 2: When, while creating it
An upper limit on the number of campaigns your users can receive
in a day, week and month
can be set through the
Settings
section of your dashboard. Here’s how we calculate the time period:
A day
is calculated as
12:00 am to 11:59 pm.
This means that the daily frequency cap will reset at 12:00 am for all your users.
A week
is defined as
12:00 am Sunday to 11:59 pm Saturday.
This means that the weekly cap will reset at 12:00 am every Sunday.
A month
is defined as
12:00 am of Day 1 to 11:59 pm of Last Day, depending on the calendar month.
This means that the monthly cap will reset at 12:00 am on the first day of every month.
All the durations mentioned above are detected in real-time, for each user. This means that your frequency capping settings will be applied to all your users only in the context of their time zone! When set for multiple periods, a combination of the settings will be applied to each user.
Configuring Frequency Capping settings for your account
Further, the cap can be set at 2 levels -
Channel-wise
and
All Channels Combined.
When set for both, a combination of your settings will be applied. Let's go over a few examples to demonstrate how this works:
👍
Case 1: When Frequency Cap is Set Only for Channels
Let's assume that you have set the following upper limits, per
Day
for each channel:
Push:
2
SMS:
2
Web Push:
1
Email:
1
This means - your users will be able to receive a maximum of 6 messages in a
Day,
excluding
In-app
and
On-site Notifications.
👍
Case 2: When Frequency Cap is Set Only for All Channels Combined
Now let's assume that you set a cap of 10 messages per
Week
for
All Channels Combined.
This means - your users will receive only the first 10 messages sent through
Push, SMS, Web Push, and Email,
within a
Week.
The first 10 messages could include the following possibilities:
10 Push Notifications
10 SMSes
10 Web Push Notifications
10 Emails
or a combination like
3 Push Notifications, 2 SMSes, 3 Web Push Notifications, 2 Emails
and so on.
👍
Case 3: When Frequency Cap is Set for Each Channel and All Channels Combined
Let's assume that you have set a cap of 3 messages per
Day
for each channel and a cap of 5 messages for
All Channels Combined.
This means - your users will receive only the first 5 messages sent through any of the channels -
Push, SMS, Web Push, and Email
and a maximum of 3 messages through each channel, in a
Day.
Once the total number of messages delivered to a user equals the upper cap, all additional messages get queued for delayed delivery.
(The concept of Queueing has been discussed in further detail
here.
)
Time Gap
You can maintain a healthy interval between successive messages by defining a
time gap.
Doing so will ensure that all your users receive campaigns spread out evenly over a period of time, eliminating all possibilities of you unknowingly spamming a user through multiple channels.
A time gap can be specified in
Minutes, Hours or Days,
as per your engagement strategy.
It can be set at 2 levels -
Channel-wise
and
All Channels Combined.
When set for both, the level with the higher duration will override the other settings. Let's go over a use-case to help you understand this better:
👍
When Time Gap is Set for Each Channel and All Channels Combined
Case 1:
Let's assume that you have set a time gap of 30 minutes for
Email
and
Push
and a time gap of 1 hour for
All Channels.
Since the time gap duration specified for
All Channels
is higher, it will override the Channel settings of
Email
and
Push.
This means that all emails and push campaigns will be delivered after a gap of 1 hour.
Time gap is always applied as a part of your frequency capping settings to a campaign and cannot be disabled separately.
Disabling Frequency Capping
If you are sending an important message, then you can always choose to ignore the frequency cap and time gap at step 2: When, while creating the campaign. This can be done for all the campaigns sent through
Push, SMS, Web Push, and Email.
Select 'Ignore Frequency Capping' if you're sending a time-sensitive message
Doing so will ensure that the message is sent to your users even if the daily, weekly or monthly cap has been exhausted for a user. Further, these messages will not be counted towards the upper limit defined for that day, week or month. Let's go over a short example to show how it works:
👍
How Disabling FC Affects the Way the Upper Cap is Calculated
Let’s say that you have set a daily cap of 5 messages for
All Channels Combined.
But given the urgent nature of a few messages, you choose to ignore frequency capping for 2 campaigns. And by the end of the day, you have sent a total of 6 messages through various channels.
Under regular circumstances, the 6th message will not be sent as the upper limit for the day is 5. However, since you have ignored the setting for 2 campaigns, the total number of messages for computing the frequency cap will be 4 (6-2).
This means that users who received the 2 messages mentioned above will be able to receive a total of 7 messages through
All Channels Combined,
on that day.
Impact of Transactional Campaigns on Frequency Capping
As discussed under
Campaigns and Its Type
, Transactional Campaigns
consist of time-sensitive messages that are triggered for a user as soon as a particular scenario occurs in their lifecycle.
Since most users expect to receive such messages from you, it becomes imperative to deliver them immediately, irrespective of the number of messages they may have received previously.
Hence,
Frequency Capping and Time Gap settings
are not applied to
Transactional Campaigns
.
This is why we recommend that carefully consider the number of
Transactional Messages
a user could receive within a span of time while specifying a
Frequency Cap.
Doing so will help ensure that you maintain a healthy flow of communication at all times.
Applying Frequency Cap to a Journey
As discussed under
Journey Campaigns
,
all journey campaigns are tied to a journey and are sent to your users as per the conditions defined while creating it. Thus, given the dependent nature of journey campaigns, the
Frequency Capping
and
Time Gap
settings of your account are applied to the entire journey. These settings cannot be disabled for a particular journey campaign.
Frequency Capping
and
Time Gap
are applicable only to
Push, SMS, Web Push,
and
Email
campaigns of a journey. These settings will not be applied to
In-app and On-site as journey campaigns are triggered through these channels only when users are active on your app and website, rendering such restrictions unnecessary.
Frequency Capping
can be enabled/disabled for the entire journey while creating it, or through its
Live Overview
section after it’s published, as shown below.
Configuring Frequency Capping (& Time Gap) for a Journey
Which
Frequency Cap
and
Time Gap
is applied to a journey?
As discussed under
How It Works
,
an upper limit (frequency cap) and time gap can be specified at two levels -
All Channels Combined
and
Channel-wise (Push, SMS, Web Push, Email).
Both settings are applied to a journey's campaigns, depending on the channel they're sent through.
We hope this gives you a clear understanding of how frequency capping works. Please feel free to reach out via
[email protected]
in case you have any further queries or related feedback. We're just an email away :)
Updated
7 months ago
Campaign Variations and Multivariate Testing
DND Hours
Copy Page
