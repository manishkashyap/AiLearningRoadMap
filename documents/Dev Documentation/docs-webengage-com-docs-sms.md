# SMS

- URL: https://docs.webengage.com/docs/sms
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
SMS
While you will be using
WebEngage
to create all your
SMS campaigns,
the actual delivery of the message to your target audience is facilitated by an
SMS Service Provider (SSP)
like
Twilio
,
Exotel
,
Plivo
,
mGage
and so on.
👍
We recommend integrating your Website or App with WebEngage to send real time personalization messages to your users
(Doing so will enable real-time personalization of messages sent to each user!)
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
SMS Marketing Concepts
Let’s quickly walk you through a few related concepts:
Transactional SMS
Messages that convey updates or information related to the
user's lifecycle
like
account balance, payment received, account debited/credited, subscription expired/renewed, out for delivery, product dispatched/delivered, unable to deliver,
and so on are generally classified as
Transactional SMSes.
Most users usually expect to receive such messages while performing certain actions on your app/website or offline.
Such texts override all international
DND
regulations, owing to their urgent nature and are usually sent through the
SSP’s Transactional Messaging Pipeline.
Promotional SMS
Messages that are aimed at engaging users with offers, coupons or nudge users to perform a certain action like
completing the purchase, continue streaming, try out a new service
and so on are generally classified as
Promotional SMSes.
Such text campaigns are strictly regulated by a
national do not call list
in several countries like
India, Singapore, UK, Canada, US
and are delivered through the
SSP's Promotional Messaging Pipeline.
Depending on your
SSP,
you could opt-in for a
High-priority Promotional Messaging Pipeline
to ensure timely message delivery.
Whitelisting
Depending on the
SSP
you're using, you may need to whitelist the message body, personalization tokens
(User’s Name, Order ID, Purchased Product, Account Number)
and links for all your
Transactional Messages
. Whitelisting
ensures that the message is delivered through the
SSP's transactional pipeline
as soon as possible, even if the user’s number is registered in a
national do not call list
.
This means that before you start sending
Transactional SMSes,
you will need to create a standard copy for each use-case and have it registered or whitelisted with your
SSP.
For example, let’s say that we’re whitelisting the following text:
👍
Transactional SMS Template for Delivery Update
Hey
{{user['system']['first_name']}}
,
Your Order ID,
{{event['custom']['Order Placed']['custom']['Order ID']}}
is out for delivery! Track it here:
https://dummylink.com/track-order
{{user['system']['first_name']}}
personalizes message to each user's registered first name
{{event['custom']['Order Placed']['custom']['Order ID']}}
personalizes message to the latest order placed by each user
Then, while whitelisting the message, you will need to request your
SSP
for a standard code they use to identify the personalization tokens and links. This means that the actual message you whitelist would look something like this (depending on the codes used by your
SSP
):
👍
Whitelisting Delivery Update SMS with an SSP
Hey
#123#
,
Your Order ID
#123#
is out for delivery! Track it here:
@yxz
However, do keep in mind that any major deviation in the text being sent to your users, and the whitelisted text will cause the
SMS
to be treated as a
Promotional Message
.
SSP
You can think of
SSPs
as middle-men that transmit the message from
WebEngage
to the
Mobile Network Operators
of your users. We have partnered with several global SSP leaders to help make
SMS marketing
a seamless process for you.
Click to enlarge
SSP Integration
As shown below, you can integrate multiple
SSPs
with your project by navigating to
Data Platform> Integrations > SMS Setup (Configure) > SMS
.
Click to enlarge
Here, you will find a list of all the
SSPs
for which we provide ready-to-use integrations. And if you have already added a few
SSPs
to your project, then you will be able to view the configuration details in the first half of this section. For example, in the visual below, you can see that two
Twilio
accounts have been integrated.
Click to enlarge
🚧
SSP Setup
Please select an SSP from the left navigation panel (Channel Configurations > SMS) to continue configuration.
Setting Up SSP for Sending Different Types of SMS Campaigns
Depending on the
SSP
you’re using, you may need to purchase separate licenses/Sender IDs for sending
Transactional
and
Promotional Messages,
respectively. Thus, while creating an
SMS campaign,
please be mindful of the fact that the
SSP
selected at
Step 3: Message
has been set up to send the
SMS Type
selected at
Step 1: Audience
.
A mismatch between the two may cause your campaign to fail.
Managing Configuration
Click to enlarge
As shown above, integrated SSPs are listed under the section,
Your SMS Service Provider List.
You can choose to
Edit
or
Delete
the integration anytime you like by accessing the
Actions
menu placed on the extreme right.
The
Actions
menu also indicates the
unique Webhook URL
you can add to your
WSP dashboard
to ensure that
delivery status notifications (
sent, failed, queued, delivered
)
are tracked under campaign stats in your WebEngage dashboard.
Editing an SSP
You can choose to edit configuration details in cases where incorrect details were entered during configuration, or the SSP updated some details post-integration.
As shown below, select
Edit
from the
Actions menu,
make your changes, and click
Save.
Click to enlarge
Deleting an SSP
Deleting an integration will cease campaign delivery for all
Running
and
Upcoming
campaigns where the respective SSP was selected for sending it. In such cases, you will be prompted by the following message.
Click to enlarge
Thus, please ensure that no existing campaigns are dependant on the SSP (you intend to delete) for sending SMSes to your users.
As shown below, select
Delete
from the
Actions menu,
and click the
Delete button
in the pop-up to confirm your decision.
Click to enlarge
Updated
7 months ago
In-app
TRAI DLT Regulations (India)
Copy Page
