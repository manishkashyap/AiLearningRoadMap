# Advanced

- URL: https://docs.webengage.com/docs/react-native-advanced
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
React Native
Advanced
Linking WebEngage React Native library manually
Android
Include the WebEngage React Native directory in your Android project. To do this, add the below snippet in
android/settings.gradle
file.
JavaScript
include ':react-native-webengage'
project(':react-native-webengage').projectDir = new File(settingsDir, '../node_modules/react-native-webengage/android')
Add React Native dependency in
android/app/build.gradle
file.
Java
dependencies {
 ...
 compile project(':react-native-webengage')
}
Create a new object of WebEngage package in
android/app/src/main/java/[your/package]/MainApplication.java
file.
Java
import com.webengage.WebengagePackage;

...
...

@Override
protected List<ReactPackage> getPackages() {
 return Arrays.<ReactPackage>asList(
 ... ,
 new WebengagePackage()
 );
}
iOS
Open your iOS folder in Xcode.
Drag and drop
node_modules/react-native-webengage/ios/RNWebengage.xcodeproj
into the Libraries folder of your project in Xcode. Check Step 1
here
for detailed instructions.
Drag and drop the
libRNWebengage.a
product in
RNWebengage.xcodeproj
into your project's target's
Link Binary With Libraries
section. Check Step 2
here
for detailed instructions.
Under Build Settings, add a
Header Search Path
pointing to
$(SRCROOT)/../node_modules/react-native-webengage/ios
. Check Step 3
here
for detailed instructions.
Updated
7 months ago
Callbacks
Troubleshooting
Copy Page
