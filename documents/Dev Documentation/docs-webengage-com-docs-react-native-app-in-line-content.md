# App In-line Content

- URL: https://docs.webengage.com/docs/react-native-app-in-line-content
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
React Native
App In-line Content
📘
Supported from React Native SDK v1.3.0
App In-line Content allows you to insert content directly into your app's screen without disturbing the user experience. It also allows you to dynamically update your app's content and run relevant and contextual campaigns.
You may use the In-line content to change areas of your app or show banner ads based on live triggers and segmentation.
This capability is provided in WebEngage Personalization SDK, a child SDK that handles Inline campaigns.
Installation
Step 1:
Integrate the WebEngage SDK by following the steps mentioned in
this
doc.
Step 2:
Install the
react-native-we-personalization
library in your project using either npm or yarn:
Shell
npm i react-native-we-personalization --save
Or
Shell
yarn add react-native-we-personalization
Link Dependency
Use this command to automatically link the WebEngage dependency to your project.
Shell
react-native link react-native-we-personalization
🚧
You can manually link the library by following these steps.
Linking WebEngage React Native library manually
Android
Include the WebEngage React Native directory in your Android project. To do this, add the below snippet in
android/settings.gradle
file.
JavaScript
include ':react-native-we-personalization'
project(':react-native-we-personalization').projectDir = new File(settingsDir, '../node_modules/react-native-we-personalization/android d
Add React Native dependency in
android/app/build.gradle
file.
gradle
dependencies { 
 ... 
 implementation project(':react-native-we-personalization') 
}
Create a new object of WebEngage package in
android/app/src/main/java/[your/package]/MainApplication.java
file.
Java
import com.webengagepersonalization.WEPersonalizationPackage;

 ...
 ...

@Override
protected List<ReactPackage> getPackages() {
 return Arrays.<ReactPackage>asList(
 ... ,
 new WEPersonalizationPackage()
 );
}
iOS
Open your iOS folder in Xcode.
Drag and drop
node_modules/react-native-we-personalization/ios/WePersonalization.xcodeproj
into the Libraries folder of your project in Xcode. Check Step 1
here
for detailed instructions.
Drag and drop the
libWePersonalization.a
product in
WePersonalization.xcodeproj
into your project's target's
Link Binary With Libraries
section. Check Step 2
here
for detailed instructions.
Under Build Settings, add a
Header Search Path
pointing to
$(SRCROOT)/../node_modules/react-native-we-personalization/ios
. Check Step 3
here
for detailed instructions.
Screen Tracking
Screen tracking is crucial for ensuring the proper functioning of App-Inline, as the inline views are dependent on the screen name.
webengage.screen
accepts two parameters: Screen Name (
String
) and Screen Data (
Object
). You can call
webengage.screen
with either both screen name and screen data as parameters or only the screen name.
dart
import WebEngage from 'react-native-webengage'; 
var webengage = new WebEngage(); 
... 
webengage.screen("Purchase Screen", { 
 "productId": "~hs7674", 
 "price" : 1200 
});
❗️
Mandatory step
Before adding the
WEInlineWidget
widget to screens, please follow the
Screen Tracking
documentation.
Step 4:
To display the app-inline content, add the
WEInlineWidget
component to the desired location in your application
dart
import { WEInlineWidget } from 'react-native-we-personalization';
...

 <WEInlineWidget
 style={styles.inlineStyle}
 screenName={screenName}
 androidPropertyId={androidPropertyId}
 iosPropertyId={iosPropertyId}
 onRendered={onRenderedCallback}
 onDataReceived={onDataReceivedCallback}
 onPlaceholderException={onPlaceholderExceptionCallback}
 />
The above code snippet demonstrates the usage of the
WEInlineWidget
component to display a view within your app. The following props are used:
Key
Type
Definition
style
Style Object
Defines the styling for the inline view.
screenName
String
Refers to the current screen name of the view
androidPropertyId
String
Refers to the unique ID of the inline view, which corresponds to a property in the WebEngage dashboard for Android. This ID should be unique for each screen.
iosPropertyId
Integer
Refers to the unique ID of the inline view, which corresponds to a property in the WebEngage dashboard for iOS. This ID should be unique for each screen.
onDataReceived
Callback
This callback is triggered when the rule is passed before rendering the UI.
onRendered
Callback
This callback is triggered immediately after the UI is rendered.
onPlaceholderException
Callback
This callback is triggered in case of any exception that occurs while fulfilling the campaign.
Callbacks
WECampaignCallback: Campaign callbacks
Register
Callbacks can be registered globally in the App.js class or locally in the individual screens. This will be triggered throughout the component’s lifecycle.
Add below snippet in your code:
dart
import { registerWEPlaceholderCallback } from 'react-native-we-personalization';
...

React.useEffect(() => {
 const WECampaignCallback = {
 onCampaignPrepared,
 onCampaignShown,
 onCampaignClicked,
 onCampaignException,
 };
 registerWECampaignCallback(WECampaignCallback);
}, []);
We create an object named
WECampaignCallback
with four callback methods, namely
onCampaignPrepared
,
onCampaignShown
,
onCampaignClicked
, and
onCampaignException
.
These callbacks are passed to the
registerWECampaignCallback()
method, which will be registered for the
WECampaigns
.
Params
Type
Definition
onCampaignPrepared
Callback
Triggered when data for the qualified campaign is retrieved from the WebEngage servers
onCampaignShown
Callback
When the SDK displays the Campaign on the screen, this callback is triggered. This will only be triggered for
Banner
and
Text
templates, not
Custom
templates.
onCampaignClicked
Callback
Triggered when clicked on the campaign view that is rendered by the SDK. This will only be triggered for
Banner
and
Text
templates, not
Custom
templates.
onCampaignException
Callback
This callback will get triggered when the campaign retrieval/showing will get failed.
By using these callbacks, you can effectively handle and manage the WECampaigns in your React application.
🚧
Please Note
Callbacks will be available unless the component is unmounted and is deregistered from the campaign callbacks.
De-register
To ensure proper cleanup, you should always call
deregisterWECampaignCallback
() when the component is being unmounted. This can be done using the
componentWillUnmount
() lifecycle method or the
useEffect
() hook with a cleanup function.
dart
import { deregisterWECampaignCallback } from 'react-native-we-personalization';
...
React.useEffect(() => {
 return () => {
 deregisterWECampaignCallback();
 };
}, []);
At Last your
WECampaignCallbacks.js
file will look like below
dart
import React from 'react'
import { View } from 'react-native'
import WebEngage from 'react-native-webengage';
import { registerWECampaignCallback, deregisterWECampaignCallback } from 'react-native-we-personalization';

function WECampaignCallbacks() {
var webengage = new WebEngage();

 React.useEffect(() => {
 webengage.screen("weCampaignScreen");
 const WECampaignCallback = {
 onCampaignPrepared,
 onCampaignShown,
 onCampaignClicked,
 onCampaignException,
 };
 registerWECampaignCallback(WECampaignCallback);
 return () => {
 deregisterWECampaignCallback();
 };
 }, []);

 const onCampaignPrepared = (weCampaignData) => {
 console.log('onCampaignPrepared ', weCampaignData);
 };

 const onCampaignShown = (weCampaignData) => {
 console.log('onCampaignShown ', weCampaignData);
 };

 const onCampaignException = (weCampaignData) => {
 console.log('onCampaignException ', weCampaignData);
 };

 return (
 <View>
 <Text> Registering for WECampaignCallbacks</Text>
 </View>
 )
}

export default WECampaignCallbacks;
Exceptions
You will receive exception details in
onCampaignException
of WECampaignCallback &
onPlaceholderException
of WEPlaceholderCallback
Types of Exception:
Error Key
Error Description
timeout
Campaign failed to render in set time.
missingTargetView
Target property missing.
campaignFetchingFailed
Campaign fetching failed.
resourceFetchingFailed
Resource fetching falied
WECampaignData
You can access the Campaign Id and Placeholder details like name (id) and content. It consists of the following members
Name
Variable type
Definition
targetViewId
String
Placeholder name (id).
content
Object
Campaign view content which contains custom key-value pairs.
campaignId
String
The id for the running campaign on the placeholder. Default value would be blank.
WECampaignContent
Personalization SDK renders the Banner, Text view through this data. You can access the custom key-value pairs through this.
Name
Variable type
Definition
customData
Object
Custom key-value pairs defined for the campaign.
Creating Custom Views
WEPlaceholderCallback: Placeholder Callbacks
To implement
WEGInlineWidget
without view i.e Custom View
Register for the callback inside the component, you can add the following code either in the useEffect() or componentDidMount() method, or anywhere else that is appropriate:
dart
import { registerWEPlaceholderCallback, deregisterWEPlaceholderCallback } from 'react-native-we-personalization';
...
React.useEffect(() => {
 ...
 registerWEPlaceholderCallback(
 androidPropertyId,
 iOSPropertyId,
 screenName,
 onDataReceived,
 onPlaceholderException
 )
 return () => {
 deregisterWECampaignCallback();
 };
}, []);
This code will register the specified placeholder callback for the given androidPropertyId/iOSPropertyId and screenName, allowing you to receive notifications when custom data is received for the placeholder and when an exception occurs.
By registering for these callbacks, you can effectively manage and handle the placeholders in your screen. You can use these callbacks to update the UI with custom data, perform custom actions or handle errors and exceptions.
Params
Type
Definition
screenName
String
Refers to the current screen name of the view
androidPropertyId
String
Refers to the unique ID of the inline view, which corresponds to a property in the WebEngage dashboard for Android. This ID should be unique for each screen.
iosPropertyId
Integer
Refers to the unique ID of the inline view, which corresponds to a property in the WebEngage dashboard for iOS. This ID should be unique for each screen.
onDataReceived
Callback
This callback is triggered when the rule is passed before rendering the UI.
onPlaceholderException
Callback
This callback is triggered in case of any exception that occurs while fulfilling the campaign.
Tracking Campaign Impressions and Clicked Events for Custom Views
🚧
Please Note
Tracking impression and tracking clicks are mandatory steps for Custom View campaigns. If not added then impression and click data for these campaigns will not be recorded.
Record Viewed Impression
Impression tracking is simply tracking the number of views each campaign receives.
For example, if a user visits the screen and sees a campaign and visits the screen again then they will see the exact same campaign again, two impressions would be counted.
To track impressions for your campaign, use the
trackImpression()
method once the custom view has been shown on the screen by the application. This impression should be called only after
onDataReceived
is triggered for the customView
dart
import { trackImpression } from 'react-native-we-personalization';
//attributes: object data 
trackImpression(propertyId, objectData);
In the code given above
propertyId
- propertyId of the CustomView for which track impression needs to be fired.
objectData
- objectData if any attributes to be tracked otherwise it can be null.
Record Clicked Impression
You can track click impressions whenever the user clicks on the campaign view on the screen. This impression should be called only after
onDataReceived
is triggered for the customView from
registerWECampaignCallback
dart
import { trackImpression } from 'react-native-we-personalization';
//attributes: objectData 
trackClick(propertyId, objectData)
Updated
7 months ago
Troubleshooting
Flutter
Copy Page
