# Refreshing Lists

- URL: https://knowledgebase.webengage.com/docs/refreshing-lists
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Refreshing Lists
Refreshing Lists
refers to a type of list that you can update or reload either by manually triggering a refresh action or by setting a periodic schedule i.e. daily, weekly, monthly, for automatic refreshing. The purpose of this refresh is to update the content of the list based on any changes that may have occurred since the last time it was loaded.
📘
Note
Static Lists will here after be known as 'Lists' in the navigation bar of your dashboard.
How It Works
Refreshing list
acts as a connection or bridge between Static Lists and Live segments. It allows you to update the content of your lists daily, weekly or monthly as per your choice, either manually or periodically, to bring in the latest information from the live segment.
• You can engage the user pool of a Refreshing List with highly personalized
One-time,
Triggered
, and
Recurring campaigns
through
Push
,
SMS
,
Web Push
,
Email
, and
WhatsApp
.
• Given their unchanging nature, Refreshing user Lists lack real-time context and cannot be used to run Relays or deliver Transactional Campaigns. Their usage is heavily restricted for building Journeys and can be used only for triggering a Journey experience for users who are already in the Segment.
• Currently, you cannot export Refreshing Lists to your Facebook Business and Google Adwords accounts to run targeted ad campaigns. We'll soon make this possible for you!
Creating Refreshing Lists
You can start creating your Refreshing Lists by navigating to 'Lists' under 'Segments' in the navigation panel.
From here use the following steps to start creating your Refreshing Lists.
• Step 1:
Start by clicking on the ➕ the 'Lists' page.
• Step 2:
After which you will be presented with 2 option, i.e. 'Create List using Criteria' and 'Create List using CSV File'; by clicking on the
'Create List using Criteria'
option you can start with creating your Refreshing Lists.
• Step 3:
Provide a name to the Refreshing list that you are going to create and a 'Refresh Frequency' ranging from 3 options i.e. daily, weekly, monthly.
Option 1:
When you select
'daily' refresh
option you will be presented with the options to select time when the List is to be refreshed.
Option 2:
When you selects the
'Weekly' refresh
option, the option to select the days of week along with the time will be visible.
Option 3:
When you select the
'Monthly' refresh
option, then a dropdown to select days of a month ( from 1st of Month to 28th of Month) along with the time for the same.
📘
Keep a note
If you don't set the refreshing frequency while creating the List, the list created will be classified as a static list. You can make a static list as refreshing list by setting a refresh frequency for the list.
• Step 4:
Start by setting the users for your Refreshing Lists from the dropdown with the options: 'All Users', 'New'. 'Returning Users' and 'No. of Sessions'.
• Users (Optional):
You can also further criteria on the users for your list, by adding filters for
'Last Seen', 'Created On', 'Geo filtering', 'User Attribute', 'First Acquisition Source', 'User Ids', 'Reachability', 'Intelligent Attributes'.
• Behavioural (Optional)
: You can also add behavioural filters i.e.
‘Users Who Did These Events’, ‘Users Who Did Not Do These Events’
• Technological (Optional)
: You also have the option to add technological filters such as choosing from 'Android', 'iOS' and 'Web'; each of which have the following options to use as sub-filter.
👍
Note
Creation of criteria for the refreshing list remains same as static list.
• Step 5:
Once you have done setting up all of the above-mentioned steps save the list by clicking on the
'Save'
button on the top right corner of the page.
Editing Refreshing Lists
The List criteria in the Refreshing List cannot be changed. You
can only change the refresh frequency
but will
not be able to change the definition
.
You can start editing your refreshing lists in 2 ways
•
Option 1:
Either from List page by clicking on the three dots adjacent to the list you would like to edit.
•
Option 2:
Or on the List Overview page by clicking on the list you would like to edit and then clicking on the 🖊️.
🚧
You will be only able to edit the List name and refresh frequency. This is done to keep the context the same.
The List criteria will be in read-only format and you will not be able to make any changes to only the Name and refresh frequency.
Deleting a Refreshing List
📘
Disclaimer
You cannot delete a refreshing list if it is being used in any campaigns, journeys or relays. So if you wish to delete these refreshing list you need to first unselect them from the campaigns journeys etc and then delete the same.
You can delete a refresh list by two methods.
By clicking on the delete option adjacent to the list you want to delete on the listing page. (OR) on the list overview page by clicking on the 🗑️.
After which you will be shown an alert pop-up stating that the deletion of the list is irreversible and you will not be able to use it in campaigns, journeys etc. anymore.
Live Segment vs. Refreshing List: Understanding the Differences
Refreshing Lists
Refreshing Lists allow you to segment users based on their attributes or behaviors (events). As the name suggests, the list updates and refreshes itself at regular intervals. You can set the refresh frequency to daily, weekly, or monthly, depending on how often you need the list to update.
Example:
Last 7 Days Purchasers:
You can create a Refreshing List that segments users who have made purchases in the last 7 days. By setting the refresh frequency to Daily, the list will evaluate users every day, ensuring that users who have made a purchase within the last 7 days either enter or remain on the list. Users who no longer meet the criteria will be removed.
Live Segment
Live Segments also segment users based on their attributes or behavior, but with one key difference: the evaluation is done in real-time. Whenever a user performs an action or updates an attribute, the segment is evaluated immediately. This makes Live Segments ideal for triggering real-time actions, such as in-app notifications or immediate follow-ups.
Example:
App Uninstall Trigger:
You can create a Live Segment to capture users who uninstall your app. As soon as a user uninstalls the app, they are immediately added to the Live Segment, allowing you to send an offer or prompt to reinstall the app in real-time.
Loan Tab Visits:
Suppose a user visits the "BORROW (Loan)" tab on your app. A Live Segment can instantly add them and trigger an action, like sending an in-app message or redirecting them to a support agent for assistance.
Key Differences
The primary difference between Live Segments and Refreshing Lists is timing:
Live Segments: Users enter the segment as soon as they meet the criteria. This real-time evaluation is ideal for immediate actions.
Refreshing Lists: Users are added or removed based on a scheduled evaluation (daily, weekly, or monthly). This is suitable for non-urgent use cases.
Brewing Process
The brewing process is a unique aspect of Live Segments. It involves identifying users who qualify for the segment and marking them accordingly, ensuring real-time actions can be taken. This brewing process takes time, approximately 20x longer than creating a Refreshing List, because it prepares the system for immediate user actions.
When Live Segments are Unavoidable:
Live Segments are necessary for real-time, immediate actions where timing is critical. Some key use cases include:
On-Site Notifications
On-Site Feedback & Surveys
Near Real-Time Journeys, such as:
App Uninstall Recovery
Loan Application Intent (triggering call center support)
Advantages of Refreshing Lists over Live Segments
If your use case doesn't involve real-time actions, a
Refreshing List
is a more efficient option. Using a Refreshing List can save you time by avoiding the brewing process.
You should opt for Refreshing Lists when:
Sending
outbound campaigns
(one-time or recurring).
Counting users
based on certain criteria.
Running
journeys
that aren’t time-sensitive and can wait a day for updates.
Example:
Weekly Purchasers:
For campaigns like weekly promotional emails, where real-time updates aren’t necessary, a Refreshing List set to weekly would work perfectly.
Updated
7 months ago
Analyzing Lists
Predictive Segments
Copy Page
