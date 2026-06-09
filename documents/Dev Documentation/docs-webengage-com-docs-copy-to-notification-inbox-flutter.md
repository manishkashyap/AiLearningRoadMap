# Copy Push to Notification Inbox - Flutter

- URL: https://docs.webengage.com/docs/copy-to-notification-inbox-flutter
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Flutter
Push Messaging
Copy Push to Notification Inbox - Flutter
Flutter WebEngage Inbox is a powerful and user-friendly library that enhances your Flutter app's notification management capabilities by providing an inbox for organizing and accessing missed notifications. This library enables you to effortlessly deliver, store, and retrieve important notifications within your app.
Prerequisites
To get started with integrating Notification Inbox make sure:
Make sure that SDK authentication is enabled. (You can enable it by following the steps in this
document
)
Once the Intialization steps mentioned in this document are completed, you can raise a request to us on
[email protected]
to enable this feature.
Installation
Step 1
: Integrate the WebEngage SDK by following the steps mentioned in
this
doc.
Step 2
: Add dependency in
pubspec.yaml
Swift
we_notificationinbox_flutter: ^1.0.0
Initialize the Notification Inbox
Step 1:
Initialize the WebEngage Notification Inbox SDK by calling
WENotificationInbox().init()
;. This needs to be done only once, and right after the WebEngage SDK Plugin initialization.
In
main.dart
file after initializing the WebEngage plugin, call the initialization of the NotificationInbox plugin in
initState
method.
Swift
import 'package:we_notificationinbox_flutter/we_notificationinbox_flutter.dart';

 WENotificationInbox().init();
Fetch Notification Count
The
getNotificationCount()
function allows you to retrieve the count of unread notifications, making it easier to keep track of pending alerts.
Functional Signature:
Swift
getNotificationCount()
Returns:
This method returns a numeric value representing the total count of notifications in the WebEngage Inbox.
Usage:
Swift
final _weNotificationinboxFlutterPlugin = WENotificationinboxFlutter();
...
Future<void> getNotificationCount() async {
 String notificationCount = "0";
 WENotificationResponse weNotificationResponse = await _weNotificationInboxFlutterPlugin.getNotificationCount();
 if(weNotificationResponse.isSuccess) {
 if (kDebugMode) {
 notificationCount = weNotificationResponse.response;
 print("WebEngage-Sample-App: notificationCount in the sample App \n ${weNotificationResponse.response}");
 }
 } else {
 if (kDebugMode) {
 print("WebEngage-Sample-App: Exception occurred while accessing Notification Count \n ${weNotificationResponse.errorMessage} ");
 }
 }
 }
Reset Notification Count
The
resetNotificationCount()
function is designed to handle the event when the user clicks on the notification icon within the application. Its key functionality is to reset the notification count to 0, signifying that the user has acknowledged and viewed the notifications and that there are no pending unread alerts.
Function Signature:
Swift
resetNotificationCount();
Usage:
Swift
// Function to handle the notification icon click event
void onNotificationIconClick() {
 // Code to handle the notification icon click event

 // Resets the notification count to 0
 _weNotificationinboxFlutterPlugin.resetNotificationCount();
}
Fetch Notification List
The
getNotificationList
function allows you to retrieve the list of notifications from the WebEngage Inbox. It offers pagination support by accepting an offset object as a parameter. By providing different offset values, you can fetch the initial list or subsequent notification items, making it easier to manage and display notifications in your app.
Function Signature:
Swift
getNotificationList(offsetJSON: offset)
Parameters:
Parameter
Description
Mandatory
Offset
An optional parameter that can be a Notification object containing offset information for pagination.
Optional
Returns:
This method returns an object containing the
notificationData
. The
notificationData
object contains two properties:
Property
Description
hasNext
Indicates whether there are more notifications available beyond the current list.
notificationList
An array containing the list of retrieved notifications.
Usage:
Fetch the Initial List of Notifications:
Swift
Future<void> fetchNotificationList() async {
 Map<String, dynamic> fetchedNotifications;
 WENotificationResponse weNotificationResponse =
 await _weNotificationInboxFlutterPlugin.getNotificationList();
 if (weNotificationResponse.isSuccess) {
 Map<String, dynamic> fetchedNotificationList =
 weNotificationResponse.response;
 // handle success
 } else {
 var errorMessage = weNotificationResponse.errorMessage;
 // handle error
 }
 }
