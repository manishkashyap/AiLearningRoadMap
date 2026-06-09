# Advanced

- URL: https://docs.webengage.com/docs/android-advanced
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
Advanced
Tracking in Android WebViews: JavaScript Bridge
JavaScript bridge is useful if you are using WebViews in your Android app.
WebEngage provides a JavaScript bridge which enables you to handle
WebEngage Website SDK
calls from your Android WebViews. When you use this bridge, all WebEngage JavaScript API calls (such as
track
,
user.setAttribute
,
screen
) made from web pages inside WebViews will be redirected to WebEngage Android native APIs. This will ensure that tracked data is attributed to the right devices, even if Website SDK APIs are called from within your Android app WebViews.
Follow the steps below to create a bridge between WebEngage Website SDK and Android SDK. These steps assume that you have already integrated the
Website SDK
and are using it to track users, events and other information on your website.
Step 1:
Replace your existing WebEngage
Website SDK integration code
with the one below at the end of the
<head>
section of each page you are tracking.
JavaScript
<script id="_webengage_script_tag" type="text/javascript">
 var webengage;
 ! function(w, e, b, n, g) {
 function o(e, t) {
 e[t[t.length - 1]] = function() {
 r.__queue.push([t.join("."), arguments])
 }
 }
 var i, s, r = w[b],
 z = " ",
 l = "init options track screen onReady".split(z),
 a = "feedback survey notification".split(z),
 c = "options render clear abort".split(z),
 p = "Open Close Submit Complete View Click".split(z),
 u = "identify login logout setAttribute".split(z);
 if (!r || !r.__v) {
 for (w[b] = r = {
 __queue: [],
 __v: "6.0",
 user: {}
 }, i = 0; i < l.length; i++) o(r, [l[i]]);
 for (i = 0; i < a.length; i++) {
 for (r[a[i]] = {}, s = 0; s < c.length; s++) o(r[a[i]], [a[i], c[s]]);
 for (s = 0; s < p.length; s++) o(r[a[i]], [a[i], "on" + p[s]])
 }
 for (i = 0; i < u.length; i++) o(r.user, ["user", u[i]])
 }
 }(window, document, "webengage");

 if (window.__WEBENGAGE_MOBILE_BRIDGE__) {

 (function(bridge) {

 var type = Object.prototype.toString;

 webengage.user.login = webengage.user.identify = function(id) {
 bridge.login(id)
 };
 webengage.user.logout = function() {
 bridge.logout()
 };

 webengage.user.setAttribute = function(name, value) {
 var attr = null;

 if (type.call(name) === '[object Object]') {
 attr = name;
 } else {
 attr = {};
 attr[name] = value;
 }

 if (type.call(attr) === '[object Object]') {
 bridge.setAttribute(JSON.stringify(attr));
 }
 };

 webengage.screen = function(name, data) {
 if (arguments.length === 1 && type.call(name) === '[object Object]') {
 data = name;
 name = null;
 }

 bridge.screen(name || null, type.call(data) === '[object Object]' ? JSON.stringify(data) : null);
 };

 webengage.track = function(name, data) {
 bridge.track(name, type.call(data) === '[object Object]' ? JSON.stringify(data) : null);
 };

 })(window.__WEBENGAGE_MOBILE_BRIDGE__);

 } else {

 setTimeout(function() {
 var f = document.createElement("script"),
 d = document.getElementById("_webengage_script_tag");
 f.type = "text/javascript",
 f.async = !0,
 f.src = ("https:" == window.location.protocol ? "https://ssl.widgets.webengage.com" : "http://cdn.widgets.webengage.com") + "/js/webengage-min-v-6.0.js",
 d.parentNode.insertBefore(f, d)
 });

 }

 webengage.init("__LICENSE_CODE__");
</script>
🚧
Make sure you replace
YOUR_WEBENGAGE_LICENSE_CODE
with your
WebEngage license code
.
Step 2:
Inject WebEngage Mobile Bridge into your Android WebView as shown below.
Java
Kotlin
import com.webengage.sdk.android.bridge.WebEngageMobileBridge;
 ...
 ...
myWebView.addJavascriptInterface(new WebEngageMobileBridge(this), WebEngageMobileBridge.BRIDGE_NAME);
import com.webengage.sdk.android.bridge.WebEngageMobileBridge;
 ...
 ...
