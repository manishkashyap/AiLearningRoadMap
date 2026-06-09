# Integration of WEPersonalization SDK

- URL: https://docs.webengage.com/docs/integration-of-wepersonalization-sdk
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
App In-line Content
Integration of WEPersonalization SDK
CocoaPods
WEPersonalization supports
Cocoapods
WEPersonalization's CocoaPods distribution requires Xcode 13.3.1 and CocoaPods 1.10.0 or higher.Here's how to install WEPersonalization using CocoaPods:
Create a Podfile if you don't already have one. From the root of your project directory, run the following command:
Shell
$ pod init
To your Podfile, add the WEPersonalization pod that you want to use in your app.
Ruby
pod 'WEPersonalization'
Install the pods, then open your .xcworkspace file to see the project in Xcode:
Shell
$ pod install --repo-update
Text
open your-project.xcworkspace
Integrate manually
WebEngage provides a pre-built binary XCFramework distribution for users who want to integrate WEPersonalization without using a dependency manager. To install WEPersonalization:
XCFramework
Download the
XCFramework SDK zip
. This file contains architecture slices for all available target architectures for all WEPersonalization SDKs and thus may take some time to download.
Unzip the file, then drag and drop this file in to Project/Workspace settings in
General >> Framework , Libraries and Embedded content
Section
Updated
7 months ago
App In-line Content
In-app Messaging
Copy Page
