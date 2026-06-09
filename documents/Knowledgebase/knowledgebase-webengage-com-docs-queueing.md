# Queueing

- URL: https://knowledgebase.webengage.com/docs/queueing
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Queueing
A comprehensive explanation of how you can set up campaigns for delayed delivery
To ensure that all campaigns reach your users even after the frequency cap is met or DND hours have kicked-in, we have built a feature called
Queueing.
This feature enables delayed delivery of your campaigns to a user, ensuring minimal gaps in user communication.
🚧
Please ensure that you have a broad understanding of how
Frequency Capping
and the
DND settings
of your account are applied to a campaign and journey before proceeding. This will lay a strong foundation for understanding how campaign are queued, as per both the settings.
How It Works
If
Frequency Capping
or
DND
are enabled for a campaign or a journey, then all the respective campaigns created through
Push, SMS, Web Push, and Email
will be queued by default for 1 Day
(or as per the custom queueing duration specified by you)
if:
Case 1:
The frequency cap for a day, week, or month is exhausted
Case 2:
The time gap specified by you doesn’t allow a message to be delivered immediately
Case 3:
DND hours have kicked in for certain users
Case 4:
If a combination of any two or all of the cases mentioned above occurs
In
case 1
, we will hold on to the campaign until the frequency cap reset on the next day, week, or month or the queueing duration expires, whichever occurs first.
In
case 2
, we will hold on to the campaign until the next campaign delivery window opens up as per the time gap or the queueing duration expires, whichever occurs first.
In
case 3
, we will hold on to the campaign until the DND hours pass for the user or the queueing duration expires, whichever occurs first.
In all cases
, if the queueing duration expires before your settings allow us to deliver the campaign, then the campaign will fail.
Campaign failures
caused by these settings are indicated by the following terms in your dashboard:
Frequency Capping Queue Drop: Indicates failure due to frequency capping restrictions.
DND Queue Drop: Indicates failure due to DND settings.
And in all cases, depending on the reason for queueing, either of the following statuses is shown in the
Campaign's Overview
section:
DND Queue:
Any message that could not be delivered because of DND hours gets queued provided you have specified a queueing time.
Frequency Capping Queue:
Any message that could not be delivered because of Frequency Capping limits gets queued provided you have specified a queueing time.
🚧
Please Note
Queueing
or delayed campaign delivery cannot be configured for
In-app
and
On-site
campaigns as
Frequency Capping
and
DND Hours
are not applicable to these channels.
Custom Queueing
We have made it possible for you to specify a custom queueing duration in
minutes, hours or days,
while creating a campaign to minimize campaign failures. This can be specified for all campaigns created through
Push, SMS, Web Push, and Email
as shown below.
(
How it works for a journey & its campaigns
)
Queueing a Campaign for delayed delivery to a user if Frequency Capping and/or DND are currently applicable to the user
Doing so will ensure that we hold on to your campaign for the specified duration and send it only when a combination of your
Frequency Capping
and
DND settings
allow us to.
(
Detailed read on how delivery time is determined for queued campaigns
)
Disable Queueing
You can always choose to disable
Queueing
for a campaign while creating it. This option comes in handy especially when creating time-sensitive campaigns. This can be done for all the campaigns created through
Push, SMS, Web Push, and Email,
as highlighted below.
Disabling Queueing (delayed delivery) for a campaign
Let's go over a short use-case to help you understand its application, better:
👍
Use-case: Disabling Queueing for Flash Sale Campaigns
Let’s say that you have a planned a flash sale from 4 pm to 7 pm on your e-commerce app and have scheduled 2 push notifications to promote it. Both campaigns are scheduled to be sent as per your DND settings to avoid disturbing users in different time zones.
Hence, in this case, we recommend that you disable queueing for the campaigns as your flash sale would have ended by the time the delayed campaigns reach users located within the DND timezones.
Queueing Journey Campaigns
As discussed under
Journey Campaigns
, all journey campaigns are tied to a journey and are sent to your users as per the conditions defined while creating it. Thus, given the dependent nature of journey campaigns, a queueing duration can be specified only for the journey and is automatically applied to all its campaigns. As shown below, it can be configured through the journey's
Frequency Capping & DND
section.
Setting up Queueing for a Journey
📘
Please Note
All journey campaigns are queued for
2 Days
by default if
Frequency Capping, DND Hours
or a combination of both settings are currently applicable to a user.
As shown above, you can specify a custom queueing duration in
Minutes, Hours, or Days
for the entire journey. However, the queueing duration will be applied to only the
Push, SMS, Web Push
, and
Email
campaigns sent through the journey.
(Not applicable to In-app & On-site as FC & DND cannot be configured for these channels)
You can choose to disable queueing while creating a journey or through its
Live Overview
section after it's published. However, we strongly recommend you specify an optimum queueing duration if
Frequency Capping
or
DND hours
have been applied to a particular journey. This will help ensure that all the users entering the journey have a consistent experience.
Time Determination for Campaign
You must be wondering
how delivery time is determined for a ser when the campaign is Queued as per DND, Frequency Capping & Time Gap settings.
Let's go over a use-case to help you understand how a combination of your
Frequency Capping, Time Gap
and
DND settings
help determine when a queued campaign is delivered to a user.
👍
Let’s assume that you have;
Specified a
Frequency Cap of 5 Messages for All Channels, per Day
Specified a
Time Gap of 30 minutes for All Channels, per Day
Set up
Daily DND Hours
as
22:00 hrs to 08:00 hrs (10 pm to 8 am)
Added a
Queueing Duration
of
1 Day
for each campaign you create
In this case, we’ll ensure that campaigns are sent to your users only when a combination of all three settings allow us to do so. If either of the settings is found to be applicable to a user, then the campaign will be queued for a maximum of 1 Day. During this period, we will constantly evaluate the status of each user to detect any open windows of delivery.
For example, if the 5th message (Campaign 5) was sent to a user at 10:00 pm, then no further messages will be delivered to the user until the frequency cap resets at 12:00 am.
👍
In continuation...how Frequency Capping and DND are applied to Campaign 6
Now let's suppose that you schedule Campaign 6 for delivery at 11:30 pm to the same user.
However, since the frequency cap for the day has expired, we will queue the campaign for a maximum of 1 day, during which we will try to deliver the campaign at the earliest delivery window. A combination of both settings will determine the delivery window.
This means that as per your FC settings, Campaign 6 can be delivered as soon as the cap for the next day kicks-in at 12 am.
However, as per your DND settings, no campaigns can be sent to the user at 12 am. Hence, we will attempt to deliver Campaign 6 as soon as the DND hours pass, at 08:01 am, as this is the earliest delivery window available.
👍
In continuation...how Time Gap, DND and Queueing are applied to Campaign 7
Now, let’s suppose that you send another message (Campaign 7) to the same user at 2 am, during the DND hours.
So just like Campaign 6, this one too will get queued for a maximum of 1 Day and will be delivered as soon as possible.
This means that as per your DND settings, Campaign 7 can be delivered as soon as the DND hours end - at 8:01 am.
However, since a previous message (Campaign 6) is already queued for the user, the nearest delivery window of 8:01 am will be allotted to it. So, Campaign 7 will get delivered after Campaign 6.
Hence, as per your time gap settings, Campaign 7 will be delivered at 8:31 am - 30 minutes after Campaign 6.
We hope this gives you a clear understanding of how campaigns are queued for each user. Please feel free to reach out via support(AT)webengage.com in case you have any further queries, we're just an email away :)
Updated
7 months ago
DND Hours
Throttling (Message Rate-Limiting)
Copy Page
