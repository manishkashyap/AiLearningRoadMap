# Web Push for iOS

- URL: https://docs.webengage.com/docs/web-push-for-ios
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
Web Push
Web Push for iOS
Apple recently added support for Web Push on iOS devices for Safari browsers. This document covers the things to keep in mind for making your website compatible for Web Push notifications on iOS devices
Prerequisites
iOS device (iPhone or iOS) should be on version 16.4 or above
Safari browser version should be 16+
Update the WebEngage SDK snippet
Your website should be PWA (progressive web app)
Getting Started
🚧
The step mentioned below can be avoided if your website is already configured for sending Web Push notifications.* If you’re already registering your own service worker, then please set
webpush.registerServiceWorker
to
false
so that WebEngage can stop registering the same service worker. (
How to implement configuration flags
)
Create a Service Worker:
To get started with Web Push, you will need to create a service worker. This will handle the push events and display the notifications.
Register the Service Worker:
Once you have created the service worker, you will need to register it in your website. This can be done in the main JavaScript file of your website. Add the below code snippet in the
service-worker.js
file under the root directory of your website.
If You're Using WebEngage's Global Data Center: All your data is stored in our Global Data Center by default. Thus, if your dashboard URL starts with dashboard.webengage.com, then it means you're using our US Data Center.
service-worker.js file code - Global Data Center
importScripts('https://ssl.widgets.webengage.com/js/service-worker.js');
If You're Using WebEngage's India Data Center: You will need to specifically request for your data to be stored in our India Data Center in your contract with WebEngage. Thus, if your dashboard URL starts with dashboard.in.webengage.com, then it means you're using our India Data Center.
service-worker.js file code - India Data Center
importScripts('https://widgets.in.webengage.com/js/service-worker.js');
If You're Using WebEngage's Kingdom of Saudi Arabia (KSA) Data Center: You will need to specifically request for your data to be stored in our Saudi Arabia Data Center in your contract with WebEngage. Thus, if your dashboard URL starts with dashboard.ksa.webengage.com, then it means you're using our Saudi Arabia Data Center.
service-worker.js file code - Saudi Arabia Data Center
importScripts('https://widgets.ksa.webengage.com/js/service-worker.js');
Making website compatible
For receiving web push notifications on iOS devices, the end users need to update the WebEngage SDK and add your website to their Home screen. For this you need to follow the guidelines for Progressive Web Apps (PWAs).
📘
If your website is already complaint with PWA guidelines, then this step can be skipped.
Update Web SDK snippet
Add the below script in your web SDK:
JavaScript
webengage.options("safariWebPush",true)
Create PWA
For PWAs, you need to create a web app manifest JSON file and serve it alongside your website. It includes information such as the app name, icons, and start URL. Make sure to include the necessary properties in the manifest for your PWA to be recognized by iOS.
Here is a sample manifest JSON file:
JSON
{ "$schema": "https://json.schemastore.org/web-manifest-combined.json",
 "display": "standalone",
 "start_url": "/",
 "name": "Webengage",
 "short_name": "Webengage",
 "icons": [
 {
 "src": "/icon-192x192.png",
 "sizes": "192x192",
 "type": "image/png"
 },
 {
 "src": "/icon-256x256.png",
 "sizes": "256x256",
 "type": "image/png"
 },
 {
 "src": "/icon-384x384.png",
 "sizes": "384x384",
 "type": "image/png"
 },
 {
 "src": "/icon-512x512.png",
 "sizes": "512x512",
 "type": "image/png"
 }
 ]
}
👍
Once all the above mentioned steps are completed, your website is compatible to send web push notifications on iOS devices.
Website based opt-in prompt
Safari 16+ does not allow the native browser opt-in prompt to be shown without explicit permission from a user. Hence, you will need to set up a preceding opt-in prompt for it. Follow the steps mentioned
here
to set-up an opt-in prompt for Safari.
FAQ
What are the steps required to be performed by end users to receive web push notifications on their iOS devices?
To receive web push notifications on iPhone or iPad devices, the end user's device must:
Be on iOS version 16.4 or above
Have Safari 16
If the above conditions are met, then, following steps by them in order to receive web push notifications:
Open the website on Safari browser
Tap on the share icon in the Safari toolbar (which looks like a square with an upward arrow)
Scroll down in the share menu and select "Add to Home Screen"
In the "Add to Home Screen" menu, customize the name of the website (optional) and tap "Add" in the top-right corner.
Once the website is added to your home screen, open the website from the home screen icon.
The end user will now be able to see website based opt-in prompt asking to subscribe to web push notifications. Clicking on Allow button will open the Native prompt.
Once the user taps on "Allow" to subscribe to push notifications from the website, they will start receiving the web push.
Updated
7 months ago
Web Push for AMP
Troubleshooting
Copy Page
