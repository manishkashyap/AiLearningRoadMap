# Tracking Events

- URL: https://docs.webengage.com/docs/android-tracking-events
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
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
🚧
Important!
Please note that the attribute,
sdk_id
(referred to as 'Platform' on your WebEngage dashboard) of
Custom Events
signifies the SDK type.
sdk_id
1 = Web
sdk_id
2 = Android
sdk_id
3 = iOS
Tracking Custom Events
All Events related APIs are part of WebEngage Android SDK's
Analytics
object. Here's how you can get an instance of the WebEngage
Analytics
object:
Java
Kotlin
// import WebEngage ‘Analytics’
import com.webengage.sdk.android.Analytics;

// Get an instance of ‘Analytics’ object
Analytics weAnalytics = WebEngage.get().analytics();
// import WebEngage ‘Analytics’
import com.webengage.sdk.android.Analytics;

// Get an instance of ‘Analytics’ object
val weAnalytics = WebEngage.get().analytics()
Guidelines
Here are a few things to keep in mind:
WebEngage sends all events data periodically in batches to minimize network usage and maximize mobile battery life for your users.
(How to Set Event Priority)
Custom Event
and
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
, all subclasses of
Number
,
Boolean
,
Date
,
List
,
Map
.
You can create a maximum of 25
Event Attributes
of each data type for a
Custom Event.
If an
Event Attribute
value is
List
or
Map
, then it cannot be used to create segments. It can only be used to personalize campaigns.
The first datapoint synced to WebEngage defines the data type for that event attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Event Attribute
data will stop flowing to your WebEngage dashboard.
After WebEngage has been successfully initialized, you can track a
Custom Event
in the following manner:
Java
weAnalytics.track("Product - Page Viewed");
Tracking Event Attributes
You can use a
Map
to specify a
Custom Event Attribute
and attach it to the
Custom Event
for which you'd like to track it, in the following manner:
Java
Kotlin
Map<String, Object> addedToCartAttributes = new HashMap<>();
addedToCartAttributes.put("Product ID", 1337);
addedToCartAttributes.put("Price", 39.80);
addedToCartAttributes.put("Quantity", 1);
addedToCartAttributes.put("Product", "Givenchy Pour Homme Cologne");
addedToCartAttributes.put("Category", "Fragrance");
addedToCartAttributes.put("Currency", "USD");
addedToCartAttributes.put("Discounted", true);

weAnalytics.track("Added to Cart", addedToCartAttributes);

Map<String, Object> orderPlacedAttributes = new HashMap<>();
orderPlacedAttributes.put("Amount", 808.48);
orderPlacedAttributes.put("Product 1 SKU Code", "UHUH799");
orderPlacedAttributes.put("Product 1 Name", "Armani Jeans");
orderPlacedAttributes.put("Product 1 Price", 300.49);
orderPlacedAttributes.put("Product 1 Size", "L");
orderPlacedAttributes.put("Product 2 SKU Code", "FBHG746");
orderPlacedAttributes.put("Product 2 Name", "Hugo Boss Jacket");
orderPlacedAttributes.put("Product 2 Price", 507.99);
orderPlacedAttributes.put("Product 2 Size", "L");
String dateStr = "2017-10-06T09:27:37Z";
SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'");
try {
 Date date = format.parse(dateStr);
 orderPlacedAttributes.put("Delivery Date", date);
} catch (ParseException e) {
 e.printStackTrace();
}
orderPlacedAttributes.put("Delivery City", "San Francisco");
orderPlacedAttributes.put("Delivery ZIP", "94121");
orderPlacedAttributes.put("Coupon Applied", "BOGO17");

weAnalytics.track("Order Placed", orderPlacedAttributes);
val addedToCartAttributes: MutableMap<String, Any> = HashMap()
 addedToCartAttributes["Product ID"] = 1337
 addedToCartAttributes["Price"] = 39.80
 addedToCartAttributes["Quantity"] = 1
 addedToCartAttributes["Product"] = "Givenchy Pour Homme Cologne"
 addedToCartAttributes["Category"] = "Fragrance"
 addedToCartAttributes["Currency"] = "USD"
 addedToCartAttributes["Discounted"] = true

 weAnalytics.track("Added to Cart", addedToCartAttributes)

 val orderPlacedAttributes: MutableMap<String, Any> = HashMap()
 orderPlacedAttributes["Amount"] = 808.48
 orderPlacedAttributes["Product 1 SKU Code"] = "UHUH799"
 orderPlacedAttributes["Product 1 Name"] = "Armani Jeans"
 orderPlacedAttributes["Product 1 Price"] = 300.49
 orderPlacedAttributes["Product 1 Size"] = "L"
 orderPlacedAttributes["Product 2 SKU Code"] = "FBHG746"
 orderPlacedAttributes["Product 2 Name"] = "Hugo Boss Jacket"
 orderPlacedAttributes["Product 2 Price"] = 507.99
 orderPlacedAttributes["Product 2 Size"] = "L"
 val dateStr = "2017-10-06T09:27:37Z"
 val format = SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'")
 try {
 val date: Date = format.parse(dateStr)
 orderPlacedAttributes["Delivery Date"] = date
 } catch (e: ParseException) {
 e.printStackTrace()
 }
 orderPlacedAttributes["Delivery City"] = "San Francisco"
 orderPlacedAttributes["Delivery ZIP"] = "94121"
 orderPlacedAttributes["Coupon Applied"] = "BOGO17"

 weAnalytics.track("Order Placed", orderPlacedAttributes)
