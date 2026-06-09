# Unifonic

- URL: https://docs.webengage.com/docs/unifonic
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
SMS
Unifonic
Pre-requisite: Prefix Customer Phone Numbers With Country Code
Unifonic
requires all its clients to pass their user's phone numbers, prefixed with a country code without + sign. Failing to pass data in this format will cause message delivery failure.
For example, if a user is located in the UAE and their phone number is
50336029
, then please pass it to your WebEngage dashboard as
971 50336029
against the
System User Attribute
,
phone
Doing so will enable us to pass on the user details to
Unifonic
in the specified format while sending your SMS campaign.
Configuration
Follow the below steps to configure
Unifonic
as your SMS Service Provider (SSP).
Step 1: Select Unifonic
Goto Integrations > SMS Setup > Select Unifonic from the List of Available SSPs. After doing so, you will be prompted by a configuration modal.
Step 2: Name your Configuration
Please add a user-friendly name that will help you identify the right SSP for a campaign
while creating it
. This comes in handy especially when you have multiple accounts with the same SSP for sending different types of campaigns.
For example, if you have chosen to use
Unifonic
for sending Transactional campaigns, then we recommend that you indicate the same by naming the configuration something like Unifonic Transactional, UNI_Transactional etc.
Step 3: Add APPS ID
Goto your
Unifonic dashboard
, Navigate to Developers > Applications > SMS HTTP APPLICATIONS. Copy
APPS ID
and paste it in the configuration modal to connect your account with WebEngage.
Step 4: Add SSP
Click on
Add SSP
, and you're good to go!
Step 5: Add WebEngage Webhook URL in Unifonic Dashboard
(Highly Recommended)
Adding the WebEngage Webhook in
Unifonic
will enable us to receive delivery status notifications for each user. This includes
campaign performance indicators
like messages
delivered
,
failed
, and
queued
.
Here's how you can go about it:
Step 5.1.: As shown below, you will find your Unifonic integration under the section,
Your SMS Service Provider (SSP)List
.
Step 5.2.: Click the overflow menu placed on the extreme right, click View Webhook URL, and copy it.
Step 5.3.: Goto your
Unifonic dashboard
, navigate to Developers > Webhook Management > Add new Webhook > Paste the Webhook URL here, and save your settings.
👍
Congratulations!
You've now successfully integrated
Unifonic
with your WebEngage dashboard.
You can test the integration by creating a test SMS campaign and sending it to a group of internal users or your teammates.
A quick guide on
Editing/ Deleting
an integration.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries or feedback. We're always just an email away!
Updated
7 months ago
SMPP
Salla
Copy Page
