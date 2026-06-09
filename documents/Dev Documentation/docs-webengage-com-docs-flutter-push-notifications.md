# Push Messaging

- URL: https://docs.webengage.com/docs/flutter-push-notifications
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Flutter
Push Messaging
🚧
Before continuing, please ensure that you've
added the Flutter SDK to your app
.
For Android
Push Notifications are messages that pop up on mobile devices. App publishers can send them at any time; even if the recipients aren’t currently engaging with the app or using their devices.
1. Integration with FCM
This section details WebEngage integration with FCM-enabled Flutter Android apps, with options for using a plugin or native code.
CHOOSE ONE
Integrating WebEngage with FCM Using Plugin Methods
Using Android Native Code with FCM Integrated
Integrating WebEngage with FCM Using Flutter Plugin
Follow these steps to set up an FCM client on Flutter.
Set up a Firebase Cloud Messaging client app on Flutter
and
webengage_flutter
Version should be 1.6.0 or Later
Step 1:
Pass Firebase tokens to WebEngage.
Dart
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:webengage_flutter/webengage_flutter.dart';

var token = await FirebaseMessaging.instance.getToken();
if (token != null) {
 WebEngagePlugin.setPushToken(token);
}
To be notified whenever the token is updated, subscribe to the onTokenRefresh stream:
Dart
FirebaseMessaging.instance.onTokenRefresh.listen((token) {
 WebEngagePlugin.setPushToken(token);
 }).onError((err) {});
Step 2:
Message handling
Based on your application's current state, incoming payloads of different messages type require different implementations to handle them:
Foreground messages
Dart
FirebaseMessaging.onMessage.listen((RemoteMessage message) {
 WebEngagePlugin.onPushMessageReceive(message.data);
});
Background messages
Dart
@pragma('vm:entry-point')
Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
 await Firebase.initializeApp();
 WebEngagePlugin.onPushMessageReceive(message.data);
}

void main() {
 //Your previous code
 FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);
 runApp(MyApp());
}
Step 3:
Add your Firebase Credentials to WebEngage
Once all the above steps are completed, you can start sending Push notification!
OR
Using Android Native Code with FCM Integrated
Step 1:
Pass Firebase tokens to WebEngage using
FirebaseMessagingService
.
Java
Kotlin
import com.webengage.sdk.android.WebEngage;
import io.flutter.plugins.firebase.messaging.FlutterFirebaseMessagingService;

public class MyFirebaseMessagingService extends FlutterFirebaseMessagingService {
 @Override
 public void onNewToken(String s) {
 super.onNewToken(s);
 WebEngage.get().setRegistrationID(s);
 }
}
import io.flutter.plugins.firebase.messaging.FlutterFirebaseMessagingService;
import com.webengage.sdk.android.WebEngage;

class MyFirebaseMessagingService : FlutterFirebaseMessagingService() {
 override fun onNewToken(s: String) {
 super.onNewToken(s)
 WebEngage.get().setRegistrationID(s)
 }
 
}
Highly Recommended!
Passing Firebase tokens to WebEngage from the
onCreate
method of your Application class ensures that changes in the user’s Firebase token are communicated to WebEngage. Here's how you can execute this.
Java
Kotlin
import com.google.android.gms.tasks.Task;
import com.google.firebase.messaging.FirebaseMessaging;
import com.google.android.gms.tasks.OnCompleteListener;
import androidx.annotation.NonNull;
import com.webengage.sdk.android.WebEngage;

public class MainApplication extends FlutterApplication {
 @Override
 public void onCreate() {
 super.onCreate();
 
 FirebaseMessaging.getInstance().getToken()
 .addOnCompleteListener(new OnCompleteListener<String>() {
 @Override
 public void onComplete(@NonNull Task<String> task) {
 if (!task.isSuccessful()) {
 Log.w(TAG, "Fetching FCM registration token failed", task.getException());
 return;
 }
 // Get new FCM registration token
 String token = task.getResult();
 WebEngage.get().setRegistrationID(token);
 }
 });
 }
}
import com.google.android.gms.tasks.Task;
import com.google.firebase.messaging.FirebaseMessaging;
import com.google.android.gms.tasks.OnCompleteListener;
import androidx.annotation.NonNull;
import com.webengage.sdk.android.WebEngage;

