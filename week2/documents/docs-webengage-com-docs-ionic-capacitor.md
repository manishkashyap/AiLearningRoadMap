# Ionic Capacitor

- URL: https://docs.webengage.com/docs/ionic-capacitor
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Ionic Capacitor
Ionic Capacitor
is an open-source native runtime for building Web Native apps. Create cross-platform iOS, Android, and Progressive Web Apps with JavaScript, HTML, and CSS.
Step 1: Install WebEngage Plugin
Use the below command to install WebEngage plugin for both Android and iOS platforms.
Bash
npm install cordova-plugin-webengage
npm install @awesome-cordova-plugins/webengage
Step 2: Initialize WebEngage
To initialize WebEngage, add the following code snippet to your project based on the framework you are using. This will ensure WebEngage runs immediately when the app launches.
For Angular:
Add the following to
src/app/app.component.ts
TypeScript
import { Platform } from '@ionic/angular';
import { Webengage } from '@awesome-cordova-plugins/webengage';
constructor(private platform: Platform) {
 this.platform.ready().then(() => {
 Webengage.engage(); // Add This
 // Your Code
 });
}
For React:
Add the following to
App.ts
For a working example, check out the
Sample React App
on GitHub
TypeScript
import React, { useEffect } from 'react';
import { Webengage } from '@awesome-cordova-plugins/webengage';
const App = () => {
 useEffect(() => {
 Webengage.engage(); // Add This
 // Your code
 }, []);
 return (
 // Your app components
 );
};
export default App;
For Vue:
Add the following to
src/main.ts
:
For a working example, check out the
Sample Vue App
on GitHub
TypeScript
import { createApp } from 'vue';
import App from './App.vue';
import { Webengage } from '@awesome-cordova-plugins/webengage';
const app = createApp(App);
document.addEventListener("deviceready", () => {
 Webengage.engage(); // Add This
 // Your code
});
app.mount('#app');
Step 3: Configure the iOS Project
3.1: Generate the iOS directory:
Bash
npm run build # Compiles web assets for your application.
npx cap copy ios #Copies web assets into your iOS project.
npx cap sync ios #Syncs changes from your web app into your iOS project.
npx cap update ios #Updates Capacitor and plugins in your iOS project.
npx cap open ios #Opens your iOS project in Xcode for further development and deployment tasks.
3.2: Modify Info.plist:
Follow the quick guide
here
and add the required properties to the
Info.plist
file of your project
Here is an example of an
Info.plist
configuration for reference.
info.plist
<key>WEGLogLevel</key>
<string>VERBOSE</string> <!-- or DEFAULT -->
<key>WEGEnvironment</key>
<string>IN</string> <!-- or DEFAULT -->
<key>WEGLicenseCode</key>
<string>YOUR-LICENSE-CODE</string>
Step 4: Configure Android Project
4.1: Generate the Android directory
Bash
npm run build # Compiles the web assets of your application.
npx cap sync android # Syncs changes specifically into your native Android project.
npx cap copy android # Copies web assets into your native Android project.
npx cap open android # Opens your native Android project in Android Studio for further development and deployment tasks.
4.2: Modify
AndroidManifest.xml
Add the following lines inside the
<application>
tag in your Android project's
AndroidManifest.xml.
Make sure to replace YOUR_WEBENGAGE_LICENSE_CODE with your actual WebEngage license code, available under the Account Setup section of your dashboard. Depending on your data center location, set
ENVIRONMENT_VALUE
to either "us" or “in” or "ksa".
XML
<meta-data android:name="com.webengage.sdk.android.key" android:value="YOUR_WEBENGAGE_LICENSE_CODE" />
<meta-data android:name="com.webengage.sdk.android.debug" android:value="true" />
<meta-data android:name="com.webengage.sdk.android.environment" android:value="ENVIRONMENT_VALUE" />
Step 5: Additional Features
Attribution Tracking (Android only)
Follow the WebEngage
documentation
for enabling attribution tracking.
Google Advertisement ID Changes (Android 13+)
Follow the WebEngage
documentation
to understand and enable advertisement ID tracking. Ignore the section on "Tracking Advertising ID for selected users" from the provided link, and instead, follow the steps outlined below.
Tracking Advertising ID for selected users for GAID
WebEngage tracks the advertising ID for all users by default. To track the advertising ID for specific users, follow the steps below.
In the
onDeviceReady
method, set
autoGAIDTracking
to true by passing the following arguments to
webengage.engage()
:
JavaScript
Webengage.engage({ android: { autoGAIDTracking: true } });
Enable advertisement ID tracking for any user with this code:
JavaScript
Webengage.startGAIDTracking();
👍
Congratulations!
You have successfully integrated WebEngage with your Capacitor app and are sending user session data to WebEngage. Please note that it may take up to a few minutes for data to reflect in your dashboard.
Sample Application
For further instructions, refer to our
Sample Application
available on Github.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Unity Callbacks
Tracking Users
Copy Page
