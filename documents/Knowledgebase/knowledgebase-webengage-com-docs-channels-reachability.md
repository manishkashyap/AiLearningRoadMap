# Channels & Channel Reachability

- URL: https://knowledgebase.webengage.com/docs/channels-reachability
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Channels & Channel Reachability
Understanding how channel reachability is determined for a user in various scenarios
Channels
📘
At WebEngage, any medium that allows you to engage and communicate with your users through your app, website or any other platform is called a
Channel.
Currently, you can leverage the following channels in WebEngage to engage your users in real-time, backed by their personal and behavioral data (also called
user attributes
and
events
, respectively):
Push
In-app
SMS
On-site
(Notification, Surveys)
Web Push
Email
WhatsApp
Facebook Retargeting
Each channel comes equipped with ready-to-use templates and an intuitive 6-step creation interface, allowing you to create, schedule and test various versions of your message. Further, all your messages can be contextually personalized to each user, helping you create highly engaging experiences every single time!
At WebEngage, we believe that contextual engagement is the key to customer retention. However, given the multi-channel nature of user interactions today, it's becoming harder and harder for brands to reach their users at the right time, through the right channel. We found a unique, data-driven solution to this persistent problem in the form of
Reachability
.
Understanding Channel Reachability
📘
Reachability
is a measure of whether or not a user can be reached through the channels listed in your dashboard. It's an indicator of your user's preferences, helping you identify the most viable channel to engage each user, segment and your entire user base.
Once you connect your WebEngage account with your app and website, the platform starts collecting several details related to your users and their behavior. By processing their channel preferences and contact information, we can determine channel reachability at a granular level.
For example, if our platform detects that an email failed to get delivered due to an invalid email address, then the user will automatically be deemed unreachable through
Email.
And if the user updates their correct email address later, then they will be deemed reachable through the channel.
Here's how we determine reachability for each channel:
Push (Mobile)
All users who have
enabled push notifications for your app on their device AND have not uninstalled your app
are reachable through the channel.
Now, let's show you how push reachability is calculated when a user is using your app through multiple devices.
👍
Case 1: Using the app on multiple devices with same OS
Let's say that a user has downloaded your app on two devices, Device A and Device B.
Reachable on Push:
If the user disables push notifications OR uninstalls the app on
Device A
but continues to use your app through
Device B
with push notifications enabled, then the user will be deemed reachable through
Push
as a channel.
Not Reachable on Push:
If the user disables push notifications OR uninstalls the app on both
Device A
and
Device B
, then the user will be deemed unreachable through
Push
as a channel.
Now, let's show you how reachability is calculated when a user accesses your app through multiple devices that run on a different OS.
👍
Case 2: Using the app on multiple devices with a different OS
Let's say that a user has downloaded your app on four devices:
Device A
and
Device B
run on
Android
Device C
and
Device D
run on
iOS
Reachability will be calculated in the following manner:
Reachable on Android:
Now let's consider that the user has disabled push notifications only for
Device A
and continues to use your app through
Device B
with push enabled. Then as discussed under Case 1, the user will be deemed reachable on
Android.
Reachable on iOS:
Considering the same scenario as above, if the user has uninstalled your app on
Device C
but continues to use it through
Device D
with push notifications enabled, Then as discussed under Case 1, the user will be deemed reachable on
iOS.
Reachable on Push:
Since the user is reachable on both
iOS
and
Android,
the user is definitely reachable on
Push
as a channel.
However, when calculating the total number of reachable users, this user will be added to the sum only once (even though they are reachable through 2 devices and 2 operating systems) to avoid double counting. This ensures that you always get an exact idea of how many users can be engaged through a channel at any given point in time.
In-app (Messaging)
All users who have
interacted with your app at least once over the last 30 days AND have not uninstalled your app
are considered reachable through in-app messaging.
If a user has downloaded your app on multiple devices, then their In-app reachability will be calculated using the same logic as
Mobile Push
.
SMS
All users that have
a phone number AND are not registered on a
national do-not-call list
are considered reachable through SMS.
On-site
All users who have
interacted with your website over the last 30 days
are considered reachable through on-site notifications, and surveys widget.
Web Push
All users who have
opted-in to receive web push notifications through your domain AND have not blocked web push notifications from your website
are considered reachable through web push.
If the user has opted-in to receive web push notifications through several browsers and devices, then their Web Push reachability will be calculated using similar logic as
Mobile Push
.
Email
All users that have
an email address AND have not unsubscribed AND have not recorded a
hard-bounce
are considered reachable through email.
WhatsApp
All users that have
opted-in to receive WhatsApp messages from your business and have not blocked your account
are considered reachable through the channel.
By default, users that have a phone number are considered unreachable, due to
WhatsApp's strict opt-in guidelines
.
Rich Communication Service (RCS)
All users that have _a phone number AND _opted-in to receive RCS messages from your business are considered reachable through the channel.
How Reachability is Determined at a User-level
🚧
Must read
Please ensure that you have read through the concepts of
Users and User Profiles
before proceeding. Doing so will lay the foundation for understanding how reachability is determined for all your users in WebEngage.
Now that you have a robust understanding of how we determine reachability across all channels, let's walk you through a simple user lifecycle to demonstrate how varying user behavior affects this metric.
👍
Case 1: Determining Reachability for an Unknown App User
Let's take the example of a first-time user who has recently downloaded your e-commerce app. The user still hasn't signed up on your platform, making them an
Unknown User
in your WebEngage dashboard.
Here's how we'll determine the reachability of this user across all channels:
If the user has
not disabled push notifications
on their device, then they will be deemed
reachable
through
Push.
Since the user has recently downloaded your app, they will be considered an
active user,
making them
reachable
through
In-app.
Since the user has
not signed up
yet, we don't have their phone number or email address. Hence, they will be
unreachable
through
SMS
and
Email.
Since the user has been
acquired through your mobile app
and is currently an
unknown user,
there is no way for us to know if they have interacted with your website. Hence, they will be
unreachable
through
On-site
and
Web Push.
However, if this user interacts with your website, then a new
Unknown User Profile
will be created, adding another user to your total user base. As per this profile, the user will be reachable through
On-site
and
Web Push,
and will not be reachable through
Push, In-app, SMS
and
Email
for the same reason discussed above.
👍
Case 2: Determining Reachability for a Known App User
In continuation of the example discussed under Case 1 - let's assume that the user wants to make a purchase and thus, signs into your app. While signing up, they provide the following details:
Name:
Marge Simpson
Email address:
[email protected]
Phone number:
123-547-9800
Thus, Marge will now become a
Known User
in your dashboard, and all the historical data from her
Unknown User Profile
(in Case 1) will get merged with the latest
Known User Profile.
Here's how we'll determine the reachability of Marge now:
Since we have all her historical data in one place, we know that she is still
reachable
through
Push
and
In-app.
As we have her email address and phone number, she will now be deemed reachable through
Email
and
SMS
too!
She will still be
unreachable
through
On-site
and
Web Push
as she has not logged into her account through the e-commerce business's website, yet.
👍
Case 3: Determining Reachability for a Known User Who is Logged Out of Your App
Now, let's assume that Marge stopped using the e-commerce app and logged out of the account. However, after a few weeks, she received an email announcing the release of your latest fashion line, prompting her to revisit your app.
But she merely browses through the collection and forgets to log into her existing account.
Here's how we'll determine the reachability of Marge now:
As she is currently logged out of her account, you will not be able to engage her with personalized
push notifications
or
in-app messages.
However, you will still be able to reach her as an
Unknown User
through these channels. This means that you will not be able to use elements of personalization like name, recommendations based on products viewed when she was logged in, etc. in the notifications and messages, until she logs into her account again.
And just like Case 2, you will still be able to engage her with highly personalized and contextual messages through
Email
and
SMS.
Marge will still be unreachable through
On-site
and
Web Push.
👍
Case 4: Determining Reachability for Multiple Users Using the Same Device
Now, let's assume that Marge's daughter too, takes a fancy to your latest fashion line and starts using her mother's phone to browse through the products. She finds a dress that she'd like to purchase and signs up to complete the transaction. Here are the details she provides:
Name:
Lisa Simpson
Email address:
[email protected]
Phone number:
123-547-9800 (same as her mother, as they share a mobile device)
Here's how we'll determine reachability for the new user, Lisa:
As discussed under Case 2, Lisa too will be reachable through the channels of
Push, In-app, Email
and
SMS.
As discussed under Case 1, Lisa too will be unreachable through
On-site
and
Web Push.
Now, let's delve deeper into the complexities that arise from the fact that both the users are using the same device and phone number:
Same device
Push notifications
will be sent only to Lisa as she is currently logged into your app. This means you will not be able to engage Marge until she logs into the app again (and Lisa logs out). Thus, at any given point in time, only one user can be reached through a device.
In-app messages
will be sent only to Lisa now. You will not be able to engage Marge through In-app as a different user is currently logged into the app.
Same phone number
SMS messages
for both, Marge and Lisa will be sent to the same phone number. In the case of generic messages meant for all users, they will receive the SMS twice.
We hope this equips you with a robust understanding of how the channel reachability of each user is detected across various stages of their lifecycle.
Now, let's get you acquainted with all the reachability metrics tracked for your users.
How Reachability is Calculated
Across your dashboard, the channel reachability of your users is indicated by two metrics:
1. Overall Reachability
It indicates the total number of users, out of a segment or your entire user base, that can be reached through at least one channel of engagement.
If a user can be reached through two or more channels then they are counted towards the
Overall Reachability
number/percentage only once to avoid any double counting of users.
2. Reachability
(for a channel)
This indicates the number of users, out of a segment or your entire user base, that can be reached through a particular channel.
If a user can be reached on more than one channel, then they are counted towards the
Reachability
number/percentage for all the respective channels they are reachable.
Let's go over a brief use-case to help you understand how these metrics are calculated:
👍
Use-case: Determining (Channel) Reachability and Overall Reachability of a Segment of Users
Let's assume that you have created a segment that contains 1,000 users at present.
The
Overall Reachability
of this segment is 700 users.
This means that the segment includes 300 users that cannot be reached through any channel of engagement.
The channel-wise
Reachability
of all the reachable users is as follows:
Push: 150
In-app: 75
SMS: 50
On-site: 100
Web Push: 500
Email: 350
Here, you will notice that if you added up the numbers, then the sum (1225) is higher than the
Overall Reachability
(700).
This is because users who are reachable on multiple channels, like
Web Push
and
Email
are counted towards the
Reachability
numbers of both the channels. But are counted towards the
Overall Reachability
number of the segment only once.
Both metrics are calculated over the entire lifetime of a user and are updated on a daily basis to factor in the reachability of new users and the changing channel preferences of the existing ones.
For the same reason,
Overall Reachability
and
(Channel) Reachability
cannot be analyzed for a particular time frame across your dashboard.
🚧
The Concept of Reachability is Applicable to the Following Sections in Your Dashboard:
User Overview
:
Amongst other metrics, this section also indicates the reachability of your entire user base against each channel, in real-time.
User Profile
:
For any user that has interacted with your app or website at least once, the platform creates a user profile. Amongst other vital details, the user profile also presents a detailed account of the user's reachability against each channel.
Segment Creation
:
When segmenting your users, you can choose to bucket them into micro-segments depending on the channels they can or cannot be reached on.
Segment Overview
:
Once you create a segment, using its Overview section you can analyze the reachability of all the users included in it to identify the most effective channels to engage them.
Engagement Overview
:
Using this section, you can analyze the reachability of your total user base for each channel, helping you identify the most effective channels to engage them.
Channel Overview:
Each channel listed in your dashboard comes with an Overview section which indicates the channel's reachability index, calculated against your total user base on a daily basis.
(
Push
,
In-app
,
SMS
,
Web Push
,
Email
,
WhatsApp
)
Journey Creation
:
When creating a journey, you can design the engagement strategy as per the reachability of users on various channels.
We hope this has equipped you with a comprehensive understanding of how
Channel Reachability
works in WebEngage. Please feel free to drop in a few lines at
[email protected]
in case you have any queries. We’re always just an email away :)
Updated
7 months ago
So, what's next?
Now, let's show you how you can leverage all the channels to engage your users across their lifecycle with various types of campaigns.
Campaigns and Its Types
Copy Page
