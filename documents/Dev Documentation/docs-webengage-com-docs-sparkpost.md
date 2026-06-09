# SparkPost

- URL: https://docs.webengage.com/docs/sparkpost
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
Email
SparkPost
Prerequisites
Please ensure that the following settings are in place before you integrate your
SparkPost account
with WebEngage:
1. From Email/Domain Verification
Please verify all the
Sender IDs
you'll be using for Email marketing in your
SparkPost dashboard
before proceeding.
2. Creating a New API Key for WebEngage
Step 1:
As shown below, navigate to the section,
API Keys
in your
SparkPost dashboard
and click
Create API Key.
Click to enlarge
Step 2:
Add API Name and Select Permissions
Choose an
API Key Name
and select
All
against
API Permissions
. If you prefer granting specific permissions, then please ensure that you check the boxes shown below. Failing to do so can cause integration failure.
Click to enlarge
Next, click the
Create API Key
button, and you're good to go!
Click to enlarge
3. If You're Using an Existing API Key
Step 1:
Navigate to the
API Key section
in your
SparkPost dashboard
.
Step 2:
Select the
API Key
you'd like to use for integrating WebEngage and select
All
against
API Permissions.
If you prefer granting specific permissions, then please ensure that you check the boxes shown below. Failing to do so can cause integration failure.
Click to enlarge
Next, click the
Update API Key
button, and you're good to go!
4. Sending AMP Emails
WebEngage now supports the delivery of AMP Emails in collaboration with SparkPost! However, you will need to implement a few additional settings before you can start engaging your users with highly personalized AMP Emails.
Step 1: Create a Tracking Domain
While email delivery status notifications are automatically tracked for all non-AMP emails in your WebEngage dashboard, you will need to create a custom tracking domain to track user engagement for your AMP Emails. This is a one-time setup and can be configured in your SparkPost dashboard.
🚧
Step-by-step Guide to Creating HTTPS Tracking Domain for AMP Email Delivery Tracking via SparkPost
Step 2: Add WebEngage's Custom Cname in SparkPost Dashboard
Once you've created the custom tracking domain for your brand, you will need to add a Cname entry for
sparkpost.webengage.com
in your SparkPost dashboard to ensure that all the components of your AMP Email are rendered successfully for your users.
Now, let's show you how you can configure SparkPost as an ESP in your WebEngage dashboard.
Configuration
Click to enlarge
As shown above:
Step 1: Select ESP
Select
SparkPost
from the List of Available ESPs. In doing so, you will be prompted by a configuration modal.
Step 2: Name your Configuration
Please add a user-friendly name that enables you to identify the right ESP for a campaign
while creating it
. This comes in handy especially when you have multiple accounts with the same ESP for sending different types of campaigns
(Transactional/ Promotional).
For example, if you have configured a
SparkPost
account for sending transactional campaigns, then you can name the configuration:
SparkPost T
SparkPost Transactional
Step 3: Select Account Type
Please select the same account type from the dropdown that was chosen while setting up your SparkPost account. A mismatch between the two may cause integration failure.
Step 4: Add API Key
Navigate to your
SparkPost dashboard
to find and copy your
API Key,
paste it in the configuration modal.
###Step 5: Add Enterprise Endpoint
If you've selected
Enterprise
as the
Account Type
at
Step 3,
then add your
SparkPost enterprise API endpoint
here.
Step 6: Add ESP
Click
Add ESP,
and you're good to go!
👍
Congratulations!
You've now successfully integrated
SparkPost
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
SendinBlue
Private ESP
Copy Page
