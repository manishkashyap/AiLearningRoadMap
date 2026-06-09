# Configuring 2-step Opt-in

- URL: https://docs.webengage.com/docs/web-push-enabling-2-step-opt-in
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
Web Push
Configuring 2-step Opt-in
A step-by-step guide to setting up Web Push opt-in (Recommended for HTTP domains)
🚧
Please Note
This document is an extension of
Web Push
channel configuration. Please ensure the following before proceeding:
Your Website is Integrated with WebEngage
Web Push is Enabled in your Dashboard
Once you've set up 2-step Web Push opt-in, your users' subscription experience will be similar to the visual below:
2-step Web Push opt-in
Let's get you started!
Click to enlarge
As shown above, here are a few mandatory steps to enable 2-step opt-in for your users:
Step 1: Add Sub-Domain Name
When you switch the
Web Push
toggle on, you will notice that 2-step opt-in is selected by default with a pre-filled
Sub-Domain,
based on your project's name in WebEngage. It can be changed to any sub-domain name you like.
Step 2: Upload Icon & Badge
(Badge is applicable only to Chrome v56+ x Android v6+)
Step 1:
Upload your site icon. It'll be shown in all your
Web Push Notifications
by default.
You can always choose to add a dynamically personalized icon while creating the campaign.
(
Step-by-step guide
)
Step2:
Upload custom site badge to replace Chrome's logo in
Web Push Notifications
that are delivered to
Chrome x Android users.
Or you could
add it while creating the Web Push campaign
.
A few guidelines for uploading the badge:
The badge must be monochrome as the OS-browser does not support RGB colors.
We recommend a width:height ratio of 1:1 with the ideal image size being 72px by 72px.
Please upload the image in .png, .gif, .webp, .ico, .cur, .bmp formats only, in a file size not exceeding 1MB.
🚧
Congratulations!
Web Push Opt-in
has been set up for your account! You can now
start creating
Web Push campaigns
for all your subscribers.
OR
Continue setting up optional configurations
Step 3 (Optional): Configure What to Show
By default, the
WebEngage On-site Notification
that initiates
Web Push opt-in
for a user is shown on the bottom left of their screen as a bell prompt. You can choose to configure its message, position, and look and feel through this section.
Here's how you can go about it:
Click to enlarge
Step 1:
Customize the
notification position
by selecting an option from the field,
Position.
Step 2:
Add a
custom message
for the prompt in the field,
Message.
Step 3:
Change the
Allow Button Text
to something more warm and friendly.
Step 4:
Change the
Don't Allow Button Text
to something less dismissive.
Step 5:
Customize the
prompt's background and text
as per your brand guidelines through the fields,
Background Color
, and
Text Color
, respectively.
Step 6 (Important):
Determine what happens if a user clicks the
Don't Allow Button.
(By default, we will continue to them the opt-in prompt each time they visit your website or specified webpage/s.)
📘
The following options can be selected here:
Never show opt-in prompt again
Show opt-in prompt in a new session
Show opt-in prompt after a time delay of
<enter duration in minutes>
Continue to show opt-in prompt
Step 4 (Optional): Define When & Where to Show
By default, the
Onsite Notification prompt
is shown to all users as soon as they start their session on any webpage. It's shown each time an unsubscribed user re-visits your site.
Using this section, you can modify the default settings by specifying:
The type of users that must be engaged with the prompt.
(
How it works
)
The page(s) on which it must be displayed
(Where). (
How it works
)
The context
(When)
in which a user must be shown the opt-in prompt.
(
How it works
)
Here's how you can configure it:
Step 4.1: Define Whom To 'Show To'
Click to enlarge
By default, the
Web Push opt-in prompt
is shown to all your users. However, you can choose to narrow down the target audience by specifying a segment that you'd like to target with the prompts.
As shown above, you can select a segment from the dropdown.
This setting can be changed anytime you like and will not affect the existing list of subscribers.
🚧
Haven't Created a Segment Yet?
Let's get you started!
Step 4.2: Define Where To 'Show On'
Click to enlarge
Select
All Pages
to show the opt-in prompt as soon as a user lands on a webpage
Select
Specific Page
to selectively curate only those users as subscribers who visit certain pages of your website
(
How to define
)
Select
Event Occurrence
to selectively curate only those users as subscribers who perform certain actions on your website
(
How to define
)
Show on Specific Page
Selecting this option enables you to show the
Web Push opt-in prompt
only on select pages of your site like
product review pages, order tracking pages, recommendation pages
and so on.
Click to enlarge
Step 1: Add Page URL
Step 2: Combine Multiple URLs with AND/OR Logic
Click the
Add Rule Button
to specify multiple pages and combine the URLs by the AND/OR Logic.
🚧
How It Works: Combining Page URLs by AND/OR Logic
AND:
Implies that only those users will be shown the Web Push opt-in prompt who have visited all the defined URLs
(helping you narrow down the target audience).
OR:
Implies that all users who visit either of the defined URLs will be shown the Web Push opt-in prompt
(helping you widen the target audience).
Show on Occurrence of Event
🚧
Must Read
Please ensure that you have a robust understanding of
Events and Event Attributes
before proceeding. Doing so will help you understand this section, better.
Selecting this option enables you to show the opt-in prompt whenever an event happens eg. whenever the user purchases something when he is likely to subscribe to your notifications given that a successful transaction has taken place.
Click to enlarge
Step 1: Select Event
As shown above, click the dropdown to select from a list of all the
Custom Events
and
System Events
being tracked for your dashboard.
Step 2: Define Scope of Occurrence by Adding Event Attribute Filters
You can further define the scope of occurrence of the
Event
by adding
Event Attribute filters
to it.
Click the filter icon to select
Event Attributes.
Multiple
Event Attributes
can be combined by the
AND/OR Logic
.
🚧
How It Works: Combining Event Attribute Filters by AND/OR Logic
AND:
Implies that the
Web Push opt-in prompt
will be shown only to those users who perform the
Event
in the context of all the
Event Attributes. (Helps you narrow down the target audience)
OR:
Implies that the
Web Push opt-in prompt
will be shown to all users who perform the
Event
in the context of any one of the
Event Attributes. (Helps you widen the target audience)
Step 3: Click Add Event to Specify More Events
Step 4.3: Configure Delay Time, Scroll % & Max. Display Limit
(Not applicable if
Event Occurrence
is selected at
Step 4.2: Where to 'Shown On'
)
Click to enlarge
Add Time Delay:
You can choose to delay the appearance of the opt-in prompt by a few seconds after a user lands on a webpage. As highlighted above, specify the duration and you're good to go!
Define Scroll %:
You can choose to contextually show the Web Push opt-in prompt to users only if they've scrolled through a certain percentage of your webpage.
This is a great way to capitalize on user intent and show the opt-in prompt to only high-intent users (as they've expressed interest by scrolling down to a specific section of the webpage).
As highlighted above, specify the percentage and you're good to go!
Define 'Maximum Times' Message Can Be Shown:
Nudging a user to opt-in until they half-heartedly give in, or abandon your website completely is not the best strategy. This is why you can set an upper cap on the number of times a user can be shown the prompt in a session.
As highlighted above, specify the upper cap and you're all set!
Step 5 (Optional): Configure Native Browser Prompt
Once a user clicks the
Allow Button
on the
WebEngage On-site Notification,
they are asked to confirm their subscription through a
Native Browser Prompt
that's shown in a new window.
Click to enlarge
As shown above, you can choose to copy the message that is shown in the
WebEngage On-site Notification prompt,
here. Or you could craft a brand new one. Here's how you can customize it:
Step 1:
Add your
Message.
Step 2:
Upload an
Icon
(warm, friendly and welcoming image recommended!)
Step 3:
Customize the background and text color as per your brand guidelines through the fields,
Background Color
, and
Text Color
, respectively.
Step 6 (Optional): Configure Acknowledgement
By default, no subscription acknowledgment is sent to users once they've opted-in to your channel. Using this section, you can set up a custom notification to welcome users to your subscribers' community. Here's how you can go about it:
Click to enlarge
Step 1:
Click the toggle switch to enable the acknowledgment notification.
Step 2:
Customize the
Title
and
Message
as per your engagement strategy.
Step 3:
Upload a custom icon (warm, friendly, and welcoming image recommended!)
📘
Please Note
Web Push does not work in
Incognito Mode, Private Browsing Mode, and Guest Browser Mode
. However, while browsing your website in incognito mode, you might see the
Notification Prompt
appear because of technical constraints imposed by browsers that don't allow the detection of incognito mode. Kindly make sure you are not in incognito mode while testing any
Web Push Campaign
.
Congratulations! You're all set to use
Web Push
as a channel of engagement in WebEngage. Please feel free to drop in a few lines at
[email protected]
in case you have any queries or feedback. We're always just an email away :)
Updated
7 months ago
So, what's next?
Let's help you launch your first Web Push Campaign!
Getting Started with Web Push Notifications
Copy Page
