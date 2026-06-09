# Push Messaging

- URL: https://docs.webengage.com/docs/xamarin-ios-push-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.iOS
Push Messaging
Push Notifications are messages that pop up on mobile devices. App publishers can send them at any time; even if the recipients aren’t currently engaging with the app or using their devices.
🚧
Before continuing, please ensure that you have
added the WebEngage SDK to your app
.
Configure Push Messaging
Here's how you can enable Push Messaging for your Xamarin.iOS app:
Step 1:
Follow the steps mentioned in
Push messaging integration document for iOS
.
Step 2:
Log in to your WebEngage dashboard and navigate to
Integrations
>
Channels
. In
Push
tab, under the
iOS
section, make sure you have uploaded either your push certificate or auth key.
Step 3:
In your Xamarin.iOS app's
Entitlements.plist
, check
Enable Push Notifications
.
Step 4:
Add
remote-notifications
as type string under
App Background Modes
in your app's
info.plist
.
Step 5:
Set
autoregister
to
true
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
 public override bool FinishedLaunching(UIApplication application, NSDictionary launchOptions)
 {
 ...
 WebEngage.SharedInstance().Application(application, launchOptions, true);
 return true;
 }
 ...
 }
 ...
}
Enable Rich Push Notifications
Follow the below steps to use rich push notifications in your Xamarin.iOS app.
1. For Banner Push Notifications
Step 1:
Add a new project named
NotificationService
with
Notification Service Extension
as target in your main app.
Step 2:
Download
WebEngage Banner Push Notification Extension SDK
.
Step 3:
Add
WebEngageBannerPushXamariniOS.dll
to
References
in your
NotificationService
project.
Step 4:
Replace
NotificationService.cs
with the below code.
C#
using Foundation;
using WebEngageBannerPushXamariniOS;

namespace NotificationService
{
 [Register("NotificationService")]
 public class NotificationService : WEXPushNotificationService
 {

 }
}
2. For Rating and Carousel Push Notifications
Step 1:
Add a new project named
NotificationViewController
with
Notification Content Extension
as target in your main app.
Step 2:
Download
WebEngage Notification App Extension SDK
.
Step 3:
Add
WebEngageAppExXamariniOS.dll
to
References
in your
NotificationViewController
project.
Step 4:
Open the
Info.plist
file for
NotificationViewController
. Expand
NSExetnsion
>
NSExtensionAttributes
. Look for
UNNotificationExtensionCategory
under
NSExtensionAttributes
. If it is not present, add it and set the type as
Array
. In its items, add the following values:
WEG_CAROUSEL_V1
for Carousel Push Notifications
WEG_RATING_V1
for Rating Push Notifications
Step 5:
Replace
NotificationViewController.cs
with the below code.
C#
using System;
using Foundation;
using UserNotifications;
using WebEngageAppExXamariniOS;

namespace NotificationViewController
{
 public partial class NotificationViewController : WEXRichPushNotificationViewController
 {
 protected NotificationViewController(IntPtr handle) : base(handle)
 {
 
 }

 public override void ViewDidLoad()
 {
 base.ViewDidLoad();
 }

 [Export("didReceiveNotification:")]
 public override void DidReceiveNotification(UNNotification notification)
 {
 base.DidReceiveNotification(notification);
 }
 }
}
3. Set App Groups of All 3 Projects
Set App Groups as
group.[app-bundle-id].WEGNotificationGroup
in
Entitlements.plist
of all three projects (your Xamarin.iOS app,
NotificationService
and
NotificationViewController
).
And you're good to go!
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away.
Updated
7 months ago
Tracking Events
In-app Messaging
Copy Page
