# Uninstalls

- URL: https://knowledgebase.webengage.com/docs/uninstall-analytics
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Uninstalls
A walkthrough of how you can leverage our uninstall analytics to curb app uninstalls & win back lost users
One of the most heartbreaking realities for mobile marketers is seeing users vanish. One moment they're interacting with your app, and the next moment they decide to drag your app into the
Remove bin. :(
While it's impossible to eliminate this behavior, we can definitely empower you with all the data and insights you need to curb it.
Presenting,
Uninstalls!
- Your go-to section for gaining rich insights into all the users who have uninstalled your app. This section is great for:
Analyzing
Push Notifications
that cause a high number of users to uninstall.
(
skip to Overview, Push Campaigns Leading to Most Uninstalls
)
Identifying campaigns through which most of the lost users were acquired
(and start investing less in these). (
skip to Overview, Acquisition
)
Gaining in-depth insights into what's causing uninstalls to strategize how to curb it and win back lost users.
(
skip to Analyze
)
Digging into a churned user to understand who they are, why they uninstalled and downloading a customized list of all churned users for retargeting via other platforms.
(
skip to List of Users
)
How Uninstalls Are Detected
At WebEngage, we detect app uninstalls in the following ways:
Method 1: Silent Push Notifications
A
silent notification
with an empty payload is sent to all the devices registered to all your users once a day. If we're unable to reach a device during this process, then we learn that your app has been uninstalled.
Method 2: FCM Response on Attempting Notification Delivery
All
Push Notifications
are sent to FCM for delivery to your Android users. Each time FCM (Firebase Cloud Messaging) is unable to deliver a
Push Notification
to a user due to the fact the app has been deleted, it's conveyed as the
Delivery Failure
reason -
Uninstalled. (Can be analyzed under a
Push Campaign's Overview section
)
In both cases, these users are:
Counted towards
Total Uninstalls
, indicated under this section.
Marked as
unreachable on Push
.
(If a user reinstalls your app on a later date, then they will be deemed reachable on
Push
once again.)
Now, let's dig in!
First Impression
By default,
Uninstalls
presents a comprehensive overview of all the users who have
Uninstalled
and
Installed
your Android and iOS apps within the last 7 days.
Click to enlarge
To give you structured insights,
Uninstalls
has been divided into three sections -
Overview, Analyze, List of Users.
You can toggle between these sections through the navigation bar highlighted below.
Click to enlarge
You can choose to analyze Uninstall (and Install) trends for a custom time frame as per your analytical needs. Let's show you how you can go about it:
Click to enlarge
As shown above, using the filter placed on the top right, you can choose to analyze users who have uninstalled your app within a specific time frame across all three sections:
Overview, Analyze and List of Users.
📘
The following time periods can be selected here:
Today
Yesterday
Last 7 Days
Last 30 Days
Last 90 Days
Custom Dates (as selected by you)
Now, let's get you acquainted with the workings of each section:
Overview
This section presents a top-level view of all users who have uninstalled your Android or iOS app within the selected time frame against important parameters like:
Total number of users who have uninstalled and their channel reachability
(
skip to Overview
)
Trends of app installs and uninstalls
(
skip to Install & Uninstall Trends
)
Campaigns that have caused highest uninstalls
(
skip to Push Campaigns Leading to Most Uninstalls
)
Sources of acquisition of all lost users
(
skip to Acquisition
)
Technological preferences and locations of all lost users
(
skip to Technology & Location
)
Let’s deep-dive into each subsection:
1. Overview
Click to enlarge
Let's go over each card:
Total Uninstalls
Indicates the total number of users who have uninstalled your
Android or iOS app
within the selected time frame.
This number is further broken down by
iOS and Android,
indicating the number of users who have uninstalled the respective apps.
Reachable Users
Indicates the total number of users who have uninstalled your app but can still be reached through at least one channel of engagement, at present.
Users who are reachable through multiple channels are counted towards the
total number of reachable users
only once to avoid double counting.
This number is further broken down by
SMS
,
Web Push
, and
Email
- helping you identify the most viable mediums to engage and win back these users.
Users who are reachable through multiple channels are counted towards the reachability number of all the respective channels. This is why, a sum of users reachable through
SMS, Web Push, and Email
is greater than the total.
🚧
Related Read
Please refer to
Channels and Channel Reachability
for a robust understanding of what user reachability means for each channel.
Total Installs
Indicates the total number of users who have installed your Android or iOS app within the selected time frame.
This number is further broken down by
iOS and Android,
indicating the number of users who have installed the respective apps.
👍
Fact Check
The total number of app users acquired within the selected time frame equals
Total Installs minus Total Uninstalls.
2. Install & Uninstall Trends
Click to enlarge
As shown above, by default, behavioral trends are shown only for the first three metrics -
Total Uninstalls, Android Uninstalls, iOS Uninstalls
for the selected time frame.
You can choose to deselect these or select
App Install
metrics from the list on the right, as per your analytical needs.
📘
App install-uninstall trends can be analyzed against the following metrics:
Total Uninstalls:
Presents a sum of users who have uninstalled your Android or iOS app within the selected time frame.
Android Uninstalls
iOS Uninstalls
Total Installs:
Presents a sum of users who have installed your Android or iOS app within the selected time frame.
Android Installs
iOS Installs
Changing the Format of Visualization
While the default format of data visualization is a
Line Graph,
you can change this to a
Bar Graph
or a
Table
through the overflow menu placed on the top right, as shown below.
Click to enlarge
When analyzing install-uninstall trends as a
Table,
you can choose to view the data in an ascending/descending order, as per your analytical needs. :)
Now, let's analyze a short use-case to show you how you can make the most of these insights:
👍
Analyzing Install & Uninstall Trends for an E-commerce app for a Month
Let's take the example of an early stage e-commerce app. Recently they noticed a worrying drop in their user base. While they have both, Android and iOS users, the share of Android users has always been higher.
Hence, they decided to draw a comparison between the
Install
and
Uninstall
trends for their Android app, for the
Last 30 Days
to understand what's happening.
Here's what their analysis looked like:
Click to enlarge
Key takeaways:
While for most days they have recorded a healthy app install trend, you can clearly notice spikes where uninstall numbers were close to total installs. This indicates a poor retention rate.
When compared to the app install trends - the highest number of uninstalls were detected on
March 18 and March 20.
However, on
March 20,
the number of
app installs (8,789)
dipped below the number of
uninstalls (9,135)
- indicating that they lost a significant number of users on this day.
So, what happened? Why did a majority of users decide to uninstall their apps on_March 20?_
Let's dig deeper into the list of
push campaigns
shown in the next section for more insights. Here's what they found:
Click to enlarge
Key takeaways:
Their onboarding journey campaign,
App Install & Register
has been attributed with maximum
uninstalls (10,085)!
This is especially worrisome as it indicates that users may have uninstalled shortly after installing the app.
The second highest number of
app uninstalls (7,023)
have been attributed to their cart abandonment journey campaign,
Cart abandonment - smart trigger.
The third campaign highlighted above -
March 20 New Android Push
it's attributed with
4,674
of the
9,135 uninstalls
that occurred on
March 20.
Problems with their onboarding, cart abandonment, and promotional campaigns suggest a huge gap between their user's needs and their messaging. Seems like marketers of the app will need to dig deeper into all the respective campaign and analyze their entire engagement strategy to ensure a better retention rate.
Doing a
Cohort analysis
of
App Installs to App Uninstalls
for the same time frame, could help you dig deeper into such trends.
3. Push Campaigns Leading to Most Uninstalls
Click to enlarge
Here you will find a detailed account of the top 10 push campaigns that have been attributed with the highest number of app uninstalls within 24 hours of being delivered to a user, within the selected time frame.
You can analyze the overall impact of each campaign against the following performance indicators:
Delivered
Unique Clicks
Unique Conversions
(No conversions will be tracked for a campaign if you have not defined a Conversion Event for it or its journey.
Detailed read
.)
Revenue
(No revenue will be tracked for a campaign if its Conversion Event has not been mapped as a Revenue Event.
Detailed read
.)
Uninstalls
These metrics are updated in real-time, presenting an accurate view of the impact of all campaigns on user engagement and app uninstalls.
You can choose to analyze a campaign in further detail by accessing its
Overview
section through the (hyperlinked)
Campaign Name,
as highlighted above.
(
How to Analyze a Push Campaign
)
🚧
Related Reads
Please refer to
Campaign and Channel Performance Indicators
for a robust understanding of how all the metrics listed above are calculated.
Please refer to
Campaign Types
for a detailed understanding of terms used under the column,
Type.
Select Data Format (Optional)
While the default view shows you numbers (#) under all columns - as shown below, using the overflow menu on the top left, you can choose to view
Unique Clicks, Unique Conversions, and Uninstalls
as a percentage value (%). This comes in handy when drawing a comparison between the uninstall rate of all the campaigns.
The percentage values are calculated against the total number of
Delivered
messages.
Click to enlarge
4. Acquisition
Click to enlarge
As shown above, here you will find details of the campaigns that led to your app being installed by users who subsequently uninstalled it, within the selected time frame. The idea is to help you identify campaigns which are not helping you acquire a high-intent user base and optimize your acquisition strategy accordingly.
You can choose to deselect value of the pie-charts to visualize the data as per your analytical needs.
Let's quickly go over the user acquisition details shown here:
Campaign Source:
Indicates where your users discovered you,
Google Search, Facebook, Twitter, Pinterest
and so on.
Campaign Name:
Indicates names of all the major campaigns
(on Google Search, Facebook, Twitter, Pinterest)
through which the lost users were acquired.
🚧
Please Note
All app acquisition data is gleaned from third-party platforms like
AppsFlyer
,
Tune
,
Adjust
and
Branch
. If none of the platforms have been integrated with your WebEngage account, then no acquisition data will be shown.
(Please click on a platform for step-by-step instructions on how to integrate)
5. Technology & Location
Click to enlarge
As shown in the visual above, the last section under
Uninstalls Overview
presents a breakup of all lost users by their technological preferences and locations.
You can toggle between the two options using the navigation bar.
You can also choose to deselect value of the pie-charts to visualize the data as per your analytical needs.
Let's quickly go over the details shown under each subsection:
1. Technology:
Shows details of the device on which your app was uninstalled, helping you identify uninstall trends for a particular version of your app, OS, device type and so on. The following parameters can be analyzed here:
Android/iOS App Version:
Shows a breakup of total uninstalls by your app's version.
Android/iOS Version:
Shows a breakup of total uninstalls by the OS version of the device.
Device Model:
Shows a breakup of total uninstalls by device's model
(iPhone, Redmi Note 4, Google Pixel 6, Samsung Galaxy Note 9 and so on).
Device Type:
Shows a breakup of total uninstalls by
Mobile and Tablet
devices.
2. Location:
Shows the major locations from which your app has been uninstalled, helping you identify uninstall trends by the top 5 countries
(Country)
and cities
(City).
Analyze
This section allows you to slice-and-dice all the data related to uninstalls and lost users in multiple ways, helping you gain actionable insights.
Click to enlarge
As highlighted above, the default view of
Analyze
shows you a breakup of all users who have uninstalled your Android and iOS app within the selected time frame by their
Location (Country).
Using the query bar, you can change this view to analyze churned users against two dimensions.
Let's analyze a real-life use-case to help you understand the workings of this section better:
👍
Analyzing App Uninstall Trends for Premium Members
Let's take the example of a music app that offers subscriptions for streaming ad-free music. Recently, they noticed a spike in their uninstall rates and were curious about how many premium members (subscribers) they've lost.
Hence, they decided to
analyze uninstall trends for the previous month for Android and iOS against Membership Status (Active, Inactive, Canceled).
Here's how they went about it:
Step 1: Select Time Frame
As discussed above, we'll select
Last 30 Days
as the time period of our analysis.
Click to enlarge
Step 2: Select
Dimension 1
to Analyze Uninstalls Over
Next, we'll add the first parameter we'd like to analyze uninstalls over, using the first field of the query bar.
For our analysis, we'll select the
OS Name
for comparing total uninstalls for
Android and iOS,
as shown below.
Click to enlarge
Key takeaway:
Seems like a high number of Android users (3,947) uninstalled the app over the last 30 days.
Step 3: Select
Dimension 2
under Split By
Next, we'll add the second parameter we'd like to analyze uninstalls by, using the second field of the query bar.
For our analysis, we'll select the
custom user attribute
, Membership Status,
as shown below. This will help us compare uninstalls for each OS by the membership status of premium users.
Click to enlarge
Key takeaway:
Seems like the maximum number of premium members uninstalled the app after their subscription expired (indicated by
Inactive
under each OS.)
This behavior can easily be curbed by engaging users with reminders and offers each time their subscription is up for renewal.
📘
The following user attributes can be selected under both the fields of the query bar:
Location
(Country, City)
Technology
(OS Name, Device Manufacturer, Device Model, Carrier, App Version, App ID, SDK Version)
Acquisition
(Channel, Campaign Source, Campaign Medium, Campaign Name, Referrer Host, Referrer URL)
Custom
(customer user attributes defined by you for your account,
detailed read
)
In case you'd like to analyze users against just one parameter, leave
Split By
blank and press
Enter.
Step 4: Select the Format of Visualization
Lastly, while the default format of data visualization is a
Bar Graph,
you can change this to a
Line Graph
or a
Table
through the overflow menu placed on the top right, as shown below.
Click to enlarge
When analyzing uninstalls as a
Table,
you can choose to view the data in an ascending/descending order, as per your analytical needs. :)
List of Users
This section presents extensive details of all the users who have uninstalled your Android and iOS app within the selected time frame. It comes in handy when digging into the details of a premium customer or downloading a list of users who have uninstalled your app.
Click to enlarge
Let’s get you acquainted with the most useful features of this section:
1. Customize List by Adding/ Removing Attribute Columns
By default, the table helps you analyze churned users against the following
user attributes
for all the devices on which they have uninstalled your app, within the selected time frame.
User ID
Name
Android (Device ID)
Vendor ID (iOS)
Install Date
Uninstall Date
Email (address)
Phone (number)
Country
You can choose to deselect these or select additional attributes by clicking the filter icon placed next to the search bar, as shown below.
Click to enlarge
2. View details of Multiple Devices Registered to a User
As shown below, using the down arrow placed next to the
User ID,
you can analyze details of multiple devices on which a user has uninstalled your app, within the selected time frame.
Click to enlarge
3. Access User Profiles
As discussed under
Users, User Attributes and User Profiles
,
a user profile is automatically created for all users who interact with your app and website. You can access the profile of each user by clicking their (hyperlinked) User ID.
🚧
About the documentation of 'List of Users' and 'User Profiles'
Hey there,
We request you to refer to the following documents for a detailed walk-through of all the features of
List of Users
and
User Profiles.
How to analyze the List of Users
How to analyze User Profiles
Don't worry; these sections function in the same manner across your dashboard. :)
Happy reading!
We hope this has given you a good idea of how you can make the most of our
Uninstall analytics
to curb app uninstalls and win back lost users. Please feel free to reach out via
[email protected]
in case you have any further queries. We’re always just an email away!
Updated
4 months ago
FAQ
Live
Copy Page
