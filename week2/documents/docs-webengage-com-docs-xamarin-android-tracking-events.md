# Tracking Events

- URL: https://docs.webengage.com/docs/xamarin-android-tracking-events
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Xamarin.Android
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
WebEngage starts tracking some events automatically as soon as you
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
can further be defined by
Event Attributes like price, quantity, category
and so on. Such granular data enables you to engage users through highly contextual and personalized campaigns through all the
channels of engagement
.
Tracking Custom Events
All Events related APIs are part of WebEngage Xamarin.Android SDK's
Analytics
object. Here's how you can get an instance of the WebEngage
Analytics
object:
C#
// import WebEngage SDK
using Com.Webengage.Sdk.Android;
...
 
// Get an instance of ‘Analytics’ object
Analytics weAnalytics = WebEngage.Get().Analytics();
Guidelines
Here are a few things to keep in mind:
WebEngage sends all events data periodically in batches to minimize network usage and maximize mobile battery life for your users.
(How to Set Event Priority)
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
can be of these data types: String ,
Java.Lang.Boolean
,
Java.Util.Date
,
Java.Lang.Number
,
IList<Java.Lang.Object>
and
IDictionary<string, Java.Lang.Object>
.
You can create a maximum of 25
Event Attributes
of each data type for a
Custom Event.
If an
Event Attribute
value is
IList<Java.Lang.Object>
or
IDictionary<string, Java.Lang.Object>
, then it cannot be used to create segments. It can only be used to personalize campaigns.
The first datapoint synced to WebEngage defines the data type for that event attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Event Attribute
data will stop flowing to your WebEngage dashboard.
After WebEngage has been successfully initialized, you can track a
Custom Event
in the following manner:
C#
weAnalytics.Track("Product - Page Viewed");
Tracking Event Attributes
You can use
IDictionary<string, Java.Lang.Object>
to specify a
Custom Event Attribute
and attach it to the
Custom Event
for which you'd like to track it, in the following manner:
C#
using Java.Lang;
...

IDictionary<string, Object> addedToCartAttributes = new Dictionary<string, Object>();
addedToCartAttributes.Add("Product ID", 1337);
addedToCartAttributes.Add("Price", 39.80);
addedToCartAttributes.Add("Quantity", 1);
addedToCartAttributes.Add("Product", "Givenchy Pour Homme Cologne");
addedToCartAttributes.Add("Category", "Fragrance");
addedToCartAttributes.Add("Currency", "USD");
addedToCartAttributes.Add("Discounted", true);

weAnalytics.Track("Added to Cart", addedToCartAttributes);

IDictionary<string, Object> orderPlacedAttributes = new Dictionary<string, Object>();
orderPlacedAttributes.Add("Amount", 808.48);
orderPlacedAttributes.Add("Product 1 SKU Code", "UHUH799");
orderPlacedAttributes.Add("Product 1 Name", "Armani Jeans");
orderPlacedAttributes.Add("Product 1 Price", 300.49);
orderPlacedAttributes.Add("Product 1 Size", "L");
orderPlacedAttributes.Add("Product 2 SKU Code", "FBHG746");
orderPlacedAttributes.Add("Product 2 Name", "Hugo Boss Jacket");
orderPlacedAttributes.Add("Product 2 Price", 507.99);
orderPlacedAttributes.Add("Product 2 Size", "L");
orderPlacedAttributes.Add("Delivery Date", new Date("2017-10-21T09:27:37Z"));
orderPlacedAttributes.Add("Delivery City", "San Francisco");
orderPlacedAttributes.Add("Delivery ZIP", "94121");
orderPlacedAttributes.Add("Coupon Applied", "BOGO17");

weAnalytics.Track("Order Placed", orderPlacedAttributes);
Complex Event Attributes
WebEngage allows you to pass complex event attributes as
IList<Java.Lang.Object>
and
IDictionary<string, Java.Lang.Object>
data types. You will be able to use these complex attributes to personalize campaigns, as shown below. However, you will not be able to use complex attributes for creating segments.
Click to enlarge
You can pass complex event attributes in the following manner:
C#
using Java.Lang;
using Android.Runtime;
...

IDictionary<string, Object> product1 = new JavaDictionary<string, Object>();
product1.Add("SKU Code", "UHUH799");
product1.Add("Product Name", "Armani Jeans");
product1.Add("Price", 300.49);

JavaDictionary<string, Object> detailsProduct1 = new JavaDictionary<string, Object>();
detailsProduct1.Add("Size", "L");
product1.Add("Details", detailsProduct1);

IDictionary<string, Object> product2 = new JavaDictionary<string, Object>();
product2.Add("SKU Code", "FBHG746");
product2.Add("Product Name", "Hugo Boss Jacket");
product2.Add("Price", 507.99);

JavaDictionary<string, Object> detailsProduct2 = new JavaDictionary<string, Object>();
detailsProduct2.Add("Size", "L");
product2.Add("Details", detailsProduct2);

IDictionary<string, Object> deliveryAddress = new JavaDictionary<string, Object>();
deliveryAddress.Add("City", "San Francisco");
deliveryAddress.Add("ZIP", "94121");

JavaDictionary<string, Object> orderPlacedAttributes = new JavaDictionary<string, Object>();
JavaList<Object> products = new JavaList<Object>();
products.Add(product1);
products.Add(product2);

JavaList<string> coupons = new JavaList<string>();
coupons.Add("BOGO17");

orderPlacedAttributes.Add("Products", products);
orderPlacedAttributes.Add("Delivery Address", deliveryAddress);
orderPlacedAttributes.Add("Coupons Applied", coupons);

weAnalytics.Track("Order Placed", orderPlacedAttributes);
Event Priority
Events accumulate over time, and WebEngage sends events in batches periodically to minimize network usage and maximize battery life of the device. Event priority allows you to override this behaviour of the SDK.
Since high priority events are reported more frequently than batched events, it will cause your app to drain your user's device battery faster. Hence, we stronly recommend that you user this feature sparingly.
setHighReportingPriority
works only when
reporting strategy is set to
BUFFER
. In case reporting strategy is set to
FORCE_SYNC
, all your events will be reported at high priority by default.
You can set any particular event's priority to 'high' in the following manner:
C#
weAnalytics.Track("Checkout Started", new Analytics.Options().SetHighReportingPriority(true));
The WebEngage SDK reports such events immediately (provided network connectivity is available), and does not batch them with events whose priority is not set to high.
You can also set high priority for events that have attributes attached to them, in the following manner:
C#
IDictionary<string, Object> checkoutStartedAttributes = new Dictionary<string, Object>();
checkoutStartedAttributes.Add("Cart ID", 35651);
checkoutStartedAttributes.Add("Cart Size", 3);
checkoutStartedAttributes.Add("Cart Value", 445.59);
checkoutStartedAttributes.Add("Cart Category", "Women Dresses");

weAnalytics.Track("Added to Cart", checkoutStartedAttributes, new Analytics.Options().SetHighReportingPriority(true));
Please feel free to drop in a few lines at
[email protected]
or get in touch with your
Onboarding Manager
in case you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
Push messaging
Copy Page
