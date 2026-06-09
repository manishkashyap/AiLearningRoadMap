# Push Troubleshooting

- URL: https://docs.webengage.com/docs/android-push-troubleshooting-guide
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
Push Messaging
Push Troubleshooting
Solutions to a few problems commonly faced by developers while enabling Push for Android
Basic Troubleshooting Guide
The easiest way to check if push notifications are working correctly is by sending a push campaign to specific users and then troubleshoot at each step in the push delivery pipeline.
Step 1: Send Push Campaign to Specific Users
Create a new user segment using your user ID as shown below. Send a one-time campaign to this segment.
Click to enlarge
Step 2: Check if Push is Sent Through WebEngage Push Pipeline
After launching this campaign, check the campaign’s screen for the number of messages sent. This number indicates the number of messages that were sent out by the WebEngage push pipeline.
🚧
Note that push notifications may take up to 15 minutes to be delivered after being triggered to be sent.
If after this time the
Sent
counter does not indicate that messages have been sent, this means that the messages have not been sent by the WebEngage pipeline. Check if there is a problem with Google Cloud Messaging / Firebase Cloud Messaging / Apple Push Notification service settings. Go to your
Data Platform > Integrations > Push Setup (Configure)
settings.
Step 3: Verify Credentials Added to Dashboard
Verify that the Android app
Package Name
and
FCM Server Key
are entered correctly under the
Data Platform > Integrations > Push Setup (Configure) > Channel > Push
section in your dashboard.
Case 1: Notification is Sent, But Not Received
Please consider the following factors to debug:
1. Instrumentation Problem
If this is the case, then there is most likely an instrumentation problem in the app. The push message not being displayed in spite of reaching the device could be caused by problems in push message reception logic in the app. Double-check this if you are using a custom push notification listener/receiver.
On Android, you can use ADB to verify if the push message bundle has been received. Send a push campaign while the device is set for debugging. You should be able to see the following message from WebEngage in the ADB log, showing that the push message bundle from WebEngage is received.
Java
D/WebEngage: Processing event: push_notification_received, system-data: {experiment_id=cnbdng||31b9143eacbi2e0_7cdb47cc-edb8-4066-a0f7-82516b413c04#1:1588737902383, id=~6449370}, event-data: {amplified=false}
If a push notification bundle is received but the notification is not displayed, check if any customizations have been done to the push in the app or if you are using a custom notification listener/receiver and if that is configured properly. The custom listener/receiver might be intercepting and handling the push instead of the WebEngage SDK. If this is the case, it could cause the message to not appear or events like push click to not be tracked.
2. User Opted out of Push Notifications
Make sure the user profile you are using for testing is not
opted out
from receiving push notifications.
3. Push Notifications Blocked on Device
Push notifications can be blocked on the device because of multiple reasons. Operating systems give users a choice to do that for a particular app. In case of Android, neither the GCM token is invalidated nor the GCM app server is informed about this de-activation.
Make sure your app has push notification permissions. Some battery saving apps also force stop running apps, because of which push notifications of those apps couldn’t be delivered.
4. Device Specific Issues
Verify your device’s network connection. Unstable network connection may potentially prevent push notifications from arriving. Make sure background data is not restricted for your app and for Google Play Services app. If mobile or Wi-Fi data usage is restricted then SDK will not be able to make a network connection and so push notifications will not be delivered.
Some Xiaomi and Lenovo devices are known to not receive push notifications after the app is force killed.
For Xiaomi devices:
If auto start permission is not given to application then background processes are restricted. This blocks push notifications if application is force killed by user. It also affects WebEngage
session management
since the session destroy timer of 15 seconds is not triggered and hence background session is never created.
If power saver mode is on for your application, background process and network connectivity is restricted. This affects push notifications, event reporting and displaying images for carousel or banner notification.
UnknownHostException
is thrown from apache HTTP client when trying to make any HTTP connection.
You can expand push notifications on Xiaomi devices with a 2-finger pinch-to-zoom gesture.
OnePlus devices: If "Battery Optimization" is turned on for your app, push notifications are not received after the app is force killed.
5. Additional Troubleshooting
If you are still not able to identify the issue, then:
Reset app preferences by going to your device's
Settings
app >
Apps
>
Menu Button
>
Reset app preferences
.
Prevent power saving mode from activating, for example by leaving your phone plugged into a power source.
Keep your Wi-Fi on during sleep mode by going to your phone's
Settings
app >
Wi-Fi
>
Settings
icon >
Keep Wi-Fi on during sleep
>
Always
.
Uninstall any task killers. These will hinder the app from receiving messages when you are not using it.
Update Google Play Services app.
Toggle mobile data / WiFi on/off setting.
7. Specifically for Android 4.1 – 4.4:
Make sure that Wi-Fi optimization is turned off in your phone's
Settings
app >
Wi-Fi
>
Menu Button
>
Advanced
>
Wi-Fi optimization
.
8. Specifically for Android 6.0+:
Make sure Do not disturb is turned off or you have allowed your app notifications in priority mode in your phone's
Settings
app >
Sound
>
Do not disturb
.
If none of the above steps help, it is possible that you are not receiving updates from Google's Push Notification Service.
Case 2: Message Received on Device, But Clicks Not Recorded
If your push messages are being sent as expected but the click counts are not reflected on the WebEngage dashboard, make sure that your Android application is
passing messages to WebEngage SDK
correctly.
Case 3: Unable to Receive Push Notifications
If push notification is not showing up on your device, then please check the following parameters:
Make sure that WebEngage SDK is
successfully integrated
.
Make sure you have
integrated FCM
.
Make sure you have entered the correct FCM Server Key and package name under the
Data Platform
>
Integrations>
>
Push Steup (Configure)
>
Push
section in your dashboard.
Click to enlarge
Make sure that your FCM Server Key is not restricted to only accept requests from certain IP addresses.
Make sure that you wait for at least 10 minutes after installing your application as it take some time for the device to become push reachable after its first launch. "First launch" is any launch after installation.
If testing on an emulator, try cleaning and rebuilding your project, and restarting ADB.
Check that the device is set to show push notifications from this app under device
Settings
menu.
Some devices (Xiaomi, Lenovo) do not show push notifications if you force kill the app. In such devices you need to grant extra
permissions
so that your app can restart in the background.
If you have implemented
push notification callbacks
then make sure that you are not doing anything that might cause an
Exception
in
onPushNotificationReceived
method.
Make sure that the user is not
opted out
from receiving push notifications from WebEngage.
Make sure that the current status of your push notification campaign on dashboard is
Ended
. If the status is
Failed
, contact WebEngage support at [
[email protected]
](mailto:
[email protected]
).
Case 4: Push Notifications' Small Icon Appears as a Solid White Square
Since the release of Lollipop (API 21), the
material design style
dictates that all non-alpha channels in notification icons be ignored. Therefore, the small notification icon will be rendered solid white if it is not transparent.
Hence, if you have provided a custom small icon during SDK initialisation as shown above, then you need to make sure that it is transparent.
We hope this has helped you get
Push Notifications
up and running for your Android app. Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
6 months ago
Customizing Push Notifications
Configuring Custom Channels & Sound
Copy Page
