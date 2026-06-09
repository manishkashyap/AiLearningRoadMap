# Custom Events

- URL: https://knowledgebase.webengage.com/docs/custom-events-management
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Custom Events
This section will guide you through the Custom Events section and how you can change the custom events' attributes.
Each
Custom Event
in WebEngage has
Event Attributes
attached to it that help you understand the user's preferences and motivations better. You can define
Custom Events
for all your app/web users to analyze, segment, and engage them with personalized experiences at scale.
Custom Events
are all the events that have been defined and passed by you to your WebEngage account, depending on your requirements. Custom Events can be anything that can help you track your user data more minutely. Depending on your industry vertical and business model, these events could be anything like,
Added to Cart, Course Purchase, Cart- Checkout, Free Trial Started, Lead Found, Music Played
and so on.
This section lists the
Custom Events
tracked for your users and enables you to
manage custom events
, while the
Event Attributes* Help you
identify tracking errors
,
stop tracking attributes
, and
change data type
- reducing dependence on your tech team!
Once you've integrated WebEngage with your apps & website, you can utilize the full potential of our
Customer Data Platform
by tracking the unique preferences and spending habits of each user as
Custom Events
. Depending on your industry vertical and business model, these attributes could be anything like, Added to Cart, Course Purchase, Cart- Checkout, Free Trial Started, Lead Found, Music Played* and so on. You can easily leverage all this data to:
Deliver contextual brand experiences at scale.
Engage users with highly personalized messages through their preferred channels.
Analyze users to identify their primary motivators and group them into highly differentiated segments.
Identify high-risk & dormant users to prevent churn.
Identify brand loyalists & high-spenders to fuel retention-led growth.
And much more!
How to Access
As shown below, you can access this section through
Data Platform > Data Management > Custom Events
in the main navigation panel of your dashboard.
Click to enlarge
Check Usage
At WebEngage, each event has an upper limit on the number of attributes you can have per data type. You can check the number of attributes currently utilized for each event by hovering on the info icon beside the event name.
Click to enlarge
Overview
Here you will find key details for each
Event
and
Event Attribute
tracked from all your sources - apps, website, REST API, third-party platforms, and manual data uploads.
Click to enlarge
Custom Events tab comprises of following 7 elements:
Events
Here you will find the list of all the
Custom Events
.
Event Attributes
for the particular event can be accessed through the drop-down sign next to
Events
. By default, only the event name is visible on the dashboard. However,
🚧
Please Note
Since the event attributes are passed by you, there can be chances of them being passed with the wrong data type. In this case, if the attribute will be visible by default along with the event's name.
Personally Identifiable Information (PII)
We understand your concerns regarding data security. This is why we've made it possible for you to mask the actual values tracked against each
Event Attribute
across your dashboard. You can do this by
marking crucial data points as
PII
(as highlighted below).
How PII Masking Helps Secure User Data
Only account admins who have permission to View PII will see and download actual values tracked against the marked event attribute. Values will remain hidden for all other admins.
Don't worry; this doesn't affect user analysis, segmentation, and campaign personalization in any way!
👍
Use Case: Marking Health Insurance Purchased as PII
Let's take the example of a Health Insurance Company that has a website and apps to track the user data to customize their marketing campaigns. Currently, the company is tracking their users in of the campaigns who have or are looking to purchase health insurance from them. The purchase value of each user through the
Currency, Plan Purchased, Sum Insured, Term,
and
Validity
. These are crucial business insights, which if leaked, can give your competitors insights into your users, revenue, and growth strategy.
With PII masking, you can ensure that such situations remain a distant nightmare!
Event Attributes
can be marked PII, which means that the attribute will not be visible to the team members who do not have access to view the functionality.
Click to enlarge
Data Type
Data types refer to the format in which you track the data points for a user against each Event Attribute. At WebEngage, you can pass event attributes in any of the following formats:
String:
Strings are a set of characters: alphabets, digits, blank spaces, punctuation marks, etc.
Number:
The integer data types are Numeric values.
Date:
Date shows the value of the date in the format:
YYYY-MM-DDTHH:MM: SS.000Z.
Boolean:
Boolean can be either True or False, depending on the attribute.
Array:
An array is a collection of elements (values or variables), each selected by one or more indices computed at run time during the execution of a program.
Map:
Allows you to create and track values of multiple event attributes in one go, as
Key-Value pairs
. Here the
Key
is an
Event Attribute
, and
Value
is the actual data point tracked for a user, a
String, Number, Date, Boolean, or Array
.
Click to enlarge
Data Source and Tracking Status
Click to enlarge
Source gives an idea of which source the data is collected from. The source is divided into Website, Android, iOS, and Others (REST API, server data from Segment.com). Under the source columns, the data collected status is shown in the form of color-coded signals.
👍
Understanding How Tracking Status Works
Only the last four hours of data is considered because one web page or app may send the attribute in some data type to another page or screen in another data type. In this case, the signal will keep toggling red/ green over and over again. Hence, a window of 4 hours to correct any error that might be there.
Only the latest version of the app is considered for the data. If a new version of the app is released after correction, then the new app version overrides the previous error, and the status is reported only for the latest version.
Tracking Status
It indicates whether you're receiving data for an attribute through the respective data sources in real-time! You can easily turn off tracking for an attribute and activate it later, as per your needs.
Let's walk you through each status:
Status
What It Means
Success
(
Green
)
Actively receiving correct data from the
Source
.
Error
(
Red
)
Incorrect data has been received in the last 4- hours.
It is important to note the only the latest version for apps is considered for status tracking. If the error has been rectified in the 4- hour window, it will turn green when the window ends; else, it will remain red for the next 4- hours.
If multiple reds are recorded, kindly consider the latest error to figure out when the four-hour window starts.
Stale
(
Orange
)
The data was received for the attribute that was received more than 2 days ago.
Stopped
(
Light Grey
)
A marketer has the choice to turn off tracking for any attribute. Hovering over it will show you the date and time when it was stopped from tracking.
No Data
(
Dark Grey
)
It shows that no attribute was ever received for that data from the source.
🚧
Please Note
The Source applies to both
Event
and
Event Attributes
. If the event is recorded and the event attributes have an error in the data types, then the tracking status of the
Event
will indicate 'Error' in red for that source unless no event data is recorded for that source in the last 2 days.
1. Website
Indicates the tracking status for all
Event
and
Event Attributes
gleaned through the
Web SDK
or
GTM integration
. This includes data from
AMP pages
and Segment.com's Device Mode integration.
2. Android
Indicates data tracking status for all
Event
and
Event Attributes
gleaned through all your Android apps where the
WebEngage's Android SDK
is present. This includes data from all hybrid apps built on Cordova, React Native, Flutter, Xamarin, Unity, and Segment.com's Device Mode integration.
3. iOS
Indicates data tracking status for all
Event
and_Event Attributes_ gleaned through all your iOS apps integrated via the
WebEngage's iOS SDK
. This includes data from all hybrid apps built on Cordova, React Native, Flutter, Xamarin, Unity, and Segment.com's Device Mode integration.
4. Others
Indicates tracking status for all
Event
and
Event Attributes
gleaned through your REST APIs, Segment.com's Cloud Mode integration, and user data created through manual CSV upload.
Managing Custom Events
Depending on your business needs, you can choose Stop (and later Start) tracking a specific
Event
from all your data sources
(apps, website, server, third-party integrations).
Here's how you can go about it:
Click to enlarge
Stop/Start Tracking Data
There are several instances where you may want to stop tracking an
Event
, like:
Your app/website was updated, rendering specific sections (and the data tracked for them) redundant.
You are tracking an event's value via another
Event,
in a different format.
📘
Important
When you Start/ Stop tracking the
Event
, all the
Event Attributes
attached to it, starts/ stops tracking.
How It Works
Stopping data tracking enables you to reduce the data clutter across various sections of your dashboard, helping you retain only the most relevant data points for segmentation and message personalization.
You can stop tracking events only if they are not attached to a
Campaign, Journey, Relay, Segment, or Funnel.
If you'd like to stop tracking an event currently in use, you will need to delete the respective
Campaign/ Journey/ Relay/ Segment/ Funnel
before proceeding. This process has been put in place to preserve the sanctity of your data and ensure that all your engagement strategies keep running smoothly.
Currently, you cannot choose to stop data tracking for a specific platform. This means that if you're tracking an Event for your Android, iOS apps, and website, we will stop receiving the attribute from all 3 platforms.
We recommend that you collaborate with your tech team to stop tracking data for a specific platform.
Once stopped, the event will be made unavailable for use across your dashboard. Don't worry; you can always start tracking an event if you'd like to use it in the future!
The event will still be listed under
Events
with the
Status, No Data
(indicating that you've stopped tracking it).
👍
Use Case: Stop Tracking an Event
Let's assume that you are an E-commerce website and want to turn off tracking for one of the
Event
called
Sort Applied
since an updated event
Product Sort
has been added.
Sort Applied
becomes a redundant event and tracking the same serves no purpose.
You can start/ stop tracking an event as per your requirement.
As shown below, select
Stop Tracking
from the
Actions menu
against the
Sort Applied
event to implement the change.
Click to enlarge
You will be prompted by the following message if we're unable to execute your change 👇
Click to enlarge
However, if you wish to start tracking the event again, you can do by following the steps. As shown below, select
Start Tracking
from the
Actions menu
against the
Sort Applied
event, and make it available across your dashboard.
Click to enlarge
Managing Event Attributes
Depending on your business needs, you can choose to:
Mask the event attribute values.
Change the data type tracked against each attribute.
Stop (and later Start) tracking a specific event attribute from all your data sources
(apps, website, server, third-party integrations).
Here's how you can go about it:
PII Masking
As shown below, you can hide the value of an attribute across your dashboard and reports by selecting
Mark as PII
from the
Actions
menu.
(How It Works)
*
Click to enlarge
You can unmask a PII attribute anytime you like by selecting
Mark as Not PII
from the
Actions menu
(as shown below).
Click to enlarge
Change Data Type
You can edit the data type of the value tracked against a
Event Attribute
directly through your dashboard. Doing so will help you utilize the data more effectively when personalizing campaigns.
Once updated, the existing data tracked for all users will be deleted and replaced with the new values, as per the new format.
🚧
Please Note
You can change the data type only if the attribute is not a part of a
running Campaign, Journey, Relay, an Active Live Segment, or Funnel.
As long as the attribute is attached to either one, you will not be able to edit its data type.
Here's how you can go about it:
Click to enlarge
In cases where the
Event Attribute
is still in use, you will be prompted by the following message:
Click to enlarge
Stop/Start Tracking Data
There are several instances where you may want to stop tracking an Event Attribute, like:
Your app/website was updated, rendering specific sections (and the data tracked for them) redundant.
You are tracking an attribute's value via another
Event Attribute,
in a different format. Let's help you understand this better with an example.
👍
Tracking a User's Added to Cart Event Attribute
Every time your user makes a purchase, the following attributes of the event
Added to Cart
are tracked as well:
Cart ID
Cart Value
Cart Size
Cart Category
There can be instances where you would want to stop tracking certain attributes if they have become redundant, you have updated your app/ website, or for any other reason. You can turn off the tracking of certain event attributes so that your data does not become redundant.
This way, you can reduce the number of Event Attributes being used to track a data point and easily personalize messages.
How It Works
Stopping data tracking enables you to reduce the data clutter across various sections of your dashboard, helping you retain only the most relevant data points for segmentation and message personalization.
You can stop tracking and event attributes only if they are not attached to a
Campaign, Journey, Relay, Segment, or Funnel.
If you'd like to stop tracking an event attribute currently in use, you will need to delete the respective
Campaign/ Journey/ Relay/ Segment/ Funnel
before proceeding. This process has been put in place to preserve the sanctity of your data and ensure that all your engagement strategies keep running smoothly.
Currently, you cannot choose to stop data tracking for a specific platform. This means that if you're tracking an Event Attribute for your Android, iOS apps, and website, we will stop receiving the event attribute from all 3 platforms.
We recommend that you collaborate with your tech team to stop tracking data for a specific platform.
Once stopped, the event attribute will be made unavailable for use across your dashboard. Don't worry; you can always start tracking an event attribute if you'd like to use it in the future!
The event attribute will still be listed under
Event Attributes
with the
Status, No Data
(indicating that you've stopped tracking it).
Stop Tracking
As shown below, select
Stop Tracking
from the
Actions menu
of the respective
Event Attribute
to implement the change.
Click to enlarge
You will be prompted by the following message if we're unable to execute your change 👇
As shown below, select
Start Tracking
from the
Actions menu
to activate the
Event Attribute
and make it available across your dashboard.
Click to enlarge
Updated
4 months ago
User Profile Attributes
Revenue Mapping
Copy Page