myWebView.addJavascriptInterface( WebEngageMobileBridge(this), WebEngageMobileBridge.BRIDGE_NAME)
Here
myWebView
is the WebView for which you are adding this bridge.
Event Reporting Strategy
WebEngage stores every datapoint in local database and sends them periodically to server in a background thread when a certain criteria is met. The criteria is based on the number of events in local database and last synced time.
WebEngage allows you to change the event reporting behaviour during SDK initialization , so that you can make events sync faster to WebEngage if available connectivity is good.
Java
Kotlin
WebEngageConfig webEngageConfig = new WebEngageConfig.Builder()
 .setEventReportingStrategy(ReportingStrategy.FORCE_SYNC) //During initialization
 .build();
WebEngage.engage(this.getApplicationContext(), webEngageConfig);
val webEngageConfig = WebEngageConfig.Builder()
 .setEventReportingStrategy(ReportingStrategy.FORCE_SYNC) //During initialization
 .build()
 WebEngage.engage(this.applicationContext, webEngageConfig)
Alternatively you can also change this behaviour anytime during application lifecycle using below API.
Java
Kotlin
WebEngage.get().setEventReportingStrategy(ReportingStrategy.BUFFER);
WebEngage.get().setEventReportingStrategy(ReportingStrategy.BUFFER);
🚧
setEventReportingStrategy
is to be called only once in a session. The SDK remembers this setting unless your app is restarted.
By default, the reporting strategy is set to
ReportingStrategy.BUFFER
. See
ReportingStrategy
for details.
Fetch WebEngage Configuration
Returns WebEngage configuration. See
WebEngageConfig
for details.
Java
Kotlin
WebEngageConfig weConfig = WebEngage.get().getWebEngageConfig();
val weConfig = WebEngage.get().webEngageConfig
Logging
You can enable/disable logs from WebEngage SDK during SDK initialization as shown below.
Java
Kotlin
WebEngageConfig webEngageConfig = new WebEngageConfig.Builder()
 .setDebugMode(true)
 .build();
WebEngage.engage(this.getApplicationContext(), webEngageConfig);
val webEngageConfig = WebEngageConfig.Builder()
 .setDebugMode(true)
 .build()
 WebEngage.engage(this.applicationContext, webEngageConfig)
Alternatively, you can change log level anytime using below API.
Java
Kotlin
WebEngage.get().setLogLevel(Logger.SILENT);
WebEngage.get().setLogLevel(Logger.SILENT);
🚧
This is to be used only in development mode.
Alternative WebEngage Initialization
Use this approach if you are targeting devices below Android API level 14.
Step 1:
Initialize WebEngage SDK from the
onCreate
of your
Application
class.
Java
Kotlin
import com.webengage.sdk.android.WebEngageConfig;

public class MyApplication extends Application {
 @Override
 public void onCreate() {
 super.onCreate();
 WebEngageConfig webEngageConfig = new WebEngageConfig.Builder()
 .setWebEngageKey(YOUR_WEBENGAGE_LICENSE_CODE)
 .setDebugMode(true) // only in development mode
 .build();
 WebEngage.engage(this, webEngageConfig);
 }
}
val webEngageConfig = WebEngageConfig.Builder()
 .setWebEngageKey(YOUR_WEBENGAGE_LICENSE_CODE)
 .setDebugMode(true) // only in development mode
 .build()
WebEngage.engage(this, webEngageConfig)
Step 2:
Manually call WebEngage's session tracking API from
onStart
and
onStop
of each of your activities.
Java
Kotlin
import com.webengage.sdk.android.WebEngage;

...
...

@Override
public void onStart(){
 super.onStart();
 WebEngage.get().analytics().start(this);
}

@Override
public void onStop(){
 super.onStop();
 WebEngage.get().analytics().stop(this);
}
import com.webengage.sdk.android.WebEngage;

...
...
 
 override fun onStart() {
 super.onStart()
 WebEngage.get().analytics().start(this)
 }

 override fun onStop() {
 super.onStop()
 WebEngage.get().analytics().stop(this)
 }
You are now ready to continue with the setup process
here
.
Location Tracking
WebEngage Android SDK allows you to define location tracking accuracy, or to disable location tracking, which enables you to optimize for resources - device battery and data usage. Follow the steps below to set location tracking accuracy:
Step 1:
Add Google Play location dependency in your app's
build.gradle
.
Groovy
dependencies {
 implementation 'com.google.android.gms:play-services-location:21.3.0'
}
🚧
Note
Starting from Android SDK version 4.17.1, WebEngage requires
play-services-location
version 21.0.1 or later.
To use
play-services-location
version 21.0.0 or earlier, please downgrade the WebEngage SDK to version 4.17.0 or below.
Step 2:
Add the below location permissions in your AndroidManifest.xml file.
XML
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name"android.permission.ACCESS_BACKGROUND_LOCATION"/> if your app targets Android 10 (API level 29) or higher
Step 3:
Use
setLocationTrackingStrategy
to define location tracking accuracy. Note that this method is to be called after
WebEngage SDK initialization
.
Method 1: Setting Location Tracking Strategy in WebEngageConfig
Java
Kotlin
import com.webengage.sdk.android.WebEngageConfig;
import com.webengage.sdk.android.LocationTrackingStrategy;

