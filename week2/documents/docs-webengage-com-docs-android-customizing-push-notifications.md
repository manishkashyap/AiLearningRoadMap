# Customizing Push Notifications

- URL: https://docs.webengage.com/docs/android-customizing-push-notifications
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
Push Messaging
Customizing Push Notifications
Step-by-step guide to customizing the appearance of Push Notifications through your app
Custom Push Notification Layouts
WebEngage Android SDK has included two new functional interfaces in v3.10.1 which allows you to modify the default push notification layouts.
🚧
Please ensure you follow the
Android notification layout guidelines
before creating your own custom layouts. Usually, collapsed view layouts are limited to 64 dp, and expanded view layouts are limited to 256 dp.
1. CustomPushRender
: Called for rendering push notifications. This is where you can set your custom layouts and notify push notifications.
Java
public interface CustomPushRender {
 /**
 * @return: Return true if notification is rendered successfully, else return false.
 */
 boolean onRender(Context context, PushNotificationData pushNotificationData);
}
2. CustomPushRerender
: Called for re-rendering/updating push notifications. This is where you can update your push notifications.
Java
public interface CustomPushRerender {
 /**
 * @return: Return true if notification is re-rendered successfully, else return false.
 */
 boolean onRerender(Context context, PushNotificationData pushNotificationData, Bundle extras);
}
Custom push render callbacks are only called when you provide
we_custom_render:
true in the custom key-values while creating push campaign from WebEngage dashboard and CustomPushRender and CustomPushRerender implementations are registered using
WebEngage.registerCustomPushRenderCallback
and
WebEngage.registerCustomPushRerenderCallback
APIs.
If
onRender
or
onRerender
method returns false, then notification will not be displayed.
Push Notification Data
The instance of
PushNotificationData
available to you in the
onRender
and
onRerender
callbacks contains the details required to construct and show the push notification.
🚧
Rich Text handling
Available from SDK v3.20.0 and needs to be handled properly to avoid showing proper title and message in push notifications.
Handling Rich text
From SDK version 3.20.0 and above you will start getting rich text in PushNotifictaionData hence it needs to be handled accordingly.
Push title, message, summary and action text will start coming in HTML format so to handle them, kindly follow the steps below.
Handling Push Title text
Java
Kotlin
WEHtmlParserInterface weHtmlParserInterface = new WEHtmlParserInterface();
 Spannable title = weHtmlParserInterface.fromHtml(pushNotificationData.getTitle());

...
//Now use the title as your input to remote views.
val weHtmlParserInterface = WEHtmlParserInterface() 
 val title = weHtmlParserInterface.fromHtml(pushNotificationData.title)

...
//Now use the title as your input to remote views.
Handling Push Description text
Java
Kotlin
WEHtmlParserInterface weHtmlParserInterface = new WEHtmlParserInterface();
 Spannable description = weHtmlParserInterface.fromHtml(pushNotificationData.getContentText());

...
//Now use the description as your input to remote views.
val weHtmlParserInterface = WEHtmlParserInterface() 
val description = weHtmlParserInterface.fromHtml(pushNotificationData.contentText)
...
//Now use the description as your input to remote views.
Handling Push Summary text
Java
Kotlin
WEHtmlParserInterface weHtmlParserInterface = new WEHtmlParserInterface();
 Spannable summary = weHtmlParserInterface.fromHtml(pushNotificationData.getContentSummary());

