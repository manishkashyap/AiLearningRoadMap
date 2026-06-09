# Push Messaging

- URL: https://docs.webengage.com/docs/react-native-push-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
React Native
Push Messaging
Push Notifications are messages that pop up on mobile devices. App publishers can send them at any time; even if the recipients aren’t currently engaging with the app or using their devices.
🚧
Before continuing, please ensure that you have added
react-native-webengage
to your App.
Android
You can incorporate push messaging into your React Native application with react-native-webengage through two different methods.
React Native Approach
:
Approach-1
Native Approach
:
Approach-2
📘
If you're using multiple Firebase messaging providers, we suggest following
Approach 2
.
Approach 1: React Native Approach (Using Firebase Plugin)
Step 1: Integrating WebEngage with your React-Native Android App
📘
If you've already integrated @react-native-firebase/messaging, you can skip Step 1 and proceed directly to Step 2.
For optimal integration, we recommend utilising the
@react-native-firebase/messaging
library exclusively for Android platform. Implement methods with help of
React Native Firebase Messaging Docs
to facilitate seamless WebEngage integration with push notifications
Step 2: Integrating WebEngage with your React-Native Android App
Assuming you have integrated firebase using
@react-native-firebase/messaging
and implemented all the necessary methods outlined in the
React Native Firebase Messaging Docs
for Android, proceed to invoke our WebEngage methods within the Firebase callbacks as outlined below
2.1: Pass Push Token To WebEngage
In the
App.js
or
App.tsx
file, inside the
useEffect
block, obtain the FCM token using
messaging().getToken()
and pass it to WebEngage like this:
JavaScript
TypeScript
import WebEngage from 'react-native-webengage';
import messaging from '@react-native-firebase/messaging';
...
useEffect(() => {
 const webengage = new WebEngage();
 const registerDeviceAndSendToken = async () => {
 await messaging().registerDeviceForRemoteMessages();
 // Get Token From Firebase
 const token = await messaging().getToken();
 // Pass Token to WebEngage
 webengage.push.sendFcmToken(token); // Add This
 };

 registerDeviceAndSendToken();
}, []);
import messaging from '@react-native-firebase/messaging';
import WebEngage from 'react-native-webengage';
import WebEngagePlugin from 'react-native-webengage/types';

...
useEffect(() => {
 const webengage: WebEngagePlugin = new WebEngage();
 const registerDeviceAndSendToken = async () => {
 await messaging().registerDeviceForRemoteMessages();
 // Get Token From Firebase
 const token = await messaging().getToken();
 // Pass Token to WebEngage
 webengage.push.sendFcmToken(token); // Add This
 };

 registerDeviceAndSendToken();
}, []);
2.2: Add Firebase Dependency
To enable Firebase Cloud Messaging, add the dependency in your module’s
build.gradle
file, usually located at:
YourApp/android/app/build.gradle
Groovy
dependencies { 
 // Other Dependencies
 implementation 'com.google.firebase:firebase-messaging:22.0.0' // Add This
}
2.3: Additional step for passing Token to WebEngage from Native Android Code
Passing Firebase tokens to WebEngage from the
onCreate
method of your Application class ensures that changes in the user’s Firebase token are communicated to WebEngage. Here's how you can execute this.
Java
Kotlin
import com.google.android.gms.tasks.Task;
import com.google.firebase.messaging.FirebaseMessaging;
import com.google.android.gms.tasks.OnCompleteListener;
import androidx.annotation.NonNull;
import com.facebook.react.ReactApplication;
import com.webengage.sdk.android.WebEngage;
 
