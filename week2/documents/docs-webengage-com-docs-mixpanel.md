# Mixpanel

- URL: https://docs.webengage.com/docs/mixpanel
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Partners Integrations
Mixpanel
Mixpanel
is a business analytics platform that provides real-time insights into app/website interactions and helps you devise effective marketing strategies. We've built an out-of-the-box integration with
Mixpanel
that enables you to export
Cohorts
as
Static Lists
in your WebEngage dashboard. This is ideal for:
Driving retention-led growth by activating dormant customers, promoting repeat purchases, driving platform engagement & content consumption.
Engaging cohort users with highly targeted & personalized messages through their preferred channel.
Pre-requisite
Mixpanel only exports
identified user profiles
to match to WebEngage - users without user profiles (i.e. anonymous users) will not export.
Hence, the exported users are properly mapped in WebEngage's system
only if the distinct_id in Mixpanel and the
user ID in WebEngage
have the same value
.
How to configure
This is a one-time integration and enables you to transfer Cohort user data from
Mixpanel
seamlessly to
WebEngage
as a
Static List
.
Here's how you can go about it:
🚧
Support for Personal API Keys will be discontinued soon. We recommend migrating to Service Accounts for continued API access.
Know more about
Service Accounts
.
Step 1: Get WebEngage REST API Key
As shown below, you can find your unique
API Key
by navigating to
Data Platform > Integrations
from the left panel. Scroll down to
REST API
and click
View
to access your credentials. Copy the
API Key
to proceed.
Click to enlarge
Step 2: Configure the API Key in the Mixpanel Dashboard
Navigate to
Integration
in your Mixpanel dashboard, select
WebEngage
and then select
Connect
.
Paste the WebEngage API key to save the configuration.
How to export a Cohort from Mixpanel to WebEngage
Select the cohort that you want to export. Click on the three-dot icon on the right side of the cohort.
Click Export to WebEngage. Select either one-time export or dynamic sync. Click
Start Sync
.
👍
Congratulations, you've successfully integrated WebEngage with Mixpanel :)
You can test the integration by exporting a test cohort from
Mixpanel.
The user list should appear under
List of Static Lists
in your WebEngage dashboard.
Sync types
This integration supports two types of exports: one-time export and dynamic sync.
One-Time Export
In a one-time export, Mixpanel sends WebEngage a static export of users who currently qualify for the cohort. The cohort data will not be updated in WebEngage after a one-time export.
Dynamic Sync
In dynamic sync, Mixpanel initiates sync between a cohort and WebEngage every two hours. The exported cohort will be updated every two hours to reflect the most recent list of users in a cohort.
When you generate a one-time export or dynamic sync, it overwrites the previous export with an updated export that reflects users who qualify for the cohort at the time of export.
How to export Events from WebEngage to Mixpanel?
On your WE dashboard navigate to the Data Platform tab, and Integrations sub-tab, and locate Data Destinations.
Choose Mixpanel and click on Configure.
Once you’ve been redirected to this page, click on the ➕button, and create your connection by providing the following details.
Connection Name: A name to identify this connection.
Project Token: you can obtain the project token by navigating to your Mixpanel dashboard settings > Project Setting > Access keys.
You can also edit your connection details by clicking on the action button adjacent to the connection on the listing page.
Once the connection is established you can now start exporting the events using this connection.
Navigate to the Data Platform tab, and Data Management sub-tab, and locate Data exports.
Click on the ➕, and provide the following information to establish the connection between WebEngage and Mixpanel.
Export Name: A name to identify the export.
Using Connection: In this drop down, you get to choose which partner’s connection you wish to use.
Export Events: You are provided with 3 options i.e. All Events, All Campaign Events, Selected Events Only,
Cadence: Choose a time span between ‘Near Real Time’, ‘Every 15, 30mins, 1, 6, 12, 24 hours’.
Click on ‘Save’.
Please feel free to drop in a few lines at
[email protected]
if you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
Let's show you how you can analyze the users you just exported from Mixpanel as a Static Segment.
Analyzing Static Segments
Copy Page
