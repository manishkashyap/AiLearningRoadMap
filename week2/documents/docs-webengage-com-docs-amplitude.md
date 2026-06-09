# Amplitude

- URL: https://docs.webengage.com/docs/amplitude
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Partners Integrations
Amplitude
Amplitude is a business analytics platform that provides real-time insights into app/website interactions and helps you devise effective marketing strategies. We've built an out-of-the-box integration with Amplitude that enables you to export Cohorts as
Static Lists
in your WebEngage dashboard. This is ideal for:
Driving retention-led growth by activating dormant customers, promoting repeat purchases, and driving platform engagement & content consumption.
Engaging cohort users with highly targeted & personalized messages through their preferred channel.
Considerations
Keep these things in mind when sending Cohorts to
WebEngage
:
You must enable this integration in each Amplitude project that you want to use it in.
You need a paid WebEngage plan to enable this integration.
Amplitude matches the user_id to the CUID within WebEngage to associated events. If a user with that ID does not exist within WebEngage, a user will not be created. Ensure the Amplitude
user_id
field matches the WebEngage CUID field to avoid user duplication.
Prerequisites
To configure your Cohort integration from Amplitude to WebEngage, you need the following information from WebEngage:
API Key: To start sending data into WebEngage, you first have to get your WebEngage API Key. See the WebEngage documentation for more help.
How to Configure
Go to your Amplitude account to access the
Data tab
.
Navigate to
Connections
and click on
Destinations
.
Add a new destination by clicking on the
+Add Destination
button.
Search for
WebEngage
in the search bar.
Enter a name for your Cohort and input your WebEngage API key. Click on
Save
to complete the setup.
🚧
Support for Personal API Keys will be discontinued soon. We recommend migrating to Service Accounts for continued API access.
Know more about
Service Accounts
.
How to export a Cohort from Amplitude to WebEngage
Select a Cohort and click on the
Sync To
button.
Select WebEngage as your destination.
Select the frequency of the sync.
The Cohorts are exported as Static Lists. You can navigate to your Cohorts by clicking on
Lists
under the
Segments
section of the WebEngage dashboard.
The
Source
of the exported list will be Amplitude, and the
Type
will be Static.
How to export Events from WebEngage to Amplitude?
On your WE dashboard navigate to the Data Platform tab, and Integrations sub-tab, and locate Data Destinations.
Choose Amplitude and click on Configure.
Once you’ve been redirected to this page, click on the ➕button, and create your connection by providing the following details.
Connection Name - A name to identify this connection.
API Key - API key which is available in Amplitude dashboard. (Amplitude Dashboard > Settings > Org Settings > Projects > API Key)
Data Residency: choose the server you want to save this.
You can also edit your connection details by clicking on the action button adjacent to the connection on the listing page.
Once the connection is established you can now start exporting the events using this connection.
Navigate to the Data Platform tab, and Data Management sub-tab, and locate Data exports.
Click on the ➕, and provide the following information to establish the connection between WebEngage and Amplitude.
Export Name: A name to identify the export.
Using Connection: In this drop down, you get to choose which partner’s connection you wish to use.
Export Events: You are provided with 3 options i.e. All Events, All Campaign Events, Selected Events Only,
Cadence: Choose a time span between ‘Near Real Time’, ‘Every 15, 30mins, 1, 6, 12, 24 hours’.
Click on ‘Save’.
Use Cases
Exporting user or behavioral-based Amplitude cohorts to WebEngage enables you to:
Drive retention-led growth by activating dormant customers.
Promote repeat purchases.
Drive platform engagement & content consumption.
Engage cohort users with highly targeted & personalized messages through their preferred channels of engagement.
Updated
7 months ago
Mixpanel
AWS S3
Copy Page
