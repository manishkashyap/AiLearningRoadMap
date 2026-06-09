# Copy Push to Notification Inbox - iOS

- URL: https://docs.webengage.com/docs/copy-to-notification-inbox-ios
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
Push Messaging
Copy Push to Notification Inbox - iOS
Notification Inbox is a powerful feature through which your users can have a unified and streamlined notification experience, where they can easily access and manage their notifications in one place.
Through WebEngage, you can now
copy push notifications to your app's Notification Inbox
. In this approach the app will have the control on the notification message layout, while through WebEngage integration the message data will be passed on to your app, thereby providing your users personalized experiences.
📘
Notification Inbox as a complete channel to be launched soon!
Prerequisites
To get started with integrating Notification Inbox make sure:
WebEngage iOS SDK v6.3.2 or higher is integrated
SDK authentication is enabled. (You can enable it by following the steps in
this document
)
Once the Intialization steps mentioned in this document are completed, you can raise a request to us on
[email protected]
to enable this feature.
Installation
Step 1:
Integrate WebEngage SDK by following the steps mentioned in this
doc
.
Step 2:
Add WebEngage Notification Inbox SDK to your project.
Depending on your dependency manager, follow the steps below to link the
WebEngageNotificationInbox
module:
Install Using Swift package manager
If you selected
WebEngageNotificationInbox
during the initial SPM setup, you are good to go. If you missed it, go to your
Project Targets > General > Frameworks, Libraries, and Embedded Content
to add it manually.
Install Using Cocoapods
add the WebEngage Notification Inbox SDK in your Podfile under your project's target.
pod 'WENotificationInbox'
Initialize the SDK
To use the Notification Inbox SDK, you need to initialize a WebEngage object with your API key and endpoint.
Swift
Objective C
// Import SDK 
import WENotificationInbox
#import <WENotificationInbox/WENotificationInbox.h>
Methods to call Notification Messages
Get notification messages:
Fetch the notification inbox list in the
ViewController
where you want to show the Notification Inbox data. This will return the first set of notifications list.
Swift
Objective C
WENotificationInbox.shared.getNotificationList { data, error in
 if let response = data{
 // data : WEInboxData
 }else if let weInboxError = error{
 //error: WEInboxError
 }
}
[[WENotificationInbox shared] getNotificationListWithLastInboxData:nil
 completion:^(WEInboxData *data, WEInboxError *error) {
 if (data != nil){
 // data : WEInboxData
 }else if (error != nil){
 //error: WEInboxError
 }
}];
Get notification messages with offset:
The
lastInboxData
received on the success of above API call has a boolean value
hasNextPage
, which will be
true
if more data is available to fetch. To fetch the next batch of the notification list you need to send the last message object
WEInboxMessage
of
WEInboxData.inboxData
Swift
Objective C
WENotificationInbox.shared.getNotificationList(lastInboxData: lastInboxData,
 completion: { data, error in
 if let response = data{
 // data : WEInboxData
 }else if let weInboxError = error{
 //error: WEInboxError
 }
})
[[WENotificationInbox shared] getNotificationListWithLastInboxData:nil
 completion:^(WEInboxData *data, WEInboxError *error) {
 if (data != nil){
 // data : WEInboxData
 }else if (error != nil){
 //error: WEInboxError
 }
}];
Retrieve unread notification count
This method provides the count of
unread
notifications. The value will be either a single digit number or the number with a "+" sign.
For example: the value can be 7 or 10+
Swift
Objective C
WENotificationInbox.shared.getUserNotificationCount { data, error in
 if let count = data{
 print("Notification Count : \(count)")
 }else if let weInboxError = error{
 //error: WEInboxError
 }
}
[[WENotificationInbox shared] getUserNotificationCountWithCompletion:^(id count, WEInboxError *error) {
 NSLog(@"WA: count : %@",count);
}];
WEInboxData
This object hold the list of message data and a value that represent if more notifications to be fetched.
Name
Variable type
Definition
hasNextPage
Bool
the value will be true if there is more notification messages to download.
messageList
WEInboxMessage
Collection of WEInboxMessage objects. With additional details of each notifications.
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
Swift
Objective-C
let messagesList = weInboxData.messageList
let messageObject = messagesList[i]

