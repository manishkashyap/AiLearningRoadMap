# In-app Messaging

- URL: https://docs.webengage.com/docs/xamarin-ios-in-app-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.iOS
In-app Messaging
While
creating In-app Campaigns
, you can specify multiple conditions, on the occurrence of which, the in-app message must be displayed for a user. You can choose to display the message on a specific screen in your app by tagging it with a
Screen Name
or tracking
Screen Data
for it.
🚧
Before continuing, please ensure that you have
added the WebEngage SDK to your app
.
Tagging App Screens
Screens are mobile equivalent of web pages, which can have associated properties. WebEngage SDK allows you to tag whenever a user sees a screen in your Xamarin.iOS app pages. These tags allow you to pinpoint screens in your app where you would later render in-app messages using WebEngage dashboard. A Xamarin.iOS app can have multiple screens and vice versa is also possible. Note that screens are only usable for targeting in-app engagements.
(Detailed read on how this works)
All screen related APIs are part of WebEngage Xamarin.iOS SDK's Analytics object. You get an instance of WebEngage Analytics object as follows.
C#
// import WebEngage SDK
using WebEngageXamariniOS;

// Get an instance of ‘Analytics’ object
Analytics weAnalytics = WebEngage.SharedInstance().Analytics;
After WebEngage has been successfully initialized, you can tag screens by calling the APIs on Analytics object.
C#
weAnalytics.NavigatingToScreenWithName("Purchase Screen");
🚧
NavigatingToScreenWithName
informs WebEngage SDK that the user has navigated to a new screen. Any previously set screen data is lost.
Tracking Screen Data
Every screen can be associated with some contextual data, which can be part of the targeting rule for in-app messages. Your app can update the data associated with a screen using the screen APIs described below.
C#
var screenData = new NSDictionary("productId", "~hs7674",
 "price", 1200);
weAnalytics.UpdateCurrentScreenData(screenData);
🚧
These APIs can be called any number of times after calling
NavigatingToScreenWithName
.
You can set the screen name and data in a single API call as shown below.
C#
weAnalytics.NavigatingToScreenWithName("Purchase Screen", screenData);
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Push Messaging
Callbacks
Copy Page
