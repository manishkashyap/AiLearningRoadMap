# Push Messaging

- URL: https://docs.webengage.com/docs/xamarin-android-push-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.Android
Push Messaging
Push notifications are messages that pop up on mobile devices. App publishers can send them at any time; even if the recipients aren’t currently engaging with the app or using their devices.
🚧
Before continuing, please ensure that you have
added the WebEngage SDK to your app
.
Enable Push Messaging
Step 1:
Integrate
Xamarin.Firebase.Messaging
Nuget package with your Xamarin.Android app.
Step 2:
Send FCM Registration token to WebEngage from your
FirebaseInstanceIdService
class as shown below.
C#
using Firebase.Iid;
using Com.Webengage.Sdk.Android;
...

[Service] [IntentFilter(new[] {
 "com.google.firebase.INSTANCE_ID_EVENT"
})]

public class YourFirebaseInstanceIdService : FirebaseInstanceIdService
 {
 public override void OnTokenRefresh()
 {
 var refreshedToken = FirebaseInstanceId.Instance.Token;
 SendRegistrationToServer(refreshedToken);
 }

 void SendRegistrationToServer(string token)
 {
 WebEngage.Get().SetRegistrationID(token);
 }
 }
It is recommended to send this token to WebEngage from your Application class as well, as shown below.
C#
using Firebase.Iid;
using Com.Webengage.Sdk.Android;
...
 
 [Application]
 public class YourApplication : Application
 {
 ...

 public override void OnCreate()
 {
 base.OnCreate();
 ...

 string token = FirebaseInstanceId.Instance.Token;
 WebEngage.Get().SetRegistrationID(token);
 }
 }
Step 3:
Send the notification message data to WebEngage from your
FirebaseMessagingService
class as shown below.
C#
using Com.Webengage.Sdk.Android;
...

 [Service] 
 [IntentFilter(new[] {
 "com.google.firebase.MESSAGING_EVENT"
 })]
 public class YourFirebaseMessagingService : FirebaseMessagingService
 {
 public override void OnMessageReceived(RemoteMessage message)
 {
 base.OnMessageReceived(message);
 IDictionary<string, string> data = message.Data;
 if (data.ContainsKey("source") && "webengage".Equals(data["source"])) {
 WebEngage.Get().Receive(data);
 }
 }
 }
Step 4:
Log in to your WebEngage dashboard and navigate to **Data Paltform> Integrations> Push Setup (Configure).
Under the
Android
section, enter your application package name under the field labeled “Package Name”.
Paste your FCM/GCM server key under the field labeled “GCM/FCM Server Key” and click
Save
.
Click to enlarge
And you're good to go!
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away.
Updated
7 months ago
So, what's next?
In-app messaging
Copy Page
