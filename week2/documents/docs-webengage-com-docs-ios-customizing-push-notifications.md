# Customizing Push Notifications

- URL: https://docs.webengage.com/docs/ios-customizing-push-notifications
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
Push Messaging
Customizing Push Notifications
A step-by-step guide to customizing the appearance of iOS Push Notifications through your app
Introduction
Custom push notifications allow businesses to style
Push Notifications
based on their business requirements. These are the features that are offered over and above the push notifications customizations offered on the WebEngage dashboard.
This means you can pass the entire message content and personalize variables while creating a push notification campaign and add features by adding customized functionalities, callbacks, styles, and so on. This can be achieved with the help of
Key-Value Pairs
📘
Please Note
All UI customizations like fonts, background colours, and styles will only be available in the notification content extension (expanded view); owing to iOS platform restrictions, UI stylings will not be considered for standard notifications (non- expanded view).
Custom Push Notifications
allows you to:
Create custom text styles
Create custom backgrounds
Create custom layouts.
Example of customized font and color (Click to enlarge)
Pre-requisites
Before starting to create custom push notifications for iOS, certain prerequisites must be fulfilled:
WebEngage iOS/Hybrid SDK
Set of specific
Key values
to be added to complete the notification creation
Necessary changes have been made on the application side
Let's discuss these pre-requisites further:
Setting Key-Value Pairs
While creating the
Push Notification
campaign, you will find a
Key-value pair
option under the
Message
section. To utilize custom push, provide the following keys and values in the key-value pairs section:
To enable customization:
JSON
we_ios_custom_push : true
For Custom Category:
JSON
we_ios_category : "CUSTOM_CATRGORY_NAME"
Click to open
Changes made on the Application side
Step 1:
Create one content extension using the class
WEXRichPushNotificationViewController
to keep existing WebEngage notifications working.
Step 2:
Create a second Content Extension with a custom UI and a custom category that can be sent to the Notification APS payload from the dashboard as per the new functionality of
custom_ios_push
.
Kindly refer to the documentation for custom appearance
Apple Developer Documentation
for further understanding.
Step 3:
The second content extension will include default classes and protocols.
You will be able to find all notification details in:
Swift
didReceive(_ notification: UNNotification)
Sample APNs Payload
Swift
{
 "aps" : {
 "alert": {
 "body" : "test",
 "title" : "test"
 },
 "category" : "customCategory",
 "content-available" : 1,
 "mutable-content" : 1,
 "sound" : "default"
 },
 "cta_list" :[
 {
 "mainCta" : {
 "ctaId" : "main",
 "deeplink" : ""
 }
 }
 ],
 "customData" : [
 {
 "key" : "provider",
 "value" : "APNS"
 }
 ],
 "expandableDetails" :{
 "cta1" : {
 "actionLink" : "",
 "actionText" : "Yes",
 "id" : "892c07db",
 "templateId" : "56ghe26"
 },
 "category" : "customCategory",
 "image" : "",
 "message" : "test",
 "ratingScale" : 5,
 "style" : "BIG_PICTURE"
 },
 "experiment_id" : "T_~1ni6p4g||~583gfb169jiccfd_c4e9b090-439b-49a2-a5f7-5e4f581cad25#2:1625752052322",
 "license_code" : "licenceCode",
 "notification_id" : "~6oo5f8",
 "source" : "webengage"
}
Tracking notifications actions {Recommended}
Button actions presented on Webengage’s dashboard won’t be directly available to custom category notifications
In order to add those button actions to custom category notification (content extension), you need to register those actions as mentioned in the code below
Swift
import UserNotifications

class NotificationService: WEXPushNotificationService {
 let service = WEXPushNotificationService()
 
 override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
 
 if let apsPayload = request.content.userInfo["aps"] as?[String:Any]{
 if let category = apsPayload["category"] as? String{
 if category == "1234"{ // CHOOSE THEIR CUSTOM CATEGORY NAME
 if let userInfo = request.content.userInfo as? [String:Any]{
 self.registerCTA(category: category,
 userInfo: userInfo,
 dismissActiontitle: "Dismiss")
 }
 }
 }
 }

