# Campaign Variations and Multivariate Testing

- URL: https://knowledgebase.webengage.com/docs/campaign-variations-testing
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Campaign Variations and Multivariate Testing
A detailed explanation of how you can test multiple versions of a campaign and automatically send the winning variant!
As marketers, we understand how subtle nuances in messaging, layouts, and colors can impact your campaigns' overall engagement and conversion rate. One approach doesn't fit all, and it usually takes a few rounds of trial-and-error to determine the exact mix for creating a hit campaign.
Most marketers rely on A/B testing to understand what resonates with their audience. But there's a hidden downside to it - while you test multiple versions of a campaign to establish a winner, you're exposing a large number of users to a less effective experience. And by the time you've identified a winning variant, you could be on the verge of losing these users, minimizing your conversion and revenue generation opportunities.
But why risk churn when you can smartly optimize your campaigns?
With WebEngage, multivariate testing is a simple, automated process! All you need to do is;
Step 1:
Create multiple
Variations
of your campaign's message
Step 2:
Set up
Send Winning Variation Automatically
Step 3:
Click the
Launch
button.
We'll test all the versions with a small group, and once we determine a winner, we'll automatically send it to the larger target audience for greater effectiveness!
Variations
When creating a campaign through
Push, In-app, SMS, Web Push, Email, WhatsApp, or a Journey
you can choose to create up to 5 versions of its message. Each version is called a
Variation
and is created independent of the other, allowing you to test all the aspects of your campaign, including the layout, body copy, buttons, links, colors, sender details, and so on.
Creating multiple Variations for testing different versions of a campaign's message
As shown above,
Campaign Variations
are referred to in the following manner in your dashboard:
Variation A:
The first version of the message created by you.
Variation B:
The second version of the message being tested by you.
Variation C, D, E:
All the subsequent versions of the message created for testing.
Now, let's deep dive into how automated
Variation
testing works.
Send Winning Variation Automatically: Concepts
Once you have created multiple
Variations
of a campaign's message, you can choose to automate the testing process by enabling -
Send Winning Variation Automatically.
Doing so will enable you to test all the
Variations
(and
Control Group
if enabled) with a smaller test audience before we determine a winning variant and send it to the entire target audience :).
Let's run you through a few related concepts:
Size of Test Audience
All the
Variations
of a campaign are equally distributed amongst a
test audience
for testing their overall impact. The
test audience
is picked from the
target audience
of the campaign, and its size can be custom-defined for all
One-time, Triggered
and
Journey campaigns.
When Campaigns get Queued or Fails
If campaigns get
Queued
for delayed delivery or fail to get delivered to users of a
test audience,
then the respective users are removed from the
test audience.
An equal number of users are picked from the
target audience
to ensure that all
Variations
are tested with a significant number of users.
Impact of Control Group
If you have added a
Control Group
to a campaign or journey, then all the users included in it will also be considered a part of the
test audience.
This will ensure that a fair comparison is drawn between the
Conversions
achieved by all the
Variations
and the
Control Group
(as users included in the control group will not receive the campaign).
All the
Variations
and
Control Group
are equally distributed amongst the
test audience
to ensure that a fair comparison is drawn between each one's performance.
👍
How Variations and Control Group are Distributed Amongst the Test Audience
Let's assume that you have created
3 Variations
of a campaign's message and have added a
Control Group
to it. As per the campaign's settings, we carve out a test audience of 6,000 users. This means;
Each
Variation (Variation A, B, C)
will be sent to 1,500 users.
(6000/4)
The
Control Group
will consist of 1,500 users who will not be sent any message.
Time to Test
Test time is the duration for which the performance of all the campaign
Variations
(and
Control Group
if enabled) are tested against a
Win Criteria
specified by you.
Depending on the type of campaign and the size of its
Test audience
, the
test time
may vary. Here's how it works for
one-time
,
triggered
,
recurring
and
journey
campaigns.
Win Criteria
Depending on your business and the target audience, a campaign can have various goals like
motivating users to make a monetary transaction, driving platform engagement by notifying users about a new blog post/video/podcast, reminding users about upcoming renewals/ tests, and so on.
In each case, the way you measure the success of the campaign will vary. For example:
The end goal of a campaign,
motivating users to make a monetary transaction,
will be measured by its
Conversions.
The end goal of a campaign,
driving platform engagement,
will be measured by its
Clicks.
The end goal of a campaign,
reminding users about upcoming renewals/ tests,
will be measured by its
Clicks, Impressions
or
Opens
(depending on the channel).
The
Win Criteria
is a similar parameter that helps us determine a winning
Variation
according to each campaign's end goal. Hence, we have made it possible for you to custom define it as
Conversions
,
Clicks
,
Impressions
or
Opens
,
depending on the channel and your strategic needs. Let's get you acquainted with each:
1. Conversions
Tracked for all the engagement channels,
Conversions
can be selected as a
Win Criteria
only if you have defined a
Conversion Event
for the campaign or journey.
Selecting
Conversions
as the
Win Criteria
will ensure that the
Variation
that achieves the highest
Unique Conversion rate
within the
Test Time
is determined as the winner.
Impact of Control Group:
If you have added a
Control Group
to the campaign or journey, then
Conversions
will be the sole
Win Criteria
of the test. This is because users of a
Control Group
do not receive any messages, deeming
Conversions
the only criteria that can help us compare the impact of each
Variation
and organic user behavior.
If the
Control Group
achieves a higher
Unique Conversion
rate within the
Test Time
, it will be determined as the winner. As a result, the campaign will not be sent to its target audience.
2. Clicks
Tracked for all the engagement channels, selecting
Clicks
as the
Win Criteria
will ensure that the
Variation
that achieves the highest
Unique Click
rate
within the
Test Time
is determined as the winner.
3. Impressions
Can be defined as the
Win Criteria
for all types of campaigns sent through
In-app
and
Web Push.
Selecting
Impressions
as the
Win Criteria
will ensure that the
Variation
that achieves the highest number of
Unique Impressions
within the
Test Time
is determined as the winner.
4. Opens
This campaign event is tracked only for
Email
and thus, can be defined as a
Win Criteria
for all types of campaigns sent through the channel.
Selecting
Opens
as the
Win Criteria
will ensure that the
Variation
achieves the highest
Unique Open
rate
within the
Test Time
is determined as the winner.
Send Winning Variation Automatically: How It Works
A winning
Variation
is determined by calculating the performance of each campaign
Variation
against the
Win Criteria
selected by you, within the campaign's
Test Time.
Test results are calculated solely based on all the messages that have been successfully delivered to the
Test audience
.
Messages that fail to get delivered to the users included within the
Test Audience
are removed from the scope of the test. An equal number of new users are picked from the campaign's target audience to match the size specified by you. This cycle continues until the campaign is successfully delivered to the specified size of the
Test Audience.
An ongoing
Variation
test will be restarted, causing the loss of any data collected previously, if:
The campaign's target audience is changed from the existing segment to a new one
The campaign's type is modified
The campaign's targeting settings (only for in-app), start date, or end date are modified
Frequency Capping
or
DND settings
are enabled/disabled
The message or settings of a campaign
Variation
are modified
A campaign
Variation
is added/removed
The
Conversion Tracking
settings are modified
Control Group
is removed/added during the test
The
Size of the Test Audience,
Time to Test
or Win Criteria
are modified.
If multiple campaign
Variations
and the
Control Group
achieve the same win rate, as per the selected
Win Criteria,
then
Variation A
will be sent to the entire target audience by default.
If the
Control Group
achieves a higher
Unique Conversion
rate than a
Variation,
then the campaign will not be sent.
Once the test ends, you will be able to analyze each
Variation
(and
Control Group
) performance through the campaign's
Overview section,
as highlighted below.
click to enlarge
🚧
Related Read
Step-by-step guide on how to compare and analyze
Variations
for
Push
,
In-app
,
SMS
,
Web Push
,
and
Email
campaigns when
Send Winning Variation Automatically
is enabled.
Now, let's show you how
Send Winning Variation Automatically
works for different
types of campaigns
:
Testing One-time Campaigns
All one-time campaign
Variations
are equally distributed amongst the
Test Audience. Once the
Test Time
ends, the winning
Variation
is determined as per the
Win Criteria* and is sent to the larger target audience as the only campaign.
Click to enlarge
Let's get you acquainted with all the settings configured in the above visual:
Size of Test Audience:
You can choose to test the
Variations
and
Control Group
(if added) with 5% to 25% of the campaign's entire target audience.
If the campaign's target audience includes less than
2,000 users,
then you will not be able to automate
Variation testing
for it, owing to the insignificant size of the resulting
test audience.
In such cases, you can choose to
test the Variations manually
.
Time to Test:
A custom
Time to Test
can be specified in
Minutes
or
Hours,
and all
Variations
can be tested for a maximum duration of
24 hours (1440 minutes).
Depending on the channel, the best time to engage users with a campaign may vary. This is why we suggest that you launch the campaign well in advance for testing and schedule it for delivery at the most viable time slot (suggested by the channel's engagement trends). Doing so will ensure that your users receive the most effective version of your campaign at a time that records the highest engagement rate.
As soon as the test time ends, we will determine a winning
Variation
as per the
Win Criteria
and send it to the entire target audience (immediately or at the scheduled time of delivery).
🚧
Please Note
Automated variation testing is currently not available for one-time campaigns that are sent
in user's timezone
.
Testing Triggered Campaigns
Triggered campaigns are the ongoing communication cycles and are sent to users only when they choose to perform a certain action or event. Thus, the most scientific way to test
Variations
of a triggered campaign is by ensuring that a significant number of messages are delivered before we draw a comparison.
Click to enlarge
Let's get you acquainted with all the settings configured in the above visual:
Size of Test Audience:
The
test audience
can be defined only in terms of
the number of messages delivered.
This means that
Variation testing
will continue until the specified number of messages have been successfully delivered.
A minimum of
500 messages
must be delivered to the target audience of a triggered campaign to ensure that all the
Variations
and
Control Group
(if added) are tested with a significantly sized audience.\
This means that the first 500 users who perform the trigger event will be considered the campaign's test audience.
During an ongoing test, if a user chooses to perform the trigger event multiple times in quick succession, they will be counted towards the test audience each time they perform the event and may receive multiple
Variations
of the campaign.
Time to Test:
The performance of all the
Variations
is calculated daily at
6 am
and
6 pm
for all triggered campaigns.
This means that once the specified number of messages are delivered, we will wait for the closest time slot to calculate each
Variation's
performance against the selected
Win Criteria
to determine a winner.
Once we identify a winning
Variation,
it will be sent as the only campaign to all the subsequent users who perform the trigger event.
Testing Recurring Campaigns
Recurring campaigns are ongoing cycles of communication that are scheduled to be sent periodically to their target audience on specific days and time.
Click to enlarge
Let's get you acquainted with all the settings configured in the above visual:
Size of Test Audience:
The entire first run of a recurring campaign is considered to be its test audience* by default.
This means that the first time you launch the campaign, all the
Variations
and
Control Group
(if added) will be equally distributed amongst the entire target audience.
If the campaign's target audience includes less than 2000 users, you will not be able to automate
Variation testing
for it, owing to the insignificant size of the resulting
test audience.
In such cases, you can choose to test the Variations manually.
Time to Test:
Test results are calculated 1 hour before the second run of the campaign. This means that depending on the frequency of the recurring campaign, its
test time
could be any of the following:
For Daily Recurring Campaigns:
23 Hours
For Weekly Recurring Campaigns:
6 Days and 23 Hours
For Monthly Recurring Campaigns:
28/29/30/31 Days and 23 Hours (depending on the calendar month)
A winning
Variation
will be determined as per the
Win Criteria
and sent as the only campaign for all the subsequent runs.
Testing Journey Campaigns
Journey campaigns are highly personalized campaigns that are sent to users only in the context of their actions, attributes, location, and so on. Each journey campaign is tied to a journey and is triggered for a user as per your conditions while creating it.
Thus, configuring
automated variation testing
for a journey campaign follows the same steps as
Triggered campaigns.
For example, as shown below, we have configured automated variation testing for an
In-app journey campaign.
Click to enlarge
Let's get you acquainted with all the settings configured in the above visual:
Size of Test Audience:
The
test audience
can be defined only in terms of
Entries
or the number of times users enter the campaign block of the journey.
This means that
Variation testing
will continue until the specified number of entries occur.
This also implies that all the
Variations
will be equally divided amongst the first
(specified number)
users who enter the journey's campaign block.
A minimum of
500 entries
must be specified to ensure that all the
Variations
are tested with a substantially sized audience.
Time to Test
:
The performance of all the
Variations
is calculated daily at
6 am
and
6 pm
for all journey campaigns.
This means that once the specified number of
Entries
occur, we will wait for the closest time slot to calculate each
Variation's
performance against the selected
Win Criteria
to determine a winner.
The winning
Variation
will be sent as the only campaign to all subsequent users that enter the journey's campaign block.
Set Variation Distribution Manually
Once you have created multiple
Variations
of a campaign's message, you can choose to automate the testing process by enabling -
Send Winning Variation Automatically
.
However, you can opt to test the
Variations
and
Control Group
,
manually if:
You are unable to automate testing due to the small size of the target audience (less than 2,000 users) of a
One-time
or
Recurring
campaign.
You are unwilling to test a
Triggered
or
Journey
campaign with a minimum of 500 messages or entries, respectively.
How It Works
By default, each
Variation
is equally distributed amongst the entire target audience of the campaign. You can choose to alter the distribution by defining a custom audience share for each
Variation,
as shown below.
Click to enlarge
👍
How Variations Are Distributed Amongst the Target Audience
For example, let's assume that you have created
4 Variations
and the campaign's target audience consists of 8,000 users.
This means that each
Variation
will be sent to 25% of the entire target audience or 2,000 users each.
However, you can choose to specify a custom distribution percentage like:
20% each for Variation A and B
30% each for Variation C and D or the likes of it.
Once set, all the
Variations
will be tested throughout the lifecycle of the campaign.
This implies that if you set up manual variation distribution for a
triggered
,
recurring
or
journey
campaign, then we will continue to deliver all the
Variations
until the campaign's
End Date
or till you decide to
Pause
or
End
the campaign.
Impact of Control Group:
If you have added a
Control Group
to a campaign or a journey, then by default, we will consider 5% of the entire target audience as the
Control Group.
You can choose to include a wider audience by increasing its share.
🚧
Related Read
Determining the ideal size of a
Control Group
as per the size of the campaign's target audience.
Comparing Variations:
You will be able to analyze the performance of each
Variation
through the campaign's
Overview section,
as highlighted below. Doing so will enable you to identify a winning
Variation
or
Control Group (if enabled)
on the basis of the
Conversions
and
Revenue
tracked for each.
Click to enlarge
🚧
Related Read
Step-by-step guide on how to compare and analyze
Variations
for
Push
,
In-app
,
SMS
,
Web Push
,
and
Email
campaigns when
Variation
distribution is set manually.
We hope this has equipped you with a robust understanding of how you can leverage variation testing to optimize your campaigns for maximum impact. Please feel free to reach us through support(AT)webengage.com in case you have any further queries, we’re always happy to help!
Updated
7 months ago
Campaign & Channel Performance Indicators
Frequency Capping
Copy Page
