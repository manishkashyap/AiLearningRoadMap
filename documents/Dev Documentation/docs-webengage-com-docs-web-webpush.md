# Web Push

- URL: https://docs.webengage.com/docs/web-webpush
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Website
Web Push
🚧
Must Read
Please refer here
for our Web Push channel configuration guide.
Web Push Opt-in Configuration
Property
Type
Description
Default
webpush.disablePrompt
Boolean
If set to
true
, an unsubscribed visitor will not be automatically shown any opt-in prompts. You can use this to handle the rendering of the opt-in prompt.
Note that you need to call
webengage.webpush.prompt()​
once the user gives permission for web push on your opt-in prompt.
false
webpush.registerServiceWorker
Boolean
If set to
false
, WebEngage will not automatically register the service worker script - our SDK will rely on your website to perform the registration.
true
JavaScript
/*
 * Set this option to 'true' if you want to hide the prompt on page load
 * and programmatically enable it later
 */
webengage.options('webpush.disablePrompt', true);

/*
 * Set this option to 'false' if your website is registering
 * the service worker script by itself
 */
webengage.options('webpush.registerServiceWorker', false);
Public SDK Methods
webengage.webpush.prompt
Shows the opt-in prompt if the visitor is not subscribed to push notifications. The behavior changes depending on the opt-in mode:
Two-step opt-in:
Opens a popup window to a WebEngage managed site where the subscription prompt for push notifications is shown. Call this in a elements' click event listener, otherwise, the browser's popup blocker will prevent the popup from opening.
One step opt-in:
You may call this at any time to show the browser prompt for notifications.
Along with setting the
webpush.disablePrompt
configuration property to
true
, this API can be used to customize the opt-in experience as per the needs of your site. Always call this API from within
webengage.onReady
JavaScript
webengage.onReady(function () {
 webengage.webpush.prompt();
});
webengage.webpush.onSubscribe
Registers the passed function, to be called when a visitor allows push notifications and the subscription completes successfully. Always call this API from within
webengage.onReady
.
JavaScript
webengage.onReady(function () {
 webengage.webpush.onSubscribe(function () {
 alert('Thanks! You are now subscribed');
 });
});
webengage.webpush.isSubscribed
Returns
true
if the visitor is already subscribed for web push notifications,
false
otherwise. Always call this API from within
webengage.onReady
One possible use of this method is to determine user subscription and then hide the opt-in prompt for subscribed users.
JavaScript
webengage.onReady(function () {
 var subscribed = webengage.webpush.isSubscribed();

 if (subscribed) {
 console.log('User is already subscribed');
 } else {
 console.log('User is not yet subscribed');
 }
});
webengage.webpush.isPushNotificationsSupported
Takes a callback which is then asynchronously invoked with a boolean argument. If the argument is true then push notifications are supported in the current browsing context, else they are not. Always call this API from within
webengage.onReady
.
Push notifications are supported in latest versions of Chrome and Firefox browsers on Windows, macOS, Linux and Android operating systems. They also don't work in private browsing / incognito mode.
JavaScript
webengage.onReady(function () {
 webengage.webpush.isPushNotificationsSupported(function (supported) {
 if (supported) {
 alert('Push notifications are supported');
 }
 });
});
Get current web push subscription status
JavaScript
webengage.webpush.isSubscribed()
Check if the push notification is supported or not
JavaScript
webengage.webpush.isPushNotificationsSupported()
Listen to web push subscription event
JavaScript
webengage.webpush.onSubscribe(() => {
 // add the code here
})
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
Tracking Events
On-site Notification
Copy Page
