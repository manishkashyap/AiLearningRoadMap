# Callbacks

- URL: https://docs.webengage.com/docs/ios-callbacks
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
Callbacks
Callbacks are useful for understanding the lifecycle stages of WebEngage events. All WebEngage callbacks are called on the main thread.
Push Message Callbacks
Import
WebEngage
class in your AppDelegate.h file and implement
WEGAppDelegate
interface.
Swift
Objective-C
import WebEngage

extension AppDelegate: WEGAppDelegate {
 ...
}
#import <WebEngage/WebEngage.h>
 
@interface AppDelegate : UIResponder < UIApplicationDelegate, WEGAppDelegate >
Push Notification Clicked
This callback is invoked when the user clicks the primary call to action of the push notification.
Swift
Objective-C
func wegHandleDeeplink(_ deeplink: String!, userData data: [AnyHashable : Any]!) {
 ...
}
- (void)WEGHandleDeeplink:(NSString *)deeplink userData:(NSDictionary *)data;
🚧
Please Note
The WebEngage iOS SDK does not require APIs to pass the device registration token (similar to
WebEngage.get().setRegistrationID(registrationId)
in Android) or APNs message (similar to
WebEngage.get().receive(bundle)
in Android). The iOS SDK handles those automatically by intercepting standard callbacks for the purpose.
In case you are using
pod 'WebEngage'
, the callback to push notification clicks -
application:didReceiveRemoteNotification:fetchCompletionHandler
will not be called when a user taps on a remote notification on an iOS 10.0 (or later) device.
This is because WebEngage SDK uses the new
UserNotifications
framework introduced in iOS 10.0 for handling push notifications, which deprecates the method.
If your app needs to use the above method to detect push calls to action, refer to
the Troubleshooting section
.
In-app Message Callbacks
In order to use In-app notification callbacks, your application must define a class which implements the
WEGInAppNotificationProtocol
and set it as the notification callback delegate in the
initialization call to SDK
with the appropriate API for the same.
Swift
Objective-C
extension AppDelegate: WEGInAppNotificationProtocol {

 func notificationPrepared(_ inAppNotificationData: [String : Any]!, shouldStop stopRendering: UnsafeMutablePointer<ObjCBool>!) -> [AnyHashable : Any]!

 func notificationShown(_ inAppNotificationData: [String : Any]!)

 func notification(_ inAppNotificationData: [String : Any]!, clickedWithAction actionId: String!)

 func notificationDismissed(_ inAppNotificationData: [String : Any]!)
}
@protocol WEGInAppNotificationProtocol <NSObject>

- (NSDictionary *)notificationPrepared:(NSDictionary<NSString *,id> *)inAppNotificationData shouldStop:(BOOL *)stopRendering;

- (void)notificationShown:(NSDictionary<NSString *,id> *)inAppNotificationData;

- (void)notification:(NSDictionary<NSString *,id> *)inAppNotificationData clickedWithAction:(NSString *)actionId;

- (void)notificationDismissed:(NSDictionary<NSString *,id> *)inAppNotificationData;

@end
In-App Notification Prepared
This callback gets triggered before the in-app message is shown to your users. It allows you to customize the UI, colors, CTAs (buttons) and content of the In-app message received from WebEngage before displaying it to your users.
Assigning the value of
stopRendering
to
YES
will not render the notification for the users.
Swift
Objective-C
func notificationPrepared(_ inAppNotificationData: [String : Any]!, shouldStop stopRendering: UnsafeMutablePointer<ObjCBool>!) -> [AnyHashable : Any]!
- (NSMutableDictionary *)notificationPrepared:(NSMutableDictionary *)inAppNotificationData shouldStop:(BOOL *)stopRendering;
In-App Notification Shown
This callback gets triggered after the notification is shown.
Swift
Objective-C
func notificationShown(_ inAppNotificationData: [String : Any]!)
- (void)notificationShown:(NSMutableDictionary *)inAppNotificationData;
In-App Notification Clicked
This callback gets triggered when the user clicks the call to action button on the notification. The ID of the button clicked is passed as the second parameter. You can look up the button IDs in the
inAppNotificationData
dictionary.
Swift
Objective-C
func notification(_ inAppNotificationData: [String : Any]!, clickedWithAction actionId: String!)
- (void)notification:(NSMutableDictionary *)inAppNotificationData clickedWithAction:(NSString *)actionId;
In-App Notification Dismissed
This callback gets triggered when the user dismisses the notification.
Swift
Objective-C
func notificationDismissed(_ inAppNotificationData: [String : Any]!)
- (void)notificationDismissed:(NSMutableDictionary *)inAppNotificationData;
Notification Callback Data (NSDictionary* inAppNotificationData)
Data received from in-app callbacks adheres to the below format.
JSON
{
 "canClose": true,
 "layoutAttributes": {
 "posX": 0,
 "posY": 0,
 "TITLE_ALIGN": "CENTER",
 "image_url": "https://s3-ap-southeast-1.amazonaws.com/wk-test-static-files/76a9d10/a6b6e04d-43e9-4c09-b15f-8acffbcfcc1a.jpg",
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
New Session Started
Session started callbacks are triggered whenever any new session gets created
This will get triggered with below parameters about session details
Parameter Name
Data Type
Description
sessionType
WEGSessionType
Type of session will receive in this param
WEGSessionTypeForeground = 1 WEGSessionTypeBackground = 2
newUser
Bool
This will be boolean value to show if session has been created for new user or for the same user
Swift
Objective-C
func sessionStarted(_ sessionType: WEGSessionType, forNewUser newUser: Bool) {
 print("Session Started")
}
- (void)sessionStarted:(WEGSessionType)sessionType forNewUser:(BOOL)newUser{
 NSLog(@"Session Started");
}
State Change Callbacks
State change callbacks are triggered whenever the state of the SDK changes.
Import
WebEngage
class in your AppDelegate.h file and implement
WEGAppDelegate
interface.
Swift
Objective-C
extension AppDelegate: WEGAppDelegate {
 ...
}
#import <WebEngage/WebEngage.h>
 
@interface AppDelegate : UIResponder < UIApplicationDelegate, WEGAppDelegate >
Anonymous ID Changed
This callback is invoked when the Anonymous ID of the user is changed. It returns the new anonymous ID and reason for which it is changed.
Swift
Objective-C
func didReceiveAnonymousID(_ anonymousID: String!, for reason: WEGReason)
- (void)didReceiveAnonymousID:(NSString *)anonymousID forReason:(WEGReason)reason;
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Copy Push to Notification Inbox - iOS
App In-line Content
Copy Page
