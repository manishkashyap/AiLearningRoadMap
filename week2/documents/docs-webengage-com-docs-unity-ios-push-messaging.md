# Push Messaging

- URL: https://docs.webengage.com/docs/unity-ios-push-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Unity.iOS
Push Messaging
🚧
Before continuing, please ensure that you have
added the WebEngage SDK to your app
.
Enable Push Messaging
Here's how you can go about it:
Step 1:
Build your iOS app through Unity Editor and open
Unity-iPhone.xcodeproj
in your
Xcode IDE
.
Step 2:
Select your main app target (Unity-iPhone), under Capabilities enable Push Notifications.
Step 3:
Also under Capabilities enable Background Modes and check Remote notifications.
Configure Rich Push Notifications
Step 1:
Enable Push Notifications, App Groups, and add the app group
group.<your-bundle-identifier>.WEGNotificationGroup
to your App ID from your Apple Developer Account.
Step 2:
Download and install the updated provisioning profile of your app in your Xcode.
Banner Push Notifications
Step 1:
Add a new App Bundle ID
<your-bundle-identifier>.NotificationService
, enable Push Notifications, App Groups, and add the group
group.<your-bundle-identifier>.WEGNotificationGroup
in this newly created App ID from your Apple Developer Account. Download and install the provisioning profile of this App ID in your Xcode.
Step 2:
Download the
WebEngageNotificationService.unitypackage
.
Step 3:
Import the downloaded
unitypackage
into your Unity project through
Assets > Import Package > Custom Package....
Step 4:
Build your iOS app through Unity Editor and open
Unity-iPhone.xcodeproj
in your
Xcode IDE
.
Step 5:
Verify that the
NotificationService
extension is added and linked to your main app target.
Rating and Carousel Push Notifications
Step 1:
Add the App Bundle ID
<your-bundle-identifier>.NotificationViewController
, enable Push Notifications, App Groups, and add the group
group.<your-bundle-identifier>.WEGNotificationGroup
in this newly created App ID from your Apple Developer Account. Download and install the provisioning profile of this App ID in your Xcode.
Step 2:
Download the
WebEngageNotificationContent.unitypackage
.
Step 3:
Import the downloaded
unitypackage
into your Unity project through
Assets > Import Package > Custom Package
Step 4:
Build your iOS app through Unity Editor and open
Unity-iPhone.xcodeproj
in your
Xcode IDE
.
Step 5:
Verify that the
NotificationViewController
extension is added and linked to your main app target.
Troubleshooting for Rich Push Notifications
If you are facing integration or build issues with rich-push notification unity plugins, then try adding the extensions and pods manually.
Remove the
WebEngageNotificationService.unitypackage
and
WebEngageNotificationContent.unitypackage
plugins (if added).
Build your iOS app through Unity Editor and open
Unity-iPhone.xcodeproj
in your
Xcode IDE
.
Follow the instructions in
WebEngage documentation
.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
In-app messaging
Copy Page
