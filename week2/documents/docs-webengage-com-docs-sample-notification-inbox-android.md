# Sample Notification Inbox Module

- URL: https://docs.webengage.com/docs/sample-notification-inbox-android
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Sample Notification Inbox Module
The Notification Inbox sample module is an easy to use plug-and-play solution created by WebEngage to help client integrate a Notification Inbox within their application without having to build it from scratch. This module provides lots of flexibility and customization to help clients in giving the Inbox the look and feel similar to their app.
After Integrating this module clients will be able to send copy of their push notifications within their App Inbox.
🚧
Please Note
Integrating this module isn't a pre-requisite for enabling Copy to Inbox feature. Clients with their self created Notification Inbox will be able to send copy of their push notifications as well.
Integration of WebEngage Android Notification Inbox Module
Follow the steps below to integrate the WebEngage Android Notification Inbox Module into your project:
Step 1: Clone the Code
Go to the WebEngage Android Notification Inbox Module
GitHub repository
and clone the code to your local machine.
Step 2: Copy the Module
Copy or import the
weNotificationInboxModule
module from the cloned code into your project.
Step 3: Update
settings.gradle
Open the
settings.gradle
file in the root of your project and add the following line:
include ':weNotificationInboxModule'
Step 4: Update
app/build.gradle
Open the
app/build.gradle
file and add the following line to the dependencies block:
implementation project(':weNotificationInboxModule')
Adding WebEngage's Notification-inbox-module
Navigate to the WebEngage notification inbox module by calling the
navigateToWEInboxModule()
method on click of a button
Kotlin
Java
import com.webengage.notification_inbox_plugin.WEInboxModule
...
WEInboxModule.get().navigateToWEInboxModule(context)
import com.webengage.notification_inbox_plugin.WEInboxModule
...
WEInboxModule.get().navigateToWEInboxModule(context);
👍
Congratulations
You have now successfully integrated our Notification Sample Module.
Get Notification Count
To retrieve the updated notification count of unread messages, add the following code snippet to your
onResume
method of
Activity
:
Kotlin
Java
override fun onResume() {
 super.onResume()
 ...
 WENotificationInbox.get(this.applicationContext, WEInboxConfig(true))
 .getUserNotificationCount(this, object : WEInboxCallback<String> {
 override fun onSuccess(result: String) {
 // Attach result string to your TextView
 }

 override fun onError(errorCode: Int, error: Map<String, *>) {
 // Handle the error
 }
 })
}
@Override
protected void onResume() {
 super.onResume();
 // ...
 WENotificationInbox.get(getApplicationContext(), new WEInboxConfig(true))
 .getUserNotificationCount(MainActivity.this, new WEInboxCallback<String>() {
 @Override
 public void onSuccess(String result) {
 // Attach result string to your TextView
 }

 @Override
 public void onError(int errorCode, Map<String, ?> error) {
 // Handle the error
 }
 });
}
Default Notification Layouts
Currently this module supports Banner and Text Layouts. Below are the styles for Text and Banner layout. If you would prefer, you can overwrite these styles to create a look and feel that better suits your app.
Navigate to
weNotificationInboxModule/src/main/res/values/styles.xml
Identify the style you want to modify, example:
WebEngage.NI.Text.Title
Copy all the styles to your
app's styles.xml
file and update the desired properties
Sample code:
<style name="WebEngage.NI.Text.Title">
 <item name="android:textSize">30sp</item>
 <item name="android:layout_margin">10dp</item>
 <item name="android:layout_width">match_parent</item>
 <item name="android:layout_height">wrap_content</item>
 <item name="android:textStyle">bold</item>
 <item name="android:maxLines">2</item> 
 <item name="android:textColor">#339F04</item>