...
//Now use the summary as your input to remote views.
val weHtmlParserInterface = WEHtmlParserInterface() 
val summary = weHtmlParserInterface.fromHtml(pushNotificationData.contentSummary)
...
//Now use the summary as your input to remote views.
❗️
Important changes while getting data from PushNotificationData
Follow the changes mentioned in the table below
Description
less than v3.20.0
greater equal v3.20.0
Fetching Description
pushNotificationData.getSummary()
pushNotificationData.getContentText()
Fetching Summary
Not Available
pushNotificationData.getContentSummary()
Tracking Push Notification Actions
In order to correctly track the push notification actions such as clicks, updates, dismissed, etc. in custom push notifications, it is mandatory to use the PendingIntents constructed through the APIs provided in the WebEngage's
PendingIntentFactory
class.
PendingIntentFactory
includes the APIs for constructing the following
PendingIntents
which must be set in the Notification for tracking different push notification actions.
1. Click PendingIntent
PendingIntent constructPushClickPendingIntent(Context context, PushNotificationData pushNotificationData, CallToAction cta, boolean autoCancel)
method returns a
PendingIntent
which can be set as
PendingIntent
for content intent or for any action button in your custom push notification.
Java
boolean autoCancel = true; // true if notification should be dismissed on click, else false
 PendingIntent contentPendingIntent = PendingIntentFactory.constructPushClickPendingIntent(context, pushNotificationData, pushNotificationData.getPrimeCallToAction(), autoCancel);
 NotificationCompat.Builder builder = new NotificationCompat.Builder(context, MY_CHANNEL_ID)
 ...
 .setContentIntent(contentPendingIntent)
 ...
2. Delete PendingIntent
PendingIntent constructPushDeletePendingIntent(Context context, PushNotificationData pushNotificationData)
method returns a
PendingIntent
that must be set as delete intent in your notification, which will help WebEngage SDK to track push notification dismisses.
Java
PendingIntent deletePendingIntent = PendingIntentFactory.constructPushDeletePendingIntent(context, pushNotificationData);
 NotificationCompat.Builder builder = new NotificationCompat.Builder(context, MY_CHANNEL_ID)
 ...
 .setDeleteIntent(deletePendingIntent)
 ...
3. Rerender PendingIntent
PendingIntent constructRerenderPendingIntent(Context context, PushNotificationData pushNotificationData, String requestCodePrefix, Bundle extraData)
method returns a
PendingIntent
which will trigger the
onRerender
callback on click. This callback can be used to update/rerender your notification.
param
String requestCodePrefix:
The request code of the returned
PendingIntent
is generated using the following code:
Java
...
 int requestCode = (requestCodePrefix + pushNotificationData.getVariationId()).hashCode();
 PendingIntent pendingIntent = PendingIntent.getService(context, requestCode, intent, PendingIntent.FLAG_UPDATE_CURRENT);
 return pendingIntent;
param
Bundle extraData
: This bundle must include additional data required for rerendering the notification. This bundle will be passed in boolean
onRerender(Context context, PushNotificationData pushNotificationData, Bundle extraData)
method as
extraData
for updating the notification.
For eg. You might want to update the push notification content when a user selects a star in rating push notification. In order to mark the star(s) as selected, you might need an additional information that tells you which star was clicked. Such additional data can be passed in the
extraData
bundle.
Java
Bundle rateClickExtraData = new Bundle();
 rateClickExtraData.putInt("current", i);
 ...

 PendingIntent rateClickPendingIntent = PendingIntentFactory.constructRerenderPendingIntent(context, pushNotificationData, "rate_click_" + i, rateClickExtraData);
 ratingView.setOnClickPendingIntent(R.id.selected_star, rateClickPendingIntent);
4. Carousel Browse PendingIntent
PendingIntent constructCarouselBrowsePendingIntent(Context context, PushNotificationData pushNotificationData, int newIndex, String navigation, String requestCodePrefix, Bundle extraData)
method returns a
PendingIntent
which will automatically track the carousel browse event on click of left/right arrows in the carousel push notification. It also triggers the
onRerender
callback which can be used to update the current carousel item.
param
int newIndex
: This is the newly calculated index of the carousel item to be shown.
param
String navigation
: This indicates the direction in which the carousel is browsed.
Java
int currIndex = 0;
 PendingIntent leftPendingIntent = PendingIntentFactory.constructCarouselBrowsePendingIntent(context, pushNotificationData, currIndex, "left", "carousel_left", browseExtraData);
 PendingIntent rightPendingIntent = PendingIntentFactory.constructCarouselBrowsePendingIntent(context, pushNotificationData, currIndex, "right", "carousel_right", browseExtraData);
 ...
 carouselView.setOnClickPendingIntent(R.id.left_arraow, leftPendingIntent);
 carouselView.setOnClickPendingIntent(R.id.right_arrow, rightPendingIntent);
 ...
