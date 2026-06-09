# Legacy SDK v2

- URL: https://docs.webengage.com/docs/android-v2-sdk
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

SDK Changelogs
Android SDK
Legacy SDK v2
GETTING STARTED
1. Install the SDK
The easiest way to use WebEngage in your Android project is with
Maven
. WebEngage Android SDK is hosted on
jcenter
Maven repository.
Update your project's
build.gradle
script to include
jcenter
.
Groovy
repositories {
 ...
 
 jcenter()
 
 ...
}
Add dependencies for WebEngage, Android Support v4 and Google Play Services Ads in your module’s
build.gradle
.
Groovy
dependencies {
 compile 'com.webengage:android-sdk:2.+'
 compile 'com.android.support:support-v4:24.2.1' 
 compile 'com.google.android.gms:play-services-ads:10.0.1'
}
2. Modify AndroidManifest.xml
Add the following snippets in your AndroidManifest.xml.
Add your WebEngage License code within the
application
element.
XML
<meta-data
 android:name="com.webengage.sdk.android.key"
 android:value="YOUR_WEBENGAGE_LICENSE_CODE" />
🚧
Make sure you replace
YOUR_WEBENGAGE_LICENSE_CODE
with your WebEngage
license code
.
Set location tracking to true if you would like to run location based campaigns. User location is recorded for each of their tracked actions.
XML
<meta-data
 android:name="com.webengage.sdk.android.location_tracking"
 android:value="true"
/>
Declare
ExecutorService
to process WebEngage events and
EventLogService
to send events to WebEngage backend.
XML
<service android:name="com.webengage.sdk.android.ExecutorService" />
<service android:name="com.webengage.sdk.android.EventLogService" />
Define in-app messages’ visual user interface. Add this only if you are going to use
in-app messaging
.
XML
<activity
 android:name="com.webengage.sdk.android.actions.render.WebEngageActivity"
 android:theme="@android:style/Theme.Translucent"
 android:configChanges="orientation|screenSize" />
WebEngage
WebEngageReceiver
and
InstallTracker
within the
application
element.
XML
<receiver
 android:name="com.webengage.sdk.android.WebEngageReceiver">
 <intent-filter>
 <action android:name="com.webengage.sdk.android.intent.ACTION" />
 <category android:name="YOUR.PACKAGE.NAME" />
 </intent-filter>
</receiver>

<receiver
 android:name="com.webengage.sdk.android.InstallTracker"
 android:exported="true">
 <intent-filter>
 <action android:name="com.android.vending.INSTALL_REFERRER" />
 </intent-filter>
</receiver>
🚧
Android only supports one
BroadcastReceiver
for the
INSTALL_REFERRER
IntentFilter
. If your app or another SDK in your app is already listening for the
INSTALL_REFERRER
IntentFilter
to track user acquisition source on Android, follow our instructions for
using WebEngage in addition to other attribution providers
.
Permissions within the manifest element
XML
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.WAKE_LOCK" />
Set debug mode to true if you want to debug WebEngage SDK.
XML
<meta-data
 android:name="com.webengage.sdk.android.debug"
 android:value="true" /> <!-- only for debugging -->
3. Initialize the SDK
If you don’t have a custom
Application
class, create one and specify the
android:name
property in the the
application
element in
AndroidManifest.xml
.
XML
<application
 android:name=".MyApplication">
