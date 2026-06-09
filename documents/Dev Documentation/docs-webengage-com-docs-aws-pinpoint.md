# AWS Pinpoint

- URL: https://docs.webengage.com/docs/aws-pinpoint
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
SMS
AWS Pinpoint
AWS Pinpoint
is a communication service and can be used in your
WebEngage dashboard
as an SMS Service Provider to send highly personalized SMSes to your entire userbase.
Pre-requisites
While all messages will be sent to Pinpoint for final delivery to users, all
Delivery Status Notifications
like
SMS Sent, Queued, Failed
, and so on, will be tracked through the
Amazon Kinesis Data Firehose Stream
that is linked to the Pinpoint account. Thus, please ensure that the following settings are configured in your
AWS Pinpoint
and
Amazon Kinesis Data Firehose
accounts before adding
Pinpoint
as an SSP in WebEngage:
Step 1: Setup AWS Pinpoint Project
You will need to create a Pinpoint project and enable SMS as a channel.
Here's how you can set it up
Step 2: Create Amazon Kinesis Data Firehose Stream
Amazon Kinesis Data Firehose
is a data streaming service that acts as a middle-man between
AWS Pinpoint
and your user's mobile network provider. It enables Pinpoint to relay delivery status notifications to WebEngage for each user in real-time.
Here's how you can set it up
Depending on the WebEngage Data Center you're using, please add the relevant URL to create a data stream.
🚧
WebEngage Tracker Endpoint URL for Global Data Center
If your dashboard URL starts with
dashboard.webengage.com
then it means that you're using our
US Data Center.
Please add the following URL against the field,
HTTP Destination
in your
AWS Kinesis Data Firehose account:
https://st.webengage.com/tracking/amazon-pinpoint-events
🚧
WebEngage Tracker Endpoint URL for India Data Center
If your dashboard URL starts with
dashboard.in.webengage.com
then it means that you're using our
India Data Center.
Please add the following URL against the field,
HTTP Destination
in your
AWS Kinesis Data Firehose account:
https://st.in.webengage.com/tracking/amazon-pinpoint-events
🚧
WebEngage Tracker Endpoint URL for Saudi Arabia Data Center
If your dashboard URL starts with
dashboard.ksa.webengage.com
then it means that you're using our
Saudi Arabia Data Center.
Please add the following URL against the field,
HTTP Destination
in your
AWS Kinesis Data Firehose account:
https://st.ksa.webengage.com/tracking/amazon-pinpoint-events
Step 3: Link Pinpoint Project with Kinesis Data Firehose Stream
In order to send delivery status notifications for each SMS from WebEngage, we need to link it with the Kinesis Data Firehose account created by you. This can be done by setting up an event stream in your Pinpoint project and pointing it to the respective
Kinesis Firehose Stream.
Here's how you can set it up
Here's a quick overview of the process:
Step 1:
Go to
Settings
in
Pinpoint dashboard.
Step 2:
Navigate to
Event Stream
and click
Edit.
Step 3:
Add details of the
Amazon Kinesis Data Firehose Stream
created previously.
Step 4:
Click
Enable.
Step 4: Give WebEngage Access to AWS Pinpoint
Create an
IAM user
in your AWS account by adding the following code snippet. Doing so grants WebEngage the minimum permissions required to access your
AWS Pinpoint Project.
Please note:
This IAM user is not be confused with the IAM user added to the Pinpoint Project and Kinesis Data Firehose account during configuration.
JavaScript
{
 "Version": "{{version_number}}",
 "Statement": [
 {
 "Action": [
 "firehose:ListDeliveryStreams",
 "firehose:DescribeDeliveryStream"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "mobiletargeting:SendMessages",
 "Resource": "arn:aws:mobiletargeting:{{aws-region}}:{{account-id}}:apps/{{pinpoint-project-id}}/messages"
 },
 {
 "Effect": "Allow",
 "Action": "mobiletargeting:GetEventStream",
 "Resource": "arn:aws:mobiletargeting:{{aws-region}}:{{account-id}}:apps/{{pinpoint-project-id}}/eventstream"
 }
 ]
}
🚧
Please replace the following placeholders in the above code snippet with values from your account:
{{version_number}}
- Of your
Pinpoint Project
where SMS is enabled.
{{aws-region}}
- Must be the same as the
Region
configured for
AWS Pinpoint
and
Kinesis Data Firehose Stream.
{{account-id}}
- Your
AWS Pinpoint Account ID.
{{pinpoint-project-id}}
- For the Pinpoint project where SMS is enabled as a channel.
Now that you're all set let's show you how you can add AWS Pinpoint as an SMS Service Provider (SSP) in your dashboard.
Configuration
Navigate to
Data Paltform > Integrations > SMS Setup (Configure)
in your dashboard to get started.
Click to enlarge
As shown above:
Step 1: Select SSP
Select
AWS Pinpoint
from the list of Available SMS Service Providers.. In doing so, you will be prompted by a configuration modal.
Step 2: Name your Configuration
Please add a user-friendly name that enables you to identify the right SSP for a campaign
while creating it
. This comes in handy especially, when you have multiple accounts with the same SSP for sending different types of campaigns.
For example, if you have chosen to use
AWS Pinpoint
for sending
Promotional campaigns,
then we recommend that you indicate the same by naming the configuration something like:
Pinpoint Promo
AWS Promo Pipeline
Step 3: Add Region
Please specify the same
Region
as the one used for configuring
Pinpoint
and
Kinesis Delivery Stream
in your
AWS dashboard.
A mismatch will cause configuration failure.
Step 4: Add Credentials
Navigate to your
AWS Pinpoint dashboard
to find and copy your
Project ID, Access Key
, and
Secret Key.
Paste them in the configuration modal.
Step 5: Add SSP
Click
Add SSP,
and you're good to go!
In case you see an error message after doing so, please refer to these
Validation Errors
.
👍
Congratulations!
You've now successfully integrated AWS Pinpoint with your WebEngage dashboard.
You can test the integration by creating a test SMS campaign and sending it to a group of internal users (aka your teammates).
A quick guide on Editing/ Deleting an integration.
Integration Validation Errors
Once you've added your
AWS Pinpoint credentials, WebEngage
runs a validation check to ensure that everything is in place. However, there are several instances where integration could fail. Here are all the error codes you will see in the dashboard and what they mean:
Error Code
What It Means
How to Resolve
2001
Pinpoint account
is not accessible for the _Region
specified during configuration.
*Step 1:** Revisit your
Kinesis Delivery Stream
and
AWS Pinpoint
configuration to ensure that they're configured for the same
Region.
*Step 2:** Ensure that the selected
Region
during configuration is the same as the one for which
Pinpoint
and the linked
Delivery Stream
have been configured.
2002
Pinpoint account
is not linked to a
Kinesis Firehose Data Stream.
*Step 1:** Go back to your Pinpoint SMS Project
*Step 2:** Check if it's linked to a valid Kinesis Firehose Data Stream.
(Steps to link)
*Step 3:** Attempt
configuration
again.
2003
The
Kinesis Firehose Data Stream
linked to your
Pinpoint account
was not found (doesn't exist).
*Step 1:** Go back to your Pinpoint SMS Project
*Step 2:** Check if it's linked to a valid Kinesis Firehose Data Stream.
(Steps to link)
*Step 3:** Attempt
configuration
again.
2004
The linked
Kinesis Firehose Data Stream
is
Inactive.
The delivery stream status can be switched to
Active
in your Kinesis dashboard. Here's how you can go about it::
*Step 1:** Go to the
Kinesis dashboard.
*Step 2:** Navigate to
Details > Edit.
*Step 3:** Switch
Status
to
Active.
*Step 4:** Attempt
configuration
again.
2005
No
HTTP destination
has been configured in the
Kinesis Firehose Data Stream
linked to your
Pinpoint account.
*Step 1:**
Follow these steps
to set up a delivery stream.
*Step 2:** Attempt
configuration
again.
2006
The
HTTP destination
configured for your
Kinesis Firehose Data Stream
does not match the
WebEngage tracker endpoint URL.
*Step 1:**
Follow these steps
to set up a delivery stream.
*Step 2:** Attempt
configuration
again.
Delivery Failure Status
There are several instances where
AWS Pinpoint
could fail to deliver your
SMS campaign
to a user's mobile network. All failures are tracked as the
Performance Indicator, SMS Failed
in your dashboard, and can be analyzed under the
Campaign's Overview section
.
While you will only see the failure reasons in your dashboard, here's an
Error Code
mapping for your reference:
Error Code
Delivery Failure Reason
What It Means
2000
Insufficient Credits
Indicates that your Pinpoint Account has reached the credit limit set by you. Please add more credits and create another campaign (containing the same message) for users who failed to receive the message.
2003
Invalid Mobile Number
Indicates that the phone number provided by the user is invalid.
2006
User Registered for NDNC
Indicates that the user's phone number if registered in a National Do Not Call list due to which you will not be able to send them promotional messages.
2008
Message Expired
2009
Undelivered
2015
Message was Rejected
Indicates that the message was rejected by the user's mobile network service provider.
2016
Time to Live Expired (DND Queue Drop / FC Queue Drop)
Indicates that the message expired while it was
Queued
for delayed delivery.
2020
Throttling Error
WebEngage uses the
SendMessages API
to deliver messages to
AWS Pinpoint.
If the rate quota is exceeded, then AWS throttles or rejects (the otherwise valid) message requests from your dashboard.
Hence, we recommend that you
specific a Throttling Limit for the campaign
if the messaging load will exceed 240,000 messages per minute.
2021
Duplicate
Indicates that
Pinpoint
received the same message multiple times for a user. Thus, only the first message will be delivered and all duplicates will be dropped by
AWS Pinpoint.
9988
Other Failures
Unknown Error
Please feel free to drop in a few lines at
[email protected]
if you have any further queries. We're always just an email away!
Updated
7 months ago
Sinch
CEQUENS
Copy Page
