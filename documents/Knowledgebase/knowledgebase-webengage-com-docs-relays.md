# Relays

- URL: https://knowledgebase.webengage.com/docs/relays
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Relays
What are Relays?
Relays helps businesses engage their users based on the occurrence of a business event. Just like you’re able to trigger a series of workflow based communication in journeys based on something that the user did eg. user did an event, user entered/exited a segment, user entered/exited a geo-fence etc., you will be able to trigger a series of workflow based communication in relays based on “something that the business did”.
Let’s understand this better through a couple of examples.
Example 1
Netflix wants to send a series of mobile push notifications and emails to its customers whenever a new series is added. In addition, Netflix wants the communication to be contextual so that a customer who likes watching
Comedy
gets notifications only when a new
Comedy
series is added. Similarly, a customer who likes watching
Action
gets notifications only when a new
Action
series is added. Please note that the event here,
New Series Added
, is an event at the business’ end. The customer has not triggered this event in any way.
Now, how should Netflix reach out to its customers whenever a new series is added?
Should it send a new campaign each time a new series is added? How about the case where it wants to engage its customers whenever a new episode is added? Wouldn’t this result in multiple such campaigns in a day given that there are hundreds of new episodes getting added on Netflix daily?
Also, should Netflix send this communication to all its users whenever a new series is added? Or should it send it only to a segment of users? Furthermore, how can Netflix make this entire communication contextual so that a user only receives communication that is relevant to them?
Example 2
A customer searches for a particular product on Amazon.com. Unfortunately the product was out of stock. However, Amazon asked the customer whether they would like to be notified if this product was added back in stock some time in the future. The customer agreed to be notified. Now, whenever this particular product is back in stock, Amazon wants to send this customer a notification or a series of notifications on one or more channels such as mobile push, email, SMS etc. to inform them that the item is back in stock. Please note that these notifications will get triggered based on the trigger event
Product Back in Stock
which is an event at the business’ end.
The above scenario was only for one particular product in Amazon’s entire catalog. Imagine this scenario for millions of Amazon’s product for hundreds of millions of its customers.
Very complicated? It is.
This is why we built
Relays
. Relays helps you automate your customer marketing based on business events.
What are Business Events?
While we’ve covered the explanation of
Business Events
in the examples above, let’s define it in a bit more detail here.
So far you’ve come across two types of events in WebEngage:
System Events
: Events that WebEngage can automatically understand such as app installed, email opened, push notification clicked etc.
Custom Events
: Events defined by you that are relevant to your business eg. added to cart, searched for product, purchase completed etc.
Business Events
is the third type of event that covers the entire gamut of actions that happen at the business’ end. All the events you see below are examples of actions (or events) that happen at the business’ end.
E-commerce
Travel
Ed-Tech
Media / OTT
Price drop
Price drop
New course added
New episode added
New arrivals
Flight rescheduled
New tutorial added
New season added
Back in stock
Flight delayed
New instructor added
New series added
Stocking running out
Rooms running out
New centre launched
New film added
As a marketer, you can probably imagine a series of workflow based communication for each of the examples above!
Just like a
System Event
and a
Custom Event
, a
Business Event
also has a number of attributes. Let’s understand this better through our previous example of Netflix’s business event
New Series Added
. This event will have a number of attributes as you can see in the table below:
Attribute Name
Attribute Data Type
Example of Attribute Value
Series Name
String
Stranger Things
Genre
String
Drama
Number of Seasons
Number
3
Cover Photo URL
String
https://www.netflix.com/st.png
Release Date
Date
2019-07-15
For Paid Users Only
Boolean
True
Now that you understand the concept of relays and business events, let’s get started on how you can create relays in WebEngage.
Updated
6 months ago
So, what's next?
Getting Started
Copy Page
