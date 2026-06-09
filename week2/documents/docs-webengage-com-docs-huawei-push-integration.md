# Huawei Push Integration

- URL: https://docs.webengage.com/docs/huawei-push-integration
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
Push Messaging
Huawei Push Integration
Steps to integrate Push services in your app
You can start sending Push Notifications to your Huawei Mobile users by following the below steps:
Create Huawei Account
Kindly follow the below steps to create your Huawei account:
Step 1:
Register as a Huawei developer by logging onto the
Huawei Website
.
Step 2:
Configure App in App Gallery Connect
.
Step 3:
Create a
project
and
add your application
on the
Huawei AppGallery Connect Website
.
Click to enlarge
Enable Push Kit
Push Kit
is a service that allows you to send messages to the apps on a user's device through the cloud-to-device channel.
Kindly follow the below steps to enable the
Push Kit
for Huawei devices:
Step 1:
Go to
Project settings > Manage APIs
and enable Push Kit.
Click to enlarge
Step 2:
Go to
Grow > Push Kit
and click
Enable Now
. In the dialog box that is displayed, click
OK
.
Click to enlarge
Step 3:
Go to
My Projects > Your Project > App Information
. Get the
App ID
and the
App Secret
of the app you have created and add the details while configuring
Huawei Messaging Service
in your WebEngage dashboard in JSON format.
Click to enlarge
Learn more
about Huawei Push Kit.
HMS SDK Integration
HMS is a lightweight IDE tool plugin that helps in integrating HMS Core API with a lower cost and higher efficiency.
Step 1:
Refer to Huawei checklist for
integration preparation
.
Step 2:
Go to
My Projects > Your Project > App Information
and download the
agconnect-services.json
file. Move the downloaded
agconnect-services.json
file to the app directory of your Android Studio project.
Click to enlarge
Configure the Manifest and Gradle files with the HMS plugin.
Modify the root-level
build.gradle
file.
Groovy
buildscript {
 repositories {
 // Configure the Maven repository address for the HMS Core SDK.
 maven {url 'http://developer.huawei.com/repo/'}
 
 }
 dependencies {
 classpath "com.android.tools.build:gradle:4.0.1"
 
 // Add the AppGallery Connect plugin configuration.
 classpath 'com.huawei.agconnect:agcp:1.6.0.300'
 }
}

allprojects {
 repositories {
 // Configure the Maven repository address for the HMS Core SDK.
 maven {url 'http://developer.huawei.com/repo/'}
 
 }
}
In Gradle 7.0 or later, configuration under
allprojects > repositories
is migrated to the project-level
settings.gradle
file.
The following is a configuration example of the settings.gradle file:
Groovy
dependencyResolutionManagement {
 ...
 repositories {
 google()
 jcenter() 
 maven {url 'https://developer.huawei.com/repo/'}
 }
}
Add the build dependencies
Open the app-level
build.gradle
file of your project and add a build dependency in the
dependencies
block.
Refer to HMS push kit version history for the
latest version
of the dependency.
Groovy
dependencies {
 //Add this for adding build depencdency for the HMS push kit.
 implementation 'com.huawei.hms:push:6.1.0.300'
}

apply plugin: 'com.huawei.agconnect'//Add This at the bottom of the file
Configure the signing certificate
Copy the signing certificate generated in Integration Preparations to the
app
directory of your project and configure the signature in the
build.gradle
file used while creating the project and app in the HMS console.
Groovy
android { 
 signingConfigs { 
 config { 
 // Replace xxx with your signing certificate. 
 keyAlias 'xxx' 
 keyPassword 'xxxx' 
 storeFile file('xxx.jks') 
 storePassword 'xxxx' 
 } 
 } 
 
 buildTypes { 
 debug { 
 signingConfig signingConfigs.config 
 } 
 release { 
 signingConfig signingConfigs.config 
 minifyEnabled false 
 proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro' 
 } 
 } 
 }
Implement Service class that extends the HmsMessageService class
In order to receive messages, you must implement a Service inherited from HmsMessageService and override all required methods in it :
onNewToken
,
onMessageReceived
and then register your Service in the
AndroidManifest.xml
file. Method
onMessageReceived
is used to receive messages sent by WebEngage.
Java
public class DemoHmsMessageService extends HmsMessageService {
 @Override
 public void onNewToken(String s, Bundle bundle) {
 super.onNewToken(s, bundle);
 MyLogger.d("DemoHmsMessageService -> New Token Received with bundle " +s);
 //log to WebEngage
 if(!TextUtils.isEmpty(s))
 WebEngage.get().setHuaweiRegistrationID(s);
 }

 @Override
 public void onNewToken(String s) {
 super.onNewToken(s);
 MyLogger.d("DemoHmsMessageService -> New Token Received" +s);
 //Log to WebEngage SDK
 if(!TextUtils.isEmpty(s))
 WebEngage.get().setHuaweiRegistrationID(s);
 }

 @Override
 public void onMessageReceived(RemoteMessage remoteMessage) {
 // super.onMessageReceived(remoteMessage);
 MyLogger.d("DemoHmsMessageService -> New Message Received "+remoteMessage.getDataOfMap());
 //Send to webengage sdk
 if(remoteMessage.getData() != null )
 WebEngage.get().receive(remoteMessage.getDataOfMap());
 }
}
In
Android 11
, the way for an app to query other apps on the user device and interact with them has been changed. If
targetSdkVersion
is
30
or later for your app, add the
queries
element in the
manifest
element in
AndroidManifest.xml
to allow your app to access HMS Core (APK).
Groovy
<manifest ...> 
 ... 
 <application ...> 
 <service android:name=".DemoHmsMessageService" android:exported="false"> 
 <intent-filter> 
 <action android:name="com.huawei.push.action.MESSAGING_EVENT"/> 
 </intent-filter> 
 </service> 
 </application> 
 ... 
 <queries> 
 <intent> 
 <action android:name="com.huawei.hms.core.aidlservice" /> 
 </intent> 
 </queries> 
 ... 
</manifest>
Sending the token to WebEngage SDK
In the application class of your app, create a new thread to obtain the token from the HMS instance and pass this token to the WebEngage SDK using
WebEngage.get().setHuaweiRegistrationID(token)
Java
private void getHMSToken() {
 MyLogger.d("Fetching HMS Token");

 // Create a thread.
 new Thread() {
 @Override
 public void run() {
 try {
 // Obtain the app ID from the agconnect-service.json file.
 String appId = Constants.HMS_APP_ID;

 // Set tokenScope to HCM.
 String tokenScope = "HCM";
 String token = HmsInstanceId.getInstance(MyApplication.getAppContext()).getToken(appId, tokenScope);
 MyLogger.d("HMS token received "+token);

 // Check whether the token is empty.
 if(!TextUtils.isEmpty(token)) {
 sendHMSRegTokenToServer(token);
 }
 } catch (ApiException e) {
 // MyLogger.e(WebEngageConstant.TAG, "HMS Token failed, " + e);
 }
 }
 }.start();
}

private void sendHMSRegTokenToServer(String token) {
 MyLogger.d("sending HMS Token to server. token:" + token);
 WebEngage.get().setHuaweiRegistrationID(token);
 //Send to WebEngage SDK
}
Configure Huawei Push creds on Dashboard
Kindly follow the steps mentioned in
this
doc to configure the Huawei creds on your Dashboard.
👍
Congratulations!
You can now successfully send push notifications using Huawei push service.
Updated
7 months ago
Xiaomi Push Integration
Copy Push to Notification Inbox - Android
Copy Page
