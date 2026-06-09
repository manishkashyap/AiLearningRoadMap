# App In-line Content

- URL: https://docs.webengage.com/docs/android-app-in-line-content
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
App In-line Content
App In-line Content allows you to insert content directly into your app's screen without disturbing the user experience. It also allows you to dynamically update your app's content and run relevant and contextual campaigns.
You may use the
In-line Content
to change areas of your app or show banner ads based on live triggers and segmentation.
This capability is provided in WebEngage Personalization SDK, a child SDK that handles Inline campaigns.
Installation
For
WebEngage Personalization SDK
to support inline campaign processing, the parent WebEngage SDK version must be
4.0.0
or higher.
Step 1:
Integrate WebEngage SDK by following the step mentioned in
this doc
.
Step 2:
Add
WebEngage Personalization SDK
to your project.
For
installation
, add the WebEngage Personalization SDK in your app/build.gradle
Groovy
dependencies {
 implementation 'com.webengage:we-personalization:1.1.3'
}
📘
If you are already using
WebEngage Parent SDK
, then you can simply replace the dependency with the above else if both parent and personalization SDK is present then Gradle merge will happen and higher version for WebEngage core will be taken into consideration.
Initialization
Step 1:
Import and initialise
WebEngage Personalization SDK
unit
Add the following initialization code inside the
onCreate
method of your
Application class
.
Note: Make sure to Initialize post
WebEngage Android SDK
initialization.
Java
Kotlin
// Import SDK 
import com.webengage.personalization.WEPersonalization;
//..

