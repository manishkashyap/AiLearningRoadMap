# Device Mode (Advanced) Integration

- URL: https://docs.webengage.com/docs/segment-advanced-integration
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Partners Integrations
Segment.com
Device Mode (Advanced) Integration
🚧
Must Read
We recommend that you get yourself acquainted with all the concepts related to
Users
and
Events
before proceeding. Doing so will help you understand the workings of this section, better.
Referred to as
Device Mode
in
Segment.com, Advanced Integration
enables you to send user data and events data through your website, app, server and leverage all the channels of engagement in your WebEngage dashboard including,
Push, In-app, SMS, On-site, Web Push, Email, WhatsApp and Facebook retargeting.
Currently, WeEngage supports the following Segment APIs -
track
,
identify
and
page
.
Identify:
When a user is identified, Segment will send that user's information to WebEngage, wherein a user will be created/updated. The
anonymousId
must be present in case of anonymous user and
userId
in case of identified user.
Page:
This is only supported on the client side. Sending page events via server side integration is not supported.
Guidelines
Your data must be sent in a specific format through Segment.com to ensure that our backend systems understand it correctly. Here are a few guidelines to help you out:
For Tracking User Attributes
A few things to keep in mind:
User Attribute
names are case sensitive and must be less than 50 characters long.
String
attribute values must be less than 1000 characters long. Additional characters will be truncated.
You can create a maximum of 25
Custom User Attributes
of each data type.
userAttributeName
must not start with
we_
. Names starting with
we_
are reserved exclusively for internal use at WebEngage. Thus, to avoid data contamination for your account, such data will be ignored if used for your
Custom User Attributes.
The first datapoint synced to WebEngage defines the data type for that user attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Users Attribute
data will stop flowing to your WebEngage dashboard.
For Tracking Events
A few things to keep in mind:
Custom Event
names must be less than 50 characters long.
Event Attribute
values can be
Boolean
,
Number
,
String
and
Date
data types.
Event Attribute
names are case sensitive and must be less than 50 characters long.
String
attribute values must be less than 1000 characters long.
eventName
or
eventAttributeName
must not start with
we_
. Names starting with
we_
are reserved exclusively for internal use at WebEngage. Thus, to avoid data contamination for your account, such data will be ignored if used for your
Custom Events.
You can create a maximum of 25
Event Attributes
of each data type for a
Custom Event.
The first datapoint synced to WebEngage defines the data type for that event attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Event Attribute
data will stop flowing to your WebEngage dashboard.
Website (JavaScript)
Here's how you can integrate your website with WebEngage:
Step 1:
Log in to your Segment.com account and go to the relevant workspace.
Step 2:
Click on
Add Destination
and search for
WebEngage
in the
Destinations Catalog.
Step 3:
Click on
WebEngage
, select
JavaScript
as the source and click
Confirm Source.
Step 4:
Enter your WebEngage
License Code
.
Leave the field,
API Key
blank.
And you're all set! You can now
test the integration
and configure channels to start engaging users.
Server
Here's how you can integrate your Server with WebEngage:
Step 1:
Log in to your Segment.com account and go to the relevant workspace.
Step 2:
Click on
Add Destination
and search for
WebEngage
in the
Destinations Catalog.
Step 3:
Click on
WebEngage
, select
Server
as the source and click
Confirm Source.
Step 4:
Enter your WebEngage
API Key
.
Leave the field,
License Code
blank.
And you're good to go! You can now
test the integration
and configure channels to start engaging users.
Android
🚧
Sample Android App
We've created a sample Android application that integrates WebEngage via Segment for your reference. Check it out in our
GitHub repository
.
Here's how you can integrate your app with WebEngage:
Step 1:
Log in to your Segment.com account and go to the relevant workspace.
Step 2:
Click on
Add Destination
and search for
WebEngage
in the
Destinations Catalog.
Step 3:
Click on
WebEngage
, select
Android
as the source and click
Confirm Source.
Step 4:
Enter your
License Code
.
Leave the field,
API Key
blank.
Step 5:
Install the WebEngage-Segment integration by adding this line to your app's
build.gradle
file:
Java
implementation 'com.webengage:android-segment:2.+'
Step 6:
After adding the dependency, you must register WebEngage's destination in your Segment's Analytics instance. To do this, import the WebEngage integration:
Java
import com.webengage.sdk.android.integrations.segment.WebEngageIntegration;
And add the following line:
Java
analytics = new Analytics.Builder(this, "YOUR_SEGMENT_WRITE_KEY")
 .use(WebEngageIntegration.FACTORY)
 .build();
