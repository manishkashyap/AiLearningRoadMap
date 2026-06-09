# Troubleshooting

- URL: https://docs.webengage.com/docs/web-push-troubleshooting-guide
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
Web Push
Troubleshooting
Basic Troubleshooting Guide
If Web Push is not working as expected, then please check the following:
Make sure that the
WebEngage Web SDK
is integrated on your website.
Log in to your WebEngage dashboard and navigate to
Integrations > Channels > Web Push
to ensure that the
Web Push
toggle switch is ON.
Ensure that
1-step opt-in
OR
2-step opt-in
have been configured as per the linked guides.
Ensure that you are opted-in to receiving Web Push Notifications on your test device.
Enter the command
Notification.permission
in the Google Chrome or Firefox console to check the permission status.
Notifications are shown only when the permission status indicates
Granted
. If it's not, then you can change the status through browser settings.
The
Web Push opt-in prompt
is not shown again if
Deny
is clicked the first time.
👍
Pro Tip: Don't Test Web Push in a Private Browsing Window!
Web Push Notifications
cannot be delivered in private browsing sessions. Hence, please avoid testing in an
Incognito Window in Chrome / Private Window in Firefox.
Case 1: 2-Step Opt-in Prompt Not Showing.
The
WebEngage Web SDK
enables you to check if the rules that show the Web Push opt-in prompt have been evaluated as expected. Here's how you can go about it:
Step 1:
Obtain the on-site notification rules from the
webengage_fs_configurationMap.config.webPushConfig.eventRuleCode
object. In your browser console window, enter
webengage_fs_configurationMap.config.webPushConfig.eventRuleCode
to obtain it.
Step 2:
Use the command
webengage.ruleExecutor.execute(null, “YOUR_NOTIFICATION_RULE”)
in your web browser console.
Replace
YOUR_NOTIFICATION_RULE
with individual rules obtained above one at a time.
The
webengage.ruleExecutor.execute
command evaluates to
true
if the entered rule is true. Your Web Push opt-in prompt will appear when all its corresponding rules evaluate as
true
. This helps you identify the rule that may not have been evaluated yet, thus causing the problem.
📘
Please Note
Web Push does not work in
Incognito Mode, Private Browsing Mode, and Guest Browser Mode
. However, while browsing your website in incognito mode, you might see the
Notification Prompt
appear because of technical constraints imposed by browsers that don't allow the detection of incognito mode. Kindly make sure you are not in incognito mode while testing any
Web Push Campaign
.
Case 2: User has Opted in, but Web Push Notification Undelivered.
Depending on the
Opt-in Type
set up in your WebEngage dashboard, the troubleshooting steps vary:
Troubleshooting for 1-Step Opt-in
Please following these steps:
Step 1:
Open the webpage in the
Google Chrome browser.
Step 2:
Go to
Google Chrome Home Tab > More Tools > Developer Tools.
Step 3:
Navigate to the
Application tab
in the console and select
Manifest
from the left panel.
It should show that a
manifest.json
file is available. Click on the file link.
The manifest file should open, which should have
gcm_sender_id
as a key with its value populated.
If you do not find the
manifest.json
file or
gcm_sender_id
, make sure you have followed the [1-step opt-in integration steps](1-step opt-in integration steps) correctly.
👍
Pro Tips
Make sure the
service-worker.js
file is in the root directory.
Verify that the correct FCM server key was added during configuration.
Troubleshooting for 1-Step Opt-in & 2-Step Opt-in
Please following these steps:
Step 1:
Open the webpage in the
Google Chrome browser.
Step 2:
Navigate to the
User
table under
Storage > IndexedDB > WE_PUSH
.
In the
context
key, there should be an
endpoint
under the
subscription
key.
If the field
endpoint
contains a URL, then your Web Push Notifications must get delivered.
If not, then please ensure that
Web Push has been integrated correctly
.
Case 3: Service Worker Not Located in the Root Directory.
Please be aware of the consequences of keeping the service worker file in a directory of your choice.
The location of the service worker file determines the scope of service worker registration. And the scope of the service worker determines which files the service worker controls. Or in other words, the paths from which the service worker will intercept requests. The default scope for WebEngage is the location of the service worker file, and this also extends to all the directories below it. So if
service-worker.js
is located in the root directory, the service worker will control requests from all files on this domain. In summary, service workers can only intercept requests originating in the scope of the directory where the service worker script is located and its subdirectories.
Case 4: Service Worker is Already Being Registered. Does WebEngage Need to Register It Again?
It is important that only one service worker remains active for a domain at all times.
WebEngage will register the service worker file as per the path specified in the dashboard in the settings above. But, there might be scenarios where you are already registering the service worker file at your end for various reasons such as offline support, caching, PWA implementation, working with Google Workbox, etc. If this is the case, then you need to inform WebEngage to stop the default registration at its end. Failing to do so might result in multiple conflicting service worker registrations. This will then cause our Web Push feature to behave abnormally. You can inform WebEngage to stops its registration by using the flag
registerServiceWorker
.
(
Detailed read
)
We hope this has helped you get
Web Push Notifications
up and running for your account. Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Web Push for iOS
Email
Copy Page