...

WebEngageConfig config = new WebEngageConfig.Builder()
 ...
 .setLocationTrackingStrategy(LocationTrackingStrategy.ACCURACY_BEST)
 .build();
import com.webengage.sdk.android.WebEngageConfig;
import com.webengage.sdk.android.LocationTrackingStrategy;

...

val config = WebEngageConfig.Builder()
...

.setLocationTrackingStrategy(LocationTrackingStrategy.ACCURACY_CITY)
.build();
Method 2: Setting Location Tracking Strategy Dynamically
Java
Kotlin
import com.webengage.sdk.android.WebEngage;
import com.webengage.sdk.android.LocationTrackingStrategy;
 
...
 WebEngage.get().setLocationTrackingStrategy(LocationTrackingStrategy.ACCURACY_BEST);
import com.webengage.sdk.android.WebEngage;
import com.webengage.sdk.android.LocationTrackingStrategy;
 
...
 WebEngage.get().setLocationTrackingStrategy(LocationTrackingStrategy.ACCURACY_BEST);
Following are the options that you can use to define location tracking accuracy.
Location accuracy level
Description
ACCURACY_BEST
Uses the highest level of accuracy. Recommended for using geofencing; consumes more device power.
Interval between location updates: 15 minutes
Fastest interval between location updates: 5 mins
Smallest displacement that can be measured: 1 km
ACCURACY_CITY
Recommended for city-level location tracking; consumes less device power.
Interval between location updates: 3 hours
Fastest interval between location updates: 1 hour
Smallest displacement that can be measured: 20 km
ACCURACY_COUNTRY
Recommended for country-level location tracking; consumes less power.
Interval between location updates: 12 hours
Fastest interval between location updates: 12 hours
Smallest displacement that can be measured: 100 km
DISABLED
Disables location tracking by WebEngage SDK. With this value, WebEngage will neither track any user location nor update it on your WebEngage dashboard.
If you are using this configuration, you can manage location updates by using
setLocation
to manually set the location.
🚧
Note that
WebEngage.get().setLocationTracking(true)
is deprecated.
Apps targeting Android Marshmallow and above would need to
request
location permission from user and set location tracking to
true
or
false
from permission request
callback
depending on whether location permission is granted or not.
Geofence
A Geofence is a virtual boundary set around a specific area. When you enter or leave this area, the app can trigger specific actions, like sending a notification or updating your status. It’s like a digital fence that monitors when you step in or out of a defined zone.
WebEngage simplifies geofencing setup in your app. Just follow these steps to enable geofencing capabilities and configure geofences through the WebEngage dashboard.
Steps to Enable Geofencing in Your Application
Ensure that you followed and completed setup of
Location Tracking
Obtain Background Location Permission:
Confirm that users have granted background location access.
Optimize Location Accuracy:
Use
LocationTrackingStrategy.ACCURACY_BEST
for the most accurate geofencing results.
For details on setting up geofences in the WebEngage dashboard, refer to the
Geofence Setup Guide
.
🚧
Note
Maximum number of geofences allowed per app is 100.
Enable User Storage Encryption
🚧
Supported on
android-sdk:4.18.1
or above.
Overview :
User Storage Encryption enhances the security of user data by encrypting it before storing it on the device. This ensures that sensitive information remains protected from unauthorized access
Steps to Enable User Storage Encryption:
To enable User Storage Encryption, modify the WebEngage configuration in your application as follows:
Implementation in WebEngage Config Builder :
Use the
.shouldEncryptUserStorage(true)
method to enable encryption when initializing WebEngage
Java
Kotlin
WebEngageConfig.Builder builder = new WebEngageConfig.Builder()
 .setWebEngageKey(LICENSE_CODE)
 .shouldEncryptUserStorage(true);
val builder: WebEngageConfig.Builder = WebEngageConfig.Builder()
 .setWebEngageKey(LICENSE_CODE)
 .shouldEncryptUserStorage(true)
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Callbacks
Troubleshooting
Copy Page