Step 7:
Include the following rules in your ProGuard file.
Groovy
-keep class com.webengage.sdk.android.**{*;}
-dontwarn com.webengage.sdk.android.**
Step 8 (Optional): Advanced Settings (Location Tracking, EAttribution)
Follow this guide
to configure advanced options like attribution and location tracking for your Android app.
Follow this guide
to configure the SDK authentication for your Android app. You can set the Authentication Token after calling the Segment's
identify
function.
And you're done!
You can now
test the integration
and configure channels to start engaging users.
🚧
Additional Configurations For Sending Push & In-app Notifications Through WebEngage
Step-by-step guide to configuring
Push Notifications
for Android
Step-by-step guide to configuring
In-app Messaging
for Android
Additional steps for India Environment (Data Centre) support
📘
Support for IN Environment SDK
Below steps are only to be performed if your project is on
WebEngage's IN environment
.
If you are not sure which environment your account is on, kindly check the URL of your dashboard:
For US environment, the URL begins with:
https://dashboard.webengage.com
For Indian environment, the URL begins with:
https://dashboard.in.webengage.com
Kindly reach out
[email protected]
if you need any further assistance.
IN environment clients are required to perform the steps below as their license code cannot be configured through Segment's dashboard directly.
For apps integrated with WebEngage's IN environment Android SDK, add the appropriate meta-data under the application tag of your
AndroidManifest.xml
file.
AndroidManifest.xml
<meta-data android:name="com.webengage.sdk.android.environment" android:value="in" />
<meta-data android:name="com.webengage.sdk.android.key" android:value="WEBENGAGE-LICENSE-KEY" />
Additional steps for Saudi Arabia Environment (Data Centre) support
📘
Support for KSA Environment SDK
Below steps are only to be performed if your project is on
WebEngage's KSA environment
.
If you are not sure which environment your account is on, kindly check the URL of your dashboard:
For US environment, the URL begins with:
https://dashboard.webengage.com
For Indian environment, the URL begins with:
https://dashboard.in.webengage.com
For Saudi Arabia environment, the URL begins with:
<https://dashboard.ksa.webengage.com>
Kindly reach out
[email protected]
if you need any further assistance.
KSA environment clients are required to perform the steps below as their license code cannot be configured through Segment's dashboard directly.
For apps integrated with WebEngage's KSA environment Android SDK, add the appropriate meta-data under the application tag of your
AndroidManifest.xml
file.
AndroidManifest.xml
<meta-data android:name="com.webengage.sdk.android.environment" android:value="ksa" />
<meta-data android:name="com.webengage.sdk.android.key" android:value="WEBENGAGE-LICENSE-KEY" />
iOS
🚧
Sample iOS App
We've created a sample iOS application that integrates WebEngage via Segment for your reference. Check it out in our
GitHub repository
.
Here's how you can integrate your app with WebEngage:
Step 1:
Log in to your Segment.com account and go to the relevant workspace.
Step 2:
Click on
Add Destination
and search for
WebEngage
in the
Destinations Catalog.
Step 3:
Click on
WebEngage
, select
iOS
as the source and click
Confirm Source.
Step 4:
Enter your
License Code
.
Leave the field,
API Key
blank.
Step 5:
Install the Segment-WebEngage integration by adding this line to your
CocoaPods
Podfile
:
Ruby
pod "Segment-WebEngage"
If you are using Xcode 9 and face build issues, then we recommend that you try this code:
Ruby
pod "Segment-WebEngage/Xcode9"
Step 6:
After adding the dependency, you must register the integration with our SDK. To do this, import the WebEngage integration in your
AppDelegate
:
Objective-C
Swift
#import <Segment-WebEngage/WEGSegmentIntegrationFactory.h>
import Segment_WebEngage
And add the following lines to your AppDelegate's
application:didFinishLaunching:WithOptions:
method.
Objective-C
Swift
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
 
 //Initialise Segment
 SEGAnalyticsConfiguration *configuration = [SEGAnalyticsConfiguration configurationWithWriteKey:@"XXXXXXXXXXXXXXXXXXXXXXXXXXX"];
 
 //Additional Segment Configuration
 configuration.trackApplicationLifecycleEvents = NO; // Enable this to record certain application events automatically!
 configuration.recordScreenViews = NO; // Enable this to record screen views automatically!
 
 //Register WebEngage Integration With Segment
 [configuration use:[WEGSegmentIntegrationFactory instanceWithApplication:application launchOptions:launchOptions]];
 
 [SEGAnalytics setupWithConfiguration:configuration];
 
 return YES;
}
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
 // Initialise Segment
 let configuration = AnalyticsConfiguration(writeKey: "XXXXXXXXXXXXXXXXXXXXXXXXXXX")
 // Additional Segment Configuration
 configuration.trackApplicationLifecycleEvents = false
 // Enable this to record certain application events automatically!
 configuration.recordScreenViews = false // Enable this to record screen views automatically!
 // Register WebEngage Integration With Segment
 configuration.use(WEGSegmentIntegrationFactory.instance(with: application, launchOptions: launchOptions))
 Analytics.setup(with: configuration)
 return true
 }