📘
Please Note
To optimize data retrieval,
getNotificationList
method fetches a batch of 10 items in the
notificationList
. Pagination can be used to access further batches beyond the initial 10, facilitating efficient navigation and data retrieval for managing notification lists.
Fetch the Next Set of Notifications:
Swift
Future<void> fetchNext() async {
 Map<String, dynamic> fetchedNotifications;
 var offset = _notificationList[_notificationList.length - 1];
 WENotificationResponse weNotificationResponse =
 await _weNotificationInboxFlutterPlugin.getNotificationList(offsetJSON: offset);
 if (weNotificationResponse.isSuccess) {
 Map<String, dynamic> fetchedNotificationList =
 weNotificationResponse.response;
 // handle success
 } else {
 var errorMessage = weNotificationResponse.errorMessage;
 // handle error
 }
 }
👍
Keep in Mind
hasNext
property indicates whether there are furthermore items in the pagination list beyond the current page or not, facilitating efficient navigation and data retrieval.
Single Notification Actions
Mark Read
The
markRead()
method allows you to mark a specific notification as read within the "Flutter WebEngage Inbox" library. This function is particularly useful when you want to indicate that a user has seen and acknowledged a particular notification.
Parameters:
notificationItem
: An object representing the notification item to mark as read.
Usage:
Swift
_weNotificationinboxFlutterPlugin.markRead(notificationItem);
Mark Unread
The
markUnread()
method enables you to mark a specific notification as unread in the "Flutter WebEngage Inbox" library. By using this function, you can conveniently notify users about important or unread alerts.
Parameters:
notificationItem
: An object representing the notification item to mark as unread.
Usage:
Swift
_weNotificationinboxFlutterPlugin.markUnread(notificationItem);
Mark Delete
The
markDelete()
method is designed to mark a specific notification for deletion within the "Flutter WebEngage Inbox" library. This function allows you to handle the removal of notifications that are no longer relevant or required.
Parameters:
notificationItem
: An object representing the notification item to mark for deletion.
Usage:
Swift
_weNotificationinboxFlutterPlugin.markDelete(notificationItem);
Batch Notification Actions
Read All
The
readAll()
method enables you to mark multiple notifications as read within the "Flutter WebEngage Inbox" library. This function is particularly useful when you want to acknowledge and mark a batch of notifications as seen by the user.
Parameters
notificationList
: An array of notification items to mark as read.
Usage
Swift
_weNotificationinboxFlutterPlugin.readAll(notificationList);
UnRead All
The
unReadAll()
method allows you to mark multiple notifications as unread in the "Flutter WebEngage Inbox" library. This function is useful when you want to indicate a batch of notifications as unread for users to revisit and take action.
Parameters
notificationList
: An array of notification items to mark as unread.
Usage:
Swift
_weNotificationinboxFlutterPlugin.unReadAll(notificationList);
Delete All
The
deleteAll()
method is designed to delete multiple notifications simultaneously within the "Flutter WebEngage Inbox" library. This function allows you to efficiently handle the removal of a batch of notifications that are no longer required or relevant.
Parameters:
notificationList
: An array of notification items to delete.
Usage:
Swift
_weNotificationinboxFlutterPlugin.deleteAll(notificationList);
📘
Batch Notification Actions(readAll/unReadAll/deleteAll) are designed to operate exclusively on the items provided as arguments. When using these batch actions, only the specific items within the
notificationList
passed as arguments will be affected, while the remaining notifications will remain unchanged.
Tracking Events
Track Click
The
trackClick()
method allows you to track a click event on a specific notification. Trigger this event when a user interacts with the notification by clicking on it, indicating their interest in the content or call-to-action associated with the notification.
Parameters:
notificationItem
: An object representing the notification item clicked
Usage:
Swift
_weNotificationinboxFlutterPlugin.trackClick(notificationItem);
Track View
The
trackView()
method enables you to track a view event for a specific notification. Trigger this event when a user views the notification without necessarily interacting with it, providing insights into the reach and visibility of notifications.
Parameters
notificationItem
: An object representing the notification item viewed.
Usage
Swift
_weNotificationinboxFlutterPlugin.trackView(notificationItem);
🚧
Please Note
Tracking Views and tracking clicks are mandatory steps. If not added then view impression and click data for these campaigns will not be recorded.
Updated
7 months ago
Push Messaging
In-app Messaging
Copy Page
