# Callbacks

- URL: https://docs.webengage.com/docs/react-native-callbacks
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
React Native
Callbacks
Callbacks are useful for understanding the lifecycle stages of WebEngage messages. All WebEngage callbacks are called on the main thread.
🚧
Please Note
Before proceeding, please ensure that the
react-native-webengage
version is 1.2.2 or above.
To update the package to the latest version run the following command:
npm i react-native-webengage
Callback Configuration
iOS
Integrate the WebEngage bridge into your native code to facilitate seamless interactions between native and React Native. The following configuration is essential for handling push notifications and in-app callbacks.
Step 1
: Add the below code snippet in
ios/YourApp/AppDelegate.h
Objective-C
#import <WEGWebEngageBridge.h> // Add This
...
@interface AppDelegate : UIResponder <UIApplicationDelegate>
// Your code
@property (nonatomic, strong) WEGWebEngageBridge *weBridge; // Add This
@end
Step 2
: Modify WebEngage SDK initialisation by changing
ios/YourApp/AppDelegate.m
, as per the following code snippet.
For React-Native Version <=0.70
Objective-C
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
 // Your Code
 
 // Initializes WebEngage Bridge
 self.weBridge = [WEGWebEngageBridge new];
 // Initialize RCTBridge with a delegate and launch options
 RCTBridge *bridge = [[RCTBridge alloc] initWithDelegate:self.weBridge launchOptions:launchOptions];
 // Initializes Push with WebEngage Bridge
 [WebEngage sharedInstance].pushNotificationDelegate = self.weBridge;
 // Initializes InApp with WebEngage Bridge
 [[WebEngage sharedInstance] application:application didFinishLaunchingWithOptions:launchOptions notificationDelegate:self.weBridge];
 return YES;
}
For React-Native Version >= 0.71
Objective-C
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
 // Your Code
 
 // Initializes WebEngage Bridge
 self.weBridge = [WEGWebEngageBridge new];
 // Initializes Push with WebEngage Bridge
 [WebEngage sharedInstance].pushNotificationDelegate = self.weBridge;
 // Initializes InApp with WebEngage Bridge
 [[WebEngage sharedInstance] application:application didFinishLaunchingWithOptions:launchOptions notificationDelegate:self.weBridge]; 
 BOOL success = [super application:application didFinishLaunchingWithOptions:launchOptions];
 return success;
}
Handling Multiple Push Service Providers
If you have integrated multiple push service providers in your iOS app, you need to perform an additional step to
disable swizzling
for WebEngage and proceed with manual integration.
Android
👍
No additional steps are required for using callbacks in your Android app
React Native Callbacks
Push Notification Callbacks
onClick
onClick
allows you to register a callback function that is executed after an push notification is clicked by the user.
The callback handler receives one parameter:
pushNotificationData
: The data Object for the received push notification
JavaScript
useEffect(() => {
 webengage.push.onClick(function(pushNotificationData) {
 console.log("App: push-notification clicked with deeplink: " + pushNotificationData["deeplink"]);
 //Write your own logic to handle deeplink navigation across your application using the pushNotificationData
 });
}, []);
In-app Message Callbacks
onPrepare
onPrepare
allows you to register a callback function that is executed before the In-app message is shown to the user.
The callback handler receives one parameter:
notificationData
: The data Object for the received in-app notification
JavaScript
useEffect(() => {
 webengage.notification.onPrepare(function(notificationData) {
 ...
 });
}, []);
onShown
onShown
allows you to register a callback function that is executed after an in-app notification is shown to the user.
The callback handler receives one parameter:
notificationData
: The data Object for the shown in-app notification
JavaScript
useEffect(() => {
 webengage.notification.onShown(function(notificationData) {
 ...
 });
}, []);
onDismiss
onDismiss
allows you to register a callback function that is executed after an in-app notification is closed by the user.
The callback handler receives one parameter:
notificationData
: The data Object for the shown in-app notification
JavaScript
useEffect(() => {
 webengage.notification.onDismiss(function(notificationData) {
 ...
 });
}, []);
onClick
onClick
allows you to register a callback function that is executed after an in-app notification is clicked by the user.
The callback handler receives two parameters:
notificationData
: The data Object for the shown in-app notification
clickId
: The String identifier for the action button
JavaScript
useEffect(() => {
 webengage.notification.onClick(function(notificationData, clickId) {
 console.log("App: in-app notification clicked: click-id: " + clickId + ", deep-link: " + notificationData["deepLink"]);
 ...
 });
}, []);
Anonymous ID Changed
📘
Supported from React Native SDK
v1.6.0
onwards
The anonymousId is a unique identifier assigned to a user, used to track user activity anonymously.
This callback is triggered in the following scenarios:
When the Anonymous ID (LUID) changes
— Typically after a user logout or a fresh installation/re-installation of the app.
When the WebEngage SDK is initialised
— Even if the Anonymous ID remains unchanged.
JavaScript
webengage.user.onAnonymousIdChanged(function (anonymousId) {
 console.log('Anonymous ID is ' + anonymousId);
});
📘
Ensure that you implement WebEngage callbacks as soon as the application is mounted, ideally within the
App.tsx
file.
Sample Application
For further instructions, refer to our
Sample Application
available on Github. Additionally, you can find the following crucial files within the application:
App.tsx
index.js
Sample In-App Payload
Data received from in-app callbacks adheres to the below format.
JSON
{
 "description": null,
 "id": "173050749",
 "actions": [
 {
 "actionEId": "~3284c402",
 "actionText": "Hello",
 "actionLink": "http://www.google.com",
 "actionCategory": "CTA",
 "actionTarget": "_top",
 "isPrime": true,
 "type": "EXTERNAL_URL"
 }
 ],
 "layoutId": "~483819e",
 "showTitle": true,
 "canMinimize": true,
 "layoutAttributes": {
 "exitAnimation": "FADE_OUT",
 "fullscreen": true,
 "wvHeight": 100,
 "image_url": "https://s3-ap-southeast-1.amazonaws.com/wk-static-files/~2024c585/6035287f-62e3-4c6b-8d56-e893941da6bf.png",
 "posX": 0,
 "animDuration": 1000,
 "type": "BLOCKING",
 "posY": 0,
 "wvWidth": 100,
 "entryAnimation": "FADE_IN"
 },
 "title": null,
 "config": {
 "closeIconColor": "#FFFFFF",
 "hideLogo": false,
 "c2aTextColor": "#FFFFFF",
 "c2aTextFont": "Sans-Serif",
 "c2aBackgroundColor": "#4A90E2"
 },
 "canClose": true,
 "notificationEncId": "13cjj4m",
 "direction": "ltr",
 "isActive": true
}
Sample Push Payload
Data received from push callbacks adheres to the below format.
JSON
{
 "userData": {
 "license_code": "YOUR_LICENSE",
 "rm": "<!DOCTYPE html><html><head></head><body><span style=\"text-decoration: line-through;\">Desc</span></body></html>",
 "packageName": "com.webengage.reactSample",
 "experimentId": "T_3hc61oq||47j478h5h3f06a_30f41227-25f6-4dc1-b3fc-f40b47fa6e48#1:1714745756912",
 "messageAction": "NOTIFICATION",
 "bckColor": "",
 "cta": null,
 "expandableDetails": {
 "style": "BIG_PICTURE",
 "ratingScale": 5,
 "message": "Desc",
 "image": "https://afiles.webengage.com/cdn-cgi/image/q=50/~134105693/08c4e1d9-07ad-4bf0-92e4-dcb40ae47af9.png"
 },
 "timeToLive": 0,
 "identifier": "~5bl1mio",
 "priority": null,
 "title": "Title!",
 "childExperimentMetaData": null,
 "message": "Desc",
 "custom": [
 {
 "key": "provider",
 "value": "FCM"
 }
 ],
 "customEventData": null,
 "rt": "<!DOCTYPE html><html><head></head><body><strong>Title!</strong></body></html>",
 "image": null
 },
 "deeplink": null,
 "provider": "FCM"
}
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries or feedback. We're always just an email away!
Updated
7 months ago
In-app Messaging
Advanced
Copy Page
