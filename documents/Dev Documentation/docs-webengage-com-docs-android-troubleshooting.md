# Troubleshooting

- URL: https://docs.webengage.com/docs/android-troubleshooting
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
Troubleshooting
1. How do I know if Android SDK integration is successful?
To check whether the integration is successful or not, you can monitor debug logs from WebEngage SDK in Android Studio.
To enable debug mode, enable logs from WebEngage SDK during initialization as shown below.
Java
WebEngageConfig webEngageConfig = new WebEngageConfig.Builder()
 .setDebugMode(true)
 .build();
WebEngage.engage(this.getApplicationContext(), webEngageConfig);
Now clean, build and launch your application, and set log level of Android Studio as Verbose with filter as
WebEngage
.
You should start seeing debug logs. If integration is successful, "WebEngage Successfully Initialized" will be logged. Else, "WebEngage Initialization Failed" will be logged along with error message.
Successful integration sample logs
Unsuccessful integration sample logs.
2. Why are Users/ Events not showing up in the dashboard even after successful SDK integration?
Make sure that WebEngage SDK is
successfully integrated
.
Make sure that you have entered the correct
License Code
while
initializing the SDK
from
onCreate
callback of your Application class.
If there are any network issues (either from your device or from WebEngage servers) then "Event Logging failed, scheduling next sync" should be logged in your console. This indicates that events tracked in SDK are not being successfully reported to WebEngage servers. If your device has network access but you still do not see data being reflected on the dashboard, contact WebEngage support at [
[email protected]
](mailto:
[email protected]
).
📘
If you are seeing "Events successfully Logged to server, scheduling next sync" in your logs, then the events are being successfully reported to WebEngage servers and should be reflected on your dashboard within 2-3 mins. If you do not see data being reflected on the dashboard within 5 minutes,
contact WebEngage support
.
3. How can I get FCM registration ID & messages from WebEngage SDK?
If FCM registration and messaging are handled by WebEngage SDK, you need to implement
Lifecycle callbacks
to receive FCM registration ID and messages.
4. Why am I unable to receive Push/ In-app Notification callbacks?
A few reasons include:
For WebEngage
SDK version < 1.8
make sure that:
You have annotated your callback implementation class(es) with
WebEngageCallback.
Your callback implementation class(es) resides inside your declared application package.
For WebEngage
SDK version >= 1.8 and <= 1.9.7
make sure that:
You are properly registering your callbacks to WebEngage SDK.
Your app is holding a strong reference to your callback implementation.
_For WebEngage_SDK version >= 1.9.8
, ensure that you are properly registering your callbacks to WebEngage SDK.
5. Why do I see the error, '
Android credentials could not be saved as the values entered are invalid
,' in my dashboard?
You will see this error if the GCM/FCM key is found to be invalid.
To fix this:
Check for any other typos that might have occurred while pasting your GCM key on the dashboard.
Clear IP whitelist, if any, that might be associated with this Server Key from your Google API console.
Create a new Server Key and use this on the dashboard.
6. How can I update the WebEngage Android SDK to the latest version?
From 2.x.x to 3.x.x
Google Cloud Messaging integration changes
Starting with version 3, WebEngage SDK uses a separate Push Receiver for handling messages from GCM. So, below changes are required
only
if the value of meta data tag
com.webengage.sdk.android.auto_gcm_registration
is set to
true
in your AndroidManifest.xml.
Step 1:
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
Step 2:
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
Step 1:
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
Step 2:
WebEngage.get().setRegistrationID(String registrationID, String projectNumber)
has been deprecated. Use
WebEngage.get().setRegistrationID(String registrationID)
.
setRegistrationID
now only accepts GCM/FCM registered token.
From (SDK version <= 1.7) to (SDK version >= 1.8)
Step 1:
Remove
WebEngageCallback
annotation from all your callback implementations.
Step 2:
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
7. Why did I receive an email from Google stating that I am using a non-compliant version of WebEngage SDK?
Your app is using the Webengage SDK, which collects Advertiser ID and Android ID. Persistent device identifiers may not be linked to other personal and sensitive user data or resettable device identifiers.You may consider upgrading to a policy-compliant version of this SDK, if available from your SDK provider, or removing the SDK. Google is not endorsing or recommending any third-party software. Please consult the SDK provider for further information.
You will receive this mail if you have any release track with an older version of WebEngage SDK. We suggest you to follow below steps:
Make sure to use the latest WebEngage SDK version. Refer
Change Logs
for the latest version of the WebEngage SDK.
Further, read through the User Data policy for more details and accordingly make appropriate changes to your app, and be sure to address the issue identified above. In addition to your Production release, if you have other release types that you use for testing and/or quality assurance checks (for example, Internal test, Closed, Open), please make sure to update those tracks as well.
Check that your app is compliant with all other Developer Program Policies. Additional enforcement could occur if there are further policy violations.
Sign in to your Play Console, upload the modified policy compliant APK across all tracks, and deactivate the non-compliant APK(s).
Click
Manage track > Create new release
If the release with the violating app bundles / APKs are in a draft state, discard the release.
Otherwise, add the policy compliant version of app bundles / APKs.
Make sure the non-compliant version is under the
Not Included
section of this release.
Enter a release name and click Save. Once saved, click Review release, then proceed to roll out the release to 100%.
If the non-compliant versions are released to multiple tracks, repeat step 5 in each track.
Submit the update to your app.
We hope this has helped you integrate your Android app with WebEngage. Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
Push troubleshooting guide
Copy Page
