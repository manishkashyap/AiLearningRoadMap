# In-App Messaging

- URL: https://docs.webengage.com/docs/ionic-capacitor-in-app-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Ionic Capacitor
In-App Messaging
While
creating In-app Campaigns
, you can specify multiple conditions, on the occurrence of which, the in-app message must be displayed for a user. You can choose to display the message on a specific screen in your app by tagging it with a
Screen Name
or tracking
Screen Data
for it.
🚧
Before continuing, please ensure that you have added the WebEngage library to your Application
Message Placement
Screens are web pages in the hybrid app which can have associated properties. WebEngage SDK allows you to tag whenever a user sees a screen in your hybrid app pages. These tags allow you to pinpoint screens in your app where you would later render in-app messages using WebEngage dashboard. A hybrid app can have multiple screens and vice versa is also possible. Note that screens are only usable for targeting in-app engagements.
Every screen can be associated with some contextual data, which can be part of the targeting rule for in-app messages. Your app can update the data associated with a screen using
Webengage.screen
as shown below.
Webengage.screen
accepts two parameters: Screen Name (
String
) and Screen Data (
Object
). You can call
Webengage.screen
with either both screen name and screen data as parameters or any one of these.
JavaScript
Webengage.screen("Home Screen" );
JavaScript
Webengage.screen("Purchase Screen", {
 "productId": "~hs7674",
 "price" : 1200
});
🚧
Webengage.screen
informs WebEngage SDK that the user has navigated to a new screen. Any previously set screen data is lost.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Push Messaging
Callbacks
Copy Page
