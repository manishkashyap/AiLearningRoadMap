# In-app Messaging

- URL: https://docs.webengage.com/docs/unity-android-in-app-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Unity.Android
In-app Messaging
No additional steps are required for enabling
In-app Notifications.
However, we recommend that you track the various sections of your app as
Screens
to customize In-app message placement. You can also track specific app-user interactions as
Screen Data
to contextually show the In-app message. These data points can be used to
configure In-app message targeting
while creating the campaign.
🚧
Before continuing, please ensure that you have
added the WebEngage SDK to your app
.
Tagging App Screens
Screens are the mobile equivalent of web pages, which can have associated properties. WebEngage SDK allows you to tag whenever a user sees a screen. These tags allow you to pinpoint screens in your app where you can later render in-app messages. Please do keep in mind that screens are only usable for targeting In-app message targeting.
C#
using WebEngageBridge;
 ...
 
 // Set screen name
 WebEngage.ScreenNavigated("Purchase Screen");
Tracking Screen Data
Every screen can be associated with some contextual data, which can be part of the targeting rule for in-app messages. Your app can update the data associated with a screen using the code snippet below.
C#
using WebEngageBridge;
 ...
 
 // Update current screen data
 Dictionary<string, object> currentData = new Dictionary<string, object>();
 currentData.Add("productId", "~hs7674");
 currentData.Add("price", 1200);
 WebEngage.SetScreenData(currentData);

 // Set screen name with data
 Dictionary<string, object> data = new Dictionary<string, object>();
 data.Add("productId", "~hs7674");
 data.Add("price", 1200);
 WebEngage.ScreenNavigated("Purchase Screen", data);
Please feel free to drop in a few lines at
[email protected]
in case you have any queries or feedback. We're always just an email away!
Updated
7 months ago
Push Messaging
Unity.iOS
Copy Page
