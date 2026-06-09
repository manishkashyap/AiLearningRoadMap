# Xamarin.iOS

- URL: https://docs.webengage.com/docs/xamarin-ios
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.iOS
Xamarin.iOS
exposes the complete iOS SDK for .NET developers. It enables you to build fully native iOS apps using C# or F#.
Here's how you can integrate the WebEngage SDK with your Xamarin.iOS app:
1. Installation
Step 1:
Download
WebEngage Xamarin.iOS Library
.
Step 2:
To consume this downloaded .DLL in your Xamarin.iOS app, you must add a reference to your Xamarin.iOS project by right-clicking on the References node of your project and selecting
Add Reference
.
2. Initialization
Step 1:
Add the following properties to the Info.plist file of your project.
Key
Type
Value
Description
WEGLicenseCode
String
Your WebEngage license code
Mandatory
If you have multiple apps, then you can use the same license code for all of them.
UIBackgroundModes
Array
fetch
,
location
Optional
Required only if you want to track location updates in background.
WEGEnableLocationAuthorizationRequest
String
ALWAYS
/
IN_USE
/
NO
Optional
Enables WebEngage SDK to request user to authorize for location on behalf of the app. If this is absent or the value is anything other than
ALWAYS
or
IN_USE
, WebEngage SDK would not make any authorization request on behalf of the app. It will track location updates only if the app itself has sought relevant permissions from the user.
NSLocationAlwaysUsageDescription
String
App specific description
Mandatory if:
The app makes authorization request to always use location, or
Value of
WEGEnableLocationAuthorizationRequest
is
ALWAYS
.
NSLocationWhenInUseUsageDescription
String
App specific description
Mandatory if:
The app makes authorization request to use location when the app is in use, or
Value of
WEGEnableLocationAuthorizationRequest
is
IN_USE
.
WEGLogLevel
String
DEFAULT
/
VERBOSE
Optional
Available from SDK version 3.2. In
VERBOSE
mode, you get detailed SDK logs.
VERBOSE
mode logs are a superset of
DEFAULT
mode logs.
WEGEnvironment
String
DEFAULT
/
in
Optional
If you're specifically using our India data center to store/access your data, please ensure that you specify
in
as the value for
WEGEnvironment
WEGAlternateAppSupport
Boolean
YES
/
NO
Optional
WebEngage supports running multiple apps within the same License Code.
Ensure that you are using Auth Keys instead of APNS Certificates for Push Notifications.
To enable Multi App Support, in app's
Info.plist
file, enter
WEGAlternateAppSupport
key as
Boolean
type & set it to
YES
.
Please note that this should not be used for Staging & Production builds of the same app.
Step 2:
Initialize WebEngage SDK with your license code from
FinishedLaunching
callback of your
AppDelegate
class as shown below.
C#
...
using WebEngageXamariniOS;

namespace YourNamespace
{
 [Register("AppDelegate")]
 public class AppDelegate : UIApplicationDelegate
 {
 ...
 public override bool FinishedLaunching(UIApplication application, NSDictionary launchOptions)
 {
 ...
 WebEngage.SharedInstance().Application(application, launchOptions);
 return true;
 }
 ...
 }
}
3. Additional Steps (Optional)
For other integrations such as
location tracking
, please refer to the
Advanced section
.
🚧
Congratulations!
You have successfully integrated WebEngage with your app and are sending user session data to WebEngage. Please note that it may take up to a few minutes for data to reflect in your dashboard.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
We recommend that you implement the following integrations with your app before releasing it with WebEngage for the first time:
Track User Properties as User Attributes
Track User Actions as Events
Configure Push Messaging
Configure In-app Messaging
Copy Page
