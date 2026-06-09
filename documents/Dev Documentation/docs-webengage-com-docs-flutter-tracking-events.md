# Tracking Events

- URL: https://docs.webengage.com/docs/flutter-tracking-events
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Flutter
Tracking Events
🚧
Must Read
We recommend that you get yourself acquainted with the concept of
System Events
,
Custom Events
and their attributes before proceeding. Doing so will help you better understand the workings of this section.
Here are a few
Custom Event Templates
to help you get started
.
WebEngage starts tracking some events as soon as you
integrate the SDK
. These are called
System Events
and track some generic user interactions with your app and campaigns.
Here's a list of the
System Events
that are automatically tracked by us.
You can create
Custom Events
to track any other user interactions that are crucial for your business. Each
Custom Event
can further be defined by
Event Attributes
like price, quantity, category, and so on. Such granular data enables you to engage users through highly contextual and personalized campaigns through all the
channels of engagement
.
Tracking Custom Events & Attributes
Custom Events
can be tracked using the
WebEngagePlugin.trackEvent
method of our
Flutter SDK.
You can also send some associated data as
Event Attributes
with each
Custom Event
to your WebEngage dashboard. For example, in the below code snippet,
Order Placed
is the
Custom Event
and
Amount
is the
Custom Event Attribute
attached to it.
Dart
import 'package:webengage_flutter/webengage_flutter.dart';
...
 // Track simple event
 WebEngagePlugin.trackEvent('Added to Cart');

 // Track event with attributes
 WebEngagePlugin.trackEvent('Order Placed', {'Amount': 808.48});
```
The above code snippet can be used to track
Custom Event Attributes
of
String
,
Number
,
Boolean
,
Array
, and
Object
type data.
For Tracking
Date
type Custom Event Attributes:
Please use this dart package
and refer to the below code snippet for accepted date formats.
🚧
Note
Date should be in UTC format.
Dart
final DateTime now = DateTime.now().toUtc();
 
final DateFormat formatter = DateFormat("'~t'yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");

WebEngagePlugin.trackEvent('Date', {'date': formatter.format(now)});
Guidelines
Here are a few things to keep in mind:
Custom Event
names must be less than 50 characters long.
Custom Event Attribute
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
Custom Event Attributes
can be of these data types:
String
,
Number
,
Boolean
,
Date
,
Array
,
Object
.
You can create a maximum of 25
Event Attributes
of each data type for a
Custom Event.
If an
Event Attribute
value is
Array
or
Object
, then it cannot be used to create segments. It can only be used to personalize campaigns.
The first datapoint synced to WebEngage defines the data type for that event attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Event Attribute
data will stop flowing to your WebEngage dashboard.
Please feel free to drop in a few lines at
[email protected]
or get in touch with your
Onboarding Manager
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Tracking Users
Push Messaging
Copy Page
