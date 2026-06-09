# Creating In-app Campaigns

- URL: https://knowledgebase.webengage.com/docs/creating-in-app-campaigns
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Creating In-app Campaigns
A step-by-step guide on creating In-app Notifications in your dashboard
Engaging users with
In-app Notifications
is an effective way to keep active users engaged with contextual messages (related to their latest app interactions). Your dashboard comes with a highly intuitive 5-step campaign creation interface that makes it easy to create and execute highly personalized campaigns in minutes!
🚧
Must Read
At WebEngage, we are obsessed with enabling consumer business, like yours, to create personalized and contextual experiences that facilitate retention-led growth. This is why user data
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
Create highly targeted messages,
tailored to each user's app interactions in real time!
(
skip to Step 2: When
)
Leverage ready-to-use templates to
engage users with rich In-app Notifications
(
skip to Step 3: Message, Layout
)
Personalize messages
to each user's preferences and behavior, across the various
stages of their lifecycle
(
skip to Step 3: Message
)
Deep link the_Notification_
to specific screens in your app
(
skip to Step 3: Message
)
Automate multivariate message testing
for your campaign - we'll automatically identify a winner and send it to the entire audience
(
skip to Step 4: Conversion Tracking & Variation Distribution
)
How to Access
As shown below, the campaign creation interface can be accessed by clicking the
Plus icon
placed on the top left of
List of Campaigns
,
or the central hub of
In-app.
Click to enlarge
Now, let's walk you through all the steps of campaign creation.
Step 1: Define the Audience
Click to enlarge
1. Name your Campaign
The first step is to give your campaign a unique name that helps you identify its purpose.
2. Select Target Devices
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
3. Select Target Apps
📘
Please Note
This option will show only if you have integrated multiple Android/ iOS apps while
configuring In-app
& target a few of these through the campaign selectively
3A. Specify Target Android Apps
If you have added multiple app credentials while configuring
In-app for Android,
then by default, all the apps will be targeted. You can alter this by removing
Android Package Names
to target specific apps with the message. You will see the following two options:
Send to all apps
send the
In-app Notifications
to all the configured apps.
Send to specific apps
will send the notification to the particular apps of your choice. You can select which apps the notification will be sent to by clicking on the
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
You can choose up to 20 apps at a time.
3B. Specify Target iOS Apps
If you have added multiple app credentials while configuring
In-app for iOS,
then by default all the apps will be selected here as target apps. You can choose to remove the respective
iOS Bundle Identifiers
to target select apps with the message. You will see the following two options:
Send to all apps
send the
In-app Notifications
to all the configured apps.
Send to specific apps
will send the notification to the particular apps of your choice. You can select which apps the notification will be sent to by clicking on the
Pencil
icon. A new modal will open with the list of apps, letting you choose the apps by selecting or deselecting them. You can also search the
Package Name
through the search bar. Click
Save
to save the changes as shown below.
Click to enlarge
This field is hidden if you have selected Android only under
Target Devices
.
📘
Please Note
You can choose up to 20 apps at a time.
4. Define Target Audience (Send To)
One of the key differentiators of successful campaigns is that they're tailored to the behavior and preferences of a specific group of users. Thus, you can create highly contextual
In-app Notifications
for a specific segment of users by selecting the
Segment
or
Lists
from the dropdown placed beside,
Send To,
as shown below.
📘
Please Note
To use
Lists
as Target Audience you have to ensure that the SDKs are updated to:
Android: 4.17.0 or later
iOS: 6.13.0 or later
Click to enlarge
As shown above, on selecting a segment, you will be able to preview a snapshot of
Reachable Users
and the
Rules of Segmentation.
Let's quickly walk you through
Segment Preview
:
Reachable Users
:
Indicates the number of users, from the selected segment, that can be engaged through
In-app Messaging
as a channel, at present.
Rules of Segmentation
:
You can choose to segment your entire user base by 3 broad parameters - User (attributes), Behavior and Technology. Thus,
Segment Preview
presents a snapshot of all the users, against the parameters based on which, they have been grouped together.
Edit Segment
Click on the
Edit icon,
placed next to the dropdown,
Send To,
to edit the selected
Segment.
In doing so, you will be prompted by a pop-up, pre-populated with the existing rules of segmentation, as shown below.
Click to enlarge
Simply make your edits and click
Save
to proceed. In doing so, you will be able to preview the number of reachable users as per your edits.
Create a New Segment
You can choose to create a new _Segment_of users from the campaign creation interface by clicking the
Create Segment button.
In doing so you will be prompted by a pop-up, allowing you to build a new segment, as shown below.
Click to enlarge
Once created, you will be able to access the
Segment
through the
List of Segments
in your dashboard.
🚧
Related Read: Rules of Segmentation
Please refer to
Creating Segments
for step-by-step guidance on how you can segment your users by their
attributes
, behavior (
events
), and technological preferences.
Creating a New, Single-use Segment
You can also choose to create disposable segments or segment users specifically for the campaign and avoid adding it to the
List of Segments
in your dashboard.
Click to enlarge
As shown above, this can be achieved by leaving the field,
Name
blank while creating the segment. In doing so, it will become an
Ad hoc segment
in your dashboard which will be available only for sending the campaign you're currently creating.
Apply Universal Control Group
📘
Conditional Option
This is a conditional option which will be shown only if the you have created Universal control group in your account.
Click here
to know how to create Universal control group.
Click to enlarge
When the box is checked:
the campaign will not be sent to users who are part of the Universal Control Group in the segment that is selected.
When the box is unchecked:
the campaign will be sent to all users that are part of the segment inclusive of the
Universal Control Group
users.
Step 2: Specify When to Show, Which Screen to Show on & How Many Times to Show
Given the highly targeted nature of
In-app Notifications,
they have been categorized as
Triggered campaigns
across your dashboard. These are on-going cycles of communication that are triggered for a specific user only when they:
Perform a certain action or a combination of several actions
(Custom Events
)
in your app
(
Configure for your campaign
)
Spend a certain amount of time browsing through your app or a specific screen in a session
(
Configure for your campaign
)
Visit a specific screen in your app
(
Configure for your campaign
)
Visit a specific number of screens (2, 3, 4...) in a session
(
Configure for your campaign
)
Perform a combination of a few/all the conditions listed above
This makes
In-app
an ideal channel to create contextual app experiences that enable users to move along their
lifecycle
and stay engaged for longer durations.
Click to enlarge
As highlighted above, we have divided
Step 2: When
into two sections:
Campaign Schedule
(helps you determine the lifespan of the campaign)
Where and When to Show
(helps you define the targeting rules, where, when & how many times to show the message in your app)
Here's how you can configure these settings:
1. Setup Campaign Schedule
Since all
In-app Campaigns
are on-going cycles of communication, you can choose to run these for specific periods of time by defining a
Start Date
and
End Date.
Step 1:
Specify the
Start Date
or the date-time on which the campaign should start getting shown to the target audience. As highlighted below:
Select
Now
to activate the campaign immediately
Select
Later
to activate the campaign at a later date-time
Click to enlarge
Step 2:
Specify the
End Date
or the date-time on which the campaign should cease getting shown to the target audience. As highlighted above:
Select
Never
to run the campaign indefinitely
(you can always
Pause
the campaign through its
Campaign Overview
)
Select
Later
to end the campaign at a specific date and time in the near future
2. Specify Where & When to Show
These settings allow you to specify the app screens on which the message must be shown and the context in which users will receive it.
Click to enlarge
As highlighted above:
Select
Show on any screen as soon as the user opens the app
to engage them as soon they start their session
Select
Show on specific screens and/or show when specific conditions are met
to engage users only in the context of their app interactions, in real-time
Selecting this option allows you to configure the following rules:
Where to Show
(Define the screen(s) on which the message will be shown to users)
When to Show
(Define the context in which users will be shown the message)
Let's show you how you can configure these options:
🚧
Skip to
3. Specify How Many Times to Show (Show Limit)
to complete *Step 2: When, of the campaign creation process.
Step 2.1: Where to Show
🚧
Please Note
This rule can be configured only if you have selected,
Show on specific screens and/or show when specific conditions are met
under
2. Where & When to Show
Here you can define exactly where you'd like to show the
In-app Message
by specifying names of app screens and/or data points (tracked across your app) that indicate specific user-app interactions.
Click to enlarge
As highlighted above:
Select
On screens that meet certain Screen Name conditions
to show the message only on specific app screens (
How it works
)
Select
On screens that meet certain Screen Data conditions
to show the message only when users interact with your app in a specific way, no matter which screen (
How it works
)
Select
both options
to show the message on specific app screens when users interact with them in a certain way (
How it works
)
In-app Targeting by Specifying
Screen Name
You can choose to selectively engage users who visit a specific screen or a combination of related screens, in an on-going session. Here's how you can configure this targeting rule:
Click to enlarge
Step 1:
Click the checkbox to select the option,
On screens that meet certain_Screen Name_ conditions
against
Where to Show
Step 2:
As shown above, select a condition to set the context in which the
Screen Name(s)
should be understood by your app.
📘
Screen Names can be prefixed by any one of the following conditions:
Equal to
Not equal to
One of
None of
Starts with
Does not start with
Ends with
Does not end with
Matches regex
(regex is a sequence of characters that define a search pattern - used in several coding languages.
Detailed read
)
Does not match regex
Contains
Does not contain
Is empty
(implies that message can be shown on any screen that has not been tagged with a name in your app's code)
Is not empty
(implies that message can be shown on any app screen that has been tagged with a name in your app's code)
Step 3:
Add the Screen Name(s), as tagged in your app's code
Please check in with your tech team to ensure that the values entered here match the names in the code. Any discrepancy between the two can cause your campaign to fail or show up randomly across your app, leading to confusing user experiences.
Step 4 (Optional):
Click the
Add Condition
button to add more
Screen Names
to the targeting rules
In doing so, a new row will be added to the screen. Repeat
Step 2 & 3
and proceed.
Further, you can choose to club multiple
Screen Names
by the AND/OR logic to define the scope of
In-app
targeting.
🚧
How It Works: Clubbing Screen Names by AND/OR Logic
AND:
Clubbing
Screen Names
by the AND logic helps you narrow down the number of users who receive the
In-app Notification.
It implies that a user will have to
visit all the specified Screens, in any order,
to receive the campaign.
OR:
Clubbing
Screen Names
by the OR logic helps you increase the number of users who receive the
In-app Notification.
It implies that a user will receive the campaign if they
visit any one of the specified Screen Names.
🚧
Skip to
configuring
When to Show
to define the context in which a user should receive the
In-app Notification
In-app Targeting by Specifying
Screen Data Attribute
Depending on the end-goal of your campaign, you can choose to engage only those users who interact with your app in a specific manner, no matter which screen they're on. This can be achieved by tracking app-user interactions as
Screen Data Attributes.
Here's how you can configure this targeting rule:
Click to enlarge
Step 1:
Click the checkbox to select the option,
On screens that meet certain_Screen Data_ conditions
against
Where to Show
Step 2:
As shown above, add the
Screen Data Attribute(s),
as tracked in your app's code
Please check in with your tech team to ensure that the values entered here match the values in the code. Any discrepancy between the two can cause your campaign to fail or show up randomly across your app, leading to confusing user experiences.
Step 3:
Select the appropriate data type, as conveyed by your tech team (so that your app understands the value of the specified
Screen Data Attribute)
📘
Any one of the following data types can be selected here:
Number:
Indicates that the value of the specified data attribute contains only numbers.
String:
Indicates that the value of the specified data attribute contains text, numbers, special characters, spaces or a combination of these.
Boolean:
Indicates that the specified data attribute has one of two possible values denoted by
true
or
false
.
Date:
Indicates that the value of the specified data attribute contains a date/date-time.
Step 4 (Optional):
Click the
Add Condition
button to add more
Screen Data Attributes
to the targeting rules
In doing so, a new row will be added to the interface. Repeat
Steps 2 & 3
to proceed.
Further, you can choose to club multiple
Screen Data Attributes
by the AND/OR logic to define the scope of
In-app
targeting.
🚧
How It Works: Clubbing Screen Data Attributes by AND/OR Logic
AND:
Clubbing
Screen Data Attributes
by the AND logic helps you narrow down the number of users who receive the
In-app Notification.
It implies that a user will have to
meet all the specified Screen Data conditions
to receive the campaign.
OR:
Clubbing
Screen Data Attributes
by the OR logic helps you increase the number of users who receive the
In-app Notification.
It implies that a user will receive the campaign only if they
meet any one of the specified Screen Data conditions.
🚧
Skip to
configuring
When to Show
to define the context in which a user should receive the
In-app Notification
Thus, whenever a user visits a screen that contains the term _'
listing'
in their tagged
Screen Name
AND happens to explore any of the specified
Sub-category IDs,
they'll be nudged with the
Free Shipping offer!
Step 2.2: When to Show
🚧
Please Note
This rule can be configured only if you have selected,
Show on specific screens and/or show when specific conditions are met
under
2. Where & When to Show
Here you can define the context in which the
In-app Notification
must be shown to a user during an on-going session. This could be anything like - total time spent on a screen or in the app, a particular action
(
Custom Event
)
performed by the user, and so on.
Click to enlarge
As highlighted above:
Select
Total time spent on a screen in a session by a user is
<enter number>
seconds
to display the message only once the specified duration is exceeded
Select
Total time spent on your app in a session by a user is
<enter number>
seconds
to display the message only once the specified duration is exceeded
Select
Number of screens viewed in a session by a user is <select value>,
<enter number>
to display the message only once the specified criteria is met
Select
User does one or more events
to display the message only if the user performs an action (
Custom Event
) or a combination of several actions (in any order), in the context of the added
Event Attribute filter(s)
, during a session (
How it works
)
Select
all or multiple options
to display the message when a user's actions match any one of the configured rules
For example, in the visual above, the
In-app Notification
will be shown to all users who
have spent more than 10 secs on a screen OR have spent more than 30 secs on the app OR have viewed more than 5 screens OR have performed the event, Browse.
Triggering In-app Notification When User Performs an Event or Multiple Events
Selecting the option,
User does one or more events
against
When to Show
,
allows you to engage only those users of the target audience that perform specific actions in your app, in a session. These actions
(
Custom Events
)
could be anything like
Browse, Search, Page_Viewed, Product_Viewed, Checkout_Started, Wishlist_Viewed
and so on.
Here's how you can configure this rule:
Click to enlarge
Step 1:
Click the dropdown nested under the option to select a
Custom Events
(in the context of which users will receive the message)
Step 2 (Optional):
Click the
Filter icon
to add
Custom Attribute filters
to the selected Event
Further, you can choose to club multiple event attributes by the AND/ OR logic to define the scope of occurrence of the event. Doing so ensures that the
In-app Notification
is triggered for a user only when they perform the event in the context of the applied attribute filters.
🚧
How It Works: Clubbing Custom Event Attributes by AND/OR Logic
AND:
Clubbing
attribute
filters by the AND logic helps you narrow down the number of users who receive the message. It implies that the
In-app campaign
will be shown to only those users who perform the
Custom Event
in the context of all the event attributes added to it.
OR:
Clubbing
attribute
filters by the OR logic helps you increase the number of users who receive the message. It implies that a user will receive the campaign if they perform the
Custom Event
in the context of any one of the specified event attributes.
Step 3 (Optional):
Click the
Add Event
button to specify more actions
In doing so, a dropdown will be added to the screen, allowing you to select from a list of all the
Custom Events
being tracked for your account. Repeat
Step 2 & 3
to proceed.
Further, you can club multiple
Custom Events
by the AND/OR logic to define the context in which the occurrence of all specified events should be understood by us.
3. Advanced Control for App Personalisation Channels
We have now added additional controls to our In-app Notifications, that will allow you to define a campaign's view limits, recur campaigns, etc. Here is more information on the specifics of the feature.
Click to enlarge
Frequency Capping
This setting caps the number of notifications a user can view within a session along with option to set the time interval between 2 notifications. You can set Frequency Capping as follows:
Follow
: Configured account level FC setting will be followed.
Ignore
: Configured account level FC setting will be ignored.
📘
Set Frequency Capping Limits
If you have not set up Frequency Capping yet, then you can choose to configure it by clicking the Configurations > Frequency Capping on the left navigation panel. Once set, you will be able to send all your campaigns with FC enabled.
Detailed read on
How to configure FC & Time Gap
.
Lifecycle
Lifecycle
is an enhancement to our earlier ‘Max Limit’ option. This feature is a campaign level setting that allows you to set the number of times a notification is to be shown to a user and whether it should be repeated/ recurred. This can be set using the following two choices:
A Cycle Ends when Clicked Once with No View Limit:
When you select this option, your users will keep receiving the notification (in every new session) until they click on it once. If they have either viewed or dismissed the notification, the cycle will persist.
A Cycle Ends when Clicked Once or Viewed up to 'n' times:
When you select this option, you have the flexibility to determine the maximum number of times a notification should be viewed by a user. However, the cycle concludes with just one click. Let's illustrate this with an example: If you set the view count to 5, your users can potentially view the campaign notification up to 5 times. But, if they click on the notification during the 4th viewing, the cycle ends, and they won't encounter it for the 5th time.
Repeat the cycle
Once you've made the previous selections, you also have the flexibility to determine the frequency at which your cycle repeats, i.e. every Minute/Hour/Day/Week/Month; these resets occur based on the calendar week that starts from Monday to Sunday and not when the user views them. Moreover, you can decide the duration of this repetition: either
'Until the campaign ends'
or the
'Upto'
option.
👍
Here's an example of what happens when you choose either of the options
Example 1:
If you choose to repeat the cycle ‘Daily’ and 'Until the campaign ends,'
your users will receive the notification every day until the campaign concludes. Consider the same scenario as the previous example, the notification will be sent to your user upto 5 times in a day (in different sessions), but when they’ve clicked it on their 4th viewing, they won’t be seeing it for the 5th time
on that day
. However the next day the counter will reset and user will again become eligible to view the campaign upto 5 times or until clicked once. This cycle will continue until the campaign ends.
Example 2:
If you choose the 'Weekly' option and 'Upto' 3 times
then, considering the previous example, a user can view the notification up to 5 times a week (as per calendar week) but if they click on it, for instance, on their 4th viewing on Tuesday, they won't see it for the rest of the week (until Sunday). But because the cycle is set to repeat weekly, it will restart again at the start of the new calendar week i.e Monday. Now consider following scenarios for Week 2, 3 and 4 -
Week 2 - User completes all 5 view across the week but never clicks
Week 3 - User never opens the app. (This will be counted in the cycle)
Week 4 - User views the campaign once and clicks on it
Since the limit of repeating the cycle was
'Upto 3'
, the user will no longer be viewing the campaign after 4th week's 1st view (since the campaign was clicked).
Step 3: Create the Message
Click to enlarge
As highlighted above, the message creation interface comes loaded with intuitive features like
Variations
,
Layouts
,
Deep linking
,
Dynamic Personalization
,
Themes
and
Message Preview
- enabling you to create high impact
In-app Notifications
in minutes.
Let's get you acquainted with each feature:
Select a Layout or Template
You can choose from the following ready-to-use templates or layouts to create a
Variation
.
Click to enlarge
Let's quickly walk you through each layout:
Layout
Header
A short and simple template,
Header Notifications
are ideal for keeping users engaged with contextual offers and updates. You can easily tailor the message, icon and button link to each user and customize the theme as per your brand guidelines in an instant!
Personalizing Header Notification to each user's preferences & behavioral history
For example, in the visual above, we have personalized the notification to the user's first name and the last product they viewed in your app. All you need to do is:
Step 1:
Create a
Personalized Message
Step 2 (Optional):
Add a
Background Image
Step 3:
Configure the
Buttons
Step 4:
Customize the
Theme
and you're good to go!
🚧
Related Read
Image and text guidelines
for creating Header style In-app messages
Footer
A small buttonless template, you can easily personalize
Footer Notifications
to each user's preferences and behavioral history, creating minimally intrusive In-app experiences.
Personalizing Footer Notification to each user's preferences & behavioral history
For example, in the visual above, we have tailored the notification to the user's first name and the last product they viewed in your app. All you need to do is:
Step 1:
Create a
Personalized Message
Step 2:
Configure the
On-click Action
Step 3:
Customize the
Theme
and you're good to go!
🚧
Related Read
Image and text guidelines
for creating Footer style In-app Messages
Popout Modal
A comprehensive template, the
Popout Modal
is ideal for prompting users with a prominent message, accompanied by a thumbnail-sized image and CTA.
Click to enlarge
As highlighted above, you can easily customize the template's button, image, links, message, and theme to create highly contextual experiences. All you need to do is:
Step 1:
Create a
Personalized Message
Step 2:
Configure the
Button
Step 3:
Customize the
Theme
and you're good to go!
🚧
Related Read
Image and text guidelines
for configuring the Popout Modal in Landscape or Portrait Mode
Classic Modal
A rich media template, the
Classic Modal
is ideal for engaging users with brief, yet visually enticing messages.
Personalizing Classic Modal to each user's preferences & behavioral history
As highlighted above, you can easily customize the template's buttons, image, links, message, and theme to create highly contextual experiences. All you need to do is:
Step 1:
Create a
Personalized Message
Step 2:
Add a
Background Image
Step 3:
Configure the
Buttons
Step 4:
Customize the
Theme
and you're good to go!
🚧
Related Read
Image and text guidelines
for configuring the Classic Modal in Landscape or Portrait Mode.
Creating
Custom HTML
templates for Classic Modal.
Full-screen Modal
A visually impressive template, the
Full-screen Modal
brings the best of both - message & media to help you engage active users in style.
Personalizing Full-screen Modal to each user's preferences & behavioral history
For example, in the above visual we have personalized the notification's message and image to the user's first name, the product last viewed by them, respectively. All you need to do is:
Step 1:
Create a
Personalized Message
Step 2:
Configure the
Buttons
Step 3:
Customize the
Theme
and you're good to go!
🚧
Related Read
Image and text guidelines
for configuring the Full-screen Modal in Landscape or Portrait Mode.
Creating
Custom HTML
templates for Full screen Modal.
Screen Blocker
A pure rich media template, screen blockers are ideal for promoting fashion collections, movies, courses, albums and the likes of it, with custom banners.
Personalizing Screen Blocker to each user's preferences & behavioral history
For example, in the above visual, we have contextually personalized the notification's banner to the product, last viewed by the user. All you need to do is:
Step 1:
Add a
Background Image
Step 2:
Configure the
Buttons
Step 3:
Customize the
Theme
and you're good to go!
🚧
Related Read
Image specifications
for Screen-blocker style In-app messages in Landscape or Portrait Mode
Depending on the layout selected by you, the steps of message creation may vary.
Here's a generic guide to help you create dynamically personalized_In-app Notifications_:
Add Message
👍
Fact Check
If your message is in a language that incorporates right-to-left alignment, then it will automatically be oriented that way when users receive the
In-app Notification!
Add Title & Description
(Applicable to all Layouts except
Screen Blocker
| Number of characters accepted for each Layout differs,
details
)
Click to enlarge
Using the personalization icon nested in the fields,
Title
and
Description
, you can easily create dynamically personalized content. Simply select a value from a list of all the
Custom User attributes
and
Custom Events
being tracked for your app and place them appropriately within the text. We'll add the exact value tracked for each user, helping you deliver one-on-one messages at scale :)
Click to enlarge
For example, in the above visual, we have personalized the message with: User attribute,
First Name
-
{{user['system']['first_name']}}
Thus, whenever the message is sent to a user, we will populate the
First Name
with the respective values gleaned for their user profile.
Add Icon/ Background Image
(
Icon & Image specs for each Layout
)
Click to enlarge
As shown above, a generic Icon/Image can be added in two ways:
1. Insert Icon/ Image Link:
The image must be hosted on a crawlable/publicly accessible domain to ensure that it renders for all users receiving the message.
2. Upload Icon/ Image:
Click the
Upload
button placed next to the field, image and select a file from your desktop. In doing so, the image will get hosted on WebEngage's domain:
https://afiles.webengage.com
.
You can always click the
Reset
button to link/upload a new image.
🚧
Personalizing Notification's Icon/Image to Each User's Interests
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
as the path parameter. Then manually add the image format like,
.png, .jpeg, .jpg, .gif,
at the end of the link structure
(
Step-by-step guide on how to execute this
)
Templates
Spin the Wheel
WebEngage now introduces pre-built HTML templates that you can use for In-app campaigns to make your users more entertained, with the spin the wheel template.
Once you reach the message tab of creating your In-app notifications, you are presented with a ‘Select a Layout’ where you can find various layouts and templates WebEngage provides.
Click on ‘
Spin the Wheel
’ template either by scrolling down in this tab or by using the search tab, or by clicking on ‘templates’ in the dropdown on the right.
You’re then presented with the following fields
The Layout Section consists of 2 fields :
Template i.e. Spin the Wheel, and
Type in portrait mode.
Note:
This template will only be shown when the phone is in Portrait Mode and will not appear when the phone is in landscape mode.
You can see the pre-entered HTML code of Spin the Wheel template, which can be customized according to your preference.
Event Tracking
We also offer you the ability to track the events that users will be doing with respect to this template.
Here are 2 custom events that you can track for the Spin the Wheel template, which can be viewed from the Event Analytics page.
When users click on the Spin button ‘
In-app Template - Spin Clicked
’ is tracked and following are the attributes of this event -
Win
,
Respin
, and
Respin count
.
When users click on the copy coupon code ‘
In-app Template - Copy Clicked
’ is tracked, and this is the attribute for the event is- Coupon Code.
📘
Please note
You would need to update to Android Core SDK v4.11.0 and iOS Core SDK v6.7.0 for tracking spin button and copy code events.
On the campaign overview page you can find the stats of ‘Clicks’ and ‘Closes’ which are tracked on ‘Continue Shopping’ and ‘Close’ icon clicks respectively.
Scratch Card
Once you reach the message tab of creating your In-app notifications, you are presented with a ‘
Select a Layout
’ where you can find various layouts and templates WebEngage provides.
Click on ‘
Scratch Card
’ template either by scrolling down in this tab or by using the search tab, or by clicking on ‘templates’ in the dropdown on the right.
You’re then presented with the following fields. The
Layout Section
consists of 2 fields :
Template - Scratch card, and
Type - portrait mode.
Note:
This template will only be shown when the phone is in
Portrait Mode
and will not appear when the phone is in landscape mode.
You can see the pre- entered HTML code of Scratch Card template, which can be customized according to your preference. You also have the option to show or hide the close button, which by default will be selected as hide.
Event Tracking
You will also have the ability to track the events that users will be doing with respect to this template.
Here are 2 custom events that you can track for the Scratch card template, which can be viewed from the Event Analytics page.
When users scratch the card, ‘In-app Template - Card Scratched’ and the attributes are:
Card Scratched, Win
When users click on the Close button, ‘In-app Template - Close clicked’ is tracked, and this is the attribute for the event is -
Coupon Code
.
On the campaign overview page you can find the stats of ‘Clicks’ and ‘Closes’ which are tracked on ‘Continue Shopping’ and ‘Close’ icon clicks respectively.
NPS Rating Template
WebEngage now introduces pre-built HTML templates that you can use for NPS surveys to make gathering user feedback more engaging.
Once you reach the message tab of creating your In-app notifications, you are presented with a ‘Select a Layout’ page where you can find various layouts and templates WebEngage provides.
Click on ‘NPS Rating’ template either by scrolling down in this tab or by using the search tab, or by clicking on ‘templates’ in the dropdown on the right.
Note
: This template will only be shown when the phone is in Portrait Mode and will not appear when the phone is in landscape mode.
You can see the pre-entered HTML code of the NPS Rating template, which can be customized according to your preference.
Event Tracking for NPS**
Response tracking of your users can be done by the Custom events on ‘Submit’ button click and passing rating count and response as attributes.
Event name of NPS Rating ‘Submit’ button click is ‘In-app Template - Submit NPS Rating Clicked’.
Attributes for ‘In-app Template - Submit NPS Rating Clicked’ :- Rating : 1 - 10 ; Response filled : Yes/No ; Response : String.
Carousel
Carousel Template is a visually engaging, auto-scrolling layout designed to display a series of cards that your users can swipe through, offering a more dynamic and interactive user experience.
Once you reach the Message tab while creating your In-app notification, you will be presented with the Select a Layout modal.
Here, you can either scroll, search, or filter by ‘Templates’ in the dropdown to find and select the ‘Carousel’ template.
Upon selecting the Carousel template, the Layout section will display the field type to be Portrait, which cannot be changed
Note:
This template will only be shown when the phone is in Portrait Mode and will not appear when the phone is in Landscape Mode.
Custom HTML Section
You will find the Carousel template’s HTML code pre-filled in the Custom HTML field. This HTML is designed to:
A full-screen layout that appears only in portrait mode.
Three predefined carousel cards
Users can navigate through cards using finger swipe gestures
The carousel will auto-scroll to the next card every 3 seconds (configurable) if no interaction is detected
User Interaction Tracking
WebEngage tracks user engagement through event-based analytics for Carousel templates:
Carousel Card CTA Click
Event name: In-app Template - Carousel Card Clicked
Attribute: Card Number (Numeric value representing which card was clicked)
Explore More
button clicks are tracked as
CLICKS
Close
icon taps are tracked as
CLOSES
Raw Preview
As the name suggests, it renders the
In-app Notification
with the raw message and attributes, as added by you to the
Message
.
Click to enlarge
User Preview
Allows you to view the
Notification
for an actual user from your account by populating it with data from their user profile, as per the elements of personalization added to the
Message
.
Click to enlarge
For example, in the visual above, we have visualized the
In-app Notification
for the
User ID, katherinem_2206,
personalizing the
Icon Image, Button Link
and
Message.
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
of the campaign's target segment (as specified at
Step 1: Audience
)
to identify an ideal user
Step 3:
Click the
Search and Populate
button
In doing so, you will be shown a summary of the values against the respective attributes and events included in the message. This is a good way to ensure that all the values are available for the user, if not then you can enter an alternate
User ID.
Step 4:
Click the
See Preview
button on the pop-up to visualize the notification with real user data.
Configure Buttons (CTA) & Close Button
Barring
Footer Style Notifications
,
you can add customized buttons to all the
In-app Layouts
being created by you. As shown below, you can also choose to disable the
Buttons
for all
Layouts
if the end goal of the campaign is to simply convey information.
Click to enlarge
Here's how you can configure CTAs:
🚧
Or
skip to
deep linking entire
footer style notification
to a specific app screen
Setting up Call-to-Action Buttons (Primary/Secondary)
Step 1: Add Label (Text):
Label
refers to the button text, motivating users to perform a certain action. As shown above, we have added a custom label,
BUY NOW
nudging active users to start shopping before the sale ends!
Step 2: Insert Deep Link (On-click Action):
You can deep link buttons to specific screens in your
Android
and
iOS apps,
as shown above.
Further, you will notice that the deep link specified for the
Android app
is in a different format compared to the
iOS
link. This is because we have created a unique
URI
for our
Android app screens
while we are leveraging
Universal Links
for the iOS app (the same link is also used for our website).
🚧
Personalizing On-click Action to a User's Preferences or Behavioral History
You can easily
personalize the
On-click Action
to your users based on the
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
Setting Up Close Button
(Applicable only to
Header
&
Classic Modal
)
It's always advisable to allow users to close
In-app Notifications
to ensure that they continue browsing instead of quitting your app. However, in case you'd like to force specific behavior like
app updates, joining a live class/session, renewing video streaming subscription
and so on, then you can always choose to hide the button by clicking the toggle switch, as shown below.
Further, you can customize the button's label or text to anything you like. For example, we have changed it to a more subtle term,
NO, THANKS
for our notification.
Click to enlarge
👍
Fact Check
Each time a user clicks the
Close Button,
we track it as the performance indicator -
Unique Closes
for all
In-app campaigns.
Setting up On-click Action
(Applicable only to
Footer Notifications
)
Just like you can deep link buttons to specific screens of your
Android
and
iOS
apps, you can choose to deep link a
Footer Notification
by specifying an
On-click Action,
as shown below. This link will be applied to the entire notification, barring the
Close Icon.
(
How to personalize the on-click action to each user's preferences or behavioral history
)
Click to enlarge
Customize Theme
Depending on the
Layout
selected by you, the number of customizable elements may vary. Hence, we have mentioned the limitations of each component concerning all the available layouts, in the following sections.
🚧
Customizing In-app Notification's Appearance in Your App Before Showing it to Users
While we have tried our best to accommodate all your branding/theme related needs, you can always make additional changes in the notification's
colors, fonts, icons, button links, text
in your app, before showing it to your users. This can be achieved by setting up
In-app Callbacks.
Here's how you can go about it:
Step 1:
Tie up with your tech team to set up the callback,
In-app Received
or
In-app Prepared.
Here's how you can go about it:
Android apps
iOS apps
React Native apps
Hybrid apps (Cordova, PhoneGap, Ionic)
Xamarin.Android apps
Xamarin.iOS apps
Step 2:
Collaborate with the tech guys to build the required customizations into your app's code so that it knows what to do when the callback is called.
Step 3:
Test and implement :)
Here's how you can create a custom theme for each_In-app Notification_:
Configuring Close Icon
(Applicable only to
Footer
,
Screen Blocker
&
Full-screen Modal
Layouts)
Close Icon:
It's always advisable to allow users to close
In-app Notifications
to ensure that they continue browsing instead of quitting your app. However, in case you'd like to force specific behavior like
app updates, joining a live class/session, renewing video streaming subscription
and so on, then you can always choose to hide the close icon by selecting
Hide,
as shown below.
Click to enlarge
Close Icon Color:
As shown above, using the
Color Selector,
you can customize the
Close Icon's
color as per the background hues.
👍
Fact Check
Each time a user clicks the
Close Icon,
we track it as the performance indicator -
Unique Closes
for all
In-app campaigns.
Configuring Background Color
(Applicable to all layouts except
Screen Blocker
)
As shown below, you can customize the notification's background color by selecting a hue from the
Color Selector
or by specifying a custom
CMYK Hex(#) code
as per your brand colors.
Click to enlarge
🚧
Please Note
The color of the
Buttons
of
Classic Modal
and
Header
style notifications are automatically derived from the
Background Color
and cannot be specified separately.
Configuring Buttons
(Applicable only to
Popout Modal
,
Screen Blocker
&
Full-screen Modal
)
As shown below, you can customize the
Button Text Color
and
Button Background Color
by selecting a hue from the
Color Selector
or by specifying a custom
CMYK Hex(#) code
as per your brand colors.
Configuring Text & Fonts
(Applicable to all layouts except
Screen Blocker
)
Font Family:
As shown below, you can choose from a list of all the custom fonts uploaded to your dashboard
(
specifically for In-app campaigns
)
to customize the
Title & Description's
font style.
Font Color:
As shown above, you can customize the color of your
Title and Description
by selecting a hue from the
Color Selector
or by specifying a custom
CMYK Hex(#) code
as per your brand colors.
Text Alignment:
As shown above, you can choose to align the
Title and Description
to
Left, Center
or
Right,
as per your design needs.
Text Wrap:
As shown above, if your notification's
Title
includes a fairly long sentence, then you can choose to
Wrap
it (by selecting
Yes)
to ensure that the entire text is displayed.
Creating Custom HTML Templates
(Supported only for
Classic Modal
and
Full screen Modal
)
📘
Please Note
JavaScripts are now supported for in-apps, allowing you to create engaging experiences with spin the wheel, carousel, scratch card, and more.
If you would like to run some use cases, which cannot be fulfilled through our Preset templates, then
Custom HTML
template gives you that flexibility. Custom HTML gives you the capability to completely own up the content area and run engaging in-app notification campaigns as per your use cases. With these Custom templates, you can add GIFs or run Videos within in-app notifications.
To create a campaign with custom template:
Create a in-app notification campaign
On Message tab, Select the layout type as Classic or Full screen
Select the Template as 'Custom HTML' and add the content body in Raw HTML format.
Preview Notification
As shown below, the left half of the campaign creation interface provides a real-time preview of the
In-app Notification
being created by you.
Click to enlarge
At any given point, you can toggle between a
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
In doing so, you will be prompted to select a
Layout
to draft the particular variant
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
Step 4: Set up Conversion Tracking & Variation Testing
The fourth step of campaign creation allows you to measure the effectiveness of your campaign in various ways like:
Tracking conversions
for a specific goal
Comparing performance against a
control group
Testing multiple variations
of the message and identify a winning version
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
Click the toggle button to enable the setting and configure it.
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
Click the toggle button to enable the respective settings and configure them.
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
In-app campaigns.
As shown below, you can use the toggle switch to enable it.
Click to enlarge
Step 1: Select a Conversion Event
The term,
Conversion Event
is an alias that helps you identify the event you expect users to perform after receiving the
In-app Message.
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
Jimmy Choo Pumps Purchased, Episode 3 Streamed, Chapter 7 Started, MF Investment Done, Game Credits Purchased
and so on.
This can be done by adding
attribute filters
to the selected
Conversion Event
.
Here's how you can go about it:
Step 1:
As shown above, click on the filter icon placed next to the drop down
In doing so, you will be prompted by a pop-up allowing you to select an attribute and specify its value
For example, in the above visual, we have filtered the
event, Checkout Completed,
by the attribute filter,
Cart Value
which is
greater than 100 ((indicates the monetary value of the transaction, irrespective of the
currency
)
This implies:
Only those users who make a purchase of more than 100 (as per the account's currency) will be counted towards the campaign's conversion metrics.
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
In-app campaigns
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
🚧
Must Read
Why you should (almost) always use
Control Group
to measure the effectiveness of your campaign and
how it works in your dashboard
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
Skip to:
How to set up
Send Winning Variation Automatically
for testing In-app (triggered) campaigns
Variation Distribution (Multivariate Testing)
If you have created multiple versions of the
In-app Notification
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
if you are unwilling to test the campaign with a minimum of test audience of 500 messages.
Here's how each setting works:
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
📘
Please Note
Given the highly targeted nature of
In-app campaigns,
they are treated as
Triggered campaigns
across your dashboard. These are ongoing cycles of communication that are sent to users only when they perform a certain action or
Event
. Thus, the most scientific way to test
Variations
of an
In-app campaign
is by ensuring that a significant number of messages are delivered before we draw a comparison.
Step 1: Specify Size of Test Audience
The
Test Audience
can be defined only in terms of the number of messages delivered. This means that
Variation
testing will continue until the specified number of messages have been successfully delivered.
As shown below, we have specified that a minimum of 1500 messages must be triggered to users to identify a winning version. This means that all the
Variations ( &
Control Group, if enabled
)
will be equally divided amongst the specified number.
Click to enlarge
Step 2: Select Win Criteria
The
Win Criteria
is a performance indicator that helps us determine a winning
Variation
according to the campaign's end goal. As shown above, it can be defined as any of the following:
Impressions
Clicks
Conversions
Once we identify a winning
Variation
, it will be sent as the only campaign to all the subsequent users who perform the
trigger event
.
🚧
Quick Read:
How automated variation testing works for triggered campaigns
Manual Distribution
If you are unwilling to test the
In-app campaign
with a minimum test audience of 500 messages, then you can choose to test the
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
Keep in Mind
In a particular campaign, Custom Control Group and campaign control group cannot be applied together.
Universal control group can be added irrespective of Custom Control Group or Campaign Control Group is selected.
In case multiple control groups are applied within same campaign (E.g: Universal Control Group + Custom Control Group or Universal Control Group + Campaign control): In this case, since the users in both the control group are mutually exclusive, the overall control group size will increase and the target audience size will decrease.
Step 5: Test Campaign
Test your In-app campaigns just as your users would experience them. Previously, you could only preview the UI on the dashboard, but now you can conduct full end-to-end tests on devices.
Steps to Test In-App Campaigns
You can test the In-app from 2 places
The Message step of the campaign creation
The Test Campaign step of the campaign creation
Create a test segment based on user IDs by clicking on the ➕ icon
Trigger the test In-App by clicking on the Test Campaign button (Prerequisite Push permission should be granted and the user should be reachable for Push for test In-App to be rendered on the user’s device).
📘
Testing your Campaigns are optional
Although testing your campaign with an internal test is optional, WE do highly recommend it.
Behavior of Test In-App Notifications
If the app is in the foreground you’ll get the Test In-App on the app.
If the app is in the background or killed state, a push notification will be received. On clicking on it the app will be opened and the Test In-App will be shown.
If there is already an In-App shown on screen it will be dismissed and the Test In-App will be shown to the user. On dismissing the Test In-App, previous In-App will be visible again.
If there is already a Test In-App shown on screen, it will be dismissed and the new Test In-App will be shown to the user. On dismissing the Test In-App previous test In-App will not be visible again.
The Push can fail in certain scenarios and there can be a delay as well so rendering can delay after clicking on the Send Test Button.
Step 6: Preview & Launch
Once you've set up the campaign it's time to start to engaging app uses! But before that, we recommend that you conduct a quick preview of the campaign's message and settings to ensure that it's in line with your end goal.
Click to enlarge
As shown above, the last step of campaign creation presents a snapshot of its:
Target apps and segment
(
Step 1: Audience
)
Target screens, message frequency and trigger settings
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
Edit icon,
placed next to each step's header. In doing so, you will be directed back to the step.
Simply make your edits, save them, toggle back to
Step 6: Preview & Launch
to continue your review, as shown above.
Saving Campaign as a Draft
If you're unsure or are awaiting approval of the campaign's contents, then you can simply go back to the
central hub of In-app
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
In-app, List of Campaigns
, as shown below.
Click to enlarge
What Happens After a Campaign is Launched?
Once launched, messages are sent to users included in the target audience as per the campaign's settings. Throughout it's run time, the campaign's status will indicate
Running
(in
In-app, List of Campaigns
)
until it ends or is manually paused by you.
1. Analyzing Campaign's Performance
You can analyze each campaign's real-time impact on user engagement, conversions, and revenue by accessing its
Overview section
through the
List of Campaigns
of In-app
, as shown below.
2. Modifying the Campaign
Further, you can always choose to
Edit
or
Pause
an
Upcoming
or
Running
)
campaign if you feel the need to.
(
Step-by-step guide on modifying In-app campaigns
)
3. Scheduling Campaign Reports
Once you have launched a campaign, you easily monitor its performance through scheduled reports, delivered straight to your (& your teammate's) inbox! This can be configured through the campaign's analysis section.
Here's how you can go about it.
Further, you can also schedule Channel-wise reports to monitor the overall performance of
In-app
through the
Settings
section of your account.
Here's how you can go about it
.
We hope this has equipped you with a robust understanding of how you can:
Contextually engage app users with visually stunning in-app messages.
Track conversions.
Automate multivariate testing.
Please feel free to drop in a few lines at
[email protected]
in case you have any related queries or feedback. We're always just an email away!
Updated
2 months ago
So, what's next?
Let's show you how you can analyze In-app campaigns to measure their impact on user engagement, conversions, and revenue.
Analyzing In-app Campaigns
Copy Page
