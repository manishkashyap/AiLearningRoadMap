# Callbacks

- URL: https://docs.webengage.com/docs/xamarin-android-callbacks
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.Android
Callbacks
Callbacks are useful for understanding the lifecycle stages of WebEngage messages. All WebEngage callbacks are called on the main thread.
Push message callbacks
Implement your class with
IPushNotificationCallbacks
using the callbacks you want to use from below ones and register it in your Application class as shown.
C#
...
using Com.Webengage.Sdk.Android;
using Com.Webengage.Sdk.Android.Callbacks;
...

 [Application]
 public class MyApplication : Application
 {
 ...

 public override void OnCreate()
 {
 base.OnCreate();
 ...

 WebEngage.RegisterPushNotificationCallback(new MyPushNotificationCallbacks());
 }
 }
}
Push Notification Received
This callback is invoked before push notification is shown. This allows you to customize the push message data received from WebEngage.
C#
using Android.Content;
using Android.Util;
using Com.Webengage.Sdk.Android.Actions.Render;
using Com.Webengage.Sdk.Android.Callbacks;

namespace YourNamespace
{
 public class MyPushNotificationCallbacks : Java.Lang.Object, IPushNotificationCallbacks
 {
 public MyPushNotificationCallbacks()
 {
 }

 public PushNotificationData OnPushNotificationReceived(Context context, PushNotificationData pushNotificationData)
 {
 ...
 return p1;
 }
 }
}
Push Notification Shown
This callback is invoked after the notification is shown.
C#
using Android.Content;
using Android.Util;
using Com.Webengage.Sdk.Android.Actions.Render;
using Com.Webengage.Sdk.Android.Callbacks;

namespace MyNamespace
{
 public class MyPushNotificationCallbacks : Java.Lang.Object, IPushNotificationCallbacks
 {
 public MyPushNotificationCallbacks()
 {
 }

 public void OnPushNotificationShown(Context context, PushNotificationData pushNotificationData)
 {
 ...
 }
 }
}
Push Notification Clicked
This callback is invoked when the user clicks the main intent (i.e. primary call to action) of the notification.
Return
true
if the click was handled by your app, or
false
to let WebEngage SDK handle it.
C#
using Android.Content;
using Android.Util;
using Com.Webengage.Sdk.Android.Actions.Render;
using Com.Webengage.Sdk.Android.Callbacks;

namespace MyNamespace
{
 public class MyPushNotificationCallbacks : Java.Lang.Object, IPushNotificationCallbacks
 {
 public MyPushNotificationCallbacks()
 {
 }

 public bool OnPushNotificationClicked(Context context, PushNotificationData pushNotificationData)
 {
 ...
 return false;
 }
 }
}
Push Notification Action Clicked
This callback is invoked when the user clicks the non-primary call to action button (if any) of the notification.
Return true if the click was handled by your app, or false to let WebEngage SDK handle it.
C#
using Android.Content;
using Android.Util;
using Com.Webengage.Sdk.Android.Actions.Render;
using Com.Webengage.Sdk.Android.Callbacks;

namespace MyNamespace
{
 public class MyPushNotificationCallbacks : Java.Lang.Object, IPushNotificationCallbacks
 {
 public MyPushNotificationCallbacks()
 {
 }

 public bool OnPushNotificationActionClicked(Context context, PushNotificationData pushNotificationData, string buttonId)
 {
 ...
 return false;
 }
 }
}
Push Notification Dismissed
This callback is invoked when the user dismisses the notification either by swiping it away or by clearing system notification tray.
C#
using Android.Content;
using Android.Util;
using Com.Webengage.Sdk.Android.Actions.Render;
using Com.Webengage.Sdk.Android.Callbacks;

namespace MyNamespace
{
 public class MyPushNotificationCallbacks : Java.Lang.Object, IPushNotificationCallbacks
 {
 public MyPushNotificationCallbacks()
 {
 }

 public void OnPushNotificationDismissed(Context context, PushNotificationData pushNotificationData)
 {
 ...
 }
 }
}
📘
Read operation on
PushNotificationData
fields can be done from any push notification callback function.
Any changes done to
PushNotificationData
fields will be reflected only if they are called from
OnPushNotificationReceived
callback. For example :
notificationData.getPrimeCallToAction().setAction("http://www.example.com", CallToAction.TYPE.LINK,context)
will be effective only if it is called from
OnPushNotificationReceived
.
In-app message callbacks
In-app message callbacks can help you prevent conflicts with views in your app.
Implement your class with
IInAppNotificationCallbacks
using the callbacks you want to use from below ones and register it in your Application class as shown.
C#
...
using Com.Webengage.Sdk.Android;
using Com.Webengage.Sdk.Android.Callbacks;
...

 [Application]
 public class MyApplication : Application
 {
 ...

 public override void OnCreate()
 {
 base.OnCreate();
 ...

 WebEngage.RegisterInAppNotificationCallback(new MyInAppNotificationCallbacks());
 }
 }
}
In-app Message Received
This callback is invoked before the in-app message is shown. t allows you to customize the UI, colors, CTAs (buttons) and content of the In-app message received from WebEngage before displaying it to your users.
C#
using Android.Content;
using Android.Util;
using Com.Webengage.Sdk.Android.Actions.Render;
using Com.Webengage.Sdk.Android.Callbacks;

