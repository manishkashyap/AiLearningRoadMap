# Creating Transactional WhatsApp Campaigns

- URL: https://knowledgebase.webengage.com/docs/creating-transactional-whatsapp-campaigns
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Creating Transactional WhatsApp Campaigns
Step-by-step guide on setting up transactional campaigns in your dashboard
📘
Please Note
Before you begin creating your campaign, we recommend that you get yourself acquainted with how
Transactional Campaigns
work in WebEngage. Doing so will help you better understand the steps of campaign creation.
👍
Pre-requisites For WhatsApp Message
Before you set out to create and send WhatsApp messages, kindly make sure you have your WhatsApp Service Provider (WSP) setup and add the Whitelisted Message Template.
To know how to set up WSP and add templates, kindly refer to the
WhatsApp Integration guide
.
WhatsApp is one of the most preferred channels globally. And the WhatsApp Business API, opens up a reliable and direct channel of communication between brands and their customers. So, irrespective of the product/service you're marketing, WhatsApp messages have the potential to drastically amplify your user experience. This is why we bring to you -
Transactional Campaigns,
your one-stop solution to communicating critical messages instantly!
Simply launch your campaign and set up the
Transactional Campaign API
for the
Campaign ID
- we'll personalize the message and send it as soon as the API is triggered. You can sit back and watch the retention metrics go up :)
Campaign Creation
As shown below, click the
Plus icon
placed on the top left in the
List of Campaigns
or the central hub of
WhatsApp.
In doing so, you will be prompted by a pop-up, allowing you to select the type of campaign you'd like to create.
Select
Transactional
to begin creating your campaign.
Click to enlarge
Basic Info
This is where you set the basic details for your campaigns like campaign name, campaign tags, and campaign type.
The first step is to give your campaign a unique name that helps you identify its purpose.
Campaign Tags
is a handy feature that helps you categorize your campaigns as per their purpose, target audience, frequency, or any other parameter that makes them easier to search for.
Edit Campaign Type by clicking the
Edit icon
(in case you change your mind!)
Click to enlarge
Apply Universal Control Group
📘
Conditional Option
This is a conditional option which will be shown only if the you have created Universal control group in your account.
Click here
to know how to create Universal control group.
When the box is checked
(as shown in the gif above), the campaign will not be sent to users who are part of the Universal Control Group in the segment that is selected.
When the box is unchecked
, the campaign will be sent to all users that are part of the segment inclusive of the
Universal Control Group
users.
Message
The message creation interface comes loaded with intuitive features like
Variations
and
Personalized Preview
, enabling you to create impactful
Transactional WhatsApp Campaigns
in minutes.
Click to enlarge
Here's how it works:
Template Name
Click to enlarge
Template Text
Transactional Campaigns
can be personalized only through the
personalization tokens
that have been created in your backend. Thus, each time the
Transactional Campaign API
is triggered for a user, your tech team will need to ensure that values of all the personalization tokens are passed along to your dashboard. This way we'll know which token needs to be replaced with which value, facilitating one-on-one personalization at scale.
Simply add your personalization tokens in the format,
{{token.your_personalization_token}}
and you're good to go!
👍
Grocery Ordering App: Shipping Confirmation Message
Let's take the example of a grocery shopping app that sends a WhatsApp message to the user whenever the user's order has been shipped.
The message conveys several details like user name, order id, and how much money they saved on their order.
Thus, marketers of the app collaborated with their tech team to track these details as the following personalization tokens:
User's first name:
first_name
Order id:
order_id
Total amount saved:
value_saved
The message template thus created is:
*Hi {{token.first_name}},
Your order ID - {{token.order_id}} has been shipped! And it's a wonderful feeling to know that we helped you save ${{token.value_saved}} on your groceries.*
Personalizing Links
🚧
Tracking Clicks for WhatsApp Campaigns
Each time a user clicks on a link included with the message, it's tracked as the performance indicators:
Total Clicks
and
Unique Clicks
under the
Campaign's Overview
section.
How?
Whenever you add a link against a personalization variable while creating the message, we automatically append it to a WebEngage domain (weurl.co) while sending the campaign. This allows us to track users who click on it.
Hence, if you have not added a link, then no
Clicks
will be tracked for your WhatsApp campaign.
As demonstrated in the use-case discussed above, you can easily personalize app deep links and web links in any of the following ways:
Method 1:
Track the link as a personalization token (discussed above).
Method 2:
Build the link in your dashboard by adding the personalization token as the path.
The second method relies on creating a personalization token in your backend that captures the same value as the link's pathname. The idea is to replicate the link structure in your dashboard by adding the personalization token as the path (
detailed read
).
Create Variations
Variations are just different versions of the campaign's message that facilitate easy multivariate testing and are referred to in the following manner in your dashboard:
Variation A
(the first version of the message),
Variation B
(second version of the message), and so on for subsequent versions.
Click to enlarge
As shown above, by default, the message creation interface consists of a single Variation A. You can create up to 5 variations of the message by clicking on the Plus icon.
Select
Create New
to start building the new Variation from scratch.
Select
Copy from Variation A
(or any of the previous versions) to make minor edits to the new Variation.
Each Variation can be created independent of the other, allowing you to test varying messages and links to identify what works best with your target audience.
The percentage values indicate the share of users that will receive a Variation and can be customized during Conversion Tracking.
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
Preview Message
Click to enlarge
As shown above, the left half of the campaign creation interface provides a real-time preview of the
WhatsApp
being created by you. At any given point, you can toggle between
Raw Preview
and
Personalized Preview
to gauge the message's appearance.
Raw Preview
As the name suggests, it renders the message with the raw
personalization tokens
added while creating the message.
Personalized Preview
The personalized preview allows you to visualize the message for an ideal user by replacing the
personalization tokens
with placeholder values. This is a great way to gauge the message's actual appearance and optimize it.
Here's how you can go about it:
Step 1:
Select
Personalized Preview
from the dropdown placed on the top left. In doing so, you will be prompted to add values against all the
personalization tokens
added to the message.
Step 2:
Add a sample of the actual value that may be tracked against each
personalization token
for an ideal user.
Step 3:
Click
See Preview
to visualize!
Conversion Tracking
Conversion tracking allows you to measure the effectiveness of your transactional campaign in various ways like:
Tracking conversions for a specific goal
Comparing performance against a control group
Testing multiple variations of the message to identify the most effective copy/layout
Hence, it has been divided into two sections:
Conversion Tracking
Variation Distribution
Click to enlarge
Conversion Tracking
🚧
How to Set Up Conversion Tracking & Control Group
Kindly refer to this
Step-by-step guide
on setting up
Conversion Tracking
for your campaign.
Since the setting works in the same manner for
Transactional Campaigns,
as it does for other campaign types, the guide will get you going in no time at all!
Variation Testing
If you have created multiple variations while creating the campaign then you can easily automate testing by configuring
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
Size of the Test Audience
All
Transactional Campaigns
are triggered for a user on the occurrence of a specific scenario in their lifecycle. Thus, the best method to test its
Variations
is by ensuring that a significant number of messages are delivered before we draw a comparison.
This is why the
Test Audience
can be defined in terms of the number of messages that must be delivered to your users.
Click to enlarge
For example, in the above visual, we have specified a test audience of 2000 messages. This means that all the
Variations
will be equally divided amongst the specified number, and testing will continue until a total of 2000 messages have been successfully delivered.
Win Criteria
The
Win Criteria
is a performance indicator
Clicks
or
Conversions
that helps us determine a winning
Variation.
For example, in the above visual, we have selected
Clicks
as the
Win Criteria.
This means that once 2000 messages have been successfully delivered to the users, we will determine a winner based on the number of clicks tracked for each
Variation.
🚧
Prefer Manual Variation Testing?
Follow this guide
to test the
Variations
and
Control Group (if enabled)
manually.
Test Campaign (Recommended)
Iron out all the creases in your message by testing it with internal team members for maximum impact! While this is an optional step, we recommend that you test your
Transactional Campaign
to ensure that everything's in order.
Click to enlarge
Variation To Test
As shown below, by default,
Variation A
is selected against the field -
Variation To Test.
However, if you have created multiple
Variations
then you can test each one by sending them consecutively to a
Test Segment.
Send Test Message To
All the test segments created while testing a campaign for any channel
(Push, SMS, Web Push, Email, WhatsApp),
can be found under the dropdown,
Send Test Message To.
As shown above, click the dropdown to select a relevant test segment and preview user details before proceeding.
🚧
Haven't created a test segment yet?
Step-by-step guide
on creating a test segment.
Related Guides:
Editing
/
Deleting
a test segment
Token Values
Click to enlarge
As shown above, you will find a list of all the
personalization tokens
added while creating the campaign against the field,
Token Values
. Add a sample of the actual value that may be tracked against each
personalization token
for an ideal user. Launch the test campaign by clicking the
Send Test & Proceed
button.
Preview & Launch
Once you are satisfied with the test results, it's time to launch the
Transactional WhatsApp Campaign!
But before that, we recommend that you conduct a quick preview of its settings.
Click to enlarge
As shown above, the last step of the campaign creation interface presents a snapshot of its:
Sample API Call containing the
Personalization Tokens
added at creating the campaign (copy code & edit to test with a service like
Postman
)
Variations with an OS-wise preview
Conversion Tracking and Multivariate Test settings
Edit Before Campaign Launch
You can always choose to edit a step by clicking the
Pencil icon,
placed next to each header. In doing so, you will be directed back to the step, as shown below.
Click to enlarge
As shown above, simply make your edits, save them and toggle back to
Preview & Launch
to continue.
We hope this has equipped you with a robust understanding of how you can create
WhatsApp Transactional Campaigns
for various campaigns, track conversion, automate multivariate testing and test your campaign internally before launch. Please feel free to drop in a few lines at
[email protected]
if you have any related queries or feedback. We're always just an email away!
Updated
7 months ago
Creating WhatsApp Campaigns
Accessing and Understanding WhatsApp Campaigns
Copy Page