class MainApplication : FlutterApplication() {
 override fun onCreate() {
 super.onCreate()
 FirebaseMessaging.getInstance().token
 .addOnCompleteListener(OnCompleteListener { task ->
 if (!task.isSuccessful) {
 return@OnCompleteListener
 }
 // Get new FCM registration token
 val token: String = task.getResult()
 WebEngage.get().setRegistrationID(token)
 })
 }
}
Step 2.
Pass messages to WebEngage while using Flutter Firebase Messaging plugin.
Create a class that extends
FlutterFirebaseMessagingService
and pass messages to WebEngage.
Java
Kotlin
import com.google.firebase.messaging.RemoteMessage;
import com.webengage.sdk.android.WebEngage;

import java.util.Map;

import io.flutter.plugins.firebase.messaging.FlutterFirebaseMessagingService;

public class MyFirebaseMessagingService extends FlutterFirebaseMessagingService {
 public void onMessageReceived(RemoteMessage remoteMessage) {
 super.onMessageReceived(remoteMessage);
 Map<String, String> data = remoteMessage.getData();
 if(data != null) {
 if(data.containsKey("source") && "webengage".equals(data.get("source"))) {
 WebEngage.get().receive(data);
 }
 }
 }

 public void onNewToken(String s) {
 super.onNewToken(s);
 WebEngage.get().setRegistrationID(s);
 }
}
import io.flutter.plugins.firebase.messaging.FlutterFirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;
import com.webengage.sdk.android.WebEngage;

public class MyFirebaseMessagingService : FlutterFirebaseMessagingService() {

 override fun onMessageReceived(remoteMessage: RemoteMessage) {
 val data = remoteMessage.data
 if (data != null) {
 if (data.containsKey("source") && "webengage" == data["source"]) {
 WebEngage.get().receive(data)
 }
 }
 }
}
Step 3.
Register the service to the application element of your
AndroidManifest.xml
file as shown below.
XML
<service
 android:name=".MyFirebaseMessagingService"
 android:exported="false" >
 <intent-filter>
 <action android:name="com.google.firebase.MESSAGING_EVENT"/>
 </intent-filter>
</service>
Step 4.
Add your Firebase Credentials to WebEngage
Once all the above steps are completed, you can start sending Push notification!
2. Integration without FCM
📘
These steps are for clients who have not yet integrated FCM with their Flutter App. If FCM is already integrated with your app kindly check
this
section for integration steps.
You can start sending Push Notifications to your Android users via WebEngage by configuring Firebase Cloud Messaging (FCM).
Here's how you can enable Push Messaging for your Android app via the WebEngage Flutter SDK.
Step 1:
Add Firebase to Your Project by following the necessary steps in
FCM Docs
Step 2:
Add the below dependencies in the app-level
build.gradle
file.
Groovy
implementation platform('com.google.firebase:firebase-bom:25.12.0')
implementation 'com.google.firebase:firebase-analytics'
implementation 'com.google.firebase:firebase-messaging:20.2.1'
Step 3:
Add the following to your dependencies section in
project/build.gradle
file.
Groovy
classpath 'com.google.gms:google-services:4.3.4'
Step 4:
Pass Firebase tokens to WebEngage using
FirebaseMessagingService
.
Java
Kotlin
import com.google.firebase.messaging.FirebaseMessagingService;
import com.webengage.sdk.android.WebEngage;

public class MyFirebaseMessagingService extends FirebaseMessagingService {
 @Override
 public void onNewToken(String s) {
 super.onNewToken(s);
 WebEngage.get().setRegistrationID(s);
 }
}
import com.google.firebase.messaging.FirebaseMessagingService;
import com.webengage.sdk.android.WebEngage;

class MyFirebaseMessagingService : FirebaseMessagingService() {
 override fun onNewToken(s: String) {
 super.onNewToken(s)
 WebEngage.get().setRegistrationID(s)
 }
 
}
Highly Recommended!
Passing Firebase tokens to WebEngage from the
onCreate
method of your Application class ensures that changes in the user’s Firebase token are communicated to WebEngage. Here's how you can execute this.
Java
Kotlin
package your.application.package;

