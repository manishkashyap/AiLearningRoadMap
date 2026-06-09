# FAQ

- URL: https://knowledgebase.webengage.com/docs/inapp-notification-faq
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

FAQ
Commonly asked questions related to In-app messages
1. Can I use Branch.io deep links in my In-app Notifications?
Yes. Add the Branch.io deep link in the relevant fields (On-click Action/ Button Link) while
creating the In-app campaign
, and you're good to go!
🚧
Related read:
Integrating Branch with WebEngage
to capture user-app interactions as 'Events'
2. How are consecutive In-app Messages shown to a user?
Let's go over a short use-case to help you understand how users receive multiple In-app messages in the context of their app interactions.
👍
Engaging a User with In-app Messages When They Add Products to Cart
Let's take the example of an e-commerce app that contextually engages it's users with recommendations and offers.
Campaign 1 (Buy 1, Get 1):
Each time a user adds a product to their cart, they receive a contextual message highlighting more products that they could purchase along with it and avail a 50% discount!
Campaign 2 (Add-on Benefits):
Users who have purchased a premium membership are nudged with an additional message, highlighting the add-on benefits they can avail of the purchase. Depending on the product, this could be anything like
free shipping, free installation, free servicing, an extended return period, etc.
Pre-requisites:
Each time a user added a product to their cart, it's tracked as the
Custom Event
, Cart_Prod_Added
.
All products on which the
Buy 1, Get 1 scheme
is applicable are tracked through the
Custom Event Attribute
, Offer_Type
.
Each time a user purchases a premium membership, it's tracked as the
Custom User Attribute
, Customer_Type
.
Here's how the campaigns are triggered:
Campaign 1 (Buy 1, Get 1):
Triggered through a
Journey
,
targeting all users who perform the event,
Cart_Prod_Added
where the
Custom Attribute, Offer_Type = buy 1 get 1
.
Campaign 2 (Add-on Benefits):
Triggered through a
Journey
,
targeting users whose
Custom User Attribute, Customer_Type = Premium
AND have performed the custom event,
Cart_Prod_Added
.
This means:
If a
Premium Member
chooses to purchase a product on which the
Buy 1, Get 1 scheme
is applicable, then they'll receive
2 In-app Messages,
back-to-back.
So, which
In-app Notification
will a
Premium Member
receive first?
There is no fixed order. Users will receive the campaigns in the order of which your WebEngage dashboard triggers them. This means:
Some users could receive
Campaign 1 (Buy 1, Get 1)
first, followed by
Campaign 2 (Add-on Benefits).
While others could receive
Campaign 2 (Add-on Benefits)
first, followed by
Campaign 1 (Buy 1, Get 1).
The second
In-app Notification
will be rendered only once the user finishes interacting with the first notification
-
Clicks
on it or
Closes
it.
Similarly, if a user performs two
Events
consecutively and is bound to receive an
In-app Notification
in the context of each interaction, then:
They will receive notification 1 as per the
Event
that was performed first.
The notification tied to the second
Event
will be rendered only once they have
Clicked
/
Closed
notification 1.
In case the user ends their sessions after viewing notification 1, then notification 2 may be shown in their subsequent session.
(If the In-app message is sent through a Journey, then it will be shown only if the user starts another session within the Validity period defined by you.)
3. How can I customize the In-app Notification's placement in my app?
You can easily define where the
In-app Notification
must be shown in your app by tagging its relevant sections as
Screens.
Screens
are the mobile equivalent of web pages. Thus, using the
WebEngage SDK,
you can create a tag whenever a user sees a screen. These tags allow you to pinpoint
Screens
in your app where you can render
In-app messages.
Further, each
Screen
can be associated with some contextual
Screen Data,
that can be used to define where to show the
In-app Notification.
Thus, while
creating an In-app Campaign
, you can specify the
Screen Name
or
Screen Data parameter
to show the message on specific sections of your app.
🚧
How to Tag Screens in Your App & Pass Screen Data
Android apps
iOS apps
React Native apps
Cordova/ PhoneGap/ Ionic apps
Xamarin.Android apps
Xamarin.iOS apps
Unity.Android apps
Unity.iOS apps
4. What image & text specs should I follow for creating In-app Notifications?
Please follow these guidelines
for configuring the
In-app Layouts
available in your dashboard.
Please feel free to drop in a few lines at
[email protected]
in case you have any questions or feedback. We're always just an email away!
5. How can I set priority for the multiple In-App Notification campaigns eligible for the same users?
There are 2 ways to access this feature from the ‘List of campaigns’ page of in-app notifications. By clicking on the ‘Prioritize campaign’ icon beside the search box OR Clicking on the actions dropdown menu of any running or upcoming campaign and selecting the ‘Prioritize’ option. Once you are in the priority modal Click on ’Reorder’, Drag and drop the campaign that you would like to reorder and Click on ‘Save’.
6. If I have not set any priority, what would be the default priority set for my campaigns?
By default, journey and relay campaigns (if present) will be listed together in the top priority bucket and all standalone campaigns will be listed together in the next priority bucket.
7. Can I reorder/edit the campaign priority as often as I like?
Yes, you can reorder/edit the campaign priority as many times as you like as long as you have campaign maker or campaign checker permissions.
Updated
7 months ago
In-app Layouts: Image & Text Guidelines
App In- Line Content
Copy Page
