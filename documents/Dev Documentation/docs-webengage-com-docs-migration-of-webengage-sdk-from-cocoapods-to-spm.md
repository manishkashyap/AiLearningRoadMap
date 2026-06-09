# Migration Of WebEngage SDK From Cocoapods To SPM

- URL: https://docs.webengage.com/docs/migration-of-webengage-sdk-from-cocoapods-to-spm
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
Getting Started
Migration Of WebEngage SDK From Cocoapods To SPM
Swift Package Manager (SPM)
is now the recommended way to integrate the WebEngage iOS SDK. WebEngage is deprecating CocoaPods support for new projects and strongly recommends SPM for all new and existing integrations.
Step 1: Remove CocoaPods Integration
Start by cleanly removing the existing CocoaPods configuration from your project.
Open your project’s
Podfile
in a text editor.
Remove any line that references the WebEngage SDK, for example:
Ruby
pod 'WebEngage'

# check which ever SDK is integrated already, and based on that remove it.
pod 'WEPersonalization'
pod 'WebEngage/Core'
pod 'WENotificationInbox'
Save the file and open your project’s root directory in the terminal.
Run the following command to update your workspace:
Shell
pod install
This will regenerate your project without the WebEngage CocoaPods dependency.
Step 2: Integrate via Swift Package Manager
Now add the WebEngage SDK through Swift Package Manager in Xcode.
Open your project in Xcode.
Go to
File → Add Package Dependencies
.
In the search field, enter the WebEngage SDK repository URL:
URL
https://github.com/WebEngage/webengage-ios-sdk.git
When prompted for the dependency rule, choose either:
Branch: main
, or
Up to Next Major Version
and select the latest stable version.
Click
Add Package
.
In the
Choose Package Products
step, select the WebEngage modules your app uses:
WebEngageCore
(required)
WebEngageLocation
(optional) - refer to
Location Module Guide
to know more.
WebEngagePersonalization
(optional) - refer to
Personalization Module Guide
to know more.
WebEngageNotificationInbox
(optional) - refer to
Notification Inbox Module Guide
to know more.
Under
Add to Target
, select the app target(s) where you want to integrate the SDK.
For detailed instructions on SPM integration, refer to the
SPM Integration Guide
.
🚧
Be sure to include the Swift package products that correspond to the WebEngage features currently enabled in your app (e.g., Location, Personalization, Notification Inbox).
Step 3: Post-Migration Verification
After completing the migration, verify that the integration is working correctly.
Open your project workspace in Xcode.
In the
Project Navigator
, confirm that the
WebEngage
package appears under the
Dependencies / Package Dependencies
section.
Clean the build folder (
Product → Clean Build Folder
) and build the project.
Run the app and verify that:
The project compiles without errors.
The SDK initializes successfully (check logs or a test event).
Existing WebEngage features (events, notifications, location tracking) continue to function as expected.
This migration preserves your current WebEngage configuration while moving to the modern Swift Package Manager workflow.
Updated
about 2 months ago
Integration through CocoaPods
Tracking Users
Copy Page
