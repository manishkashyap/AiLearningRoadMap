# Creating Transactional Email Campaigns

- URL: https://knowledgebase.webengage.com/docs/creating-transactional-email-campaigns
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Creating Transactional Email Campaigns
Step-by-step guide on setting up transactional campaigns in your dashboard
Transactional Emails
like
Password Reset, Order Confirmation, Payment Invoice
and
Shipping Notices
can achieve an 8 times higher
Open Rate
compared to regular marketing campaigns! This makes transactional emails the perfect way to subtly reinforce your brand's value proposition. So in addition to conveying information, you can contextually personalize the campaign to include coupons, cross-sell products/services/courses and even build referral loops by incentivizing their next purchase. This is why we bring to you -
Transactional Campaigns,
your one-stop solution to communicating critical messages instantly!
Simply launch your campaign and set up the
Transactional Campaign API
for the
Campaign ID
- we'll personalize the message and send it as soon as the API is triggered. You can sit back and watch the retention metrics go up :)
🚧
Must Read
Before you begin creating your campaign, we recommend that you get yourself acquainted with how
Transactional Campaigns
work in WebEngage. Doing so will help you better understand the steps of creation.
How to Access
As shown below, click the
Plus icon
placed on the top left in the
List of Campaigns
or the central hub of
Email.
In doing so, you will be prompted by a pop-up, allowing you to select the type of campaign you'd like to create.
Select
Transactional
to begin creating your campaign.
Click to enlarge
Now, let's walk you through all the steps of campaign creation.
🚧
Please ensure that you have integrated an
Email Service Provider (ESP)
with your account before proceeding as it enables message delivery to all your users.
Here's the integration guide
.
Step 1: Configure Basic Info
The first step is to give your campaign a unique name that helps you identify its purpose.
As shown below, you can click the
Edit icon
to alter the campaign type selected by you (in case you change your mind!)
Click to enlarge
Apply Universal Control Group
📘
Conditional Option
This is a conditional option which will be shown only if the you have created Universal control group in your account.
Click here
to know how to create Universal control group.
When the box is checked
, the campaign will not be sent to users who are part of the Universal Control Group in the segment that is selected.
When the box is unchecked
, the campaign will be sent to all users that are part of the segment inclusive of the
Universal Control Group
users.
Step 2: Create the Message
The message creation interface comes loaded with intuitive features like
Variations
,
Drag & Drop Email Editor
and
Personalized Preview
, enabling you to create impactful
Transactional Email Campaigns* in minutes.
Let's get you acquainted with each feature:
Create Variations
Variations
are just different versions of the campaign's message that facilitate multivariate testing and are referred to in the following manner in your dashboard:
Variation A:
The first version of the message.
Variation B:
The second version of the message.
Variation C, D, E:
Subsequent versions of the message created for testing.
Click to enlarge
As shown above, click on the
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
How to automate Variation testing
)
The percentage value indicates the share of users that will receive a
Variation
and can be customized at
Step 4: Conversion Tracking
.
👍
Pro Tip: Why You Must Always Test Multiple Variations of a Transactional Campaign
Most marketers like you and me would agree that A/B testing marketing campaigns is the best way to determine the exact message that resonates with the target audience. This inherently leads to higher platform engagement, conversions, and revenue.
But can A/B testing the way you
'confirm a purchase'
or
'convey a delivery update'
help you drive your business goals?
YES!
Why? Because most users expect to receive a transactional message each time they interact with your app/website/store or when certain scenarios occur in their lifecycle.
This makes
transactional campaigns
the perfect opportunity to:
build trust in your brand
Reinforce the value proposition of your brand in their lives
Motivate users to continue their association with you, aka. drive retention
Thus, we highly recommend that you create multiple
Variations
of your transactional campaign to test and identify a winning version that helps you achieve your business goals.
Select an ESP
While the
Email campaign
is created and personalized through your dashboard, the actual message is delivered to by an
Email Service Provider (ESP).
We have partnered with several global
ESPs
to enable 2-click integration with your WebEngage account.
(
How to configure an SSP
)
As shown below, use the dropdown to select an
ESP
through which you'd like to send the transactional campaign.
Click to enlarge
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
Personalize Message
🚧
Creating the Email Campaign's Body
You can choose to build the message in any of the following ways:
Method 1:
Create a
Rich Text
Message
Method 2:
Build a
Custom HTML
Template from scratch
Method 3:
Leverage ready-to-use templates with
Drag & Drop Editor
Irrespective of the method you choose, please follow the steps listed below to personalize the text, images, and links.
Transactional Campaigns
can be personalized only through the
personalization tokens that have been created in your backend
. Thus, each time the
Transactional Campaign API
is triggered for a user, your tech team will need to ensure that values of all the personalization tokens are passed along to your dashboard. This way we'll know which token needs to be replaced with which value, facilitating one-on-one personalization at scale.
Simply add your personalization tokens in the format,
{{token.your_personalization_token}}
and you're good to go!
Let's go over a short use-case to show you how it works:
👍
E-commerce: Shipping Notice (Out for Delivery Update)
Let's take the example of an e-commerce business. Each time a user makes a purchase, shipping updates are communicated through a series of
Emails
or
Push Notifications
(depending on their channel preferences).
In a bid to deliver personalized user experiences across the board, marketers of the platform decided to create a dynamically personalized
Shipping Notice Email.
They teamed up with their tech team to track the following details as personalization tokens for all their app and website users:
User's first name:
first_name
Auto-generated order ID:
order_id
Shipping Method selected at checkout:
shipping_method
Shipping Address specified at checkout:
shipping_address
Date of delivery:
del_date
Live status tracking link, auto-generated when order is placed:
del_track_link
Here's how they created the
Message:
Click to enlarge
As you can see above, we have added a
nunjucks code
along with the personalization token for displaying the delivery date in a specific format -
{{token.del_date | we_date(YYYY-MM-DD)}}
.
Hence, each time a shipment is out for delivery, users receive an
Email,
similar to the one shown below for
Andria:
Click to enlarge
Similarly, you can personalize your
Transactional Email Campaigns
to deliver highly contextual experiences each time.
Personalizing Links
You can easily personalize links (webpages, deep links, images) in any of the following ways:
Method 1:
Track the link as a personalization token
Method 2:
Build the link in your dashboard by adding the personalization token as the path
This method relies on creating a personalization token in your backend that captures the same value as the link's pathname. The idea is to replicate the link structure in your dashboard by adding the personalization token as the path.
(
detailed read
)
All you need to do is - replicate the above link structure in your dashboard. This can easily be done by tracking
User ID
as the personalization token,
user_id
.
Here's how you can go about it:
Step 1:
Add the parent link - *investapp://evaluation/
Step 2:
Add the personalization token,
user_id
as
{{token.user_id}}
to the link to replicate the pathname.
Thus, each time a user invests in a plan, they will be directed to their portfolio evaluation section through the personalized deep link -
investapp://evaluation/{{token.user_id}}
.
Preview Message
Click to enlarge
As highlighted above, the top panel of the message creation interface allows you to toggle between a
Raw Preview
and
User Preview
to gauge the email's appearance. Here's how it works:
Raw Preview
As shown below, it renders the
Email
with the raw
personalization tokens
added to the
Message
.
Personalized Preview
As shown below, it allows you to visualize the entire email template for an ideal user by replacing the
personalization tokens
with placeholder values. This is a great way to gauge the message's actual appearance and optimize it.
Here's how you can go about it:
Step 1:
Select
Personalized Preview
from the dropdown placed on the top left.
In doing so, you will be prompted to add values against all the
personalization tokens
added to the
Message
.
Step 2:
Add a sample of the actual value that may be tracked against each
personalization token
for an ideal user.
Step 3:
Click
See Preview
to visualize!
Step 3: Set up Conversion Tracking & Variation Testing
The third step of campaign creation allows you to measure the effectiveness of your transactional campaign in various ways like:
Tracking conversions for a specific goal
Comparing performance against a control group
Testing multiple variations of the message to identify the most effective copy/layout
Hence, it has been divided into two sections:
Conversion Tracking
and
Variation Distribution
.
Click to enlarge
Conversion Tracking
🚧
How to Set Up Conversion Tracking & Control Group
Hey there,
Please refer to this
Step-by-step guide
on setting up
Conversion Tracking
for your campaign. Since the setting works in the same manner for
Transactional Campaigns,
as it does for
One-time, Triggered, Recurring
campaigns, the guide will get you going in no time at all!
Variation Testing
If you have created multiple
Variations
at
Step 2: Message
,
then you can easily automate testing by configuring
Send Winning Variation Automatically
.
Doing so will allow you to test all the
Variations
(and
Control Group
if enabled) with a small test audience. We'll automatically identify a winner and send it to all the subsequent users for whom the
Transactional Campaign
is triggered.
Here's how you can set it up:
Step 1: Specify Size of the Test Audience
All
Transactional Campaigns
are triggered for a user on the occurrence of a specific scenario in their lifecycle. Thus, the most scientific method to test its
Variations
is by ensuring that a significant number of messages are delivered before we draw a comparison.
This is why, the
test audience
can be defined in terms of the number of messages that must be delivered to your users.
Click to enlarge
For example, in the above visual, we have specified a test audience of 500 messages. This means that all the
Variations
will be equally divided amongst the specified number and testing will continue until a total of 600 messages have been successfully delivered.
Step 2: Select Win Criteria
The
Win Criteria
is a performance indicator
(
Opens
,
Clicks
or
Conversions
)
that helps us determine a winning
Variation.
For example, in the above visual we have selected
Clicks
as the
Win Criteria.
This means that once 500 messages have been successfully delivered to the users, we will determine a winner based on the number of clicks tracked for each
Variation.
🚧
Prefer Manual Variation Testing?
Follow this guide
to test the
Variations
and
Control Group (if enabled)
manually.
Step 4: Test Your Campaign (Recommended)
Iron out all the creases in your Email by testing it with internal team members for maximum impact! While this is an optional step, we recommend that you test your
Transactional Campaign
to ensure that everything's in order. Here's how you can go about it:
Step 4.1: Select Variation
As shown below, by default,
Variation A
is selected against the field -
Variation To Test.
However, if you have created multiple
Variations
then you can test each one by sending them consecutively to a
Test Segment.
For example, we have chosen to test
Variation B.
Click to enlarge
Step 4.2: Select Test Segment
All the test segments created while testing a campaign for any channel
(Push, SMS, Web Push, Email),
can be found under the dropdown,
Send Test Message To.
Click to enlarge
As shown above, click the dropdown to select a relevant test segment and preview user details before proceeding.
🚧
Haven't created a test segment yet?
Step-by-step guide on creating a test segment
.
Related Guides:
Edit
/
Delete
test segment
Step 4.3: Enter Token Values
Click to enlarge
As shown above, you will find a list of all the
personalization tokens
added at
Step 2: Message
against the field,
Token Values
.
Add a sample of the actual value that may be tracked against each
personalization token
for an ideal user.
Next, launch the test campaign by clicking the
Send Test & Proceed
button.
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
👍
Pro Tip
If users included within the test segment don't receive the test campaign within a maximum duration of 10 minutes, then we suggest that you look into the following aspects to debug:
Did you use the correct personalization tokens (as created by your tech team)?
Has the ESP been integrated correctly with your WebEngage account?
Please feel free to drop in a few lines at
[email protected]
in case you need assistance. We're just an email away!
Step 5: Preview & Launch
Once you are satisfied with the test results, it's time to launch the
Transactional Email Campaign!
But before that, we recommend that you conduct a quick preview of its settings.
Click to enlarge
As shown above, the last step of the campaign creation interface presents a snapshot of its:
Sample API Call containing the
Personalization Tokens
added at
Step 2: Message
(copy code & edit to test with a service like
Postman
)
Variations with an OS-wise preview
(
Step 2: Message
)
Conversion Tracking and Multivariate Test settings
(
Step 3: Conversion Tracking
)
Edit Before Campaign Launch
You can always choose to edit a step by clicking the
Pencil icon,
placed next to each header. In doing so, you will be directed back to the step, as shown below.
As shown above, simply make your edits, save them and toggle back to
Step 5: Preview & Launch
to continue.
What Happens After the Campaign is Launched?
Once the transactional campaign is launched, no messages will be sent to your users until the
Transactional Messaging API
is called through your backend.
Each time the trigger event occurs in your backend, a POST call must be made through the API, sending details of the user for whom the event has occurred
(User ID & Email Address)
, along with the values gleaned for the personalization tokens added to the message.
The campaign's message will be personalized with the exact values gleaned for each user through the
Transactional Messaging API
WebEngage will then send the
Email
to the
ESP
integrated with your account for delivering it to the user.
🚧
Detailed Read
How
Transactional Campaigns
work in your dashboard
We hope this has equipped you with a robust understanding of how you can automate
Transactional Email Campaigns
for all your users. Please feel free to drop in a few lines at
[email protected]
in case you have any queries or feedback. We're always just an email away!
Updated
7 months ago
So, what's next?
Now let's show you how you can analyze the impact of your Email campaign!
Analyzing Email Campaigns
Copy Page
