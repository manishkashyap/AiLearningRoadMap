# Push Messaging

- URL: https://docs.webengage.com/docs/unity-android-push-notifications
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Unity.Android
Push Messaging
🚧
Before continuing, please ensure that you have
added the WebEngage SDK to your app
.
Method 1: Using FCM Unity Plugin
Step 1:
Import FCM Unity plugin as instructed
here
into your Unity project.
Step 2:
If you have replaced the
Assets/Plugins/Android/AndroidManifest.xml
then make sure to add back your WebEngage license-code and debug-mode meta-data tags in the
AndroidManifest.xml
file.
Step 3:
In your script where you have registered callbacks for
OnTokenReceived
and
OnMessageReceived
, add the following code snippets.
C#
using WebEngageBridge;
 ...
 Firebase.FirebaseApp.CheckAndFixDependenciesAsync().ContinueWith(task => {
 var dependencyStatus = task.Result;
 if (dependencyStatus == Firebase.DependencyStatus.Available)
 {
 Firebase.Messaging.FirebaseMessaging.TokenReceived += OnTokenReceived;
 Firebase.Messaging.FirebaseMessaging.MessageReceived += OnMessageReceived;
 }
 else
 {
 ...
 }
 });
 
 public void OnTokenReceived(object sender, Firebase.Messaging.TokenReceivedEventArgs token)
 {
 ...
 WebEngage.SetPushToken(token.Token);
 }

 public void OnMessageReceived(object sender, Firebase.Messaging.MessageReceivedEventArgs e)
 {
 Dictionary<string, string> data = new Dictionary<string, string>(e.Message.Data);
 if (data.ContainsKey("source") && "webengage".Equals(data["source"]))
 {
 WebEngage.SendPushData(data);
 }
 ...
 }
🚧
Please Note
Using this method,
Push Notifications
will work as expected when the app is in foreground. However, they will not be shown when the app is in background. In such cases, the notification will be cached and will be shown whenever the app is launched next by the user. If you wish to prevent this behavior, then please follow the steps to
Overriding FCM Unity Plugin,
as described below.
Method 2: Overriding FCM Unity Plugin
Step 1:
Import FCM Unity plugin as instructed
here
into your Unity project.
Step 2:
If you have replaced the
Assets/Plugins/Android/AndroidManifest.xml
then make sure to add back your WebEngage license-code and debug-mode meta-data tags in the
AndroidManifest.xml
file.
Step 3:
Download and add the
webengage-android-fcm.aar
file in
Assets/Plugins/Android/
directory of your Unity project.
Step 4:
Add the following service tag in your
Assets/Plugins/Android/AndroidManifest.xml
file as shown below.
XML
<?xml version="1.0" encoding="utf-8"?>
<manifest
 ...>

 <application
 ...>

 <service android:name="com.webengage.android.fcm.WebEngageFirebaseMessagingService">
 <intent-filter>
 <action android:name="com.google.firebase.MESSAGING_EVENT" />
 </intent-filter>
 </service>

 ...
 </application>
</manifest>
Step 5:
Update the FCM registration token on app start as shown below.
C#
using WebEngageBridge;
 ...

 WebEngage.UpdateFcmToken();
Please feel free to drop in a few lines at
[email protected]
in case you have any queries or feedback. We're always just an email away!
Updated
7 months ago
Tracking Events
In-app Messaging
Copy Page
