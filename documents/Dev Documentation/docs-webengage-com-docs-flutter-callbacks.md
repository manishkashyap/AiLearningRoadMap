# Callbacks

- URL: https://docs.webengage.com/docs/flutter-callbacks
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Flutter
Callbacks
Push Notification Callbacks
Follow these steps for setting up callbacks for your
Flutter app
using the
setUpPushCallbacks
method:
Step 1.
Add below subscribeToPushCallbacks() method inside the class which extends state of
main.dart
and call it from
initState()
Dart
void subscribeToPushCallbacks() {
 //Push click stream listener
 _webEngagePlugin.pushStream.listen((event) {
 String deepLink = event.deepLink;
 Map<String, dynamic> messagePayload = event.payload;
 });

 //Push action click listener
 _webEngagePlugin.pushActionStream.listen((event) {
 print("pushActionStream:" + event.toString());
 String deepLink = event.deepLink;
 Map<String, dynamic> messagePayload = event.payload;
 //Implement the code here to use deeplink
 });
 }
Step 2.
Add the below code snippet inside the class which extends state of
main.dart
for disposing of the push streams.
Dart
//Close the streams in dispose()
 @override
 void dispose() {
 _webEngagePlugin.pushSink.close();
 _webEngagePlugin.pushActionSink.close();
 super.dispose();
 }
Let's quickly walk you through the function of each method:
Callback Method
What It Means
pushStream
Push Notification Clicked:
The callback is invoked when a user clicks on the push notification.
pushActionStream
Push Notification CTA Clicked:
The callback is invoked when a user clicks on the call to action of the push notification.
The callback is invoked when a user clicks on the primary call to action of the push notification.
👍
And you're good to go!
For Android
Callbacks will be automatically attached as expected after adding the dart changes.
For iOS
Follow these steps for setting up a
Push Click callback
using the
pushNotificationDelegate
method. This callback is invoked when the user clicks the primary call to action of the push notification.
Step 1.
Add the below code snippet in the
AppDelegate
file for importing and defining
WebEngagePlugin
variable
AppDelegate.h
AppDelegate.swift
#import <WebEngagePlugin.h>
//...

@property (nonatomic, strong) WebEngagePlugin *bridge;
import WebEngage
//...

var bridge:WebEngagePlugin? = nil
Step 2.
Initialize bridge variable in
didFinishLaunchingWithOptions
and assign value to push notification delegate.
AppDelegate.m
AppDelegate.swift
self.bridge = [WebEngagePlugin new];
 //For setting push click callback set pushNotificationDelegate after webengage SDK is initialised

//Assign bridge variable to push delegates
[WebEngage sharedInstance].pushNotificationDelegate = self.bridge;

//Init WebEngage
[[WebEngage sharedInstance] application:application didFinishLaunchingWithOptions:launchOptions];
bridge = WebEngagePlugin()

// Push notification delegates
WebEngage.sharedInstance().pushNotificationDelegate = self.bridge
//Initialize SDK
WebEngage.sharedInstance().application(application, didFinishLaunchingWithOptions: launchOptions)
👍
And you're good to go!
In-app Notification Callbacks
In-app message callbacks can help you prevent conflicts with views in your app. These callbacks can be implemented for both, your Android and iOS apps. Here's how you can configure them:
Step 1.
Add the below code snippet in the
AppDelegate
file for importing and defining
WebEngagePlugin
variable
AppDelegate.h
AppDelegate.swift
#import <WebEngagePlugin.h>
//...

@property (nonatomic, strong) WebEngagePlugin *bridge;
import WebEngage
//...

var bridge:WebEngagePlugin? = nil
Step 2.
Initialize bridge variable in
didFinishLaunchingWithOptions
and assign value to push notification delegate.
AppDelegate.m
AppDelegate.swift
self.bridge = [WebEngagePlugin new];
 //For setting in-app click callback set notificationDelegate while initialising WebEngage SDK
 
[[WebEngage sharedInstance] application:application didFinishLaunchingWithOptions:launchOptions notificationDelegate:self.bridge];
//Initialize SDK with in-app notification delegates

WebEngage.sharedInstance().application(application, didFinishLaunchingWithOptions: launchOptions, notificationDelegate: self.bridge)
Step 3: Add the below methods in
main.dart
Objective-C
void _onInAppPrepared(Map<String, dynamic>? message) {
 print("This is a inapp Prepated callback from native to flutter. Payload " +
 message.toString());
 }
 void _onInAppClick(Map<String, dynamic>? message,String? s) {
 print("This is a inapp click callback from native to flutter. Payload " +
 message.toString());

 }

 void _onInAppShown(Map<String, dynamic>? message) {
 print("This is a callback on inapp shown from native to flutter. Payload " +
 message.toString());
 }

 void _onInAppDismiss(Map<String, dynamic>? message) {
 print("This is a callback on inapp dismiss from native to flutter. Payload " +
 message.toString());
 }
Let's quickly walk you through the function of each method:
Callback Method
What It Means
onInAppPrepared
In-App Notification Prepared:
This callback gets triggered before the in-app message is shown to your users.
onInAppShown
In-App Message Shown:
This callback is invoked after the message is displayed to an active user in your app.
onInAppClick
In-app Message Clicked:
This callback gets triggered when the user clicks the primary call to action button on the notification.
onInAppDismiss
In-App Message Dismissed:
This callback is invoked when the user dismisses the message.
Step 4: Add the below code inside
initmethod()
in
main.dart
Text
_webEngagePlugin.setUpInAppCallbacks(
 _onInAppClick, _onInAppShown, _onInAppDismiss, _onInAppPrepared);
AnonymousId Change Callbacks
This callback is invoked when the Anonymous ID of the user is changed and when the SDK gets initialsed.
Anonymous ID changes on logout and installations/re-installations.
For Android
Callbacks will be automatically attached as expected after adding the changes
here
.
For iOS
Add the below code snippet in the
AppDelegate
file for registering the callback if not already added.
AppDelegate.m
AppDelegate.swift
self.bridge = [WebEngagePlugin new];
 //For setting push click callback set pushNotificationDelegate after webengage SDK is initialised

//Assign bridge variable to push delegates
[WebEngage sharedInstance].pushNotificationDelegate = self.bridge;

//Init WebEngage
[[WebEngage sharedInstance] application:application didFinishLaunchingWithOptions:launchOptions];
bridge = WebEngagePlugin()

// Push notification delegates
WebEngage.sharedInstance().pushNotificationDelegate = self.bridge

//Initialise SDK
WebEngage.sharedInstance().application(application, didFinishLaunchingWithOptions: launchOptions)
❗️
Warning
Assign pushNotificationDelegate before initialising the SDK as shown in above code snippet.
Dart changes
Add below code in your main.dart file.
Text
_webEngagePlugin.anonymousActionStream.listen((event) {
 var anonymousdId = event!['anonymousUserID'];
 });
👍
And you're good to go!
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
5 months ago
In-app Messaging
App In-line Content
Copy Page
