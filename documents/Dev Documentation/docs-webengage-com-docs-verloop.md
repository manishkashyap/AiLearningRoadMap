# Verloop

- URL: https://docs.webengage.com/docs/verloop
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
WhatsApp
Verloop
📘
Please Note
Verloop WhatsApp Plugin is enabled only for selected accounts. If you wish to use this plugin, kindly reach out to
[email protected]
to get this plugin enabled for your account.
Kindly refer to
this
section to note important pointers when using Verloop plugin.
This document only covers how you can integrate
Verloop
as a
WSP
in
WebEngage.
Please contact
Verloop
* for further details on their services.
Configuring WSP (Verloop)
Following are the steps that will enable you to add the
WhatsApp Service Provider
to the list of WSPs offered by WebEngage.
Click to enlarge
Step 1: Add WhatsApp Service Provider (WSP)
Click the
Add WhatsApp Service Provider
or
Plus
icon on the top or click on the banner of the WSP at the bottom. In doing so, you will be prompted by a configuration modal. Select
Verloop
from the first dropdown,
WhatsApp Service Provider.
Step 2: Configuration Name
Adding a name enables you to identify the appropriate WSP for a campaign while creating it. This comes in handy, especially when you have multiple accounts with the same WSP.
Step 3: Add WhatsApp Business Number
Kindly specify the verified phone number that you'll be using to send all your
WhatsApp campaigns
in this field.
Step 4: Add Username & Password
Navigate to your
Verloop dashboard
to find your
publicApiKey
, add it in the configuration modal and click
Add WSP.
Please connect with your
Infobip Account Manager
for further assistance.
Step 5: Add Headers
To configure
Verloop
you will have to add the location where your account is located as shown below:
Click to enlarge
Kindly add
Header1
as
clientId
and
Header2
as
callback
. You can get the details for the same from your
Verloop
dashboard.
🚧
Important
Kindly get in touch with Verloop support for further assistance regarding
Header
details.
For
Verloop
, kindly add a custom header with param
callback
. The value to be passed is either
https://wt.webengage.com/tracking/events
if your WebEngage dashboard is located in the US server or
https://wt.ksa.webengage.com/tracking/events
if your WebEngage dashboard is located in the Saudi Arabia server or
https://wt.in.webengage.com/tracking/events
if its located in the India server. This configuration is required for tracking DSN (Delivery Status Notification)
📘
Find your account server location
If you are not sure which server your account is on, kindly check the URL of your dashboard:
For the US server, the URL is
https://dashboard.webengage.com
For the Indian server, the URL is
https://dashboard.in.webengage.com
For the Saudi Arabia server, the URL is
https://dashboard.ksa.webengage.com
Step 6: Add WebEngage Webhook URL in Verloop Dashboard (Highly Recommended)
Adding the
WebEngage Webhook
in
Verloop
will enable us to receive delivery status notifications for each user. This includes
campaign performance indicators
like the message delivered, failed, and queued.
Click to enlarge
As shown above, on clicking
Add WSP,
you will be prompted by a pop-up confirming that your WSP is ready to use.
Copy the
Webhook URL,
add it to the relevant field in your
Verloop dashboard
, and click
Save.
Please connect with your
Verloop Account Manager
for further assistance.
WhatsApp Templates
WhatsApp templates can be easily created by following the below steps:
Click to enlarge
Step 1: Getting Started
Click on the Plus icon next to WhatsApp Templates to get started.
Step 2: Select the WSP
Select
Verloop Messenger
from the drop-down menu to send the campaign.
Step 3: Add Template Details
Template Type:
You can choose one template type from the given options: Text, Image, Video, Document, and
Location.
Template Name:
Give the template a name for your reference.
Template Text
:
Add the message to the template. To know how to add variables in template text click here.
Template Language:
From the dropdown menu, choose the preferred language for the template.
Button (Optional):
Toggle to add the CTA button to your message.
Footer (Optional):
Enter the footer note for the template.
Template Name
Give the template a name for your reference. When entering the template name of the template kindly make sure it is in the format
templatename__campaignID
.
campaignID
will be available through your Verloop dashboard. Please contact Verloop team for furhter assistance.*
🚧
Important
Kindly make sure that there are 2 underscores
<_><_>
between
templateID
and
campaignID
.
For example,
As you can see in the above visual, we have given the Template Name as
Temp1__Campaign1
with double underscore
<_><_>
between
Temp1
and
Campaign
.
Step 4: Template Text
Add the message to the template. To know how to add variables in template text click
here
.
Step 5: Template Language
From the dropdown menu, choose the preferred language for the template.
Step 6: Footer (Optional)
Enter the footer note for the template.
Step 7: Click Add Template
Your template is now saved and ready to send your campaign.
Once you've added the templates, your
Data Platform> Integrations > WhatsApp
section will look like as shown below. You can choose to edit/ delete a template anytime by clicking on the Actions menu.
Click to enlarge
Things to Note:
Verloop plugin has a specific format for creating Template. Kindly refer to
Template Name
section to know more.
If a user blocks your business number, Verloop currently doesnt pass the same to WebEngage and you may be get a delivered status for that user.
👍
Congratulations!
You've now successfully integrated
Verloop
with your WebEngage dashboard.
You can test the integration by creating a test WhatsApp campaign and sending it to a group of internal users (aka your teammates).
A quick guide on
Editing/ Deleting
an integration.
Please feel free to drop in a few lines at
[email protected]
in you have any further queries. We're always just an email away!
Updated
7 months ago
ValueFirst
Yellow.ai
Copy Page
