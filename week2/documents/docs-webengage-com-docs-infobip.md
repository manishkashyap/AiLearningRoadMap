# Infobip

- URL: https://docs.webengage.com/docs/infobip
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
SMS
Infobip
Pre-requisite: Prefix Customer Phone Numbers With Country Code
Infobip requires all its clients to pass their user's phone numbers, prefixed with a country code. Failing to pass data in this format will cause message delivery failure.
For example, if a user is located in the US and their phone number is
(925) 336 0294
, then please pass it to your WebEngage dashboard as
+1 (925) 336 0294
against the
System User Attribute
,
phone
.
Doing so will enable us to pass on the user details to
Infobip
in the specified format while sending your SMS campaign.
Configuration
🚧
New Rules of SMS Marketing in India - Important!
W.e.f from Sept 25, 2020 (tentatively), TRAI has mandated the registration of -
SMS templates, Business entities, Sender IDs & User consent
with mobile operator owned DLT portals. Failing to do so will cause message delivery failure for all your campaigns.
(Detailed read)
Follow the below steps to configure
Infobip
as your SMS Service Provider (SSP).
Click to enlarge
As shown above:
Step 1: Select Infobip
Select Infobip from the List of Available SSPs. In doing so, you will be prompted by a configuration modal.
Step 2: Name your Configuration
Please add a user-friendly name that enables you to identify the right SSP for a campaign
while creating it
. This comes in handy especially, when you have multiple accounts with the same SSP for sending different types of campaigns.
For example, if you have chosen to use
Infobip
for sending
Transactional campaigns,
then we recommend that you indicate the same by naming the configuration something like:
Infobip Transactional
Infobip T Pipeline
Step 3: Add Username & Password
Navigate to your
Infobip dashboard
to find your credentials. Paste them in the configuration modal, Click
Add SSP
, and you're good to go!
Step 4: Add Principal Entity ID
(Applicable only if you are sending messages to users located in India via domestic messaging pipeline. International messaging routes remain unaffected.)
As per
TRAI's latest SMS Marketing regulations for India
, you must be registered on a DLT portal as a business entity. Once registered, a unique Principle Entity ID (PE ID) will be assigned to you.
W.e.f from Nov 19, 2020, it is mandatory for all SSPs to pass a PE ID in the payload of each SMS message being sent to Indian phone numbers. We have partnered with
Infobip
to make this a seamless process for you.
Simply add your PE ID during configuration - we will ensure that it is relayed to the SSP for each SMS sent to your users.
Step 5: Add SSP
Click on
Add SSP,
and you're good to go!
👍
Congratulations!
You've now successfully integrated
Infobip
with your WebEngage dashboard.
You can test the integration by creating a test SMS campaign and sending it to a group of internal users (aka your teammates).
A quick guide on
Editing/ Deleting
an integration.
Please feel free to drop in a few lines at
[email protected]
in you have any further queries. We're always just an email away!
Updated
7 months ago
ICS
Kalyera Self Serve
Copy Page
