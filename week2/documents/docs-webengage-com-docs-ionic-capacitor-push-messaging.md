# Push Messaging

- URL: https://docs.webengage.com/docs/ionic-capacitor-push-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Ionic Capacitor
Push Messaging
Android
There are two approaches to integrate WebEngage with Capacitor for Android FCM (Firebase Cloud Messaging) notifications:
Using WebEngage’s library:
This approach is recommended for projects that have not yet integrated Capacitor’s Push Notification plugin. It involves installing the WebEngage plugin, configuring the project settings, and updating the FCM token.
Using Capacitor’s Push Notification:
This approach is for projects that have already integrated Capacitor’s Push Notification plugin. It involves creating custom classes to handle FCM token registration and message reception, and registering these classes in the project configuration.
🚧
Note
Check your package.json for "@capacitor/push-notifications" dependency
If you have other push notification providers integrated, please follow
Approach 2
.
Approach 1: Using WebEngage’s library
Install Plugin
: Install the plugin as a local npm module by running:
Bash
npm install we-cap-android-fcm
Import Plugin:
JavaScript
import { WEAndroidFCM } from 'we-cap-android-fcm';
Update Token
: Add the following code snippet to execute when the App launches:
JavaScript
WEAndroidFCM.updateToken();
Update
build.gradle
: Add the following line inside the project-level
build.gradle
(Project android/build.gradle)
:
Groovy
classpath 'com.google.gms:google-services:4.4.2'
Add
google-services.json
: Place the
google-services.json
file inside the app directory of your project (Project
android/app
).
📘
Android 13 Push Permission
Refer to the “
Making Your App Compatible with Android 13 Push Changes
” section for guidance on supporting Android 13 and later devices.
Approach 2: Using Capacitor’s Push Notification Library
Create
MainApplication.java
: Create a file
MainApplication.java
inside your android platform folder:
.../android/app/src/main/java/<package-directory>
.
Add the following code to enable sending FCM tokens to WebEngage:
Java
import android.app.Application;
import androidx.annotation.NonNull;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.messaging.FirebaseMessaging;
import com.webengage.sdk.android.WebEngage;

public class MainApplication extends Application {
 @Override
 public void onCreate() {
 super.onCreate();
 FirebaseMessaging.getInstance().getToken().addOnCompleteListener(new OnCompleteListener<String>() {
 @Override
 public void onComplete(@NonNull Task<String> task) {
 try {
 String token = task.getResult();
 // Pass FCM Token to WebEngage
 WebEngage.get().setRegistrationID(token);
 } catch (Exception e) {
 e.printStackTrace();
 }
 }
 });
 }
}
Register
MainApplication
in
AndroidManifest.xml
: Add the
name
attribute in the
application
tag:
XML
<application
 android:name=".MainApplication"
 ...
Create
MyMessagingService.java
: Create a new class
MyMessagingService
extending
com.capacitorjs.plugins.pushnotifications.MessagingService
:
Java
import android.util.Log;
import androidx.annotation.NonNull;
import com.capacitorjs.plugins.pushnotifications.MessagingService;
import com.google.firebase.messaging.RemoteMessage;
import com.webengage.sdk.android.WebEngage;
import java.util.Map;

public class MyMessagingService extends MessagingService {
 private static final String TAG = "custom-fcm-service";

 static boolean includesWebEngage() {
 try {
 Class.forName("com.webengage.sdk.android.WebEngage");
 return true;
 } catch (ClassNotFoundException e) {
 Log.e(TAG, "WebEngage Not Found", e);
 } catch (Throwable t) {
 Log.e(TAG, "Error while checking for WebEngage", t);
 }
 return false;
 }

 @Override
 public void onMessageReceived(@NonNull RemoteMessage remoteMessage) {
 super.onMessageReceived(remoteMessage);
 Map<String, String> data = remoteMessage.getData();
 if (data != null && includesWebEngage()) {
 WebEngage.engage(getApplicationContext());
 if ("webengage".equals(data.get("source"))) {
 WebEngage.get().receive(data);
 }
 }
 }

 @Override
 public void onNewToken(@NonNull String s) {
 super.onNewToken(s);
 if (includesWebEngage()) {
 WebEngage.get().setRegistrationID(s);
 }
 }
}
Register the Service in
AndroidManifest.xm
l: Add the following lines inside the
Application
tag:
XML
<service android:name=".MyMessagingService"
 android:exported="false">
 <intent-filter>
 <action android:name="com.google.firebase.MESSAGING_EVENT" />
 </intent-filter>
</service>
Making your app compatible with Android 13 push changes
From Android 13 onwards, clients will have to explicitly ask permissions from end user to send push notifications. This means, client will NOT recieve push opted in as true once the app is installed by the end user, unless the user explicitly subscribes for same.
To make sure your app is compatible with Android 13 changes, kindly follow these steps:
Step 1
: Kindly refer to official
Google documentation
to make your application compatible with the same.
Step 2:
Choose how you want to handle the push permission request in your application:
If you choose to manage the push permission request using native Android code:
You can use the following Java code to pass the permission status to WebEngage.
JavaScript
WebEngage.get().user().setDevicePushOptIn(true);
If you choose to use the Capacitor approach (e.g., Capacitor Push Notification plugin):
Use the following JavaScript code to pass the permission status to WebEngage.
JavaScript
webengage.user.setDevicePushOptIn(true);
🚧
Note
Pass the boolean value
true
or
false
depending on the permission the user has specified. If the user denies the permission, they will not receive push notifications.
The push permission prompt trigger should be managed by the app, either through the native Android approach or the Capacitor approach, depending on your implementation.
iOS
Refer to the
iOS Push Messaging Guide
for instructions on setting up Push Messaging for your Capacitor iOS application.Please note that step 4 is handled separately through callbacks, which you can access in the capacity callbacks section.
👍
Push Integration Success
Your Capacitor application is now integrated with push messaging. You can now send push notifications from the WebEngage Dashboard.
Sample Application
For further instructions, refer to our
Sample Application
available on Github.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Tracking Events
In-App Messaging
Copy Page
