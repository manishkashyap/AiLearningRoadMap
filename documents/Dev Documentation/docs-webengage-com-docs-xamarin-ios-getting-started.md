# Getting Started

- URL: https://docs.webengage.com/docs/xamarin-ios-getting-started
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Getting Started
1. Installation
Download
WebEngage Xamarin.iOS Library
.
To consume this downloaded .DLL in your Xamarin.iOS app, you must add a reference to your Xamarin.iOS project by right-clicking on the References node of your project and selecting
Add Reference
.
2. Initialization
Add the following properties to the Info.plist file of your project.
Key
Type
Value
Description
WEGLicenseCode
String
Your WebEngage license code
Mandatory
If you have multiple apps, you can use the same license code for all of them.
UIBackgroundModes
Array
fetch
,
location
Optional
Required if you want to track location updates in background.
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
Make sure you replace
YOUR_WEBENGAGE_LICENSE_CODE
with your WebEngage license code.
Locating your WebEngage license code
As shown above, naviagte to the
Account Setup
section to find your license code. Your License Code might start with tilde (
~
).
3. Additional steps (Optional)
For other integration options such as
location tracking
, refer the Advanced section.
Next steps
Congratulations! You have now successfully integrated WebEngage with your Hybrid app and are now sending user session data to WebEngage.
Note that it may take a few minutes for your data to show up on the WebEngage dashboard. We suggest you meanwhile proceed to read the next sections to learn how to:
Track user properties as attributes
Track user actions as events
Integrate push messaging
Integrate in-app messaging
Updated
7 months ago
Getting Started
Copy Page
