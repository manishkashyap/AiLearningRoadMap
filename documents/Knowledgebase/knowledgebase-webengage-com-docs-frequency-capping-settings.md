# Frequency Capping

- URL: https://knowledgebase.webengage.com/docs/frequency-capping-settings
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Frequency Capping
A step-by-step guide on how to set up a frequency cap and time gap for all your channels
Frequency Capping
is a simple one-time setup that helps you avoid spamming users by controlling the number of messages they receive within a day, week and month, spaced out evenly over a time gap.
Why is this a good idea?
It helps you determine how intensively you engage each user through the various channels of communication within a short period of time.
It also helps you solve for various dilemmas like,
How many campaigns should we send today? What if users uninstall my app after receiving too many push notifications? What if a user receives multiple promotional campaigns in a day?
and so on.
🚧
Please Note
This setting can be configured by only those
Admins
that have access to
Account Management.
If you are unable to configure, then please get in touch with the account owner.
How to Access
Frequency Capping
can be accessed through the
Settings
section of your account, as shown below.
Click to enlarge
First Impression
As shown below, this section is divided into two sub-sections -
Frequency Capping Settings and Time Gap Settings.
Both setting are implemented together for each campaign and journey as a part of their
Frequency Capping
settings.
Here's a detailed read on how it works.
Click to enlarge
Now, let's show you how you can set up
Frequency Cap
and
Time Gap
for all your channels.
📘
Frequency Capping Settings for In- App Notifications
While setting the Frequency capping for In-app Notifications the controls differ. Here are the following two Frequency Capping controls can be set:
No. of Views Per Session:
Meaning the number of In-app notifications one can see within a session.
Timegap between In-apps:
You can now specify the time interval between displaying multiple notifications. If this setting is enabled, then it prevents two notifications from being displayed back to back in case your user has been qualified for multiple notifications.
How to Set a Frequency Cap
You can specify an upper limit on the number of messages a user can receive through a channel or all channels combined by adding a numerical value in the fields listed under the columns -
Per Day, Per Week and Per Month.
📘
Here’s how we calculate the time period
A day
is calculated as
12:00 am to 11:59 pm.
This means that the daily frequency cap will reset at 12:00 am for all your users.
A week
is calculated as
12:00 am Sunday to 11:59 pm Saturday.
This means that the weekly cap will reset at 12:00 am every Sunday.
A month
is calculated as
12:00 am of Day 1 to 11:59 pm of Last Day, depending on the calendar month.
This means that the monthly cap will reset at 12:00 am on the first day of every month.
All the periods mentioned above are detected as per each user's timezone. This means that the uper limit specified under each column will be implemented as and when the time period occurs in a user's timezone.
Let's go over a use-case to demonstrate how you can set this up.
👍
Adding a Frequency Cap for All Channels Combined
Let's assume that you leverage multiple channels to engage your users daily. Since it's difficult to manually keep track of how many messages a user receives through the various channels, you decide to specify the following upper limits to avoid spamming them:
Per Day:
2 messages
Per Week:
6 messages
Per Month:
24 messages
As shown in the visual below, all you need to do is;
Step 1:
Add the numerical value - 2 under the column,
Per Day
against
All Channels Combined.
Step 2:
Add the numerical value - 6 under the column,
Per Week
against
All Channels Combined.
Step 3:
Add the numerical value - 24 under the column,
Per Month
against
All Channels Combined.
Step 4:
Click
Save
to implement your settings!
Click to enlarge
This means:
A combination of your
Per Day, Per Week and Per Month
upper limit will be applied to all campaigns sent through the channels of
Push, SMS, Web Push, Email and In-app Notifications.
Detailed read on how it works.
*
How to Set a Time Gap
You can choose to space out all your messages evenly over a period of time, by defining a
Time Gap
for a channel or
All Channels Combined.
Doing so will ensure that your users receive subsequent messages only after the specified duration.
This time gap can be specified in
Minutes, Hours or Days,
as per your engagement strategy. Here's how you can go about it:
Click to enlarge
Step 1:
As shown above, add a numerical value in the fields against your preferred channel.
Step 2:
Using the dropdown placed on the left, select the format of time. As shown above, we have selected
Hours.
Step 3:
Hit
Save
to implement all your settings!
Modifying Frequency Capping & Time Gap Settings
The frequency capping and time gap settings of your account can be modified anytime you like. Doing so will affect the delivery time of all campaigns sent or scheduled to be sent in the future.
As shown below:
Step 1:
Add new values to the relevant fields to specify a revised upper cap or time gap
Step 2:
Click
Save
to apply your settings to all future campaigns
Click to enlarge
A Few Things to Keep in Mind
This setting can be disabled for a campaign or journey while creating it. If disabled, then the respective campaigns will be delivered even if the daily, weekly or monthly cap has been exhausted for a user.
All campaigns sent with FC enabled will either fail or get queued as per the individual campaign's queueing settings if the daily, weekly or monthly cap has been exhausted for a user.
Frequency capping
cannot be applied to
In-app
and
On-site
campaigns. Given the targeted nature of these channels, messages are sent only in the context of a user's actions on your app or website, rendering such restrictions unnecessary.
Please refer to
Frequency Cappping
and
Queueing
for a detailed understanding of how you can leverage this feature for maximum impact.
🚧
Related Read: How to Enable/Disable Frequency Capping for a Campaign/Journey While Creating It
Push Campaigns
SMS Campaigns
Web Push Campaigns
Email Campaigns
Journey
In-app Notifications
We hope this has helped you configure the appropriate frequency cap and time gap for messages sent through the various channels of communication. Please feel free to drop in a few lines at support(AT)webengage.com if you have any queries or related feedback. We're always just an email away!
Updated
7 months ago
So, what's next?
Let's show you how frequency capping is applied to all your users, campaigns and journeys.
Understanding How Frequency Capping Works
Copy Page