Tracking Complex Event Attributes
WebEngage allows you to pass complex event attributes as
List
and
Map
data types. You will be able to use this data to personalize campaigns, as shown below. However, you will not be able to use complex attributes for creating segments.
Click to enlarge
Here's how you can pass
Complex Event Attributes
along with a
Custom Event
to your WebEngage account:
Java
Kotlin
Map<String, Object> product1 = new HashMap<>();
product1.put("SKU Code", "UHUH799");
product1.put("Product Name", "Armani Jeans");
product1.put("Price", 300.49);

Map<String, Object> detailsProduct1 = new HashMap<>();
detailsProduct1.put("Size", "L");
product1.put("Details", detailsProduct1);

Map<String, Object> product2 = new HashMap<>();
product2.put("SKU Code", "FBHG746");
product2.put("Product Name", "Hugo Boss Jacket");
product2.put("Price", 507.99);

Map<String, Object> detailsProduct2 = new HashMap<>();
detailsProduct2.put("Size", "L");
product2.put("Details", detailsProduct2);

Map<String, Object> deliveryAddress = new HashMap<>();
deliveryAddress.put("City", "San Francisco");
deliveryAddress.put("ZIP","94121");

Map<String, Object> orderPlacedAttributes = new HashMap<>();
orderPlacedAttributes.put("Products", Arrays.asList(product1, product2));
orderPlacedAttributes.put("Delivery Address", deliveryAddress);
orderPlacedAttributes.put("Coupons Applied", Arrays.asList("BOGO17"));

weAnalytics.track("Order Placed", orderPlacedAttributes);
val product1: MutableMap<String, Any> = HashMap()
 product1["SKU Code"] = "UHUH799"
 product1["Product Name"] = "Armani Jeans"
 product1["Price"] = 300.49

 val detailsProduct1: MutableMap<String, Any> = HashMap()
 detailsProduct1["Size"] = "L"
 product1["Details"] = detailsProduct1

 val product2: MutableMap<String, Any> = HashMap()
 product2["SKU Code"] = "FBHG746"
 product2["Product Name"] = "Hugo Boss Jacket"
 product2["Price"] = 507.99

 val detailsProduct2: MutableMap<String, Any> = HashMap()
 detailsProduct2["Size"] = "L"
 product2["Details"] = detailsProduct2

 val deliveryAddress: MutableMap<String, Any> = HashMap()
 deliveryAddress["City"] = "San Francisco"
 deliveryAddress["ZIP"] = "94121"

 val orderPlacedAttributes: MutableMap<String, Any> = HashMap()
 orderPlacedAttributes["Products"] = Arrays.asList(product1, product2)
 orderPlacedAttributes["Delivery Address"] = deliveryAddress
 orderPlacedAttributes["Coupons Applied"] = Arrays.asList("BOGO17")

 weAnalytics.track("Order Placed", orderPlacedAttributes)
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
Java
Kotlin
weAnalytics.track("Checkout Started", new Analytics.Options().setHighReportingPriority(true));
weAnalytics.track("Checkout Started", Analytics.Options().setHighReportingPriority(true))
The WebEngage SDK reports such events immediately (provided network connectivity is available), and does not batch them with events whose priority is not set to high.
You can also set high priority for events that have attributes attached to them, in the following manner:
Java
Kotlin
Map<String, Object> checkoutStartedAttributes = new HashMap<>();
checkoutStartedAttributes.put("Cart ID", 35651);
checkoutStartedAttributes.put("Cart Size", 3);
checkoutStartedAttributes.put("Cart Value", 445.59);
checkoutStartedAttributes.put("Cart Category", "Women Dresses");

weAnalytics.track("Added to Cart", checkoutStartedAttributes, new Analytics.Options().setHighReportingPriority(true));
val checkoutStartedAttributes: MutableMap<String, Any> = HashMap()
 checkoutStartedAttributes["Cart ID"] = 35651
 checkoutStartedAttributes["Cart Size"] = 3
 checkoutStartedAttributes["Cart Value"] = 445.59
 checkoutStartedAttributes["Cart Category"] = "Women Dresses"

 weAnalytics.track(
 "Added to Cart",
 checkoutStartedAttributes,
 Analytics.Options().setHighReportingPriority(true)
 )
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