</style>
Following are details for each layout:
Text Layout
Reference No.
Variable Name
1
WebEngage.NI.Text.Title
2
WebEngage.NI.Text.MessageDescription
3
WebEngage.NI.Text.Time
4
WebEngage.NI.Text.ReadButton
/
WebEngage.NI.Text.UnReadButton
5
WebEngage.NI.Text.DeleteButton
Card
WebEngage.NI.Text.CardView
Banner Layout
Reference No.
Variable Name
1
WebEngage.NI.Banner.CardImageView
2
WebEngage.NI.Banner.Title
3
WebEngage.NI.Banner.MessageDescription
4
WebEngage.NI.Banner.Time
5
WebEngage.NI.Banner.ReadButton
/
WebEngage.NI.Banner.UnReadButton
6
WebEngage.NI.Banner.DeleteButton
Card
WebEngage.NI.Banner.CardView
📘
Please Note
WebEngage supports four types of push notification layouts: banner, text, carousel, and rating. However, the current version of the notification-inbox-module only supports text and banner layouts. If your application receives notifications with carousel or rating layouts, they will be displayed as text layouts by default, which can be overridden by your own custom layouts.
Customizing Default Properties
To customize the behavior of the WebEngage Notification Inbox Module’s default layouts by creating your own class, follow these steps:
Step 1: Create Your Own Class
Create a new class called
CustomWEInboxAdapter
and extend it with
WEInboxAdaptercustomizing
. This class will be responsible for Customizing the adapter’s behaviour.
Kotlin
Java
import com.webengage.notification_inbox_plugin.view.WEInboxAdapter
...
class CustomWEInboxAdapter : WEInboxAdapter() {
 // Add your customizations and overrides here
}
import com.webengage.notification_inbox_plugin.view.WEInboxAdapter;
...

