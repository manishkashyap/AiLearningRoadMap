# SendGrid (by Twilio)

- URL: https://docs.webengage.com/docs/sendgrid
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
Email
SendGrid (by Twilio)
Prerequisites
Please ensure that the following settings are in place before you integrate your
Sendgrid account
with WebEngage:
1. From Email/Domain Verification
Please verify all the Sender IDs you'll be using for Email marketing in your
Sendgrid dashboard
before proceeding.
2. Create API Key & Configure Access Permissions
🚧
Here's how you can create an API Key in your Sendgrid dashboard
Once created, we highly recommend that you give WebEngage
Full Access
across all permission categories. If that's not feasible, and you prefer granting
Restricted Access
, then please ensure that
Full Access
is given for the following:
Alerts
Email activity
Mail Send
Mail Settings
Stats
Suppressions
Tracking
User account
Restricting access to the aforementioned aspects can cause integration failure.
3. Sending AMP Emails
WebEngage now supports the delivery of AMP Emails in collaboration with SendGrid! However, you will need to implement a few additional settings before you can start engaging your users with highly personalized AMP Emails.
Step 1: Create a Tracking Domain
While email delivery status notifications are automatically tracked for all non-AMP emails in your WebEngage dashboard, you will need to create a custom tracking domain to track user engagement for your AMP Emails. This is a one-time setup and can be configured in your SendGrid dashboard.
🚧
Step-by-step Guide to Creating HTTPS Tracking Domain for AMP Email Delivery Tracking via SendGrid's documentation
Step 2: Add WebEngage's Custom Cname in SendGrid Dashboard
Once you've created the custom tracking domain for your brand, you will need to add a Cname entry for
sendgrid.webengage.com
in your SendGrid dashboard to ensure that all the components of your AMP Email are rendered successfully for your users.
Now, let's show you how you can configure SendGrid as an ESP in your WebEngage dashboard.
Configuration
Click to enlarge
As shown above:
Step 1: Select ESP
Select
Sendgrid
from the List of Available ESPs. In doing so, you will be prompted by a configuration modal.
Step 2: Name your Configuration
Please add a user-friendly name that enables you to identify the right ESP for a campaign
while creating it
. This comes in handy especially when you have multiple accounts with the same ESP for sending different types of campaigns
(Transactional/ Promotional).
For example, if you have configured a
Sendgrid
account for sending both transactional and promotional campaigns, then you can name the configuration:
Sendgrid all campaigns
Sendgrid Global
Step 3: Add API Key
Navigate to your
Sendgrid dashboard
to find and copy your
API Key,
paste it in the configuration modal.
Step 4 (Optional): Add IP Pool Name
If you're using a specific IP for email marketing, then please specify the same here. You can skip this field if no such settings have been configured in your Sendgrid dashboard.
Step 5: Add ESP
Click
Add ESP,
and you're good to go!
👍
Congratulations!
You've now successfully integrated
Sendgrid
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
Octane (by ValueFirst)
SendinBlue
Copy Page