5. Rating Submit PendingIntent
PendingIntent constructPushRatingSubmitPendingIntent(Context context, PushNotificationData pushNotificationData, int rateValue)
method takes an integer for rating as parameter which will track rating submit event on click of submit button in rating notification.
param
int rateValue
: This is the last rating value selected by the user.
Java
int currIndex = extraData.getInt("current"); // current index can be obtained from extraData bundle provided while setting Click PendingIntent
 PendingIntent rateSubmitPendingIntent = PendingIntentFactory.constructPushRatingSubmitPendingIntent(context, pushNotificationData, currIndex);
 ratingView.setOnClickPendingIntent(R.id.rating_submit_button, rateSubmitPendingIntent);
Note
: Any
PendingIntents
used in the push notification which is not provided by the above specified APIs, will not be tracked by the WebEngage Android SDK and hence will not be seen on the campaign stats page in your WebEngage dashboard.
Sample usage of these PendingIntents can be found in the code snippets of sample custom layouts given below.
Sample Custom Layouts
Prerequisites:
Create implementations of
CustomPushRender
and
CustomPushRerender
interfaces as shown below.
Java
public class MyPushRenderer implements CustomPushRender, CustomPushRerender {
 @Override
 public boolean onRender(Context context, PushNotificationData pushNotificationData) {
 // render your notification here
 return true;
 }

 @Override
 public boolean onRerender(Context context, PushNotificationData pushNotificationData, Bundle bundle) {
 // re-render your notification here
 return true;
 }
}
Make sure to register for custom push render callbacks in your Application class as shown below.
Java
public class MainApplication extends Application {
 private static final String TAG = MainApplication.class.getSimpleName();

 @Override
 public void onCreate() {
 super.onCreate();

 ...

 // Register for custom push render callbacks
 MyPushRenderer myPushRenderer = new MyPushRenderer();
 WebEngage.registerCustomPushRenderCallback(myPushRenderer);
 WebEngage.registerCustomPushRerenderCallback(myPushRenderer);
 }
}
Please refer to the following sample code snippets which might help you to build your own custom push notification layouts -
Text Layout
,
Banner Layout
,
Carousel Layout (Landscape)
,
Carousel Layout (Portrait)
,
Rating Layout
.
For the following sections, you can customize your push messages by implementing
push message callbacks
in your application.
Overriding Push Title, Message and Image
You can override the title, message or image of the push notification that you had set on WebEngage dashboard while creating the campaign.
Java
@Override
 public PushNotificationData onPushNotificationReceived(Context context, PushNotificationData notificationData) {
 notificationData.setTitle("YOUR_TITLE"); // Add or change title
 notificationData.setContentText("YOUR_MESSAGE"); // Change message
 WebEngageConstant.STYLE style = notificationData.getStyle();
 if (style != null) {
 switch (style) {
 case BIG_PICTURE:
 // Change image
 notificationData.getBigPictureStyleData().setBigPictureUrl("http://www.example.com");

 //Add title which will be shown when notification is expanded
 notificationData.getBigPictureStyleData().setBigContentTitle("YOUR_EXPANDED_TITLE");
 // Add summary which will be shown when notification is expanded.
 notificationData.getBigPictureStyleData().setSummary("YOUR_SUMMARY");
 break;

 case BIG_TEXT:
 // Add or change title which will be shown when notification is expanded.
 notificationData.getBigTextStyleData().setBigContentTitle("YOUR_EXPANDED_TITLE");
 // Change message which will be shown when notification is expanded.
 notificationData.getBigTextStyleData().setBigText("YOUR_EXPANDED_MESSAGE");
 break;
 }
 }
 return notificationData;
 }