public class CustomWEInboxAdapter extends WEInboxAdapter {
 // Add your customizations and overrides here
}
Step 2: Override the
onBindViewHolder
Method
Inside the
CustomWEInboxAdapter
class, override the
onBindViewHolder
method. This method is called when binding data to each item in the adapter.
Kotlin
JSON
override fun onBindViewHolder(
 holder: RecyclerView.ViewHolder,
 mNotificationList: ArrayList<WEInboxMessage>,
 position: Int
) {
 super.onBindViewHolder(holder, mNotificationList, position)
 mWEInboxDataList = mNotificationList
 if (mWEInboxDataList != null && mWEInboxDataList.size > 0) {
 when (holder) {
 is ViewHolderTextObject -> {
 holder.mTitleTextView.text = "Custom Header" // Updating Title Text
 holder.mContainer.setBackgroundColor(ContextCompat.getColor(mContext!!, R.color.colorAccent)) // Change background color of the card
 holder.mTimeStamp.visibility = View.GONE // Hide Timestamp
 }
 else -> super.onBindViewHolder(holder, mNotificationList, position)
 }
 }
}
@Override
public void onBindViewHolder(RecyclerView.ViewHolder holder, ArrayList<WEInboxMessage> mNotificationList, int position) {
 super.onBindViewHolder(holder, mNotificationList, position);
 mWEInboxDataList = mNotificationList;
 if (mWEInboxDataList != null && mWEInboxDataList.size() > 0) {
 if (holder instanceof ViewHolderTextObject) {
 ViewHolderTextObject textHolder = (ViewHolderTextObject) holder;
 textHolder.mTitleTextView.setText("Custom Header"); // Updating Title Text
 textHolder.mContainer.setBackgroundColor(ContextCompat.getColor(mContext, R.color.colorAccent)); // Change background color of the card
 textHolder.mTimeStamp.setVisibility(View.GONE); // Hide Timestamp
 } else {
 super.onBindViewHolder(holder, mNotificationList, position);
 }
 }
}
Step 3: Set
CustomWEInboxAdapter
as the Adapter for WebEngage Notification Inbox Module
To set your
CustomWEInboxAdapter
as the adapter for the WebEngage Notification Inbox Module in the
onCreate method
of your MainActivity, use the
WEInboxDataRepository.setWEAdapter()
method, as shown below:
Kotlin
Java
override fun onCreate(savedInstanceState: Bundle?) {
 super.onCreate(savedInstanceState)
 setContentView(R.layout.activity_main)

 // Create an instance of your CustomWEInboxAdapter
 val customAdapter = CustomWEInboxAdapter()

 // Set your CustomWEInboxAdapter as the adapter for the WebEngage Notification Inbox Module
 WEInboxModule.get().setWEAdapter(customAdapter)

 // Continue with the rest of your activity initialization
 // ...
}
@Override
protected void onCreate(Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 setContentView(R.layout.activity_main);

 // Create an instance of your CustomWEInboxAdapter
 CustomWEInboxAdapter customAdapter = new CustomWEInboxAdapter();

 // Set your CustomWEInboxAdapter as the adapter for the WebEngage Notification Inbox Module
 WEInboxModule.get().setWEAdapter(customAdapter);

 // Continue with the rest of your activity initialization
 // ...
}
Customize the Time Format
Customize the received time format of messages based on your preference. You have the flexibility to choose a different date format for each layout. In the example below, the text and banner layouts have separate patterns available. If you do not initialize a custom format for any or both of the layouts, the default format provided by WebEngage will be used.
Kotlin
Java
override fun onCreate(savedInstanceState: Bundle?) {
 ...
 WEInboxModule.get().updateDateFormat("MM-dd HH:mm:ss", WENotificationInboxConstants.TEXT)
 WEInboxModule.get().updateDateFormat("dd/mm/yyyy", WENotificationInboxConstants.BANNER)
 ...
}
@Override
protected void onCreate(Bundle savedInstanceState) {
 ...
 // Create an instance of your CustomWEInboxAdapter
 CustomWEInboxAdapter customAdapter = new CustomWEInboxAdapter();

 // Set your CustomWEInboxAdapter as the adapter for the WebEngage Notification Inbox Module
 WEInboxModule.get().setWEAdapter(customAdapter);

 // Continue with the rest of your activity initialization
 // ...
}
Creating Custom Layout
You can add your own custom layout to the WebEngage Notification Inbox Module for all 4 layouts.
Create a new class. Let’s name it
CustomWEInboxAdapter
and extend it with
WEInboxAdapter
Kotlin
Java
import com.webengage.notification_inbox_plugin.view.WEInboxAdapter

class CustomWEInboxAdapter : WEInboxAdapter() {
 // Add your customizations and overrides here
}
import com.webengage.notification_inbox_plugin.view.WEInboxAdapter;

