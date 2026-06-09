# Location Module

- URL: https://docs.webengage.com/docs/location-module
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
Getting Started
Location Module
This SDK enables location-based tracking of users. It allows you to trigger campaigns and personalize experiences based on a user's real-time or last known location.
Installation
Depending on your dependency manager, follow the steps below to link the Location module:
Install using Swift Package Manager (SPM)
If you selected
WebEngageLocation
during the initial SPM setup, you are good to go. If you missed it, go to your
Project Targets > General > Frameworks, Libraries, and Embedded Content
to add it manually.
Install Using CocoaPods
Add the following line to your
Podfile
:
Ruby
pod 'WebEngage/Location'
Then, run the installation command in your terminal:
Shell
pod install
🚧
Important
Starting from iOS 14.0, Apple gives users control over the level of location precision an app can access. Due to this,
region monitoring (geofence)
will not work when the user has disabled precise location sharing for the app.
Region monitoring is supported only with
“Always” authorization
. It is
not supported
when the app has only
“When‑In‑Use” authorization
.
Additionally,
dwell triggers are not supported
on iOS; therefore, the WebEngage SDK supports only
Enter
and
Exit
geofence triggers.
Info.plist Requirements
For the Location module to function, Apple requires specific privacy keys. Add these to your
Info.plist
:
Key
Value / Type
Description
WEGEnableLocationAuthorizationRequest
ALWAYS
/
IN_USE
Enables WebEngage SDK to request the user for location tracking authorization on behalf of the app.
If property is absent or value is not set to ALWAYS or IN_USE, then WebEngage SDK will track location updates only if the app itself has sought relevant permissions from the user.
NSLocationAlwaysUsageDescription
String
Explain why you need background location.
NSLocationWhenInUseUsageDescription
String
Explain why you need location while using the app.
UIBackgroundModes
fetch / location
Required only if you want to track location updates in the background.
The Location module initializes automatically alongside the Core SDK if the library is linked.
Updated
about 2 months ago
Getting Started
Integration through CocoaPods
Copy Page
