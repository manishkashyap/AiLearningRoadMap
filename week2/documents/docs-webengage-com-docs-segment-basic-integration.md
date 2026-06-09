# Cloud Mode (Basic) Integration

- URL: https://docs.webengage.com/docs/segment-basic-integration
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Partners Integrations
Segment.com
Cloud Mode (Basic) Integration
🚧
Must Read
We recommend that you get yourself acquainted with all the concepts related to
Users
and
Events
before proceeding. Doing so will help you understand the workings of this section, better.
Referred to as
Cloud Mode
in
Segment.com, Basic Integration
enables you to receive all the user data and events data in your WebEngage account from your website, mobile apps, and server.
However, integration via this method does not support
Push
and
In-app Messaging.
Hence, we recommend that you configure
Advanced Integration
if you'd like to engage app users through WebEngage.
Currently, WebEngage supports the following Segment APIs -
track
,
identify
and
page
.
Identify:
When a user is identified,
Segment
will send that user's information to WebEngage, wherein a user will be created/updated. The
anonymousId
must be present in the case of an anonymous user and
userId
in case of an identified user.
Page:
This is only supported on the client-side. Sending page events via server-side integration is not supported.
Guidelines
Your data must be sent in a specific format through Segment to ensure that our backend systems understand it correctly. Here are a few guidelines to help you out:
For Tracking User Attributes
A few things to keep in mind:
User Attribute
names are case sensitive and must be less than 50 characters long.
String
attribute values must be less than 1000 characters long. Additional characters will be truncated.
You can create a maximum of 25
Custom User Attributes
of each data type.
userAttributeName
must not start with
we_
. Names starting with
we_
are reserved exclusively for internal use at WebEngage. Thus, to avoid data contamination for your account, such data will be ignored if used for your
Custom User Attributes.
The first datapoint synced to WebEngage defines the data type for that user attribute. Thus, data types must be consistent with the value that you want to store against the attribute. If the data type is changed at a later date, then
Custom Users Attribute
data will stop flowing to your WebEngage dashboard.
For Tracking Events
A few things to keep in mind:
Custom Event
names must be less than 50 characters long.
Event Attribute
values can be
Boolean
,
Number
,
String
and
Date
data types.
Event Attribute
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
Event Attribute
data will stop flowing to your WebEngage dashboard.
Website Integration
Here's how you can integrate your website with WebEngage:
Step 1:
Enter your domain name for which you're performing the Website SDK integration on the WebEngage dashboard under
Integrations > SDK > Website
.
Step 2:
Log in to your Segment.com account and go to the relevant workspace.
Step 3:
Click on
Add Destination
and search for
WebEngage
in the
Destinations Catalog.
Step 4:
Click on
WebEngage
, select
JavaScript
as the source and click
Confirm Source.
Step 5:
Enter your WebEngage
License Code
.
Leave the field,
API Key
blank.
And you're all set! You can now
test the integration
and configure channels to start engaging users.
Android/ iOS/ Server Integration
Please follow these steps for integrating your Android apps, iOS apps, and Server with your WebEngage account:
Step 1:
Log in to your Segment.com account and go to the relevant workspace.
Step 2:
Click on
Add Destination
and search for
WebEngage
in the
Destinations Catalog.
Step 3:
Click on
WebEngage
, select
Android/ iOS/ Server
as the source and click
Confirm Source.
You can integrate only one source at once, hence you will need to repeat these steps for integrating other sources.
Step 4:
Enter your WebEngage
API Key
.
Leave the field,
License Code
blank.
And you're good to go! You can now
test the integration
and configure channels to start engaging users.
Please feel free to drop in a few lines at
[email protected]
or get in touch with your
Onboarding Manager
in case you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
Complete the one-time channel configuration to start engaging users!
SMS
On-site
Web Push
Email
WhatsApp
Facebook
Copy Page
