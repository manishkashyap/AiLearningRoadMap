# In-app Messaging

- URL: https://docs.webengage.com/docs/android-in-app-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
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
Screens are mobile equivalent of web pages, which can have associated properties. WebEngage SDK allows you to tag whenever a user sees a screen in your Android activities. These tags allow you to pinpoint screens in your app where you would later render in-app messages using WebEngage dashboard. An Android activity can have multiple screens and vice versa is also possible. Note that screens are only usable for targeting in-app engagements.
All screen related APIs are part of WebEngage Android SDK's
Analytics
object. You get an instance of WebEngage
Analytics
object as follows.
Java
Kotlin
// import WebEngage ‘Analytics’
import com.webengage.sdk.android.Analytics;

// Get an instance of ‘Analytics’ object
Analytics weAnalytics = WebEngage.get().analytics();
// import WebEngage ‘Analytics’
import com.webengage.sdk.android.Analytics;

// Get an instance of ‘Analytics’ object
val weAnalytics = WebEngage.get().analytics()
You can tag screens from the
onStart
of your Android activity as shown below.
Java
Kotlin
import com.webengage.sdk.android.Analytics;

...
...

@Override
protected void onStart() {
 super.onStart();
 Analytics weAnalytics = WebEngage.get().analytics();
 weAnalytics.screenNavigated("Purchase Screen");
}
import com.webengage.sdk.android.Analytics;

...
...

override fun onStart() {
 super.onStart()
 val weAnalytics = WebEngage.get().analytics()
 weAnalytics.screenNavigated("Purchase Screen")
 }
🚧
Please Note
screenNavigated
informs WebEngage SDK that the user has navigated to a new screen. Any previously set screen data is lost.
Tracking Screen Data
Every screen can be associated with some contextual data, which can be part of the targeting rule for in-app messages. Your app can update the data associated with a screen using the screen APIs described below.
Java
Kotlin
Map<String,Object> screenData = new HashMap<String, Object>();
screenData.put("productId", "~hs7674");
screenData.put("price", 1200);

weAnalytics.setScreenData(screenData);
val screenData: MutableMap<String, Any> = HashMap()
 screenData["productId"] = "~hs7674"
 screenData["price"] = 1200

weAnalytics.setScreenData(screenData)
🚧
These APIs can be called any number of times after calling
screenNavigated
.
You can set the screen name and data in a single API call as shown below.
Java
Kotlin
weAnalytics.screenNavigated(String screenName, Map<String,Object> screenData);
weAnalytics.screenNavigated("screen-name", screenData)
Please feel free to drop in a few lines at
[email protected]
in case you have further queries. We're always just an email away!
Updated
7 months ago
Understanding Device Reachability and Deliverability
App In-line Content
Copy Page
