# FAQ

- URL: https://knowledgebase.webengage.com/docs/app-in-line-faq
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

FAQ
Commonly asked questions related to App In-line campaigns
Basics
1. What is App In-line Personalization?
App In-line Content
allows you to create dynamic campaigns that appear native to the app and enable you to run personalized campaigns without interrupting the user experience. It also allows you to manage (Run/ Edit/ Stop) the campaigns and such native in-line campaigns do not require any app updates.
2. How is it different from In-app Notification?
App In-line Content
differs in a way that it is native to the app, unlike the
In-App Notification
. In simple words, App In-line Content appears like any normal content (Banner/ Text) that is a part of the screen. The App In-line Content can be highly personalized and the best part is they don't interfere with the normal user experience on your app.
Pre-requisites
1. What are pre-requisites for App In-line campaigns?
Before you start creating
App In-line
campaigns, there are some pre-requisites:
Integrate the WebEngage Personalization SDK for both
iOS
and
Android
.
Create Properties for your app.
Register the Properties with WebEngage.
📘
Please Note
WebEngage currently supports App In-line only for Native Android and Native iOS.
2. What are properties?
Properties
or
Property IDs
are the predefined placeholders on the app's page/ screen to run your campaigns. Properties allow users to create display ads that look native to the app and enable them to run personalized campaigns on the app to help achieve their use cases without hindering the end user’s experience. To know more about properties,
click here
.
3. Is it necessary to create Properties to run App In-line?
Yes, it is. You will not be able to run In-line campaigns if
Properties
are not created.
4. What type of campaigns can I run with App In-line
With App In-line, you will be able to run
Text, Banner, and Custom
campaigns.
Text
Text Layout allows you to add only text along with basic styling and adding buttons for your App In-line content.
Banner
Banner Layout consists of an image addition option with basic styling and adding buttons for your App In-line content.
Custom
The custom Layout option gives you the flexibility of creating your own custom layouts that match your application theme.
Implementation
1. How can I match the UI of these campaigns with my App UI?
WebEngage allows you to create your own layout through Custom Views. This means the entire onus of UI (its look and rendering) for such campaigns is managed by your App while WebEngage will be passing you the personalized data for your campaign.
2. Do I need to do extra implementations to use Custom View?
Yes. Since WebEngage provides template to create Text and Banner layouts, Custom View is an option that allows you to go beyond Text an dBanner layouts and create your own personalized view.
To render Custom View, kindly get in touch with your tech team. To track the stats of the same, you will have to add a bit of extra code for
iOS
and
Android
.
3. Are there any limitations on running this type of campaign?
Some limitations on running App In-line campaigns:
App In-line is not supported on
Recycler View, Table View, and Collection View
.
If the same Property IDs are on the same screen multiple times, the campaign will run only on the first one.
Currently, Static lists are not supported for App In-line content.
4. What is the set timeout field?
It is the time limit for the campaign to render. If campaign rendering takes more than the set time, the campaign will not be shown.
5. Why did my campaign not show up/ render?
There can be multiple reasons for the campaign not to show up on the screen.
Please make sure the
Property ID
added on the WebEngage dashboard exactly matches with the one added in the app.
The user did not qualify for the campaign based on the segment targeted.
The
Event
did not get triggered
Set timeout value might need to be increased.
You refer to
this
doc to understand reasons for campaign failure
Kindly reach out to
[email protected]
for further assistance.
6. Why
Custom View
stats are not getting tracked?
To track the stats of the
Custom Views
, you will have to add a bit of extra code for
iOS
and
Android
.
7. How can I set priority for the multiple App In-line Content campaigns eligible for the same users?
Firstly you can prioritise the campaigns within properties. There are 2 ways to access this feature from the ‘Properties’ page of App In-line Content: Click on the actions dropdown menu of any running or upcoming campaign and select the ‘Prioritize campaign for this property’ option OR Select a property, Click on the ‘Prioritize Campaigns’ beside the edit icon on the top bar. Once you are in the priority modal Click on ’Reorder’, Drag and drop the campaign that you would like to reorder and Click on ‘Save’.
8. If I have not set any priority, what would be the default priority set for my campaigns?
By default within a property, all the journey and relay campaigns (if present) will be listed together in the top priority bucket and all standalone campaigns will be listed together in the next priority bucket.
9. Can I reorder/edit the campaign priority as often as I like?
Yes, you can reorder/edit the campaign priority as often as you like as long as you have campaign maker or campaign checker permissions.
Updated
7 months ago
Analyzing App In-line Overview
Audit Log
Copy Page
