# Advanced

- URL: https://docs.webengage.com/docs/xamarin-android-advanced
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.Android
Advanced
Event reporting strategy
WebEngage stores every datapoint in local database and sends them periodically to server in a background thread when a certain criteria is met. The criteria is based on the number of events in local database and last synced time.
WebEngage allows you to change the event reporting behaviour during SDK initialization, so that you can make events sync faster to WebEngage if available connectivity is good.
C#
using Com.Webengage.Sdk.Android.Actions.Database;
...

WebEngageConfig config = new WebEngageConfig.Builder()
 .SetEventReportingStrategy(ReportingStrategy.Buffer)
 .Build();

RegisterActivityLifecycleCallbacks(new WebEngageActivityLifeCycleCallbacks(this, config));
Alternatively you can also change this behaviour anytime during application lifecycle using below API.
C#
using Com.Webengage.Sdk.Android.Actions.Database;
...

WebEngage.Get().SetEventReportingStrategy(ReportingStrategy.Buffer);
🚧
SetEventReportingStrategy
is to be called only once in a session. The SDK remembers this setting unless your app is restarted.
By default, the reporting strategy is set to
ReportingStrategy.Buffer
. See
ReportingStrategy
for details.
Fetch WebEngage configuration
Returns WebEngage configuration. See
WebEngageConfig
for details.
C#
WebEngageConfig weConfig = WebEngage.Get().WebEngageConfig;
Logging
You can enable/disable logs from WebEngage SDK during SDK initialization as shown below.
C#
using Com.Webengage.Sdk.Android;
...

WebEngageConfig config = new WebEngageConfig.Builder()
 .SetDebugMode(true)
 .Build();

RegisterActivityLifecycleCallbacks(new WebEngageActivityLifeCycleCallbacks(this, config));
Alternatively, you can change log level anytime using below API.
C#
WebEngage.Get().SetLogLevel(Logger.Debug);
🚧
This is to be used only in development mode.
Location tracking
WebEngage Xamarin.Android SDK allows you to define location tracking accuracy, or to disable location tracking, which enables you to optimize for resources - device battery and data usage. Follow the steps below to set location tracking accuracy.
Add
Xamarin.GooglePlayServices.Location
from Nuget Package Manager.
Add the below location permission in your AndroidManifest.xml file under the
Properties
folder of your project.
XML
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
Use
SetLocationTrackingStrategy
to define location tracking accuracy. Note that this method is to be called after
WebEngage SDK initialization
.
Method 1: Setting location tracking strategy in
WebEngageConfig
C#
using Com.Webengage.Sdk.Android;
...

WebEngageConfig config = new WebEngageConfig.Builder()
 ...
 .SetLocationTrackingStrategy(LocationTrackingStrategy.AccuracyCity)
 .Build();
Method 2: Setting location tracking strategy dynamically
C#
using Com.Webengage.Sdk.Android;

...

WebEngage.Get().SetLocationTrackingStrategy(LocationTrackingStrategy.AccuracyBest);
Following are the options that you can use to define location tracking accuracy.
Location accuracy level
Description
AccuracyBest
Uses the highest level of accuracy. Recommended for using geofencing; consumes more device power.
Interval between location updates: 15 minutes
Fastest interval between location updates: 5 mins
Smallest displacement that can be measured: 1 km
AccuracyCity
Recommended for city-level location tracking; consumes less device power.
Interval between location updates: 3 hours
Fastest interval between location updates: 1 hour
Smallest displacement that can be measured: 20 km
AccuracyCountry
Recommended for country-level location tracking; consumes less power.
Interval between location updates: 12 hours
Fastest interval between location updates: 12 hours
Smallest displacement that can be measured: 100 km
Disabled
Disables location tracking by WebEngage SDK. With this value, WebEngage will neither track any user location nor update it on your WebEngage dashboard.
If you are using this configuration, you can manage location updates by using
setLocation
to manually set the location.
Apps targeting Android Marshmallow and above would need to
request
location permission from user and set location tracking to
true
or
false
from permission request
callback
depending on whether location permission is granted or not.
Updated
7 months ago
Callbacks
Xamarin.iOS
Copy Page
