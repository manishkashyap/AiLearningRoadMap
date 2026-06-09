# Xiaomi Push Integration

- URL: https://docs.webengage.com/docs/xiaomi-push-integration
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
Push Messaging
Xiaomi Push Integration
❗️
Deprecated
Mi Push service outside Mainland China has been shut down by Xiaomi from 12:00 AM on April 2, 2024. Upon that time, you will no longer be able to use the Mi Push service.
Before getting started with Mi Push SDK integration, kindly make sure to:
Integrate Mi Push SDK v5.0.6 or above
Integrate WebEngage core Android SDK v.4.2.0 or above
Create Xiaomi Account
Kindly follow the below steps to create your Xiaomi account:
Step 1:
Register as a Xiaomi developer by logging onto the
Xiaomi Developer Account
.
Step 2:
Click on Create App and enter the required details.
Step 3:
After the App is created, click on the App Name to find the *Package Name and App Secret and configure the same on your dashboard by following the steps mentioned in
this
Integrating Xiaomi Push SDK in Android Studio Project
Step 1:
Login to your Xiaomi Account and download the
Xiaomi Android SDK
.
Step 2:
Integrate the latest
MiPush_SDK_Client
file into your Android Studio Project.
Step 3:
Add the following code inside the
AndroidManifest.xml
file
XML
<uses-permission android:name="android.permission.INTERNET" />
 <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
 <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
 <uses-permission android:name="android.permission.READ_PHONE_STATE" />
 <uses-permission android:name="android.permission.VIBRATE" /><!-- the following 2 yourpackage should be changed to your
 package name -->
 <permission
 android:name="yourpackage.permission.MIPUSH_RECEIVE"
 android:protectionLevel="signature" />

 <uses-permission android:name="yourpackage.permission.MIPUSH_RECEIVE" />
 <uses-permission android:name="android.permission.VIBRATE" />

 <service
 android:name="com.xiaomi.push.service.XMPushService"
 android:enabled="true"
 android:process=":pushservice" />
 <service
 android:name="com.xiaomi.push.service.XMJobService"
 android:enabled="true"
 android:exported="false"
 android:permission="android.permission.BIND_JOB_SERVICE"
 android:process=":pushservice" /><!--NoteThis service must be added to the version 3.0.1 or
 laterincluding version 3.0.1-->
 <service
 android:name="com.xiaomi.mipush.sdk.PushMessageHandler"
 android:enabled="true"
 android:exported="true" />
 <service
 android:name="com.xiaomi.mipush.sdk.MessageHandleService"
 android:enabled="true" /><!--Notethis service must be added to version 2.2.5 or later
 includes version 2.2.5-->
 <receiver
 android:name="com.xiaomi.push.service.receivers.NetworkStatusReceiver"
 android:exported="true">
 <intent-filter>
 <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
 <category android:name="android.intent.category.DEFAULT" />
 </intent-filter>
 </receiver>
 <receiver
 android:name="com.xiaomi.push.service.receivers.PingReceiver"
 android:exported="false"
 android:process=":pushservice">
 <intent-filter>
 <action android:name="com.xiaomi.push.PING_TIMER" />
 </intent-filter>
 </receiver>
Receive messages
Kindly implement a BroadcastReceiver inherited from
PushMessageReceiver
and implement all required methods in it:
onReceivePassThroughMessage
,
onCommandResult
, and then register your receiver in the
AndroidManifest.xml file
. Method
onReceivePassThroughMessage
is used to receive transparent messages sent by the server.
To pass the received push payload to WebEngage SDK, add the following code inside
onReceivePassThroughMessage
of your receiver class.
Java
Kotlin
@Override
 public void onReceivePassThroughMessage(Context context, MiPushMessage miPushMessage) {
 super.onReceivePassThroughMessage(context, miPushMessage);
 String content = miPushMessage.getContent();
 WebEngage.get().receive(PushUtils.prepareMap(content));
 }
override fun onReceivePassThroughMessage(context: Context?, miPushMessage: MiPushMessage) {
 super.onReceivePassThroughMessage(context, miPushMessage)
 val content = miPushMessage.content
 WebEngage.get().receive(PushUtils.prepareMap(content))
 }
