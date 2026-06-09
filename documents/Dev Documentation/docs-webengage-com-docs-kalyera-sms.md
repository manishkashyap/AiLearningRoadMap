# Kalyera Self Serve

- URL: https://docs.webengage.com/docs/kalyera-sms
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
SMS
Kalyera Self Serve
Follow the below steps to configure
Kaleyra
as your
SMS Service Provider (SSP)
.
Click to enlarge
As shown above:
Step 1: Select SSP
Select
Kaleyra
from the List of Available SSPs. In doing so, you will be prompted by a configuration modal.
Step 2: Name your Configuration
Please add a user-friendly name that enables you to identify the right SSP for a campaign
while creating it
. This comes in handy especially, when you have multiple accounts with the same SSP for sending different types of campaigns.
For example, if you have chosen to use
Kaleyra
for sending
Promotional campaigns,
then we recommend that you indicate the same by naming the configuration something like:
Kaleyra Promo
Kaleyra Mobile Promo Pipeline
Step 3: Add API Key
Navigate to your
Kaleyra
dashboard to find your
API Key
. Paste them in the configuration modal to connect your account with WebEngage.
Step 4: Account Type
From the drop-down, choose whether your account is
Promotional, Transactional, or Global
.
Step 5: Add Principal Entity ID
(Applicable only if you are sending messages to users located in India via domestic messaging pipeline. International messaging routes remain unaffected.)
As per
TRAI's latest SMS Marketing regulations for India
, you must be registered on a DLT portal as a business entity. Once registered, a unique Principle Entity ID (PE ID) will be assigned to you.
W.e.f from Nov 19, 2020, it is mandatory for all SSPs to pass a PE ID in the payload of each SMS message being sent to Indian phone numbers. We have partnered with
Kaleyra
to make this a seamless process for you.
Add your PE ID during configuration - we will ensure that it is relayed to the SSP for each SMS sent to your users.
Step 6: Add Header
Click to enlarge
For
Kaleyra SSP
, kindly add custom header with param
callbackurl
. The value to be passed is either
https://st.webengage.com/tracking/events
if your WebEngage dashboard is located in the US server or
https://st.in.webengage.com/tracking/events
if its located in the India server or
https://st.ksa.webengage.com/tracking/events
if its located in the Saudi Arabia server.. This configuration is required for tracking DSN (Delivery Status Notification).
📘
Find your account server location
If you are not sure which server your account is on, kindly check the URL of your dashboard:
For the US server, the URL is
https://dashboard.webengage.com
For the Indian server, the URL is
https://dashboard.in.webengage.com
For the Saudi Arabia server, the URL is
https://dashboard.ksa.webengage.com
Step 7: Add SSP
Click
Add SSP
, and you're good to go!
Step 8: Add WebEngage Webhook URL in Kaleyra Dashboard (Highly Recommended)
Adding the WebEngage Webhook in
Kaleyra
will enable us to receive delivery status notifications for each user. This includes campaign performance indicators like the
message delivered, failed, and queued
.
Here's how you can go about it:
Click to enlarge
Step 8.1.:
As shown below, you will find your
Kaleyra
integration under the section, Your
SMS Service Provider
List.
Step 8.2.:
Click the overflow menu placed on the extreme right, click
View Webhook URL
, and copy the link.
Step 8.3.:
Paste the
WebEngage Webhook URL
under the relevant field in your
Kaleyra dashboard
and click
Save
. Please connect with your
Kaleyra Account Manager
for further assistance.
👍
Congratulations!
You've now successfully integrated
Kaleyra
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
Infobip
Future
Copy Page
