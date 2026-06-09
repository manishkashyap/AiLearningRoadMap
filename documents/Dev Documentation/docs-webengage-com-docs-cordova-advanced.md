# Advanced

- URL: https://docs.webengage.com/docs/cordova-advanced
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Cordova
Advanced
Other configurations
All configurations go under the
config.xml
file in the root directory of your project.
Location tracking
Android
If you want to track your users' location, add the below snippet in your
config.xml
file.
XML
<widget ... >
 ...
 <!-- For Android -->
 <platform name="android">
 <config-file parent="/manifest/application" target="AndroidManifest.xml">
 ...
 <meta-data android:name="com.webengage.sdk.android.location_tracking" android:value="true" />
 </config-file>
 <config-file parent="/manifest" target="AndroidManifest.xml">
 ...
 <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
 </config-file>
 </platform>

</widget>
iOS
If you want to track your users' location, add the below snippet in your
config.xml
file.
XML
<widget ... >
 ...

 <!-- For iOS -->
 <platform name="ios">
 ...
 <config-file parent="UIBackgroundModes" target="*Info.plist">
 <array>
 <string>location</string>
 </array>
 </config-file>
 </platform>

</widget>
Upgrade plugin from 1.0.0 to 1.0.1
If you are using
Integration through Cocoapods
and if you face the below error
Remove "WebEngage.framework" from the Embedded frameworks list.
Updated
7 months ago
Callbacks
React Native
Copy Page
