# Getting Started

- URL: https://docs.webengage.com/docs/android-getting-started
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
Getting Started
1. Installation
The easiest way to use WebEngage in your Android project is with
Maven
. WebEngage Android SDK is hosted on
mavenCentral
Maven repository.
Add dependencies of WebEngage in the
app/build.gradle
file.
Groovy
dependencies {
 implementation 'com.webengage:android-sdk:4.+'
}
🚧
Please Note
After application build, WebEngage SDK size is around 345kB if
minifyEnabled
is set to
false
. The size will be less than 200kB if
minifyEnabled
is set to
true
.
2. Initialization
Step 1:
Import WebEngage packages in your Application class.
Java
import com.webengage.sdk.android.WebEngageConfig;
import com.webengage.sdk.android.WebEngageActivityLifeCycleCallbacks;
Step 2:
Initialize WebEngage SDK with your license code from
onCreate
callback of your Application class as shown below.
Java
Kotlin
@Override
public void onCreate() {
 super.onCreate();
 WebEngageConfig webEngageConfig = new WebEngageConfig.Builder()
 .setWebEngageKey(YOUR_WEBENGAGE_LICENSE_CODE)
 .setDebugMode(true) // only in development mode
 .build();
 registerActivityLifecycleCallbacks(new WebEngageActivityLifeCycleCallbacks(this, webEngageConfig));

}
override fun onCreate() {
 super.onCreate()
 val webEngageConfig = WebEngageConfig.Builder()
 .setWebEngageKey(YOUR_WEBENGAGE_LICENSE_CODE)
 .setDebugMode(true) // only in development mode
 .build()
 registerActivityLifecycleCallbacks(
 WebEngageActivityLifeCycleCallbacks(
 this,
 webEngageConfig
 )
 )
 }
Please replace
YOUR_WEBENGAGE_LICENSE_CODE
with your WebEngage license code in the code snippets provided above.
Locating your WebEngage license code
As shown above, navigate to the
Account Setup
section to find your license code.
Your License Code might start with tilde (
~
).
It is the value of
manifest key
:
com.webengage.sdk.android.key
.
Step 3: Add
meta-data
under in the
AndroidManifest.xml
file
🚧
IMPORTANT: Identifying Your Data Center
If your WebEngage dashboard URL starts with
dashboard.webengage.com
, then it means you're using our
Global Data Center.
(All data is stored here by default).
If you have specifically asked for your data to be stored in our
India Data Center
in your contract with WebEngage, then your dashboard url will start with
dashboard.in.webengage.com
.
If you have specifically asked for your data to be stored in our
Saudi Arabia Data Center
in your contract with WebEngage, then your dashboard url will start with
dashboard.ksa.webengage.com
.
Thus, depending on your data center, add the appropriate
meta-data
under the
application
tag of your
AndroidManifest.xml
file:
Data Center
Meta Data Tag
Global (US)
<meta-data android:name="com.webengage.sdk.android.environment" android:value="us" />
India
<meta-data android:name="com.webengage.sdk.android.environment" android:value="in" />
Saudi Arabia
<meta-data android:name="com.webengage.sdk.android.environment" android:value="ksa" />
🚧
Please Note
If you support Android API level less than 14 then use
alternative initialization
instead of the above approach.
If you have multiple apps, you can use the same license code for integrating all of them.
Step 4:
Disable automatic backup inside the
application
tag in your
AndroidManifest.xml
file.
XML
<application
 ...
 android:allowBackup="false"
 ....
 >
If your application needs
allowBackup
to be set as
true
, then follow the steps below:
a. Create backup rules inside res/xml folder (
res/xml/my_backup_rules.xml
)
XML
<?xml version="1.0" encoding="utf-8"?>
 <full-backup-content>
 <exclude domain="sharedpref" path="webengage_prefs.txt.xml" />
 <exclude domain="sharedpref" path="webengage_volatile_prefs.txt.xml" />
 <exclude domain="database" path="event_data.db" />
 <exclude domain="database" path="http_data.db" />
 <exclude domain="database" path="user_data.db" />
 <exclude domain="file" path="we_http_cache" />
b. Add backup file inside application tag in your AndroidManifest.xml
XML
<application
 ...
 android:allowBackup="true"
 android:fullBackupContent="@xml/my_backup_rules">
