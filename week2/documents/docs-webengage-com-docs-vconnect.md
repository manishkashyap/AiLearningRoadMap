# V-connect

- URL: https://docs.webengage.com/docs/vconnect
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
SMS
V-connect
Follow the below steps to configure
V-connect
as your
SMS Service Provider (SSP)
.
Click to enlarge
As shown above:
Step 1: Select SSP
Select
V-connect
from the List of Available SSPs. In doing so, you will be prompted by a configuration modal.
Step 2: Name your Configuration
Please add a user-friendly name that enables you to identify the right SSP for a campaign
while creating it
. This comes in handy especially, when you have multiple accounts with the same SSP for sending different types of campaigns.
For example, if you have chosen to use
V-connect
for sending
Promotional campaigns,
then we recommend that you indicate the same by naming the configuration something like:
V-connect Promo
V-connect Mobile Promo Pipeline
Step 3: Add Username and Password
Navigate to your
V-connect
dashboard to find and copy your account details. Paste them in the configuration modal.
Step 4: Add Principal Entity ID
(Applicable only if you are sending messages to users located in India via domestic messaging pipeline. International messaging routes remain unaffected.)
As per
TRAI's latest SMS Marketing regulations for India
, you must be registered on a DLT portal as a business entity. Once registered, a unique Principle Entity ID (PE ID) will be assigned to you.
W.e.f from Nov 19, 2020, it is mandatory for all SSPs to pass a PE ID in the payload of each SMS message being sent to Indian phone numbers. We have partnered with
V-connect
to make this a seamless process for you.
Add your PE ID during configuration - we will ensure that it is relayed to the SSP for each SMS sent to your users.
Step 5: Add Header
Please get in touch with your relationship manager at
V-connect
if these authentication headers aren't readily available in your dashboard.
Step 6: Add SSP
Click
Add SSP
, and you're good to go!
Step 7: Add WebEngage Webhook URL in V-connect Dashboard (Highly Recommended)
Adding the WebEngage Webhook in
V-connect
will enable us to receive delivery status notifications for each user. This includes campaign performance indicators like the
message delivered, failed, and queued
.
Here's how you can go about it:
Click to enlarge
Step 7.1.:
As shown below, you will find your
V-connect
integration under the section, Your
SMS Service Provider
List.
Step 7.2.:
Click the overflow menu placed on the extreme right, click
View Webhook URL
, and copy the link.
Step 7.3.:
Paste the
WebEngage Webhook URL
under the relevant field in your
V-connect dashboard
and click
Save
. Please connect with your
V-connect Account Manager
for further assistance.
👍
Congratulations!
You've now successfully integrated
V-connect
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
Twilio
ValueFirst
Copy Page
