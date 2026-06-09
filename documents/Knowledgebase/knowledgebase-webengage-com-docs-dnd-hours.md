# DND Hours

- URL: https://knowledgebase.webengage.com/docs/dnd-hours
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

DND Hours
A comprehensive explanation of how DND Hours are implemented for each user and campaign
An integral aspect of user engagement is respecting the boundaries of each user's comfort and availability. Thus, using the
DND settings
of your account, you can prevent users from receiving campaigns during specific periods such as when they may be asleep, for example, from 10 pm to 8 am.
How It Works
DND time slots can be defined at 4 levels:
Daily
(applicable to all days of the week)
Per day
Weekends
(Saturday and Sunday)
Weekdays *(Monday, Tuesday, Wednesday, Thursday, Friday)
This is a one-time set-up and can be changed anytime you like, through the
Configurations > DND
section of your dashboard, as shown below.
Configuring DND Hours for your account
The best part - DND hours are determined individually for each user. This means that
the periods specified by you will be applied to all your users only in the context of their time zone!
By detecting the location of each user in real-time, we ensure that no matter where your users are located, they will remain undisturbed during the specified hours, irrespective of your account’s time zone.
If you choose to define DND hours at all 4 levels then the delivery of all your campaigns will be restricted for a combination of all the time slots. Let's help you understand how this works with a short use-case:
👍
When DND Hours are set for all days (Daily) and Weekends
Let's assume that you have set DND hours for all
days (Daily)
as - 10 pm to 8 am. And have specified 10 pm to 10 am as the DND hours for
Weekends.
This means that for all days of the week, no campaigns will be delivered to users between 10 pm and 8 am, as per the timezone they're located in. However, on Saturday and Sunday (weekends) campaigns will be delivered to all users only after 10 am.
DND hours can be applied to all the campaigns sent through
Push, SMS, Web Push, and Email
while creating the campaign.
Configuring DND Hours for a campaign
This setting cannot be configured for
On-site
and
In-app.
Given the targeted nature of these channels, messages are sent to your users only in the context of their behavior in real-time, implying no intrusion of privacy.
Here's how it works for journeys.
All campaigns sent, or scheduled to be sent during DND hours will be queued for delayed delivery to the respective users.
(The concept of Queueing has been discussed in further detail
here.
)
Disable DND Hours
Select 'Ignore DND Settings' to disable for a particular campaign
You can choose to ignore DND settings while creating a campaign while creating it, as highlighted above. Doing so will ensure that the campaign is sent immediately or as scheduled, overriding your DND settings. This comes in handy, especially when sending time-sensitive messages to your users. Let's go over a use-case to help you understand its application:
👍
Disabling DND Hours for Mobile Wallet Account Updates
Let's assume the case of a digital wallet app that notifies all its users through SMS or Push notifications each time a credit or debit is processed for their account.
Give the sensitive nature of this communication, disabling DND hours for such campaigns is essential as users need to be notified as soon as the monetary transactions occur.
Transactional Campaigns DND Hours
As discussed under
Campaigns and Its Type
, Transactional Campaigns
consist of time-sensitive messages triggered for a user as soon as a particular scenario occurs in their lifecycle.
Since most users expect to receive such messages from you, it becomes imperative to deliver them immediately.
Hence,
DND Hours
are not applied to
Transactional Campaigns
.
Journey DND Hours
As discussed under
Journey Campaigns
,
all journey campaigns are tied to a journey and are sent to your users as per the rules defined while creating it. Thus, given the dependent nature of journey campaigns, DND settings are applied to the entire journey and cannot be disabled for a particular campaign.
DND hours are applied to all
Push, SMS, Web Push, and Email campaigns of a journey.
However, these settings are
not applicable
to
In-app and On-site journey campaigns.
Given the targeted nature of these channels, messages are sent to your users only in the context of their actions on your app and website, implying no intrusion of privacy.
You can choose to enable/disable the DND setting while creating a journey or through its
Live Overview
section after it’s published, as shown below.
Configuring DND Hours for a Journey
We hope this provides you a detailed understanding of how
DND Hours
are applied to all your users. Please feel to drop in a few lines at support(AT)webengage.com in case you have any further queries, we're always just an email away :)
Updated
7 months ago
Frequency Capping
Queueing
Copy Page