3. Attribution Tracking
Add the following
Google Install referrer
library in your
app/build.gradle
file (ensure that the SDK version being used is >= 3.16.0):
Groovy
dependencies {
 implementation 'com.android.installreferrer:installreferrer:2.2'
}
🚧
Please Note
App Installed
event and
First Acquisition Details
data in user profile will not be tracked on your Android app unless you follow the above step.
4. Additional steps (Optional)
If you are using WebViews in your Android app, check out
WebEngage JavaScript bridge
.
For other integration options such as
location tracking
, please refer to the
Advanced section
.
Session Lifecycle
WebEngage SDK automatically starts tracking user data (e.g., device model, OS version, device IDs) and engagement with the basic setup above. This data is stored on the device and is periodically uploaded in batches to reduce network and power usage, and to increase the likelihood of successful uploads. The upload cycle is based on the number of datapoints in local database and last synced time. This local database size is capped and is deleted as soon as it is successfully uploaded. WebEngage allows you to change this upload behavior during runtime, so that you can
make events sync faster
to WebEngage if available network connectivity is good.
WebEngage SDK also starts tracking user sessions with this basic setup. Upon app backgrounding, the SDK marks the current time. If the user returns to the app after more than 15 seconds since the user had last backgrounded the app, the SDK will close the previous session. If the user foregrounds the app within 15 seconds of the previous backgrounding, the previous session is resumed as if the user did not leave the app at all. Also, if the user force kills the app and launches it again after being force killed (irrespective of the time gap between force kill and launch), the SDK will close the previous session upon force-kill and start a new session upon app launch.
Configuring Session Timeout limit
📘
Configure Session timeout limit
Session inactivity time limit can be configured upto 60 min. To configure this time kindly update to SDK v3.19.2 post which you can either reach out to us on
[email protected]
or you can follow the steps mentioned below.
Note:
This capability is currently supported for Native - Android and iOS, React native and Flutter.
To update your session timeout limit, kindly update your Android SDK to v3.19.2 or above and follow the steps below:
Java
Kotlin
WebEngageConfig webEngageConfig = new WebEngageConfig.Builder()
 .setWebEngageKey(YOUR_WEBENGAGE_LICENSE_CODE)
 .setDebugMode(true) // only in development mode
 .setSessionDestroyTime(40) //Value to be set in seconds
 .build();
val webEngageConfig: WebEngageConfig = WebEngageConfig.Builder()
 .setWebEngageKey(YOUR_WEBENGAGE_LICENSE_CODE)
 .setDebugMode(true) // only in development mode
 .setSessionDestroyTime(40) //Value to be set in seconds
 .build()
🚧
Congratulations!
You have now successfully integrated the WebEngage SDK with your Android app and are sending user session and
system events
data to your dashboard. Please note that it may take up to a few minutes for your data to reflect on the dashboard.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Advertising ID tracking
🚧
Please Note
Adding the Google Play Service Ads dependency is optional. Use it only if you have integrations enabled with other attribution partners. Kindly, upgrade to the latest WebEngage version to enable proper tracking of GAID on Android 13 devices and above. Check out
this
section for changes in Advertising ID in Android 13 and above.
For tracking the Google Advertising ID, add a dependency of Google Play Service Ads in your
app/build.gradle
file.
Groovy
dependencies {
 implementation 'com.google.android.gms:play-services-ads:20.2.0'
}
Add your AdMob app ID to your app's
AndroidManifest.xml
file as follows: You can find or generate your AdMob ID
here
XML
<manifest>
 <application>
 <meta-data
 android:name="com.google.android.gms.ads.APPLICATION_ID"
 android:value="ca-app-pub-xxxxxxxxxxxxxxxx~yyyyyyyyyy"/>
 </application>
</manifest>
Once above steps have been implemented, WebEngage will start tracking the advertising ID.
Tracking Advertising ID for selected users
WebEngage tracks the advertising ID for all users. If you want to track the Advertising ID for selective users, follow below steps.
In the WebEngage Config Builder, disable auto GAID tracking by using
.setAutoGAIDTracking(false)
as follows.
Java
Kotlin
WebEngageConfig.Builder builder = new WebEngageConfig.Builder()
 .setWebEngageKey(LICENSE_CODE)
 .setAutoGAIDTracking(false);
val builder: WebEngageConfig.Builder = WebEngageConfig.Builder()
 .setWebEngageKey(LICENSE_CODE)
 .setAutoGAIDTracking(false)
You can then enable the advertisement ID tracking for any user by using below code.
Java
Kotlin
WebEngage.get().startGAIDTracking();
WebEngage.get().startGAIDTracking()
🚧
Please Note
This is supported from WebEngage SDK
v4.4.3
.
After the user logs out, the GAID tracking will be disabled for the new user by default. You need to call the
startGAIDTracking()
function for the new user again.
Once enabled, for the given user, the advertising ID will be tracked for the device till the user calls the logout function.
Google Advertisement ID changes (Android 13 and above)
In late 2021, Google announced updates to Google Play service policies in relation to collecting Android Advertising ID.
Read here
to more about the changes.
Due to these changes, to access the device's Advertising ID, apps targeting Android 13 (API 33) and higher will need to declare a regular Google Play services permission in their manifest file.
The permission is granted at installation time because it is not a run-time authorization.
SDK changes
The AD ID permission is now declared in the SDK's AndroidManifest.xml as of WebEngage Android SDK V3.21.0. The SDK's manifest automatically combines with your app's manifest when the app is developed, adding the permission even if the app doesn't explicitly declare it. There won't be a collision if the permission is present in both the app and the SDK.
XML
<manifest ...>
 <!-- Required only if your app targets Android 13 or higher. -->
 <uses-permission android:name="com.google.android.gms.permission.AD_ID"/>

 <application ...>
 ...
 </application>
</manifest>
Kids Apps:
According to
Google’s Policy
, apps that target children must not transmit the Advertising ID. If you're building an app for kids and you are using SDK V3.21.0 and above, you must revoke the AD_ID permission.
XML
<uses-permission android:name="com.google.android.gms.permission.AD_ID" tools:node="remove"/>
Impact on Hybrid SDKs (React, Cordova, Flutter. etc.)
Refer these
React
,
Cordova
and
Flutter
documents to make your apps compatible with Android 13 Advertising ID policy changes.
Updated
7 months ago
So, what's next?
We recommend that you implement the following integrations before releasing your app for the first time with WebEngage.
Track User Properties as User Attributes
Track User Actions as Events
Configure Push Messaging
Configure In-app Messaging
Copy Page
