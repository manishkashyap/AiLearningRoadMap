# FAQ

- URL: https://knowledgebase.webengage.com/docs/email-faq
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

FAQ
Commonly asked questions related to Email Marketing
Campaign Creation
Your dashboard comes with a highly-intuitive
6-step campaign creation interface
that enables you to customize, personalize, and test your messages with great ease. Here are a few questions that are frequently asked by WebEngage users:
1. Can I send Email campaigns to encrypted email addresses?
Yes, this can be achieved by setting up a
Private ESP
at your end. You can think of a
Private ESP
as a middle layer between WebEngage and your
ESP (Email Service Provider)
that enables you to decrypt the encrypted email addresses shared with your WebEngage account. It's a great way to maintain your user's privacy and protect their
Personally Identifiable Information (PII Data).
(In case you're wondering - a Private ESP integration works for sending all types of campaigns, including transactional messages.)
Here's how it works👇:
Step 1:
Create and launch your Email campaign.
(
Step-by-step guide
)
Once launched, we will send the messages to the endpoint URL specified as the Private ESP under
Integrations < Channels <
Email section
in your dashboard.
Step 2:
Your Private ESP receives the messages and decrypts phone numbers of your target audience.
Step 3:
The Private ESP forwards the Email campaign with the real email addresses to the
ESP (Email Service Provider)
you're using to deliver the messages to users.
Step 4:
The ESP receives the campaign and starts delivering the messages to the specified phone numbers.
Step 5:
Users included within the campaign's target audience receive the message and start interacting with it!
All interactions can be analyzed in real-time through the
Email Campaign's Overview section
.
Step 6:
The ESP pings back your
Private ESP
with the delivery status of each message which could be any of:
Failed
Delivered
Queued
Step 7:
Your
Private ESP
forwards the delivery status for each user to your WebEngage dashboard through a
Webhook
.
Step 8:
As soon as we receive data from your
Private ESP,
it starts reflecting under the
Email Campaign's Overview section
.
🚧
Detailed Read
How to Send Encrypted Email Addresses to WebEngage
Integrating a Private ESP with WebEngage
2. Can I send personalized attachments in an Email?
Yes, here's how you can go about it:
Step 1:
Scroll down to the
Attachments section
at
Step 3: Message
while creating the
Email campaign.
Step 2:
Specify the parent URL of the domain where the attachments are being hosted.
Step 3:
Complete the parent URL by adding a personalization token from the personalization icon nested in the field.
Please note, this will work only if the attachment file names match the exact value tracked against the
User Attribute
or
Event Attribute
used to complete the link.
In cases where the attachment is not found for a user, the Email campaign fails to get delivered. Such failures are indicated under the
Email Campaign's Overview
with the reason,
Invalid Attachment URL
.
Campaign Delivery & Failures
Here are a few questions that are frequently asked by WebEngage users:
1. What happens when a soft bounce is recorded for an Email sent to a user?
A soft bounce indicates a temporary roadblock in delivering the Email to a user. A few common reasons include:
the mailbox was full
the server was down
the message was too large for the recipient's inbox and so on.
In such cases, your ESP attempts to delivery the email at various intervals for the
Queueing Duration
specified while creating the campaign or journey. The same is reflected against the performance indicator,
Queued
with the reason,
Soft Bounce
under the
Email Campaign's Overview
.
In cases where the queueing duration expires before the user can be reached, the message is dropped by the ESP.
If you have disabled
Queueing
while creating the campaign, then the message will be dropped immediately by the ESP after attempting delivery for the first time.
In both cases, since the Email was successfully sent to the ESP, it will still be counted towards the performance indicator,
Sent
for the campaign.
👍
Fact Check
Users, for whom a Soft Bounce has been recorded are still deemed
reachable through Email
and will continue to receive messages through the channel.
2. Why are my Emails landing in the spam folder?
There are multiple factors that can cause your Email campaigns to be marked as spam by popular inbox providers like Gmail, Yahoo! mail, Microsoft Outlook and Apple Mail. A few common culprits include
incorrect domain IP warm-up before sending out emails, sending bulk emails frequently, incorrect DKIM and SPF settings
and so on.
Rest assured, WebEngage does not impact Email delivery in any way. All Email are sent to an
ESP
integrated with your dashboard, which then delivers it to your users.
🚧
Detailed Read
28 tips on How to Avoid Spam Filters When Sending Emails
3. What happens when a user clicks the unsubscribe link provided by WebEngage?
While creating an Email campaign, you can add the auto-generated unsusbcribe link to your message at
Step 3: Message
.
Unsubscribing to
Email
is a two-step process designed by us, here's how it works:
Step 1:
User clicks on the unsubscribe link. Doing so directs the user to a confirmation page designed by WebEngage.
Step 2:
User confirms their decision to unsubscribe.
As soon we receive this information for a user, the user is deemed unreachable through the channel, preventing them from receiving an further promotional email campaigns from you. However, you will still be able to engage the user through transactional email campaigns.
The user's updated channel preferences are reflected in the following sections of your dashboard:
User Profile < Channels
Email Channel Reachability under
Segments
and
Users
Email Campaign Overview
🚧
Important!
Please do not edit the auto-generated unsubscribe link while adding it to your email campaign. Doing so will prevent users from exercising their right to stop receiving further communication from you. This can cause you to unknowingly spam users, leading to reduced domain authority, poor brand reputation and even blacklisting (in extreme cases).
4. My Emails were getting delivered, until suddenly all campaigns started failing. Why is this happening?
This usually happens when email credits expire prematurely with the ESP being used to deliver the campaigns. You can easily cross-check this by analyzing failures under each
Email Campaign's Overview section
. Such failures are indicated by the reason,
ESP Quota Limit Reached/ Insufficient Credits
. Please get in touch with your ESP to upgrade your account or add more credits to ensure delivery.
Once you've fixed the situation, you can retarget all users for whom the campaign has failed. Here's how you can go about it:
Step 1:
Create a segment of users for whom an Email campaign failed
Step 2
Edit the Email campaign and add the new segment under
Step 1: Audience
5. Why do Emails fail to get delivered to some users?
Email campaigns may fail to get delivered to a few users for various reasons like,
incorrect email address, user has unsubscribed, ESP's monthly quota has expired
and so on.
🚧
Detailed Read
Email Delivery Failure Reasons
Analyzing Failures for an Email Campaign
6. Why do Emails get queued for some users?
The term,
Queued
indicates the number of messages that have been sent to a campaign's target audience but are currently lined up for delayed delivery. It usually happens when
DND Hours
or
Frequency Capping settings
are applicable for a user.
🚧
Detailed Read
How Delivery Time is Determined for Queued Messages
Analyzing Queued Messages for an Email Campaign
7. Why have my email opens suddenly increased?
Your email opens may look higher because Gmail sometimes auto-loads images before a user actually opens the email. These automatic image prefetches can get counted as opens, which increases your open rate even if the user has not viewed the email yet.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries or feedback. We're always just an email away!
8. What are True Opens?
True Opens represent email opens after removing machine opens identified through heuristic detection methods.
For example, features like Apple’s Mail Privacy Protection (MPP) prefetch email content, which trigger email open events even if the recipient has not actively opened the email. Such reliably identified machine opens, can be excluded from the total unique opens.
The remaining count reflects True Opens which gives a clearer indicator of genuine user engagement and human interaction with your email campaigns.
True Opens % is calculated as (True Opens ÷ Delivered) × 100.
Updated
about 2 months ago
Image & Text Guidelines
AMP Emails
Copy Page
