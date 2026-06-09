# Netcore

- URL: https://docs.webengage.com/docs/netcore
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
Email
Netcore
Prerequisites
Please ensure that the following settings are in place before you integrate your
Netcore account
with WebEngage:
1. From Email/Domain Verification
Please verify all the Sender IDs you'll be using for Email marketing in your
Netcore dashboard
before proceeding.
2. Generate & Verify API Key
Here's how you can go about it:
Step 1:
As shown below:
Login to your
Netcore Falconide
dashboard and navigate to the
Settings > API > Sending API
section.
Click on
View Settings
under the section,
SMTP, HTTP, & TRIGGERARE API Details.
Step 2:
Under the section,
API Credentials
, click
Show.
Step 3:
Verify your
Netcore
credentials again to view the
API Key
.
Now, let's show you how you can configure Netcore as an ESP in your WebEngage dashboard.
Configuration
Click to enlarge
As shown above:
Step 1: Select ESP
Select
Netcore
from the List of Available ESPs. In doing so, you will be prompted by a configuration modal.
Step 2: Name your Configuration
Please add a user-friendly name that enables you to identify the right ESP for a campaign
while creating it
. This comes in handy especially when you have multiple accounts with the same ESP for sending different types of campaigns
(Transactional/ Promotional).
For example, if you have configured a
Netcore
account for sending both transactional and promotional campaigns, then you can name the configuration:
Netcore Global
Netcore (all types)
Step 3: Add API Key
Navigate to your
Netcore dashboard
to find your
API Key,
paste it in the configuration modal.
Step 4: Add ESP
Click on
Add ESP
and you are good to go!
Step 5: Add WebEngage Webhook URL in Netcore dashboard
(Highly Recommended)
Adding the
WebEngage Webhook
in
Netcore
will enable us to receive delivery status notifications for each user. This includes
campaign performance indicators
like message delivered, failed, queued, opened,
and so on.
Here's how you can go about it:
Step 5.1.:
As shown below, you will find your
Netcore integration
under the section,
Your Email Service Provider List.
Step 5.2.:
Click the overflow menu placed on the extreme right, click
View Webhook URL
, and copy it.
Step 5.3.:
As shown below, Navigate to
Settings > API > Webhooks
in your
Netcore dashboard
and configure the following settings:
Select
POST
as the
Method of Data Transmission
Configure the section
Custom APIs
and leave global API blank. Here's how you can go about it:
Paste the WebEngage Webhook URL under the following fields & check all the boxes under each to provide permissions:
Emails are Sent
Emails are Bounced
Emails are Unsubscribed
Emails are Abuse
Emails are Dropped
Emails are Invalid
Do not add the
Webhook URL
under the fields;
Emails are Opened, Emails are Clicked.
Don't forget to save all your settings. :)
👍
Congratulations!
You've now successfully integrated
Netcore
with your WebEngage dashboard.
You can test the integration by creating a test Email campaign and sending it to a group of internal users (aka your teammates).
A quick guide on
Editing/ Deleting
an integration.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries or feedback. We're always just an email away!
Updated
7 months ago
mGage (Karix)
Octane (by ValueFirst)
Copy Page
