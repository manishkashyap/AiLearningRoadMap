# React Native

- URL: https://docs.webengage.com/docs/react-native
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
React Native
React Native
lets you build mobile apps using only JavaScript. It uses the same design as React, letting you compose a rich mobile UI from declarative components.
Here's how you can integrate the WebEngage SDK with your react native apps:
1. Install WebEngage React Native Library
Use the below command in your project directory to install WebEngage React Native library.
npm
yarn
npm install react-native-webengage --save
yarn add react-native-webengage
2. Install Android SDK
Step 2.1:
For setting up your Android application, refer to the
Initialization
instructions to utilize the Android SDK. You can bypass Step 1 - Installation and proceed directly to Step 2.
⚠️
Ensure that you finish the
Android Integration
steps before proceeding with the step below.
Step 2.2:
After completion of Android Integration proceed with the following step
Java
Kotlin
import com.webengage.WebengageBridge;

@Override
public void onCreate() {
 super.onCreate();
 WebengageBridge.getInstance(); // Add This
 //...WebEngage initialization
 WebEngageConfig webEngageConfig = new WebEngageConfig.Builder()
 .setWebEngageKey(YOUR_WEBENGAGE_LICENSE_CODE)
 .setDebugMode(true) // only in development mode
 .build();
 registerActivityLifecycleCallbacks(new WebEngageActivityLifeCycleCallbacks(this, webEngageConfig));
}
import com.webengage.WebengageBridge;

override fun onCreate() {
 super.onCreate()
 WebengageBridge.getInstance(); // Add This
 // ... Webengage Initialization
 val webEngageConfig = WebEngageConfig.Builder()
 .setWebEngageKey(YOUR_WEBENGAGE_LICENSE_CODE)
 .setDebugMode(true) // only in development mode
 .build()
 registerActivityLifecycleCallbacks(
 WebEngageActivityLifeCycleCallbacks(
 this,
 webEngageConfig
 )
 )
}
Attribution Tracking (Only Android)
Add the following
Google Install referrer
library in your
app/build.gradle
file (ensure that the SDK version being used is >= 3.16.0):
Groovy
dependencies {
 implementation 'com.android.installreferrer:installreferrer:2.2'
}
🚧
Please Note
App Installed
event and
First Acquisition Details
data in user profile will not be tracked on your Android app unless you follow the above step.
3. Install iOS SDK
When constructing your iOS application, proceed with the
iOS Integration
instructions to install the iOS SDK. Skip the "Step 1 - Install the SDK" section and begin directly with "Step 2 - Initialise SDK" in the
iOS documentation
.
4 . Setting Up the SDK in React-Native
Grab a reference to the WebEngage React Native library in your JavaScript file.
ℹ️
We advise utilizing this code within your application's App.js or App.tsx file
JavaScript
TypeScript
import WebEngage from 'react-native-webengage';
var webengage = new WebEngage();
import WebEngage from 'react-native-webengage';
import WebEngagePlugin from 'react-native-webengage/types';

var webengage: WebEngagePlugin = new WebEngage();
✅
Congratulations!
You have successfully integrated WebEngage with your React Native apps and are sending user session data to WebEngage. Please note that it may take up to a few minutes for data to reflect in your dashboard
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
about 2 months ago
So, what's next?
We recommend that you implement the following integrations with your app before releasing it with WebEngage for the first time:
Track User Properties as User Attributes
Track User Actions as Events
Configure Push Messaging
Configure In-app Messaging
Copy Page