public class MyApplication extends Application {

public void onCreate() {
 super.onCreate();
 // Initialise WebEngage SDK
 ..
 ..
 // Now initialise Personalization SDK
 WEPersonalization.Companion.get().init();
}
import com.webengage.personalization.WEPersonalization

class MyApplication : Application() {
 override fun onCreate() {
 super.onCreate()
 // Initialise WebEngage SDK
 ..
 ..
 // Now initialise Personalization SDK
 WEPersonalization.get().init()
 }
}
Step 2:
Setting up Personalization content Placeholder
Based on the use cases and template types, there are 2 approaches to set up Placeholder/Property:
Approach 1: Using WebEngage/Native Views (Recommended)
This implementation will allow you to use WebEngage pre-defined templates (
Banner
&
Text
) right out of the box, with the SDK handling campaign rendering and tracking stats. In the case of the
Custom View
template, you can easily obtain data via
callbacks
and render your own UI in the same placeholder.
To configure the property on your screen, follow the steps below:
You can add a placeholder/property to your screen by using WebEngage’s custom view
WEInlineView
(extends FrameLayout).
Create a view in Android through Interface Builder or Programatically.
Give ID/Tag to the view. This identifier will be referred to as Property ID on the dashboard.
For example, a placeholder view has been added in Interface builder,
placeholder_id
has been given to the
View
.
XML
<com.webengage.personalization.WEInlineView
 android:layout_width="match_parent"
 android:layout_height="200dp"
 app:shouldCache="false"
 android:id="@+id/placeholder_id"/>
📘
Recommendation
Though
WEInlineView
is recommended for property creation, you can also use other native
ViewGroup
such as
LinearLayout
,
FrameLayout
, and
RelativeLayout
.
Declare the placeholder view's height, as this will ensure that the resulting campaign is rendered inside the stated height.
In the above example, the height of the placeholder has been declared as 200dp.
Approach 2: Rendering complex use cases using Custom template
❗️
Please Note
This approach is supported only for Custom templates (Not supported for Text and Banner templates).
For this approach you need to register your property (not necessary a part of your XML) with WebEngage and obtain campaign data to build your own UI; however, this only allows you to obtain data; you must still track impressions and clicks by referring the steps mentioned
here
.
To configure the property on your screen, follow the steps below:
Register your property by passing the ID/TAG (or any other unique property identifier) through
WEPlaceholderCallbacks
, inside the
onStart
method of your
Activity
or
Fragment
and after calling
screenNavigated
Java
Kotlin
@Override
protected void onStart() {
 super.onStart();
 WebEngage.get().analytics().screenNavigated("SCREEN_NAME");
 WEPersonalization.Companion.get().registerWEPlaceholderCallback("placeholder_identifier", this);
}
override fun onStart() {
 super.onStart()
 WebEngage.get().analytics().screenNavigated("SCREEN_NAME")
 WEPersonalization.get().registerWEPlaceholderCallback("placeholder_identifier", this)
}
After registering the property, you can obtain the data (key-value) pairs inside
onDataReceived
function of WEPlaceholderCallbacks, post that you can render your own UI using the same
data
.
Java
Kotlin
@Override
public void onDataReceived(@NonNull WECampaignData data) {
 //Build your own UI using the data
}
override fun onDataReceived(data: WECampaignData) {
 //Build your own UI using the data
}
Make sure to track
Impressions
and
Clicks
of these Custom Views to analyze your campaigns.
Step 3:
Tag your Screen/Activity with a name.
Because properties are attached to screens Activity/Fragment, tagging screens with appropriate screen names is a required step for In-line Campaigns to function properly.
🚧
Please Note
This is a mandatory step.
Add screen name in onStart() for your Activity/Fragment.
Java
Kotlin
@Override
protected void onStart() {
 super.onStart();
 WebEngage.get().analytics().screenNavigated("SCREEN_NAME");
 //Callbacks to be configured after screen navigation step.
}
override fun onStart() {
 super.onStart()
 WebEngage.get().analytics().screenNavigated("SCREEN_NAME")
 //Callbacks to be configured after screen navigation step.
}
Callbacks
There are two types of callbacks available in Personalization SDK.
WEPlaceholderCallback: Placeholder Callbacks
You can subscribe to the callbacks basis on placeholder views created with property id to receive updates and respective data in the callback methods. This callback is needed for Advanced integration and if you want to get property wise updates.
Register
Register your callback/property by passing the ID/TAG (or any other unique property identifier), inside the onStart method of your
Activity
or
Fragment
and after calling
screenNavigated
Java
Kotlin
@Override
protected void onStart() {
 super.onStart();
 WebEngage.get().analytics().screenNavigated("SCREEN_NAME");
 WEPersonalization.Companion.get().registerWEPlaceholderCallback("placeholder_identifier", this);
}
override fun onStart() {
 super.onStart()
 WebEngage.get().analytics().screenNavigated("SCREEN_NAME")
 WEPersonalization.get().registerWEPlaceholderCallback("placeholder_identifier", this)
}
Callback methods
🚧
Please Note
Make sure to Register the placeholder to start getting callbacks.
All callbacks are optional
Following are the callback methods available in
WEPlaceholderCallback
:
onDataReceived
: This callback will get triggered when the campaign data will be received for Placeholder View. For Custom templates, you can obtain the data (key-value) pairs and can render your own UI using the same
data
(This method will give you accessibility to load the view dynamically. This is generally used in use-cases which involves RecyclerView or views which are server driven.). This will be called for all the templates Banner, Text and Custom available in WebEngage’s dashboard.
Java
Kotlin
@Override
public void onDataReceived(@NonNull WECampaignData data) {
 //Build your own UI using the data
override fun onDataReceived(data: WECampaignData) {
 //Build your own UI using the data
}
onRendered
: When the SDK displays the Campaign on the screen (view event is triggered), this callback is triggered. This will only be triggered for Banner and Text templates.
This will not be triggered for Custom templates,
because they are handled by your application, and in cases where you have called
stopRendering
through WECampaignCallback.
Java
Kotlin
@Override
public void onRendered(@NonNull WECampaignData data) {
 // This will be executed when a placeholder view with campaign will be shown
}
override fun onRendered(data: WECampaignData) {
 // This will executed when placeholder view with campaign will be shown
}
onPlaceholderException
: This callback will get triggered when the campaign showing for a
Property
or
Placeholder
will get failed. If the property is already visible, use this method to hide it or to display some default UI. Kindly refer to
Exceptions
for types of exceptions.
Java
Kotlin
@Override
public void onPlaceholderException(@Nullable String campaignId, @NonNull String targetViewId, @NonNull Exception error) {
 // This will executed once exception occured
}
override fun onPlaceholderException(
 campaignId: String?,
 targetViewId: String,
 error: Exception
 ) {
 // This will executed once exception occured
 }
📘
Note
Placeholder callback
onRendered
will be triggered for Banner and Text layouts while only
onDataReceived
will be triggered for Custom layout.
WECampaignCallback
: Campaign Callbacks
You can register for the callbacks globally in the Application class or locally in the activity. This will be triggered throughout the lifecycle of a campaign.
Register the callback inside your Application or Activity class
Register your callback whether in
onCreate
method of your Application class or
onStart
method of your screen Activity/Fragment
Java
Kotlin
@Override
protected void onStart() {
 super.onStart();
 WebEngage.get().analytics().screenNavigated("SCREEN_NAME");
 //Callbacks to be configured after screen navigation step.
 WEPersonalization.Companion.get().registerWECampaignCallback(this);

}
override fun onStart() {
 super.onStart()
 WebEngage.get().analytics().screenNavigated("SCREEN_NAME")
 //Callbacks to be configured after screen navigation step.
 WEPersonalization.get().registerWECampaignCallback(this)
}
Following are the callback methods available in WECampaignCallback
onCampaignPrepared
: This is the first callback method that is triggered when data for the qualified campaign is retrieved from the WebEngage servers. You can also stop rendering the campaign by calling
stopRendering()
method of
WECampaignData
(generally this can come handy if you want to just retrieve some data and render on your own for layout. This will always be called for your templates (banner, text and custom).
Java
Kotlin
@Override
public WECampaignData onCampaignPrepared(@NonNull WECampaignData data) {
 // You will get data received for campaign 
 return data;
}
override fun onCampaignPrepared(data: WECampaignData): WECampaignData {
 // You will get data received for campaign 
 return data
}
onCampaignShown
: When the SDK displays the Campaign on the screen, this callback is triggered. This will only be triggered for Banner and Text templates and
not
for Custom templates (since they are handled by your application). This callback will also
not
be triggered in cases where you have called
stopRendering
.
Java
Kotlin
@Override
public void onCampaignShown(@NonNull WECampaignData data) {
 //Campaign Shown
}
override fun onCampaignShown(data: WECampaignData) {
 //Campaign Shown
}
onCampaignClicked
: This callback will get triggered when clicked on the campaign view rendered by the SDK. This will only be triggered for Banner and Text templates and
not
Custom templates (since they are handled by your application).
Make sure to handle your deeplinks in this method
; returning false results in automatic redirection because the SDK will handle and attempt to open the link, whereas when returning true instructs the SDK not to perform any redirection because the application will handle the same.
Java
Kotlin
@Override
 public boolean onCampaignClicked(@NonNull String actionId, 
 @NonNull String deepLink, 
 @NonNull WECampaignData data) {
 // Returning true would not redirect automatically to action Url. Write your redirection code here and return false. 
 // Returning false would open Action Url in Browser
 return false; 
}
override fun onCampaignClicked(
 actionId: String,
 deepLink: String,
 data: WECampaignData
): Boolean {
 // Returning true would not redirect automatically to action Url. Write your redirection code here and return false.
 // Returning false would open Action Url in Browser
 return false 
}
onCampaignException
: This callback will get triggered when the campaign retrieval/showing will get failed.
Java
Kotlin
@Override
public void onCampaignException(@Nullable String campaignId,
 @NonNull String targetViewId,
 @NonNull Exception error) {
 // Exception occurred
}
override fun onCampaignException(campaignId: String?,
 targetViewId: String,
 error: Exception) {
 // Exception occurred
}
Exceptions
You will receive exception details in
onCampaignException
of WECampaignCallback &
onPlaceholderException
of WEPlaceholderCallback
Types of Exception:
Error Key
Error Description
timeout
Campaign failed to render in set time.
missingTargetView
Target property missing.
campaignFetchingFailed
Campaign fetching failed.
resourceFetchingFailed
Resource fetching falied.
WECampaignData
You can access the Campaign Id and Placeholder details like name (id) and content. It consists of the following members
Name
Variable type
Definition
targetViewId
String
Placeholder name (id).
content
WECampaignContent
Campaign view content which contains custom key-value pairs.
campaignId
String
The id for the running campaign on the placeholder. Default value would be blank.
WECampaignContent
Personalization SDK renders the Banner, Text view through this data. You can access the custom key-value pairs through this.
Name
Variable type
Definition
customData
Kotlin: HashMap <String, Any>
Java: HashMap <String, Object>
Custom key-value pairs defined for the campaign.
WEInlineView
This is a WebEngage custom view for rendering campaigns and can be directly included in layout XML or can also be initialized programmatically.
Following are the methods available:
Method name
Params
Return type
Params Definition
load
identifier
of type
String
: This is a property identifier (ID/TAG).
listener
of type
WEPlaceholderCallback
: This is for attaching Placeholder callbacks for your property view
:void
This method will give you accessibility to load the view dynamically. This is generally used in use-cases which involves
RecyclerView
or views which are server driven.
Unregister the callbacks
❗️
Please Note
we-personalization
SDK v1.0.0 will require you to unregister placeholder callbacks in
onStop
, from v1.1.0 and above will unregister
WEPlaceHolderCallback
automatically for that screen.
Hence, you are not required to unregister the
WEPlaceHolderCallback
if you are using version v1.1.0 and above.
This step is just as important as registering for the placeholder and campaign callbacks.
Implement the following code inside
onStop
of your activity.
Java
Kotlin
@Override
protected void onStop() {
 super.onStop();

//Unregister Placeholder callback
WEPersonalization.Companion.get().unregisterWEPlaceholderCallback("placeholder-id");

//Unregister Campaign callback
WEPersonalization.Companion.get().unregisterWECampaignCallback(this);

}
override fun onStop() {
 super.onStop() 

//Unregister Placeholder callback
WEPersonalization.get().unregisterWEPlaceholderCallback("flPersonalizeId")

//Unregister Campaign callback
WEPersonalization.get().unregisterWECampaignCallback(this)

}
Track Campaign Impressions and Clicked Events for Custom Views
For
Custom Views
, Personalization SDK will pass the custom data
WECampaignData
, which should be managed/rendered by your application only.
🚧
Please Note
Tracking Impressions
and
tracking Clicks
are mandatory steps for Custom View campaigns. If not added then Impression and Click data for these campaigns will not be recorded.
Record Viewed Impression
Impression tracking is simply tracking the number of views each campaign receives.
For example, if a user visits the screen and sees a campaign and visits the screen again then they will see the exact same campaign again, two impressions would be counted.
Now,
trackImpression
will allow you to track impressions for your campaign. Kindly, use the mentioned method of
WEGCampaignData
once the custom view has been shown on the screen by the application.
📘
Recommendation
WEGCampaignData
will be received both in
onDataReceived
of
WEPlaceholderCallback
and
onCampaignPrepared
of
WECampaignCallback
.
Java
Kotlin
//attributes: any custom Map<String, Object> of data you want to record with this event

//data: WEGCampaignData

data.trackImpression(null);
//attributes: any custom Map<String, Any> of data you want to 
record with this event

//data: WEGCampaignData

data?.trackImpression(attributes:nil)
Record Click Impression
You can track click impressions whenever the user clicks on the campaign view on the screen.
Java
Kotlin
//attributes: any custom Map<String, Object> of data you want to record with this event

//data: WEGCampaignData

data.trackClick(null);
//attributes: any custom Map<String, Object> of data you want to record with this event

//data: WEGCampaignData

data?.trackClick(attributes:nil)
Updated
7 months ago
In-app Messaging
Callbacks
Copy Page
