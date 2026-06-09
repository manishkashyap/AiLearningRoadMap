# Copy Push to Notification Inbox - Android

- URL: https://docs.webengage.com/docs/copy-to-notification-inbox-android
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
Push Messaging
Copy Push to Notification Inbox - Android
Notification Inbox is a powerful feature through which your users can have a unified and streamlined notification experience, where they can easily access and manage their notifications in one place.
Through WebEngage, you can now
copy push notifications to your app's Notification Inbox
. In this approach the app will have the control on the notification message layout, while through WebEngage integration the message data will be passed on to your app, thereby providing your users personalized experiences.
📘
Notification Inbox as a complete channel to be launched soon!
Prerequisites
To get started with integrating Notification Inbox make sure:
WebEngage Android SDK version 4.4.1 or above is integrated
SDK authentication is enabled. (You can enable it by following the steps in
this document
)
Once the initialization steps mentioned in this document are completed, you can raise a request to us on
[email protected]
to enable this feature.
Initialize the SDK
To use the Notification Inbox SDK, you need to initialize a WebEngage object with your API key and endpoint.
Gradle
implementation 'com.webengage:we-notification-inbox:1.0.0'
Methods to call Notification Messages
Retrieve unread notification count
This method provides the count of
unread
notifications. The value will be either a single digit number or the number with a "+" sign.
For example: the value can be 7 or 10+
Java
Kotlin
WENotificationInbox.get(context).getUserNotificationCount(mContext, 
 new WEInboxCallback<String>() {
 @Override
 public void onSuccess(String countStr) {
 }

 @Override
 public void onError(int errorCode, @NonNull Map<String, ?> error) {
 }
 });
WENotificationInbox.get(context).getUserNotificationCount(context, object : WEInboxCallback<String> {
 override fun onSuccess(result: String) {

 }

 override fun onError(errorCode: Int, error: Map<String, Any?>) {

 }
 })
Get notification messages:
Fetch the notification inbox list in the
Activity
/
Fragment
where you want to show the Notification Inbox data. This will return the
first set
of notifications list.
Java
Kotlin
WENotificationInbox.get(context).getNotificationList(context, 
 new WEInboxCallback<WEInboxData>() {
 @Override
 public void onSuccess(WEInboxData weInboxData) {
 //Handle the data
 }
 @Override
 public void onError(int errorCode, @NonNull Map<String, ?> error) {
 //Handle error state
 }
 });
WENotificationInbox.get(context).getNotificationList(context,
 object: WEInboxCallback<WEInboxData> {
 override fun onSuccess(result: WEInboxData) {
 //Handle the data
 }

 override fun onError(errorCode: Int, error: Map<String, Any?>) {
 //Handle error state
 }
 })
Get notification messages with offset:
The
weInboxData
received on the success of above API call has a boolean value
hasNext
, which will be
true
if there is a possibility of additional data being available for retrieval. To fetch the next batch of the notification list you need to send the last message object
weInboxMessage
of
weInboxData.getMessageList()
.
Java
Kotlin
WENotificationInbox.get(context).getNotificationList(context, weInboxMessage, 
 new WEInboxCallback<WEInboxData>() {
 @Override
 public void onError(int errorCode, @NonNull Map<String, ?> error) {
 }
 @Override
 public void onSuccess(WEInboxData weInboxData) {
 }
 });
WENotificationInbox.get(context).getNotificationList(context, weInboxMessage , object : WEInboxCallback<WEInboxData>{
 override fun onSuccess(result: WEInboxData) {
 }

 override fun onError(errorCode: Int, error: Map<String, Any?>) {
 }
 })
