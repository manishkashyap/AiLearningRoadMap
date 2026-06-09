# AWS SES

- URL: https://docs.webengage.com/docs/aws-ses
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
Email
AWS SES
Prerequisites
Please ensure that the following settings are in place before you integrate your
AWS SES account
with WebEngage:
1. From Email/Domain Verification
As shown below, navigate to
Domains > Email Addresses
in your
AWS SES dashboard
and verify all the
Sender IDs
you'll be using for email marketing.
Click to enlarge
Further, please avoid using your
AWS SES account
in
Sandbox Mode
while integrating it with WebEngage. If it's absolutely necessary to do so, then please ensure that the recipient address is also verified.
2. Credential Permissions
As shown below, please provide the following permissions to WebEngage for your account credentials.
3. Message Send Rate Settings
As shown below, navigate to your
AWS SES dashboard's Support Center > Create Case
to request that they increase the send rate to
2500 emails/second.
Doing so will ensure better throughput.
4. Using Dedicated IPs to Send Emails (Optional)
If your email marketing strategy entails sending high volumes of emails to thousands of subscribers, then we highly recommend that you create and use a dedicated IP (other than your actual business domain) to do so. You can easily use this IP for sending email campaigns through WebEngage by:
Step 1:
Creating a
Configuration Set
in your
AWS SES account.
Step 2:
Mapping the dedicated email marketing IP(s) to that
Configuration Set.
As shown below, this can be done by navigating to
Email Sending > Configuration Sets > Create Configuration Set
in your
AWS SES dashboard.
Now, let's show you how you can configure AWS SES as an ESP in your WebEngage dashboard.
Configuration
As shown above:
Step 1: Select ESP
Select
AWS SES
from the List of Available ESPs. In doing so, you will be prompted by a configuration modal.
Step 2: Name your Configuration
Please add a user-friendly name that enables you to identify the right ESP for a campaign
while creating it
. This comes in handy especially, when you have multiple accounts with the same ESP for sending different types of campaigns
(Transactional/ Promotional).
For example, if you have configured an
AWS SES
account for sending transactional campaigns, then you can name the configuration:
AWS Transactional
AWS SES T
Step 3: Add Credentials
Navigate to your
AWS SES dashboard
to find and copy your
Access Key
and
Secret Key.
Paste them in the configuration modal.
Step 4: Add Region
Please specify the same
Region
as the one used for configuring the
From Email/Domain
in your
AWS SES dashboard.
A mismatch between the two may cause configuration failure.
Step 5 (Optional): Add Configuration Set
In case you're using dedicated IPs for email marketing, then we recommend that you
[follow these steps to create a
Configuration Set
in your
AWS SES dashboard
](aws-ses#4-using-dedicated-ips-to-send-emails-optional)
and enter its name in this field.
Step 6: Add ESP
Click
Add ESP
, and you're good to go!
👍
Congratulations!
You've now successfully integrated
AWS SES
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
Email
Elastic Email
Copy Page