Pass the Push Token and Region to WebEngage
Kindly add the following code inside the
MIPushReceiver onCommandResult
method.
Java
Kotlin
@Override
 public void onCommandResult(Context context, MiPushCommandMessage message) {
 super.onCommandResult(context, message);
 String command = message.getCommand();
 List<String> arguments = message.getCommandArguments();
 String cmdArg1 = ((arguments != null && arguments.size() > 0) ? arguments.get(0) : null);
 String cmdArg2 = ((arguments != null && arguments.size() > 1) ? arguments.get(1) : null);
 if (MiPushClient.COMMAND_REGISTER.equals(command)) {
 if (message.getResultCode() == ErrorCode.SUCCESS) {
 String region = MiPushClient.getAppRegion(context);
 WebEngage.get().setXiaomiRegistrationID(MiPushClient.getRegId(context), region);
 }
 }
 }
override fun onCommandResult(context: Context?, message: MiPushCommandMessage) {
 super.onCommandResult(context, message)
 val command = message.command
 val arguments = message.commandArguments
 val cmdArg1 = if (arguments != null && arguments.size > 0) arguments[0] else null
 val cmdArg2 = if (arguments != null && arguments.size > 1) arguments[1] else null
 if (MiPushClient.COMMAND_REGISTER == command) {
 if (message.resultCode == ErrorCode.SUCCESS) {
 val region = MiPushClient.getAppRegion(context)
 WebEngage.get().setXiaomiRegistrationID(MiPushClient.getRegId(context), region)
 }
 }
 }
Example of BroadcastReceiver: MIPushReceiver
Java
Kotlin
public class MIPushReceiver extends PushMessageReceiver {
 @Override
 public void onReceivePassThroughMessage(Context context, MiPushMessage miPushMessage) {
 super.onReceivePassThroughMessage(context, miPushMessage);
 String content = miPushMessage.getContent();
 WebEngage.get().receive(PushUtils.prepareMap(content));
 }

 @Override
 public void onCommandResult(Context context, MiPushCommandMessage message) {
 super.onCommandResult(context, message);
 String command = message.getCommand();
 List<String> arguments = message.getCommandArguments();
 String cmdArg1 = ((arguments != null && arguments.size() > 0) ? arguments.get(0) : null);
 String cmdArg2 = ((arguments != null && arguments.size() > 1) ? arguments.get(1) : null);
 if (MiPushClient.COMMAND_REGISTER.equals(command)) {
 if (message.getResultCode() == ErrorCode.SUCCESS) {
 String region = MiPushClient.getAppRegion(context);
 WebEngage.get().setXiaomiRegistrationID(MiPushClient.getRegId(context), region);
 }
 }
 }

}
class MIPushReceiver : PushMessageReceiver() {
 override fun onReceivePassThroughMessage(context: Context?, miPushMessage: MiPushMessage) {
 super.onReceivePassThroughMessage(context, miPushMessage)
 val content = miPushMessage.content
 WebEngage.get().receive(PushUtils.prepareMap(content))
 }

 override fun onCommandResult(context: Context?, message: MiPushCommandMessage) {
 super.onCommandResult(context, message)
 val command = message.command
 val arguments = message.commandArguments
 val cmdArg1 = if (arguments != null && arguments.size > 0) arguments[0] else null
 val cmdArg2 = if (arguments != null && arguments.size > 1) arguments[1] else null
 if (MiPushClient.COMMAND_REGISTER == command) {
 if (message.resultCode == ErrorCode.SUCCESS) {
 val region = MiPushClient.getAppRegion(context)
 WebEngage.get().setXiaomiRegistrationID(MiPushClient.getRegId(context), region)
 }
 }
 }
}
In the application file, add the following code to initialize MI Code.
Please Note:
For few devices, we have found that MI SDK throws an error asking the app to register a region first for MI SDK. During our testing, we have found that this region set does not decide the token region.
However, to avoid the error, we suggest you to set the default region to either Global or India based on your app geography.
Java
MiPushClient.setRegion(Region.Global); //Set default region to Global or India

//Register for MI Push
MiPushClient.registerPush(this, Constants.MI_APP_ID, Constants.MI_APP_KEY);
Updated
7 months ago
Push Messaging
Huawei Push Integration
Copy Page
