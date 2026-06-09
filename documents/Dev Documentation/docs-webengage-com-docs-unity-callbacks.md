# Unity Callbacks

- URL: https://docs.webengage.com/docs/unity-callbacks
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Unity.iOS
Unity Callbacks
Callbacks are useful for understanding the lifecycle stages of WebEngage events. All WebEngage callbacks are called on the main thread.
To get started, import below statements to access WebEngage bridge functionalities
C#
using WebEngageBridge;
using static WebEngageBridge.WebEngage;
Push Message Callbacks (Clicked)
create a callback method in which you wish to receive push notification clicked callback
C#
// Push Notification Callbacks
[AOT.MonoPInvokeCallback(typeof(callback))]
public static void handlepushNotificationClicked(string json)
{
 Debug.Log("/*/*/*/* UNity Callback received on PUSH NOTIFICATION CLICKED");
}
To receive callbacks, you must now register this method with WebEngage Bridge as shown below (This can be done in the start method of your class):
C#
WebEngage.setPushClickCallBack(handlepushNotificationClicked);
In-app notifications callbacks
📘
In order to use In-app notification callbacks, follow the
import step
present at start of document.
In-App Notification Prepared
This callback gets triggered before the notification is shown to your users. It allows you to customize the UI, colors, CTAs (buttons) and content of the In-app message received from WebEngage before displaying it.
Create a method in which you wish to receive callback as mentioned below
C#
[AOT.MonoPInvokeCallback(typeof(callback))]
public static void handleInAppNotificationPrepared(string json)
{
 Debug.Log("/*/*/*/* UNity Callback received on InAppNotificationPrepared");
 Debug.Log("/*/*/*/* isSDKInitialised" + WebEngage.getIsSDKInitialised());
}
To receive callbacks, you must now register this method with WebEngage Bridge as shown below.
This can be done in start method of your class
C#
WebEngage.setInAppPreparedCallBack(handleInAppNotificationPrepared);
In-App Notification Shown
This callback gets triggered after the in-app notification is shown.
Create a method in which you wish to receive callback as mentioned below
C#
[AOT.MonoPInvokeCallback(typeof(callback))]
public static void handleInAppNotificationShown(string json)
{
 Debug.Log("/*/*/*/* UNity Callback received on InAppNotificationShown");
}
To receive callbacks, you must now register this method with WebEngage Bridge as shown below.
This can be done in start method of your class
C#
WebEngage.setInAppShownCallBack(handleInAppNotificationShown);
In-App Notification Clicked
This callback gets triggered when the user clicks the call to action button on the notification.
Action details will be come as json string in parameters
Create a method in which you wish to receive callback as mentioned below
C#
[AOT.MonoPInvokeCallback(typeof(callback))]
public static void handleInAppNotificationClicked(string json)
{
 Debug.Log("/*/*/*/* UNity Callback received on InAppNotificationClicked");
}
To receive callbacks, you must now register this method with WebEngage Bridge as shown below.
This can be done in start method of your class
C#
WebEngage.setInAppClickedCallBack(handleInAppNotificationClicked);
In-App Notification Dismissed
This callback gets triggered when the user dismisses the notification.
Create a method in which you wish to receive callback as mentioned below
C#
[AOT.MonoPInvokeCallback(typeof(callback))]
public static void handleInAppNotificationDismssed(string json)
{
 Debug.Log("/*/*/*/* UNity Callback received on InAppNotificationDismssed");
}
To receive callbacks, you must now register this method with WebEngage Bridge as shown below.
This can be done in start method of your class
C#
WebEngage.setInAppDismissedCallBack(handleInAppNotificationDismssed);
Updated
7 months ago
In-app Messaging
Ionic Capacitor
Copy Page
