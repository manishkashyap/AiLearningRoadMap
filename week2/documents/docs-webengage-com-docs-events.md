# Events

- URL: https://docs.webengage.com/docs/events
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Overview
Events
❗️
Update 23rd April 2026
We've updated the Event names for system events across all channels for clarity.
See the full list of changes
.
All behavioral data points are called
Events
in your dashboard. And each
Event can further be understood in the context of its Attributes
which includes details like
time, location, device details, price, quantity,
and so on.
This enables you to gain in-depth insights into user interactions across your app, website, and channels. You can also leverage this data to segment users, personalize messages and configure campaign targeting.
Events
📘
The term
Event
refers to all the actions performed by users while interacting with your mobile apps, website and campaigns.
For example, if a user needs to click on a product to view its details, then it is advisable to track this action as the
Event, Product Viewed
as it brings them a step closer to making a purchase.
Events
are classified into 2 categories in WebEngage:
System Events
:
Pre-defined by WebEngage, automatically tracked for platforms post intergation.
Custom Events
:
Defined by you for each platform and tracked through the respective SDKs.
Let's walk you through this.
System Events
We have pre-defined several generic actions that users can perform while interacting with your app, website and campaigns. These actions are referred to as
System Event
and are automatically tracked for your platforms once you integrate them with your WebEngage account.
Here's a list of all the
System Events
that are automatically tracked for all your users post integration:
Name on Dashboard
Name in Backend
Description
App Installed
app_installed
When the app is installed and launched for the first time.
App Upgraded
app_upgraded
When the app is upgraded.
App Crashed
app_crashed
When the app crashes.
App Uninstalled
app_uninstalled
When app is uninstalled.
User Login
user_logged_in
Whenever you call the login function on user login, signup etc.
User Logout
user_logged_out
Whenever you call the logout function.
Session Started
user_session_started
Whenever a new session is started by your user.
(Here's what a session means in WebEngage)
Campaign Conversion
goal_accomplish
When a user performs the
Conversion Event
defined for a campaign or journey.
GCM or APNs Registered
gcm_registered
When a device is registered successfully to receive
Push Notifications
.
APNs Registration Failed
apns_registration_failed
When an iOS device fails to get registered for receiving
Push Notifications
.
Push (Mobile) Sent
gcm_notification_response
When a
Push Notification
is sent to FCM for delivery by WebEngage.
Push (Web & Mobile) Queued
push_notification_queued
When a
Mobile Push Notification
is Queued for delivery by WebEngage to FCM. OR When a
Web Push Notification
is
Queued
for delivery to our VAPID server.
Push (Web) Accepted
push_notification_accepted
When a
Web Push Notification
is sent to our VAPID server for delivery by WebEngage.
Push (Web & Mobile) Rejected
push_notification_rejected
When a
Mobile Push Notification
is rejected by FCM. OR When a
Web Push Notification
is rejected by our VAPID server.
Push (Mobile) Received
push_notification_received
When a device successfully receives a
Mobile Push Notification
.
Push (Web & Mobile) Dismiss
push_notification_close
When a user dismisses a
Mobile Push Notification
or
Web Push Notification.
Push (Web & Mobile) Impression
push_notification_view
When our system renders a
Mobile Push Notification
or
Web Push Notification.
Push (Web & Mobile) Click
push_notification_click
When a user clicks a
Mobile Push Notification
or
Web Push Notification.
Push (Mobile) Rating Submitted
push_notification_rating_submitted
When a user submits a rating for a
Rating-style Push Notification
.
Push (Mobile) Carousel Item Viewed
push_notification_item_view
When a user views the images of a
Carousel-style Push Notification
.
Notification (On-site & In-app) Impression
notification_view
When a user views an
On-site Notification
or an
In-app Notification.
Notification (On-site & In-app) Close
notification_close
When a user closes an
On-site Notification
or an
In-app Notification.
Notification (On-site & In-app) Click
notification_click
When a user clicks on an
On-site Notification
or an
In-app Notification.
On-site Feedback View
feedback_view
When a user views the
On-site Feedback Widget.
On-site Feedback Close
feedback_close
When a user closes the
On-site Feedback Widget.
On-site Feedback Submit
feedback_submit
When a user submits
Feedback
through the widget.
On-site Survey View
survey_view
When a user views an
On-site Survey.
On-site Survey Close
survey_close
When a user closes an
On-site Survey.
On-site Survey Complete
survey_complete
When a user completes an
On-site Survey.
On-site Survey Submit
survey_submit
When a user submits an
On-site Survey.
SMS Queued
sms_queued
When an
SMS is Queued
for delivery by WebEngage to an
SSP
.
SMS Accepted
sms_accepted
When an SSP accepts the SMS sent by WebEngage for delivery to the customer.
SMS Rejected
sms_rejected
When an SSP rejects the SMS sent by WebEngage for delivery to the customer.
SMS Sent
sms_sent
When an SSP send the message to your user's network provider for delivery.
SMS Failed
sms_failed
When an SSP reports
delivery failure for an SMS
sent to a user.
SMS Click
sms_click
When a user clicks on a link in a SMS.
Email Queued
email_queued
When an
Email is Queued
for delivery by WebEngage to an
ESP
.
Email Accepted
email_accepted
When an ESP accepts the email sent by WebEngage for delivery to the customer.
Email Attempted
email_attempted
When an ESP has attempted to send a email WebEngage to the customer.
Email Rejected
email_rejected
When an ESP rejects the email sent by WebEngage for delivery to the customer.
Email Processed
email_processed
When an ESP receives the email sent by WebEngage for delivery to the customer.
Email Sent
email_sent
When an ESP sends the email to your user. Subsequently, the message may or may not get delivered. (Due to hard-bounces and soft-bounces).
Email Bounced
email_bounce
When an email is bounced back from the user's inbox, as reported by the ESP.
Email Delivered
email_delivered
When the email is successfully received by a user, as reported by the ESP.
Email Complaint
email_complaint
When a user or an inbox provider like Gmail complains about the email (in case of phishing etc.).
Email Abuse Report
email_abusereport
When a user marks your email as Spam.
Email Resubscribe
email_resubscribe
When a user subscribes again to receive emails from you.
Email Unsubscribe
email_unsubscribe
When a user unsubscribes to your emails.
Email Spam Report
email_spam
When a user marks an email as Spam.
Email Open
email_open
When a user opens your email.
Email Click
email_click
When a user clicks on a link embedded in the email.
Push (Web) Registered OR Web Push Subscribe Process - Device Registered / User Login
push_notification_registered
When a user subscribes to your
Web Push Notifications
by clicking
Allow
on the native browser prompt
When Session Starts or User Logins or User Logouts or Session Resets: Since in all these cases, the
LUID
changes and the WebSDK reloads, the event is fired to map the latest
LUID
with a valid subscription token.
Main purpose is to map a reachable subscription token to a valid
LUID
or
CUID
.
Event originates from the end-user’s
service-worker
file and can be fired if the end-user is on the webpage or from the
service-worker
running in the background.
Push (Web) Unregistered
push_notification_unregistered
When a user revokes Web Push permission for your site through their browser settings.
(Event is fired at end-user’s
service-worker
file)
When the server returns the error, token not present or Token updates
(Event is fired at end-user’s
service-worker
file for older tokens that get unsubscribed)
When a user logs out of their account
(Event is fired to indicate that the user is no longer reachable on the device-browser).
When message delivery fails
(Event is fired at
web-push-sender-service
at WebEngage’s backend for tokens that get invalidated by FCM)
Web Push Subscribe Viewed
push_notification_window_view
When a user views the native browser prompt that requests them to subscribe to
Web Push Notifications. (Event is fired at end-user’s
service-worker
file)
Web Push Subscribe Denied
push_notification_window_denied
When a user clicks
Deny
or
Block
on the native browser Web Push opt-in prompt.
Web Push Subscribe Successful
push_notification_subscribe_notification_allowed
When a user subscribes to your
Web Push Notifications
by clicking
Allow
on the native browser prompt.
This should be followed by the event,
Push (Web) Registered
given that the end-user’s
service-worker
is in a healthy state.
Please Note:
* No. of times
Push (Web) Registered
is fired will always be higher than
Web Push Subscribe Successful
as the former is fired in addition to fresh subscriptions. In most cases, discrepancies can be traced back to an integration issue with end-user’s
service-worker
file.
Web Push Subscribe Notification Viewed
push_notification_prompt_view
When a user views the
On-site Notification prompt
prompt that requests for permission to display the
native browser Web Push opt-in prompt.
Web Push Subscribe Notification Denied
push_notification_prompt_denied
When a user clicks
Deny
or
Block
on the
On-site Notification prompt
requesting them to display the
native browser Web Push opt-in prompt.
Web Push Subscribe Notification Allowed
push_notification_prompt_allowed
When a user clicks
Allow
on the
On-site Notification prompt
requesting them to display the
native browser Web Push opt-in prompt.
WhatsApp Sent
whatsapp_sent
When the message is sent by WebEngage to your WSP for delivery to your user.
WhatsApp Accepted
whatsapp_accepted
When the message is accepted by the WSP for delivery to the user.
WhatsApp Rejected
whatsapp_rejected
When the WSP rejects the message. This could happen when the your account has exhausted its message limit and so on.
WhatsApp Failed
whatsapp_failed
When the
WSP reports delivery failure
for a user.
WhatsApp Read
whatsapp_read
When the WSP reports that the message has been 'read' or viewed by your user.
WhatsApp Click
whatsapp_click
When the WSP reports that a user has clicked on a link included in the message.
WhatsApp Queued
whatsapp_queued
When the
WhatsApp message is Queued
by WebEngage for delivery to your WSP.
RCS Sent
rcs_accepted
Event fired when the RCS message has been accepted by the RSP
RCS Rejected
rcs_rejected
Event fired when the RCS message sent from our side as been rejected by the RSP
RCS Delivered
rcs_delivered
Event fired when we get the Delivered event from the RSP
RCS Failed
rcs_failed
Event fired when the RCS message has failed to be delivered by the VSP
Note:
* For failure due to RCS non-compatible device, then explicit error code, error type, reason, should be set
RCS Queued
rcs_queued
Event fired when the RCS messages are queued
RCS Control Attempted
rcs_control_attempted
Event fired when a user has been added to Control Group
RCS Click
rcs_click
Event fired when a user clicks a link or button in the message received by the end user
RCS Read
rcs_read
Event fired when the user opens and views the message. This will be dependent on DLR (webhook)
📘
Note
In user profile this event
Push (Web) Registered
is shown as
Web Push Subscribe Process - Device Registered
or
User Login
🚧
Please Note
The
System Events,
User Login
and
User Logout
are not automatically tracked for your users. You will need to call the respective SDK functions whenever these actions occur on your platforms. These actions are also ideal moments to identify your users. Here's how you can go about it:
Website
Android
iOS
React Native
Cordova/ Phone Gap/ Ionic
Xamarin.Android
Xamarin.iOS
Unity.Android
Unity.iOS
How Does WebEngage Define Session?
For Websites:
Session timeout duration = 30 minutes
Sessions time
is the amount of time for which users are 'active' on your website. Here, 'activity' could mean any of the following:
Performing Events like search, browse, viewing products, categories and so on.
Refreshing or reloading the same webpage.
Opening a new webpage.
If a user is detected to be 'inactive' for 30 minutes, then their on-going session is ended. Here's 'inactivity' could mean any of the following:
The user is on your site but has not performed any of the actions mentioned above.
The user has navigated to another tab.
The user is switching between your website and another tab but has not performed any of aforementioned actions.
For Mobile Apps (iOS & Android):
Session timeout duration = 15 seconds
Session time
is the amount of time for which the app is open in the device's foreground. If the user pushes your app to the background and doesn't bring it back to the foreground within 15 seconds, then their on-going session will end. If they bring it to the foreground after 15 seconds, then we'll record it as a new session.
Custom Events
Custom Events
are behavioral data points that you can custom define and track for your users across your apps and website. These enable you to understand your users better and deliver contextually personalized experiences in real-time.
Depending on your business, these events could be anything like:
Product Page Viewed
Course Details Viewed
Susbcription Purchased
Video Played
|
Video Paused
|
Video Ended
Game Started
|
Game Ended
Checkout Started
|
Checkout Completed
Review Submitted
and so on.
🚧
Sample Custom Event Templates
We've complied
Custom Event templates for each industry vertical
to help you get started. While the data you track for your users will vary greatly as per your business model, you can use these as a reference point.
Event Attributes
📘
Event Attributes
are details attached to each
Event
that convey the context in which a user performed it.
For example, the attributes of a
Custom Event, Order Confirmed
could be
Order Value, Delivery Date, Number of Items, Primary Product Category, Delivery Address, Order ID, Event Time, Device Type
and so on.
Event Attributes
have been classified into 2 categories in WebEngage:
System Attributes
:
Tracked for all
System Events
and
Custom Events
by default.
Custom Attributes
:
Tracked only for the
Custom Events
to which they're attached.
Let's walk you through this:
System Attributes
These are generic details that have been predefined by us and are automatically tracked for all the
System Events
and your
Custom Events
. These data points cannot be modified by you.
Here's a list of all the_System Attributes_ tracked for your apps and website post integration:
Name on Dashboard
Type
Description
Event Time
DateTime
Time at which the event occurred (in ISO format).
Country
String
Country from where user performed the event.
City
String
City from where user performed the event.
Browser Name
String
Name of the browser on which user performed the event.
OS Name
String
Operating System of the device through which user performed the event.
Device Manufacturer
String
Name of the device manufacturer through which user performed the event.
Device Model
String
Model of the device through which user performed the event.
Carrier
String
Name of the cellular network provider of the device through which user performed the event.
App Version
String
Version of your app on which the user performed the event.
App ID
String
ID of your app on which the user performed the event.
Platform
String
The platform on which user performed the event (Android/ iOS, Website).
Page URL
String
The page URL on which user performed the event.
(only for website)
Screen Name
String
The screen name on which user performed the event.
(only for apps)
Channel
String
The channel
(Direct, Organic Search, Social)
that resulted in the occurrence of the event.
Campaign Source
String
UTM source of the marketing campaign that resulted in the occurrence of the event.
Campaign Medium
String
UTM medium of the marketing campaign that resulted in the occurrence of the event.
Campaign Name
String
UTM name of the marketing campaign that resulted in the occurrence of the event
Campaign ID
String
ID of the campaign resulted in the occurrence of the event.
Variation ID
String
ID of the
message variation
of a campaign that resulted in the occurrence of the event.
Journey ID
String
ID of the
journey
through which the campaign was sent, that resulted in the occurrence of the event.
Custom Attributes
Custom Attributes
are details that can be attached to each
Custom Event
defined by you. You can choose to attach a maximum if 25 custom attributes of a single data type to each
Custom Event
to better understand each user's platform interactions and contextually engage them.
For example, if an ed-tech platform tracks course purchases as the _Custom Event, Course-Enrolled_then it's
Custom Event Attributes
would be:
Course Name
Course ID
Course Value
Course Duration
Number of Chapters
Course Category
and so on.
🚧
Sample Custom Event & Attribute Templates
We've complied
Custom Event & Attribute templates for each industry vertical
to help you get started. While the data you track for your users will vary greatly as per your business model, you can use these as a reference point.
Tracking Custom Events & Custom Event Attributes
System Events
and
System Event Attributes
are automatically tracked by WebEngage once you integrate a platform through our SDKs. However, you will need to specifically define and pass each
Custom Event
and their
Custom Attributes
from your various platforms to your WebEngage account.
Here are a few guidelines to help you get started:
Please ensure consistent usage of the names of
Custom Events
and their
Custom Attributes
across all your apps (Android, iOS) and website. Doing so will make it easier for you to segment users, personalize campaigns and configure campaign targeting in your dashboard.
We highly recommend that you create an excel sheet to list down:
The
Custom Events
you want to track.
The corresponding
Custom Attributes
of each
Event.
The
data type
of the values you will be tracking against each
Custom Attribute.
The first datapoint synced to WebEngage defines the data type for that event attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Event Attribute
data will stop flowing to your WebEngage dashboard.
You can create a maximum of 25
Event Attributes
of each data type for a
Custom Event.
(ie. 25 attributes of
Number
data type, 25 attributes of
String
data type and so on).
Custom Event
and
Custom Event Attribute
names are case sensitive must be less than 50 characters long.
String
attribute values must be less than 1000 characters long.
Names must not start with
we_
as the term is reserved exclusively for internal use at WebEngage. Thus, to avoid data contamination for your account, such data will be ignored if used for your
Custom Events.
🚧
Please Refer to the Respective SDK Functions to Track Custom Events & their Attributes
Website
Android
iOS
React Native
Cordova/ Phone Gap/ Ionic
Xamarin.Android
Xamarin.iOS
Unity.Android
Unity.iOS
(You will need to integrate the respective platforms with WebEngage before you start tracking custom events and their attributes.)
Updated
about 1 month ago
Users
Sample Event Templates
Copy Page
