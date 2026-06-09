# FAQ

- URL: https://knowledgebase.webengage.com/docs/web-push-notification-faq
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

FAQ
Commonly asked questions related to Web Push campaigns
Campaign Creation
Your dashboard comes with a highly-intuitive 6-step campaign creation interface that enables you to customize, personalize and test your messages with great ease. Here are a few questions that are frequently asked by our clients:
1. Which OS & Browsers support the Layouts available in my dashboard?
You can leverage the following layouts to create highly effective
Browser Push Notifications
:
Layout
Personalized Image
Buttons
Personalized Title & Message
Personalized Icon
Text
No
Yes (2)
Yes
Yes
Banner
Yes
Yes (2)
Yes
Yes
Both Layouts are compatible with all the Browser-OS combinations that support
Web Push Notifications.
Here's a
Browser x OS compatibility map
to help you plan your Web Push engagement strategy as per each
Segment's
technological preferences:
Device OS
Browsers that support Web Push
Android (Mobile + Tablet)
Chrome 50+, Firefox 44+, Opera 46+
Windows
Chrome 48+, Firefox 44+, Opera 42+, Edge 17+
iOS (Mobile + Tablet)
Safari 16+ (If PWA is created)
Mac OS X
Chrome 48+, Firefox 44+, Opera 42+
Max OS 16.4
Safari 16, Chrome, Firefox
Linux
Chrome 48+, Firefox 44+, Opera 42+
Here's a
Layout Element - Browser x OS compatibility map
to help you understand the limitations of all major OS and browsers preferred by users to receive
Web Push Notifications:
Browser x OS
Title Char. Limit
Message Character Limit
Custom Buttons
Icon
Banner Image
Chrome
x
Android
47
49
(95 if no Banner Image)
Yes
Yes
Yes
Chrome
x
Windows 9
57
126
Yes
Yes
Yes
Chrome
x
Windows 10+
67
159
Yes
Yes
Yes
Chrome
x
Mac OS X
27
27
No
Yes (not supported from 16+)
No
Firefox
x
Android
48
555
No
Yes
No
Firefox
x
Windows 9
54
200
No
Yes
No
Firefox
x
Windows 10+
52
135
No
Yes
No
Firefox
x
Mac OS X
37
42
No
Yes (not supported from 16+)
No
Safari
x
Mac OS 16+
40
90
No
No
No
Safari
x
iOS 16.4+
40
90
No
No (PWA icon only)
No
However, given the varying number of characters supported by each Browser-OS combination, we've compiled a few neutral guidelines to ensure that your message is visible across most:
Web Push Text Guidelines.
2. How can we target specific devices and browsers?
You can easily create
Web Push Notifications
targeted at users with specific device, browser or OS preferences by grouping them into a
Segment
.
As shown below, this can be achieved by adding parameters under the section,
Technology
while creating the segment.
Click to enlarge
🚧
Detailed read:
Step-by-step Guide to Creating Segments
3. How can I send a notification as per each user's timezone?
You can easily schedule a
Web Push Notification
for delivery in your user's timezone by selecting
One-time
as the
Campaign Type
at
Step 2: When
.
Click to enlarge
As highlighted above:
Step 1:
Select
Later
against
Delivery Time
Step 2:
Specify the delivery date-time, select
In User's timezone
from the last dropdown and you're all set!
Step 3:
Continue building your campaign.
.
4. How can I engage users in multiple segments through Web Push?
You can easily combine multiple segments under
Step 1: Audience
while creating a campaign.
Click to enlarge
As highlighted above:
Step 1:
Select
Send to users in multiple segments and/or...
against the field,
Audience Type
Step 2:
Select the logic by which you'd like to combine the segments:
Send to only those users who are included in ALL Segments
OR
Send to users in ANY of the selected Segments
Step 3:
Continue building your campaign
Campaign Delivery, Failures & Queueing
Here are a few questions that are frequently asked by our clients:
1. What happens when Web Push Notification is sent to an offline user?
All Web Push Notifications are delivered through VAPID at WebEngage. In cases where a user is offline, the notification is
qeued for delayed delivery
as per the
Queueing Duration
specified while creating the campaign.
If a delivery window opens up within the specified duration (user comes online), then we'll deliver the message to them. If not, then the message will be dropped and will be counted towards the campaign's
Failures
stats with the reason -
Other Failures.
If
Queueing
is disabled while creating the campaign, then the message will fail to get delivered, indicated by the reason,
Other Failures (under
Web Push Campaign Overview
).
2. Why do Web Push Notifications look different on Chrome x Windows 10?
With the release of Chrome v68 in July 2018, Google Chrome now supports the native notifications system of Windows 10. This means that all users who have opted-in to your channel through Chrome v68+ through a Windows 10+ device will now experience
Web Push Notifications
like the visual below.
Click to enlarge
The notification will be displayed above the taskbar and will also appear in the Windows Action Center until a user dismisses it or clicks on it.
The banner image’s height will be cropped to 360px and will be displayed above the icon & text (120px is cropped from the bottom of the image).
The custom buttons will appear side-by-side, as shown above.
🚧
Detailed read:
Image and Text Guidelines for creating Web Push Notifications
3. Why do some Web Push Notifications fail to get delivered?
Web Push Notifications
may fail to get delivered to a few users for various reasons like,
the user has unsubscribed, the campaign was triggered through a Journey for a user who is not reachable on the channel,
and so on.
🚧
Detailed Read
Web Push Delivery Failure Reasons
Analyzing Failures for a Web Push Campaign
4. Why do some Web Push Notifications get Queued?
The term,
Queued
indicates the number of messages that have been sent to a campaign's target audience but are currently lined up for delayed delivery. This usually happens when
DND Hours
or
Frequency Capping
settings are applicable for a user.
🚧
Detailed Read
How Delivery Time is Determined for Messages that get Queued
Analyzing Queued Messages for a Web Push Campaign
How to avoid Unwanted Notifications with Machine Learning in Chrome?
Why is Chrome showing warnings for some notifications?
Chrome now uses machine learning to identify and warn users about notifications that may be spammy, deceptive, or harmful. These include prompts that could trick users into downloading suspicious software, sharing sensitive data, or making unsafe purchases.
How does Chrome detect unwanted notifications?
Chrome uses an on-device machine learning model to analyze the text content of notifications (title, body, and button text). If the model detects potentially deceptive or spam-like content, the user is shown a warning before interacting with the notification.
What happens when a notification is flagged?
When Chrome flags a notification:
You’ll see the site name and a warning message about potential spam or deception.
You can choose to unsubscribe, view the notification, or always allow notifications from that site in the future.
Does Google see my notification data?
No. All detection and analysis happen locally on your users device. Notifications are end-to-end encrypted and never sent to Google’s servers for review.
What other steps does Chrome take to protect users from harmful notifications?
Revoking permissions for abusive sites identified by Google Safe Browsing.
One-tap unsubscribe option on Android notifications.
Chrome Safety Check to review revoked permissions and manage site notification settings.
What is the goal with this ?
These updates strengthen Chrome’s ongoing commitment to user safety, privacy, and control over notifications, with possible expansion to other platforms in the future.
How to avoid notifications being marked as spam by Google Chrome?
Be honest and explicit. If the notification promotes something, say exactly what it is and who it is from.
Give control to the user. Make subscribing and unsubscribing simple and obvious.
Avoid manipulative language or high-pressure CTAs. No “
you won’t believe this
”, “
download now
”, or
fake urgency
.
Keep tech and security clean.
Good delivery + Good content = Better Reputation
.
Other Concrete Rules to Keep in Mind
Permission UX
Use a clear, contextual prompt before the browser permission request. Explain value in one short sentence.
Don’t prompt immediately on first page load. Let users interact first.
Only ask users who are likely to want updates - avoid asking everyone.
Notification content
Use the site name in every notification title or body so users know the source.
Avoid misleading headlines. The title and body must match the action the notification asks for.
Avoid deep links to downloads, installers, or payment pages from the notification itself.
Keep text simple and factual: update, reminder, order status, price drop, message from X.
Frequency and relevance
Limit volume. Don’t flood users with repeats. Set sane caps by user segment.
Personalize your content so it is relevant. Generic mass blasts are more likely to be flagged.
Technical best practices you can follow
Deliver notifications over HTTPS and follow web push standards.
Ensure correct origin, icons, and manifest details so Chrome can verify sender authenticity.
Monitor your push endpoint for errors and retry safe practices.
Reputation and safety signals
Avoid linking to low-quality or suspicious domains.
Maintain good site hygiene: clean up spammy pages, remove malicious links, fix compromises quickly.
Be responsive to abuse reports and complaints.
Privacy and data handling
Do not collect or request personal or financial details inside a notification.
Don’t use notifications to phish or ask for credentials.
Easy unsubscribe and feedback
Include an immediate one-tap unsubscribe action in the notification, or make unsubscribing a single click from the notification body.
Provide an in-app/website page explaining why a user got the notification and how to manage preferences.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries or feedback. We're always just an email away!
Updated
7 months ago
Web Push Layouts: Image & Text Guidelines
Email
Copy Page
