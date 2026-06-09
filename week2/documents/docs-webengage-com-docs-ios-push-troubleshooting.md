# Push Troubleshooting

- URL: https://docs.webengage.com/docs/ios-push-troubleshooting
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
Push Messaging
Push Troubleshooting
Solutions to a few problems commonly faced by developers while enabling Push for iOS
1. Can I use different Development & Distribution Certificates for testing Push Notifications in Development & Production builds through the same account?
No, as of now you cannot use two different certificates for the same account. However, you may create a separate account for testing push notifications in Development mode using a development certificate.
You may also create a Universal Certificate to test push notifications on both the environments. But it would still require you to change the mode (Development / Production) on WebEngage dashboard.
2.
'application: didReceiveRemoteNotification: fetchCompletionHandler:'
method not getting called on iOS 10 devices when the user taps on the Push Notification?
This method is deprecated in iOS 10 and WebEngage SDK makes use of new
UserNotifications
Framework for iOS 10. You can solve this problem in one of the following ways:
Implement the
UserNotifications
framework's
UNNotificationCenterDelegate
protocol to get the click callback against this deprecated method.
OR
In your Podfile (if using CocoaPods), change the
WebEngage
dependency to
WebEngage/Xcode7
. The Xcode7 WebEngage dependency doesn't use the new
UserNotifications
framework and hence your pre iOS 10 callbacks are triggered as expected. In case you are using the Direct Integration method, the Xcode7 binary is located under the xc7 directory in the downloaded WebEngage SDK distribution that your should integrate with.
📘
Please Note
In case you are using Rich Push Notifications, add
pod 'WebEngage/Xcode7'
only in your Main App Target. For the
Notification Service Extension
and
Notification Content Extension
targets, use the
pod WebEngage
dependency only.
Refer to the sample Podfile below:
target 'MyAppTarget' do
 
 pod 'WebEngage/Xcode7'
 
end

target 'NotificationService' do
 
 pod 'WebEngage'
 
end

target 'NotificationViewController' do
 
 pod 'WebEngage'
 
end
3. I am trying to send a push notification but it is failing with the error "Not Registered" for some/most users.
If you are getting
Not Registered
error for your users, first of all make sure these users were not created while testing the integration on a simulator.
You can do that by identifying the concerned user ID in the
List of Users
section under
Users
on the dashboard. Check if there is any "APNs Registration Failed" event logged in the Activity section.
In case you observe any "APNs Registration Failed" event:
Expand the "APNs Registration Failed" event to check the
error_description
attribute. It will help you get an idea on why your device registration is failing.
Click to enlarge
Add
WEGLogLevel
key in your Info.plist file with the value as "VERBOSE", launch the app again and search for the error logs or implement application:didFailToRegisterForRemoteNotificationsWithError: and put a debug point to catch the error causing the failure.
Common reasons:
Testing in the Simulator doesn't work.
Push notifications don't work in the simulator. You should use a real device for testing the same.
APNs entitlement not found.
Select the project from the Navigation Menu. Go to
Capabilities
>
Push Notifications
and switch on
Push Notifications
. Refer to the screenshot below.
Click to enlarge
4. App is unable to receive Remote Push Notifications. How to debug?
Make sure the
SDK is successfully integrated
and initialized.
If your app uses
WebEngage login APIs
and you are testing for a particular user logged in to your app, verify on the dashboard if "GCM Registered" event is listed under the User Activity section. If it is not listed in the activity and/or
APNS Registration Failed
event is observed, verify the
reason for device APNs registration failure
.
If "GCM Registered" event was observed for the user in concern, make sure the device under test is observed under the user's devices in Iser profile on the dashboard. If the device is not found in the user profile, uninstall the app from the device and reinstall after waiting for around 5 minutes. Observe that you find a fresh "GCM Registered" event for the user. Try to send a push message again. You can also check if "GCM Registered" / "APNS Registration Failed" events were fired or not by checking the console logs in Verbose mode. Look for
gcm_registered
or
apns_registration_failed
. You can use the same method to debug for anonymous users as well.
Make sure you have uploaded the .p12 file with correct details, including your bundle identifier, password etc. Also, the environment (Development/Distribution) for your .p12 file should match with that of your app build that you are testing with. For development builds, you need to use a development .p12 certificate, which is different from your distribution certificate for App Store build.
5. WEGHandleDeeplink delegate method not getting called when push notification is clicked
This also applies in cases when Push Notification Clicked event does not get recorded.
This happens when the WebEngage delegate gets overwritten by some other delegate like
UNUserNotificationCenterDelegate
. If
UNUserNotificationCenterDelegate
delegate is set to
self
after initializing WebEngage SDK in
didFinishLaunchingWithOptions
, it overwrites the notification delegate and hence WebEngage notification delegate will not work.
Hence it is recommended that you initialize WebEngage SDK at the end of
didFinishLaunchingWithOptions
, just before returning
YES
. This is illustrated below.
Objective-C
UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
 center.delegate = self;
//Initialize WenEngage after setting the above delegate
[[WebEngage sharedInstance] application:[UIApplication sharedApplication] didFinishLaunchingWithOptions:launchOptions notificationDelegate:self autoRegister:YES];
6. I am not receiving images in push notifications. I receive only the text messages. How do I enable rich push notifications?
Please ensure that all the steps to implement Rich Push Notifications as per our
documentation
have been implemented. If you still face issues, please verify the following:
Ensure that Deployment Target is set to iOS 10 or above for Notification Service & Content Extension Targets
Ensure that
platform: ios, '10.0'
or similar is specified in Podfile
Ensure that appropriate App Groups for Extension & App Target is set in Xcode Capabilities tab
If you are using
https://
image URLs, ensure App Transport Security (ATS) key is set in Extension Targets
Ensure that Info.plist of Content Extension Targets has appropriate
NSExtension
keys
Ensure that you haven't specified
use_frameworks!
in your Podfile
Run
pod install
again after removing
use_frameworks!
Depending on your project, some other third party dependencies might not have been updated & may cause build errors after removing
use_frameworks!
. It's recommended that you update to the latest version of such dependencies.
7. How can push notifications be shown to a user if app is in foreground?
Enable Background Modes/Remote notifications to be able to use remote notifications properly. In Xcode, navigate to Targets -> Your App -> Capabilities -> Background Modes and check Remote notifications. This will automatically enable the required settings.
Now, to show notifications while being in the foreground (available starting from iOS 10) add the following code snippet:
Swift
import UserNotifications

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

 func application(_ application: UIApplication,
 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool { 
 ...
 UNUserNotificationCenter.current().delegate = self
 return true
 }
}

extension AppDelegate: UNUserNotificationCenterDelegate {
 @available(iOS 10.0, *)
 func userNotificationCenter(_ center: UNUserNotificationCenter,
 willPresent notification: UNNotification,
 withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
 
 completionHandler([.alert, .badge, .sound])
 }
}
We hope this has helped you get
Push Notifications
up and running for your iOS app. Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Push Messaging
Customizing Push Notifications
Copy Page
