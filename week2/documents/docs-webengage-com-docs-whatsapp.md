# WhatsApp

- URL: https://docs.webengage.com/docs/whatsapp
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
WhatsApp
A step-by-step guide to configuring WhatsApp as a marketing channel
While you will be using WebEngage to create and analyze all your WhatsApp campaigns, the message is delivered to your target audience through a
WhatsApp Service Provider (WSP).
👍
We recommend integrating your Website or App with WebEngage to send real time personalization messages to your users
Doing so will enable real-time personalization of all WhatsApp messages sent to each user!
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
Getting Started with WhatsApp Marketing
Strict guidelines laid down by Facebook control WhatsApp marketing. Hence, you must follow these steps to ensure that you can use WhatsApp uninterruptedly through WebEngage.
Step 1: Get WhatsApp Business Account Approved
The first step is to create a business account and submit it to Facebook for approval.
Here's how you can go about it
.
We recommend that you use a phone number exclusively for your
WhatsApp Business Account.
Here are a few guidelines to help you out:
The phone number must be owned by you, preferably registered to your business address, and must include a country code. It cannot be used for another WhatsApp account.
Phone numbers can easily be migrated from one WSP to another. However, once your business account is approved, the attached phone number cannot be changed.
You should be able to receive a call/SMS on the number for channel activation. Phone numbers that have an IVR service attached cannot be used unless IVR can be disabled to receive the activation code.
Step 2: Get Message Templates Whitelisted
📘
Message templates
are pre-approved messages that can contain a maximum of 4,096 characters including elements of
personalization
, links, emojis, and
WhatsApp
specific formatting. These messages can be used to initiate a conversation with opted-in users
(through campaigns)
and respond to user queries in the
Customer Service Window
.
To curb marketing spam, WhatsApp has mandated whitelisting for each message that you'd like to send to your users. Promotional marketing is restricted, and the primary focus of this new channel is to provide customer support and contextual lifecycle updates. This means that early adopters can stand out - if you do it right!
Thus, we highly recommend that you restrict
WhatsApp campaigns
to
conveying account updates, appointment updates, payment updates, personal finance updates, reservation updates, shipping updates and providing issue resolution.
Messages that contain any of the following elements are at a high risk of being disapproved:
Discounts, promotions, product recommendations or offers.
Surveys, product/service reviews, and rating requests.
Media files (videos & images).
You can submit message templates
directly to Facebook
or on your WSP dashboard for approval. Once they're approved,
upload these templates to your WebEngage dashboard
to create WhatsApp campaigns.
Whitelisting Personalized Message Templates
Depending on your use-case, there may be several aspects that you'd like to personalize in the message. It could be anything like the
user's name, name of purchase product(s), order number, date of appointment, upcoming events
, and so on.
📘
Keep in Mind
Header:
1 token + emojis allowed (with validation).
Body:
Multiple tokens + emojis supported.
Button URL (Dynamic)
: 1 token only. No emoji support.
Validation rules:
URLs must start with
https\://
and can include one token at the end.
Example:
https://www.webengage.com/{{token_1}}
Tokens must be numbered sequentially ({{1}}, {{2}}, …).
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
Thus, while creating the message template, we'll replace each element with a numbered placeholder in the format,
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
WhatsApp Message Receive by User
Hey
Jess
, thanks for your order!
We'll keep you posted on when it's ready to be shipped! You can track order number
45360d
, here
www.example.com/order-tracking/45360d
. Stay awesome 🤙
🚧
Please Note
As per
WhatsApp's guidelines
, a message template must include at least one parameter,
{{1}}
. It can later be replaced with text, numbers, special characters or a link, as per your needs.
Step 3: Collect User Opt-ins
By default, all users that have a valid phone number listed in their WebEngage
User Profile
are considered unreachable via
WhatsApp.
This is because
WhatsApp's Guidelines
require users to provide explicit consent for receiving messages.
Hence, we recommend that you create a WhatsApp opt-in form on your app/website or add a call-to-subscription to your purchase/platform discovery flow.
(
Detailed Read
)
Please ensure that you capture the user's country code along with the phone number. If a country code doesn't exist, then
WhatsApp
will try sending the message to a user by appending the country code of your business phone number.
Each time a user provides consent, you can track it as the
System User Attribute
,
we_whatsapp_opt_in
and set the status to
true
. Doing so will make the user reachable via WhatsApp in your dashboard.
(
Detailed Read
)
🚧
Setting WhatsApp Opt-in Status for Users
Our platform integration SDKs enable you to set a user's opt-in status for
WhatsApp, SMS, and Email.
You can also choose to pass this data through a Rest API integration or manually upload it to your dashboard.
Website Users
Android Users
iOS Users
Rest API
Manual CSV Upload
Please Note:
It's extremely important that you opt-in only those users who have explicitly provided consent. Violating Facebook's user opt-in policies may put you at the risk of having your WhatsApp business account suspended.
You can also promote WhatsApp subscription through contextual
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
WhatApp Service Provider (WSP)
You can think of
WhatsApp Service Providers
as middlemen that transmit the message from your WebEngage account to a user's WhatsApp account. Currently, you can leverage
Infobip
,
Gupshup
,
Kaleyra
, and
ValueFirst
to engage users via WhatsApp. We'll be adding more WSPs to the stack pretty soon!
Click to enlarge
WSP Integration
As highlighted below, access
WhatsApp
through the
Data Platform> Integrations > Whatsapp Setup (Configure)
menu on the left side of your dashboard. Click the
Add WhatsApp Service Provider button
to get started.
Click to enlarge
🚧
WSP Setup
Please select a WSP from the left navigation panel (Channel Configurations > WhatsApp) to continue configuration.
Template Creation
Once you’re on the WhatsApp Integrations page of your WE dashboard, you can proceed with creating your template by clicking on the ➕ icon, which opens the ‘Create Modal’ tab.
Continue to fill in the following details to proceed in creating your template. There are
2 methods
of creating templates for your WhatsApp campaigns:
Add Templates
: Upload an already whitelisted template from the WSP dashboard (traditional method)
Create Templates
: Create and submit templates for approval directly from WebEngage. (currently supported only for Infobip WSP).
Creating Templates for Automated Approval
❗️
Currently only Infobip WSP supports auto- approval
Once you've been presented with the template creation modal, proceed to filling in the template details.
Template name
: Give your template a relevant template name.
Creation Process
: Currently
only Infobip WSP supports auto- approval
, hence by using the same you will have an option to either
Add template
or
Create Template
; but since you're going to be creating a template, you can proceed by clicking on the '
Create Template
' option.
WSP
: Select a WSP from the dropdown that supports auto approval, i.e. as of now
WebEngage only offers this for our
Infobip
WSP.
Category
: Choose your template category between Marketing and Utility. For more information on this refer to this
document
.
Template type
: Choose from all the current templates that are provided by WebEngage i.e. text, image, video, document, carousel, location.
Header, Text and Footer
: Enter the header, text and footer for your template.
Template Namespace
: An option exclusive for Infobip WSP
Template Language
: Choose a language for your template.
Buttons
: You can add upto a total of 10 buttons. WE provides 2 types of buttons- CTA and Quick reply buttons.
CTA Buttons include:
Visit website
: You can add up to 2 website buttons with static or dynamic URLs.
Copy offer code
: An autofill button text.
Call Phone Number
: You can add up to 1 phone number button with a specific phone number format.
Once that’s done and click on
Save
.
Note
: For a template that was created on the WE dashboard, you can await the approval from META, after which it can be used in your campaigns.
Uploading Whitelisted Templates
Click to enlarge
As shown above:
Step 1:
Click the
Add WhatsApp Template
button to get started.
Step 2:
Select the WSP through which you've whitelisted the template/ would like to send the campaign.
🚧
Please Note
Each template is mapped to a WSP in your dashboard. Thus, while creating the campaign, the list of templates will include only those messages that have been mapped to the WSP selected at
Step 3: Message
.
Step 3:
Add template details (may vary for each WSP):
Template Name
(Paste the exact name that has been approved).
Template Text
(Paste the exact message that has been approved, do no edit).
Template Namespace
(While copying from your Facebook/WSP dashboard, please ensure that you use the format,
<template_namespace>:<template_name>
, for namespace)
Template Language
(
List of languages
supported by WhatsApp).
Please get in touch with your
WSP Account Manager
or
Facebook business support
if you're unable to find these details.
Once you've added the templates, your
Channels > WhatsApp
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
WhatsApp!
Button Capabilities
WhatsApp allows the addition of up to 10 buttons in a message, with specific limits on each type of call-to-action (CTA) button, such as phone numbers and URLs. Any extra buttons can be set as quick reply buttons.
When combining quick reply and CTA buttons, they must be grouped separately. Here’s how you can organize them:
Call to Action URLs: You can add up to 2, either dynamic or static.
Call Phone Number: You can add only 1 button for dialling.
Copy Offer Code: You can add only 1 button type that copies a coupon code when clicked. Note that the text for the 'Copy offer code' button cannot be edited or updated.
Quick Reply Button: Up to 10 can be added in a template.
Note
: If CTA buttons are added, the maximum limit of quick reply buttons is reduced. For example, if 2 CTA buttons are added, the maximum number of quick reply buttons is 8 (10 - 2).
To utilize the new WhatsApp button features, go to the integrations page and navigate to WhatsApp. Once there, click on ‘configure’
Carousel Template
This template allows you to display your products using images and videos. To set up a WhatsApp carousel template via the data platform's integrations page, follow these steps:
📘
Keep In Mind
Capability to add up to 10 buttons and
Carousel
template type is currently only available for Infobip, for other self serve please get in touch with your service provider or support team.
Access WhatsApp integration and click 'Create Template'.
Select 'Carousel' and fill in the required details:
Template Name
Template Text
Template Namespace (only for Infobip users)
Template Language
Media Type (applicable to all cards; choose either Image or Video)
Number of carousel cards (a minimum of 2 and up to 10 cards)
For each carousel card, specify the following:
Media: Images or videos
Caption
Up to 2 buttons: At least one button is mandatory, with options including Quick Reply, Phone Number, or URLs.
Note
: Footers are not supported for this template.
📘
Note
The Carousel template for Infobip is supported only on cloud senders. Using it on non-cloud senders may result in message rejection. Please contact your Infobip account manager to ensure your account is on a cloud sender to use the updated features swiftly.
Template Approval Status
You can track the approval status of your templates under the "WhatsApp Templates" section. Keep in mind that statuses that are blank indicates that the WSP does not support automated approval. The statuses that will be visible in this section include:
Blank
: Indicates WSP does not support auto-approval.
Approved
: Templates approved by Meta, ready for campaign use.
In-Review
: Templates under review.
Rejected
: Templates that did not pass Meta's review.
Paused
: Templates paused due to negative feedback or low read rates.
Disabled
: Templates disabled due to consistent negative feedback.
Filters
: Templates can be filtered by status.
🚧
Keep in Mind
Note must be taken that only templates that have been approved can be used in creation of campaigns.
Managing Configuration
Click to enlarge
As shown above, integrated WSPs are listed under the section,
Your WhatsApp Service Provider List.
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
WSP dashboard
to ensure that
delivery status notifications (
sent, failed, queued, delivered
)
are tracked under campaign stats in your WebEngage dashboard.
Editing a WSP
You can choose to edit configuration details in cases where incorrect details were entered during configuration, or some details were updated at the WSP's end post-integration.
As shown below, select
Edit
from the
Actions menu,
make your changes, and click
Save.
Adding more authentication headers to configuration & updating it's name (click to enlarge)
Deleting a WSP
Deleting an integration will:
Cease campaign delivery for all
Running
and
Upcoming
campaigns where the respective WSP was selected for sending it.
Cause the deletion of all
WhatsApp Templates
mapped to the specific WSP in your dashboard.
Thus, while doing so, please ensure that no existing campaigns are dependant on the WSP for sending WhatsApp messages to your users.
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
SMTP
Infobip
Copy Page
