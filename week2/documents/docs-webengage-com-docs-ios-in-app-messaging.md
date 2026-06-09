# In-app Messaging

- URL: https://docs.webengage.com/docs/ios-in-app-messaging
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
In-app Messaging
No additional steps are required for enabling
In-app Notifications.
However, we recommend that you track the various sections of your app as
Screens
to customize In-app message placement. You can also track specific app-user interactions as
Screen Data
to contextually show the In-app message. These data points can be used to
configure In-app message targeting
while creating the campaign.
🚧
Before continuing, please ensure that you have
added the WebEngage SDK to your app
.
Tagging App Screens
Screens are the mobile equivalent of web pages, which can have associated properties. WebEngage SDK allows you to tag whenever a user sees a screen in your container view controllers like UITabBarController or UINavigationController. These tags allow you to pinpoint screens in your app where you would later render in-app messages using WebEngage dashboard. A view controller can have multiple screens and vice versa is also possible. Note that screens are only usable for targeting in-app engagements.
All screen related APIs are part of WebEngage iOS SDK's
WEGAnalytics
object. You can get an instance of
WEGAnalytics
object as follows.
Swift
Objective-C
var weAnalytics = WebEngage.sharedInstance().analytics
// Get an instance of `WEGAnalytics` object
id weAnalytics = [WebEngage sharedInstance].analytics;
After WebEngage has been successfully initialized, you can tag screens by calling the APIs on WEGAnalytics object.
Swift
Objective-C
weAnalytics.navigatingToScreen(withName: "Purchase Screen")
[weAnalytics navigatingToScreenWithName:@"Purchase Screen"];
🚧
navigatingToScreenWithName
informs WebEngage SDK that the user has navigated to a new screen. Any previously set screen data is lost.
Tracking Screen Data
Every screen can be associated with some contextual data, which can be part of the targeting rule for in-app messages. Your app can update the data associated with a screen using the screen APIs described below.
Swift
Objective-C
var screenData = ["productId": "~hs7674", "price": 1200]
weAnalytics.updateCurrentScreenData(screenData)
NSDictionary *screenData=@{
 @"productId":@"~hs7674",
 @"price":@1200
};

[weAnalytics updateCurrentScreenData:screenData];
🚧
These APIs can be called any number of times after calling
navigatingToScreenWithName
.
You can set the screen name and data in a single API call as shown below.
Swift
Objective-C
var screenData = ["productId": "~hs7674", "price": 1200]
weAnalytics.navigatingToScreen(withName: "Purchase Screen", andData: screenData)
NSDictionary *screenData=@{
 @"productId":@"~hs7674",
 @"price":@1200
};

[weAnalytics navigatingToScreenWithName:@"Purchase Screen" andData:screenData];
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Integration of WEPersonalization SDK
Advanced
Copy Page