Campaign-level Customization
While creating a push message campaign on WebEngage dashboard, you can define key-value pairs. This data is a part of the push message payload, and can be accessed using push callbacks. This allows you to customize your push messages at a campaign level from within your app. This is illustrated below using
onPushNotificationDismissed
. You can use any of the push message callbacks depending on where you want to customize the user experience.
Java
@Override
public void onPushNotificationDismissed(Context context, PushNotificationData notificationData) {
 Bundle customData = notificationData.getCustomData();
 if (customData != null) {
 // Your customization logic goes here
 }
}
📘
If you have multiple apps using the same WebEngage license code, you can target them selectively using push notifications by adding key-value pairs in the campaign body and using them as identifiers in your apps as illustrated above.
Call to Action
Calls to action are the deep links or URIs where a user lands on clicking the push message. You can add CTAs while creating your push campaign on WebEngage dashboard. They are divided into two categories in
WebEngage Android SDK - Primary CTA
and
Non-primary CTA.
Primary CTA
A push message can have at most one primary CTA which performs action (directs the user to a particular URI or a deep link) when the user taps on the content of the push notification. If no URI or deep link is configured for primary CTA then the user will be redirected to your application's launcher activity upon clicking the push notification.
Click to enlarge
Non-primary CTAs
A push notification can have at most 2 non-primary CTAs which perform action when the user clicks on their respective action buttons.
Sometimes you may desire to take control of the click action of a push notification for performing tasks such as creating your own back navigation. When the user enters your app with a deep link that starts the activity in its own task, it's necessary for you to synthesize a new back stack because the activity is running in a new task without any back stack at all. This is illustrated below using push message callbacks.
Java
@Override
public boolean onPushNotificationClicked(Context context, PushNotificationData notificationData) {
 return buildNavigation(context, notificationData.getPrimeCallToAction());
 }

@Override
public boolean onPushNotificationActionClicked(Context context, PushNotificationData notificationData, String buttonID) {
 return buildNavigation(context, notificationData.getCallToActionById(buttonID));
 }

 private boolean buildNavigation(Context context, CallToAction callToAction) {
 if (callToAction != null) {
 if (callToAction.isPrimeAction()) {
 //User clicked on notification content
 String action = callToAction.getAction();
 if (action == null) {
 // Primary CTA was not configured with a URI or deep link.
 // Return false if you want WebEngage SDK to open launcher activity with default intent flags.
 // Return true and write your own code to open desired activity with custom intent flags.

 } else {
 CallToAction.TYPE type = callToAction.getType();
 if (type != null) {
 switch (type) {
 case LINK:
 //This CTA was configured with a link while creating the push notification campaign.
 // This link can be either an http url or your custom deep link.
 // Return false if you want WebEngage SDK to open this link with default flags or return true
 // and write your own code to open this link.

 break;

 case LAUNCH_ACTIVITY:
 //This CTA was configured with an activity path while creating the push notification.
 // Return false if you want WebEngage SDK to open this activity with default flags or return true 
 // and write your own code to open this activity.

 break;
 }
 }
 }
 //NOTE: To get action string use callToAction.getAction()
 } else {
 // User clicked on one of the action buttons.
 // Handle this CTA in the same way above primary CTA is handled, if only desired.
 }
 }
 return false;
 }
🚧
Please Note
Read operation on
PushNotificationData
fields can be done from any push notification callback function.
Any changes done to
PushNotificationData
fields will be reflected only if they are called from
onPushNotificationReceived
callback.
For example :
notificationData.getPrimeCallToAction().setAction("https://www.example.com", CallToAction.TYPE.LINK,context)
will be effective only if it is called from
onPushNotificationReceived
.
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
In-app messaging
Copy Page