 service.didReceive(request, withContentHandler: contentHandler)
 }
 
 
 // This will register default CTA's received from WebEngage dashboard
 /// NOTE: This list wont have dismiss type of button You need to manually add them as required
 /// - Parameters:
 /// - category: custom Catgory name where you want to register CTA
 /// - userInfo: Notification payload userInfo
 /// - dismissActiontitle : If you want to have dismiss button then pass title for dismiss
 func registerCTA(category:String,
 userInfo:[String:Any],
 dismissActiontitle:String?){
 var actions:[UNNotificationAction] = []
 if let expandableDetails = userInfo["expandableDetails"] as? [String:Any]{
 for i in 1...3{
 if let ctaDetails = expandableDetails["cta\(i)"] as? [String:Any]{
 if let templateId = ctaDetails["templateId"] as? String,
 let actionText = ctaDetails["actionText"] as? String{
 let actionObject = UNNotificationAction(identifier: templateId,
 title: actionText,
 options: UNNotificationActionOptions(rawValue: 0))
 actions.append(actionObject)
 }
 }
 }
 }
 
 // add dimiss button if required
 if let dismissTitle = dismissActiontitle{
 let actionObject = UNNotificationAction(identifier: "dismiss" // This identifier can be anything
 , title: dismissTitle,
 options: UNNotificationActionOptions(rawValue: 0))
 actions.append(actionObject)
 }
 
 // Define the notification type
 let customCategory =
 UNNotificationCategory(identifier:category,
 actions: actions,
 intentIdentifiers: [],
 hiddenPreviewsBodyPlaceholder: "",
 options: .customDismissAction)
 // Register the notification type.
 let notificationCenter = UNUserNotificationCenter.current()
 notificationCenter.setNotificationCategories([customCategory])
 }

}
Every
Click
on these actions will be tracked by WebEngage SDK Automatically.
Kindly refer to the documentation for Actions
Apple Developer Documentation
for further understanding.
📘
Please Note
All the notification's impressions will be recorded automatically by WebEngage SDK.
The Simple click on a
Notification
will be tracked automatically by WebEngage SDK.
UNNotificationActions
provided to custom categories will be tracked automatically by WebEngage SDK.
Custom buttons and behaviours on custom content extension UI
will not be tracked automatically
by WebEngage SDK; you must manually track these occurrences.
This will register default CTA's received from the WebEngage dashboard and the list won't have dismissed type of button so you need to manually add them as required
Customizing notification content {optional}
If you'd like to customize the content of a notification received via
NotificationService
, you must override the notification service to operate with
WEXPushNotificationService
and your custom notification content.
👍
For example,  if you want to change notification body content to the title if it exceeds the specified character limit ( > 50), show the title without being truncated.
iOS allows us to change the content of body runtime, and we can change it to title and show title as blank to show full title without being truncated.
To work customization and default Web Engage Functionalities, you must override the Notification service extension as demonstrated in the reference code below.
📘
Please Note
Since iOS does not display the body in bold letters, this step will display standard notifications.
Swift
import UserNotifications

class NotificationService: UNNotificationServiceExtension {
 
 let service = WEXPushNotificationService()
 
 override func didReceive(_ request: UNNotificationRequest,
 withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
 
 let bestAttempContent = request.content.mutableCopy() as! UNMutableNotificationContent
 if bestAttempContent.title.count > 60{
 let title = bestAttempContent.title
 bestAttempContent.body = title
 bestAttempContent.title = ""
 }
 let requestCopy = UNNotificationRequest(identifier: request.identifier,
 content: bestAttempContent,
 trigger: request.trigger)
 service.didReceive(requestCopy, withContentHandler: contentHandler)
 }
}
Updated
7 months ago
Push Troubleshooting
Copy Push to Notification Inbox - iOS
Copy Page