public class MainApplication extends Application implements ReactApplication {
    @Override
    public void onCreate() {
        super.onCreate();
    // WebEngage Initialization
 
 // Access Firebase Token
    FirebaseMessaging.getInstance().getToken()
      .addOnCompleteListener(new OnCompleteListener<String>() {
          @Override
          public void onComplete(@NonNull Task<String> task) {
 if (!task.isSuccessful()) {;
 return;
 }
            // Get new FCM registration token
            String token = task.getResult();
 // Pass FCM registration token to WebEngage
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
import com.facebook.react.ReactApplication;
 
class MainApplication : Application(), ReactApplication {
    fun onCreate() {
        super.onCreate()
        // WebEngage Initialization
 
 // Access Firebase Token
        FirebaseMessaging.getInstance().token
            .addOnCompleteListener(OnCompleteListener { task ->
                if (!task.isSuccessful) {
                    return@OnCompleteListener
                }
                // Get new FCM registration token
                val token: String = task.getResult()
 // Pass FCM registration token to WebEngage
                WebEngage.get().setRegistrationID(token) 
        })
    }
}
2.4: Pass push payload to WebEngage
To leverage the full capabilities of WebEngage's push notification rendering features, it is crucial to invoke the
onMessageReceived
method provided by the WebEngage SDK. This method should be called from the following Firebase methods:
onMessage
: Invoke the WebEngage's
onMessageReceived
method within this method to render foreground notifications with WebEngage layouts.
Update the
onMessage
handler within
App.js
or
App.tsx
JavaScript
TypeScript
import messaging from '@react-native-firebase/messaging'; 
import WebEngage from 'react-native-webengage';

function App() { 
 const webengage = new WebEngage(); 
 useEffect(() => { 
 ... 
 // onMessage Firebase Method is invoked when a notification is displayed on foreground
 const onMessageHandler = messaging().onMessage(async remoteMessage => { 
 ... 
 const webengage = new WebEngage();
 // Pass push payload to WebEngage
 webengage.push.onMessageReceived(remoteMessage); // Add This 
 }); 
 ... 
 return () => { 
 onMessageHandler(); 
 }; 
 }, []); 
 ... 
} 
export default App;
import messaging from '@react-native-firebase/messaging'; 
import WebEngage from 'react-native-webengage';
import WebEngagePlugin from 'react-native-webengage/types';

function App() { 
 const webengage: WebEngagePlugin = new WebEngage(); 
 useEffect(() => { 
 ... 
 // onMessage Firebase Method is invoked when a notification is displayed on foreground
 const onMessageHandler = messaging().onMessage(async remoteMessage => { 
 ... 
 const webengage: WebEngagePlugin = new WebEngage();
 // Pass push payload to WebEngage
 webengage.push.onMessageReceived(remoteMessage); // Add This 
 }); 
 ... 
 return () => { 
 onMessageHandler(); 
 }; 
 }, []); 
 ... 
} 
export default App;
setBackgroundMessageHandler
: Invoke the WebEngage's
onMessageReceived
method within this handler method to render background notifications with WebEngage layouts.
Update the
setBackgroundMessageHandler
within
index.js
JavaScript
import { AppRegistry } from 'react-native'; 
import messaging from '@react-native-firebase/messaging'; 
import WebEngage from 'react-native-webengage'; 
import App from './App';

// Register background handler for killed/Background state
messaging().setBackgroundMessageHandler(async (remoteMessage) => {
 ... 
 const webengage = new WebEngage();
 // Pass push payload to WebEngage
 webengage.push.onMessageReceived(remoteMessage); // Add This
});

AppRegistry.registerComponent('app', () => App);
By invoking the above WebEngage's mentioned methods, you ensure that WebEngage's advanced push notification rendering capabilities are utilised, enabling you to display rich and engaging push notifications to your users.
These modifications ensure that the WebEngage onReceive method is called when receiving messages both in the foreground and background. Make sure to handle any additional requirements specific to your application.
🚧
Android 13 Push Permission
Follow
Making your app compatible with Android 13 push changes
Approach 2: Native Approach
Step 1: Integration
Refer to the
Android Push Messaging Guide
for instructions on setting up Push Messaging for your React Native Android application
Step 2: Additional Step for using Multiple Push providers
📘
If you have integrated multiple push providers who are using Firebase Messaging Service in your app, you need to create a single
FirebaseMessagingService
class to handle the incoming payloads from all the providers.
Inside the
onMessageReceived
method, check the source of the incoming payload. If the source is WebEngage, pass the payload to the WebEngage SDK. Otherwise, handle the payload from the other provider(s).
Java
Kotlin
package your.application.package;

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;
import com.webengage.sdk.android.WebEngage;

public class MyFirebaseMessagingService extends FirebaseMessagingService {
 ...
 @Override
 public void onMessageReceived(RemoteMessage remoteMessage) {
 Map<String, String> data = remoteMessage.getData();
 // Check if the payload is from WebEngage
 if(data.containsKey("source") && "webengage".equals(data.get("source"))) {
 WebEngage.get().receive(data);
 } else {
 // Handle the payload from other providers
 // ...
 }
 }
}
package your.application.package;

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;
import com.webengage.sdk.android.WebEngage;

class MyFirebaseMessagingService : FirebaseMessagingService() {
 ...
 override fun onMessageReceived(remoteMessage: RemoteMessage) {
 val data = remoteMessage.data
 // Check if payload is recieved from WebEngage
 if (data.containsKey("source") && data["source"] == "webengage") {
 // Pass the payload to the WebEngage SDK
 WebEngage.get().receive(data)
 } else {
 // Handle the payload from other providers
 // ...
 }
 }
}
🚧
Android 13 Push Permission
Follow
Making your app compatible with Android 13 push changes
Making your app compatible with Android 13 push changes
From Android 13 onwards, clients will have to explicitly ask permissions from end user to send push notifications. This means, client will NOT receive push opted in as true once the app is installed by the end user, unless the user explicitly subscribes for same.
To make sure your app is compatible with Android 13 changes, kindly follow these steps:
Step 1. Kindly refer to
official Google documentation
to make your application compatible with the same.
Step 2. On the basis of the permission provided by the user, pass the status to WebEngage by following the code snippet below:
JavaScript
webengage.user.setDevicePushOptIn(true)
🚧
Note
Pass the boolean value
true
or
false
depending on the permission the user has specified. If users denies the permission, they will not receive push alerts.
Push permission Prompt trigger to be managed by the App.
And you're good to go!
iOS
Refer to the
iOS Push Messaging Guide
for instructions on setting up Push Messaging for your React Native iOS application.Please note that step 4 is handled separately through callbacks, which you can access
here
for React Native.
If you don't require Rich Push integration, simply follow steps 1 to 3.
Additional podfile configuration for Rich Push
If you've enabled Rich Push integration from iOS, proceed with the following mechanism.
🚧
Note
When using
use_frameworks!
in the main target of your Podfile, it automatically extends to all other targets, simplifying framework integration across your project. For instance, when integrating rich push, make sure to adhere to the following setup.
podfile
target 'YOURAPP' do
 config = use_native_modules!
 use_frameworks! :linkage => :static // If you have Added This
 // Your code
 end

# ServiceExtension Target
target 'NotificationService' do
 use_frameworks! :linkage => :static // Add This also
 pod 'WEServiceExtension'
end

# ContentExtension Target
target 'NotificationViewController' do
 use_frameworks! :linkage => :static // Add This also
 pod 'WEContentExtension'
end
Sample Application
For further instructions, refer to our
Sample Application
available on Github. Additionally, you can find the following crucial files within the application:
App.tsx
index.js
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
In-app messaging
Copy Page