if let pushTemplateData = messageObject.message as? PushNotificationTemplateData{
 let title = pushTemplateData.title
 let description = pushTemplateData.body
 let customData = pushTemplateData.customData
}
NSArray *messageList = weInboxData.messageList;
WEInboxMessage *messageObject = messageList[i];
PushNotificationTemplateData *pushData = (PushNotificationTemplateData *) messageObject.message;
NSString *title = pushData.title;
NSString *description = pushData.body;
NSDictionary *customData = pushData.customData;
Name
Swift Variable type
Objective-C Variable Type
Definition
title
String?
NSString *_Nullable
Title of the notification.
body
String?
NSString *_Nullable
Description of the notification.
callToActionsList
[String: AnyObject]?
NSDictionary<NSString*,id> _Nullable
call to action Button details of the notification.
customData
[String: AnyObject]?
NSDictionary<NSString*,id> _Nullable
One can access the custom key-value pairs with this.
summary
String?
NSString *_Nullable
Summary of the notification
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
You can track this event when a user has marked the message as 'Read'.
Swift
Objective C
// inboxMessage: WEInboxMessage
inboxMessage.markRead()
[inboxMessage markReadWithAttributes:nil];
Mark notifications Read in Bulk
Swift
Objective C
// listOfInboxData: [WEInboxMessage]
WENotificationInbox.shared.markStatus(listOfInboxData), status: .READ)
// listOfInboxData: NSArray<WEInboxMessage *>
[[WENotificationInbox shared] markStatus:listOfInboxData status:Read];
Mark a notification as unread
This marks the notification as unread. User can mark the already Read message as Unread.
Swift
Objective C
// inboxMessage: WEInboxMessage
 inboxMessage.markUnread()
// inboxMessage: WEInboxMessage
[inboxMessage markUnreadWithAttributes:nil];
Mark notifications as Unread in bulk
Swift
Objective C
// listOfInboxData: [WEInboxMessage]
 WENotificationInbox.shared.markStatus(listOfInboxData, status: .UNREAD)
// listOfInboxData: NSArray<WEInboxMessage *>
[[WENotificationInbox shared] markStatus:listOfInboxData status:Unread];
Mark notification Delete
Marking the status of a message to delete, will delete the message from the notification list from remote.
Swift
Objective C
// inboxData: WEInboxMessage
inboxData.markDelete()
// inboxMessage: WEInboxMessage
[inboxMessage markDeleteWithAttributes:nil];
Mark Notification as Delete in Bulk
Swift
Objective C
// listOfInboxData: [WEInboxMessage]
WENotificationInbox.shared.delete(listOfInboxdata: listOfInboxData)
// listOfInboxData: NSArray<WEInboxMessage *>
[[WENotificationInbox shared] deleteWithListOfInboxdata:listOfInboxData];
Track the user activity with the notifications
Track Views/Impressions
For example, if a user have viewed the message from the notification inbox and to keep a track on the viewed impression, you can call the
trackView()
.
Swift
Objective C
// inboxMessage: WEInboxMessage
inboxMessage.trackView()
// inboxMessage: WEInboxMessage
[inboxMessage trackViewWithAttributes:nil];
Track notification message Click
For example, if a user have clicked the message from the notification inbox and to keep a track on the clicked impression, you can call the
trackClick()
.
Swift
Objective C
// inboxMessage: WEInboxMessage
inboxMessage.trackClick()
// inboxMessage: WEInboxMessage
[inboxMessage trackClickWithAttributes:nil];
Track the click on the notification icon/button
You can track the user's click on the notification Icon. This should be added to track the click of icon/button which will show the list. This will reset the notification count fetched.
Swift
Objective C
WENotificationInbox.shared.onNotificationIconClick()
[[WENotificationInbox shared] onNotificationIconClick];
Sample Notification Inbox Module
WebEngage has built a sample Notification Inbox module that is a plug-and-play solution. This solution is beneficial for clients who still haven't created a Notification Inbox in their apps. You can learn more about the module and its flexibilities
here
.
Updated
about 2 months ago
Customizing Push Notifications
Callbacks
Copy Page
