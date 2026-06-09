# In-app Messaging

- URL: https://docs.webengage.com/docs/xamarin-android-in-app-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.Android
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
Screens are mobile equivalent of web pages, which can have associated properties. WebEngage SDK allows you to tag whenever a user sees a screen in your Xamarin.Android app pages. These tags allow you to pinpoint screens in your app where you would later render in-app messages using WebEngage dashboard. A Xamarin.Android app can have multiple screens and vice versa is also possible. Note that screens are only usable for targeting in-app engagements.
All screen related APIs are part of WebEngage Android SDK's Analytics object. You get an instance of WebEngage Analytics object as follows.
C#
// import WebEngage SDK
using Com.Webengage.Sdk.Android;
...
 
// Get an instance of ‘Analytics’ object
Analytics weAnalytics = WebEngage.Get().Analytics();
You can tag screens from the
onStart
of your Android activity as shown below.
C#
using Com.Webengage.Sdk.Android;
using Java.Lang;
...

 public class YourActivity : Activity
 {
 ...
 protected override void OnStart()
 {
 base.OnStart();
 weAnalytics.ScreenNavigated("Purchase Screen");
 ...
 }
 }
🚧
ScreenNavigated
informs WebEngage SDK that the user has navigated to a new screen. Any previously set screen data is lost.
Tracking Screen Data
Every screen can be associated with some contextual data, which can be part of the targeting rule for in-app messages. Your app can update the data associated with a screen using the screen APIs described below.
C#
IDictionary<string, Object> screenData = new Dictionary<string, Object>();
screenData.Add("productId", "~hs7674");
screenData.Add("price", 1200);

weAnalytics.SetScreenData(screenData);
🚧
These APIs can be called any number of times after calling
screenNavigated
.
You can set the screen name and data in a single API call as shown below.
C#
weAnalytics.ScreenNavigated("Purchase Screen", screenData);
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Push Messaging
Callbacks
Copy Page
