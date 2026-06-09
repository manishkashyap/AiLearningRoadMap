# Copy Push to Web Inbox

- URL: https://docs.webengage.com/docs/copy-to-web-inbox
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Website
Copy Push to Web Inbox
Notification Inbox is a powerful feature through which your users can have a unified and streamlined notification experience, where they can easily access and manage their notifications in one place.
Through WebEngage, you can now
copy push notifications to your web's Notification Inbox
. In this approach the web/app will have the control on the notification message layout, while through WebEngage integration the message data will be passed on to your app, thereby providing your users personalized experiences.
📘
Notification Inbox as a complete channel to be launched soon!
Prerequisites
To get started with integrating Notification Inbox make sure:
WebEngage Web SDK is integrated
SDK authentication is enabled. (You can enable it by following the steps in
this document
Intialization steps mentioned in this doc are completed. Once done, you can raise a request to us on
[email protected]
to enable this feature.
Initialize the Web SDK
Follow the steps mentioned in
this document
to integrate and initialize the latest version of WebEngage Web SDK.
Methods to call Notification Messages
Retrieve unread notification count
JavaScript
webengage.notificationInbox.getUserNotificationCount(callback)
Get notification messages:
JavaScript
var notifications = [] // Use this to access each message object, and do operations
webengage.notificationInbox.getNotificationList({}, function (data) {
 notifications.push(...data)
})
Get notification messages with offset:
JavaScript
webengage.notificationInbox.getNotificationList(notifications[lastMessageIndex], function (data) {
 notifications.push(...data)
})
Track Notification Events
Track Views/Impressions
JavaScript
notifications[index].view()
Track notification Read
You can track this event when a user has marked the message as 'Read'.
JavaScript
notifications[index].read()
Track notification Clicks
JavaScript
notifications[index].click(actionId, actionLink, isPrime, aTarget)
Track notification Delete
JavaScript
notifications[index].delete()
Track Notification Bulk Detele
JavaScript
// callback is optional
webengage.notificationInbox.delete(notifications, callback)
Track Notification Bulk Read
JavaScript
// callback is optional
webengage.notificationInbox.markStatus(notifications, 1, callback)
Track Unread Notification
JavaScript
notifications[index].unread()
Track Bulk Unread Notification
JavaScript
// callback is optional
webengage.notificationInbox.markStatus(notifications, 2, callback)
Track the click on the notification icon/button
JavaScript
webengage.notificationInbox.onNotificationIconClick()
Updated
7 months ago
On-site Survey
Callbacks
Copy Page
