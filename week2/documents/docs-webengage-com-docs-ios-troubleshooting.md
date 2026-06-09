# Troubleshooting

- URL: https://docs.webengage.com/docs/ios-troubleshooting
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
Troubleshooting
1. Where do I find the WebEngage license code for SDK integration?
You will find your License Code on the WebEngage dashboard. Log in to your WebEngage dashboard and go to
Account Setup
section, as highlighted in the image below. Note that your License Code might start with tilde (
~
), please include it as a part of the entire license code while copying.
It is the value of
Info.plist
key:
WEGLicenseCode
Click to enlarge
2. How do I pass the device token to WebEngage SDK if I am manually registering APNs?
WebEngage SDK will automatically receive the token when it is received via APNs registration call, provided you have initialized the SDK properly.
If you are making the APNs registration manually, you will receive the device token in your app’s AppDelegate callback
application:didRegisterForRemoteNotificationsWithDeviceToken:
.
You may implement this callback for your own custom handling. WebEngage SDK automatically intercepts your callback method to receive the device token.
📘
For manually registering your app with APNS, you need to call the appropriate initialization API with the auto-register flag as
NO
(or
false
). Refer to
Initialization APIs
.
3. How do I verify the integration status?
Enable Verbose logging by adding the
WEGLogLevel
key in the
Info.plist
file and set its value to
VERBOSE
.
Launch your app through Xcode and verify the logs. Search for the log statement: "SDK Integration Verification complete" in the Xcode console. In case it's there, your SDK integration is likely to be complete and correct unless your configuration values are wrong. If you don't see this statement,
continue with the troubleshoot
.
📘
Please Note
Double-check your license code in the
Info.plist
(
WEGLicenseCode
key) against the WebEngage dashboard.
4. I didn't get the log message, 'SDK Integration Verification complete'. How do I troubleshoot?
If you do not find a log message saying 'SDK Integration Verification complete', you should get one saying
SDK Integration is not complete. Validations failed
. You may get other specific error messages (s) before this log. In that case, act according to the instructions in the error message.
5. Users/Events not showing up in dashboard even after successful SDK integration. How do I troubleshoot?
Please go over the following checklist:
Make sure you have
successfully integrated
WebEngage SDK in your app.
Verify that your
license code is correctly configured
in your
Info.plist
file.
Check the logs for the error messages
Error while reporting the event to network
and
Error: Timeout occurred while waiting for events response in flush
. The error messages may also provide some context of the error that occurred while trying to sync events.
In case handling the error is out of the scope of your app, let us know at
[email protected]
with the detailed console logs after enabling
Verbose logging
in
Info.plist
.
📘
Successful Event Reporting from SDK
In case events are successfully sent from the SDK, the console should print a message
Reported Events to Network
in the Verbose mode. In case you observe this log on the console but events/users not showing up on the dashboard, contact support at
[email protected]
.
6. How do I know which version of the WebEngage iOS SDK is being used in my app?
In case you have integrated WebEngage using CocoaPods, check the
Podfile.lock
file in your project directory. This file stores the WebEngage SDK version.
For Direct Integration, look for the
Info.plist
file in the WebEngage.framework directory (within the downloaded and extracted .zip file). For the WebEngage SDK version, check the file for the property named
Bundle versions string, short
if viewing in the visual editor. Check for
CFBundleShortVersionString
when viewing in the source code editor.
7. What's the latest available version of the WebEngage iOS SDK?
You can check
this link
for the latest publicly released version of the SDK.
Other than that we also make internal beta releases. Beta releases are only available through CocoaPods integration. You can get the latest beta released SDK version details
here
.
8. How do I update to the latest WebEngage iOS SDK version?
Updating WebEngage coreSDK
If you are using CocoaPods, go to your project directory or the directory holding the Podfile in the terminal and execute:
WebEngage
pod update WebEngage
Updating Rich Push/Extension SDKs
WebEngage Rich push SDK supports sending rich content in push notifications (images, carousel etc.) along with optimizations for tracking push impressions. If you have not installed our rich push SDK, please click
here
.
To update to our latest ServiceExtension SDK, go to your project directory or the directory holding the Podfile in the terminal and execute:
ServiceExtension
pod update WebEngageBannerPush
To update to our latest ContentExtension SDK, go to your project directory or the directory holding the Podfile in the terminal and execute:
ContentExtension
pod update WebEngageAppEx
The command should show up the latest version being installed. Verify from
here
if the downloaded version is actually the latest version.
- In case the above step doesn't download the latest version of the SDK, run:
Shell
pod repo update
And then again re-run the previous commands.
For Direct Integration, first
check the version
of iOS SDK you've installed. If you are not using the latest version, download the latest version from
here
and replace the existing one under
Linked Frameworks and Libraries
section of the project settings. Refer Direct Integration under
iOS SDK Setup
.
We hope this has helped you integrate your iOS app with WebEngage. Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
9. How to fix the warning from Apple (app includes references to location-related APIs)?
Currently, the iOS SDK requires clients to add the
NSLocationAlwaysAndWhenInUseUsageDescription
&
NSLocationWhenInUseUsageDescription
keys along with a placeholder purpose string in the Info.plist, even if their app does not use location services.
For apps that do not use location services should migrate from WebEngage to WebEngage/Core. Below are the steps:
Step 1:
Update your Podfile by replacing:
Ruby
pod 'WebEngage'
with:
Ruby
pod 'WebEngage/Core'
And then run the following command on terminal.
Shell
$ pod install
This change ensures you're using only the core functionalities of the WebEngage SDK, excluding location-related capabilities.
Step 2:
If your app doesn’t require location tracking, remove the following keys from your Info.plist file:
NSLocationAlwaysAndWhenInUseUsageDescription
NSLocationWhenInUseUsageDescription
These keys are no longer necessary when using the core variant and helps avoid unnecessary warnings during publishing the app to AppStore.
Updated
7 months ago
Advanced
Apple Privacy Manifest Update
Copy Page