public class CustomWEInboxAdapter extends WEInboxAdapter {
 // Add your customizations and overrides here
}
Override the following methods in the
CustomWEInboxAdapter
class:
createViewHolder(parent: ViewGroup, type: Int)
: In this method, create a new custom ViewHolder object by inflating Layout based on the type received as an argument. You can create a separate class for your custom viewholder.
onBindViewHolder(holder: RecyclerView.ViewHolder, mNotificationList: ArrayListWEInboxMessage>, position: Int)
: In this method, handle the binding of data to the custom ViewHolder object. You can access the ViewHolder object that you created in the createViewHolder method and control the view based on it. The mNotificationList parameter will contain a list of notifications.
getViewType(notificationList: ArrayListWEInboxMessage>, position: Int)
: This method allows you to determine your own view type apart from the default types (0 for banner, 1 for text, 2 for carousel, and 3 for rating). The same viewType will reflect in the createViewHolder’s type. You can define your custom view type based on the notificationList and position parameters.
CustomViewHolderObject
: This is your custom ViewHolder class that should initialize the layout widgets needed to bind the view.
Listeners: You can create listeners for actions such as read, unread, and delete. Implement the following methods to access the listeners:
Kotlin
Java
override fun getReadListener(weInboxItemRead: WebEngageRecyclerViewAdapter.WEInboxItemRead?)
override fun getUnReadListener(weInboxItemUnread: WebEngageRecyclerViewAdapter.WEInboxItemUnread?)
override fun getDeleteListener(weInboxItemDelete: WebEngageRecyclerViewAdapter.WEInboxItemDelete?)
public void getReadListener(WebEngageRecyclerViewAdapter.WEInboxItemRead weInboxItemRead)
public void getUnReadListener(WebEngageRecyclerViewAdapter.WEInboxItemUnread weInboxItemUnread)
public void getDeleteListener(WebEngageRecyclerViewAdapter.WEInboxItemDelete weInboxItemDelete)
Trigger Read/Unread/Delete Methods: You can trigger these actions on your listeners when required.
For example:
Kotlin
Java
mWeInboxItemRead.onItemRead(null, position)
mWeInboxItemUnread.onItemUnread(null, position)
mWeInboxItemDelete.onItemDelete(null, position)
mWeInboxItemRead.onItemRead(null, position);
mWeInboxItemUnread.onItemUnread(null, position);
mWeInboxItemDelete.onItemDelete(null, position);
Finally, set your
CustomWEInboxAdapter
as the adapter for the WebEngage Notification Inbox Module in the
onCreate method of your MainActivity
and and use the
WEInboxDataRepository.setWEAdapter()
method, as shown below:
Kotlin
Java
override fun onCreate(savedInstanceState: Bundle?) {
 super.onCreate(savedInstanceState)
 setContentView(R.layout.activity_main)

 // Create an instance of your CustomWEInboxAdapter
 val customAdapter = CustomWEInboxAdapter()

 // Set your CustomWEInboxAdapter as the adapter for the WebEngage Notification Inbox Module
 WEInboxModule.get().setWEAdapter(customAdapter)

 // Continue with the rest of your activity initialization
}
@Override
protected void onCreate(Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 setContentView(R.layout.activity_main);

 // Create an instance of your CustomWEInboxAdapter
 CustomWEInboxAdapter customAdapter = new CustomWEInboxAdapter();

 // Set your CustomWEInboxAdapter as the adapter for the WebEngage Notification Inbox Module
 WEInboxModule.get().setWEAdapter(customAdapter);

 // Continue with the rest of your activity initialization
}
Example of a Custom Adapter Where user is overriding the new customTextViewHolder
Kotlin
Java
class CustomWEInboxAdapter : WEInboxAdapter() {

 private var mWEInboxDataList: List<WEInboxMessage>? = null
 private var mWeInboxItemRead: WebEngageRecyclerViewAdapter.WEInboxItemRead? = null

 // onCreateViewHolder -> Redefine your Layout Type
 override fun createViewHolder(parent: ViewGroup, type: Int): RecyclerView.ViewHolder {
 return when (type) {
 // inflating layout custom_we_text_inbox
 WENotificationInboxConstants.VIEW_TYPE_TEXT -> return CustomViewHolderTextObject(
 LayoutInflater.from(parent.context)
 .inflate(R.layout.custom_we_text_inbox, parent, false)
 )
 // if required for banner/Carousel/Rating -> create a layout and return with ViewHolder
 else ->
 super.createViewHolder(parent, type)
 }
 }

 // Client can Initialize Views and modify based on their preference
 override fun onBindViewHolder(
 holder: RecyclerView.ViewHolder,
 mNotificationList: ArrayList<WEInboxMessage>,
 position: Int
 ) {
 super.onBindViewHolder(holder, mNotificationList, position)
 mWEInboxDataList = mNotificationList
 if (mWEInboxDataList != null && mWEInboxDataList?.size!! > 0) {
 // Updating only Text Type and rest layouts have default layouts
 when (holder) {
 is CustomViewHolderTextObject -> {
 val pushNotificationTemplateData =
 mWEInboxDataList?.get(position)?.message as PushNotificationTemplateData
 // Title Text
 holder.customTitle.text =
 WEHtmlParserInterface().fromHtml(pushNotificationTemplateData.title)
 //ButtonListeners
 holder.customReadButton.setOnClickListener {
 markAsRead(position)
 }
 }
 }
 }
 }

