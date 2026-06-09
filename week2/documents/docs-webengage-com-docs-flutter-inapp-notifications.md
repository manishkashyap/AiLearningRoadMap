# In-app Messaging

- URL: https://docs.webengage.com/docs/flutter-inapp-notifications
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Flutter
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
Before continuing, please ensure that you've
added the Flutter SDK to your app
.
Tagging App Screens
Screens are the mobile equivalent of web pages, which can have associated properties. WebEngage SDK allows you to tag whenever a user sees a screen. These tags allow you to pinpoint screens in your app where you can render in-app messages through the WebEngage dashboard.
Dart
import 'package:webengage_flutter/webengage_flutter.dart';
 
 WebEngagePlugin.trackScreen('Home Page');
Tracking Screen Data
Every screen can be associated with some contextual data, which can be part of the targeting rule for in-app messages. Your app can update the data associated with a screen using the below code snippet.
Dart
import 'package:webengage_flutter/webengage_flutter.dart';
 
 WebEngagePlugin.trackScreen('Product Page', {'Product Id': 'UHUH799'});
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Copy Push to Notification Inbox - Flutter
Callbacks
Copy Page
