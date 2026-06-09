# FAQ

- URL: https://knowledgebase.webengage.com/docs/push-notification-faq
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

FAQ
Commonly asked questions related to Push campaigns
Campaign Creation
Your dashboard comes with a highly-intuitive
6-step campaign creation interface
that enables you to customize, personalize and test your messages with great ease. Here are a few questions that are frequently asked by WebEngage users:
1. How can I customize the appearance of my Push Notification as per my branding?
While you can easily
personalize the notification's images, links and text
as per each user's preferences and behavioral history, the campaign creation interface currently does not support customizations
like changing the font color, font style, font type, background color, and so on.
Such customizations can be made in your app before rendering the
Push Notification
for a user. This can easily be achieved by building
Key-Value Pairs
in your app's code.
You can think of
Key-Value pairs
as a set of linked data points in which the
Key
acts as a unique identifier and the
Value
either represents the data or points to the location of the data that is identified by the
Key.
🚧
Detailed Read
How Key-Value Pairs work
How to customize Push Notification's appearance using Key-Value Pairs
Further, you can choose to execute these customizations for your Android apps using the
WebEngage Android SDK.
Here's how you can go about it.
2. How can I send a Push Notification to multiple apps at once?
You can easily target multiple Android and iOS apps through a single
Push Notification
by:
Connecting the apps with your WebEngage dashboard.
(
OS-specific guide
)
Specifying them as the target apps while creating a campaign.
(
Step-by-step guide
)
Here's how it works:
Step 1:
As shown below, add
Android app's Package Name
and
iOS app's Bundle Identifier
under
Integrations< Channels < Push.
Click to enlarge
Step 2:
As shown below, select the
Target Android Apps
and
Target iOS Apps
at
Step 1: Audience
while creating the Push campaign.
Click to enlarge
And you're all set!
Step 3:
Continue building the campaign.
3. What image & text specifications should I follow for creating Push Notifications?
Please follow these guidelines
for configuring the
Push Layouts
available in your dashboard.
4. Can I use Branch.io for deep linking Push Notifications?
Yes. Add the Branch.io deep link in the relevant fields (On-click Action/ Button Link) while
creating the Push campaign
, and you're good to go!
🚧
Related read:
Integrating Branch with WebEnage
to capture user-app interactions as
Custom Events
5. Are GIFs files supported in Push Notifications?
While you can add animated GIF files to
Push Notifications,
GIFs are supported only on iOS v4+ devices.
GIFs are not supported by Android and are rendered as static images in a
Push Notification.
Videos and audio files are currently not supported by your dashboard.
Thus, if you plan on including animated GIFs in your
Push Notification
then we recommend that:
You exclusively target only iOS devices.
Follow these image specs
to optimize the GIF's dimensions as per the
Layout
selected for creating the campaign.
6. How can I create geotargeted Push Notifications?
Geotargeted Push Notifications
can be sent through the
Journeys
section in your dashboard. You can easily leverage the
Geofence Trigger block
to start a
Journey experience
for users who enter/exit the fence and engage them with highly personalized
Push Notifications
in real-time! (
Step-by-step Guide
)
7. How can I engage users in multiple segments through Push?
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
8. How can I schedule my campaign for delivery in the user's timezone?
You can easily schedule a
Push Notification
for delivery in your user's timezone by selecting
One-time
as the
Campaign Type
at
Step 2: When
.
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
.
Campaign Delivery, Failures & Queueing
Here are a few questions that are frequently asked by WebEngage users:
1. What happens when a Push Notification is sent to an offline user?
Depending on the user's device OS, their experience will differ:
For Android devices
All
Push Notifications
are sent to FCM for delivery to your users. So, in cases where the user is offline at the time of sending the Push campaign, FCM queues it for delivery as soon as the user's device comes online. The notification is queued upto the
Queueing Duration
specified while creating the campaign and is referred to as
TTL
(
time_to_live
) by FCM.
In cases where the TTL expires before the notification can be delivered to the user, the message is dropped by FCM.
If
Queueing
is disabled while creating the campaign, then the notification is immediately dropped by FCM (as it would mean that the parameter,
time_to_live
equals 0 for the notification.)
In all cases, since the
Push Notification
was successfully delivered to FCM, it's counted towards the performance indicators,
Sent
and
Delivered
for the campaign.
If a user recieves multiple_Push Notifications_ when they're offline:
All
Push Notifications
will be delivered as soon as the user's device is online (only if their TTL hasn't expired).
For iOS devices
All Push Notifications are sent to APNs for delivery to your users. So, in cases where the user's device is offline at the time of sending the campaign, APNs stores the notification for a limited (unspecified) duration and attempts delivery as soon as the user is online.
If a device remains offline for a long (unspecified) period, then all its stored notifications are discarded by APNs.
In all cases, since the
Push Notification
was successfully delivered to APNs, it's counted towards the performance indicators,
Sent
and
Delivered
for the campaign.
If a user recieves multiple_Push Notifications_ when they're offline:
Only the latest notification is stored and delivered by APNs when they're online. All previous messages are discarded.
🚧
Detailed Read
How
time_to_live
works in FCM
How APNs stores messages when user is offline
2. How does our Amplification engine work? How can I analyze its impact?
Our Amplification engine boosts
Push Notification
delivery to _Chinese Android devices like Xiaomi, Lenovo, Oppo, LeEco,_and so on, in cases where FCM fails to deliver the message. Such scenarios are usually a result of battery optimization where apps running in the background are killed by chinese devices. This means that unless a user launches your app, they will not receive the notification. Subsequently, the notification is dropped by FCM and is recorded as
Delivery Failure
in your dashbord.
This device-level optimization creates a barrier between you and your users. This is why, we built our
Amplification Engine.
It's a smart delivery system that identifies the notifications FCM was unable to deliver and reattempts delivery on app launch - helping you effectively engage a wider audience.
Here’s how it works:
As highlighted below, you can easily analyze the impact of
WebEngage's Amplification Engine
on driving
Clicks, Conversions
and
Revenue
through the
Push Campaign's Overview section
.
Click to enlarge
3. Why do some Push Notifications fail to get delivered?
Push Notifications
may fail to get delivered to a few users for various reasons like;
the user has unsubscribed, error in message/ image/ link personalization, FCM was misconfigured for your account,
and so on.
🚧
Detailed Read
Push Notification Delivery Failure Reasons
Analyzing Failures for a Push Campaign
4. Why do some Push Notifications get queued?
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
Analyzing Queued Messages for a Push Campaign
Miscellaneous
Here are a few questions related to mobile marketing that are frequently asked by WebEngage users:
1. How are app uninstalls tracked in WebEngage?
Each time a user uninstalls your app, it's automatically tracked as the
System Event
, app_uninstalled
in your dashboard. You can leverage this data to re-engage users through alternate channels, motivating them to continue their association with you.
App uninstalls are detected in the following ways at WebEngage:
Method 1: Silent Push Notifications
A
silent notification
with an empty payload is sent to all the devices registered to all your users once a day. If we're unable to reach a device during this process, then we learn that your app has been uninstalled.
Method 2: FCM Response on Attempting Notification Delivery
All
Push Notifications
are sent to FCM for delivery to your Android users. Each time FCM (Firebase Cloud Messaging) is unable to deliver a
Push Notification
to a user due to the fact the app has been deleted, it's conveyed as the
Delivery Failure
reason -
Uninstalled. (Can be analyzed under a
Push Campaign's Overview section
)
In both cases, these users are:
Counted towards
Total Uninstalls
, indicated under the
Uninstalls section
in your dashboard.
Marked as
unreachable on Push
.
2. How can I analyze uninstalls, possibly caused by Push Notifications?
You can extensively analyze users who have uninstalled your app and the
Push Notifications
which may have caused this behavior, through the
Uninstalls section
shown below.
WebEngage Uninstall Analytics
3. What is a Silent Push Notification?
A
Silent Push Notifications
is a hidden instruction that is delivered to the app installed by your user. Unlike regular
Push Notifications
that invoke user interaction,
Silent Push Notifications
remain hidden. Hence the term 'silent'.
Such notifications quietly ping the app and can be used to deliver data, notify their apps about the availabilty of new content, initiate code/content download in the background and so on. For example, makers of a podcast app can leverage
Silent Push Notifications
to notify their apps about a new episode and initiate content download in the background.
At WebEngage, we leverage
Silent Push Notifications
to track app uninstalls for you. A silent notification is sent to all devices registered to all your users once a day. If we're unable to reach a device during this process, then we learn that your app has been uninstalled.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries or feedback. We're always just an email away!
Updated
6 months ago
Creating Dynamic Push Experiences Using Key-Value Pairs
SMS
Copy Page
