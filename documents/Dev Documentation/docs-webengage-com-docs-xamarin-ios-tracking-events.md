# Tracking Events

- URL: https://docs.webengage.com/docs/xamarin-ios-tracking-events
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.iOS
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
to track any other user interactions that are curcial for your business. Each
Custom Event
can further be defined by Event Attributes like price, quantity, category and so on. Such granular data enables you to engage users through highly contextual and personalized campaigns through all the
channels of engagement
.
Tracking Custom Events
All Event related APIs are part of WebEngage Xamarin.iOS SDK's
Analytics
object. Here's how you can get an instance of the WebEngage
Analytics
object:
C#
// import WebEngage SDK
using WebEngageXamariniOS;

// Get an instance of ‘Analytics’ object
Analytics weAnalytics = WebEngage.SharedInstance().Analytics;
Guidelines
Here are a few things to keep in mind:
WebEngage sends all events data periodically in batches to minimize network usage and maximize mobile battery life for your users.
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
NSString
,
NSNumber
,
Boolean
,
NSDate
,
NSMutableArray
and
NSDictionary
.
You can create a maximum of 25
Event Attributes
of each data type for a
Custom Event.
If an
Event Attribute
value is
NSMutableArray
or
NSDictionary
, then it cannot be used to create segments. It can only be used to personalize campaigns.
The first datapoint synced to WebEngage defines the data type for that event attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Event Attribute
data will stop flowing to your WebEngage dashboard.
After WebEngage has been successfully initialized, you can track a
Custom Event
in the following manner:
C#
weAnalytics.TrackEventWithName("Product - Page Viewed");
Tracking Event Attributes
You can use
NSDictionary
to specify a
Custom Event Attribute
and attach it to the
Custom Event
for which you'd like to track it, in the following manner:
C#
var addedToCartAttributes = new NSDictionary("Product ID", 1337, 
 "Price", 39.80, 
 "Quantity", 1, 
 "Product", "Givenchy Pour Homme Cologne",
 "Category", "Fragrance",
 "Currency", "USD",
 "Discounted", true
 );
weAnalytics.TrackEventWithName("Added to Cart", addedToCartAttributes);

var orderPlacedAttributes = new NSDictionary("Amount", 808.48, 
 "Product 1 SKU Code", "UHUH799", 
 "Product 1 Name", "Armani Jeans", 
 "Product 1 Price", 300.49,
 "Product 1 Size", "L",
 "Product 2 SKU Code", "FBHG746",
 "Product 2 Name", "Hugo Boss Jacket",
 "Product 2 Price", 507.99,
 "Product 2 Size", "L",
 "Delivery Date", NSCalendar.CurrentCalendar.DateFromComponents(new NSDateComponents
 {
 Day = 29,
 Month = 4,
 Year = 2001
 }),
 "Delivery City", "San Francisco",
 "Delivery ZIP", "94121",
 "Coupon Applied", "BOGO17"
 );
weAnalytics.TrackEventWithName("Order Placed", orderPlacedAttributes);
###Tracking Complex Event Attributes
WebEngage allows you to pass complex event attributes as
NSMutableArray
and
NSDictionary
data types. You will be able to use this data to personalize campaigns, as shown below. However, you will not be able to use complex attributes for creating segments.
Click to enlarge
Here's how you can pass
Complex Event Attributes
along with a
Custom Event
to your WebEngage account:
C#
using WebEngageXamariniOS;

var detailsProduct1 = new NSDictionary("Size", "L");

var product1 = new NSDictionary("SKU Code", "UHUH799",
 "Product Name", "Armani Jeans",
 "Price", 300.49,
 "Details", detailsProduct1
 );
var detailsProduct2 = new NSDictionary("Size", "L");

var product2 = new NSDictionary("SKU Code", "FBHG746",
 "Product Name", "Hugo Boss Jacket",
 "Price", 507.99,
 "Details", detailsProduct2
 );
var deliveryAddress = new NSDictionary("City", "San Francisco", 
 "ZIP", "94121"
 );
var products = new NSMutableArray<NSDictionary>(product1, product2);

var orderPlacedAttributes = new NSDictionary("Products", products,
 "Delivery Address", deliveryAddress,
 "Coupons Applied", new NSMutableArray<NSString>(new NSString("BOGO17"), new NSString("BGH025"))
 );
weAnalytics.TrackEventWithName("Order Placed", orderPlacedAttributes);
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
