# RFM Analysis

- URL: https://knowledgebase.webengage.com/docs/predictive-rfm-segmentation
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

RFM Analysis
A step-by-step guide to gaining deep behavioral insights via predictive RFM segmentation
RFM Analysis
provides one of the most reliable indicators of how long your existing user base will continue transacting with your business. It's a well-loved technique based on a scientific scoring model that groups people as per their transaction history – how recently, how often, and the worth of how much they bought.
At WebEngage, we can help you project each user's likeliness to continue their association with your brand via AI-driven
Predictive RFM Segmentation.
The projection is based on an algorithm that scores each user's behavior against the parameters -
Recency, Frequency, and Monetary Value.
And helps answer questions like:
How many users are likely to churn?
How many loyal customers have you earned thus far?
Which users make high-value purchases regularly?
How many users have you lost?
Which users can you potentially convert into profitable customers?
and more!
Let's quickly help you understand how it works.
How It Works
🚧
Must Read
Please ensure that you have a working understanding of
Events and Event Attributes
before proceeding. These concepts lay the foundation for RFM Analysis at WebEngage.
Depending on your business needs, you can specify up to 2
Custom Events (
Recency-Frequency Event
&
Monetary Event
)
to define the behavior you'd like to analyze.
Based on this, our in-house AI will:
Stage 1:
Narrow down the target audience to only those who have performed the specified
Event/s
within the selected time frame.
Stage 2:
Score users against the respective
Event/s
on a scale of 1 - 5 for
Recency, Frequency, and Monetary Value (of their transaction). (
How R,F,M Scoring Works
Stage 3:
Predict the likeliness of each user to continue their association with your brand by grouping them into mutually exclusive
RFM Segments
(
Here's What Each Segment Means
)
You can then leverage these segments to:
Analyze key behavioral traits of your users and identify high-intent groups.
(Analyzing RFM Grid)
Engage users in each segment with contextually personalized campaigns to fast-track your growth!
(Saving RFM Segment to Connect with Users)
RFM Scoring
At WebEngage, our in-house AI scores each user on a scale of 1 - 5 against each parameter,
Recency
,
Frequency
,
Monetary Value
.
👍
Scoring Scale
Highest (5) > High (4) > Moderate (3) > Low (2) > Lowest (1)
The user's final score is an average of the R, F, M scores, based on which they are grouped into
RFM Segments
that help you predict their behavior and identify high-intent groups.
👍
Fact Check
High RFM Score
=
High Probability of Long-term Customer Retention
Recency (R)
Measures how recently users performed the
Recency-Frequency Event
within the selected time frame. It's measured in days where a score of between 1 to 5 can be understood as
Least Recently to Most Recently.
When predicting RFM segments, users with the lowest scores are grouped into
Cold Lead Segments
(churned/ at risk of leaving) and vice versa.
Cold Segments
broadly indicate that if your existing engagement strategy remains unchanged, these users will eventually abandon your brand.
(Detailed read)
Frequency (F)
Measures how frequently users performed the
Recency-Frequency Event
within the specified time frame. It's measured as the total number of times the event was performed where a score of 1 to 5 can be understood as
Performed Event At least Once to Highest Number of Times.
When predicting RFM segments, users with the highest score are grouped into
Hot Lead Segments
(brand champions, potential loyalists), and vice versa.
Hot Segments
broadly indicate highly engaged users who have a promising affinity towards your brand and are very likely to become long-term customers. These are low-hanging fruits that you can easily leverage to drive those revenue metrics!
(Detailed read)
👍
Use-case: Understanding Frequency Scoring
Let's assume the case of an OTT platform where users can purchase monthly subscriptions. This means, that if we're analyzing RFM for the last 90 Days, then an ideal customer can be expected to purchase/ renew their monthly subscription at least 3 times.
Purchase Frequency
Score Range
0 (Users didn't subscribe within the last 90 days)
1 - 2
1
2 - 3
2
3 - 4
3 (User renews subscription regularly).
4 - 5
Monetary Value (M)
Measures how much users spent when they performed the
Monetary Event
within the selected time frame. It's based on the purchase value tracked against a
Custom Event Attribute
specified along with the event. Here, a score of 1 to 5 can be understood as
Lowest Purchase Value to Highest Purchase Value.
Depending on how a user scores against R and F, they can be grouped into
Hot Lead Segments
or
Cold Lead Segments.
Why? Because in the real world, a recent (or frequent) mid-value purchaser is a lot more valuable than a high-spender who hasn't interacted with your brand in a long-time.
(Detailed read)
*
👍
Fact Check
You can map all your monetary events as
Revenue Events
in your dashboard to track
Revenue
generated via each
Campaign
and
Journey
Configure a View
As shown below, this section can be accessed by selecting RFM from the navigation panel on the left. In doing so, you will be directed to an
RFM Query Bar
where you can define the parameters for your analysis -
Recency-Frequency Event
and
Monetary Event
.
Click to enlarge
Let's get you acquainted with the query bar:
Step 1: Select Time Frame
By default, users are scored and grouped into pre-defined RFM Segments only if they've performed the
Recency-Frequency Event
and
Monetary Event
within the last 30 days. You can alter this by specifying a time frame through the
Date Range filter.
Click to enlarge
Step 2: Select Recency & Frequency Event
This is the first parameter that determines the target audience of your analysis. Users will be grouped into various segments as per the
Recency
and
Frequency
at which they performed the Event within the selected time frame.
You can also add
Event filters
to the Recency and Frequency event for this analysis by clicking on the filter option adjacent to the dropdown.
On clicking the
filter
icon, you’ll be presented with a new window, where you can choose filters events for your analysis.
Click to enlarge
📘
The following events can be selected here:
All
Custom Events
being tracked in your dashboard
System Events:
Session Started, App Installed, App Uninstalled, User Login, User Logout, Campaign Conversion
(Here's what each event tracks)
Step 3: Select Monetary Event (& Event Attribute to Aggregate By)
You can think of the
Monetary Event
as behavioral data that tracks a monetary transaction on your app/website. It's the second parameter that determines the target audience. This means
RFM Analysis will be done for only those users who have performed the_
Recency-Frequency Event
_ AND the
Monetary Event
within the selected time frame.
🚧
It's Optional!
While we highly recommend that you specify a
Monetary Event
so that we can present highly actionable insights into your users, you can choose to skip it. Such can be the case when analyzing:
Content readership/ viewership
Usage of a specific feature on your app/website,
and so on.
In such cases, the
RFM Grid
will not indicate segments where
Monetary Value
is a deciding factor and no values will be indicated against
Monetary
in the
R, F, M Range Table
.
Here's how you can go about it:
Step 1:
As shown below, click the second dropdown to select the parameter for computing each user's monetary value and predicting their worth as a marketing lead.
You can also add Event filters for your monetary event of this analysis by clicking on the filter option adjacent to the dropdown.
On clicking the filter icon, you’ll be presented with a new window, where you can choose filters events for your analysis.
Click to enlarge
📘
The following Events can be selected here:
All
Custom Events
being tracked in your dashboard
System Event:
Campaign Conversion
*
Step 2:
Select Event Attribute (to aggregate actual monetary value)
As you are aware, each
Event
can be further understood in the context of its
Event Attributes
. Thus, specifying an event attribute of the monetary event enables us to compute its actual value for each user and group them into a relevant RFM segment.
Click to enlarge
👍
For example, in the above visual we're analyzing the
Monetary Value
of the
Custom Event
, Checkout Completed
, aggregated by the
Event Attribute
, Cart Value.
This means:
Our algorithm will first identify the highest spends and the lowest spends
(
also indicated as Monetary Range in the R, F, M Range Table
)
Users will be scored on a scale of 1 - 5 as per their total
Cart Value
(over the last 30 days), taking the above-mentioned range as a benchmark.
Based on their score, users will be grouped into an appropriate
RFM Segment
.
Analyzing RFM Grid
Based on the events specified in the
Query Bar,
each user is scored and bucketed into an RFM group predefined by us at WebEngage. Each tile in the RFM grid represents an RFM Segment and its size is directly proportional to the number of users grouped under it.
What Each RFM Segment Indicates
Click to enlarge
👍
Fact Check
You may not see all
11 RFM Segments
in the grid for your query. This usually happens if none of the users' scores fall within the
Scoring Range
of a particular segment. As a result, the respective segment is eliminated from the grid.
(Don't worry! Your dashboard is working just as it's supposed to.)
View Analysis
In this option you will be able to select a segment and a user attribute, this will filter only the users in the segment or the user attribute and the RFM will be calculated for only those users in the filter.
1. RFM Segments
Based on the parameters defined by you, each user in the target audience is scored and grouped into 11
RFM Segments
defined by us. These groups are mutually exclusive and a user can belong to only one at any given point in time. In terms of business opportunity, you can analyze the RFM Segments as indicators of
Cold Leads
and
Hot Leads
aka.
Users Most Likely to Churn
vs.
Users Most Likely to Stay.
Here's a list of all the pre-defined RFM Segments in ascending order of marketing opportunity, starting from the coldest segment to the hottest ones. Typically, the growth optimization sweet spot lies between the segments
Cannot Lose Them
and
Potential Loyalists
as these users can potentially be converted into
Brand Champions (with an aggressive, yet measured engagement strategy, over a long period of time of course!)
Lost
Hibernating
About to Sleep
At Risk
---- Retention & Revenue Optimization Sweet Spot Begins! ----
Cannot Lose Them
Need Attention
New Users
Promising
Potential Loyalists
---- Retention & Revenue Optimization Sweet Spot Ends ----
Loyal
Champions
Now, let's walk you through each segment and how you can engage the users to achieve your marketing goals:
Lost
(Behavioral traits of users are usually marked by the
Lowest Recency + Lowest Frequency + Lowest Spends
)
These customers generate a tiny percentage of your overall revenue. This segment has the lowest priority. Do not waste resources on them as they are doubtful to come back, and even if they did, they are unlikely to spend a lot.
About to Sleep
(Behavioral traits of users are usually marked by
Low Recency + Moderate Frequency + Lowest Spends
)
The customers in this segment have not purchased in a relatively long time but not to the extent that they are unapproachable. Hence, their interest might be revived, and you can try to motivate them to make another purchase by offering discounts.
Hibernating
(Behavioral traits of users are usually marked by
Moderate Recency + Low Frequency + Low Spends
)
Probably only around 5% of your revenue comes from this segment. The customer value of members of this group is below average. Do not overspend on advertising for this group, as your investment return is not likely to be positive.
At-risk
(Behavioral traits of users are usually marked by
Moderate Recency + High Frequency + Moderate Spends
)
This group is very similar to the "Cannot lose them" segment, but its members have made a purchase on your website more recently. This segment might be even slightly more valuable than "Cannot lose them" as the approached customers from these groups are more likely to respond. Approach this group as you did with the previous segment but based on the profit-difference between them, decide which of these two groups deserves more of your campaign resources.
Cannot Lose Them
(Behavioral traits of users are usually marked by
Lowest Recency + Moderate Frequency + High Spends
)
The customer value of this segment's members is above average, but they have not made a purchase recently. They likely continue to buy products from the same category as they did in the past but started to purchase from your competitors. It would help if you prepared a discount and gift campaign for them. You've probably already earned high margins from their purchases, which should give you the confidence to invest in them so that you get them back as your customers. The campaign should involve recommendations based on their previous activity, consisting of both items purchased and items viewed. It would help if you also approached them with the new and popular products they had been previously interested in. Often these customers had some negative experience based on which they stopped buying from you. You should try to find the reason by asking them directly in an email and then giving them a gift if they respond.
Need Attention
(Behavioral traits of users are usually marked by
High Recency + Moderate Frequency + High Spends
)
These customers are probably considering now from whom should they buy a product next. It would help if you motivated them to choose you over your competitors. It would help if you communicated to this group the most effective time-limited promotional campaigns that are most effective when displaying countdown banners. Use product recommendations based on their behavior on the website. You also need to show your customers that your selling proposition is unique - show all the important advantages of choosing your brand with a personalized web layer catering to the specific wants of the particular customer.
New Users
(Behavioral traits of users are usually marked by
Highest Recency + Low Frequency + Moderate Spends
)
These customers bought from you relatively recently for the average or below-average price, and they have not been frequent customers - possibly this is their first purchase from your website. You do not know these customers yet, so they still can turn up as highly valuable. It would help if you offered them discounts for an additional product in the basket to see whether they are the customer's kinds to whom you can upsell. It would help if you also tried to get their consent for your newsletter to include them in your regular marketing communication. You can also send them satisfaction surveys concerning their recent order to get a better awareness of who these customers are and what they want.
Promising
(Behavioral traits of users are usually marked by
Highest Recency + Moderate Frequency + High Spends
)
These customers bought from you relatively recently for high value, but they have not been frequent customers - possibly this is their first purchase from your website. You need to motivate to make another purchase because if they do, it will probably be another purchase of high monetary value. High profits from the first purchase give you the resources to invest in these customers so that you will be able to retain them and turn them into regulars. Inform them about special offers related to their high-value purchases. It is useful for you to further analyze the members of this group and find out what motivated them to make such a high-value purchase, mainly if more customers bought the same high-value purchase.
Potential Loyalist
(Behavioral traits of users are usually marked by
High Recency + High Frequency + Moderate Spends
)
These customers already bought from you more than once, but their basket size was not too big. Try to motivate them to increase the number of items in their cart by showing them cross-selling recommendations.
Loyal
(Behavioral traits of users are usually marked by
High Recency + Highest Frequency + High Spends
)
These are very active and therefore precious customers. They possibly account for up to 20% of your revenue. You probably have an excellent ability to communicate with them as they visit your website regularly, and most of them subscribed to your newsletter. Your goal with this segment is to make these customers even more satisfied to preserve their current behavior. As you know, these customers well use highly personalized communication. Prevent the tendency for spamming them, propose fewer products but the ones they are very likely to be interested in. You can try to motivate them to share their positive experiences online as they are relatively likely to do so after being asked.
Champions
(Behavioral traits of users are usually marked by
Highest Recency + Highest Frequency + Highest Spends
)
These customers are responsible for a big share of your revenue, so put a lot of effort into keeping them happy. Give them something extra that the regulars do not get, for example, limited series of products or special discounts to make them feel valued. Use communication similar to the "Loyal" segment. You might make them your ambassadors, giving them a margin of your profits to bring you, new customers. You should also regularly ask them for feedback as they might know your products and services even better than you.
We hope this helps you identify specific behavioral patterns so that you can respond to them with an appropriate engagement strategy that fosters retention-led growth.
2. R, F, M Range
You can take a quick peek into each RFM Segment in the Grid by analyzing its key behavioral traits. This helps answer questions like:
How long ago did the interaction occur?
How frequently does the segment interact with your app/website?
How much revenue has the segment generated within the entire duration?
You can find these insights in the
R, F, M Range Table
that indicates the actual values tracked against the
R&F Event
and
Monetary Event
for the entire segment. As shown below, the range table can be accessed by clicking on a
Tile.
Click to enlarge
Let's quickly get you acquainted with the table:
Range
Average
Indicates the actual values (min to max) tracked for all users in the segment.
Indicates the most common behavior you can expect from a user in the segment.
Recency
Indicates how long ago users performed the
R&F Event
in days.
Indicates the median recency at which users of this segment interacted with your app/website.
Frequency
Indicates how many times users interacted with your app/website within the selected time frame.
Indicates how often you can expect a user in this segment to perform the
R&F Event
Monetary
Indicates how much the users have spent within the selected time frame.
Indicates the average spending power of a user.
👍
Understanding R, F, M Range for Order Placed via E-commerce App
In the below visual we've analyzed the segment,
Cannot Lose Them
for users who have performed the:
R&F Event:
Order Placed
Monetary Event:
Order Placed
, Aggregated by:
Order Value
Within the last 90 Days.
These insights indicated that:
Users in this segment placed at least one order between the last 54 - 89 Days.
Users in this segment placed 10 orders on average within the last 90 days, with some users placing up to 169 orders!
Users in this segment contributed an average of $263 in revenue over the entire duration, with some users contributing up to $637.
3. Saving RFM Segment Data
You can easily export an
RFM Segment
as a
Static List
in your dashboard to:
Save all its data permanently in your dashboard
(under
Segments > Static Segments
).
You can analyze the segment in further detail to identify
Known Users, Unknown Users,
and their preferred channels of engagement.
Engage users in the RFM group with highly personalized messages through multiple channels
(like Mobile Push, In-app, SMS, On-site, Web Push, Email & WhatsApp).
Here's how you can Save an RFM Segment:
Click to enlarge
Step 1:
Click on the RFM tile, and click the
Save as List
button on the info card. In doing so you will be prompted by a pop-up.
Step 2:
Give your segment an appropriate name that helps you track it down via
List of Segments
at a later time, in your dashboard.
Step 3:
Select the type of list you want to create i.e.
Static or Refreshing list
.
For
Static list
, continue by selecting the checkboxes with the segments you’d like to include in your list.
For a
Refreshing list
, mention the time period for which you’d like your list to be created, along with the refresh frequency.
Step 4:
In the table below, you'll see all the RFM titles along with their associated users. The title you have selected will be pre-selected by default. You can also select multiple RFM titles to combine their users into a single list. After making your selections, click on '
Create List
'.
Step 5:
You can find these lists in the
Segments tab under the Lists subsection
.
🚧
Related Read
Analyzing the RFM Segment You Just Saved
We hope this has equipped you with a robust understanding of how you can leverage
WebEngage's Predictive Segmentation
to retain & nurture your users more effectively.
Please feel free to drop in a few lines a
[email protected]
if you have any queries or feedback. We're always just an email away!
Updated
4 months ago
So, what's next?
Now that you have hot insights into your users - let's show you how you can engage each RFM group with highly targeted messages!
Creating Push Campaigns
Creating In-app Campaigns
Creating SMS Campaigns
Creating On-site Notifications
Creating Web Push Campaigns
Creating Email Campaigns
Copy Page
