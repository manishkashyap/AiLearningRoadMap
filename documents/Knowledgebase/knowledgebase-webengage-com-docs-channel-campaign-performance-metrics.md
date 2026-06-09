# Campaign & Channel Performance Indicators

- URL: https://knowledgebase.webengage.com/docs/channel-campaign-performance-metrics
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Campaign & Channel Performance Indicators
A list of all the engagement metrics tracked for Push, In-app, SMS, On-site, Web Push, Email & WhatsApp campaigns
At WebEngage, we believe that data-driven messaging is one of the most scientific ways to deliver contextual experiences tailored to each user. This is why we have identified a list of all the generic actions users can perform while interacting with campaigns sent through each channel of engagement and track them as
Campaign Events
.
Thus, each time you send a campaign, we automatically track several performance indicators or campaign events like
Deliveries, Failures, Opens, Impressions, Dismisses, Unsubscribes, Clicks, and so on,
helping you gauge its impact in real-time!
🚧
For Your Reference
Here's a
list of System (Campaign) Events
gleaned for each channel post-integration.
Now, let's walk you through the performance indicators that help you analyze the impact of each channel and its campaigns, across your dashboard.
Push
Once you send a
Push campaign
to your users, it goes through the following stages in its lifecycle:
The lifecycle of a Push Notification
Each stage is tracked as a
campaign event
or a performance indicator, helping you
analyze the campaign's impact
on user engagement, conversions, and revenue. You can also analyze the collective impact of all the campaigns sent through the channel by
analyzing Push Overview
.
Additionally, we have also made it possible for you to identify the stage at which a campaign is currently at, for each user through
Latest Message Status.
Detected in real-time, it can be analyzed through the
List of Users
of a campaign and each
User's Profile
.
Now, let's get you acquainted with all the performance indicators tracked for_Push_ campaigns:
Sent
Indicates the total number of messages sent to a push campaign's target audience, within the selected time frame.
Failures (Push)
Indicates the total number of messages that failed to get delivered to a campaign's target audience, within the selected time frame.
Here's a list of all the reasons due to which a
Push
campaign could fail:
Uninstalled:
Indicates that the user uninstalled your app, due to which the notification could not be delivered.
🚧
Related Read
Head over to our
Uninstall analytics
to gain deep insights into uninstalls and learn how you can curb churn!
Configuration Issue:
Indicates an error with your auth keys, certificates or incorrect FCM (Firebase Cloud Messaging) configuration. Detailed read on
how to configure Push as a channel
.
DND Queue Drop:
All messages meant to be delivered during a user's DND hours get queued as per the campaign's queueing duration. However, if the duration expires before a delivery window opens up, then the campaign will fail. Such failures are indicated by
DND Queue Drop.
Engagement Window:
If a campaign is sent with DND Hours enabled and no Queueing Duration has been specified for it, then all messages sent during a user's DND Hours will fail to get delivered. The same is indicated by
Engagement Window.
🚧
Please refer to
DND Hours
and
Queueing
for a detailed read.
Frequency Capping Queue Drop:
If the daily, weekly or monthly frequency cap has been exhausted for a user, then all additional campaigns will get queued for delayed delivery, as per each campaign's queueing duration. However, if the duration expires before a delivery window opens up, then the campaign will fail. Such failures are indicated by
Frequency Cap Queue Drop.
🚧
Please refer to
Frequency Capping
and
Queueing
for a detailed read.
Personalization Error:
Indicates an error with the personalization variables (user attributes, event attributes) or Nunjucks syntax used in the push notification's copy.
Device Not Registered/ No Device:
Indicates any of the following errors:
Delay in Registering Device:
A device is registered and available for delivering push notifications as soon as we receive its FCM (Android) or APNs (iOS) details. The first time a user installs your app, it takes a few seconds to a minute for us to glean these details. Thus, if campaign delivery is attempted before the device is registered, then it will fail to get delivered.
Incorrect Integration with WebEngage:
if there is a technical glitch in the way the WebEngage SDK has been integrated with your app, then all push notifications will fail to get delivered to your users. Detailed read on how to integrate WebEngage with your
Android
,
iOS
,
React Native
,
Xamarin.Android
,
Xamarin.iOS
and
Hybrid app
.
Time Zone Elapsed:
This error is generally recorded for one-time campaigns scheduled for delivery
in the user's timezone
. If the local time (for a user) has already passed the delivery time specified for the campaign, then the message will fail to get delivered.
Channel Not Available:
This error is generally recorded for journeys wherein a
Push
campaign is triggered for users who were not reachable through the channel.
🚧
Please refer to
Channels and Channel Reachability
for a detailed read on how reachability is determined for users in various scenarios.
Other Failures:
All off-beat reasons for campaign failures are clubbed under this header.
Delivered
Indicates the total number of messages that have been delivered to the target audience of a campaign, within the selected time frame.
👍
Fact Check
Total number of
Delivered
messages =
Sent - (Failures + Queued)
Queued (Push)
Indicates the total number of messages that have been
sent
to a campaign's target audience, but are currently
Queued
for delayed delivery.
A few common reasons due to which campaigns get queued include:
DND Queue:
All messages meant to be delivered during a user's DND hours get queued as per the campaign's queueing duration, indicated by
DND Queue.
Frequency Cap Queue:
If the daily, weekly or monthly frequency cap has been exhausted for a user, then all additional campaigns will get queued for delayed delivery, as per each campaign's queueing duration. This is indicated by
Frequency Cap Queue.
Waiting for Time Zone:
If you have scheduled a one-time push campaign for delivery
in the user's timezone
, then the message will get queued for all users where the specified time of delivery is yet to occur in their local time zone. The same is indicated by
Waiting for Time Zone.
If the
Queueing Duration
of a campaign expires before the message could be delivered to a user, then the message will
fail
.
Total/Unique Dismisses
Both metrics indicate the number of users that have dismissed a
Push
campaign within the selected time frame.
Total/Unique Clicks
Both metrics indicate the number of users that have clicked on a
Push
campaign sent within the selected time frame. This metric includes clicks on the notification, its buttons, and deep links.
Total Conversions
Indicates the total number of times a user has performed the
Conversion Event
of a
Push
campaign within the selected time frame.
Unique Conversions
Indicates the number of users that have performed the
Conversion Event
of a
Push
campaign within the selected time frame.
👍
Fact Check
Total Conversions
can be significantly higher than the
Unique Conversions
tracked for a campaign.
Reason:
A user can choose to perform the
Conversion Event
defined for a campaign, multiple times within its
Conversion Deadline
.
For example, a user can perform the event
Checkout-Complete
twice, each time purchasing a different product after receiving your campaign.
For the same reason -
Total Conversions
can be greater than 100%.
Total Click-through Conversions
Indicates the total number of times your users have performed the
Conversion Event
of a campaign, within the selected time frame, after clicking on the
Push Notification.
Detailed read on how this is tracked.
Unique Click through Conversions
Indicates the unique number of users that have converted within the selected time frame, after clicking on the
Push Notification.
Detailed read on how this is tracked.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign, then
Conversions
will not be tracked for it.
Detailed read.
Revenue
Indicates the total amount of revenue generated by the
Total Conversions
that have occurred within the selected time frame.
Click-through Revenue
Indicates the total amount of revenue generated by the
Total Click-through Conversions
that have occurred within the selected time frame.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign or if the specified
Conversion Event
is not mapped as a
Revenue Event,
then no
Revenue
will be tracked for it.
Detailed Read on how
Revenue tracking works
and how
Revenue is attributed
to a campaign.
In-app
Once you send an In-app campaign to your users, it goes through the following stages in its lifecycle:
The lifecycle of an In-app Notification
Each stage is tracked as a
campaign event
or a performance indicator, helping you
analyze the campaign's impact
on user engagement, conversions, and revenue. You can also analyze the collective impact of all the campaigns sent through a channel by
analyzing In-app Overview
.
Additionally, we have also made it possible for you to identify the stage at which a campaign is currently at, for each user through
Latest Message Status.
Detected in real-time, it can be analyzed through the
List of Users
of a campaign and each
User's Profile
.
Now, let's get you acquainted with all the performance indicators tracked for_In-app campaigns:_
Impressions
Captured from your user's device, it indicates the number of times users have seen an
In-app
message, within the selected time frame.
Closes
Indicates the total number of users that have closed the
In-app Notification
after viewing it, within the selected time frame.
Clicks
Indicates the number of users that have clicked on the
In-app Notification
within the selected time frame.
Total Conversions
Indicates the total number of times users have performed the
Conversion Event
defined for an
In-app
campaign within the selected time frame.
Unique Conversions
Indicates the number of users that have converted after receiving an
In-app
campaign within the selected time frame.
👍
Fact Check
Total Conversions
can be significantly higher than the
Unique Conversions
tracked for a campaign.
Reason:
A user can choose to perform the
Conversion Event
defined for a campaign, multiple times within its
Conversion Deadline
.
For example, a user can perform the event
Checkout-Complete
twice, each time purchasing a different product after receiving your campaign.
For the same reason -
Total Conversions
can be greater than 100%.
Total Click-through Conversions
Indicates the total number of times your users have performed the
Conversion Event
of a campaign, within the selected time frame, after clicking on the
In-app Notification.
Detailed read on how this is tracked.
Unique Click-through Conversions
Indicates the number of users that have converted within the selected time frame, after clicking on the
In-app Notification.
Detailed read on how this is tracked.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign, then
Conversions
will not be tracked for it.
Detailed read on how Conversions are tracked and attributed to campaigns.
Revenue
Indicates the total amount of revenue generated by the
Total Conversions
that have occurred within the selected time frame.
Click-through Revenue
Indicates the total amount of revenue generated by the
Total Click-through Conversions
that have occurred within the selected time frame.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign or if the specified
Conversion Event
is not mapped as a
Revenue Event,
then no
Revenue
will be tracked for it.
Detailed Read on how
Revenue tracking works
and how
Revenue is attributed
to a campaign.
SMS
Once you send an SMS campaign to your users, it goes through the following stages in its lifecycle:
The lifecycle of an SMS campaign
Each stage is tracked as a
campaign event
or a performance indicator, helping you
analyze the campaign's impact
on user engagement, conversions, and revenue. You can also analyze the collective impact of all the campaigns sent through a channel by
analyzing SMS Overview
.
Additionally, we have also made it possible for you to identify the stage at which a campaign is currently at, for each user through
Latest Message Status.
Detected in real-time, it can be analyzed through the
List of Users
of a campaign and each
User's Profile
.
Now, let's get you acquainted with all the performance indicators tracked for_SMS_ campaigns:
Sent
Indicates the total number of messages sent to an
SMS
campaign's target audience within the selected time frame.
Failures (SMS)
Indicates the total number of messages that failed to get delivered to the campaign's target audience.
Here's a list of all the reasons that can cause
SMS
delivery failure:
Hard Bounce:
Indicates permanent delivery failure caused by an invalid/defunct phone number or due to the fact that the user was out of the service network area for a prolonged duration.
Sender ID Invalid/ Unverified Sender:
Indicates that the phone number or sender ID used to send the SMS to your users is invalid (based on the response received from the SSP).
IP Not Whitelisted:
Indicates that WebEngage's IP is not whitelisted with the SSP (SMS Service Provider) being used to send the campaign. Such failures can occur while using a Private SSP integration.
Detailed read.
Message Text Error:
Indicates that the campaign was sent without a message (in the body).
SSP Quota Limit Reached/ Insufficient Credits:
Indicates that the message sending limit of the SSP (SMS Service Provider) being used to send the message has been exhausted. Please get in touch with your SSP to upgrade your account or add more credits to ensure delivery.
DND Registry/ User Registered for NDNC:
Indicates failure caused by the fact that the user has registered their phone number on a
national do-not-call list
.
India DND Hours:
Promotional SMS messages can only be delivered between 9 am and 9 pm IST. Thus, all SMS campaigns sent or scheduled to be delivered within these hours will fail due to the same reason, for all numbers registered in India.
DND Queue Drop:
All messages meant to be delivered during a user's
DND hours
get queued as per the campaign's
Queueing Duration.
However, if the duration expires before a delivery window opens up, then the campaign will fail. The same is indicated by
DND Queue Drop.
Engagement Window:
If a campaign is sent with
DND Hours
enabled and no
Queueing Duration
has been specified for it, then all messages sent during a user's DND Hours will fail to get delivered. The same is indicated by
Engagement Window.
🚧
Please refer to
DND Hours
and
Queueing
for a detailed read.
Frequency Capping Queue Drop:
If the daily, weekly or monthly frequency cap has been exhausted for a user, then all additional campaigns will get queued for delayed delivery, as per each campaign's
Queueing Duration.
However, if the duration expires before a delivery window opens up, then the campaign will fail. The same is indicated by
Frequency Cap Queue Drop.
🚧
Please refer to
Frequency Capping
and
Queueing
for a detailed read.
Personalization Error:
Indicates an error with the personalization variables (user attributes, event attributes) or Nunjucks syntax used in the message copy.
Channel Not Available/ Recipient Missing:
This error is generally recorded for journeys wherein an
SMS
campaign is triggered for users who have not shared their phone number, yet.
Time Zone Elapsed:
This error is generally recorded for one-time campaigns scheduled for delivery
in the user's timezone
. If the local date and time (for a user) have already passed the delivery date and time specified for the campaign, then the message will fail to get delivered to the user.
Other Failures:
All off-beat reasons for campaign failures are clubbed under this header.
Delivered
Indicates the total number of messages that have been delivered to the target audience of a campaign, or to all users through the channel, within the selected time frame.
👍
Fact Check
Total number of
Delivered
messages =
Sent - (Failures + Queued)
Queued (SMS)
Indicates the total number of messages that have been
Sent
to a campaign's target audience, but are currently
Queued
for delayed delivery.
A few common reasons due to which
SMS
campaigns get queued include:
DND Queue:
All messages meant to be delivered during a user's DND hours get queued as per the campaign's queueing duration, indicated by
DND Queue.
Frequency Cap Queue:
If the daily, weekly or monthly frequency cap has been exhausted for a user, then all additional campaigns will get queued for delayed delivery, as per each campaign's queueing duration. This is indicated by
Frequency Cap Queue.
Waiting for Time Zone:
If you have scheduled a one-time SMS campaign for delivery
in the user's timezone
, then the message will get queued for all users where the specified time of delivery is yet to occur in their local time zone. The same is indicated by
Waiting for Time Zone.
If the
Queueing Duration
of a campaign expires before the message could be delivered to a user, then the message will
fail
.
Total Clicks
Indicates the total number of times users have clicked on a link included in the SMS campaign, within the selected time frame. This means that if a user clicks 3 times on a link in the message, then each interaction (click) will be counted once each towards
Total Clicks.
Unique Clicks
Indicates the number of users that have clicked on a link included in the
SMS
campaign, within the selected time frame.
Total Conversions
Indicates the total number of times users have performed the
Conversion Event
of an
SMS
campaign within the selected time frame.
Unique Conversions
Indicates the number of users that have performed the
Conversion Event
of an
SMS
campaign within the selected time frame.
👍
Fact Check
Total Conversions
can be significantly higher than the
Unique Conversions
tracked for a campaign.
Reason:
A user can choose to perform the
Conversion Event
defined for a campaign multiple times within its
Conversion Deadline
.
For example, a user can perform the event
Checkout-Complete
twice, each time purchasing a different product after receiving your campaign.
For the same reason -
Total Conversions
can be greater than 100%.
Total Click-through Conversions
Indicates the total number of times users have performed the
Conversion Event
of a campaign after clicking on a link included in the
SMS,
within the selected time frame.
Detailed read on how this is tracked.
Unique Click-through Conversions
Indicates the number of users that have performed the
Conversion Event
of a campaign after clicking on a link included in the
SMS,
within the selected time frame.
Detailed read on how this is tracked.
🚧
Related Read
If you have not specified a
Conversion Event
for a campaign, then
Conversions
will not be tracked for it.
Detailed read on how Conversions are tracked and attributed to a campaign.
Revenue
Indicates the total amount of revenue generated by the
Total Conversions
that have occurred within the selected time frame of analysis.
Click-through Revenue
Indicates the total amount of revenue generated by the
Total Click-through Conversions
that have occurred within the selected time frame.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign or if the specified
Conversion Event
is not mapped as a
Revenue Event,
then no
Revenue
will be tracked for it.
Detailed Read on how
Revenue tracking works
and how
Revenue is attributed
to a campaign.
On-site Notification
Once you send an
On-site Notification
to your users, it goes through the following stages in its lifecycle:
The lifecycle of an On-site Notification
Each stage is tracked as a
campaign event
or a performance indicator, helping you analyze the campaign's impact on user engagement, conversions, and revenue.
Let's get you acquainted with all the performance indicators tracked for_On-site (Notifications)_:
Total Views
Indicates the total number of times users viewed the
On-site Notification.
Unique Views
Indicates the number of users who viewed the
On-site Notification
at least once.
Closed
Indicates the total number of users that dismissed the
On-site Notification
after seeing it.
Total Clicks
Indicates the total number of times users clicked on the notification (including button clicks).
CTA Clicks
Indicates the total number of times users clicked on the call-to-action button.
Click-through Rate
Indicates the share of users that clicked on the notification after viewing it.
👍
Fact Check
Click-through Rate = (Total Clicks/ Unique Views) x 100
Conversions
Indicates the total number of users that performed the campaign's
Conversion Goal (as defined in
Step 4: Activate
).
On-site Surveys
Once you activate a
Survey,
it goes through the following stages in its lifecycle:
The lifecycle of a Survey Questionnaire
Let's get you acquainted with all the performance indicators tracked for your_Surveys_:
Displayed
Indicates the total number of times users have viewed the survey on your website.
Attempted
Indicates the total number of users engaged through the survey questionnaire.
Submitted
Indicates the total number of users that have successfully submitted their responses.
Response Rate
Indicates the share of users that submitted their responses after viewing your survey.
👍
Fact Check
Response Rate
=
(Submitted / Displayed)
x 100
Web Push
Once you send a
Web Push campaign
to your users, it goes through the following stages in its lifecycle:
The lifecycle of a Web Push Notification
Each stage is tracked as a
campaign event
or a performance indicator, helping you
analyze the campaign's impact
on user engagement, conversions, and revenue. You can also analyze the collective impact of all the campaigns sent through the channel by
analyzing Web Push Overview
.
Additionally, we have also made it possible for you to identify the stage at which a campaign is currently at, for each user through
Latest Message Status.
Detected in real-time, it can be analyzed through the
List of Users
of a campaign and each
User's Profile
.
Now, let's get you acquainted with all the performance indicators tracked for_Web Push_ campaigns:
Sent
Indicates the total number of messages sent to a
Web Push
campaign's target audience within the selected time frame.
Failures (Web Push)
Indicates the total number of messages that failed to get delivered to a campaign's target audience.
Here's a list of all the reasons due to which a
Web Push
could fail to get delivered:
Unsubscribed:
Indicates that a user has blocked notifications from your website in their browser settings.
DND Queue Drop:
All messages meant to be delivered during a user's DND hours get queued as per the campaign's queueing duration. However, if the duration expires before a delivery window opens up, then the campaign will fail. Such failures are indicated by
DND Queue Drop.
🚧
Please refer to
DND Hours
and
Queueing
for a detailed read.
Frequency Cap Queue Drop:
If the daily, weekly or monthly frequency cap has been exhausted for a user, then all additional campaigns will get queued for delayed delivery, as per each campaign's queueing duration. However, if the duration expires before a delivery window opens up, then the campaign will fail. Such failures are indicated by
Frequency Cap Queue Drop.
🚧
Please refer to
Frequency Capping
and
Queueing
for a detailed read.
Personalization Error:
Indicates an error in the personalization variables (user attributes, event attributes) or Nunjucks syntax used in the web push notification's copy.
Device Not Registered/ No Device:
Indicates any of the following errors:
Delay in Registering Device:
A device is registered and available for delivering web push notifications as soon as we receive it's subscription details from Vapid service networks. The first time a user opts-in to receive web push notifications, it takes a few seconds to a minute for us to glean these details. Thus, if campaign delivery is attempted before the device is registered, then it will fail to get delivered.
Incorrect Integration with WebEngage:
if there is a technical glitch in the way the WebEngage SDK has been integrated with your website, then all web push notifications will fail to get delivered to your users. Detailed read on
how to integrate WebEngage with your website.
Channel Not Available:
This error is generally recorded for journeys wherein a
Web Push
campaign is triggered for users who are not reachable through the channel, yet.
🚧
Ptease Note
Please refer to
Channels and Channel Reachability
for a detailed read on how reachability is determined for users in various scenarios.
Time Zone Elapsed:
This error is generally recorded for one-time campaigns scheduled for delivery
in the user's timezone
. If the local time (for a user) has already passed the delivery time specified for the campaign, then the message will fail to get delivered to the user.
Other Failures:
All off-beat reasons for campaign failures are clubbed under this header.
Delivered
Indicates the total number of messages that have been delivered to the target audience of a campaign within the selected time frame.
👍
Fact Check
Total number of
Delivered
messages =
Sent - (Failures + Queued)
Queued (Web Push)
Indicates the total number of messages that have been
Sent
to a campaign's target audience, but are currently
Queued
for delayed delivery.
A few common reasons due to which campaigns get queued include:
DND Queue:
All messages meant to be delivered during a user's DND hours get queued as per the campaign's queueing duration, indicated by
DND Queue.
Frequency Cap Queue:
If the daily, weekly or monthly frequency cap has been exhausted for a user, then all additional campaigns will get queued for delayed delivery, as per each campaign's queueing duration. The same is indicated by
Frequency Cap Queue.
Waiting for Time Zone:
If you have scheduled a one-time push campaign for delivery
in the user's timezone
, then the message will get queued for all users where the specified time of delivery is yet to occur in their local time zone. The same is indicated by
Waiting for Time Zone.
If the
Queueing Duration
of a campaign expires before the message could be delivered to a user, then the message will
fail
.
Total Impressions
Captured from your user's device, it indicates the number of times your users have seen a
Web Push Notification
within the selected time frame.
Unique Impressions
Captured from your user's device, it indicates the number of users that have seen a
Web Push Notification
at least once within the selected time frame.
Total/Unique Dismisses
Both metrics indicate the number of users who have dismissed a
Web Push Notification
within the selected time frame.
Unsubscribers
All users who have disabled notifications for your domain in their browser settings within the selected time frame are considered towards the total number of
Unsubscribes.
Total/Unique Clicks
Both metrics indicate the number of users that have clicked on a
Web Push Notification
within the selected time frame.
Total Conversions
Indicates the total number of times users have performed the
Conversion Event
defined for a
Web Push
campaign within the selected time frame.
Unique Conversions
Indicates the number of users that have performed the
Conversion Event
defined for a
Web Push
campaign within the selected time frame.
👍
Fact Check
Total Conversions
can be significantly higher than the
Unique Conversions
tracked for a campaign.
Reason:
A user can choose to perform the
Conversion Event
defined for a campaign multiple times within its
Conversion Deadline
.
For example, a user can perform the event
Checkout-Complete
twice, each time purchasing a different product after receiving your campaign.
For the same reason -
Total Conversions
can be greater than 100%.
Total Click-through Conversions
Indicates the total number of times users have performed the
Conversion Event
of a
Web Push
campaign after clicking on it, within the selected time frame.
Detailed read on how this is tracked.
Unique Click-through Conversions
Indicates the number of users that have performed the
Conversion Event
of a
Web Push
campaign after clicking on it, within the selected time frame.
Detailed read on how this is tracked.
Total Impression-through Conversions
Indicates the total number of times users have performed the
Conversion Event
of a
Web Push
campaign after viewing it, within the selected time frame.
Detailed read on how this is tracked.
Unique Impression-through Conversions
Indicates the number of users that have performed the
Conversion Event
of a
Web Push
campaign after viewing it, within the selected time frame.
Detailed read on how this is tracked.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign, then
Conversions
will not be tracked for it.
Detailed read on how Conversions are tracked and attributed to a campaign.
Revenue
Indicates the total amount of revenue generated by the
Total Conversions
that have occurred within the selected time frame of analysis.
Click-through Revenue
Indicates the total amount of revenue generated by the
Total Click-through Conversions
that have occurred within the selected time frame.
Impression-through Revenue
Indicates the total amount of revenue generated by the
Total Impression-through Conversions
that have occurred within the selected time frame.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign or if the specified
Conversion Event
is not mapped as a
Revenue Event,
then
Revenue
will not be tracked for it.
Detailed Read on how
Revenue tracking works
and how
Revenue is attributed
to a campaign.
Email
Once you send an
Email campaign
to your users, it goes through the following stages in its lifecycle:
The lifecycle of an Email campaign
Each stage is tracked as a
campaign event
or a performance indicator, helping you
analyze the campaign's impact
on user engagement, conversions, and revenue. You can also analyze the collective impact of all the campaigns sent through the channel by
analyzing Email Overview
.
Additionally, we have also made it possible for you to identify the stage at which a campaign is currently at, for each user through
Latest Message Status.
Detected in real-time, it can be analyzed through the
List of Users
of a campaign and each
User's Profile
.
Now, let's get you acquainted with all the performance indicators tracked for_Email_ campaigns:
Sent
Indicates the total number of messages that have been sent to an
Email
campaign's target audience.
Failures (Email)
Indicates the total number of messages that failed to get delivered to the campaign's target audience.
Here's a list of all the reasons due to which an
Email
campaign could fail:
Hard Bounce:
Indicates permanent delivery failure caused by an invalid or defunct email address or in cases where the email was rejected by the user's mail server due to technical reasons.
Once a hard bounce is recorded for an email address registered to a user, the user is deemed
unreachable
through the channel.
ESP Quota Limit Reached/ Insufficient Credits:
Indicates that the message sending limit of the ESP (Email Service Provider) being used to send the email has been exhausted. Please get in touch with your ESP to upgrade your account or add more credits to ensure delivery.
Sender ID Invalid/ Unverified Sender:
Indicates Indicates that the
Email Address
or
Sender ID
being used to send the SMS to your users is invalid (based on the response received from the ESP).
Please recheck the
Sender ID
and
Email Address
registered in your ESP account and the credentials entered while integrating the ESP with your WebEngage account.
Unsubscribed:
Each time a user chooses to unsubscribe to your emails, it's recorded as an
Unsubscribe
by your ESP. Thus, the next time you sent an email campaign to the user, the ESP will not attempt to deliver it and will convey
Unsubscribed
as the reason for failure.
Once a user unsubscribes, they are deemed
unreachable
through the channel.
DND Queue Drop:
All messages meant to be delivered during a user's
DND hours
get queued as per the campaign's
Queueing Duration.
However, if the duration expires before a delivery window opens up, then the campaign will fail. Such failures are indicated by
DND Queue Drop.
Engagement Window:
If a campaign is sent with
DND Hours
enabled and no
Queueing Duration
has been specified for it, then all messages sent during a user's
DND Hours
will fail to get delivered. The same is indicated by
Engagement Window.
🚧
Please refer to
DND Hours
and
Queueing
for a detailed read.
Frequency Cap Queue Drop:
If the daily, weekly or monthly frequency cap has been exhausted for a user, then all additional campaigns will get queued for delayed delivery, as per each campaign's queueing duration. However, if the duration expires before a delivery window opens up, then the campaign will fail. Such failures are indicated by
Frequency Cap Queue Drop.
🚧
Please refer to
Frequency Capping
and
Queueing
for a detailed read.
Personalization Error:
Indicates an error with the personalization variables (user attributes, event attributes) or Nunjucks syntax used in the email's copy.
Invalid Attachment URL:
Indicates an error with the personalization variables used to personalize your dynamic email attachment or record failures in cases where the attachment was not found for a user.
Channel Not Available/ Recipient Missing:
This error is generally recorded for journeys wherein an
Email
campaign is triggered for users who have not shared their email address, yet.
Time Zone Elapsed:
This error is generally recorded for one-time campaigns scheduled for delivery
in the user's timezone
. If the local date and time (for a user) have already passed the delivery date and time specified for the campaign, then the message will fail to get delivered to the user.
Template Error:
Indicates an error with the custom HTML template used in the email's copy.
Internal Error:
Indicates an error in sending the message to the ESP (Email Service Provider) being used to send the email campaign. This could happen due to any of the following reasons:
The ESP's server is down.
The connection with the ESP timed-out, and so on.
In such cases, we suggest that you check with your ESP regarding the failure or try an alternate ESP to the send the campaign.
Here's how you can integrate various ESPs with your account.
Other Failures:
All off-beat reasons for campaign failures are clubbed under this header.
Delivered
Indicates the total number of messages that have been delivered to the target audience of a campaign within the selected time frame.
👍
Fact Check
Total number of
Delivered
messages =
Sent - (Failures + Queued)
Queued (Email)
Indicates the total number of messages that have been
Sent
to a campaign's target audience, but are currently
Queued
for delayed delivery.
A few common reasons due to which campaigns get queued include:
DND Queue:
All messages meant to be delivered during a user's DND hours get queued as per the campaign's queueing duration, indicated by
DND Queue.
Frequency Cap Queue:
If the daily, weekly or monthly frequency cap has been exhausted for a user, then all additional campaigns will get queued for delayed delivery, as per each campaign's queueing duration. This is indicated by
Frequency Cap Queue.
Waiting for Time Zone:
If you have scheduled a one-time push campaign for delivery
in the user's timezone
, then the message will get queued for all users where the specified time of delivery is yet to occur in their local time zone. The same is indicated by
Waiting for Time Zone.
Soft Bounces:
In cases where your ESP is unable to deliver emails to a user due to temporary roadblocks, it gets queued for delayed delivery as per the campaign/journey's queueing settings. A few common reasons for soft bounces include:
the mailbox was full
the server was down
the message was too large for the recipient's inbox and so on.
If the
Queueing Duration
of a campaign expires before the message could be delivered to a user, then the message will
fail
.
Unsubscribes
Indicates the total number of users that unsubscribed to your channel by clicking the
Unsubscribe link
in your email within the selected time frame.
Spam Reports
Indicates the total number of users that have marked your
Email
campaign as spam in their inbox, within the selected time frame.
Total Opens
Indicates the total number of times users have opened an
Email
within the selected time frame. This means if a user opens an email campaign 5 times, then 5 interactions (opens) will be counted towards
Total Opens.
Unique Opens
Indicates the number of users that have opened an
Email
within the selected time frame. Thus, irrespective of the number of times a user has opened an email, they will be counted towards
Unique Opens
only once.
Total Clicks
Indicates the total number of times users have clicked on a link included in your
Email
within the selected time frame.
Unique Clicks
Indicates the number of users that have clicked on a link included in your
Email
within the selected time frame.
Total Conversions
Indicates the total number of times a user has performed the
Conversion Event
of an
Email
campaign within the selected time frame.
Unique Conversions
Indicates the number of users that have converted after receiving an
Email
campaign within the selected time frame.
👍
Fact Check
Total Conversions
can be significantly higher than the
Unique Conversions
tracked for a campaign.
Reason:
A user can choose to perform the
Conversion Event
defined for a campaign multiple times within its
Conversion Deadline
.
For example, a user can perform the event
Checkout-Complete
twice, each time purchasing a different product after receiving your campaign.
For the same reason -
Total Conversions
can be greater than 100%.
Total Open-through Conversions
Indicates the total number of times users have performed the
Conversion Event
of an
Email
campaign after opening it within the selected time frame.
Detailed read on how this is tracked.
Unique Open-through Conversions
Indicates the number of users that have performed the
Conversion Event
of an
Email
campaign after opening it within the selected time frame.
Detailed read on how this is tracked.
Total Click-through Conversions
Indicates the total number of times users have performed the
Conversion Event
of an
Email
campaign after clicking on it, within the selected time frame.
Detailed read on how this is tracked.
Unique Click-through Conversions
Indicates the number of users that have performed the
Conversion Event
of an
Email
campaign after clicking on it, within the selected time frame.
Detailed read on how this is tracked.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign, then
Conversions
will not be tracked for it.
Detailed read on how Conversions are tracked and attributed to a campaign.
Revenue
Indicates the total amount of revenue generated by the
Total Conversions
that have occurred within the selected time frame.
Open-through Revenue
Indicates the total amount of revenue generated by the
Total Open-through Conversions
that have occurred within the selected time frame.
Click-through Revenue
Indicates the total amount of revenue generated by the
Total Click-through Conversions
that have occurred within the selected time frame.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign or if the specified
Conversion Event
is not mapped as a
Revenue Event,
then
Revenue
will not be tracked for it.
Detailed Read on how
Revenue tracking works
and how
Revenue is attributed
to a campaign.
WhatsApp
Once you send a WhatsApp campaign, it goes through the following stages in its lifecycle:
The lifecycle of a WhatsApp campaign
Let's get you acquainted with all the performance indicators tracked for WhatsApp campaigns:
Sent
Indicates the total number of messages sent to a WhatsApp campaign's target audience, within the selected time frame.
Failures (WhatsApp)
Indicates the total number of messages that failed to get delivered to a campaign's target audience, within the selected time frame.
Here's a list of all the reasons due to which a WhatsApp campaign could fail:
Invalid WhatsApp Number:
Indicates that the phone number (to which the message was sent) is not registered with WhatsApp.
Message Format Error:
Indicates that the message (added while creating the campaign) has errors in it. A few common reasons include:
Extra characters were added to a whitelisted template.
Personalization variables were not added properly.
Template Does Not Exist:
Indicates that the message template uploaded to WebEngage has not been approved by WhatsApp.
All message templates must be whitelisted with WhatsApp before you can start using them in your campaigns and must not be edited once approved.
Throttling Error:
Indicates that your WSP was receiving a high number of messages per second/minute/hour from your WebEngage account due to which a few messages were dropped.
User Blocked Messages:
Indicates that the user from the campaign's target audience has blocked your channel on WhatsApp.
User Did Not Initiate Session:
Indicates that a user from the campaign's target audience did not initiate the WhatsApp chat session with you and thus, will be contacted.
User Offline:
Indicates that the message could not be delivered as the user remained offlines for a prolonged duration.
WSP Configuration Error:
Indicates an error in the WhatsApp Service Provider integration with your WebEngage account.
Please head over to the
Intergations < Channels < WhatsApp section
in your dashboard to review and rectify the integration. Please get in touch with your WSP or drop in a few lines at
[email protected]
for assistance.
WSP Quota Limit Reached:
Indicates that the message sending limit of the
WSP (WhatsApp Service Provider)
being used to send the campaign has been exhausted. Please get in touch with your WSP to upgrade your account or add more credits to ensure delivery.
DND Queue Drop:
All messages meant to be delivered during a user's
DND hours
get queued as per the campaign's/ journey's
Queueing Duration.
However, if the duration expires before a delivery window opens up, then the campaign will fail. Such failures are indicated by
DND Queue Drop.
🚧
Please refer to
DND Hours
and
Queueing
for a detailed read.
Frequency Capping Queue Drop:
If the daily, weekly or monthly frequency cap has been exhausted for a user, then all additional campaigns will get queued for delayed delivery, as per each campaign's/ journey's
Queueing Duration.
However, if the duration expires before a delivery window opens up, then the campaign will fail. Such failures are indicated by
Frequency Cap Queue Drop.
🚧
Please refer to
Frequency Capping
and
Queueing
for a detailed read.
Personalization Error:
Indicates an error with the personalization variables
(
User Attributes
,
Event Attributes
)
or Nunjucks syntax used in the message copy.
Channel Not Available/ Recipient Missing:
This error is generally recorded for journeys wherein a WhatsApp campaign is triggered for users who have not shared their phone number, yet.
Time Zone Elapsed:
This error is generally recorded for one-time campaigns scheduled for delivery
in the user's timezone
. If the local date and time (for a user) have already passed the delivery date and time specified for the campaign, then the message will fail to get delivered to the user.
Undelivered (Only if
Infobip is your WSP
):
Indicates that Infobip was unable to deliver the message due to any of the following reasons:
The message has been received by the WSP, but the user's device is out of network coverage area. Hence, it could not be delivered.
The message has been sent to the user's mobile operator, but it failed to deliver it to them.
The message has been rejected by the user's mobile operator.
Other Failures:
All off-beat reasons for campaign failures are clubbed under this header.
Delivered
Indicates the total number of messages that have been delivered to the target audience of a campaign within the selected time frame.
👍
Fact Check
Total number of
Delivered
messages =
Sent - (Failures + Queued)
Queued (WhatsApp)
Indicates the total number of messages that have been
Sent
to a campaign's target audience, but are currently
Queued
for delayed delivery.
A few common reasons due to which campaigns get queued include:
DND Queue:
All messages meant to be delivered during a user's DND hours get queued as per the campaign's queueing duration, indicated by
DND Queue.
Frequency Cap Queue:
If the daily, weekly or monthly frequency cap has been exhausted for a user, then all additional campaigns will get queued for delayed delivery, as per each campaign's queueing duration. This is indicated by
Frequency Cap Queue.
Waiting for Time Zone:
If you have scheduled a one-time WhatsApp campaign for delivery
in the user's timezone
, then the message will get queued for all users where the specified time of delivery is yet to occur in their local time zone. The same is indicated by
Waiting for Time Zone.
If the
Queueing Duration
of a campaign expires before the message could be delivered to a user, then the message will
fail
.
Read (Unique)
Indicates the number of users that have viewed or 'read' your WhatsApp message at least once within the selected time frame.
Total Clicks
Indicates the total number of times users have clicked on a link included in the WhatsApp message, within the selected time frame. This means that if a user clicks 3 times on a link, then each interaction (click) will be counted once each towards
Total Clicks.
Unique Clicks
Indicates the number of users that have clicked on a link included within the WhatsApp message within the selected time frame.
Total Conversions
Indicates the total number of times users have performed the
Conversion Event
of a WhatsApp campaign within the selected time frame.
Unique Conversions
Indicates users that have performed the
Conversion Event
of a WhatsApp campaign at least once, within the selected time frame.
👍
Fact Check
Total Conversions
can be significantly higher than the
Unique Conversions
tracked for a campaign.
Reason:
A user can choose to perform the
Conversion Event
defined for a campaign/journey multiple times within its
Conversion Deadline
.
For example, a user can perform the event
Checkout-Complete
twice, each time purchasing a different product after receiving your campaign.
For the same reason -
Total Conversions
can be greater than 100%.
Total Read-through Conversions
Indicates the total number of times users have performed the
Conversion Event
of a
WhatsApp
campaign after viewing it, within the selected time frame.
Detailed read on how this is tracked.
Unique Read-through Conversions
Indicates the number of users that have performed the
Conversion Event
of a
WhatsApp
campaign after viewing it, within the selected time frame.
Detailed read on how this is tracked.
Total Click-through Conversions
Indicates the total number of times users have performed the
Conversion Event
of a
WhatsApp
campaign after clicking on a link included in the message, within the selected time frame.
Detailed read on how this is tracked.
Unique Click-through Conversions
Indicates the number of users that have performed the
Conversion Event
of a
WhatsApp
campaign after clicking on a link included in the message, within the selected time frame.
Detailed read on how this is tracked.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign, then
Conversions
will not be tracked for it.
Detailed read on how Conversions are tracked and attributed to a campaign.
Revenue
Indicates the total amount of revenue generated by the
Total Conversions
that have occurred within the selected time frame of analysis.
Click-through Revenue
Indicates the total amount of revenue generated by the
Total Click-through Conversions
that have occurred within the selected time frame.
Read-through Revenue
Indicates the total amount of revenue generated by the
Total Read-through Conversions
that have occurred within the selected time frame.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign/journey or if the specified
Conversion Event
is not mapped as a
Revenue Event,
then no
Revenue
will be tracked for it.
Detailed Read on how
Revenue tracking works
and how
Revenue is attributed
to a campaign.
Web Personalization
At WebEngage, we believe that data-driven messaging is one of the most scientific ways to deliver contextual experiences tailored to each user. This is why we have identified a list of all the generic actions users can perform while interacting with campaigns sent through Web Personalization and track them as
Campaign Events
.
Thus, each time you send a campaign, we automatically track several performance indicators or campaign events like
Deliveries, Failures, Opens, Impressions, Dismisses, Unsubscribes, Clicks, and so on,
helping you gauge its impact in real-time!
🚧
For Your Reference
Here's a
list of System (Campaign) Events
gleaned for each channel post-integration.
Now, let's walk you through the performance indicators that help you analyze the impact of each Web Personalization campaign across your dashboard.
Once you send a Web Personalization campaign to your user, it goes through the following stages in its lifecycle:
Each stage is tracked as a
campaign event
or a performance indicator, helping you
analyze the campaign's impact
on user engagement, conversions, and revenue. You can also analyze the collective impact of all the campaigns sent through a channel by
analyzing Web Personalization Overview
.
Additionally, we have also made it possible for you to identify the stage at which a campaign is currently at for each user through
Latest Message Status.
Detected in real-time, it can be analyzed through the
List of Users
of a campaign and each
User's Profile
.
Now, let's get you acquainted with all the performance indicators tracked for_Web Personalization campaigns:_
Impressions
Captured from your user's device, it indicates the number of times users have seen a
Web Personalization
banner within the selected time frame.
Clicks
Indicates the number of users that have clicked on the
Web Personalization Banner
within the selected time frame.
Total Conversions
Indicates the total number of times users have performed the _
Conversion Event
_defined for a
Web Personalization
campaign within the selected time frame.
Unique Conversions
Indicates the number of users converted after receiving a
Web Personalization
campaign within the selected time frame.
👍
Fact Check
Total Conversions
can be significantly higher than the
Unique Conversions
tracked for a campaign.
Reason:
A user can choose to perform the
Conversion Event
defined for a campaign, multiple times within its
Conversion Deadline
.
For example, a user can perform the event
Checkout-Complete
twice, each time purchasing a different product after receiving your campaign.
For the same reason -
Total Conversions
can be greater than 100%.
Total Click-through Conversions
Indicates the total number of times your users have performed the
Conversion Event
of a campaign, within the selected time frame, after clicking on the
Web Personalization Banner.
Detailed read on how this is tracked.
Unique Click-through Conversions
Indicates the number of users that have converted within the selected time frame after clicking on the
Web Personalization Banner.
Detailed read on how this is tracked.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign, then
Conversions
will not be tracked for it.
Detailed read on how Conversions are tracked and attributed to campaigns.
Revenue
Indicates the total amount of revenue generated by the
Total Conversions
that have occurred within the selected time frame.
Click-through Revenue
Indicates the total amount of revenue generated by the
Total Click-through Conversions
that have occurred within the selected time frame.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign or if the specified
Conversion Event
is not mapped as a
Revenue Event,
then no
Revenue
will be tracked for it.
Detailed Read on how
Revenue tracking works
and how
Revenue is attributed
to a campaign.
App In-line Content
Now, let's get you acquainted with all the performance indicators tracked for:
Impressions
Captured from your user's device, it indicates the number of times users have seen a
App In-line Content
within the selected time frame.
Clicks
Indicates the number of users that have clicked on the
App In-line campaign
within the selected time frame.
Total Conversions
Indicates the total number of times users have performed the _
Conversion Event
_defined for a
App In-line
campaign within the selected time frame.
Unique Conversions
Indicates the number of users converted after receiving a
App In-line
campaign within the selected time frame.
Total Click-through Conversions
Indicates the total number of times your users have performed the
Conversion Event
of a campaign, within the selected time frame, after clicking on the
App In-line campaign.
Detailed read on how this is tracked.
Unique Click-through Conversions
Indicates the number of users that have converted within the selected time frame after clicking on the
App In-line campaign.
Detailed read on how this is tracked.
🚧
Please Note
If you have not specified a
Conversion Event
for a campaign, then
Conversions
will not be tracked for it.
Detailed read on how Conversions are tracked and attributed to campaigns.
Revenue
Indicates the total amount of revenue generated by the
Total Conversions
that have occurred within the selected time frame.
Click-through Revenue
Indicates the total amount of revenue generated by the
Total Click-through Conversions
that have occurred within the selected time frame.
We hope this has equipped you with a robust understanding of all the performance indicators tracked for each channel. Please feel free to drop in a few lines at
[email protected]
in case you have any related queries or feedback. We're always just an email away!
Updated
4 months ago
Revenue Tracking
Campaign Variations and Multivariate Testing
Copy Page
