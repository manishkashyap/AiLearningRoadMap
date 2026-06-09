# Analyzing Events

- URL: https://knowledgebase.webengage.com/docs/analysing-events
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Analyzing Events
A walkthrough of how you can analyze user behavior in your dashboard
🚧
Must Read
Please ensure that you have a robust understanding of all the concepts related to
Events and Event Attributes
before proceeding. Doing so will help you understand the working of this section better.
First Impression
The default view of this section has been designed to show you a top-level view of all the custom events performed by your users over the last 7 days, in descending order.
Click to enlarge
Each event can be examined in greater detail by selecting their respective bar graphs.
On doing so, you will be shown a day-wise breakup of total user activity.
The results can further be refined by adding values to the fields of the query bar placed on top.
A Hands-on Analysis
Let's demonstrate a use-case to help you get acquainted with the workings of this section.
👍
Use-case
Let's say that you run an international e-commerce business and want to analyze the top locations contributing to purchases over the previous week. For this, we'll analyze the event
Checkout Completed
- which represents purchase in the user's lifecycle.
All we need to do is;
Select the event,
Checkout Completed
Select
Country
as the first dimension in the field
Over
Hit enter!
Click to enlarge
As you can see
Checkout Completed
has been performed by a majority of users based in Kazakhistan.
Now, let’s dig deeper to find out which city of
Kazakhistan
has contributed to maximum purchases.
For this, we’ll select the bar graph of
Kazakhistan.
Doing so will automatically change the value in the field
Over
, from
Country
to
City
, adding
Country = Indonesia
as an attribute filter to the event,
Checkout Completed
.
Click to enlarge
Now, that we have insights into the top cities, let’s find out the popular operating systems which have been used to purchase the products. All we need to do is add
OS Name
to the field
Split By
and hit enter!
Click to enlarge
There you have it - all purchases made over the last 7 days, from the various cities of the top country,
Kazakhistan
, split by
OS
of the devices used to make the purchase.
👍
Results
A majority of active users were located in
Astana, Kazakhistan
and preferred using
Windows devices
over the previous week.
Similarly, you can slice-and-dice all kinds of behavioral data to gain specific, actionable insights.
Understanding features of the event analysis section
Now that you've got the hang of how this section works, let’s deep dive into its features to help you gain maximum insights:
Step 1: Select the Date Range
Using the date range filter placed on the top right, you can specify a period for which you want to analyze user behavior. The default period has been set to,
Last 7 days
.
Click to enlarge
When you notice a recurring decline in analytics, it is often a result of reduced user activity over the weekends, specifically on Saturday and Sunday. To aid in a more thorough analysis of your data, you can click on the checkbox for the "
Highlight Weekend
" option. This will accentuate weekends on the graph, providing valuable insights into your data patterns.
Step 2: Select Show (Occurrences or Uniques)
As discussed under,
How are Events Calculated for Analysis?
,
there are two ways in which we calculate the number of times users perform an event;
occurrences
and
uniques
.
As shown in the visual below, either option can be selected from the drop-down nested under the field,
Show,
depending on your analytical needs.
Click to enlarge
To understand the impact of selecting either option, better, let's demonstrated a small use-case.
👍
Use-case: Analysing Occurrences / Uniques
Let’s assume that you run an e-commerce website and would like to find out the average number of times a user viewed product pages over the previous week.
For this, we'll do a quick,
occurrences / uniques
calculation for the event,
Product Page Viewed
, for
Last 7 days
.
Here we can see that
Occurrences
for
Product Page Viewed
equals 72,413 times for the
Last 7 days
.
Click to enlarge
But when viewing
Uniques
, we see that
Product Page Viewed
was performed by 6,269 users over the
Last 7 days
.
Click to enlarge
👍
Results
Hence, now we know that on average, a user viewed 9 product pages over the previous week.
Step 3: Select the Event
Next, define the event you'd like to examine by choosing an event or a set of events from the dropdown nested under the field,
Of
.
Click to enlarge
Multi Event
allows you to gain a more in-depth understanding of how events may coincide or affect each other by plotting and comparing multiple events to visually spot any correlation between events.
The drop-down includes all the system events, campaign events and custom events tracked for your account. All the system event and campaign events pre-defined by us are
listed here
for reference.
🚧
Using Split-by
The Split-by option will only be applicable while analyzing a single event.
Step 3.1 : Apply Attribute Filters to the Event
You can further narrow down the scope of the event by adding attribute filters to it. This can be done through the filter icon placed next to the field,
Of
.
Click to enlarge
On clicking the icon, you will be prompted with a modal, allowing you to apply several attribute filters. Each field comes with a drop-down, including only those attributes which can be applied to the selected event.
📘
The following event attributes are included in the dropdown options:
Time
(Event Time)
Location
(City, Country)
Technology
(OS, Device, Browser Name, App Version)
Marketing
(Channel, Campaign Source, Campaign Medium, Campaign Name)
Screen
(Page URL, Screen Name)
Custom Attributes
(Only when a custom event is selected)
Miscellaneous/ Other
(Session Count, API Version, Language)
Now, let's walk you through this in detail.
👍
Use-case 1: Applying One Attribute Filter
Let’s say that you want to analyze the event,
Cart Viewed
only for a set of users whose cart value exceeds $1,000. For this, we'll simply apply
Cart Value
as a filter.
Here's how you can go about it:
Click to enlarge
Step 1:
Select the event,
Cart - Viewed
Step 2:
Click the filter icon
Step 3:
Apply the attribute,
Cart Value
as a filter using the drop-down on the screen
Step 4:
Further define the scope of the event by limiting the
Cart Value
as
greater than 1000
Step 5:
Click
Apply
to view results!
👍
Use-case 2: Applying Multiple Attribute Filters
Let’s take the example of a custom event;
Product Viewed
, and add the following attributes to it for our analysis;
Product Name:
Puma running pants
Page URL:
/
www.companyname.com/women/pants
Country:
US
OS:
iOS
Now let’s show you how to apply these attribute filters to the event, using the AND-OR logic.
Click to enlarge
Method 1: Using the AND logic to club attributes filters
If we use the AND logic to apply all the attribute filters listed above, then your analysis will be limited to a set of users who have
only viewed Puma Running Pants, AND on the page,
www.companyname.com//women/pants
AND are from the US AND use an iOS device.
Implications:
So, using the AND logic to club event attributes you can narrow down the scope of analysis to a particular set of users whose actions fall in line with a sum of all the attributes.
Method 2: Using the OR logic to club attributes filters
If we use the OR logic to club and apply all the attribute filters listed above, then your analysis would include a broader set of users who have
either viewed Puma Running Pants OR have visited the page
www.companyname.com/women/pants
OR have viewed any Product Page from the US OR have performed the event on an iOS device.
Implications:
So, using the OR logic to club event attributes you can broaden the scope of analysis by including users whose actions fall in line with any one of the attribute filters.
Hence, when using the OR logic, we suggest that you broaden the user base by clubbing related parameters together. For example, including the last two attributes;
Location
and
OS
, doesn't help us gain any valuable insights as these parameters are unrelated to
Product Name
and
Page URL
.
Lastly, you can always hit the
Reset Button
to remove all the attributes and start again.
🚧
Note:
It's not possible to add attribute filters when analysing
All System Events
or
All Custom Events
as the attributes which can be applied to each event, vary.
Step 3.2 : Advanced Filters
With these advanced filtering options you can now apply filters to all the events that you are analyzing. Some of these advanced filter options are:
User Attributes Filter
: These refer to specific characteristics or traits associated with users, and they serve as customizable filters that can be employed to refine and narrow down the focus of analysis across all events within your dataset.
Common Filter
: These denote the shared attributes present across all events under analysis, exclusively relevant when multiple events are being analyzed.
Individual Event filter
: Distinct filters assigned to each of the selected events, allowing for specific and tailored adjustments or restrictions to be applied independently to each event within the chosen set.
Segment Filter
: You can apply filters on specific segments of users and the event analysis will be done only on these users. This feature helps you narrow down search results based on specific criteria, enhancing efficiency in sorting through extensive datasets or product catalogs. It provides two options: Include Segments and Exclude Segments, each offering 'User in ANY of these segments' or 'User in ALL of these segments' to precisely customize results according to user needs.
Step 4: Select the Dimension(s) for Analysis
The next step is to define the dimension(s) against which you'd like to analyze the event. The query bar has been designed to facilitate in-depth behavioral analysis by combining an exhaustive list of pre-defined parameters.
Click to enlarge
Using the dropdowns nested under the fields,
Over
and
Split By
, you can combine up to two parameters to slice-and-dice your data.
📘
Dropdown options in both fields include the following event attributes:
Time
(Days, Weeks, Months)
Time Block
(Hours of Days, Days of Week, Months of Year)
Location
(City, Country)
Technology
(OS, Device, Browser Name, App Version)
UTM Parameters
Screen
(Page URL, Screen Name)
Engagement ID
(ID of Campaign/ Journey)
Custom Attributes
(Only when a custom event is selected)
In case you'd like to analyze an event against one dimension, leave the field,
Split By
blank, and hit enter.
🚧
Note:
When analysing
All System Events
or
All Custom Events
, the field,
Over
gets deactivated automatically. This restriction has been put in place to avoid a chaotic display of insights.
Hours Granularity
Events can be analyzed on an hourly basis. To achieve this you can navigate to the ‘Over’ dropdown, where you can find ‘Hour’, by selecting this the graph that is produced will have hours on the X- axis. After which you can find the date and time (AM/PM format) on the X axis.
This hour level granularity can be used with a period of 31 days i.e maximum of one month, if you try to increase the number of days beyond 31, the ‘over’ option switches to the day option automatically along with an error.
For last 7 days
For Last 30 days
Step 5: Select the Format of Visualisation
Lastly, while
Bar Graph
has been set as the default format of visualisation, you can change this to a
Line Graph
or a
Table
, using the overflow menu placed on the top-right.
Click to enlarge
Actionable Event Analytics
Event analytics provides insights into your users behaviour, this becomes an important point where you can discover a segment of your users, for whom you would want to create a list for.
Additionally, you will be able to preserve an event analytics search or query as a list (Static and Refreshing Lists). This list may be for a single event or a collection of related events. Which can be further used to engage users by sending segmented campaigns.
How it works?
Imagine you are doing analysis over a specific set of events and wish to create a list of users who did a particular event on a particular day. Now you will be able to export users list for a specific date or user list for over a period of time.s,
You can do this by clicking on the Zoom In option when you hover over the event you are analyzing.
Lets understand 2 ways of creating List.
You can start by choosing between
Data Point or Series
:
For
Data Points
:
The data point through which you selected the option to create a list, will be selected by default.
The order will be the same as the way it is shown on the graph.
You can also select all the data points.
For
Series
:
The series through which you selected the option to create a list, will be selected by default.
The order will be the same as the way it is shown on the graph except, for “Others”, they should be anchored at the bottom and should be unselected.
You can also select all the series.
Let us consider a scenario where you choose to analyze the data points of an event. And walk through the steps of creating a list from event analytics.
Step 1:
You can now proceed with filling up the name of the list you want to create.
Step 2:
Now choose from the type of list i.e.
Static or Refreshing
.
Static:
A one time list, where users will not receive them again and are used for executing campaigns for a small group of users, these are ideal for running one-off campaigns where your end goal is to invoke immediate action like user activation, conversion, registration, or convey a personalized message. Click
here
to know more.
Refreshing:
refers to a type of list that you can update or reload either by manually triggering a refresh action or by setting a periodic schedule i.e. daily, weekly, monthly, for automatic refreshing. Click
here
to know more.
📘
Keep a note
Refreshing list cannot be created with existing refreshing list as filters.
Step 3
: If you’ve chosen the Refreshing lists option, Last ‘x’ days.
For
Refreshing Type
, text will be displayed with the last X days and number of days are editable in the future.
Step 4: Selecting Refreshing Frequency:
: A refresh schedule, similar to the one we have for the refreshing segment, to refresh the lists in every time period such as daily, weekly, or monthly.
Once the above fields have been filled, you can now proceed to selecting the data points or series from the table below.
👍
Use Case
User Onboarding Optimization
:
Use case brief
: Track user onboarding touchpoints, including account creation, profile completion, tutorial views, and feature interactions. Access a comprehensive view of the onboarding process, enabling a nuanced understanding of user interactions.
Impact
: Granular insights allow for targeted improvements to the onboarding journey, resulting in a smoother user experience.
Product Feature Adoption:
Use case brief:
To track the adoption of specific product features, combine multi-event analytics with segment and static list filters. By analyzing events related to feature usage and creating segments based on user behavior, tailor communications sent to different user groups. User attributes can further refine this targeting.
Impact:
A personalized approach to promoting features, increasing user engagement, and driving feature adoption.
User Engagement Journey Mapping
Use case brief:
Identify key touch points, behaviors, and preferences in the user journey; user attributes further refine insights. Export this data to allow for a comprehensive understanding of the user journey.
Impact:
Informed decision-making, personalized marketing strategies, and an improved overall user experience.
Step 5:
Click on Create List to save the list
Once the lists have been saved, they will be visible to you under the Segment section under Lists.
📘
Keep in mind
Once the list is created and saved you cannot update the criteria of the list. You can follow the same steps in case you want to analyze Events for Series List.
We hope this has given you a good idea of how you can make the most of the
Events
section of your dashboard to gain relevant behavioral insights. Please feel free to reach out via
[email protected]
in case you have any further queries. We’re always happy to help!
Updated
7 months ago
Preface
Copy Page
