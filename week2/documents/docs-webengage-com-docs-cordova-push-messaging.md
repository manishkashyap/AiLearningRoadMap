# Push Messaging

- URL: https://docs.webengage.com/docs/cordova-push-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Cordova
Push Messaging
Push Notifications are messages that pop up on mobile devices. App publishers can send them at any time; even if the recipients aren’t currently engaging with the app or using their devices.
🚧
Before continuing, please ensure that you have
added the WebEngage SDK to your app
.
Android (FCM Integration)
Step 1:
Add the following plugin to your Cordova project.
cordova plugin add https://github.com/WebEngage/cordova-plugin-android-fcm.git --fetch
Step 2:
Save the
google-services.json
file in the root of your project directory.
Follow the steps under
Android FCM Documentation
to get the
google-services.json
file from your Firebase Cloud account.
Step 3:
Update FCM token on app launch.
Send FCM token to WebEngage SDK in your
wwww/js/index.js
file.
JavaScript
var app = {
 ...
 onDeviceReady: function() {
 ...

 androidfcm.updateToken();
 }
}
Run and test push notifications from WebEngage dashboard on your Android app.
Step 4:
Fetch FCM token
To fetch the FCM token, add the below code inside
wwww/js/index.js
file.
JavaScript
var app = {
 ...
 onDeviceReady: function() {
 ...
 androidfcm.getToken(function onSuccess(token) {
 console.log("FCM Token: " + token);
 }, function onError(error) {
 console.error("Error getting token: " + error);
 });
 
 }
}
And you're good to go!
GCM to FCM Migration
Step 1:
Follow the
FCM Integration steps
.
Step 2:
Remove the following from your
config.xml file
, under Android Platform tag.
XML
<widget ... xmlns:android="http://schemas.android.com/apk/res/android">
 ...
 <platform name="android">
 <config-file parent="/manifest/application" target="AndroidManifest.xml">
 ...

 <!-- Remove these meta-data and receiver tags -->
 <!--
 <meta-data 
 android:name="com.webengage.sdk.android.project_number" android:value="$12345678910" />

 <meta-data 
 android:name="com.webengage.sdk.android.auto_gcm_registration" 
 android:value="true" />

 <receiver 
 android:name="com.webengage.sdk.android.WebEngagePushReceiver" android:permission="com.google.android.c2dm.permission.SEND">
 <intent-filter>
 <action android:name="com.google.android.c2dm.intent.RECEIVE" />
 <category android:name="${applicationId}" />
 </intent-filter>
 </receiver>
 -->
 </config-file>
 <config-file parent="/manifest" target="AndroidManifest.xml">
 ...
 <!-- Remove these permissions -->
 <!--
 <uses-permission android:name="com.google.android.c2dm.permission.RECEIVE" />
 <uses-permission android:name="${applicationId}.permission.C2D_MESSAGE" />
 <permission android:name="${applicationId}.permission.C2D_MESSAGE" android:protectionLevel="signature" />
 -->
 </config-file>
 </platform>
 ...
</widget>
Making your app compatible with Android 13 push changes
From Android 13 onwards, clients will have to explicitly ask permissions from end user to send push notifications. This means, client will NOT recieve push opted in as true once the app is installed by the end user, unless the user explicitly subscribes for same.
To make sure your app is compatible with Android 13 changes, kindly follow these steps:
Step 1. Kindly refer to official
Google documentation
to make your application compatible with the same.
Step 2. On the basis of the permission provided by the user, pass the status to WebEngage by following the code snippet below:
JavaScript
webengage.user.setDevicePushOptIn(true)
🚧
Please Note
Pass the boolean value
true
or
false
depending on the permission the user has specified. If users denies the permission, they will not receive push alerts.
Push permission Prompt trigger to be managed by the App.
👍
And you are good to go!
iOS
Step 1:
Enable
Push Notifications
under capabilities tab in your Xcode.
Step 2:
Add
WEGApnsAutoRegister
to
info.plist
with value
true
in
config.xml
file as shown below.
XML
<widget ...>
 ...
 <platform name="ios">
 ...
 <config-file parent="WEGApnsAutoRegister" target="*-Info.plist">
 <true />
 </config-file>
 </platform>
</widget>
And you're good to go!
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away.
Updated
7 months ago
Tracking Events
In-app Messaging
Copy Page
