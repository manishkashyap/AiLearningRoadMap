# Callbacks

- URL: https://docs.webengage.com/docs/xamarin-ios-callbacks
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.iOS
Callbacks
Callbacks are useful for understanding the lifecycle stages of WebEngage events. All WebEngage callbacks are called on the main thread.
Push Message Callbacks
Import
WebEngageXamariniOS
class in your
AppDelegate
file and implement
IWEGAppDelegate
interface.
C#
...
using WebEngageXamariniOS;

namespace YourNamespace
{
 [Register("AppDelegate")]
 public class AppDelegate : UIApplicationDelegate, IWEGAppDelegate
 {
 ...
 public override bool FinishedLaunching(UIApplication application, NSDictionary launchOptions)
 {
 ...
 WebEngage.SharedInstance().Application(application, launchOptions, true);
 return true;
 }

 // Push message callbacks go here
 }
}
Push Notification Clicked
This callback is invoked when the user clicks the primary call to action of the push notification.
C#
[Export("WEGHandleDeeplink:userData:")]
public void WEGHandleDeeplink(string deeplink, NSDictionary data)
{
 ...
}
🚧
Note that WebEngage Xamarin.iOS SDK does not require APIs to pass the device registration token (similar to
WebEngage.get().setRegistrationID(registrationId)
in Android) or APNs message (similar to
WebEngage.get().receive(bundle)
in Android). The Xamarin.iOS SDK handles those automatically by intercepting standard callbacks for the purpose.
In-app message callbacks
In order to use In-app notification callbacks, follow the below steps.
Step 1:
Create WebEngage in-app notification callback delegate class which implements the
WEGInAppNotificationProtocol
as shown below.
C#
using System;
using Foundation;
using WebEngageXamariniOS;

namespace YourNamespace
{
 public class InAppNotificationDelegate : WEGInAppNotificationProtocol
 {
 public override NSMutableDictionary NotificationPrepared(NSMutableDictionary inAppNotificationData, bool stopRendering)
 {
 ...
 return inAppNotificationData;
 }

 public override void NotificationShown(NSMutableDictionary inAppNotificationData)
 {
 ...
 }

 public override void Notification(NSMutableDictionary inAppNotificationData, string actionId)
 {
 ...
 }

 public override void NotificationDismissed(NSMutableDictionary inAppNotificationData)
 {
 ...
 }
 }
}
Step 2:
Register the in-app notification callback delegate in your
AppDelegate
while initializing WebEngage SDK as shown below.
C#
...
using WebEngageXamariniOS;

namespace YourNamespace
{
 ...
 [Register("AppDelegate")]
 public class AppDelegate : UIApplicationDelegate
 {
 ...

 private static InAppNotificationDelegate inAppNotificationDelegate;

 public override bool FinishedLaunching(UIApplication application, NSDictionary launchOptions)
 {
 ...

 inAppNotificationDelegate = new InAppNotificationDelegate();

 WebEngage.SharedInstance().Application(application, launchOptions, inAppNotificationDelegate, true);

 return true;
 }
 ...
 }
 ...
}
In-App Notification Prepared
This callback gets triggered before the notification is shown to your users. It allows you to customize the UI, colors, CTAs (buttons) and content of the In-app message received from WebEngage before displaying it.
Assigning the value of
stopRendering
to
true
will not render the notification for your users.
C#
public override NSMutableDictionary NotificationPrepared(NSMutableDictionary inAppNotificationData, bool stopRendering)
{
 ...
 return inAppNotificationData;
}
In-App Notification Shown
This callback gets triggered after the notification is shown.
C#
public override void NotificationShown(NSMutableDictionary inAppNotificationData)
{
 ...
}
In-App Notification Clicked
This callback gets triggered when the user clicks the call to action button on the notification. The ID of the button clicked is passed as the second parameter. You can look up the button IDs in the
inAppNotificationData
dictionary.
C#
public override void Notification(NSMutableDictionary inAppNotificationData, string actionId)
{
 ...
}
In-App Notification Dismissed
This callback gets triggered when the user dismisses the notification.
C#
public override void NotificationDismissed(NSMutableDictionary inAppNotificationData)
{
 ...
}
Notification Callback Data (
NSMutableDictionary* inAppNotificationData
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
State Change Callbacks
State change callbacks are triggered whenever the state of the SDK changes.
Import
WebEngage
class in your AppDelegate.h file and implement
WEGAppDelegate
interface.
C#
#import <WebEngage/WebEngage.h>
@interface AppDelegate : UIResponder <UIApplicationDelegate,WEGAppDelegate>

 
 
 
...
using WebEngageXamariniOS;

namespace YourNamespace
{
 [Register("AppDelegate")]
 public class AppDelegate : UIApplicationDelegate, IWEGAppDelegate
 {
 ...
 public override bool FinishedLaunching(UIApplication application, NSDictionary launchOptions)
 {
 ...
 WebEngage.SharedInstance().Application(application, launchOptions, true);
 return true;
 }

 // State change callbacks go here
 }
}
Anonymous ID Changed
This callback is invoked when the Anonymous ID of the user is changed. It returns the new anonymous ID and reason for which it is changed.
C#
[Export("didReceiveAnonymousID:forReason:")]
public void DidReceiveAnonymousID(string anonymousID, WEGReason reason)
{
 ...
}
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
In-app Messaging
Advanced
Copy Page
