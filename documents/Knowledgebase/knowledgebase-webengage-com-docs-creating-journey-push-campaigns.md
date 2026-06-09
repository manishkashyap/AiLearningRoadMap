# Creating Journey Push Campaigns

- URL: https://knowledgebase.webengage.com/docs/creating-journey-push-campaigns
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Creating Journey Push Campaigns
A step-by-step guide to engaging users with Push Notifications through a Journey
🚧
Please Note
This document is an extension of the
Journey Creation Guide
and only covers the aspect of
Push
campaign creation.
Here's a detailed read on how the
Send Push Block
works.
Getting Started
As shown below, using
Action Blocks
,
you can create points of engagement in your
Journey experience
to contextually engage users at various stages in their lifecycle.
Step 1:
Drag and drop the
Send Web Push Block
on the canvas.
Step 2:
Connect it to an existing block to determine the context in which users will receive the campaign.
Step 3:
Click on the block to create the campaign.
🚧
Please Note
Since
Journey Campaigns
are an extension of the
Journey experience,
the following settings cannot be configured for individual campaigns. You can configure these for the entire
Journey
and we'll automatically apply them to all attached campaigns:
Conversion Tracking
Control Group
Frequency Capping
DND Hours
Queueing Duration
Now let's walk you through all the steps of campaign creation.
Step 1: Configure Basic Info
The first step is to give your campaign a unique name that helps you identify its purpose.
Step 2: Create the Message
The most exciting part of campaign creation - building the message!
As highlighted above, the message creation interface comes loaded with intuitive features like
Variations, Layouts, Deep linking, User Preview Preview,
and
Advanced Settings
- enabling you to create high impact Push Notifications in minutes.
Personalize Message
In addition to leveraging all the
User Attributes
and
Events
being tracked for all the users in your dashboard, you can personalize
Journey campaigns
with:
Data gleaned through
GET
API call
Journey Events
or actions performed by users while experiencing the
Journey
Here's how you can go about it:
1. Personalize Message with Journey Events
2. Personalize Message with 'GET' API Data
🚧
Continue Building the Message
Now that you have a robust understanding of how you can personalize
Journey Push campaigns,
please navigate to the following sections to continue building the message:
Select a Layout
Create Variations
Basic (Text & Icon)
Configure Banner Layout
Configure Carousel Layout
Configure Ratings Layout
Advanced Options (Android)
Advanced Options (iOS)
Key-Value Pairs
(Personalization & Deep Linking)
Preview Notification
Step 3: Configure Variation Testing
If you have created multiple
Variations
at
Step 2: Message
,
then you can easily automate multivariate testing by
configuring *Send Winning Variation Automatically
.*
Alternatively, you can
configure
Variation Distribution
manually
if you'd like to specify a custom audience size for each
Variation
or are unwilling to test the campaign by sending a minimum of 500 messages to users who enter the block.
Let's walk you through each method:
Send Winning Variation Automatically
It allows you to test all the
Variations
with a small test audience and identify a winner based on their campaign interactions. We'll then automatically send the winning variant to all the subsequent users that enter the
Send Web Push Block
in the
Journey.
🚧
Must Read
Basic concepts of
Send Winning Variation Automatically
How
Send Winning Variation Automatically
enables intuitive multivariate testing
for your Journey campaigns
Here's how you can set it up:
Step 1: Specify Size of the Test Audience
Since
Journey Campaigns
are triggered for a user only when the enter the
Send Web Push Block,
the most scientific method to test its
Variations
is by ensuring that a significant number of messages are delivered before we compare the results.
This is why, the
test audience
can be defined in the number of messages that must be delivered to your users.
For example, in the above visual, we have specified a test audience of 700 messages. This means that all the
Variations
will be equally divided amongst the specified number and testing will continue until a total of 700 messages have been successfully delivered.
Step 2: Select Win Criteria
The
Win Criteria
is a performance indicator,
(
Clicks
or
Conversions
),
that helps us determine a winning
Variation.
For example, in the above visual we have selected
Clicks
as the
Win Criteria.
This means that once 700 messages have been successfully delivered to the users, we will determine a winner based on the number of clicks tracked for each
Variation.
Manual Variation Distribution
When Control Group is Added to Journey
If you have added a
Control Group
to the
Journey,
then as highlighted above, you will see two distribution meters.
The
first distribution meter
indicates the share of users that will be divided amongst:
Control Group
users that will simply pass through each block without any interactions
Users who will receive this
Journey campaign
when they enter the
Send Web Push Block
The
second distribution meter
indicates the share of users that will receive each
Variation
of this campaign when they enter the
Send Web Push Block.
As shown above, you can drag the meter to alter the share of users that will receive each
Variation
of the campaign and the share of users that will be included within the
Control Group.
Step 4: Test Campaign (Recommended)
Iron out all the creases in your
Push Notification
by testing it with internal team members for maximum impact!
While this is an optional step, we recommend that you test all campaigns that contain images, buttons, deep links and elements of personalization to ensure that everything's in order. As shown above, this can be achieved in 3 simple steps.
🚧
Continue Here...
A
step-by-step guide to testing
Push Campaigns
with your teammates
Related Guides:
Creating
/
Editing
/
Deleting
a Test Segment
What happens once you
Save
the campaign?
Once you
Save
a
Journey campaign,
you will be directed back to the
Journey creation interface
where you can continue building the experience, as shown below.
Users will start receiving the campaign only once the
Journey
is
Published
and they enter the
Send Push Block.
You can analyze the
Journey Push campaign's
impact across various performance indicators by accessing its
Campaign Overview
.
You can choose to edit the Message anytime you like by clicking on the respective
Send Push Block
in the
Journey's Live View
.
Updated
7 months ago
So, what's next?
How to create contextually relevant Journey experience by branching from the Send Push Block.
Branching Send Push Block
Copy Page
