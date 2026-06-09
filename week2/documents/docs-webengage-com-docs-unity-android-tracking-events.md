# Tracking Events

- URL: https://docs.webengage.com/docs/unity-android-tracking-events
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Unity.Android
Tracking Events
Track crucial user-app interactions as Custom Events to engage them with contextually relevant messages
🚧
Must Read
We recommend that you get yourself acquainted with the concept of
System Events
,
Custom Events
and their attributes before proceeding.
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
As shown below,
Custom Events
can be tracked using the
WebEngage.TrackEvent
method of our
Unity.Android SDK.
C#
using WebEngageBridge;
 ...

 // Track simple event
 WebEngage.TrackEvent("Product - Page Viewed");
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
You can create a maximum of 25
Event Attributes
of each data type for a
Custom Event.
The first datapoint synced to WebEngage defines the data type for that event attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Event Attribute
data will stop flowing to your WebEngage dashboard.
Tracking Event Attributes
You can track
Event Attributes
along with a
Custom Event
in the following manner:
C#
using WebEngageBridge;
 ...

 // Track event with attributes
 Dictionary<string, object> orderPlacedAttributes = new Dictionary<string, object>();
 orderPlacedAttributes.Add("Amount", 808.48);
 orderPlacedAttributes.Add("Product 1 SKU Code", "UHUH799");
 orderPlacedAttributes.Add("Product 1 Name", "Armani Jeans");
 orderPlacedAttributes.Add("Product 1 Price", 300.49);
 orderPlacedAttributes.Add("Product 1 Size", "L");
 orderPlacedAttributes.Add("Product 2 SKU Code", "FBHG746");
 orderPlacedAttributes.Add("Product 2 Name", "Hugo Boss Jacket");
 orderPlacedAttributes.Add("Product 2 Price", 507.99);
 orderPlacedAttributes.Add("Product 2 Size", "L");
 orderPlacedAttributes.Add("Delivery Date", System.DateTime.ParseExact("2017-10-21 09:27:37.100", "yyyy-MM-dd hh:mm:ss.fff", null));
 orderPlacedAttributes.Add("Delivery City", "San Francisco");
 orderPlacedAttributes.Add("Delivery ZIP", "94121");
 orderPlacedAttributes.Add("Coupon Applied", "BOGO17");
 WebEngage.TrackEvent("Order Placed", orderPlacedAttributes);
Tracking Complex Events
WebEngage allows you to pass complex event attributes as
Array
and
Object
data types. You will be able to use this data to personalize campaigns. However, you will not be able to use complex attributes for creating segments.
For example, in the below code snippet, we're tracking event attributes of the event,
Order Placed
, where 2 products have been purchased by a user.
C#
using WebEngageBridge;
 ...
 
 // Track complex event
 Dictionary<string, object> product1 = new Dictionary<string, object>();
 product1.Add("SKU Code", "UHUH799");
 product1.Add("Product Name", "Armani Jeans");
 product1.Add("Price", 300.49);

 Dictionary<string, object> detailsProduct1 = new Dictionary<string, object>();
 detailsProduct1.Add("Size", "L");
 product1.Add("Details", detailsProduct1);

 Dictionary<string, object> product2 = new Dictionary<string, object>();
 product2.Add("SKU Code", "FBHG746");
 product2.Add("Product Name", "Hugo Boss Jacket");
 product2.Add("Price", 507.99);

 Dictionary<string, object> detailsProduct2 = new Dictionary<string, object>();
 detailsProduct2.Add("Size", "L");
 product2.Add("Details", detailsProduct2);

 Dictionary<string, object> deliveryAddress = new Dictionary<string, object>();
 deliveryAddress.Add("City", "San Francisco");
 deliveryAddress.Add("ZIP", "94121");

 Dictionary<string, object> orderPlacedAttributes = new Dictionary<string, object>();
 List<object> products = new List<object>();
 products.Add(product1);
 products.Add(product2);

 List<string> coupons = new List<string>();
 coupons.Add("BOGO17");

 orderPlacedAttributes.Add("Products", products);
 orderPlacedAttributes.Add("Delivery Address", deliveryAddress);
 orderPlacedAttributes.Add("Coupons Applied", coupons);

 WebEngage.TrackEvent("Order Placed", orderPlacedAttributes)
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
