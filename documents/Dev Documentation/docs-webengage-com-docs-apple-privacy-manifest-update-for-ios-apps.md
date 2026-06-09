# Apple Privacy Manifest Update

- URL: https://docs.webengage.com/docs/apple-privacy-manifest-update-for-ios-apps
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
Apple Privacy Manifest Update
Overview
At WWDC23, Apple introduced new privacy manifests and signatures for SDKs to help app developers better understand how third-party SDKs use data, secure software dependencies, and provide additional privacy protection for users.
Starting May 1st 2024, if your new app or app update submission adds a third-party SDK that is commonly used in apps on the App Store, you must include the privacy manifest for the SDK.
Signatures are also required when you use the SDK as a binary dependency. This functionality is a step forward for all apps, and we encourage all SDKs to adopt it to better support the apps that depend on them. For more information, refer to the official announcement from Apple.
How Does WebEngage Comply with this?
This section describes how WebEngage complies with the new privacy manifests and signatures for SDKs.
Privacy Manifest
The Privacy Manifest is a file that describes the specific privacy practices and data collection activities of an iOS app. It provides essential information to users about how their personal data is collected, used, and shared by the app. This is a requirement by Apple for developers to ensure transparency and allow users to make informed decisions about their privacy. It includes details on the types of data collected (such as personal information, location, browsing history), how the data is used, and whether it is shared with third parties.
Based on the documentation from Apple, "Third-party SDKs need to provide their own privacy manifest files that record the types of data they collect. Your app’s privacy manifest file doesn’t need to cover data collected by third-party SDKs that your app links to."
WebEngage SDKs and associated modules with SDK core version 6.8.1 and above are compliant with the guidelines from Apple and the following data is declared from the Privacy manifests.
NSPrivacyCollected
DataType
NSPrivacyCollected
DataTypePurposes
NSPrivacyCollected
DataTypeLinked
NSPrivacyCollected
DataTypeTracking
UserID
Analytics ,
Product personalization,
App functionality
YES
NO
Device ID
Analytics,
Product personalization
YES
NO
Product interaction
Analytics,
Product personalization
YES
NO
What is Tracking?
Tracking involves using data from your app to monitor user behavior across other apps, websites, or offline environments for targeted advertising or sharing data with third parties. Examples include:
Showing ads based on data from other sources.
Sharing data with brokers for advertising purposes.
Not considered tracking:
Data linked only on the device.
Data shared for security or fraud prevention.
Data shared for credit reporting purposes.
What is Linking?
Linking refers to whether the data collected by your app is associated with an individual's identity. This identity linkage can occur directly through identifiers such as user IDs or names, or indirectly through data that can be traced back to the user.
Key Points:
Direct Identifiers: User ID, name, email, phone number.
Indirect Identifiers: Data that can identify a user when combined with other information.
Code Signing
When you add third-party binary SDKs to your target as XCFrameworks, the behavior of those packages becomes part of the behavior of your product. An attacker who can inject a compromised version of the SDK into your project can change your app’s behavior and cause security and privacy issues for your developers, testers, and people who use your product. To avoid those, we have code-signed all the WebEngage frameworks.
To comply with the policy, you must upgrade your iOS app with the WebEngage SDK version 6.8.2 or above.
By When Should I Upgrade My App?
Apple documentation mentions the following:
Starting March 13: If you upload a new or updated app to App Store Connect that uses an API requiring approved reasons, we’ll send you an email letting you know if you’re missing reasons in your app’s privacy manifest. This is in addition to the existing notification in App Store Connect.
Starting May 1: You’ll need to include approved reasons for the listed APIs used by your app’s code to upload a new or updated app to App Store Connect. If you’re not using an API for an allowed reason, please find an alternative. And if you add a new third-party SDK that’s on the list of commonly used third-party SDKs, these API, privacy manifest, and signature requirements will apply to that SDK. Make sure to use a version of the SDK that includes its privacy manifest and note that signatures are also required when the SDK is added as a binary dependency.
Therefore, we strongly recommend updating the WebEngage iOS SDK with your next app update. Otherwise, your next app update may get rejected.
However, you do not need to rush an app upgrade only to comply with the requirements.
What will happen to my current app users?
This change only affects App versions published on or after May 1, 2024. Users on App versions published before this will not be affected including new installs and reinstalls.
What do you need to do?
In WebEngage’s SDK, we have included all the items that we track by default. If you are tracking any user information using the WebEngage SDK, you need to specify them in the PrivacyInfo.xcprivacy file.
What all needs to be added:
NSPrivacyTracking
NSPrivacyTrackingDomains
NSPrivacyCollectedDataTypes
NSPrivacyAccessedAPITypes
NSPrivacyTrackingDomains:
You need to add the domain according to the environment you will be using, it can be Golobal, IN, KSA, and below if the respective domain that you need to add under the NSPrivacyTrackingDomains.
c.webengage.com - Global
c.in.webengage.com - IN
c.ksa.webengage.com - KSA
NSPrivacyCollectedDataTypes
The data types can be divided into 3 categories:
Collected ✔️ - WebEngage SDK collects this data, By Default.
Not Collected ❌ - WebEngage SDK does not require this data.
User Collected 💡- Not Collected by WebEngage, The user can track this using WebEngage SDK
We need to use the
data types
provided by Apple to report the categories of data your app or WebEngage SDK collects. You can obtain the complete list of items that should be added in the section under
Describing data use in privacy manifests.
Category
Collected by WebEngage or Not
Method used to track the data
Description
Contact info
Name
Email
Phone number -
Physical address
Other user contact info
User Collected💡
WebEngage.sharedInstance()?.user.setFirstName()/ WebEngage.sharedInstance()?.user.setLastName()
WebEngage.sharedInstance()?.user.setEmail()
WebEngage.sharedInstance()?.user.setPhone()
WebEngage.sharedInstance()?.user.setAttribute()
If you have set up to track this data to WebEngage SDK, then declare it accordingly.
Health & fitness
Health
Fitness
Not Collected ❌
Financial info
Payment info
Credit info
Other financial info
User Collected💡
WebEngage.sharedInstance().analytics.trackEvent()
If you have set up to track this data to WebEngage SDK, then declare it accordingly
Location
Precise location
Coarse location
User Collected💡
WebEngage.sharedInstance()?.user.setUserLocationWithLatitude()
If you have set up to track this data to WebEngage SDK, then declare it accordingly.
Sensitive info
Sensitive info
User Collected💡
WebEngage.sharedInstance()?.user.setGender()
If you have set up to track this data to WebEngage SDK, then declare it accordingly.
Contacts
Contacts
User Collected💡
WebEngage.sharedInstance().analytics.trackEvent()
If you have set up to track this data to WebEngage SDK, then declare it accordingly.
User content
Emails or text messages
Photos or videos
Audio data
Gameplay content
Customer support
Other user content
Not Collected ❌
Browsing History
Browsing history
Not Collected ❌
Search history
Search history
User Collected💡
WebEngage.sharedInstance().analytics.trackEvent()
If you have set up to track this data to WebEngage SDK, then declare it accordingly.
Identifiers
User ID
Device ID
User ID - User Collected💡Device Id - Collected ✔️
WebEngage.sharedInstance().user.login()
If you have set up to track this data to WebEngage SDK, then declare it accordingly.
Purchases
Purchase history
User Collected💡
WebEngage.sharedInstance().analytics.trackEvent()
If you have set up to track this data to WebEngage SDK, then declare it accordingly.
Usage data
Product interaction
Advertising data
Other usage data
Product interaction -Collected ✔️
Advertising data - Collected ✔️
Other usage data - User Collected💡
WebEngage.sharedInstance().analytics.trackEvent()
If you have set up to track this data to WebEngage SDK, then declare it accordingly.
Now, for each of the data you have collected, you need to provide a reason for collecting data. You can do that using the below strings as values for the NSPrivacyCollectedDataTypePurposes key in your NSPrivacyCollectedDataTypes dictionaries:
Purpose
Description
App Functionality
Such as authenticating the user, enabling features, preventing fraud, implementing security measures, ensuring server up-time, minimizing app crashes, improving scalability and performance, or performing customer support.
Analytics
Using data to evaluate user behavior, including understanding the effectiveness of existing product features, planning new features, or measuring audience size or characteristics.
Product personalization
Customizing what the user sees, such as a list of recommended products, posts, or suggestions.
Updated
7 months ago
Troubleshooting
Push
Copy Page