WEInboxData
This object hold the list of message data and a value that represent if more notifications to be fetched.
Name
Variable type
Definition
hasNext
Boolean
The value will be true if more notification messages may be available for download. Note that this does not guarantee the availability of more messages.
messageList
WEInboxMessage
Collection of WEInboxMessage objects. With additional details of each notifications
WEInboxMessage
The object contains the details of the notification. You can access the following details from this object. WEInboxMessageData holds the details needed to render the push such as title description
Name
Variable type
Definition
experimentId
String
id of the campaign
status
String
status of the message read/unread/delete
channelType
String
type of the channel push/email/sms
scope
String
category
String
category of the notification
message
WEInboxMessageData
This object hold the details needed to render the push such as title, description, summary
WEInboxMessageData
The object contains the message data required to display the details on the screen. This also allows you to access the custom key-value pairs. You must type cast this message to the appropriate data type based on the channel type.
If the channel is Push,
WEInboxMessageData
is converted to
PushNotificationTemplateData
.
Java
Kotlin
List<WEInboxMessage> weInboxMessageList = weInboxData.getMessageList();
WEInboxMessage weInboxMessage = weInboxMessageList.get(i);
PushNotificationTemplateData pushNotificationTemplateData = (PushNotificationTemplateData) weInboxMessage.getMessage();

String title = pushNotificationTemplateData.getTitle();
String description = pushNotificationTemplateData.getDescription();
Map<String, String> customDataMap = pushNotificationTemplateData.getCustomData();
var weInboxMessageList: List<WEInboxMessage> = weInboxData.getMessageList()
var weInboxMessage: WEInboxMessage = weInboxMessageList[i]
var pushNotificationTemplateData: PushNotificationTemplateData =
weInboxMessage.getMessage() as PushNotificationTemplateData

var title: String = pushNotificationTemplateData.getTitle()
var description: String = pushNotificationTemplateData.getDescription()
var customDataMap: Map<String, String> = pushNotificationTemplateData.getCustomData()
Kotlin
Name
Variable type
Definition
title
String
Title of the notification.
description
String
Description of the notification.
callToActionsList
MutableMap<String, Any?>
call to action Button details of the notification.
customData
MutableMap<String, String>
One can access the custom key-value pairs with this.
summary
String
Summary of the notification.
Java
Function Name
Return type
Definition
getTitle()
String
Title of the notification.
getDescription()
String
Description of the notification.
getCallToActionsList
Map<String,Object>
call to action Button details of the notification.
getCustomData()
Map<String, String>
One can access the custom key-value pairs with this.
getSummary()
String
Summary of the notification.
Mark Notification Events
You can record various events for each message received for the user to update the notification inbox list. This can be done through
WEInboxMessage
object. The various types of events that can be recorded for the messages are:
READ
,
UNREAD
,
DELETE
and
BULK
operations.
Mark notification Read
This marks the notification as read for the user, it helps to indicate the user in the future that the notification is already read.
Java / Kotlin
weInboxMessage.markRead();
Mark notifications Read in Bulk
Java/Kotlin
WENotificationInbox.get(mContext).markStatus(weInboxMessageList, WENotificationInbox.STATUS.READ);
Mark a notification as Unread
This marks the notification as unread. User can mark the already Read message as Unread.
Java / Kotlin
weInboxMessage.markUnread();
Mark notifications as Unread in bulk
Java / Kotlin
WENotificationInbox.get(context).markStatus(weInboxMessageList, WENotificationInbox.STATUS.UNREAD)
Mark notification Delete
Marking the status of a message to delete, will delete the message from the notification list from remote.
Java / Kotlin
weInboxMessage.markDelete();
Mark Notification as Delete in Bulk
Java / Kotlin
WENotificationInbox.get(mContext).delete(weInboxMessageList);
Track the user activity with the notifications with the following functions-
Track Views/Impressions
For example, if a user have viewed the message from the notification inbox and to keep a track on the viewed impression, you can call the
trackView()
.
Java / Kotlin
weInboxMessage.trackView();
Track notification message Click
For example, if a user have clicked the message from the notification inbox and to keep a track on the clicked impression, you can call the
trackClick()
.
Java / Kotlin
weInboxMessage.trackClick();
Track the click on the notification icon/button
You can track the user's click on the notification Icon. This should be added to track the click of icon/button which will show the list. This will reset the notification count fetched.
Java / Kotlin
WENotificationInbox.get(mContext).onNotificationIconClick();
Sample Notification Inbox Module
WebEngage has built a sample Notification Inbox module that is a plug-and-play solution. This solution is beneficial for clients who still haven't created a Notification Inbox in their apps. You can learn more about the module and its flexibilities
here
.
Updated
7 months ago
Huawei Push Integration
Notification Channels
Copy Page
