# Advanced

- URL: https://docs.webengage.com/docs/xamarin-ios-advanced
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.iOS
Advanced
Location Tracking
WebEngage Xamarin.iOS SDK allows you to define location tracking accuracy, or to disable location tracking, which enables you to optimize for resources - device battery and data usage. Use
AutoTrackUserLocationWithAccuracy
to define location tracking accuracy as shown below. Note that this method is to be called after
WebEngage SDK initialization
.
C#
WebEngage.SharedInstance().AutoTrackUserLocationWithAccuracy(WEGLocationAccuracy.ForCity);
Following are the options that you can use to define location tracking accuracy.
WEGLocationAccuracy.Best
Uses the highest level of accuracy. Recommended for real-time location tracking, as it requires more time to determine location and consumes more device power.
Smallest displacement that can be measured: 1 km
WEGLocationAccuracy.ForCity
Recommended for city-level location tracking; consumes less device power.
Smallest displacement that can be measured: 20 km
WEGLocationAccuracy.ForCountry
Recommended for country-level location tracking; consumes less power.
Smallest displacement that can be measured: 100 km
WEGLocationAccuracy.Disable
Disables location tracking by WebEngage SDK. With this value, WebEngage will neither track any user location nor update it on your WebEngage dashboard.
If you are using this configuration, you can manage location updates by using
setUserLocationWithLatitude:andLongitude
to manually set the location.
🚧
Please Note
If
AutoTrackUserLocationWithAccuracy
is not called, then the SDK will track user location only if your app has permission to read the device location, with default accuracy
WEGLocationAccuracy.ForCity
.
Calling this method after initializing the SDK will force every launch of your app to track location with the given accuracy.
If your app does not have the permission to read device location, WebEngage SDK will not track any location irrespective of the configuration.
Alternative Initialization
In order to initialize the SDK your app needs to call one of the below mentioned APIs, whichever is appropriate for the use case from your application's
AppDelegate
.
C#
bool autoRegister = true;
WebEngage.SharedInstance().Application(application, launchOptions, inAppNotificationDelegate, autoRegister);

WebEngage.SharedInstance().Application(application, launchOptions);

WebEngage.SharedInstance().Application(application, launchOptions, autoRegister);

WebEngage.SharedInstance().Application(application, launchOptions, notificationDelegate);
Parameters
launchOptions
:
NSDictionary
passed into
application:didFinishLaunching:WithOptions
of your
AppDelegate
. You must pass the same dictionary in the above method calls.
autoRegister
: If your application handles the APNs registration for remote notifications manually (or using some other SDK), set
autoRegister
to
false
. Default value for this is
true
, in which case WebEngage SDK will attempt to make the registration.
notificationDelegate
: Must be an instance of a class which implements the
WEGInAppNotificationProtocol
for In-App notification lifecycle callbacks.
You are now ready to continue with the setup process
here
.
Updated
7 months ago
Callbacks
Unity.Android
Copy Page