 private fun markAsRead(position: Int) {
 if (mWeInboxItemRead != null) {
 mWeInboxItemRead!!.onItemRead(null, position)
 }
 }

 override fun getReadListener(weInboxItemRead: WebEngageRecyclerViewAdapter.WEInboxItemRead?) {
 mWeInboxItemRead = weInboxItemRead
 super.getReadListener(weInboxItemRead)
 }

 class CustomViewHolderTextObject(itemView: View) : RecyclerView.ViewHolder(itemView) {
 val customTitle: TextView =
 itemView.findViewById(R.id.we_notification_custom_inbox_text_title)
 val customReadButton: Button =
 itemView.findViewById(R.id.we_notification_custom_inbox_text_markReadButton)
 }
}
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import com.webengage.notification_inbox_plugin.view.WEInboxAdapter;
import com.webengage.sdk.android.actions.render.PushNotificationTemplateData;

import java.util.ArrayList;
import java.util.List;

public class CustomWEInboxAdapter extends WEInboxAdapter {

 private List<WEInboxMessage> mWEInboxDataList;
 private WebEngageRecyclerViewAdapter.WEInboxItemRead mWeInboxItemRead;

 @Override
 public RecyclerView.ViewHolder createViewHolder(ViewGroup parent, int type) {
 switch (type) {
 case WENotificationInboxConstants.VIEW_TYPE_TEXT:
 // inflating layout custom_we_text_inbox
 View textObjectView = LayoutInflater.from(parent.getContext())
 .inflate(R.layout.custom_we_text_inbox, parent, false);
 return new CustomViewHolderTextObject(textObjectView);
 // if required for banner/Carousel/Rating -> create a layout and return with ViewHolder
 default:
 return super.createViewHolder(parent, type);
 }
 }

 @Override
 public void onBindViewHolder(RecyclerView.ViewHolder holder, ArrayList<WEInboxMessage> mNotificationList, int position) {
 super.onBindViewHolder(holder, mNotificationList, position);
 mWEInboxDataList = mNotificationList;
 if (mWEInboxDataList != null && mWEInboxDataList.size() > 0) {
 // Updating only Text Type and rest layouts have default layouts
 if (holder instanceof CustomViewHolderTextObject) {
 CustomViewHolderTextObject customHolder = (CustomViewHolderTextObject) holder;
 PushNotificationTemplateData pushNotificationTemplateData = (PushNotificationTemplateData) mWEInboxDataList.get(position).getMessage();
 // Title Text
 customHolder.customTitle.setText(WEHtmlParserInterface().fromHtml(pushNotificationTemplateData.getTitle()));
 // ButtonListeners
 customHolder.customReadButton.setOnClickListener(new View.OnClickListener() {
 @Override
 public void onClick(View v) {
 markAsRead(position);
 }
 });
 }
 }
 }

 private void markAsRead(int position) {
 if (mWeInboxItemRead != null) {
 mWeInboxItemRead.onItemRead(null, position);
 }
 }

 @Override
 public void getReadListener(WebEngageRecyclerViewAdapter.WEInboxItemRead weInboxItemRead) {
 mWeInboxItemRead = weInboxItemRead;
 super.getReadListener(weInboxItemRead);
 }

 public static class CustomViewHolderTextObject extends RecyclerView.ViewHolder {
 public TextView customTitle;
 public Button customReadButton;

 public CustomViewHolderTextObject(View itemView) {
 super(itemView);
 customTitle = itemView.findViewById(R.id.we_notification_custom_inbox_text_title);
 customReadButton = itemView.findViewById(R.id.we_notification_custom_inbox_text_markReadButton);
 }
 }
}
Updated
7 months ago
Getting Started
Copy Page