import com.google.android.gms.tasks.Task;
import com.google.firebase.messaging.FirebaseMessaging;
import com.google.android.gms.tasks.OnCompleteListener;
import androidx.annotation.NonNull;
import com.webengage.sdk.android.WebEngage;

public class MainApplication extends FlutterApplication {
 @Override
 public void onCreate() {
 super.onCreate();
 
 FirebaseMessaging.getInstance().getToken()
 .addOnCompleteListener(new OnCompleteListener<String>() {
 @Override
 public void onComplete(@NonNull Task<String> task) {
 if (!task.isSuccessful()) {
 Log.w(TAG, "Fetching FCM registration token failed", task.getException());
 return;
 }
 // Get new FCM registration token
 String token = task.getResult();
 WebEngage.get().setRegistrationID(token);
 }
 });
 }
}
package your.application.package;

import com.google.android.gms.tasks.Task;
import com.google.firebase.messaging.FirebaseMessaging;
import com.google.android.gms.tasks.OnCompleteListener;
import androidx.annotation.NonNull;
import com.webengage.sdk.android.WebEngage;

class MainApplication : FlutterApplication() {
 override fun onCreate() {
 super.onCreate()
 FirebaseMessaging.getInstance().token
 .addOnCompleteListener(OnCompleteListener { task ->
 if (!task.isSuccessful) {
 return@OnCompleteListener
 }
 // Get new FCM registration token
 val token: String = task.getResult()
 WebEngage.get().setRegistrationID(token)
 })
 }
}
Step 5:
Pass messages to WebEngage.
Create a class that extends
FirebaseMessagingService
and pass messages to WebEngage.
As shown below, all incoming messages from WebEngage will contain a key source with
webengage
as the corresponding value.
Java
Kotlin
package your.application.package;

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;
import com.webengage.sdk.android.WebEngage;

public class MyFirebaseMessagingService extends FirebaseMessagingService {
 @Override
 public void onMessageReceived(RemoteMessage remoteMessage) {
 Map<String, String> data = remoteMessage.getData();
 if(data != null) {
 if(data.containsKey("source") && "webengage".equals(data.get("source"))) {
 WebEngage.get().receive(data);
 }
 }
 }
}
package your.application.package;

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;
import com.webengage.sdk.android.WebEngage;

public class MyFirebaseMessagingService : FirebaseMessagingService() {

 override fun onMessageReceived(remoteMessage: RemoteMessage) {
 val data = remoteMessage.data
 if (data != null) {
 if (data.containsKey("source") && "webengage" == data["source"]) {
 WebEngage.get().receive(data)
 }
 }
 }
}
Step 6:
Register the service to the application element of your
AndroidManifest.xml
file as shown below.
XML
<service android:exported="false" 
 android:name=".MyFirebaseMessagingService">
 <intent-filter>
 <action android:name="com.google.firebase.MESSAGING_EVENT"/>
 </intent-filter>
</service>
Step 7.
Add your Firebase Credentials to WebEngage
Once all the above steps are completed, you can start sending Push notification!
Making your Flutter app compatible with Android 13 push changes
From Android 13 onwards, clients will have to explicitly ask permissions from end user to send push notifications. This means, client will NOT recieve push opted in as true once the app is installed by the end user, unless the user explicitly subscribes for same.
To make sure your app is compatible with Android 13 changes, kindly follow these steps:
Step 1. Kindly refer to official
Google documentation
to make your application compatible with the same.
Step 2. On the basis of the permission provided by the user, pass the status to WebEngage by following the code snippet below
dart
if (Platform.isAndroid) {
 WebEngagePlugin.setUserDevicePushOptIn(true/false);
}
🚧
Note
Pass the boolean value
true
or
false
depending on the permission the user has specified. If users denies the permission, they will not receive push alerts.
Push permission Prompt trigger to be managed by the App.
👍
And you're good to go!
For iOS
Follow our
native iOS Push Messaging Guide
to configure
Push Messaging
for your
iOS Flutter app.
Please feel free to drop in a few lines at
[email protected]
in case you have any queries or feedback. We're always just an email away!
Updated
7 months ago
Tracking Events
Copy Push to Notification Inbox - Flutter
Copy Page