Step 7 (optional) : Advanced Settings (Callbacks, Manual Push Registration)
Follow this guide
to configure advanced integrations like in-app callback and manual push registration for your iOS app. You can find the similar flavours of methods in Segment-WebEngage's
WEGSegmentIntegrationFactory
class.
Follow this guide
to configure SDK authentication for your iOS app. You can set the Authentication Token after calling the Segment's
identify
function.
And you're good to go!
You can now
test the integration
and configure channels to start engaging users.
🚧
Additional Configurations For Sending Push & In-app Notifications Through WebEngage
Step-by-step guide to configuring
Push Notifications
for iOS
Step-by-step guide to configuring
In-app Messaging
for iOS
Additional steps for India Environment (Data Centre) support
📘
Support For India Environment
Below steps are only to be performed if your project is on
WebEngage's IN environment
.
If you are not sure which environment your account is on, kindly check the URL of your dashboard:
For US environment, the URL begins with:
https://dashboard.webengage.com
For Indian environment, the URL begins with:
https://dashboard.in.webengage.com
Kindly reach out
[email protected]
if you need any further assistance.
IN environment clients are required to perform the steps below as their license code cannot be configured through Segment's dashboard directly.
For apps integrated with WebEngage's IN environment iOS SDK, add the appropriate key-value under
info.plist
file of your application.
Key
Type
Value
WEGEnvironment
String
IN
Additional steps for Saudi Arabia Environment (Data Centre) support
📘
Support For Saudi Arabia Environment
Below steps are only to be performed if your project is on
WebEngage's KSA environment
.
If you are not sure which environment your account is on, kindly check the URL of your dashboard:
For Saudi Arabia environment, the URL begins with:
<https://dashboard.ksa.webengage.com>
Kindly reach out
[email protected]
if you need any further assistance.
KSA environment clients are required to perform the steps below as their license code cannot be configured through Segment's dashboard directly.
For apps integrated with WebEngage's KSA environment iOS SDK, add the appropriate key-value under
info.plist
file of your application.
Key
Type
Value
WEGEnvironment
String
KSA
Please feel free to drop in a few lines at
[email protected]
in case you'd like to revert to
Basic Integration
or have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
Complete the one-time channel configuration to start engaging users!
Push
In-app
SMS
On-site
Web Push
Email
WhatsApp
Facebook
Copy Page
