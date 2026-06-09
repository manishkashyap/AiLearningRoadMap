# Web Push Layouts: Image & Text Guidelines

- URL: https://knowledgebase.webengage.com/docs/web-push-image-text-specifications
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Web Push Layouts: Image & Text Guidelines
Make the most of our ready-to-use Layouts to create powerful Web Push Notifications
🚧
Please Note
This document only covers image and text specifications for the
Web Push Notification Layouts
listed in your dashboard. Please navigate to
Creating Web Push Campaigns
,
to start building your campaign from scratch.
Visual specs apply to all
Images, Icons, Badges
that are:
Uploaded directly to the dashboard.
Added through a link.
Personalized to a user by adding a
User Attribute/Event Attribute
to the respective fields.
(Regarding the last two scenarios, please host the pictures on your server/cloud account in the aspect ratios specified below.)
Text-only Layout
A text-only template, allows you to send quick updates and offers, personalized to each user's preferences and behavioral history.
(
How to customize
)
Text only Web Push Notification, as experienced by Firefox-Mac users (click to enlarge)
Text Specifications
The number of characters shown in the
Web Push Notification
depends greatly on:
The Browser x OS through which a user has subscribed.
Screen size of the device being used.
The language selected for the message.
Since it's not feasible to create separate campaigns for each Browser-OS combination, we recommend the following guidelines to ensure that the message is visible across most combinations:
Field
Max Length Recommended
Title
32 characters
Message
160 characters
Button Label
(CTA text)
22 characters
You can add up to 2 CTAs to your
Web Push Notification
through the
Buttons
section while creating the campaign.
You can easily
personalize the Title and Message
to deliver engage one-on-one with each user at scale!
Visual Specifications
Visual Element
Size & Aspect Ratio (w:h)
File Type & Size
Icon
192px by 192px
(1:1)
JPG, JPEG, PNG
(less than 1MB)
Custom Badge
(only for Chrome-Android)
72px by 72px
(1:1)
PNG, GIF, WEBP, ICO, CUR
(less than 1MB)
You can
personalize the
Icon
for each user. This could be anything like
the last product seen by them, the upcoming movie for which they've booked tickets, announcing a new episode of a show they're currently watching
and so on!
Banner Layout
A single-fold media template that allows you create visually personalized notifications with great ease.
(
How to customize
)
Banner Web Push Notification, as experienced by Chrome-Windows users (click to enlarge)
Text Specifications
The number of characters shown in the
Web Push Notification
depends greatly on:
The Browser x OS through which a user has subscribed.
Screen size of the device being used.
The language selected for the message.
Since it's not feasible to create separate campaigns for each Browser-OS combination, we recommend the following guidelines to ensure that the message is visible across most combinations:
Field
Max Length Recommended
Title
32 characters
Message
42 characters
Button Label
(CTA text)
22 characters
You can add up to 2 CTAs to your
Web Push Notification
through the
Buttons
section while creating the campaign.
You can easily
personalize the Title and Message
to deliver engage one-on-one with each user at scale!
Visual Specifications
Visual Element
Size & Aspect Ratio (w:h)
File Type & Size
Icon
192px by 192px
(1:1)
JPG, JPEG, PNG
Less than 1MB
Banner Image
(only for Chrome on Android & Windows)
*Recommended size:** 720px by 480px
(3:2)
*Minimum size:** 360px by 240px
(3:2)
JPG, JPEG, PNG
Less than 1MB
Custom Badge
(only for Chrome v53+ on Android)
72px by 72px
(1:1)
PNG, GIF
(animation is not supported),
WEBP, ICO, CUR
Less than 1MB
You can
personalize the
Icon
and
Banner Image
for each user. This could be anything like
the last product seen by them, the upcoming movie for which they've booked tickets, announcing a new episode of a show they're currently watching
and so on!
Banner Image Tips
Banner images in web push notifications get rendered differently across different devices. The banner image in a web push notification on Chrome on Android will appear different from Chrome on Windows 10 or Edge on Windows which will appear different from Chrome on previous Windows versions. There is no one standard size for the banner image that will suit all the different devices or browser/OS combinations.
Here are a few guidelines to help you engage users with visually stunning
Web Push Notifications:
👍
Pro-tip:
Avoid portrait-oriented images at all times!
1. Adding Text to a 720px by 480px Banner Image
Click to enlarge
As highlighted above, we recommend that you:
Center-align the text area.
Avoid creating a text area that takes up more than 240px in height.
(Max Textarea = 720px by 240px)
Maintain a minimum margin of 120px on the top & bottom of the text area to ensure that it renders in an optimal way across browsers and devices. (These margins will get cropped on
Chrome x Windows
10 and
Chrome x Android.)
2. Adding Text to a 360px by 240px Banner Image
Click to enlarge
As highlighted above, we recommend that you:
Center-align the text area.
Avoid creating a text area that takes up more than 120px in height.
(Max Textarea = 360px by 120px)
Maintain a minimum margin of 60px on the top & bottom of the text area to ensure that it renders in an optimal way across browsers and devices.
3. Depending on the
Browser-OS,
the Way a User Sees the Banner Image Differs:
As shown below, you can visualize the notification for various
Browser-OS
combinations through the
Preview section
while creating the campaign.
Click to enlarge
Chrome x Android:
The banner image is hidden in the notifications tray and on the lock screen. Once the notification is expanded in the tray, the image’s height is cropped to 240px and is shown below the text
(120px is cropped from top & bottom of the image).
Chrome x Windows v9 & lower:
The entire banner image is displayed below the icon & text. The notification will appear at the bottom on the right side of the screen.
Chrome x Windows v10 & above:
The banner image’s height will be cropped to 360px and will be displayed above the icon & text
(120px is cropped from the bottom of image).
4. Banner Image is Not Supported By:
All
Mac devices,
irrespective of the browser -
Chrome/ Firefox/ Safari.
Firefox browser
on
Windows
and
Android
devices.
Things to Keep in Mind
Web Push
on Safari is supported on macOS 16 and iOS v16.4 or higher.
Safari
doesn't support
Icon
and
Banner Image.
Web Push
is not supported on
Internet Explorer.
The actual rendering of the
Web Push Notification
depends on the device's screen size, OS, and browser being used.
If you have added personalization variables to the text like
User Attributes
/
Events
/
Journey Events
/
API Call Data
/
Transactional personalization tokens
,
then we recommend that you gauge its actual length through
User Preview
or
Personalized Preview
(for Transactional campaigns).
Similarly, if you have personalized the image to a
Custom User Attribute
/
Custom Event
,
then you can view the actual image that a user will see by previewing the notification for their
User ID
through
User Preview
. (
How Image Personalization works
)
If you have added a link under the field,
Image
then:
Its URL must begin with HTTPS.
The responsiveness of the server on which the image is hosted may affect image rendering.
Web Push on Mobile Devices
iOS
devices currently do not support
Web Push Notifications.
Android users experience
Web Push Notifications
just like mobile
Push Notifications.
As shown below, the banner image and CTAs remain hidden in the notification tray until the notification is expanded by the user.
Users can choose to click on the entire notification or any of the CTAs to act upon the message. In doing so, they will be directed to the link specified by you while creating the notification, through their device's native browser.
Web Push Notifications
can be dismissed through a left swipe just like
Push Notifications.
Web Push Notification, as experienced by Android users (click to enlarge)
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries or feedback. We're always just an email away!
Updated
7 months ago
So, what's next?
Continue creating your Web Push Notification...
Creating Web Push Campaigns
Copy Page
