# Revenue Tracking

- URL: https://knowledgebase.webengage.com/docs/revenue-tracking
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Revenue Tracking
A detailed explanation of how you can track revenue for a campaign, channel & journey in your dashboard
The primary goal of all marketing strategies is to drive growth by amplifying revenue generation opportunities. This goal is achieved through a mix of acquisition, conversion and retention campaigns. Wouldn’t it be insightful if you could track the exact revenue contributed by each?
With WebEngage, you can tie back every cent to each campaign, sent through all the channels and Journeys! All you need to do is;
Step 1:
Map all the revenue critical events performed by your users as
Revenue Events
.
This is a simple one-time setup and can be done through
Revenue Mapping
,
nested under
Data Management
in your dashboard.
Step 2:
Set the
Revenue Event
as the campaign's or journey's
Conversion Event
and you're good to go. :)
🚧
Must Read
Please ensure that you have a robust understanding of how
Conversion Tracking
works in your dashboard before proceeding. It plays an important role in understanding how you can track revenue for all your campaigns and journeys.
How It Works
Once you've set up revenue mapping, you will need to set one of the
Revenue Events
as your campaign’s or journey’s
Conversion Event
.
This will enable us to track the total revenue contributed by each conversion.
As discussed under conversion tracking, the
Conversion Event
is tracked for all users only until you specify the
Conversion Deadline
. Thus,
Revenue
is calculated only for the conversions that occur within the deadline. And just like
Conversions, Revenue
too is tracked for all the campaign variations being tested by you.
🚧
Related Read
Please refer to,
Campaigns and Its Types
,
for a detailed understanding of all the different types of campaigns you can create through each channel and journeys.
Setting up Revenue Tracking for a Campaign
The
Conversion Event
of a campaign and its
Conversion Deadline
can be defined while creating it. This can be done for all campaigns sent through
Push, In-app, SMS, Web Push, and Email.
This cannot be configured for
On-site
campaigns at the moment. It will be made available shortly.
Let's walk you through a short use-case to demonstrate how it works:
👍
Tracking Revenue for a Subscription Renewal Campaign
Let's take the example of a media platform that offers premium content for its paid subscribers.
One of the biggest challenges faced by them is subscription renewals.
Most existing subscribers fail to keep a track of when the year-long subscription expires, lowering their renewal rates. An easy solution to this persistent lifecycle problem is to send them a gentle reminder a few days before the renewal date.
All purchases are tracked as a
custom event
-
Subscription-Purchased
The monetary value of the purchase is tracked as the event's
custom attribute
-
Plan-Value
All expiring subscriptions are tracked as the event's custom attribute -
Subscription-Expiry
Here's how they created the campaign and set up revenue tracking for it:
Step 1:
Create a segment that includes users whose subscription is about to expire within the next 2 days.
Rules of segmentation:
Include all users who have performed the event
Subscription-Purchased at least once
where the event attribute
Subscription-Expiry
is between
Now and next 48 hours
(
Detailed read on Creating Segments
.)
Step 2:
Define the campaign's
Conversion Event
as
Subscription-Purchased
Pre-requisite:
For tracking revenue contributed by each purchase, you will need to map
Subscription-Purchased
as a
Revenue Event
and set its
Revenue Attribute
as
Plan-Value
. This will help us track and attribute revenue to the campaign.
Step 3:
Set the
Conversion Deadline
as 2 Days.
This means:
Revenue
will be tracked for all users who renew their subscriptions within 2 days of receiving this campaign.
Purchases made by users who performed the event -
Subscription-Purchased,
but did not receive the campaign will not be attributed to it.
Subscriptions renewed by users after the deadline will not be attributed to the campaign either.
🚧
Detailed Read
Please refer to
Campaign and Channel Performance Indicators
for a comprehensive list of all the
Revenue metrics
tracked for each channel and its campaigns.
Please
refer here
for a quick read on how Revenue is attributed to a campaign.
Setting up Revenue Tracking for a Journey
As discussed under
Journey Campaigns
, all journey campaigns are tied to a
Journey
and are sent to your users as per the conditions defined while creating it. Thus,
Revenue Tracking
can be set up only for the journey and cannot be configured for individual journey campaigns.
The
Conversion Event
of a journey and its
Conversion Deadline
can be defined while creating it or after it's published through the
journey's Live View
section.
Revenue (and conversions) are tracked only for
Push, In-app, SMS, Web Push,
and
Email
campaigns sent through a journey. These settings do not apply to
On-site
journey campaigns at the moment. It will be made available shortly.
Let's walk you through a use-case to demonstrate how it works:
👍
Tracking Revenue for a Wishlist Reminder Journey
Let's take the example of an e-commerce app that nudges users who shortlist products in their wishlist and forget.
Each time a product is added to a user's wishlist, they track it as a
custom event
-
Wishlist Added.
To motivate these users to make a purchase, marketers of the app designed a journey. The idea was to engage users through Push and Email with gentle reminders, offers - driving their app's conversion rate and revenue.
All purchases made on the app are tracked as a custom event -
Checkout Complete.
The monetary value of the purchase is tracked as the event's
custom attribute
-
Cart-Value
Here's how they created the journey and set up revenue tracking for it:
Rule 1:
Since all purchases are tracked as
Checkout Complete,
we will define it as the journey's
Conversion Event.
Pre-requisite:
For tracking revenue contributed by each purchase, they mapped
Checkout Complete,
as a
Revenue Event
and set its
Revenue Attribute
as
Cart-Value.
This will help us track and attribute revenue to the journey.
Rule 2:
When a user performs the event,
Wishlist Added,
send them
Push Notification 1
after 1 Day.
Message:
A simple reminder, enticing users to own the products they shortlisted.
Rule 3:
If
Push Notification 1
doesn't facilitate a purchase, then send these users
Push Notification 2
after 1 day.
Message:
A time-bound offer - 10% off on any products purchased from the wishlist! It expires in 1 day.
Rule 4:
Since the time-bound offer expires within a day, and both the push campaigns have also been spaced out over a day, they set the
Conversion Deadline
as 1 Day.
This means:
Revenue
will be tracked for all users who perform the event -
Checkout Complete
within 1 day of receiving
Push Notification 1
or
Push Notification 2.
Purchases made by users who did not receive either push campaigns will not be attributed to the journey.
Purchases made by users (who received either push campaigns) after the deadline will not be attributed to the journey either.
🚧
Detailed Read
Please refer to
Campaign and Channel Performance Indicators
for a comprehensive list of all the
Revenue metrics
tracked for each channel and its campaigns.
Please
refer here
for a quick read on how Revenue is attributed to a journey campaign.
When No Revenue is Tracked
If
Conversion Tracking
is disabled or the campaign’s
Conversion Event
is not mapped as a
Revenue Event
, then no revenue will be tracked for the campaign or journey. In such cases, ‘--’ will be shown under the
Revenue
card in the
campaign’s Overview
section and the
journey’s Overview
section, respectively.
👍
When a Revenue Event is not set as a campaign's or journey's Conversion Event
There are several cases in which we engage users, motivating them to perform actions that are not directly tied to our revenue.
A few examples include -
sign up, watching a video, reading an article, rating your app, reviewing a product on your platform
and so on. Thus, the conversion event for all these campaigns would include events like -
Signup, Video-Played, Article-Viewed, Review-Submitted,
respectively.
All these actions either help users move closer to making a purchase or keep them engaged post-purchase and should not be mapped as
Revenue Events.
As a result, no revenue will be tracked for these campaigns or journeys.
Now that you have a clear understanding of how revenue tracking works, here's a detailed read on
how conversions (and revenue) are attributed to a campaign and journey.
.
Please feel free to drop in a few lines at support(AT)webengage.com in case you have any further queries or related feedback. We're always just an email away!
Updated
7 months ago
Control Groups
Campaign & Channel Performance Indicators
Copy Page
