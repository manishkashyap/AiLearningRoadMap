# App In-line Content

- URL: https://docs.webengage.com/docs/flutter-app-in-line-content
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Hybrid Apps
Flutter
App In-line Content
📘
Supported from Flutter SDK v1.2.3.
App In-line Content allows you to insert content directly into your app's screen without disturbing the user experience. It also allows you to dynamically update your app's content and run relevant and contextual campaigns.
You may use the In-line Content to change areas of your app or show banner ads based on live triggers and segmentation.
This capability is provided in WebEngage Personalization SDK, a child SDK that handles Inline campaigns.
Installation
Step 1:
Integrate the WebEngage SDK by following the steps mentioned in
this
document.
Step 2:
Add dependency in pubspec.yaml
dart
we_personalization_flutter: ^1.0.0
Initialization
Initialize the WebEngage Personalization SDK by calling
WEPersonalization().init()
;. This needs to be done only once, and right after the WebEngage SDK Plugin initialization.
In
main.dart
file after initialising WebEngage plugin , call initialization of personalisation plugin in
initState
method
dart
import 'package:we_personalization_flutter/we_personalization_flutter.dart';

WEPersonalization().init();
The
initState
method will look like this:
dart
import 'package:flutter/material.dart';
import 'package:webengage_flutter/webengage_flutter.dart';
import 'package:we_personalization_flutter/we_personalization_flutter.dart';

void main() {
 runApp(MyApp());
}

class MyApp extends StatefulWidget {
 @override
 MyAppState createState() => MyAppState();
}

class MyAppState extends State<MyApp> {
 @override
 void initState() {
 super.initState();
 //Initialize WebEngage Core plugin
 WebEngagePlugin _webenagePlugin = WebEngagePlugin();
 //Intialize WebEngage Personalization Plugin
 WEPersonalization().init();
 }
}
Screen Tracking
❗️
Mandatory step
Tracking screen is a mandatory step to make sure In-line campaigns are rendered. This step cannot be skipped.
To track the screen in Flutter, you can either use the
Flutter Navigator widget
or the
Route Object
mechanism. The examples for tracking screens from both mechanisms are given below.
Through Flutter Navigator widget
If you are using push name method
Navigator.of(context).pushNamed(SCREEN_NAME)
; to navigate to the different screens then use the below method to track screen.
Create a file
ScreenRouteObserver.dart
and add below code:
dart
import 'package:flutter/material.dart';
import 'package:webengage_flutter/webengage_flutter.dart';

class ScreenRouteObserver extends RouteObserver<PageRoute<dynamic>> {

 void _sendScreenView(PageRoute<dynamic> route) {
 var screenName = route.settings.name;
 if (screenName != null) {
 // your code goes here
 WebEngagePlugin.trackScreen(screenName);
 }
 }

 
 @override
 void didPush(Route route, Route? previousRoute) {
 super.didPush(route, previousRoute);
 if (route is PageRoute) {
 _sendScreenView(route);
 }
 }

 @override
 void didPop(Route route, Route? previousRoute) {
 super.didPop(route, previousRoute);
 if (previousRoute is PageRoute && route is PageRoute) {
 _sendScreenView(previousRoute);
 }
 }
}
Now in
main.dart
file, create an instance
ScreenRouteObserver
class and assign it to
navigatorObserver
in MaterialApp:
dart
@override
 Widget build(BuildContext context) {
 return MaterialApp(
 initialRoute: ScreenNavigator.SCREEN_HOME,
 routes: {
 "homeScreen": (context) => const HomeScreen(),
 "detailScreen": (context) => const DetailScreen(),

 },
 navigatorObservers: [ScreenRouteObserver()],
 );
 }
Through Route Object mechanism
If you are using PageRoute method to navigate to the different screens then use the below method to track screen:
dart
Navigator.of(context).push(MaterialPageRoute(
 builder: (context) => HomeScreen()));
Create a instance of
RouteObserver
in
main.dart
file:
dart
final RouteObserver<PageRoute> routeObserver = RouteObserver<PageRoute>();

void main() {
 runApp(const MyApp());
}
Then add
routeObserver
to
navigatorObservers
:
dart
@override
 Widget build(BuildContext context) {
 return MaterialApp(
 initialRoute: ScreenNavigator.SCREEN_HOME,
 navigatorObservers: [routeObserver],
 );
 }
Then in your screen widget class do the following:
dart
class HomeScreen extends StatefulWidget {
 CustomModel customModel;

 HomeScreen({Key? key, required this.customModel}) : super(key: key);

