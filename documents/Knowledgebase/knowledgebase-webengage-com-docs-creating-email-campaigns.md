# Creating Email Campaigns

- URL: https://knowledgebase.webengage.com/docs/creating-email-campaigns
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Creating Email Campaigns
A step-by-step guide to creating Email campaigns in your dashboard
📘
This guide only covers the creation of One-time, Triggered & Recurring Campaigns
Looking to automate
Transactional Email Campaigns?
Let's get you started!
Emails
are an effective channel for conveying updates throughout a user's lifecycles and keeping them engaged. Your dashboard comes with a highly intuitive 6-step campaign creation interface that makes it easy to execute highly personalized campaigns in minutes!
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
Leverage our extensive templates library to
create beautiful & highly responsive Email templates in minutes!
(
skip to Drag & Drop Email Editor
)
Personalize messages
to each user's preferences and behavior, across the various
stages of their lifecycle
(
skip to Step 3: Message
)
Automate multivariate message testing
for your campaign - we'll automatically identify a winner and send it to the entire audience
(
skip to Step 4: Conversion Tracking & Variation Distribution
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
Important
Please ensure that you have integrated an
ESP (Email Service Provider)
with your account before proceeding as it enables campaign delivery to all your users.
Here's the integration guide.
Select Campaign Type
As shown below, the campaign creation interface can be accessed by clicking the
Plus icon
placed on the top left of the
central hub of Email
.
In doing so, you will be prompted to select the type of campaign you'd like to create.
Click to enlarge
Let's quickly walk you through each campaign type:
One-time
These are stand-alone messages that are sent to your users only once and generally comprise of time-bound offers, festive deals, product updates, and so on. Such campaigns end as soon as they're delivered to the target audience.
When:
Launch immediately or Schedule for later
Delivery Frequency:
Once only
🚧
Skip to Step 2, When:
Campaign Schedule > Setting up One-time Campaign
Triggered
These are ongoing cycles of communication that are sent to only those users of your target audience, who perform a particular
event
on your app/website.
When:
Launch immediately or schedule for later
Delivery Frequency:
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
Launch immediately or schedule for later
Delivery Frequency:
Daily, Weekly or Monthly
🚧
Skip to Step 2, When:
Campaign Schedule > Setting up Recurring Campaign
Transactional
These are highly contextual messages that your users expect to receive while interacting with your brand through your app, website or offline. This could be anything like
acknowledging user interactions like, sign up (welcome newsletter), password reset, payment confirmation (invoice), order confirmation or conveying payment reminders, account statements
and so on.
When:
Launch immediately
Delivery Frequency:
Whenever a specific
Event
occurs in your backend
🚧
Continue here...
Step-by-step Guide to Creating Transactional Email Campaigns
Now, let's walk you through all the steps of campaign creation.
Step 1: Define the Audience
1. Name your Campaign
Click to enlarge
As shown above, the first step is to give your campaign a unique name that helps you identify its purpose.
Tag
is a handy feature that helps you categorize your campaigns as per their purpose, target audience, frequency, or any other parameter that makes them easier to search for.
Tags
also help you analyze campaign results for a group of campaigns that belong to a tag.
2. Select Content Type
Click to enlarge
As shown above:
Select
Promotional
to send the Email to only those users of the target audience who have not unsubscribed to your channel.
Users can choose to unsubscribe to your Email channel anytime they like by clicking the
Unsubscribe Link
added to the message at
Step 3: Message
.
Select
Transactional
to send Email to all users in the target audience, irrespective of whether or not they've unsubscribed to your channel in the past.
Since selecting this option overrides your users' channel preferences, we recommend that you use it cautiously.
🚧
Content Types ARE NOT RELATED TO Campaign Types / ESP Service Types
Please note that the content type selected here has no correlation to:
The
Transactional/ Promotional Messaging Services
provided by your
ESP
.
The
Transactional Email Campaigns
you can send through
WebEngage's Transactional Campaign API.
3. Select Audience Type
One of the key differentiators of successful campaigns is that they're tailored to the behavior and preferences of a specific group of users. Thus, by selecting an
Audience Type,
you can choose to target a specific segment of users or combine several segments to define your
Email campaign's
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
Send to users in multiple segments and/or exclude users from these segments
to narrow down the audience to a very specific user persona, defined by including and excluding several segments from the target audience
(How to set up the conditions -
Send To
&
Don't Send To
)
4. Select Target Segment(s)
Here's how you can set up each
Audience Type:
4A. Select a Segment (Send To)
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
Email
as a channel, at present.
Rules of Segmentation
:
You can choose to segment your entire user base by 3 broad parameters - User (attributes), Behavior and Technology. Thus,
Segment Preview
presents a snapshot of all the users, against the parameters based on which, they have been grouped together.
🚧
Skip to:
How to Edit a Segment
How to Create a New Segment
How to Create a Disposable Segment
Step 2: When
4B. Combine Segments (Send To)
(If
Send to users in multiple segments and/or exclude users from these segments
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
to specify another one.
For example, in the above visual, we have selected,
Users in ALL of these segments.
This means that the campaign will be sent to only those users who are included within all three segments at any given point in time. Users who are a part of 2 or fewer segments will not receive the message.
🚧
Skip to:
How to Edit a Segment
How to Create a New Segment
How to Create a Disposable Segment
Step 2: When
4C. Exclude Segments
(If
Send to users in multiple segments and/or exclude users from these segments
is selected as
Audience Type
)
You can choose to exclude a segment or multiple segments from the target audience by configuring the field,
Don't Send To.
This is a great way to selectively engage users that match a specific persona. Here's how you can go about it:
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
reachable on Email
AND are not included within the specified segments.
Edit Segment
Click the
Edit icon,
placed towards the right of the dropdown to edit the selected
Segment.
In doing so, you will be prompted by a pop-up, pre-populated with the existing rules of segmentation, as shown below.
Click to enlarge
Simply make your edits and click
Save
to proceed. In doing so, you will able to preview the number of reachable users as per your edits.
For example, in the above visual we can see that the number of reachable users increased from 5,400 to 15,600 as we added more locations under the field,
Geo Filtering
.
Create a New Segment
You can create a new
Segment_of users by clicking the _Plus icon
placed towards the right of the dropdown. In doing so, you will be prompted by a pop-up, allowing you to build a new segment, as shown below.
Click to enlarge
Once created, you will be able to access the
Segment
through the
List of Segments
and while creating campaign/journey.
Create a New, Single-use Segment
You can create disposable segments or segment users specifically for the campaign and avoid adding it to the
List of Segments
in your dashboard.
Click to enlarge
As shown above, this can be achieved by leaving the field,
Name
blank while creating the segment. In doing so, it will become an
Ad hoc segment
in your dashboard which will be available only for sending the campaign you're currently creating.
🚧
Related Read: Rules of Segmentation
Please refer to
Creating Segments
for step-by-step guidance on how you can segment your users by their
attributes
, behavior (
events
), and technological preferences.
Removing Duplicates
For
One-Time
and
Recurring
campaigns,
Remove Duplicates
option will automatically ensure that a particular email address doesn't receive any
Email
campaign multiple times if your project has multiple users with the same email address.
Click to enlarge
If multiple users have the same email address (as shown in the example below), WebEngage will only pick one of these users while sending the campaign.
Click to enlarge
📘
Please Note
Remove Duplicates
option will be enabled by default for new campaigns created. However, you can disable it manually as per your campaign's requirement.
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
Click to enlarge
As highlighted above, the second step of campaign creation allows you to specify when and how often you'd like the
target audience
to receive the
Email
and manage the role your campaign plays in your overall engagement strategy. Hence,
When
has been divided into two sections:
Campaign Schedule
Frequency Capping & DND
Let's get you acquainted with the workings of each:
Campaign Schedule
Click to enlarge
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
one-time Email campaign
for delivery in your user's timezone!
(
How it works
)
🚧
Skip to
Frequency Capping & DND
to complete
Step 2: When
, of the campaign creation process.
Setting up Triggered Campaign
Step 1:
As shown below, select
Triggered
as the
Campaign Type
Click to enlarge
Step 2:
As shown above, select
the
Event upon the occurrence of which
the campaign will be triggered or sent to the user
For example, in the above visual we have selected the
custom event
Product - Added to Cart
as the trigger
event
📘
The following options can be selected here:
Custom
(all the
custom events
being tracked for your account)
System
(all the
campaign events
pre-defined by us for tracking user-channel interactions like app installed, Email delivered, Email opened and so on.)
Step 3 (Optional):
Add Attribute Filters to the Event
by clicking on the filter icon.
Click to enlarge
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
(Helps you narrow down the target audience)
OR:
Implies that users will receive the campaign if they perform the
Event
in the context of any one
event attribute
.
(Helps you widen the target audience)
Step 4:
Specify the
Delivery Time
of the triggered campaign
Click to enlarge
As shown in the above:
Select
Send as soon as the event occurs
to delivery the campaign immediately
Select
Wait for (duration) and then send
to deliver the campaign after sometime
You can set up a wait time in
Minutes, Hours or Weeks
, after which, the campaign will be sent to the respective users
Step 5:
Specify the
Start Date
or the date-time on which the triggered campaign should start getting delivered to the target audience
As highlighted in the visual below:
Select
Now
to send the campaign immediately
Select
Later
to schedule the campaign
Click to enlarge
Step 6:
Specify the
End Date
or the date-time on which the triggered campaign should cease getting delivered to the target audience
As highlighted in the visual above:
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
Frequency Capping & DND
to complete
Step 2: When
, of the campaign creation process.
Setting up Recurring Campaign
Click to enlarge
Step 1:
As shown above, select
Recurring
as the
Campaign Type
.
Step 2:
Specify the
Start Date
on which the recurring campaign should start getting delivered to the target audience.
Step 3:
Specify the
Delivery Schedule
or the frequency and date-time of campaign delivery.
As shown in the visual above, the frequency of a recurring campaign can be set as:
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
Click to enlarge
Step 4:
Specify the
End Date
or the date-time on which the campaign should cease getting delivered to the target audience
As highlighted in the visual above:
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
Frequency Capping, DND, Queuing & Throttling
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
Email campaign
in the context of your entire engagement experience.
Context:
Campaigns don't exist in isolation. Most marketing campaigns are designed for a specific audience, motivating them to perform a particular action. And more often than not, users receive multiple campaigns through various channels, nudging them towards a similar goal.
Thus, these features allow you to manage the frequency and timing of campaign delivery for each user.
Let's get you acquainted with the workings of each:
FC
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
This means that if the upper limit on the number of messages a user can receive within a day, week or month is exhausted, then this campaign will get queued for delayed delivery
(
detailed read on how this works
)
Select
Ignore...
to ensure campaign delivery even if the frequency cap for the day/week/month has been met for a user (
impact of disabling FC for a campaign
)
Set Frequency Capping Limits
Click to enlarge
If you have not set up Frequency Capping yet, then you can choose to configure it by clicking the
Configurations > Frequency Capping
on the left panel. Once set, you will be able to send all your campaigns with FC enabled, including the existing one.
Detailed read on
How to configure FC & Time Gap
.
DND
Using the
DND Settings
of your account, you can prevent users from receiving campaigns during specific periods such as when they may be asleep, and so on. The best part -
DND hours
are determined individually for each user. This means that
the duration specified by you will be applied to all your users only in the context of their time zone!
Click to enlarge
As highlighted above:
Select
Follow...
to ensure that users aren't disturbed by the _Email
at the hours specified by you (as per their timezone)_
Select
Ignore...
to ensure campaign delivery even if _DND hours
are applicable to a few users (
Disabling DND for a campaign
)_
Set DND Hours
If you haven't set up
DND Hours
yet, then you can choose to configure it by clicking on
Configuration > DND
on the left panel. Once set, you will be able to send all your campaigns with
DND hours
enabled, including the existing one.
Detailed Read on
How to configure DND Hours
.
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
Select
Do not Queue messages...
to drop the message if we're unable to deliver it to a user due to FC/DND settings (
Disabling Queueing for a campaign
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
The message creation interface comes loaded with intuitive features like
Variations
,
Drag & Drop Editor
,
Message, Image, Link Personalization
,
Raw HTML templating
,
Personalizing Email Attachments
and
User Preview
- enabling you to create high impact
Emails
in minutes.
Let's get you acquainted with each feature:
Select ESP
While the
Email campaign
is created and personalized through your dashboard, the actual message is delivered to by an
Email Service Provider (ESP).
We have partnered with several global
ESPs
to enable 2-click integration with your WebEngage account.
(
How to configure an ESP
)
Click to enlarge
As shown above, using the dropdown, you can choose to send the campaign through any of the ESPs that are currently integrated with your account.
🚧
Please Note
Depending on the
ESP
you’re using, you may need to configure your account separately sending
Transactional
and
Promotional Emails,
respectively. Thus, please be mindful of the fact that the
ESP
selected here has been set up to send the
(Email) Content Type
selected at
Step 1: Audience
.
A mismatch between the two may cause your campaign to fail.
Configure Sender-Receiver Details (From & Reply To)
Click to enlarge
As shown above:
Step 1:
Add the
Name
and
Email Address
from which you'd like your users to receive the email.
We recommend using a
Sender Name
that easily helps users identify the context like
Jake from Example.com.
Step 2 (optional):
Click the toggle switch to enable
Reply To
and specify the receiving email address.
Step 3 (optional):
If you're sending a campaign that requires multiple team members to monitor responses then we recommend that you configure
CC
and
BCC.
Click the toggle switch to enable respective fields and add the email addresses.
🚧
Important
You can now add your brand's logo to your campaign emails to build brand visibility, this can be done by a new standard known as BIMI stands for Brand Indicators for Message Identification.
Detailed read
here
.
Create Email Body
Depending on your communication needs, you can choose to create the Email's body in any of the following ways:
Create a
Rich Text Message
Build a Custom HTML Template
from Scratch with the Raw HTML Builder
Pick a Responsive Template from our Ready-to-use Library
& Customize It as per Your Needs
Let's walk you through all the steps and methods of message creation:
Step 1: Add Subject Line
Click to enlarge
You can personalize the
Subject Line
to each user by adding the relevant
User Attribute
or
Custom Event Attribute
as a placeholder to the text.
Step 2 (Optional): Customize Email Preheader
Email Preheaders are the text that appears next to the subject in the email inbox. This text is extracted from the first line of the email body. Senders can now customize email preheaders, instead of capturing the text present in the first line of the email body.
Preheaders are used to construct enticing or catchy sentences that persuade recipients to open the email.
How to customize Email Preheaders?
Create your email campaigns as usual, and proceed to the messages tab.
Step 1:
Below the ‘Subject’ option is where the ‘Preheader’ field is present.
Step 2:
You can add a preheader text to your email.
Step 3:
In case you want your preheader space to be completely blank, you can select the checkbox that says ‘Blank Preheader’. This will only show the sender's name and subject in the email inbox. This is generally done to increase focus on the subject without distracting them with other text.
The fields for ‘Preheader’ and ‘Blank Preheader’ are optional. In case, the email preheader fields are left blank, then the text present in the first line of the email body will be used automatically.
📘
Note
You can add Email Preheader for Raw HTML, Rich text, Drag & Drop Editor and AMP email.
Step 3: Add Message
Let's get you acquainted with each method:
Template Library
You can choose a template for your email, from the ‘
Template Library
’ button.
On clicking on it, you are introduced to a new tab that consists of various templates such as ‘Drag n Drop’ , ‘Custom HTML’ and ‘AMP’ if you have selected the AMP supported ESP templates or from your own saved templates.
You can filter the templates based on the filters on the left i.e. All, ‘Drag n Drop’, Custom HTML, and AMP
All: Displays all the types of templates
Drag n Drop - Displays the drag and drop templates.
Custom HTML - Pre-built custom HTML templates
AMP: Pre-built AMP HTML templates.
If any Drag n Drop template is selected, then the editor would open up with options that you can use to customize email as per your need.
If the Custom HTML or AMP template is chosen, then it would directly prefill the body field with the HTML code.
Method 1: Rich Text
Click to enlarge
🚧
Personalizing Links to Each User's Preference & Behavioral History
You can easily
personalize the URLs & deep links
embedded in your Emails to your users in any of the following ways:
Method 1:
Pass screen
link or pagel_url as a
custom event attribute
,
attached to a
custom event
gleaned for your app and website, respectively.
(
Step-by-step guide on how to execute this
)_
Method 2:
Build the URL or deep link by specifying a parent link and adding a
custom event attribute/
custom user attribute
as the path parameter
(
Step-by-step guide on how to execute this
)
Method 2: Raw HTML
You can easily write
Email Messages
using HTML editor. Just enter the message details in HTML format and you are good to go!
🚧
Personalizing Images to Each User's Preferences or Behavioral History
You can easily
personalize the images included in your Email template
to your users in any of the following ways:
Method 1:
Pass
image_url
as a
custom event attribute
, attached to a
custom event
gleaned for your app.
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
Method 3: Drag & Drop Editor
Click to enlarge
Select from the list of customizable templates to create your
Email
.
🚧
Related Read
A Step-by-step guide on using the
Drag & Drop Designer
to create responsive & dynamically personalized
Emails
Step 4: Insert Unsubscribe Link
🚧
Please Note
If you've created the message using the
Drag & Drop Editor,
then you can add the link through the editor itself.
(
how to add
)
The most important step of
Email
campaign creation - adding an unsubscribe link to your email plays a big role in ensuring that your domain is not blacklisted by the user's email provider and that it doesn't land up in the spam folder.
👍
Fact Check
Each time a user clicks on the auto-generated unsubscribe link, we track it as the performance indicator,
Unsubscribes
for all your
Email campaigns & Email
as a channel.
All unsubscribed users are automatically deemed unreachable through the channel, indicated through
Email Channel Reachability
across your dashboard.
Click to enlarge
As shown above, place the cursor where you'd like to add the unsubscribe link and click
'Insert Unsubscribe Link'
to add it.
In doing so, the hyperlinked text,
'Unsubscribe here'
will be added to the body copy.
You can easily replace the text with a custom message and use the auto-generated link to hyperlink it.
For example, in the above visual, we have added the link to a custom CTA -
Don't want to hear from us? Unsubscribe & break our heart :(
🚧
Please Note
Unsubscribing to your domain is a small two-step process designed by us and allows us to update your user's preferences across your dashboard in real-time.
Hence, please do not edit the auto-generated unsubscribe link for any of your email campaigns. Doing so will prevent users from exercising their right to stop receiving further communication from you. This can cause you to unknowingly spam users, leading to reduced domain authority, poor brand reputation and even blacklisting (in extreme cases).
Add Attachments
Click to enlarge
As shown above, you can choose to add multiple attachments to your campaign in any of the following ways:
1. Upload the document:
Click the
Upload button
placed next to the field and select a file from your desktop.
2. Insert a link to the document:
The attachment must be hosted on a publicly accessible domain or cloud service (like AWS) to ensure that it renders for all your users.
UTM Parameters
Start by enabling UTM at the global level through the Configurations section on the dashboard. This ensures that campaign-level UTM tagging is enabled by default. Click
here
to know how.
Modify or Edit UTM at Campaign Level
: While global UTM is setup, you can modify parameters for specific campaigns as well as per you needs.
Disabling Global UTM
: While disabling the UTM setup at global level you can choose whether to keep UTM for already running campaigns or remove it from all campaigns.
Note
: Campaigns which are already sent with UTM parameters cannot be removed.
Preview Email
The top panel of the message creation interface allows you to toggle between a
Raw Preview
and
User Preview
to gauge the email's appearance. Here's how it works:
Raw Preview
It helps you visualize the raw message and attributes, as added by you. For example, in the visual below, the personalization token for 'first name',
{{user['first_name']}},
has been rendered in the preview as it is.
Click to enlarge
User Preview
Allows you to view the
Email's body copy
for an actual user from your account by populating it with data from their user profile, as per the elements of personalization added to
Message
.
Click to enlarge
For example, in the visual above, we have visualized the
Email's
message for the
User ID, .
Here's how you can go about it:
Step 1:
Select
User Preview
from the top panel
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
button on the pop-up to visualize the Email with real user data
While this is a great way to gauge the overall look and feel of the
Email,
we recommend that you
test the campaign with an internal test segment
to ensure that it's good to go!
Create Variations
Click to enlarge
Variations
are just different versions of the campaign's message that facilitate easy multivariate testing and are referred to in the following manner in your dashboard:
Variation A:
The first version of the message.
Variation B:
The second version of the message.
Variation C, D, E:
Subsequent versions of the message created for testing.
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
can be created independent of the other, allowing you to test multiple aspects like its layout, body copy, buttons, links, and colors to identify a mix that resonates with your entire target audience.
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
Once you have sent the message, you will be able to see whether the message has been delivered or not. If not, the reason for delivery failure will be mentioned.
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
Email campaigns.
As shown below, you can use the toggle switch to enable it.
Step 1: Select a Conversion Event
The term,
Conversion Event
is an alias that helps you identify the event you expect users to perform after receiving the
Email.
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
In doing so, you will be prompted by a pop-up allowing you to select an attribute and specify its value
For example, in the above visual, we have filtered the
event, Checkout Completed,
by the attribute filter,
Primary Category
which is
one of, Women Dresses, Women Jeans, Women Tops & Tees
This implies:
Only those users who purchase products from one of the mentioned categories will be counted towards the campaign's conversion metrics.
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
For example, in the above visual, we have defined a deadline of
12 Hours
for the
Conversion Event, Checkout - Completed.
🚧
Related Read
List of all the
Conversion
metrics and
Performance Indicators
tracked for
Email campaigns
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
This option is shown when atleast one Custom Control Groups is created in your account.
Click here
for detailed read on creating custom control group.
Since this is a pre-created control group, overlapping users within this group and the target segment won't be receiving the campaigns.
Custom control groups are good for analyzing effectiveness of multiple campaigns. For example: Analyzing effectiveness of SMS and Email campaigns during Diwali sale.
Unlike Campaign level control group, the percentage of users to be part of control group cannot be controlled when Custom control group is selected.
Variation Distribution (Multivariate Testing)
If you have created multiple versions of the
Email
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
Depending on the campaign type selected at
Step 2: When
, the steps of setting up automated variation testing will vary.
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
As shown below, we have specified that a minimum of 1500 messages must be triggered to users to identify a winning version. This means that all the
Variations
will be equally divided amongst the specified number.
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
at
Step 2: When
, then the entire first run of the campaign will be considered as its
Test Audience
by default.
We will calculate the test results 1 hour before the second run of the campaign to identify a winning variation.
A winning
Variation
will be determined as per the
Win Criteria
and will be sent as the only campaign to all users from the second run. onwards.
Thus, as shown below, just need to define the
Win Criteria
as
Clicks
or
Conversions
and we will take care of the rest.
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
Email
campaign by testing it with internal team members for maximum impact!
While this is an optional step, we recommend that you test all campaigns that contain custom HTML layouts, images, buttons, links and elements of personalization to ensure that everything's in order. This can be easily done by
creating a
Test Segment
and adding all the stakeholders to it.
However, you can always choose to skip it by clicking the
Skip Test & Proceed
button, as highlighted above. Doing so will take you to the final step of campaign creation -
Step 6: Preview & Launch
.
Now, let's show you how you can test all the message
Variations
:
Step 5.1.: Select a Variation
Click to enlarge
As shown above, by default,
Variation A
is selected against the field -
Variation To Test.
However, if you have created
multiple
Variations
then you can test each one by sending them consecutively to a
Test Segment.
For example, in the visual above, we have chosen to test
Variation D
of our
Email campaign.
Step 5.2.: Select Test Segment
Click to enlarge
As shown above, all the test segments created while testing a campaign, for any channel
(Push, SMS, Web Push, Email, WhatsApp),
can be found under the dropdown,
Send Test Message To,
along with details of all its users.
🚧
Haven't created a test segment yet?
Step-by-step Guide to Creating Test Segment
Related Guides:
Editing
/
Deleting
Test Segment
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
Click to enlarge
Step 1:
Click the
Search User
button
In doing so, you will be prompted by a pop-up allowing you to search your user base
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
Step 3:
Click the
Search and Populate Values button
In doing so, you will be shown a summary of the values against the respective attributes and events included in the message. This is a good way to ensure that all the values are available for the user. If not, then you can enter an alternate
User ID
to personalize the message.
Click the
Save and Return to Test Campaign
button to proceed with the selected user
Step 4:
Click the
Send Test & Proceed button
to test the campaign.
Click to enlarge
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
🚧
Prerequisite for adding internal team members to a test segment
As you are aware, all the data stored in your WebEngage is either gleaned from your integrated apps and website or can be manually uploaded as a CSV file. Thus, it may so happen that details of internal teammates may not be readily available in your dashboard (even if they are account admins).
Hence, we recommend that you request the respective members to sign up on your platform so that we can populate their respective
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
Email template
on multiple devices (desktop, mobile, tablet), varying screen sizes and OS (Mac, Windows, Android, iOS) to ensure that it looks stunning all across!
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
Email
to your users! But before that, we recommend that you conduct a quick preview of the campaign's message and settings to ensure that it's in line with your end goal.
Click to enlarge
As shown above, the last step of campaign creation presents a snapshot of its:
Target Segment
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
Variations (
Step 3: Message
)
Conversion Tracking
and multivariate test settings
(
Step 4: Conversion Tracking
)
Edit Campaign Before Launch
You can always choose to edit a step by clicking the
Edit icon,
placed next to each step's header. In doing so, you will be directed back to the step, as shown below.
Click to enlarge
Simply make your edits, save them, toggle back to
Step 6: Preview & Launch
to continue your review, as shown above.
Saving Campaign as a Draft
If you're unsure or are awaiting approval of the campaign's contents, then you can simply go back to the
central hub of Email
after saving your settings. Doing so will automatically save the campaign as a
Draft
,
allowing you to edit or launch it anytime you like.
Launching Scheduled Campaigns
If you have chosen to
schedule/ start the campaign at a later date-time
, then on launching it, its status will indicate
Upcoming
in
Email, List of Campaigns
, as shown below.
Click to enlarge
What Happens After a Campaign is Launched?
Once launched, messages are sent to users included in the target audience as per the campaign's settings. Throughout it's run time, the campaign's status will indicate
Running
(in
Email, List of Campaigns
)
until it ends or is manually paused by you.
1. Analyzing Campaign's Performance
You can analyze each campaign's real-time impact on user engagement, conversions, and revenue by accessing its
Overview section
through the
List of Campaigns
of Email
.
2. Modifying the Campaign
Further, you can always choose to
Edit
and
Pause
an
Upcoming
or
Running
)
campaign if you feel the need to.
(
Step-by-step guide on modifying Email campaigns
)
3. Scheduling Campaign Reports
Once you have launched a campaign, you easily monitor its performance through scheduled reports, delivered straight to your (& your teammate's) inbox! This can be configured through the campaign's analysis section.
Here's how you can go about it.
Further, you can also schedule Channel-wise reports to monitor the overall performance of
Email
through the
Settings
section of your account.
Here's how you can go about it.
We hope this has equipped you with a robust understanding of how you can create various types of campaigns, track conversion, automate multivariate testing and test your campaign internally before launch. Please feel free to drop in a few lines at
[email protected]
in case you have any queries or feedback. We're always just an email away!
Updated
7 months ago
So, what's next?
Let's show you how you can analyze Email campaigns to measure their impact on user engagement, conversions, and revenue.
Analyzing Email Campaigns
Copy Page
