# Callbacks

- URL: https://docs.webengage.com/docs/android-callbacks
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
Callbacks
Callbacks are useful for understanding the lifecycle stages of WebEngage messages. All WebEngage callbacks are called on the main thread.
Push Message Callbacks
Implement your class
PushNotificationCallbacksImpl
with
PushNotificationCallbacks
and register it to WebEngage.
Java
Kotlin
import com.webengage.sdk.android.WebEngage;

public class MyApplication extends Application {

 @Override
 public void onCreate() {
 super.onCreate();
 WebEngage.registerPushNotificationCallback(new PushNotificationCallbacksImpl());
 }
}
class MyApplication : Application() {
 override fun onCreate() {
 super.onCreate()
 WebEngage.registerPushNotificationCallback(PushNotificationCallbacksImpl())

 }
}
Push Notification Received
This callback is invoked before push notification is shown. This allows you to customize the push message data received from WebEngage.
Java
Kotlin
PushNotificationData onPushNotificationReceived(Context context, PushNotificationData pushNotificationData);
override fun onPushNotificationReceived(
 context: Context?,
 pushNotificationData: PushNotificationData
 ): PushNotificationData?
Push Notification Shown
This callback is invoked after the notification is shown.
Java
Kotlin
void onPushNotificationShown(Context context, PushNotificationData pushNotificationData);
override fun onPushNotificationShown(
 context: Context?,
 pushNotificationData: PushNotificationData?
Push Notification Clicked
This callback is invoked when the user clicks the main intent (i.e. primary call to action) of the notification.
Return
true
if the click was handled by your app, or
false
to let WebEngage SDK handle it.
Java
Kotlin
boolean onPushNotificationClicked(Context context, PushNotificationData pushNotificationData);
override fun onPushNotificationClicked(
 context: Context?,
 pushNotificationData: PushNotificationData?
 ): Boolean
Push Notification Action Clicked
This callback is invoked when the user clicks the non-primary call to action button (if any) of the notification.
Return true if the click was handled by your app, or false to let WebEngage SDK handle it.
Java
Kotlin
boolean onPushNotificationActionClicked(Context context, PushNotificationData pushNotificationData, String buttonId);
override fun onPushNotificationActionClicked(
 context: Context?,
 pushNotificationData: PushNotificationData?,
 buttonId: String?
 ): Boolean
Push Notification Dismissed
This callback is invoked when the user dismisses the notification either by swiping it away or by clearing the system notification tray.
Java
Kotlin
void onPushNotificationDismissed(Context context, PushNotificationData pushNotificationData);
override fun onPushNotificationDismissed(
 context: Context?,
 pushNotificationData: PushNotificationData?
 )
🚧
Please Note
Read operation on
PushNotificationData
fields can be done from any push notification callback function.
Any changes done to
PushNotificationData
fields will be reflected only if they are called from
onPushNotificationReceived
callback. For example :
notificationData.getPrimeCallToAction().setAction("https://www.example.com", CallToAction.TYPE.LINK,context)
will be effective only if it is called from
onPushNotificationReceived
.
In-app Message Callbacks
In-app message callbacks can help you prevent conflicts with views in your app.
Implement your class
InAppNotificationCallbackImpl
with
InAppNotificationCallbacks
and register it to WebEngage.
Java
Kotlin
import com.webengage.sdk.android.WebEngage;

public class MyApplication extends Application {

 @Override
 public void onCreate() {
 super.onCreate();
 WebEngage.registerInAppNotificationCallback(new InAppNotificationCallbackImpl());
 }
}
class MyApplication : Application() {
 override fun onCreate() {
 super.onCreate()
 
WebEngage.registerInAppNotificationCallback(InAppNotificationCallback())
 }
}
In-app Message Received
This callback is invoked before the in-app message is shown to your users. It allows you to customize the UI, colors, CTAs (buttons) and content of the In-app message received from WebEngage before displaying it to your users.
Java
Kotlin
InAppNotificationData onInAppNotificationPrepared(Context context, InAppNotificationData inAppNotificationData);
override fun onInAppNotificationPrepared(
 context: Context?,
 inAppNotificationData: InAppNotificationData?
 ): InAppNotificationData
In-App Message Shown
This callback is invoked after the message is shown.
Java
Kotlin
void onInAppNotificationShown(Context context, InAppNotificationData inAppNotificationData);
override fun onInAppNotificationShown(
 context: Context?,
 inAppNotificationData: InAppNotificationData?
)
In-App Message Clicked
This callback is invoked when the user clicks the message. The ID of the button clicked is passed as
actionId
.
Return
true
if the click was handled by your app, or
false
to let WebEngage SDK handle it.
Java
Kotlin
boolean onInAppNotificationClicked(Context context, InAppNotificationData inAppNotificationData, String actionId);
override fun onInAppNotificationClicked(
 context: Context?,
 inAppNotificationData: InAppNotificationData?,
 actionId: String?
 ): Boolean
In-App Message Dismissed
This callback is invoked when the user dismisses the message.
Java
Kotlin
void onInAppNotificationDismissed(Context context, InAppNotificationData inAppNotificationData);
override fun onInAppNotificationDismissed(
 context: Context?,
 inAppNotificationData: InAppNotificationData?
)
Notification Callback Data (
InAppNotificationData inAppNotificationData
)
Data received from in-app callbacks adheres to the below format.
JSON
{
 "canClose": true,
 "layoutAttributes": {
 "posX": 0,
 "posY": 0,
 "TITLE_ALIGN": "CENTER",
 "image_url": "http://s3-ap-southeast-1.amazonaws.com/wk-test-static-files/76a9d10/a6b6e04d-43e9-4c09-b15f-8acffbcfcc1a.jpg",
 "TITLE_WRAP": false,
 "wvWidth": 100,
 "type": "BLOCKING",
 "wvHeight": 100,
 "fullScreen": false
 },
 "showTitle": true,
 "notificationEncId": "~13ssb59",
 "description": null,
 "canMinimize": true,
 "id": "173046a46",
 "isActive": true,
 "title": "My Title",
 "actions": [{
 "actionText": "Puma",
 "actionEId": "~64c71b",
 "actionTarget": "_top",
 "type": "DEEP_LINK",
 "actionLink": "webengage://com.webengage.inapptest/start_activity/com.webengage.inapptest.Activity1",
 "isPrime": true
 }],
 "config": {
 "titleColor": "#ffffff",
 "c2aBackgroundColor": "#411ad3",
 "c2aTextFont": "Open Sans",
 "titleFont": "Open Sans",
 "c2aTextColor": "#f7f2f2",
 "hideLogo": false
 },
 "direction": "ltr"
}
Lifecycle Callbacks
Lifecycle callbacks allow you to listen to GCM registered, GCM received, app installed and app upgraded events.
Implement your class
LifeCycleCallbacksImpl
with
LifeCycleCallbacks
and register it to WebEngage.
Java
Kotlin
import com.webengage.sdk.android.WebEngage;

public class MyApplication extends Application {

 @Override
 public void onCreate() {
 super.onCreate();
 WebEngage.registerLifeCycleCallback(new LifeCycleCallbacksImpl());
 }
}
class MyApplication : Application() {
 override fun onCreate() {
 super.onCreate()
 WebEngage.registerLifeCycleCallback(LifeCycleCallbacksImpl())
 }
}
GCM Registered
Java
Kotlin
void onGCMRegistered(Context context, final String regID);
override fun onGCMRegistered(context: Context?, regID: String?)
GCM Message Received
Java
Kotlin
void onGCMMessageReceived(Context context, final Intent intent);
override fun onGCMMessageReceived(context: Context?, intent: Intent?)
App Installed
Java
Kotlin
void onAppInstalled(Context context, final Intent intent);
override fun onAppInstalled(context: Context?, intent: Intent?)
App Upgraded
Java
Kotlin
void onAppUpgraded(Context context, final int oldVersion, final int newVersion);
override fun onAppUpgraded(context: Context?, oldVersion: Int, newVersion: Int)
New Session Started
Java
Kotlin
@Override
public void onNewSessionStarted() {

}
override fun onNewSessionStarted();
State Change Callbacks
State change callbacks are triggered whenever the state of the SDK changes.
Extend your class
StateChangeCallbackImpl
with
StateChangeCallbacks
and register it to WebEngage.
Java
Kotlin
import com.webengage.sdk.android.WebEngage;

public class MyApplication extends Application {
 @Override
 public void onCreate() {
 super.onCreate();
 WebEngage.registerStateChangeCallback(new StateChangeCallbackImpl());
 }
}
class MyApplication : Application() {
 override fun onCreate() {
 super.onCreate()
 WebEngage.registerStateChangeCallback(StateChangeCallbackImpl())
 }
}
🚧
It is recommended to register
StateChangeCallbacks
after SDK initialization.
Anonymous ID Changed
This callback is invoked when the Anonymous ID of the user is changed.
Java
Kotlin
public void onAnonymousIdChanged(Context context, String anonymousUserID);
override fun onAnonymousIdChanged(context: Context?, anonymousUserID: String?)
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
App In-line Content
Advanced
Copy Page