 @override
 State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen>
 with RouteAware {

 @override
 void initState() {
 super.initState();
 trackScreen();
 }

 @override
 void didChangeDependencies() {
 super.didChangeDependencies();
 routeObserver.subscribe(this, ModalRoute.of(context) as PageRoute);
 }

 @override
 void didPopNext() {
 super.didPopNext();
 trackScreen();
 }

 @override
 void dispose() {
 routeObserver.unsubscribe(this);
 super.dispose();
 }

 void trackScreen(){
 WebEngagePlugin.trackScreen("homeScreen");
 }

 
 @override
 Widget build(BuildContext context) {
 return Scaffold(
 appBar: AppBar(
 title: Text("HOME SCREEN),
 ),
 body: Container(
 padding: const EdgeInsets.all(10),
 );
 }
Add
WEInlineWidget
widget in your widget or screen like below:
dart
import 'package:we_personalization_flutter/we_personalization_flutter.dart';

WEInlineWidget(
 screenName: "homescreen",
 androidPropertyId: "s1p1",
 iosPropertyId: 1002,
 viewWidth: 0,
 viewHeight: 100,
 placeholderCallback: this,
 ),
 );
Key
Description
screenName
The name you pass during the
trackScreen
.
androidPropertyId
Android Property ID in
String
format.
*Note:
The Property ID
cannot** be named any integer between '1' to '100'.
iosPropertyId
iOS Property ID in
Int
format.
*Note:
The Property ID
cannot** be named any integer between '1' to '100'.
viewWidth
Width of view in Double format.
*Note:** If passed 0, it will take whole parent width.
viewHeight
Height of view in Double Format.
placeholderCallback
Callback for placeholder.
Callbacks
There are two types of callbacks available in Personalization SDK.
WEPlaceholderCallback: Placeholder Callbacks
Implement
WEPlaceholderCallback
in same class where
WEInlineWidget
is present.
In your class where you have added
WEInlineWidget
implement it with
WEPlaceholderCallback
and override the methods.
dart
class _HomeScreenState extends State<HomeScreen>
 with WEPlaceholderCallback{

 @override
 void onDataReceived(data) {
 super.onDataReceived(data);
 }

 @override
 void onPlaceholderException(String campaignId, String targetViewId, String error) {
 super.onPlaceholderException(campaignId, targetViewId, error);
 }
 
 @override
 void onRendered(data) {
 super.onRendered(data);
 }

 }
onDataReceived
: This callback will get triggered when the campaign data will be received for Placeholder View. For Custom templates, you can obtain the data (key-value) pairs and can render your own UI using the same
data
(This method will give you accessibility to load the view dynamically. This is generally used in use-cases which involves RecyclerView or views which are server driven.). This will be called for all the templates Banner, Text and Custom available in WebEngage’s dashboard.
onRendered:
When the SDK displays the Campaign on the screen (view event is triggered), this callback is triggered. This will only be triggered for Banner and Text templates.
This will not be triggered for Custom templates,
because they are handled by your application, and in cases where you have called
stopRendering
through WECampaignCallback.
onPlaceholderException
: This callback will get triggered when the campaign showing for a
Property
or
Placeholder
will get failed. If the property is already visible, use this method to hide it or to display some default UI. Kindly refer to
Exceptions
for types of exceptions.
Code will look like below:
dart
import 'package:flutter/material.dart';
import 'package:we_personalization_flutter/we_personalization_flutter.dart';

class Dashboard extends StatefulWidget {
 const Dashboard({Key? key}) : super(key: key);

 @override
 State<Dashboard> createState() => _DashboardState();
}

class _DashboardState extends State<Dashboard> implements WEPlaceholderCallback{
 @override
 Widget build(BuildContext context) {
 return Container(
 color: Colors.red,
 child: WEInlineWidget(
 screenName: "DashboardScreen",
 androidPropertyId: "S1P1",
 iosPropertyId: 1001,
 viewWidth: 0,
 viewHeight: 170,
 placeholderCallback: this,
 ),
 );
 }

 @override
 void onDataReceived(WECampaignData data) {
 // TODO: implement onDataReceived
 }

 @override
 void onPlaceholderException(String campaignId, String targetViewId, String error) {
 // TODO: implement onPlaceholderException
 }

 @override
 void onRendered(WECampaignData data) {
 // TODO: implement onRendered
 }
}
WECampaignCallback: Campaign callbacks
Callbacks can be registered globally in the App class or locally in the different screens. This will be triggered throughout the campaign's lifecycle.
add below line in main.dart file after initilization of
WEPersonalization
method
dart
WEPersonalization().registerWECampaignCallback(this);
then implement
WECampaignCallback
in
_MyAppState
Class
dart
class _MyAppState extends State<MyApp> with WECampaignCallback {

@override
 void onCampaignShown(data) {
 super.onCampaignShown(data);
 print("onCampaignShown $data");
 }

 @override
 void onCampaignClicked(String actionId, String deepLink, data) {
 super.onCampaignClicked(actionId, deepLink, data);
 }

 @override
 void onCampaignPrepared(data) {
 super.onCampaignPrepared(data);
 }

 @override
 void onCampaignException(String? campaignId, String targetViewId, String error) {
 super.onCampaignException(campaignId, targetViewId, error);
 
 }

}
Following are the callback methods available in WECampaignCallback
onCampaignPrepared
: This is the first callback method that is triggered when data for the qualified campaign is retrieved from the WebEngage servers. You can also stop rendering the campaign by calling
stopRendering()
method of
WECampaignData
(generally this can come handy if you want to just retrieve some data and render on your own for layout. This will always be called for your templates (banner, text and custom).
onCampaignShown
: When the SDK displays the Campaign on the screen, this callback is triggered. This will only be triggered for Banner and Text templates and
not
for Custom templates (since they are handled by your application). This callback will also
not
be triggered in cases where you have called
stopRendering
.
onCampaignClicked
: This callback will get triggered when clicked on the campaign view rendered by the SDK. This will only be triggered for Banner and Text templates and
not
Custom templates (since they are handled by your application).
onCampaignException
: This callback will get triggered when the campaign retrieval/showing will get failed.
dart
import 'package:flutter/material.dart';
import 'package:webengage_flutter/webengage_flutter.dart';
import 'package:we_personalization_flutter/WEPersonalization.dart';

void main() {
 runApp(MyApp());
}

class MyApp extends StatefulWidget {
 @override
 MyAppState createState() => MyAppState();
}

class MyAppState extends State<MyApp> with WECampaignCallback{
 @override
 void initState() {
 super.initState();
 WebEngagePlugin _webenagePlugin = WebEngagePlugin();
 WEPersonalization().init();
 WEPersonalization().registerWECampaignCallback(this);
 WEPersonalization().autoHandleCampaignClick(true);
 }
 
 @override
 void onCampaignShown(data) {
 super.onCampaignShown(data);
 print("onCampaignShown $data");
 }

 @override
 void onCampaignClicked(String actionId, String deepLink, data) {
 super.onCampaignClicked(actionId, deepLink, data);
 }

 @override
 void onCampaignPrepared(data) {
 super.onCampaignPrepared(data);
 }

 @override
 void onCampaignException(String? campaignId, String targetViewId, String error) {
 super.onCampaignException(campaignId, targetViewId, error);
 
 }
 
}
Exceptions
You will receive exception details in
onCampaignException
of
WECampaignCallback
&
onPlaceholderException
of
WEPlaceholderCallback
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
Resource fetching falied
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
HashMap <String, dynamic>
Custom key-value pairs defined for the campaign.
Creating Custom Views
Custom View allows you to customize the layouts as per your use case. These are useful in case of creating a layout which is not available out of the box (for example. Carousels).
To implement
WEInlineWidget
without view i.e Custom View, add the below code after
initState
methods inside the Screen
dart
val ID = WEPersonalization().registerWEPlaceholderCallback(
 androidPropertyId,
 osPropertyID,
 screenName,
 placeholderCallback: this);
and in dispose method add below line
dart
WEPersonalization().deregisterWEPlaceholderCallbackById(ID);
The Code will look like this for Custom View integration
dart
import 'package:flutter/material.dart';
import 'package:we_personalization_flutter/WEPersonalization.dart';

class _CustomViewWidgetState extends State<CustomViewWidget>
 implements WEPlaceholderCallback {

 @override
 void initState() {
 super.initState();
 id = WEPersonalization().registerWEPlaceholderCallback(
 widget.customWidgetData.androidPropertyId,
 widget.customWidgetData.iosPropertyID,
 widget.customWidgetData.screenName,
 placeholderCallback: this);
 }

 @override
 Widget build(BuildContext context) {
 return Container(
 );
 }

 @override
 void onDataReceived(WECampaignData data) {
 
 }

 @override
 void dispose() {
 if (id != -1) {
 WEPersonalization().deregisterWEPlaceholderCallbackById(id);
 }
 super.dispose();
 }

 @override
 void onPlaceholderException(
 
 }

 @override
 void onRendered(WECampaignData data) {}
}
Tracking Campaign Impressions and Clicked Events for Custom Views
For
Custom Views
, Personalization SDK will pass the custom data
WECampaignData
, which should be managed/rendered by your application only.
🚧
Please Note
Tracking Impression and tracking Clicks are mandatory steps for Custom view campaigns. If not added then Impression and Click data for these campaigns will not be recorded.
Record Viewed Impression
Impression tracking is simply tracking the number of views each campaign receives. For example, if a user visits the screen and sees a campaign and visits the screen again then they will see the exact same campaign again, two impressions would be counted.
Now,
trackImpression
will allow you to track impressions for your campaign. Kindly, use the mentioned method of
WECampaignData
once the custom view has been shown on the screen by the application.
📘
Recommendation
WECampaignData
will be received both in
onDataReceived
of
WEPlaceholderCallback
and
onCampaignPrepared
of
WECampaignCallback
.
dart
//attributes: any custom Map<String, dynamic> of data you want to record with this event
//data: WECampaignData
data.trackImpression(map:attributes);
Record Click Impression
You can track click impressions whenever the user clicks on the campaign view on the screen.
dart
//attributes: any custom Map<String, dynamic> of data you want to record with this event
//data: WECampaignData
data.trackClick(map : attributes);
Updated
7 months ago
Callbacks
Xamarin.Android
Copy Page
