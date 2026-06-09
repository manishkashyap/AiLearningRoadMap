# Rich Communication Service Template Creation

- URL: https://knowledgebase.webengage.com/docs/template-creation
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Rich Communication Service Template Creation
Welcome to WebEngage's Guide to getting started with RCS Business Messaging
While you will be using WebEngage to create and analyze all your RCS campaigns, the message is delivered to your target audience through a
Rich Communication Service Provider (RSP).
🚧
Please Ensure That Your Website & Apps Are Integrated with WebEngage Before Proceeding
(Doing so will enable real-time personalization of all RCS messages sent to each user!)
Website
Android app
iOS app
React Native apps
Flutter apps
Cordova/ PhoneGap/ Ionic apps
Xamarin.Android app
Xamarin.iOS app
Unity.Android app
Unity.iOS app
Integration via Segment.com for Website, Android & iOS
Integration via GTM for Website, Android & iOS
Getting Started with RCS Marketing
Strict guidelines laid down for RCS marketing. Hence, you must follow these steps to ensure that you can use RCS uninterruptedly through WebEngage.
Step 1: Get Message Templates Whitelisted
📘
Message templates
are pre-approved messages that can contain a maximum of 4096 characters including elements of personalization, links, emojis, and
RCS
specific formatting. These messages can be used to initiate a conversation with opted-in users
(through campaigns)
To curb marketing spam, RCS has mandated whitelisting for each message that you'd like to send to your users. Promotional marketing is restricted, and the primary focus of this new channel is to provide customer support and contextual lifecycle updates. This means that early adopters can stand out - if you do it right!
Thus, we highly recommend that you restrict
RCS campaigns
to
conveying account updates, appointment updates, payment updates, personal finance updates, reservation updates, shipping updates and providing issue resolution.
Messages that contain any of the following elements are at a high risk of being disapproved:
Discounts, promotions, product recommendations or offers.
Surveys, product/service reviews, and rating requests.
Media files (videos & images).
You can submit message templates on your RSP dashboard for approval. Once they're approved,
upload these templates to your WebEngage dashboard
to create RCS campaigns.
Whitelisting Personalized Message Templates
Depending on your use-case, there may be several aspects that you'd like to personalize in the message. It could be anything like the
user's name, name of purchase product(s), order number, date of appointment, upcoming events
, and so on.
This can easily be achieved by:
Step 1:
Tracking these data points as
Custom User Attributes
,
Custom Events
, and
Custom Event Attributes
for all your app & web users.
Step 2:
Creating a placeholder in your message template for links, emojis, and personalization. Let's take the example of an order confirmation message that contains the following details:
User's First Name
Order Number
Order Tracking Link
An Emoji
Thus, while creating the message template, we'll replace each element with a placeholder in the format,
{{x}}
. Here's what the final template should look like:
👍
Whitelisting Order Confirmation Message
Hey
{{1}}
, thanks for your order!
We'll keep you posted on when it's ready to be shipped! You can track order number
{{2}}
, here
{{3}}
. Stay awesome
{{4}}
So, the message received by a user,
Jess,
will look like this👇:
👍
RCS Message Receive by User
Hey
Jess
, thanks for your order!
We'll keep you posted on when it's ready to be shipped! You can track order number
45360d
, here
www.example.com/order-tracking/45360d
. Stay awesome 🤙
Step 3: Collect User Opt-ins
By default, all users that have a valid phone number listed in their WebEngage
User Profile
are considered reachable via
RCS.
Please ensure that you capture the user's country code along with the phone number. If a country code doesn't exist, then
RCS
will try sending the message to a user by appending the country code of your business phone number.
Each time a user provides consent, you can track it as the
System User Attribute
,
we_rcs_opt_in
and set the status to
true
. Doing so will make the user reachable via RCS in your dashboard.
🚧
Setting RCS Opt-in Status for Users
Our platform integration SDKs enable you to set a user's opt-in status for
RCS, WhatsApp, SMS, and Email.
You can also choose to pass this data through a Rest API integration or manually upload it to your dashboard
Manual CSV Upload
Please Note:
_It's extremely important that you opt-in only those users who have explicitly provided consent.
You can also promote RCS subscription through contextual
Push
,
In-app
,
SMS
,
On-site Notifications
,
Web Push
, and
Email
campaigns
that convey the value proposition of connecting with you over the channel.
Rich Communication Service Provider (RSP)
You can think of
RCS Service Providers
as middlemen that transmit the message from your WebEngage account to a user's RCS account. Currently, you can leverage
Sinch
to engage users via RCS. We'll be adding more RSPs to the stack pretty soon!
RSP Integration
As highlighted below, access
RCS
through the
Data Platform> Integrations > RCS Setup (Configure)
menu on the left side of your dashboard. Click the
Add RCS Service Provider button
to get started.
Click to enlarge
🚧
RSP Setup
Please select a RSP from the left navigation panel (Channel Configurations > RCS) to continue configuration.
Uploading Whitelisted Templates
Click to enlarge
As shown above:
Step 1:
Click the
Add RCS Template
button to get started.
Step 2:
Select the RSP through which you've whitelisted the template or would like to send the campaign.
🚧
Please Note
Each template is mapped to a RSP in your dashboard. Thus, while creating the campaign, the list of templates will include only those messages that have been mapped to the RSP selected at
Step 3: Message
.
Step 3:
Add template details (may vary for each RSP):
Template Name-
Paste the exact name that has been approved.
RCS-
Choose the RCS integration.
Template Type-
Choose between Text, Rich Card, Rich Carousel
Text Template
Once you choose the
text template
, you are then presented with the following fields to fill to create a template.
Template text
: In this section you may start adding the text component of your text template. In this template format, you can add upto 11 buttons.
Rich Card Template
On choosing the
Rich Card Template
you will be able to add an image along with your content, where you can change the Orientation and Height of your image, after which you can proceed to adding your template details, and uploading the image of your choice, either by providing a link or uploading from your files. By choosing this template you will be able to add upto 4 buttons.
Rich Carousel Template
On choosing the
Rich Carousel Template
you will be able to add upto 10 images along with content for each of the carousel, in the media settings you can change the card width and media height of your image, after which you can proceed to adding your template details for each of the carousel, and uploading the image of your choice, either by providing a link or uploading from your files.
Note: You will be able to add upto 10 carousels in your template and upto 4 buttons.
You can view your saved templates on the RCS integration page under
RCS templates.
Once you've added the templates, your
Channels > RCS
section will look like this👇. You can choose to
Edit
and
Delete
a template anytime you through the
Actions
menu.
Click to enlarge
👍
Congratulations!
You're now ready to engage users via
RCS!
Managing Configuration
Click to enlarge
As shown above, integrated RSPs are listed under the section,
Your RCS Service Provider List.
You can choose to
Edit
or
Delete
the integration anytime you like by accessing the
Actions menu
placed on the extreme right.
The
Actions menu
also indicates the unique
Webhook URL
you can add to your
RSP dashboard
to ensure that
delivery status notifications (sent, failed, queued, delivered)
are tracked under campaign stats in your WebEngage dashboard.
Editing a RSP
You can choose to edit configuration details in cases where incorrect details were entered during configuration, or some details were updated at the RSP's end post-integration.
As shown below, select
Edit
from the
Actions menu,
make your changes, and click
Save.
Adding more authentication headers to configuration & updating it's name (click to enlarge)
Deleting a RSP
Deleting an integration will:
Cease campaign delivery for all
Running
and
Upcoming
campaigns where the respective RSP was selected for sending it.
Cause the deletion of all
RCS Templates
mapped to the specific RSP in your dashboard.
Thus, while doing so, please ensure that no existing campaigns are dependant on the RSP for sending RCS messages to your users.
As shown below, select
Delete
from the
Actions menu,
and click the
Delete button
in the pop-up to confirm your decision.
Click to enlarge
Please feel free to drop in a few lines at
[email protected]
in case you have any queries. We're always just an email away!
Updated
7 months ago
Analyzing RCS Campaign
FAQ
Copy Page
