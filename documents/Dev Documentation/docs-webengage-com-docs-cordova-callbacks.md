# Callbacks

- URL: https://docs.webengage.com/docs/cordova-callbacks
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Cordova
Callbacks
Callbacks are useful for understanding the lifecycle stages of WebEngage messages. All WebEngage callbacks are called on the main thread. All callbacks must be registered in
onDeviceReady
before the
webengage.engage()
call.
Push message callbacks
Push Notification Clicked
webengage.push.onClick
allows you to register a callback function which is executed when the user taps on a received push notification. This callback should be registered in
onDeviceReady
before the
webengage.engage()
call.
The callback handler receives two parameters:
deeplink
: The deep link URL
String
associated with the push message
customData
: Custom data
Object
passed from the dashboard
JavaScript
onDeviceReady: function() {

 webengage.push.onClick(function(deeplink, customData) {
 console.log("Push clicked");
 });

 ...
 ...

 webengage.engage();
}
📘
If this callback is registered in iOS, the deep link will not be opened automatically. Your app is supposed to handle it. For Android, the deep link is fired irrespective.
In-app message callbacks
In-App Notification Prepared
This callback gets triggered before the in-app message is shown to your users. It allows you to customize the UI, colors, CTAs (buttons) and content of the In-app message received from WebEngage before displaying it to your users.
The callback handler receives one parameter:
inAppData
: The data
Object
for the prepared in-app notification
JavaScript
onDeviceReady: function() {

 webengage.notification.onPrepared(function(inAppData) {
 console.log("InApp Prepared Callback Received, Data: " + JSON.stringify(inAppData));
 });

 ...
 ...

 webengage.engage();
}
In-App Notification Shown
webengage.notification.onShown
allows you to register a callback function which is executed after an in-app notification is shown to the user.
The callback handler receives one parameter:
inAppData
: The data
Object
for the shown in-app notification
JavaScript
onDeviceReady: function() {

 webengage.notification.onShown(function(inAppData) {
 console.log("In-app shown");
 });

 ...
 ...

 webengage.engage();
}
In-App Notification Dismissed
webengage.notification.onDismiss
allows you to register a callback function which is executed after an in-app notification is closed by the user.
The callback handler receives one parameter:
inAppData
: The data
Object
for the shown in-app notification
JavaScript
onDeviceReady: function() {

 webengage.notification.onDismiss(function(inAppData) {
 console.log("In-app dismissed");
 });

 ...
 ...

 webengage.engage();
}
In-App Notification Clicked
webengage.notification.onClick
allows you to register a callback function which is executed after an in-app notification is clicked by the user.
The callback handler receives two parameters:
inAppData
: The data
Object
for the shown in-app notification
actionId
: The
String
identifier for the action button
JavaScript
onDeviceReady: function() {

 webengage.notification.onClick(function(inAppData, actionId) {
 console.log("In-app shown");
 });

 ...
 ...

 webengage.engage();
}
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
Updated
7 months ago
In-app Messaging
Advanced
Copy Page