Add the following to your
Application
class.
a. Import the
WebEngage
package.
Java
import com.webengage.sdk.android.WebEngageActivityLifeCycleCallbacks
b. Initialize the SDK from the
onCreate
method.
Java
@Override
public void onCreate() {
 super.onCreate();
 registerActivityLifecycleCallbacks(new WebEngageActivityLifeCycleCallbacks(this));
}
🚧
If you support Android API level less than 14 then use
alternative initialization
instead of the above approach.
4. Configure ProGuard
This is only required if you use
ProGuard
to obfuscate your code. Update your project’s
proguard-rules.pro
file to include WebEngage exceptions as follows.
Text
-keep class com.webengage.sdk.android.**{*;}
-dontwarn com.webengage.sdk.android.**
Session lifecycle
WebEngage SDK automatically starts tracking user data (e.g., device model, OS version, device IDs) and engagement with the basic setup above. This data is stored on the device and is periodically uploaded in batches to reduce network and power usage, and to increase the likelihood of successful uploads. The upload cycle is based on the number of datapoints in local database and last synced time. This local database size is capped and is deleted as soon as it is successfully uploaded. WebEngage allows you to change this upload behavior during runtime, so that you can
make events sync faster
to WebEngage if available network connectivity is good.
WebEngage SDK also starts tracking user sessions with this basic setup. Upon app backgrounding, the SDK marks the current time. If the user returns to the app after more than 15 seconds since the user had last backgrounded the app, the SDK will close the previous session. If the user foregrounds the app within 15 seconds of the previous backgrounding, the previous session is resumed as if the user did not leave the app at all.
Next steps
Congratulations! You have now successfully integrated WebEngage SDK with your Android app and are now sending user session and
system event
data to WebEngage.
Note that it may take a few minutes for your data to show up on the WebEngage dashboard. We suggest you meanwhile proceed to read the next sections to learn how to:
Track user properties as attributes
Track user actions as events
Integrate push messaging
Integrate in-app messaging
We recommend doing these integrations before releasing your app for the first time with WebEngage.
ADVANCED
Event reporting strategy
WebEngage stores every datapoint in local database and sends them periodically to server in a background thread when a certain criteria is met. The criteria is based on the number of events in local database and last synced time.
WebEngage allows you to change the event reporting behavior during runtime, so that you can make events sync faster to WebEngage if available connectivity is good.
Java
WebEngage.get().setEventReportingStrategy(ReportingStrategy.FORCE_SYNC);
🚧
setEventReportingStrategy
is to be called only once in a session. The SDK remembers this setting unless your app is restarted.
By default, the reporting strategy is set to
ReportingStrategy.BUFFER
. See
ReportingStrategy
for details.
Fetch WebEngage configuration
Returns WebEngage configuration. See
WebEngageConfig
for details.
Java
WebEngageConfig weConfig = WebEngage.get().getWebEngageConfig();
Logging
Set log level for WebEngage. See Logger for details.
Java
WebEngage.get().setLogLevel(Logger.DEBUG);
🚧
This is to be used only in development mode.
Location tracking
Enable or disable location tracking during runtime.
Java
WebEngage.get().setLocationTracking(false);
Using WebEngage with other attribution providers
If you have an
InstallReferrer
already set up and do not want to change it, or you want some other
InstallReferrer
to be the primary one, you can still use WebEngage’s
InstallReferrer
for attribution tracking.
Pass the
Intent
broadcast received in the
BroadcastReceiver
of your primary
InstallReferrer
to
onReceive()
of WebEngage's
InstallReferrer
. This is illustrated below.
Java
public class PrimaryInstallTracker extends BroadcastReceiver {
 @Override
 public void onReceive(Context context, Intent intent) {
 WebEngage.get().analytics().onInstalled(intent);
 }
}
📘
Doing this is straightforward:
Set up a new
InstallReferrer
.
Declare it in
AndroidManifest.xml
.
Call the immutable
InstallReferrer
and WebEngage's
InstallReferrer
from the
onReceive()
of this new primary
InstallReferrer
.
Call other
InstallReferrer
s if you are using more attribution trackers.
Alternative initialization
Use this approach if you are targeting devices below Android API level 14.
Initialize WebEngage SDK from the
onCreate
of your
Application
class.
Java
public class MyApplication extends Application {
 @Override
 public void onCreate() {
 super.onCreate();
 WebEngage.engage(this);
 }
}
Manually call WebEngage's session tracking API from
onStart
and
onStop
of each of your activities.
Java
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
You are now ready to continue with the setup process
here
.
Updated
7 months ago
Android SDK
iOS SDK
Copy Page
