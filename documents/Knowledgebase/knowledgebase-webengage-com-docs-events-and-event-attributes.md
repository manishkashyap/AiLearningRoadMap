# Understanding Events & Event Attributes

- URL: https://knowledgebase.webengage.com/docs/events-and-event-attributes
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Understanding Events & Event Attributes
The following section has been designed to help you understand events, event attributes and their application across your WebEngage dashboard. Let’s start with the basics:
What is an Event?
The term
event
refers to all the actions performed by users while interacting with your mobile app, website and campaigns.
For example, if a user needs to click on a product to view its details, then it is advisable to track this action as an event
(Product Viewed)
as it brings them a step closer to making a purchase.
In this sense, tracking events is like following the footprints of your users. And when put together in chronological order, they tell a story of human behaviour.
What is an Event Attribute?
The term
event attribute
refers to all the details attached to an event which help us understand it’s context. You can think of attributes as adjectives which give an event a character and explain what it’s all about.
👍
Example: Leveraging event attributes to understand user behaviour
To understand this better, let’s take the example of an e-commerce app wherein a user views several products before making a purchase.
To assist with the purchase, you decide to send each user an email with details of the product and a one-time discount offer.
But merely knowing that a user viewed a product on your mobile app/website is not enough. You will need more details about the event;
Product Viewed
to create a contextual and personalised email. This is where event attributes come in.
👍
In this case, the event
Product Viewed
can have the following attributes;
Product Details\
Product Name
Product ID
Product Category
Product Cost
Product Rating
Time
Location
Country
City
Technology\
OS
Device Model
Device Brand
App Version
App ID and so on.
Hence, by adding these attributes as elements of personalisation to your email, you can craft one-on-one messages in an instant.
The possibilities are endless!
Types of Events and Event Attributes
When using your WebEngage account, you will notice that events and event attributes are bucketed into different types. Let’s understand this in detail.
Events and Event Attributes Automatically Gleaned by WebEngage
Auto-tracking of (predefined) events and event attributes is made possible when you connect your app and website with your WebEngage account. Now let’s get you acquainted with the terms.
System Events
At WebEngage we have predefined a comprehensive list of all the generic events which are performed by users when interacting with your mobile app and website. These events are called
system events
and include actions like;
App Installed
App Uninstalled
Session Started
Session Ended and so on.
System Attributes
We have also predefined a comprehensive list of generic attributes which can help give all the events performed by your users, more context. These are called
system attributes
and include details like;
Time
Location
Technology
(OS, Browser, App ID, Device Model etc.)
Screen
(only for mobile apps)
Campaign Events
Just like we have predefined a list of all the standard events performed by users while interacting with your app and website, we have also identified a set of generic events that users perform when interacting with your campaigns too. So all interactions like:
Email Opened
Web Push Subscribed
Push Clicked
SMS Sent and so on, are called
campaign events
.
These events are tracked for all channels including
Push, In-app, SMS, On-site, Web Push and Email.
Since users perform different actions when interacting with each channel, the campaign events and their attributes (also called system attributes) vary accordingly too.
🚧
List of System Event, Campaign Events & System Attributes
Here's a list of all the data points
that are automatically gleaned by us once you connect your app/website with WebEngage.
(So, you don’t need to worry about tracking all this data!)
Events and Event Attributes Custom Tracked For Your Business
Once your app and website are integrated with WebEngage, we start gleaning certain predefined events and attributes for your account. But this integration also makes it possible for you to custom define and track events and attributes which play an important role in your user lifecycle.
Let’s get you acquainted with the terms that help you identify these data points in your dashboard:
Custom Events
To help you understand this concept, let’s take the example of a mobile e-commerce app and map out the actions their users need to perform to make a purchase:
So, if we were to track each action as an event for this e-commerce business, it would look something like this:
User Actions
Custom Event
Search for a product
Search
View product details
Product - Page Viewed
Select product quantity
Product - Quantity Selected
Add to cart
Product - Added to Cart
View Cart
Cart Viewed
Initiate checkout
Checkout - Started
Add mode of payment
Checkout - Payment
Select delivery option
Checkout - Delivery
Confirm and place the order
Checkout Complete
All the events listed above are called
custom events
as they have been explicitly defined and tracked for the e-commerce app in reference. Similarly, all the behavioural data points defined and passed by you to your WebEngage account will also be called
custom events
.
Custom Attributes
Just like you can custom define events to track specific user behaviour, you can custom define attributes too, to understand the context of each custom event, better. For every
custom event
you pass to your WebEngage account; you can add a list of relevant attributes to get more insights into the behaviour. These are called
custom attributes
and are exclusively tied to a
custom event
.
👍
Example: Defining custom attributes for a custom event
For example, if we were to define custom attributes for the event
Checkout Complete
, then it would include details like;
Cart ID
Cart Size
Cart Value
Primary Category and so on.
Which Custom Events and Attributes Should You Track?
When your online business is in its primary stage, it’s easy to think that one needs to track all the possible events a user can perform to understand what’s going on. But collecting data in an unplanned manner generally leads to the creation of a chaotic database, which fails to provide useful insights.
This is why we suggest that before you set out to identify and track events, define your goals. Determining the utility of an event in a user journey is critical in deciding what to track and when.
👍
Here are a few questions to help you identify the custom events (and their attributes) you should track for your business:
What is the problem that you are trying to solve?
What is the end goal of collecting data related to a particular event?
How will you make use of the data being collected?
What will the data convey? Will it help fulfil your goals?
How and when will you evaluate the reported data?
How will you form a decision based on the data?
Avoid panicking about missing out on data - ignore the rest until you have the means to act upon the results. To make things easier for you, we have mapped out the key events that businesses in the industry of
E-commerce
,
Travel (Hotel Bookings)
,
Travel (Flight Bookings)
,
Gaming Apps
,
Insurance
should track for their respective user lifecycles.
How Different Events and Event Attributes Interact
Now that you have a good understanding of the different type of events and attributes; let’s show you how they interact with each other and fit into your behavioral analysis:
Click to enlarge
1. Custom Events and their attributes
All custom events defined and explicitly tracked for your business can be sent (to WebEngage) along with a set of custom attributes to help you understand their context better. This means that all custom attributes are tied to a specific custom event and cannot be used to analyse other custom events, system events or campaign events, across your dashboard.
2. Understanding the generic nature of System Attributes
System attributes are generic and can be applied as filters to all system events, campaign events and custom events as filters, for more context.
👍
Example 1: Applying custom attributes & system attributes to a custom event
For example, if the custom event is
Cart - Product Removed
, then its custom attributes will be;
Product ID
Product Name
Product Rating
Product Category
Product Cost and so on.
And the system attributes you can apply to the event will include;
Location
Browser
OS
Platform
App Version
Screen URL
👍
Example 2: Applying system attributes to a campaign event
Similarly, if the campaign event is
Email Clicked
, then it’s predefined system attributes will be;
Email ID
ESP Name
ESP Message-ID
Time
Location
Technology
Campaign ID
Journey ID and so on.
How Events are Calculated
At WebEngage, there are two ways in which we calculate the number of times users perform an event;
occurrences
and
uniques.
Let’s quickly go over the difference between each:
What does ‘Occurrences’ mean?
Occurrences refer to the total number of times an event has been performed within a specific time frame.
This means that if a user performs an event five times within a given time frame, then
occurrences
will equal five, even though just one user has performed it. So, by viewing the
occurrences
of an event, you can get a clear picture of the total number of times the event has been performed.
What does ‘Uniques’ mean?
Uniques
refers to the total number of users who have performed an event, within a specific time frame.
This means that if you are viewing uniques for an event which was performed five times by a user, then
uniques
will equal one. So, by observing the
Uniques
of an event, you can find out exactly how many users were responsible for its occurrence.
In this sense, Occurrences / Uniques = Average number of times an event is performed
🚧
The concept of 'Occurrences' and 'Uniques' is applicable to the following sections of your dashboard:
Event Analysis:
The query bar here allows you to select occurrences or uniques for analyzing the performance of the selected event.
Cohort Analysis:
The query bar here requires you to define two events for analysis,
First Event
and
Return Event.
Only the occurrences of each event are taken into account when showing results in the cohort table.
Funnel Analysis:
When creating funnels in WebEngage, each step added to a funnel needs to be defined as an event. So, when calculating:
total number of users entering the funnel
overall conversion rate
conversion rate of each step; the occurrences of the defined events are taken into account.
Creating Triggered Campaigns
:
When setting up a triggered campaign through any of the channels listed in your dashboard, you need to define an
Event
, upon the occurrence of which the campaign will be triggered. Thus, the campaign is sent to all the users who perform the defined event, each time they perform it.
We hope this gives you a good idea of how you can use
Events
and
Event Attributes
across your dashboard for behavioral analysis, user segmentation, hyper-personalized messaging and a lot more!
Updated
4 months ago
So, what's next?
A hands-on document to help you analyze behavioral data in your dashboard.
Analyzing Events in WebEngage
Copy Page
