# Troubleshooting

- URL: https://docs.webengage.com/docs/react-native-troubleshooting
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
React Native
Troubleshooting
1. Unable to receive Push Notifications on my Android app after integrating WebEngage with the Invertase React Native Firebase SDK. How can I solve this?
Before proceeding, please ensure that you've followed all the steps mentioned under
React Native Android Push Messaging
.
Here's how you can troubleshoot:
Step 1:
Modify the
onMessageReceived
method in the
MyFirebaseMessagingService.java
file:
Java
public class MyFirebaseMessagingService extends FirebaseMessagingService {
 @Override
 public void onMessageReceived(RemoteMessage remoteMessage) {
 Map<String, String> data = remoteMessage.getData();
 if (data != null && data.containsKey("source") && "webengage".equals(data.get("source"))) {
 WebEngage.get().receive(data);
 } else {
 (new io.invertase.firebase.messaging.RNFirebaseMessagingService()).onMessageReceived(remoteMessage);
 }
 }
 ...
 }
Step 2:
Add the
MyFirebaseMessagingService
tag above the
RNFirebaseMessagingService
tag in the
AndroidManifest.xml
file.
And you're good to go :)
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
2. How to fix the warning from Apple (app includes references to location-related APIs)?
Currently, the iOS SDK requires clients to add the
NSLocationAlwaysAndWhenInUseUsageDescription
&
NSLocationWhenInUseUsageDescription
keys along with a placeholder purpose string in the Info.plist, even if their app does not use location services.
For apps that do not use location services should migrate from WebEngage to WebEngage/Core. Below are the steps:
Step 1:
Add this at the top of your PodFile
Ruby
ENV['WEBENGAGE_USE_CORE'] = 'true'
And then run the following command on terminal.
Shell
$ pod install
This change ensures you're using only the core functionalities of the WebEngage SDK, excluding location-related capabilities.
Step 2:
If your app doesn’t require location tracking, remove the following keys from your Info.plist file:
NSLocationAlwaysAndWhenInUseUsageDescription
NSLocationWhenInUseUsageDescription
These keys are no longer necessary when using the core variant and helps avoid unnecessary warnings during publishing the app to AppStore.
🚧
In case, you have added WebEngage manually in the podfile, remove it.
Updated
7 months ago
Advanced
App In-line Content
Copy Page
