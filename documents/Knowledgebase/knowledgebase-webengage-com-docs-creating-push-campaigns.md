# Creating Push Campaigns

- URL: https://knowledgebase.webengage.com/docs/creating-push-campaigns
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Creating Push Campaigns
Step-by-step guide on how you can create Push Notifications in your dashboard
📘
This guide only covers the creation of One-time, Triggered & Recurring Campaigns
Looking to automate
Transactional Push Notifications?
Let's get you started!
Engaging users with
Push Notifications
is an effective way to convey time-sensitive messages, grab their attention with offers, and drive app engagement. Your dashboard comes with a highly intuitive 6-step campaign creation interface that makes it easy to create and execute highly personalized campaigns in minutes!
🚧
Must Read
At WebEngage, we are obsessed with enabling consumer business, like yours, to create contextual experiences that facilitate retention-led growth. This is why user data
(
User Attributes
)
, behavioral data
(
Events & Event Attributes
)
and
Segments
play an integral role in campaign creation. We recommend that you get yourself acquainted with the respective concepts before proceeding.
Here's a quick summary of the exciting possibilities offered by the campaign creation interface:
Personalize messages
to each user's preferences and behavior, across the various
stages of their lifecycle
(
skip to Step 3: Message
)
Deep link
Push Notification
images
to specific screens in your app
(
skip to Step 3: Message
)
Target multiple apps
with a Push campaign!
(
skip to Step 1: Audience
)
Automate multivariate message testing
for your campaign - we'll automatically identify a winner and send it to the entire audience
(
skip to Step 4: Conversion Tracking & Variation Distribution
)
Leverage ready-to-use templates to
engage users with rich Push Notifications
(
skip to Step 3: Message, Layout
)
Test your campaign with internal team members
before sending it to your users
(
skip to Step 5: Test Campaign
)
Avoid disturbing users during DND hours,
implemented in their timezone
(
skip to Step 2: When DND
)
Schedule campaigns for delayed delivery
to users who are currently unavailable
(
skip to Step 2: When, Queueing
)
🚧
Please Note
Please ensure that you have integrated
FCM (Firebase Cloud Messaging)
and
APNS (Apple Push Notification Services)
with your account before proceeding as these platforms enable campaign delivery to all your
Android
and
iOS
users, respectively.
Here's the integration guide.
Select Campaign Type
As shown below, the campaign creation interface can be accessed by clicking the
Plus icon
placed on the top left of the
central hub of Push
. In doing so, you will be prompted to select the type of campaign you'd like to create:
Click to enlarge
Let's walk you through each campaign type:
One-time
These are stand-alone messages that are sent to your users only once and generally comprise of time-bound offers, festive deals, product updates and so on. Such campaigns end as soon as they're delivered to the target audience.
When:
Launch immediately or Schedule for later
How Often:
Once only
🚧
Skip to Step 2, When:
Campaign Schedule > Setting up One-time Campaign
Triggered
These are ongoing cycles of communication that are sent to only those users of your target audience, who perform a particular
event
on your app/website.
When:
Launch immediately or Schedule for later
How Often:
Whenever the specified
Event
is performed by a user or a few
Minutes/ Hours/ Days
after the event occurs
🚧
Skip to Step 2, When:
Campaign Schedule > Setting up Triggered Campaign
Recurring
These are ongoing cycles of communication that are scheduled to be sent periodically to its target audience. Such campaigns help you automate communication for several recurring events in your user's lifecycle like
subscription renewals, policy renewals, bill payments, recurring investments
and so on.
Or you could leverage these campaigns to
engage all new users who have recently signed up, users who performed a certain action on your app but left without transacting or proceeding to the next stage
and so on.
When:
Launch immediately or Schedule for later
How Often:
Daily, Weekly or Monthly
🚧
Skip to Step 2, When:
Campaign Schedule > Setting up Recurring Campaign
Transactional
These are highly contextual messages that your users expect to receive while interacting with your brand through your app, website or offline. This could be acknowledging user interactions like,
sign up (welcome newsletter), password reset, payment confirmation (invoice), order confirmation or conveying payment reminders, account statements
and so on.
When:
Launch immediately
How Often:
Whenever a specific
Event
occurs in your backend
🚧
Continue here...
Step-by-step Guide to Creating Transactional Push Campaigns
Now, let's walk you through all the steps of campaign creation.
Step 1: Define the Audience
Name your Campaign
The first step is to give your campaign a unique name that helps you identify its purpose.
Click to enlarge
Select Target Devices
As shown above, you can choose to create campaigns exclusively for your
Android
or
iOS
users by specifying a
Target Device.
The following options can be selected here:
Both Android & iOS
Android only
iOS only
Click to enlarge
Select Target Apps
📘
Please Note
This option will show only if you have integrated multiple Android/ iOS apps while
configuring Push
& target a few of these through the campaign selectively.
3A. Specify Target Android Apps
If you have added multiple app credentials while configuring
Push for Android,
then by default, all the apps will be targeted. You can alter this by removing
Android Package Names
to target specific apps with the message.
Send to all apps send the
Push Notifications
to all the configured apps.
Send to specific apps will send the notification to the particular apps of your choice. You can select which apps the notification will be sent to by clicking on the
Pencil
icon. A new modal will open with the list of apps, letting you choose them by selecting or deselecting them. You can also search the
Package Name
through the search bar. Click
Save
to save the changes as shown below.
Click to enlarge
This field is hidden if you have selected iOS only under
Target Devices
.
📘
Please Note
You can choose up to 100 apps at a time.
3B. Specify Target iOS Apps
If you have added multiple app credentials while configuring
Push for iOS,
then by default all the apps will be selected here as target apps. You can choose to remove the respective
iOS Bundle Identifiers
to target select apps with the message.
Send to all apps send the
Push Notifications
to all the configured apps.
Send to specific apps will send the notification to the particular apps of your choice. You can select which apps the notification will be sent to by clicking on the
Pencil
icon. A new modal will open with the list of apps, letting you choose the apps by selecting or deselecting them. You can also search the
Package Name
through the search bar. Click
Save
to save the changes as shown below.
Click to enlarge
This field is hidden if you have selected
Android only
under
Target Devices
.
📘
Please Note
You can choose up to 100 apps at a time.
Check Enhanced Delivery Options
📘
Please Note
This option will show only if you have configured Mi or Huawei Push messaging services while setting up Push channel integration.
Learn more
.
Based on push channel configurations added (Mi, Huawei or both), corresponding options will be shown and will by default be selected. For e.g. if you have added Mi push services creds, then in Enhanced Delivery Options only Mi push services will be shown.
Select Audience Type
One of the key differentiators of successful campaigns is that they're tailored to the behavior and preferences of a specific group of users. Thus, by selecting an
Audience Type,
you can choose to target a specific segment of users or combine several segments to define your
Push campaign's
audience.
As shown below:
Click to enlarge
Select
Send to users in single segment
to target all users who are included within a particular segment
(
How to set it up
)
Select
Send to users in multiple segments and/or don't send to users in certain segments
to narrow down the audience to a very specific user persona, defined by including and excluding several segments from the target audience
(How to set up the conditions -
Send To
&
Don't Send To
)
Here's how you can set up each
Audience Type
:
Select Target Segment(s)
Here's how you can set up each
Audience Type
:
5A. Select a Segment (Send To)
(If
Send to users in single segment
is selected as
Audience Type
)
As shown below, click the dropdown nested beside
Send To,
to specify the target segment.
Click to enlarge
Let's quickly walk you through
Segment Preview
:
Reachable Users
:
Indicates the number of users, from the selected segment, that can be engaged through
Push
as a channel, at present.
For example, your target segment could include 10,000 users, but only 7,000 of those users could be reachable through
Push
at present. This could happen if:
A user has disabled
Push
on their registered device.
A user has uninstalled your app.
A user is not reachable on the
Android/iOS devices
selected under
Target Device
.
A user is not reachable on the
Android/iOS apps
selected by you under
Target Android Apps
and
Target iOS Apps
,
respectively.
Rules of Segmentation
:
You can choose to segment your entire user base by 3 broad parameters -
User (attributes), Behavior and Technology.
Thus,
Segment Preview
presents a snapshot of the parameters based on which users have been grouped together.
🚧
Skip To:
How to Edit a Segment
How to Create a New Segment
How to Create a Disposable Segment
Step 2: When
5B. Combine Segments (Send To)
(If
Send to users in multiple segments and/or don't send to users in certain segments
is selected as
Audience Type
)
Using multiple segments to define the target audience is an excellent way to target users that have similar preferences, belong to the same location or have performed certain actions on your app/website - without creating a new segment.
Here's how you can go about it:
Click to enlarge
Step 1: Select a Condition
Select
Users in ANY of these segments
to send the campaign to all the users included within each segment.
*Select
Users in ALL of these segments
to send the campaign only those users who are shared by all the segments.
Step 2: Select a Segment
Step 3: Click Add Segment
to select another one
For example, in the visual above, we have selected the condition,
Users in ALL of these segments
to combine 2 segments -
Inactive Users
and
Cart Abandon(ers).
On selecting the second segment, the
Reachable Users
decrease to 604 from 3,456.
This indicates that the campaign will be sent to only 604 users who are common amongst both the selected segments.
🚧
Skip to:
How to Edit a Segment
How to Create a New Segment
How to Create a Disposable Segment
Step 2: When
5C. Exclude User Frome These Segments (Don't Send To)
(If
Send to users in multiple segments and/or don't send to users in certain segments
is selected as
Audience Type
)
You can choose to exclude a segment or multiple segments from the target audience by configuring the field,
Exclude User Frome These Segments.
This is a great way to selectively engage users that match a specific persona. Here's how you can add the exclusion criteria:
Click to enlarge
Step 1: Select a Condition
Select
Users in ANY of these segments
to prevent users in each segment from receiving the campaign.
Select
Users in ALL of these segments
to prevent only those users from receiving the campaign that are common between all the segments.
Step 2: Select a Segment
Step 3: Click Add Segment
to select another one.
🚧
When Segment Isn't Specified Under the field, 'Send To'
By default, a campaign is set to be delivered to
All Users.
Thus, if no segment is selected under
Send To
AND segments are specified under
Don't Send To,
then
the campaign will be send to all the users who are
reachable on Push
AND are not included within the specified segments.
Edit Segment
Click on the
Edit icon,
placed next to the dropdown,
Send To,
to edit the selected
Segment.
In doing so, you will be prompted by a pre-populated pop-up with the existing segmentation rules.
Click to enlarge
Make your edits and click
Save
to proceed. In doing so, you will preview the number of reachable users as per your edits.
Create a New Segment
You can choose to create a new
Segment_of users from the campaign creation interface by clicking on the _Create Segment button.
In doing so, you will be prompted by a pop-up, allowing you to build a new segment.
Click to enlarge
Once created, you will be able to access the
Segment
through the
List of Segments
in your dashboard.
Creating a New, Single-use Segment
You can also choose to create disposable segments or segment users specifically for the campaign and avoid adding it to the
List of Segments
in your dashboard.
Click to enlarge
As shown above, this can be achieved by leaving the field
Name Your Segment
blank while creating the segment. In doing so, it will become an
Ad hoc segment
in your dashboard, which will be available only for sending the campaign you're currently creating.
🚧
Related Read: Rules of Segmentation
Please refer to
Creating Segments
for step-by-step guidance on how you can segment your users by their
attributes
, behavior (
events
), and technological preferences.
Apply Universal Control Group
📘
Conditional Option
This is a conditional option which will be shown only if the you have created Universal control group in your account.
Click here
to know how to create Universal control group.
Click to enlarge
When the box is checked
, the campaign will not be sent to users who are part of the Universal Control Group in the segment that is selected.
When the box is unchecked
, the campaign will be sent to all users that are part of the segment inclusive of the
Universal Control Group
users.
Step 2: Specify When to Send
As highlighted above, the second step of campaign creation allows you to specify when and how often you'd like the
target audience
to receive the
Push Notification
and manage the role your campaign plays in your overall engagement strategy. Hence,
When
has been divided into two sections:
Campaign Schedule
Frequency Capping & DND
Let's get you acquainted with the workings of each:
Campaign Schedule
Here you can specify
when and how often
the target audience should receive the campaign. This can be determined by configuring the
Campaign Type selected when you initiated creation
. Here's how you can go about it:
🚧
Navigate to:
One-time Campaign
Triggered Campaign
Recurring Campaign
Setting up One-time Campaign
Step 1:
As shown below, select
One-time
as the
Campaign Type
Click to enlarge
Step 2:
Specify the
Delivery Time
As shown above:
Select
Now
to send the campaign immediately
Select
Later
to schedule the campaign:
You can choose from the 2 options i.e.
Send Intelligently
or to send at a specific time.
Send Intelligently
: optimizes campaign send-time for each user, our system intelligently decides the best time to send a campaign based on your user’s interactions with past campaigns of each channel. Click
here
to know more.
Send at Specific Time
: You can specify the time at which you would like to send your campaign to your users, either from the
users time zone
or the campaign's
project time zone
.
You can choose to schedule a
one-time Push campaign
for delivery in your user's timezone!
(
How it works
)
🚧
Skip to
the second section,
Frequency Capping & DND
to complete
Step 2: When
, of the campaign creation process.
Setting up Triggered Campaign
Click to enalrge
Step 1:
Select
Triggered
as the
Campaign Type
Step 2:
Select
the
Event upon the occurrence of which
the campaign will be triggered or sent to the user
📘
The following options can be selected here:
Custom
(all the
custom events
being tracked for your account)
System
(all the
campaign events
pre-defined by us for tracking user-channel interactions like app installed, push delivered, push opened and so on.)
Step 3 (Optional):
Add Attribute Filters to the Event
by clicking on the filter icon
📘
The following options can be selected here:
Custom
(all the
custom attributes
attached to the custom event selected as the trigger event)
Time
(Event Time)
Location
(City, Country)
Technology
(Device Manufacturer, Device Model, Carrier, App Version, App ID, SDK Version)
Engagement
(Campaign ID, Journey ID - can be found under the
campaign's overview
& journey's overview)
These attributes are applicable only to
campaign events
like
Email Rejected, Push, Dismissed
and so on.
Others
(Session Count, Language)
Further, you can choose to club multiple event attributes by the
AND/OR logic
to define the scope of occurrence of the event.
Doing so implies that if users included within the
target segment
don't perform the specified
Event
,
in the context of the added
attribute
filter(s), then they will not receive the campaign.
🚧
How It Works: Clubbing Event Attributes by AND/OR Logic
AND:
Implies that users will have to perform the
Event
in the context of all the
event attributes
to receive the campaign.
(Helps you narrow down the target audiece)
OR:
Implies that users will receive the campaign if they perform the
Event
in the context of any one of the
event attribute
.* (Helps you widen the target audience)
Step 4:
Specify the
Delivery Time
of the triggered campaign
Select
Send as soon as the event occurs
to deliver the campaign immediately
Select
Wait for (duration) and then send
to deliver the campaign after sometime
You can set up a wait time in
Minutes, Hours or Weeks
, after which the campaign will be sent to the respective users
Step 5:
Specify the
Start Date
or the date-time on which the triggered campaign should start getting delivered to the target audience
Select
Now
to send the campaign immediately
Select
Later
to schedule the campaign
Step 6:
Specify the
End Date
or the date-time on which the triggered campaign should cease getting delivered to the target audience
Select
Never
to run the campaign indefinitely
(you can always choose to
Pause
a campaign manually through its
Campaign Overview
)
Select
Later
to stop the campaign at a specific date-time in the near future
🚧
Skip to
the second section,
Frequency Capping & DND
to complete
Step 2: When
, of the campaign creation process.
Setting up Recurring Campaign
Step 1:
As shown below, select
Recurring
as the
Campaign Type
Click to enlarge
Step 2:
Specify the
Start Date
or the date-time on which the recurring campaign should start getting delivered to the target audience.
Select
Now
to send the campaign immediately
Select
Later
to schedule the campaign
Step 3:
Specify the
Delivery Time
or the frequency and date-time of campaign delivery.
The frequency of a recurring campaign can be set as:
Daily,
at a specific
Time
Weekly,
at a specific
Day and Time
Monthly,
on a specific
Day of the Month and Time
View Realised Schedule
shows you the entire schedule for your campaign as set by you.
Step 4:
Specify the
End Date
or the date-time on which the campaign should cease getting delivered to the target audience.
Select
Never
to run the campaign indefinitely
(you can always choose to
Pause
a campaign manually through its
Campaign Overview
)
Select
Later
to stop the campaign at a specific date-time in the near future
Frequency Capping & DND
Click to enlarge
Here you can leverage the features of
Frequency Capping (FC)
,
DND Hours
,
Queueing
and
Throttling
to determine how a user perceives your
Push campaign
in the context of your entire engagement experience.
Context:
Campaigns don't exist in isolation. Most marketing campaigns are designed for a specific audience, motivating them to perform a particular action. And more often than not, users receive multiple campaigns through various channels, nudging them towards a similar goal.
Thus, these features allow you to manage the frequency and timing of campaign delivery for each user.
Let's get you acquainted with the workings of each:
Frequency Capping (FC)
Using
Frequency Capping
(FC),
you can control the number of campaigns a user receives within a
Day, Week, Month
and maintain a consistent gap between consecutive messages (sent through multiple channels or the same channel).
Click to enlarge
As highlighted above:
Select
Follow...
to send the campaign as per your account's frequency capping and
time gap
settings
This means that if the upper limit on the number of messages a user can receive within a day, week, or month is exhausted, then this campaign will get queued for delayed delivery
(
detailed read on how this works
)
Select
Ignore...
to ensure campaign delivery even if the frequency cap for the day/week/month has been met for a user (
impact of disabling FC for a campaign
)
Set Frequency Capping Limits
If you have not set up
Frequency Capping
yet, you can configure it by clicking the
Configurations > Frequency Capping.
Once set, you will be able to send all your campaigns with FC enabled, including the existing one.
(
How to configure FC & Time Gap
)
📘
Please Note
After setting
Frequency Capping
while creating the campaign, kindly refresh the campaign creation tab to enable FC.
DND
Using your account's
DND Settings
, you can prevent users from receiving campaigns during specific periods such as when they may be asleep so on. The best part -
DND hours
are determined individually for each user. This means that
the duration specified by you will be applied to all your users only in the context of their time zone!
Click to enlarge
As highlighted above:
Select
Follow...
to ensure that users aren't disturbed by the Push Notifications at the hours specified by you (as per their timezone)
Select
Ignore...
to ensure campaign delivery even if _DND hours
are applicable to a few users (
Disabling DND for a campaign
)_
Set DND Hours
If you haven't set up
DND Hours
yet, then you can choose to configure it by clicking the
Configuration > DND
in a new tab. Once set, you will be able to send all your campaigns with
DND hours
enabled, including the existing one.
(
How to configure DND Hours
)
📘
Please Note
Kindly refresh the campaign creation tab to enable after setting
DND
while creating the campaign.
Queueing
If you choose to send a campaign with
FC
or
DND
enabled, then
Queueing
is automatically enabled. It's a feature that allows delayed delivery of the message to a user, in cases where immediate delivery is not possible due to your
FC
or
DND settings.
Click to enlarge
As highlighted above:
Select
Queue message for up to...
, to enable the feature and specify a custom queueing duration for the campaign in Minutes, Hours or Days
.
Doing so will ensure that we hold on to the campaign for the specified duration and send it only when a combination of your
FC
and
DND settings
allow us to.
(
How delivery time is determined for queued messages
)
Impact on campaign delivery to Android app users:
if
FCM
is unable to deliver the campaign immediately to a user due to a technical error or if they’re out of network coverage area, then their systems too will continue to attempt message delivery until the specified queueing duration or
time_to_live
(
detailed read on TTL in FCM
)
Select
Do not Queue messages...
to drop the message if we're unable to deliver it to a user due to FC/DND settings (
Disabling Queueing for a campaign
)
Impact on campaign delivery to Android app users:
If a campaign is sent with
Queueing disabled,
and
FCM
is unable to deliver the message to a user, then the message will be dropped immediately
(
detailed read
)
Throttling
Click to enlarge
As highlighted above:
Select
Do not throttle campaign...
to send all messages instantly to the entire target audience.
Select
Throttle campaigns as per channel throttling limits
to control the number of messages delivered per minute.
Select
Throttle campaigns at...
to specify a custom message throttling duration for this campaign.
Please note, this limit cannot be higher than the channel-level throttling limit specified under
Settings > Throttling
.
Step 3: Create the Message
Click to enlarge
As highlighted above, the message creation interface comes loaded with intuitive features like
Variations
,
Layouts
,
Deep linking
,
Message Preview
,
and advanced settings like
Key-Value Pairs
- enabling you to create high impact
Push Notifications
in minutes.
Let's get you acquainted with each feature:
Select a Layout
You can choose from the following ready-to-use templates to create a
Variation
.
Click to enlarge
You can select a background color of your choice for the
Push Notification
.
Let's quickly walk you through each:
Text:
A text-only template, allows you to send quick updates and offers, personalized to each user's preferences and behavioral history.
(Creating dynamic text notifications)
Personalising Text Push Notifications
Banner:
A single-fold media template that allows you to create visually personalized notifications.
(
Creating personalized Banner Notification
)
Personalising Banner Push Notifications
Carousel:
A multi-fold rich media template that enables you to fight Push Blindness and create highly engaging app experiences.
(
Creating personalized Carousel Notification with contextual deep links
)
Personalising Carousel Push Notifications
Ratings:
A clean, UX friendly template that allows you to collect product and service feedback with great ease.
(
Creating a dynamically personalized Rating Notifications
)
Personalising Rating Push Notifications
Timer Layout:
Timer push notification allows you add a countdown timer to a push notification, creating a sense of urgency in your users and driving them to perform the desired action.
🚧
Please Note
This layout is currently access controlled. To enable it, kindly reach out to your CSM or write to us at
[email protected]
Timer layout is supported only for Android devices from SDK v4.7.0 onwards. So this layout will only be visible if in the Audience Tab, the 'Target device' selected is either 'Android' or ‘Both Android and iOS’, whereas if 'iOS only’ is selected, then the ‘timer’ layout will not be shown.
Timer layout will only be visible if in the Audience Tab, the target device selected is Android or ‘Both Android and iOS’, whereas if 'iOS only’ is selected, then the ‘timer’ layout will not be shown.
Basic (Add text)
Click to enlarge
You can easily create dynamically personalized content using the
Personalization icon
nested in the
Title,
and
Message
fields. Select a value from a list of all the
Custom User attributes
and
Custom Events
being tracked for your app and place them appropriately within the text. We'll add the exact value tracked for each user, helping you deliver one-on-one messages at scale.
Configure Banner Layout
🚧
Related Read
Text and Image guidelines for creating Banner Notifications
The
Image section
, enables you to personalize the
Banner
image to each user's preferences/behavior.
Click to enlarge
As shown above, a generic banner image can be added in two ways:
1. Insert Image Link:
The image must be hosted on a publicly accessible domain to ensure that it renders for all users receiving the message.
2. Upload Image:
Click the
Upload
button placed next to the field, image and select a file from your desktop. In doing so, the image will get hosted on WebEngage's domain:
https://afiles.webengage.com
.
You can always click the
Reset
button to link/upload a new image.
🚧
Personalizing Banner Image to Each User's Interests
You can easily
personalize images to the preferences & behavioral history
of your app users in any of the following ways:
Method 1:
Pass
image_url
as a
custom event attribute
, attached to a
custom event
gleaned for your app
(
Step-by-step guide on how to execute this
)
Method 2:
Build the image URL by specifying a parent link and adding a custom event attribute/
custom user attribute
as the path. Then manually add the image format like,
.png, .jpeg, .jpg, .gif,
at the end of the link structure
(
Step-by-step guide on how to execute this
)
Configure Overlay Layout
Create push notifications with the full Image with Text Overlay. In this layout the background image covers the entire space available for the push notification. While, the text can also be added which will appear on top of the image.
🚧
Note
This feature requires access permission. To enable it, please contact your Customer Success Manager (CSM) or email us at:
[email protected]
Step 1: Select an Image
As shown above, an overlay image can be added in two ways:
Insert Image Link
: The image must be hosted on a publicly accessible domain to ensure that it renders for all users receiving the message.
Upload Image
: Click the Upload button placed next to the field, image and select a file from your desktop. In doing so, the image will get hosted on WebEngage's domain:
https://afiles.webengage.com.
You can always click the Reset button to link/upload a new image.
Recommended image size: Dimensions to be 262:184px; in JPG, JPEG, PNG, Gif formats only and less than 1 MB in size.
Step 2: Collapsed Image (Android)
This is how your notification will look in the collapsed state, this capability is only available for Android, whereas iOS doesn’t let us do that. There are 2 options that are available here with the capability to customize the collapsed state of a push notification.
Default App Icon
: This option is selected by default, meaning there won’t be a background image in the collapsed state of your notification and a large app icon will be displayed on the right side of the notification.
Custom Image
: On choosing this option, you now have the choice of uploading another image for the collapsed state of your notification or copy the same image as you uploaded in the image field above by checking on the ‘Copy image as above’ box.
Step 3: Collapsed Image Width
You can also select the width of the background image in the collapsed state between the 2 choices: Full and Half.
Full
: This image takes up the whole width of the collapsed state of your notification.
Half
: The image would be placed on the right half of the notification area, whereas for RTL languages this would be mirrored and the image would be placed on the left half of the notification area.
Step 4: Text and Action
Set up the title, description and on-click action that you would like to compliment with the image.
📘
Use Case: Full Image with No Text
When focusing exclusively on your Android audience only, the main 'Text and Action' section would be optional, enabling you to send a full image with no text overlay, which is used for image prominence. However, if you opt for 'Both Android and iOS’, and ‘iOS only’ this section is mandatory.
Text and Action (Lower Android SDK Versions)
Overlay push notifications are currently supported only on the
latest Android Core SDK v4.8.0, iOS Core SDK v6.6.1 and Extension SDK v1.1.1 and above
. Therefore for all other lower versions of Android devices that don’t support this feature, we offer an option to add alternate text, i.e. lower SDK users will receive a text layout push notification with the title and description you provide in this section.
Below each subsection, i.e. title and description, there are checkboxes labeled ‘Copy Title and above’ and ‘Copy Description as above’ respectively, this enables you to copy the content from the previous ‘Text and Action’ section.
🚧
Keep In Mind
In case your customers are on a lower version for Android SDK, then the notification sent is a ‘Text’ Layout i.e. Title and Description provided in ‘Text and Action (Lower Android SDK Versions)’ section. Whereas, for customers on lower iOS SDK versions the notification is sent in the ‘Text’ layout, i.e. Title and Description provided in ‘Text and Action’.
Step 5: Advanced Options (Android)
By sliding this section on, you can add a few more advanced features to the notification of your users. Here are some of the advanced features you can add.
Message Summary
: Add a short summary of the message you are sending.
Sticky Push
: By checking this box, you have enabled the option to add buttons to your notification, your users will not be able to swipe and dismiss the notification. They will have to take action to dismiss the notification. Checking this option automatically enables the Buttons switch as well.
Buttons
: You can add upto 3 buttons, which will be displayed at the bottom of the notification.
Advanced Option (iOS)
By enabling this option you will be introduced to similar options as the advanced options in android, but instead of a ‘Message Summary’ you have ‘Subtitle’, and ‘Buttons'.
Subtitle
: as the name suggests, this allows you to add a subtitle to your push notification.
Buttons
: By toggling this option on, you can choose from different variations of buttons. Click
here
to know more.
Configure Carousel Layout
🚧
Text and Image guidelines for creating Carousle Push Notifications
The
Carousel
Images
section, enables you to:
Personalize the images to each user or add a generic image
to the carousel
Personalize the on-click action deep links to each user for all the mage
to a screen in your app
Here's how you can go about it:
Step 1: Select the Carousel Layout
Click to enlarge
As shown above, you can choose between a
Landscape
or
Portrait
style template for your notification, depending on the dimensions of the images being used.
Click the
Add Image button
to add a maximum of 5 images to the carousel.
Click the
Reset
button to start from scratch anytime you like!
Step 2: Auto-Scroll (Optional)
If you like the images within the carousel to scroll automatically, then select this option. You will need to specify the the time after which each image should scroll.
Note:
Once a user manually scrolls the image, the auto-scrolling will stop.
Step 3: Add Carousel Images
Click to enlarge
As shown above, a generic carousel image can be added in any of the following ways:
1. Insert Image Link:
The image must be hosted on a crawlable/publicly accessible domain to ensure that it renders for all users receiving the message.
2. Upload Image:
Click the
Upload
button placed next to the field, image and select a file from your desktop. In doing so, the image will get hosted on WebEngage's domain:
https://afiles.webengage.com
.
You can always click the
Reset
button to link/upload a new image.
Note: Gif are not supported in Carousel, due to auto scroll and multiple GIFs it may surpass limit of the Bitmap, Size of the notification will increase drastically
🚧
Personalizing Carousel Images to Each User's Interests
You can easily
personalize images to the preferences and behavioral history
of your app users in any of the following ways:
Method 1:
Pass
image_url
as a
custom event attribute
, attached to a
custom event
gleaned for your app
(
Step-by-step guide on how to execute this
)
Method 2:
Build the image URL by specifying a parent link and adding a
custom event attribute/
custom user attribute
as the path parameter. Then manually add the image format like,
.png, .jpeg, .jpg,
at the end of the link structure
(
Step-by-step guide on how to execute this
)
Step 3: Add Label (CTA)
(Mandatory)
Label
refers to the text added below the image and doubles up as a
Call-to-Action (CTA)
for each fold of the
Carousel.
Step 4: Insert Deep Link (On-click Action)
You can choose to deep-link each image to a specific screen in your
Android
and
iOS app,
or direct users to a web page by specifying an
On-click Action,
as shown below.
Further, you will notice that the deep links specified for the
Android app
are in a different format compared to the links specified for the
iOS app.
This is because we have created a unique
URI
for each collection in our
Android app
while we are leveraging
Universal Links
for the iOS app (the same link is also used for our website).
🚧
Personalizing On-click Action to a User's Preferences of Behavioral History
You can easily
personalize the
On-click Action
of each image to your users based on the
Custom User Attributes
and
Custom Events
gleaned for them. This can be achieved in any of the following ways:
Method 1:
Pass
screen_url
as a
custom event attribute
, attached to a
custom event
gleaned for your app
(
Step-by-step guide on how to execute this
)
Method 2:
Build the deep link by specifying a parent link and adding a
custom event attribute/
custom user attribute
as the path parameter
(
Step-by-step guide on how to execute this
)
Method 3:
Build
Key-Value pairs
into your app's code that facilitates deep link personalization and help you customize screen content.
(
Step-by-step guide on how to execute this
)
This is an optional field and you can choose to skip it if:
You are adding a common URL/ deep link for all the carousel images under
Advanced Options (Android)
or
Advanced Options (iOS)
.
You are using
Key-Value pairs
to link the entire
Push Notification
to an app screen or web page.
👍
Fact Check
The image
Label
and
On-click Action link
must be in sync to deliver a cohesive experience!
Configure Timer Layout
Step 1: Select a Template
We offer three distinct options for the timer template:
Countdown:
A simple countdown timer will be shown on the right side of your push notification.
Countdown with Progress bar:
A progress bar indicating how much time is remaining to start or end a campaign, along with the countdown timer will be present in your notification.
Big Countdown:
As the name suggests, the notification will have bigger countdown, thus giving more focus to the countdown.
Step 2: Set Timer
After selecting the template, you need to set the timer value. This can be done in 2 ways:
By Duration:
This option allows you to set the duration for how long you would like the timer to run for
(once the user receives the notification)
.
For example, if you’ve set the timer value (duration) for 4 hours and 30 mins, all your customers will receive a timer notification of the same duration, irrespective of the actual time of them receiving the notification. So, if one of your customers receives this notification at 11 am while the other receives at 4 pm (due to the unavailability of a cellular network) , the countdown for both of them will begin from 4 hours and 30 mins.
By End Time:
This timer automatically counts the difference between the current time of the user versus the time at which you’ve set the timer value irrespective of time. Here the value is taken in Date and Time and it needs to set as per when you would like to end the campaign. Note must be taken that you can only set the timer value 2 days from the time you have scheduled the campaign on the ‘When’ page.
Example: Suppose you have an upcoming sale on 7th December and you want to notify all your users about it on 6th December. You then set the date value as 7th December and timer value as 00:00 and launch the campaign on 6th December 6 pm. If two customers are receiving the notification and one receives it right away at 6pm, and the other receives the notification at 11 pm, then first customer will receive the notification with a countdown value starting from approximately 6 hours, whereas the second customer will receive with countdown value starting from approximately 1 hours. Therefore by using this option, the time duration will vary according to when the customer receives the notification, and is based on the difference in time from receiving the notification and the end time set for the countdown.
Timer Color and Progress Bar color
You can also choose the color of your timer and progress bar (for template with progress bar), by checking the box.
Step 3: Text and Action (for Android)
Set up the title, description and on-click action that you would like to compliment with the timer.
Step 4: Text & Action (iOS and lower Android SDK versions)
Since timer push notifications are currently
only available for Android devices, with apps using after WebEngage SDK version 4.7.0
, therefore for all other lower versions and iOS devices that don’t support this feature, we offer an option to add alternate text. These devices will receive the notification without the text set here and without the countdown.
Step 5: Add an Image (optional)
You can slide to switch on this option which then enables you to either add a link to the image or upload an image from your device that will be shown along with your notification to the users.
Note:
GIF is not supported on
Timer layout is re-rendered every second
Configure Ratings Layout
🚧
Image and text guidelines for Rating Notifications
Click to enlarge
The
Rating
section lets you configure the background image and message for your Rating style Push Notification. Here's how you can go about it:
Step 1: Add Title & Description
As shown below, you can create a dynamic
Title
and
Description
for the
Push Notification
by adding relevant
User Attributes
and
Custom Events
to the message through the
Personalization icon
nested under each field.
For example, you can personalize the
Rating template
to the user's first name and the last product purchased by them by adding the following tokens as placeholders in our message:
{{user['system']['first_name']}}
- For adding the user's first name
{{event['custom']['Order Placed']['custom']['Products']}}
- For adding the name of the product purchased by the user
Thus, whenever the
Push Notification
is sent, we will populate the tokens with the corresponding values gleaned for the respective users, helping you communicate one-on-one at scale.
Step 2: Customize Text & Background Color
You can easily add your brand colors to the palette and customize the look and feel of the
Push Notification
as per your needs. However, if you are
adding a background image
, then it will override the background color settings.
Step 3: Add Background Image
You can add a generic background image can be added in any of the following ways:
1. Insert Image Link:
The image must be hosted on a crawlable/publicly accessible domain to ensure that it renders for all users receiving the message.
2. Upload Image:
Click the
Upload
button next to the field image and select a file from your desktop. In doing so, the image will get hosted on WebEngage's domain:
https://afiles.webengage.com
.
You can always click the
Reset
button to link/upload a new image.
🚧
Personalizing Background Image to Each User
You can easily
personalize the background image to the preferences & behavioral history
of your app users in any of the following ways:
Method 1:
Pass
image_url
as a
custom event attribute
, attached to a
custom event
gleaned for your app
(
Step-by-step guide on how to execute this
)
Method 2:
Build the image URL by specifying a parent link and adding a
custom event attribute/
custom user attribute
as the path parameter. Then manually add the image format like,
.png, .jpeg, .jpg, .gif,
at the end of the link structure
(
Step-by-step guide on how to execute this
)
Text & Action
Add the
Title
and
Description
for the *Push Notification. You can customize the notification with the rich text editor support which will allow you to style (bold, italics, etc.) the text and apply font colors.
Adding
On-click Action
Link
In addition to the
On-click Action
specified for the
Carousel images
,
you can specify a global
On-click Action
for all your
Android
users, as shown in the visual above. This link will be applied to those areas of the
Push Notification
that are currently unlinked, as highlighted below.
Click to enlarge
This is a great way to nudge users to perform the desired action, no matter how they choose to interact with the
Push Notification.
🚧
Personalizing On-Click Action & Button Links
You can easily
personalize the
On-click Action
and
Button link
to your users based on the
Custom User Attributes
and
Custom Events
gleaned for them.
This can be achieved in any of the following ways:
Method 1:
Pass
screen_url
as a
custom event attribute
, attached to a
custom event
gleaned for your app
(
Step-by-step guide on how to execute this
)
Method 2:
Build the deep link by specifying a parent link and adding a
custom event attribute/
custom user attribute
as the path parameter
(
Step-by-step guide on how to execute this
)
Advanced Options (Android)
Using the options nested under this field, you can customize the experience for your
Android
users by linking the entire
Push Notification
to a particular app screen and adding
CTAs/Buttons
to it, as shown below. Simply click the
Toggle button
to enable
Advanced Options
and get started!
This field
gets hidden if you have specified
iOS only
as the
Target Device at Step 1: Audience
.
Now, let's walk you through its features:
Message Summary
This field will allow you to add content besides the App name for Android
Push Notification
.
Sticky Push
Android allows you to set a
Push Notification
as sticky i.e. the user will not be able to swipe and dismiss the push notification and will have to take an action (click the action text) for the notification to be dismissed. It is necessary to add at least
one action button
in sticky push notifications.
Sticky Push Notifications
are supported in
Text and Banner layouts
Large Icon
Large icon option allows you customize the icon shown on the right of the notification. By default, if no image is added then the app icon is shown here. This option is supported for Text, Banner, Carousel and Rating layouts.
Auto-Dismiss Notification
By enabling this option, the notification will be automatically dismissed after the time set. This option is available for all layouts except Timer.
Adding Action Buttons
Available only for
Banner
and
Text
layouts
, as shown in the image, click the toggle button to enable and add up to 3 buttons to your
Push Notification
for
Android
users.
Following are different action button types supported from SDK v4.9.0 onwards:
Sr. No
Action button type
Description
1.
URL/Deeplinks
(Selected by default) Redirects users to a particular screen or page within or outside you app.
2.
Copy
Allows users to copy the intended text (E.g OTPs, promo codes, etc.).
3.
Share
Capability to Share a specific text, link, etc. like inviting friends to join your app to avail themselves of additional offers.
4.
Call
Allows users to copy the phone number you’re providing to their native phone dial.
5.
Snooze
Clicking on this button type temporarily hides notifications by clicking the "Snooze" button. Once clicked, the notification will disappear from view and reappear after a time interval specified by you, allowing the customers to manage their notification interruptions more effectively.
6.
Track Events
Gives the capability to collect responses and track events through notification clicks and update their value (without opening the app).
7.
Set User Attribute
Gives the capability to track or update user attributes (without opening the app).
8.
Dynamic/Custom Action
Apart from the above mentioned action types, if there are any other actions that you intent to run then this option can be used. It allows you to create custom actions that allow specific to your app/ use case. This would involve assistance from your tech team.
You can
personalize the button link
to each user's behavioral history, preferences or details.
Dismiss Button
The dismiss button is supported from Android SDK versions 4.7.0 and higher. Unlike other CTA buttons, Adding Dismiss button to a push notification allows the user to dismiss the push without being redirected to the app. If a user clicks on this button, then the 'Dismiss' event will be tracked rather than the 'Click'.
📘
Note
For each campaign variation, only one Dismiss button can be added.
Why can't buttons be added to a
Carousel
or
Rating
template?
Given the highly interacted nature of these types of
Push Notifications,
we have made it possible for you to customize the buttons, images, and links individually for each layout. Hence, adding buttons separately for Android users will defeat the purpose of customization made while
Configuring the Carousel Layout
or the
Rating Layout
.
Advanced Options (iOS)
Using the options nested under this field, you can customize the experience for your
iOS
users by linking the entire
Push Notification
to a particular app screen and adding
CTAs/Buttons
to it, as shown below. Simply click the
Toggle button
to enable
Advanced Options
and get started!
Click to enlarge
This field gets hidden if you have select
Android only
as the
Target Device at Step 1: Audience
.
Now, let's walk you through its features:
Subtitle
This field will allow you to add more content below the title field for
Push Notification
. This feature is supported for
Text, Banner, and Carousel
layout.
Sound
By default, all push have the same notification sound as per the phone settings. This option allows you set a custom sound for a particular notification. You need to mention the sound file in .aiff, .wav, or .caf format.
Note:
The mentioned sound file needs to be present in app files. If not present then the default notification sound will be played. Please contact your tech team for further assistance.
Adding Buttons
As you must be aware, iOS allows you to add certain predefined CTAs or buttons towards the bottom of each
Push Notification
to facilitate seamless engagement. As shown below, you can leverage this functionality in 3 easy steps:
Step 1:
Click the toggle switch to enable
Buttons
Step 2:
Select a relevant
Button Type
for your campaign
Step 3:
Deep-link it to a relevant app screen (you can also personalize the deep links to each user's preferences or behavioral history by following
these steps
)
You can add either of the following (predefined)
Button pairs
to a
Text
or
Banner
style
Push Notification
for all iOS users:
Button Types
How It Works
Yes
or
No
Open the app or dismiss the notification - these actions are tracked as the
campaign events
,
App Opened
and
Push Dismissed,
respectively, in your dashboard for all
Push Campaigns.
Yes
or
No
Both options dismiss the notification and are tracked as the
campaign event
,
Push Dismissed
in your dashboard.
Accept
or
Decline
Open the app or dismiss the notification - these actions are tracked as the
campaign events
,
App Opened
and
Push Dismissed,
respectively, in your dashboard for all
Push Campaigns.
Accept
or
Decline
Both options dismiss the notification and are tracked as the
campaign event
,
Push Dismissed,
in your dashboard.
Shop Now
Opens the app and takes the users to the defined deep link, recorded as the
campaign event
,
Push Clicked
in your dashboard.
Buy Now
Opens the app and takes the users to the defined deep link, recorded as the
campaign event
,
Push Clicked
in your dashboard.
Download
Takes the user to the deep link specified under
On-click-Action,
and is tracked as the
campaign event
,
Push Clicked
in your dashboard.
Why can't custom buttons be added to a
Carousel
or
Rating
template?
Given the highly interacted nature of these type of
Push Notifications,
we have made it possible for you to customize the buttons, images, and links individually for each layout. Hence, adding buttons separately for iOS users will defeat the purpose of customization made while
Configuring the Carousel Layout
or the
Rating Layout
.
Key-Value Pairs
(Deep Linking, Personalization)
With
Key-Value pairs
, you can easily customize the contents of an app screen, personalize your
Push Notification
, deep link the notification to a specific app screen, web page and much more!
You can think of
Key-Value pairs
as a set of linked data points in which the
Key
acts as a unique identifier and the
Value
either represents the data or points to the location of the data that is identified by the
Key.
The best part - these are not visible to your users. All this data is sent as an
extra payload
to your app, causing its code to perform the specified action and render the
Push Notification
accordingly.
Here's how you can go about it:
Click to enlarge
Step 1:
Enable
Key-Value pairs
by clicking the
toggle button,
as shown above.
Step 2:
Add a
Key
and its corresponding
Value,
as understood by your app.
Step 3:
Click the
Add Pair button
to specify additional pairs.
For example, in the above visual, we have used the
Key, appurl
to deep link the
Push Notification
to a specific app screen, defined as the
Value.
🚧
Must Read
How
Key-Value pairs
work & how you can leverage this feature
to deliver contextually personalized app experiences (with use-cases)
Preview Notification
Click to enlarge
As shown above, the left half of the campaign creation interface provides a real-time preview of the
Push Notification
being created by you. At any given point, you can toggle between a
Raw Preview
and
User Preview
to gauge the notification's appearance for both
iOS
and
Android
users
(as per the target device selected at
Step 1: Audience
).
Raw Preview
As the name suggests, it renders the
Push Notification
with the raw message and attributes, as added by you to the
Title & Message
.
Click to enlarge
User Preview
Allows you to view the
Notification
for an actual user from your account by populating it with data from their user profile, as per the elements of personalization added to
Title & Message
.
Click to enlarge
For example, in the visual above, we have visualized the
Push Notification's
message for the
User ID, eyang_2699.
Here's how you can go about it:
Step 1:
Select
User Preview
from the dropdown placed on the top left
In doing so, you will be prompted by a pop-up allowing you to search for a user to populate the corresponding attribute and event values.
Step 2:
Enter the
User ID,
preferably of a power user included within the target audience
Access
List of Users
of the campaign's target Segment (as specified at
Step 1: Audience
)
to identify an ideal user.
Step 3:
Click the
Search and Populate
button
In doing so, you will be shown a summary of the values against the respective attributes and events included in the message. This is a good way to ensure that all the values are available for the user; if not then you can enter an alternate
User ID.
Step 4:
Click the
See Preview
button on the pop-up to visualize the notification with real user data
While this is a great way to gauge the overall look and feel of the
Push Notification,
we recommend that you
test the campaign with a test segment
to ensure that it's good to go!
Create Variations
Variations
are just different versions of the campaign's message that facilitate easy multivariate testing and are referred to in the following manner in your dashboard:
Variation A:
The first version of the message.
Variation B:
The second version of the message.
Variation C, D, E:
Subsequent versions of the message created for testing.
Click to enlarge
As shown above, by default the message creation interface consists of a single
Variation A.
You can click on the
Plus icon
to create up to 5 versions of the message.
Select
Create New
to start building the new Variation from scratch
Select
Copy from Variation A
(or any of the previous versions) to make minor edits to the new Variation
Each
Variation
can be created independent of the other, allowing you to test multiple aspects like its layout, body copy, buttons, links and colors to identify a mix that resonates with your entire target audience.
(
How to test message Variations
)
The percentage values indicate the share of users, that will receive a
Variation
and can be customized at
Step 4: Conversion Tracking
.
Test Message
You can easily test the message with an internal segment of users before sending it to your entire user base. As shown below, click the
Test Message
button to
select a Variation
and
Test Segment
. Please refer to this
Step-by-step Guide
to proceed.
Click to enlarge
Step 4: Set up Conversion Tracking & Variation Testing
The fourth step of campaign creation allows you to measure the effectiveness of your campaign in various ways like:
Tracking conversions
for a specific goal
Comparing performance against a
control group
Testing multiple variations
of the message to identify a winning version
Hence, it has been divided into two sections:
Conversion Tracking
and
Variation Distribution.
However, depending on the number of
message
Variations
created by you, the view of
Step 4: Conversion Tracking
will vary:
When only 1 Variation Exists
As shown below, on proceeding to this step from
Step 3: Message
,
you will be welcomed by an interface on which
Conversion Tracking
is disabled.
Click to enlarge
When Multiple Variations Exist
As shown below, on proceeding to this step from
Step 3: Message
,
you will be welcomed by an interface on which:
Conversion Tracking
is disabled
Variation Distribution
meter indicates the share of the audience that will receive each
Variation
Click to enlarge
Now, let's get you acquainted with the workings of
Step 4: Conversion Tracking:
Conversion Tracking
🚧
Must Read
We recommend that you gain a broad understanding of
how
Conversion Tracking
works
in your dashboard before proceeding. Doing so will lay a strong foundation for understanding whether or not you need to enable
Conversion Tracking
for the campaign and its
impact on
Revenue Tracking
.
By default,
Conversion Tracking
is disabled for all
Push campaigns.
As shown below, you can use the toggle switch to enable it.
Step 1: Select a Conversion Event
The term,
Conversion Event
is an alias that helps you identify the event you expect users to perform after receiving the
Push Notification.
Click to enlarge
As shown above, you can choose from a list of all the
Custom Events
being tracked for your account to specify the campaign's conversion goal. For example, we have specified the campaign's conversion goal as the
custom event, Checkout - Completed.
📘
The following options can be selected here:
Custom
(all the custom events being tracked for your account)
System
(Session Started, User Login)
👍
Pro Tip
We recommend that you
map all the
Custom Events
, that record the occurrence of a monetary transaction in your app, as
Revenue Events
in your dashboard. This will help ensure that selecting the respective events as the
Conversion Event
of a campaign helps you
track
Conversions
and
Revenue
for the campaign and its channel
:)
Step 2: Add Attributes to the Conversion Event
Depending on the
end goal of the campaign
, you can choose to narrow down the scope of conversion to a specific action like
Puma Leggings Purchased, Jimmy Choo Pumps Purchased, Episode 3 Streamed, Chapter 7 Started
and so on.
This can be done by adding
attribute filters
to the selected
Conversion Event
.
Here's how you can go about it:
Click to enlarge
Step 1:
As shown above, click on the filter icon placed next to the drop down
In doing so, you will be prompted by a pop-up allowing you to select an attribute and specify its value.
📘
The following options can be selected here:
Custom
(all the
custom attributes
attached to the custom event selected as the conversion event)
Time
(Event Time)
Location
(City, Country)
Step 2:
As shown below, click
Add Filter
to add more attributes to the event
You can club multiple event attributes by the
AND/OR logic
This way only those users who perform the
Conversion Event
in the context of
All/Either
attribute filters will be considered towards the
Conversion
numbers of the campaign
Click to enlarge
🚧
How It Works: Clubbing Event Attributes by AND/OR Logic
AND:
Clubbing multiple event attribute filters by the
AND logic
helps you narrow down the scope of occurrence of the
Conversion Event.
This means that only those users will be counted towards the campaign's
Conversions
who perform the
Conversion Event
in the context of all the
event attributes
.
OR:
Clubbing multiple event attribute filter by the
OR logic
helps you widen the scope of occurrence of the
Conversion Event.
This means that users who perform the
Conversion Event
in the context of any of the specified
event attributes
* will be counted towards the campaign's conversions.
Step 3: Set Conversion Deadline
The
Conversion Deadline
is a duration defined by you that tells us when to stop tracking conversions for a campaign.
This means that once your campaign is delivered, we will track users who perform the
Conversion Event
in the context of its attribute filters (if any), only till the specified
Conversion Deadline.
Click to enlarge
As shown above, by default, a
Conversion Deadline of 7 days
is set for all campaigns. You can choose to specify a custom duration in
Hours or Days,
as per the campaign's end goal.
🚧
Related Read
List of all the
Conversion
metrics and
Performance Indicators
tracked for
Push campaigns
Step 4: Enable Control Group (Optional)
Click to enlarge
A
Control Group
is a small portion of the target audience of a campaign that is randomly selected, representing the behavior and preferences of the entire segment, and does not receive the campaign.
An optional but recommended step, adding a
Control Group
to the target audience allows you to compare the campaign's performance against the organic behavior of
Control Group
users. This makes for the perfect benchmark to assess the true impact of the campaign on influencing user behavior.
📘
Detailed read on
Control Group
.
On checking the Control Group checkbox, you are presented with another choice called 'Target Control Group', that lets you choose between two options.
Set a new control group for this campaign
Custom Control Group
Option 1: Set a new control group for this campaign:
This will be a campaign level control group which means a control group that is created for a specific campaign only. The users in this control group are randomly added from the selected segment in 'Audience' tab. This control group is good if the aim is to measure impact for a specific campaign.
On clicking this option, the Variation Distribution slider is exposed that allows you to select percentage of users to be added in Control Group from target audience.
Option 2: Custom Control Group:
This option is shown when at least one Custom Control Groups is created in your account.
Click here
for detailed read on creating custom control group.
Since this is a pre-created control group, overlapping users within this group and the target segment won't be receiving the campaigns.
Custom control groups are good for analyzing effectiveness of multiple campaigns. For example: Analyzing effectiveness of SMS and Email campaigns during Diwali sale.
Unlike Campaign level control group, the percentage of users to be part of control group cannot be controlled when Custom control group is selected.
🚧
Must Read
Why you should (almost) always use
Control Group
to measure the effectiveness of your campaign and
how it works in your dashboard
###Variation Distribution (Multivariate Testing)
If you have created multiple versions of the
Push Notification
at
Step 3: Message
,
then you can choose to automate the testing process by
enabling
Send Winning Variation Automatically
.
Doing so will allow you to test all the_Variations
(and
Control Group
if enabled) with a smaller test audience and we will automatically send the winning variant to the entire target audience. _(
detailed read
)*
However, you can opt to
test the
Variations
and
Control Group
manually
if you are unable to automate testing due to the small size of the target audience (less than 2,000 users) of a
One-time
or
Recurring campaign.
Or if you are unwilling to test a
Triggered campaign
with a minimum of 500 messages.
Send Winning Variation Automatically
🚧
Must Read
Basics of setting up
Send Winning Variation Automatically
for a campaign
How
Send Winning Variation Automatically
enables intuitive multivariate testing
for your campaign
Depending on the
campaign type selected when you initiated creation
, the steps of configuring automated variation testing vary:
One-time campaign
Triggered campaign
Recurring campaign
Testing a One-time Campaign
Given the short lifespan of
one-time campaigns
, we suggest that you launch the campaign well in advance for testing, and schedule it for delivery at the most viable time slot (as suggested by the
channel's engagement trends
). Doing so will ensure that your users receive the most effective version of your campaign at a time that records the highest engagement rate.
Click to enlarge
Step 1: Specify Size of Test Audience
You can choose to test the
Variations
and
Control Group
(if added) with
5% to 25%
of the campaign's entire target audience. As shown above, we have chosen to treat 15% of all users as the
Test Audience
.
Step 2: Define Time to Test
A custom
test duration
can be specified in
Minutes
or
Hours.
As shown above, we have specified a test duration of
8 Hours.
This means that the impact of all the message
Variations
and organic behavior of the
Control Group
(if added) will be tracked for
8 Hours,
after which we will determine a winner.
Step 3: Select Win Criteria
The
Win Criteria
is a performance indicator that helps us determine a winning
Variation
according to the campaign's end goal. As shown above, it can be defined as
Clicks
or
Conversions
,
as per your needs.
🚧
Quick Read:
How automated variation testing works for one-time campaigns
Testing a Triggered Campaign
Triggered campaigns
are on-going cycles of communication that are sent to users only when they perform a certain action or
Event
. Thus, the most scientific way to test
Variations
of a triggered campaign is by ensuring that a significant number of messages are delivered before we draw a comparison.
Step 1: Specify Size of Test Audience
The
Test Audience
can be defined only in terms of the number of messages delivered. This means that
Variation
testing will continue until the specified number of messages have been successfully delivered.
Click to enlarge
Step 2: Select Win Criteria
The
Win Criteria
is a performance indicator that helps us determine a winning
Variation
according to the campaign's end goal. As shown above, it can be defined as
Clicks
or
Conversions
,
as per your needs.
Once we identify a winning
Variation
, it will be sent as the only campaign to all the subsequent users who perform the
trigger event
.
🚧
Quick Read:
How automated variation testing works for triggered campaigns
Testing a Recurring Campaign
If you choose to create a
Recurring campaign
,
then the entire first run of the campaign will be considered as its
Test Audience
by default.
We will calculate the test results 1 hour before the second run of the campaign to identify a winning variation.
A winning
Variation
will be determined as per the
Win Criteria
and will be sent as the only campaign to all users from the second run. onwards.
Thus, as shown below, just define the
Win Criteria (Clicks or Conversions),
we will take care of the rest!
Click to enlarge
🚧
Quick Read:
How automated variation testing works for recurring campaigns
Manual Distribution
If you are unable to set up
Send Winning Variation Automatically
due to the small size of the target audience (less than 2,000 users) of a
One-time
or
Recurring campaign,
or if you are unwilling to test a
Triggered campaign
with a minimum of 500 messages, then you can choose to test the
Variations
manually.
Click to enlarge
As shown above, all the
Variations
created in
Step 3: Message
are equally divided amongst the entire target audience. Using the slider, you can choose to specify a custom share for each
Variation
and
Control Group,
if enabled.
🚧
Quick Read:
How manual
Variation Distribution
works
Depending on your
Variation testing settings
, the campaign will be tested against the
Control Group
in either of the following ways:
Impact on Variation Slider if Control group is enabled
In case the
Control Groups have been enabled
the Variation Distribution slider behaves differently based on the type of control group selected:
If Campaign level control group is selected:
In this case, the user will have the option of adding the control group by deciding the percentage or size of the control group on variation distribution slider.
If Custom Control Group is selected:
You will not be able to manually select the size of the control group using the variation slider since the Custom Control Group is pre-created and overlapping users in the selected Custom Control Group and target segment, won't be receiving the campaign.
🚧
Keep in mind
In a particular campaign, Custom Control Group and campaign control group cannot be applied together.
Universal control group can be added irrespective of Custom Control Group or Campaign Control Group is selected.
In case multiple control groups are applied within same campaign (E.g: Universal Control Group + Custom Control Group or Universal Control Group + Campaign control): In this case, since the users in both the control group are mutually exclusive, the overall control group size will increase and the target audience size will decrease.
Step 5: Test Your Campaign (Recommended)
Iron out all the creases in your
Push Notification
by testing it with internal team members for maximum impact!
Click to enlarge
While this is an optional step, we recommend that you test all campaigns that contain images, buttons, deep links, and elements of personalization in the message to ensure that everything's in order. This can be easily done by
creating a
Test Segment
and adding all the stakeholders.
However, you can always choose to skip it by clicking the
Skip Test & Proceed
button, as highlighted above. Doing so will take you to the final step of campaign creation -
Step 6: Preview & Launch
.
Now, let's show you how you can test all the message
Variations
:
Step 5.1.: Select a Variation
By default,
Variation A
is selected against the field -
Variation To Test.
However, if you have created
multiple
Variations
, you can test each by sending them consecutively to a
Test Segment.
For example, in the visual above, we have chosen to test
Variation D
of our
Push Notification.
Step 5.2.: Select Test Segment
As shown above, all the test segments created while testing a campaign, for any channel
(Push, SMS, Web Push, Email, WhatsApp),
can be found under the dropdown,
Send Test Message To,
along with details of all its users.
Step 5.3.: Personalize Test Message
Click to enlarge
As highlighted above, you can test personalization in two ways:
Use own data of users included in the test segment
to receive a message personalized to your user profile
Use data of a specific user
to receive the exact message that the selected user would receive
On selecting this option, you will be prompted to search for a user in your database.
We recommend selecting this option if you have personalized the message to a very specific set of custom events or users attributes that are unlikely to be available for an internal team member.
Here's how you can personalize the message to a specific user:
Step 1:
Click on the
Search User button
In doing so, you will be prompted to search your user base.
Step 2:
Add the
User ID,
preferably of a power user included within the target audience
Access
List of Users
of the campaign's target
Segment
(as specified at
Step 1: Audience
)
to identify an ideal user
Click to enlarge
Step 3:
Click the
Search and Populate Values button
In doing so, you will be shown a summary of the values against the respective attributes and events included in the message. This is a good way to ensure that all the values are available for the user. If not, then you can enter an alternate
User ID
to personalize the message.
Next, click the
Save and Return to Test Campaign
button to proceed with the selected user.
Step 4:
Click the
Send Test & Proceed button
to test the campaign.
📘
Please Note
After the
Test Message
has been sent, you will see that it is in
Queue
. After some time you will be able to see the delivery status of the test message as
Delivered or Failed.
The
Delivery details
include
Device details, Browser Name,
and so on.
If the
Test Message
has
Failed
to deliver, then you will be able to see the reason for failure.
Creating Test Segment
Click to enlarge
🚧
Prerequisite for adding internal team members to a test segment
As you are aware, all the data stored in your WebEngage is either gleaned from your integrated apps and website or can be manually uploaded as a CSV file. Thus, it may so happen that details of internal teammates may not be readily available in your dashboard (even if they are account admins).
Hence, we recommend that you request teammates to sign up on your platform so that we can populate their
User Profiles
with their personal and behavioral data. Doing so will come in handy when:
Creating
Test Segments
Personalizing the test message
to the data of users added to the test segment
Viewing a
User Preview
of the message at
Step 3: Message
Step 1:
Name Your Test Segment
As shown below, the segment's name is prefixed with
'TEST -'
and can be customized henceforth. For example, we have named our segment,
TEST - Design team.
Click to enlarge
Step 2:
Add Internal Users Through Filters
As shown above, you can segment internal members by manually adding their
User ID, Email Address
or
Phone Number
(the chosen filter will depend on the
Unique Identifier
or the parameter that helps identify users in your WebEngage account, as specified by you).
For example, in the above visual, we have selected
User ID
as the filter and have toggled between the
List of Users
(nested under
Users)
and the campaign creation interface to identify and add the respective
User IDs
to the test segment,
Test - Design Team.
Step 3:
Click on the
Create Test Segment
button.
👍
Pro Tip
We recommend that you leverage the diverse device preferences of your teammates to test the
Push Notification
on multiple devices (mobile, tablet), varying screen sizes, app versions and OS (Android, iOS) to ensure that it looks stunning all across!
Editing Test Segment
Step 1:
As shown below, click the
Edit icon
placed next to the field -
Send Test Message To
to edit the users included within the selected
Test Segment.
In doing so, you will be prompted by a pop-up, pre-populated with details of existing users.
Click to enlarge
Step 2:
As shown above, make all your changes and click the
Update Test Segment button
to proceed. For example, we have added new members to the segment,
TEST - Content team.
Deleting Test Segment
Click to enlarge
Step 1:
As shown below, click the
Bin icon
placed next to the field -
Send Test Message To
to delete the selected
Test Segment.
In doing so, you will be prompted to confirm your decision.
Step 2:
Click the
Delete Segment
button on the pop-up.
In doing so, a notification will pop-up on the bottom right confirming the deletion.
Step 6: Preview & Launch
Once you are satisfied with the test results, it's time to send the
Push Notification
to your users! But before that, we recommend that you conduct a quick preview of the campaign's message and settings to ensure that it's in line with your end goal.
The last step of campaign creation presents a snapshot of its:
Target apps and segment
(
Step 1: Audience
)
Campaign Type, Delivery Time, Frequency Capping, DND Hours
and
Queueing
settings
(
Step 2: When
)
Message
Variations
and OS-wise preview
(
Step 3: Message
)
Conversion Tracking
and multivariate test settings
(
Step 4: Conversion Tracking
)
Edit Campaign Before Launch
You can always choose to edit a step by clicking on the
Pencil icon,
placed next to each step's header. In doing so, you will be directed back to the step, as shown below.
Click to enlarge
Simply make your edits, save them, toggle back to
Step 6: Preview & Launch
to continue your review, as shown above.
Saving Campaign as a Draft
If you're unsure or are awaiting approval of the campaign's contents, then you can simply go back to the
central hub of Push
after saving your settings, as shown below. Doing so will automatically save the campaign as a
Draft
,
allowing you to edit or launch it anytime you like.
Launching Scheduled Campaigns
If you have chosen to
schedule/ start the campaign at a later date-time
, then on launching it, its status will indicate
Upcoming
in
Push, List of Campaigns
, as shown below.
Click to enlarge
We hope this has enabled you to create various campaigns, track conversion, automate multivariate testing and test your campaign internally before launch. Please feel free to drop in a few lines at
[email protected]
if you have any related queries or feedback. We're always just an email away!
Updated
7 months ago
So, what's next?
Let's show you how you can analyze Push campaigns to measure their impact on user engagement, conversions, and revenue.
Analyzing Push Campaigns
Copy Page
