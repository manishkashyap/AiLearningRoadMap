# Tracking Events

- URL: https://docs.webengage.com/docs/ionic-capacitor-tracking-events
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Ionic Capacitor
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
can further be defined by Event Attributes like price, quantity, category, and so on. Such granular data enables you to engage users through highly contextual and personalized campaigns through all the
channels of engagement
.
Tracking Custom Events
Custom Events
can be tracked using the
Webengage.track
method of our Hybrid SDK. As shown below, you can also choose to send some associated data (event attributes) with it to WebEngage.
JavaScript
import { Webengage } from "@awesome-cordova-plugins/webengage";
...
Webengage.track(eventName, eventData);
Guidelines
Here are a few things to keep in mind:
Custom Event
names must be less than 50 characters long.
Custom Event Attribute
names are case sensitive and must be less than 50 characters long. String attribute values must be less than 1000 characters long.
eventName
or
eventAttributeName
must not start with
we_
. Names starting with
we_
are reserved exclusively for internal use at WebEngage. Thus, to avoid data contamination for your account, such data will be ignored if used for your Custom Events.
Custom Event Attributes can be of these data types:
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
You can create a maximum of
25 Event Attributes
of each data type for a Custom Event.
If an
Event Attribute
value is
Array
or
Object
, then it cannot be used to create segments. It can only be used to personalise campaigns.
The first datapoint synced to WebEngage defines the data type for that event attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then Custom Event Attribute data will stop flowing to your WebEngage dashboard.
Tracking Event Attributes
You can track Event Attributes along with a Custom Event in the following manner:
JavaScript
import { Webengage } from "@awesome-cordova-plugins/webengage";
...
Webengage.track("Added To Cart", {
 /* Numbers */
 "Product ID" : 1337,
 "Price" : 39.80,
 "Quantity" : 1,

 /* Strings */
 "Product" : "Givenchy Pour Homme Cologne",
 "Category" : "Fragrance",
 "Currency" : "USD",

 /* Boolean */
 "Discounted" : true
});

Webengage.track("Order Placed", {
 "Amount" : 808.48,
 "Product 1 SKU Code" : "UHUH799",
 "Product 1 Name" : "Armani Jeans",
 "Product 1 Price" : 300.49,
 "Product 1 Size" : "L",
 "Product 2 SKU Code" : "FBHG746",
 "Product 2 Name" : "Hugo Boss Jacket",
 "Product 2 Price" : 507.99,
 "Product 2 Size" : "L",
 
 /* Date */
 "Delivery Date" : new Date("2017-01-09T00:00:00.000Z"),
 
 "Delivery City" : "San Francisco",
 "Delivery ZIP" : "94121",
 "Coupon Applied" : "BOGO17"
});
Tracking Complex Event Attributes
WebEngage allows you to pass complex event attributes as
Array
and
Object
data types. You will be able to use this data to personalise campaigns, as shown below. However, you will not be able to use complex attributes for creating segments.
Here's how you can track Complex Event Attributes along with a Custom Event:
JavaScript
Webengage.track("Order Placed", {
 "Amount" : 2300,

 /* Date */
 "Delivery Date" : new Date("2017-01-09T00:00:00.000Z"),

 /* Complex nested data */
 "Products" : [
 {
 "SKU Code": "UHUH799",
 "Product Name": "Armani Jeans",
 "Price": 300.49,
 "Details": {
 "Size": "L"
 }
 },
 {
 "SKU Code": "FBHG746",
 "Product Name": "Hugo Boss Jacket",
 "Price": 507.99,
 "Details": {
 "Size": "L",
 }
 },
 ],

 /* Objects */
 "Delivery Address": {
 "City": "San Francisco",
 "ZIP": "94121"
 },

 /* Arrays */
 "Coupons Applied": [
 "BOGO17"
 ]
});
Please feel free to drop in a few lines at
[email protected]
or get in touch with your Onboarding Manager in case you have any further queries. We're always just an email away!
Updated
7 months ago
Tracking Users
Push Messaging
Copy Page