namespace MyNamespace
{
 public class MyInAppNotificationCallbacks : Java.Lang.Object, IInAppNotificationCallbacks
 {
 public MyInAppNotificationCallbacks()
 {
 }

 public InAppNotificationData OnInAppNotificationPrepared(Context context, InAppNotificationData inAppNotificationData)
 {
 ...
 return p1;
 }
 }
}
In-App Message Shown
This callback is invoked after the message is shown.
C#
using Android.Content;
using Android.Util;
using Com.Webengage.Sdk.Android.Actions.Render;
using Com.Webengage.Sdk.Android.Callbacks;

namespace MyNamespace
{
 public class MyInAppNotificationCallbacks : Java.Lang.Object, IInAppNotificationCallbacks
 {
 public MyInAppNotificationCallbacks()
 {
 }

 public void OnInAppNotificationShown(Context context, InAppNotificationData inAppNotificationData)
 {
 ...
 }
 }
}
In-App Message Clicked
This callback is invoked when the user clicks the message. The ID of the button clicked is passed as
actionId
.
Return
true
if the click was handled by your app, or
false
to let WebEngage SDK handle it.
C#
using Android.Content;
using Android.Util;
using Com.Webengage.Sdk.Android.Actions.Render;
using Com.Webengage.Sdk.Android.Callbacks;

namespace MyNamespace
{
 public class MyInAppNotificationCallbacks : Java.Lang.Object, IInAppNotificationCallbacks
 {
 public MyInAppNotificationCallbacks()
 {
 }

 public bool OnInAppNotificationClicked(Context context, InAppNotificationData inAppNotificationData, string actionId)
 {
 ...
 return false;
 }
 }
}
In-App Message Dismissed
This callback is invoked when the user dismisses the message.
C#
using Android.Content;
using Android.Util;
using Com.Webengage.Sdk.Android.Actions.Render;
using Com.Webengage.Sdk.Android.Callbacks;

namespace MyNamespace
{
 public class MyInAppNotificationCallbacks : Java.Lang.Object, IInAppNotificationCallbacks
 {
 public MyInAppNotificationCallbacks()
 {
 }

 public void OnInAppNotificationDismissed(Context context, InAppNotificationData inAppNotificationData)
 {
 ...
 }
 }
}
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
Lifecycle callbacks
Lifecycle callbacks allow you to listen to GCM registered, GCM received, app installed and app upgraded events.
Implement your class with
ILifeCycleCallbacks
using the callbacks you want to use from below ones and register it in your Application class as shown.
C#
...
using Com.Webengage.Sdk.Android;
using Com.Webengage.Sdk.Android.Callbacks;
...

 [Application]
 public class MyApplication : Application
 {
 ...

 public override void OnCreate()
 {
 base.OnCreate();
 ...

 WebEngage.RegisterLifeCycleCallback(new MyLifeCycleCallbacks());
 }
 }
}
GCM Registered
C#
public class MyLifecycleCallbacks : Java.Lang.Object, ILifeCycleCallbacks
{
 public void OnGCMRegistered(Context context, string regID)
 {
 ...
 }
}
GCM Message Received
C#
public class MyLifecycleCallbacks : Java.Lang.Object, ILifeCycleCallbacks
{
 public void OnGCMMessageReceived(Context context, Intent intent)
 {
 ...
 }
}
App Installed
C#
public class MyLifecycleCallbacks : Java.Lang.Object, ILifeCycleCallbacks
{
 public void OnAppInstalled(Context context, Intent intent)
 {
 ...
 }
}
App Upgraded
C#
public class MyLifecycleCallbacks : Java.Lang.Object, ILifeCycleCallbacks
{
 public void OnAppInstalled(Context context, Intent intent)
 {
 ...
 }

 public void OnAppUpgraded(Context context, int oldVersion, int newVersion)
 {
 ...
 }
}
State change callbacks
State change callbacks are triggered whenever the state of the SDK changes.
Extend your class with
StateChangeCallbacks
using the callbacks you want to use from below ones and register it in your Application class as shown.
C#
...
using Com.Webengage.Sdk.Android;
using Com.Webengage.Sdk.Android.Callbacks;
...

 [Application]
 public class MyApplication : Application
 {
 ...

 public override void OnCreate()
 {
 base.OnCreate();
 ...

 WebEngage.RegisterStateChangeCallback(new MyStateChangeCallbacks());
 }
 }
}
📘
It is recommended to register
StateChangeCallbacks
after SDK initialization.
Anonymous ID changed
This callback is invoked when the Anonymous ID of the user is changed.
C#
public class MyLifecycleCallbacks : Java.Lang.Object, ILifeCycleCallbacks
{
 public void OnAnonymousIdChanged(Context context, String anonymousUserID)
 {
 ...
 }
}
Updated
7 months ago
In-app Messaging
Advanced
Copy Page
