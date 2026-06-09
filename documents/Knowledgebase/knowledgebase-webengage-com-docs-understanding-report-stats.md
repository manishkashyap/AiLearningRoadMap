# Understanding Report Stats

- URL: https://knowledgebase.webengage.com/docs/understanding-report-stats
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Understanding Report Stats
Applicable to all Scheduled & Downloaded Performance Reports for a Channel & Individual Campaigns
Each time a campaign is sent to your users, we track its impact through
Performance Indicators
like
Deliveries, Failures, Clicks, Conversions, Revenue
and so on. You will receive only
Unique Stats
for all these performance indicators along with other key details in
Scheduled & Downloaded Reports.
For a Channel Report:
Stats are calculated as per all users engaged within the time frame specified under
Data to Include
, even if the campaigns were sent before the selected period.
For a Campaign Report:
If the campaign is still
Running
, the report includes stats for all users engaged till present.
If the campaign has
Ended,
the report includes stats for all users that have been engaged through the campaign for up to
45 days from its
End Date
.
🚧
Why a Report's Stats May Seem Different from Dashboard's Stats
Campaign and Channel performance stats in your dashboard are shown only for the messages that are sent within the selected time frame of analysis.
However, performance stats in all scheduled/ downloaded reports are calculated as per all user interactions have that occurred within the selected time frame of analysis, even if the messages were sent before the date range.
Hence, you may find certain discrepancies between report and dashboard stats. Please feel free to get in touch with your Customer Success Manager or write to us at
[email protected]
if you have any pressing concerns. We'll be delighted to assist you!
Report Data & Performance Metrics
The following details are included in all
Scheduled and Downloaded Reports:
Column Header
Whats It Means
Campaign Name
As defined at
Step 1: Audience,
while creating the campaign.
Campaign ID
A unique ID is assigned to each campaign created in your dashboard.
Variation Name
Depending on the number of
versions created for a campaign's message
, this could be any of -
Variation A/ B/ C/ D/ E.
Variation ID
A unique ID is assigned to each message variation created for a campaign.
Channel
Indicates the channel through which the campaign was sent.
Type of Campaign
This could be any of -
One-time, Triggered, Recurring, Transactional, Journey or Relay.
Segment Name
Indicates the campaign's target segments, as defined at
Step 1: Audience
, while creating it.
(Field will remain blank if campaign has been sent through a Journey.)
Segment ID
A unique ID is assigned to each segment created in your dashboard. In case you specify multiple segments as the campaign's target audience, we'll list all the ID against this field.
(Field will remain blank if campaign has been sent through a Journey OR is being sent to All Users.)
Journey Name
If the campaign has been sent through a Journey then its name will be shown here.
(Field will remain blank if campaign has been sent directly through the channel.)
Journey ID
A unique ID is assigned to each Journey created in your dashboard.
(Field will remain blank if campaign has been sent directly through the channel.)
Campaign Tags
Tags help you categorize your campaigns as per their purpose or any other parameter that make them easier to search for in your dashboard. You can add these through Campaign's Overview.
Start Date
Indicates the date on which the
Triggered
/
Recurring
/
Transactional
/
Journey
campaign
was launched or sent to its target audience for the first time.
Send Date
(for
one-time campaigns
)
Indicates the date on which the was
One-time campaign
sent.
Conversion Event
Indicates the action users are expected to perform on your app after receiving the campaign, as specified at
Step 4: Conversion Tracking,
while creating it.
Conversion Deadline
Indicates the duration till which the campaigns'
Conversion Event
will be tracked, as specified at
Step 4: Conversion Tracking,
while creating it.
Control Group
All related details are shown only if
Control Group
was enabled for the campaign or its while creating it.
Total in Control Group
Indicates the number of users included in the campaign's
Control Group.
Unique Control Group Conversions
Indicates the number of users of the
Control Group
that have performed the campaign's
Conversion Event
.
Unique Control Group Conversion Rate
Indicates organic conversion rate of users who did not receive the campaign as they were a part of the
Control Group.
🚧
Performance Indicators shown in a Report for each Channel & its Campaign
Click the respective channel to access a list of all the stats included in your report, like
Deliveries, Failure reasons, Queuing reasons, Impressions, Clicks
and so on.
Push
In-app
SMS
On-site Notifications
Web Push
Email
WhatsApp
The following additional details are included in all
Scheduled & Downloaded Reports
where
Variation-Level Data Granularity
is selected:
Column Header
Whats It Means
Layout Name
Indicates the name of the ready-to-use template selected for creating the
Push
/
In-app
/
Web Push
campaign variation.
SSP/ ESP/ WSP
For SMS:
Indicates the
SMS Service Provider (SSP)
being used to send the campaign.
For Email:
Indicates the
Email Service Provider (ESP)
being used to send the campaign.
For WhatsApp:
Indicates the
WhatsApp Service Provider (WSP)
being used to send the campaign.
Title/ Subject Line
The first 200 characters are indicated for all campaigns variations except
SMS and WhatsApp messages.
Message
The first 200 characters of the message is indicated for all campaign variations.
Default CTA Label
Indicates the primary call-to-action text for all
In-app, On-site, Web Push and carousel-style Push campaigns.
Default CTA Link
Indicates the primary button link for all
Push, In-app, SMS, On-site and Web Push campaigns.
Image
Indicates the banner image for all
Push, On-site, Web Push campaigns.
Indicates the background image for all
In-app campaigns.
Key-Value Pairs
Indicates all the
JSON
key-value pairs added to your
Push campaign
at
Step 3: Message
.
Indicated for
SMS, Email and WhatsApp
only if you're using a
Private SSP
/
Private ESP
/ Private WSP
to send the respective campaigns.
Sender ID
(only for SMS)
Indicates the
Sender ID
used to send the campaign, as added at
Step 3: Message
.
From Name
(only for Email)
Indicates the sender's name, as added at
Step 3: Message
while creating the campaign.
From Email Address
(only for Email)
Indicates sender's email address, as added at
Step 3: Message
while creating the campaign.
Template Name
(only for WhatsApp)
Indicates the name of whitelisted message template used to create the campaign.
Understanding the Date of Report Stats
A combination of the
Frequency
of report delivery and the time frame of
Data to Include
help determine the exact dates for which the campaign performance stats are included in a report. Let's go over a use-case to understand this better:
👍
How Frequency and Data to Include Determine the Stats Included in a Report
Let's assume that you subscribe to the report -
All Push Campaigns Summary
on May 1, at 3 pm. Here's what it's settings look like:
Frequency:
Daily
When:
6 pm
Data to Include:
7 Days
This means:
The
first report
(sent at 6 pm, May 1) will include a day-wise summary of the performance of all the
Push campaigns
your users interacted with over the
last 7 Days, April 24 - 30
in which:
Day 1 will show campaign stats for April 24
Day 2 will show campaign stats for April 25 and so on.
The
second report
(sent at 6 pm, May 2) will include a day-wise summary of the
Push campaigns
your users interacted with between
April 25 - May 1 (last 7 days)
and so on.
Thus, each subsequent report will include data collected only 7 days prior to the actual date of report delivery.
Please feel free to drop in a few lines at
[email protected]
if you need further clarification on report stats or would like to request
Custom Reports
. We're always just an email away!
Updated
7 months ago
Schedule Channel Performance Reports
Configurations
Copy Page
