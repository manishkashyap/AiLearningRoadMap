# Updating the SDK

- URL: https://docs.webengage.com/docs/android-updating-the-sdk
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Updating the SDK
From 2.x.x to 3.x.x
Google Cloud Messaging integration changes
Starting with version 3, WebEngage SDK uses a separate Push Receiver for handling messages from GCM. So, below changes are required
only
if the value of meta data tag
com.webengage.sdk.android.auto_gcm_registration
is set to
true
in your AndroidManifest.xml.
Remove
WebEngageReceiver
from AndroidManifest.xml.
XML
<meta-data
 android:name="com.webengage.sdk.android.auto_gcm_registration"
 android:value="true" /> 
<!--<receiver-->
 <!--android:name="com.webengage.sdk.android.WebEngageReceiver"-->
 <!--android:permission="com.google.android.c2dm.permission.SEND">-->
 <!--<intent-filter>-->
 <!--<action android:name="com.google.android.c2dm.intent.RECEIVE" />-->
 <!--<action android:name="com.webengage.sdk.android.intent.ACTION" />-->
 <!--<category android:name="YOUR.PACKAGE.NAME" />-->
 <!--</intent-filter>-->
<!--</receiver>-->
Add WebEngagePushReceiver in your AndroidManifest file under application tag.
XML
<receiver
 android:name="com.webengage.sdk.android.WebEngagePushReceiver"
 android:permission="com.google.android.c2dm.permission.SEND">
 <intent-filter>
 <action android:name="com.google.android.c2dm.intent.RECEIVE" />
 <category android:name="${applicationId}" />
 </intent-filter>
</receiver>
From 1.x.x to 2.x.x
Default value of meta-data
com.webengage.sdk.android.auto_gcm_registration
has been changed from
true
to
false
. If above meta-data is
not
present in your AndroidManifest.xml file then insert the same by following our
Push Notification set-up guide
.
WebEngage.get().setRegistrationID(String registrationID, String projectNumber)
has been deprecated. Use
WebEngage.get().setRegistrationID(String registrationID)
.
setRegistrationID
now only accepts GCM/FCM registered token.
From (SDK version <= 1.7) to (SDK version >= 1.8)
Remove
WebEngageCallback
annotation from all your callback implementations.
Manually register your
push
,
in-app
and
lifecycle
callback implementations to WebEngage.
Remove below lines from your ProGuard file.
Text
-keep class * implements com.webengage.sdk.android.callbacks.PushNotificationCallbacks{*;}
-keep class * implements com.webengage.sdk.android.callbacks.LifeCycleCallbacks{*;}
-keep class * implements com.webengage.sdk.android.callbacks.InAppNotificationCallbacks{*;}
Updated
7 months ago
Getting Started
Copy Page
