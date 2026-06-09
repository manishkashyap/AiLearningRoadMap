# On-site

- URL: https://docs.webengage.com/docs/on-site-notification-survey
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
On-site
A Step-by-step guide to configuring On-site Notifications, Surveys Widget for your site
🚧
Please Ensure That Your Website is Integrated with WebEngage Before Proceeding
Getting Started with Web SDK Integration
Integration via
Segment.com
or
Google Tag Manager (GTM)
On-site engagement is one of the most trusted tools in a marketer's arsenal. Be it engaging users through
On-site Notifications
, gauging their preferences through
Surveys
or collecting valuable inputs through widgets - it's the easiest way to engage active users in real-time.
At WebEngage, you can start engaging on-site users as soon as you integrate your website! Here's how you can set it:
Step 1: Enable Channel in Dashboard
As shown below, head over to
Data Platform> Integrations > Channel Integration Status > On-site Setup (Configure)
in your dashboard and click the toggle button against
On-site and Survey
to start sending the respective campaigns.
Click to enlarge
Step 2 (Optional): Customize Notifications, & Survey Widget
The
WebEngage Web SDK
enables you to implement several additional customizations to control the notification, and survey, widgets behaviour, data collection, and appearance. For example:
On-site Notifications
You can delay the notification's appearance instead of rendering it as soon as a user starts their session. (
delay
)
You can choose to show a particular notification on select days of the week like a
We're Offline Notification every Sunday.
(
ruleData
)
Depending on the use-case, you can choose to engage users with the On-site Notification again if they Click/Dismiss it the first time. (
forceRender
)
Survey
You can delay the survey's appearance instead of rendering it as soon as a user starts their session. (
delay
)
You can choose to engage users with a survey each time they start a new session on your website. (
scopeType
)
🚧
Start Here: Customising On-site Engagement Tools
On-site Notification
On-site Survey
With WebEngage, you can also choose to track specific user interaction and page elements as
Website Data Attributes.
This enables
advanced notification targeting
to your teammates.
Here's how you can go about it:
On-site Notification & Survey Targeting (Custom Rules)
Each user is unique. Which is why each user may choose to interact differently with the various pages on your site. Let's compare a few user personas to help you understand this better:
👍
Persona 1: Knows What They Want
Such users usually know exactly what they want when they land on your site. They'll go straight to a product page, add it to cart, signup if it's a pre-requisite to purchasing and complete payment.
👍
Persona 2: Fence-sitter
Such users are confused about whether they really want that dress or can do without it. They'll browse through products, add a few to their wishlist/cart and probably come back in another session to review their list.
Evidently, the way
Persona 1
and
Persona 2
interact with your website to make a purchase decision will be very different. This is where
Website Data Attributes
come in handy.
Each page on your website can be associated with contextual data which could be anything like:
Number of days since sign-in/ purchase/ watching a video/ playing a game.
The product category a user is viewing.
The number of products a user sees in a session.
The search filters added by a user,
and so on.
📘
Using the
WebEngage Web SDK,
you can track user interactions and page details as
Website Data Attributes.
This enables you to configure
Custom Rules
that help display the
On-site Notification/ Survey
to only those users who engage with a webpage in a specific manner.
For example:
In the case of Persona 1:
You can engage users who are purchasing products worth $500 or more with a notification, offering 10% off if their entire bill amounts to $600
(increasing your ARPU).
This can be done by:
Step 1:
Tracking the total checkout amount as the data attribute,
checkout-amount.
Step 2:
Adding the custom rule,
checkout-amount
equal to or greater than
500
under
Custom Rules > Where to Show?
while creating the campaign.
In the case of Persona 2:
You can engage users who have viewed more than 100 products on a page, highlighting the most popular styles of the season
(making it easier for them to make a purchase decision).
This can be done by:
Step 1:
Tracking the number of products viewed by a user in a session as the data attribute,
product-count.
Step 2:
Adding the custom rule,
product-count
greater than
100
under
Custom Rules > Where to Show?
while creating the campaign.
Similarly, you too can leverage
Custom Rules
to display the
On-site Notification/ Survey
only when users exhibit specific behavior on your site.
🚧
Start Here
Tracking Data Attributes for Advanced Notification & Survey Targeting
For example, an e-commerce platform decided to route all
Discount Code, Offers & Cashback
related queries to a special
Add-on Services Team.
Here's how they set it up:
Step 1:
Assign a common ID to all the discount coupons, and offers flashed across their website by tracking them as the data attribute,
element-ID
.
Step 2:
Add the custom rule - when
Data Attribute,
element-ID
exists, route user queries to
[email protected]
.
Similarly, you too can direct specific queries to different teammates to deliver delightful support experiences!
Collecting User Responses for Internal Reporting
You can easily relay
Survey
responses to your server through our
Rest APIs.
This comes in handy when:
Relaying the answers to your CRM platform for record-keeping.
(The response can be referenced when interacting with a user.)
Analyzing responses to build product features, add-on services.
Leveraging responses to segment and engage users with contextually personalized messages.
You can do this by categorizing and sending specific types of responses back to your WebEngage dashboard as
Custom User Attributes
.
You can then leverage the data to
segment users
and engage them through multiple channels.
🚧
Start Here
Querying On-site Survey Responses
We hope this has enabled you to engage on-site users effectively. Please feel free to drop in a few lines at
[email protected]
in case you have any queries or feedback. We're always just an email away!
Updated
7 months ago
Salla
Web Push
Copy Page
