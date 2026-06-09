# Tracking Events

- URL: https://docs.webengage.com/docs/ios-tracking-events
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
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
All event related APIs are part of WebEngage iOS SDK's
WEGAnalytics
object. Here's how you get an instance of the WebEngage
WEGAnalytics
object:
Swift
Objective-C
import WebEngage
let weAnalytics: WEGAnalytics = WebEngage.sharedInstance().analytics
// import WebEngage ‘Analytics’
#import <WebEngage/WEGAnalytics.h>

// Get an instance of ‘Analytics’ object
id<WEGAnalytics> weAnalytics = [WebEngage sharedInstance].analytics;
Guidelines
Here are a few things to keep in mind:
WebEngage sends all events data periodically in batches to minimize network usage and maximize mobile battery life for your users.
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
NSString
,
NSNumber
,
NSDate
,
NSArray
. You can also add
Boolean
attributes since its wrapped type is
NSNumber
.
You can create a maximum of 25
Event Attributes
of each data type for a
Custom Event.
If an
Event Attribute
value is
NSArray
or
NSDictionary
, then it cannot be used to create segments. It can only be used to personalize campaigns.
The first datapoint synced to WebEngage defines the data type for that event attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Event Attribute
data will stop flowing to your WebEngage dashboard.
After WebEngage has been successfully initialized, you can track a
Custom Event
in the following manner:
Swift
Objective-C
weAnalytics.trackEvent(withName: "Product - Page Viewed")
[weAnalytics trackEventWithName:@"Product - Page Viewed"];
Tracking Event Attributes
You can use
NSDictionary
to specify a
Custom Event Attribute
and attach it to the
Custom Event
for which you'd like to track it, in the following manner:
Swift
Objective-C
let addedToCartAttributes: [String:Any] = [
 "Product ID": 1337, 
 "Price": 39.80, 
 "Quantity": 1, 
 "Product": "Givenchy Pour Homme Cologne", 
 "Category": "Fragrance", 
 "Currency": "USD",
 "Is Premium": true
]
weAnalytics.trackEvent(withName: "Added to Cart", andValue: addedToCartAttributes)

var comps = DateComponents()
comps.day = 6
comps.month = 10
comps.year = 2017
let deliveryDate: Date = Calendar.current.date(from: comps)!
let orderPlacedAttributes : [String:Any] = [
 "Amount": 808.48, 
 "Product 1 SKU Code": "UHUH799", 
 "Product 1 Name": "Armani Jeans", 
 "Product 1 Price": 300.49, 
 "Product 1 Size": "L", 
 "Product 2 SKU Code": "FBHG746", 
 "Product 2 Name": "Hugo Boss Jacket", 
 "Product 2 Price": 507.99, 
 "Product 2 Size": "L", 
 "Delivery Date": deliveryDate, 
 "Delivery City": "San Francisco", 
 "Delivery ZIP": "94121", 
 "Coupon Applied": "BOGO17"
]
weAnalytics.trackEvent(withName: "Order Placed", andValue: orderPlacedAttributes)
NSDictionary *addedToCartAttributes=@{
 @"Product ID":@1337,
 @"Price":@39.80,
 @"Quantity":@1,
 @"Product":@"Givenchy Pour Homme Cologne",
 @"Category":@"Fragrance",
 @"Currency":@"USD",
 @"Is Premium":@YES
};
[weAnalytics trackEventWithName:@"Added to Cart" andValue:addedToCartAttributes];

NSDateComponents *comps = [[NSDateComponents alloc] init];
 [comps setDay:6];
 [comps setMonth:10];
 [comps setYear:2017];
 NSDate *deliveryDate = [[NSCalendar currentCalendar] dateFromComponents:comps];

NSDictionary *orderPlacedAttributes = @{
 @"Amount":@808.48,
 @"Product 1 SKU Code":@"UHUH799",
 @"Product 1 Name":@"Armani Jeans",
 @"Product 1 Price":@300.49,
 @"Product 1 Size":@"L",
 @"Product 2 SKU Code":@"FBHG746",
 @"Product 2 Name":@"Hugo Boss Jacket",
 @"Product 2 Price":@507.99,
 @"Product 2 Size":@"L",
 @"Delivery Date":deliveryDate,
 @"Delivery City":@"San Francisco",
 @"Delivery ZIP":@"94121",
 @"Coupon Applied":@"BOGO17"
};
[weAnalytics trackEventWithName:@"Order Placed" andValue:orderPlacedAttributes];
Tracking Complex Event Attributes
WebEngage allows you to pass complex event attributes as
NSArray
and
NSDictionary
data types. You will be able to use this data to personalize campaigns, as shown below. However, you will not be able to use complex attributes for creating segments.
Click to enlarge
Here's how you can pass
Complex Event Attributes
along with a
Custom Event
to your WebEngage account:
Swift
Objective-C
let detailsProduct1 = ["Size": "L"]
let product1 : [String:Any] = ["SKU Code": "UHUH799", "Product Name": "Armani Jeans", "Price": 300.49, "Details": detailsProduct1]
let detailsProduct2 = ["Size": "L"]
let product2 : [String:Any] = ["SKU Code": "FBHG746", "Product Name": "Hugo Boss Jacket", "Price": 507.99, "Details": detailsProduct2]
let deliveryAddress = ["City": "San Francisco", "ZIP": "94121"]
var orderPlacedAttributes = ["Products": [product1, product2], "Delivery Address": deliveryAddress, "Coupons Applied": ["BOGO17"]]
weAnalytics.trackEvent(withName: "Order Placed", andValue: orderPlacedAttributes)
NSDictionary *detailsProduct1=@{
 @"Size":@"L"
};

NSDictionary *product1=@{
 @"SKU Code":@"UHUH799",
 @"Product Name":@"Armani Jeans",
 @"Price":@300.49,
 @"Details":detailsProduct1
};

NSDictionary *detailsProduct2=@{
 @"Size":@"L"
};

NSDictionary *product2=@{
 @"SKU Code":@"FBHG746",
 @"Product Name":@"Hugo Boss Jacket",
 @"Price":@507.99,
 @"Details":detailsProduct2
};

NSDictionary *deliveryAddress=@{
 @"City":@"San Francisco",
 @"ZIP":@"94121"
};

NSDictionary *orderPlacedAttributes=@{
 @"Products":@[product1, product2],
 @"Delivery Address":deliveryAddress,
 @"Coupons Applied":@[@"BOGO17"]
};

[weAnalytics trackEventWithName:@"Order Placed" andValue:orderPlacedAttributes];
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
