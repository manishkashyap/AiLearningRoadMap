# Notification Channels

- URL: https://docs.webengage.com/docs/android-push-notification-channels
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android
Push Messaging
Notification Channels
Available only for apps targeting Android 8.0 (API level 26) & above
🚧
WebEngage SDKs 2.7.0 and above support Android push
notification channels
.
Notification channels provide a unified system to help you manage notification behaviour depending on their type. For push notifications sent via WebEngage, you can define the behaviour of the properties mentioned below using notification channels. To do this, add the respective
meta-data
tags in the application element of your
AndroidManifest.xml
as shown below. All push notifications sent via WebEngage are bundled in a single channel.
You can modify default push channel configurations by calling specific methods of
PushChannelConfiguration
class and providing its instance to
WebEngageConfig
during SDK initialization as shown below.
Java
Kotlin
PushChannelConfiguration pushChannelConfiguration = new PushChannelConfiguration.Builder()
 .setNotificationChannelID("offers_channel")
 .setNotificationChannelName("Offers")
 .setNotificationChannelDescription("Product offer weekly updates")
 .setNotificationChannelImportance(3)
 .build();

WebEngageConfig webEngageConfig = new WebEngageConfig.Builder()
 .setDefaultPushChannelConfiguration(pushChannelConfiguration)
 .build();
registerActivityLifecycleCallbacks(new WebEngageActivityLifeCycleCallbacks(this, webEngageConfig));
val pushChannelConfiguration = PushChannelConfiguration.Builder()
 .setNotificationChannelID("offers_channel")
 .setNotificationChannelName("Offers")
 .setNotificationChannelDescription("Product offer weekly updates")
 .setNotificationChannelImportance(3)
 .build()

 val webEngageConfig = WebEngageConfig.Builder()
 .setDefaultPushChannelConfiguration(pushChannelConfiguration)
 .build()
 registerActivityLifecycleCallbacks(
 WebEngageActivityLifeCycleCallbacks(
 this,
 webEngageConfig
 )
 )
To set an existing channel as the default push notification channel, set the channel ID of the existing channel.
ID
This sets the ID for the particular channel. If a channel with the ID is already present, the existing channel will be used and the values for the channel will not be overridden. If channel is not present with the channel ID provided, a new channel will be created with the configured values.
java
Kotlin
pushChannelConfiguration.setNotificationChannelID("offers_channel")
pushChannelConfiguration.setNotificationChannelID("offers_channel")
Name
This is the channel name which is visible to the user.
Java
Kotlin
pushChannelConfiguration.setNotificationChannelName("Offers")
pushChannelConfiguration.setNotificationChannelName("Offers")
Description
This is the channel description which is visible to the user.
Java
Kotlin
pushChannelConfiguration.setNotificationChannelDescription("Product offer weekly updates")
pushChannelConfiguration.setNotificationChannelDescription("Product offer weekly updates")
Importance
Sets one of five importance levels that configure the amount a channel can interrupt a user, ranging from
IMPORTANCE_NONE
(0) to
IMPORTANCE_HIGH
(4). The default importance level is 3 which displays everywhere, makes noise, but doesn't visually intrude on the user.
Java
Kotlin
pushChannelConfiguration.setNotificationChannelImportance(3)
pushChannelConfiguration.setNotificationChannelImportance(3)
Light Color
Sets the notification light color for notifications posted to this channel if the device supports this feature.
enableLights
is automatically called by WebEngage SDK when you set this tag.
Java
Kotlin
pushChannelConfiguration.setNotificationChannelLightColor(Color.parseColor("#ff0000"))
pushChannelConfiguration.setNotificationChannelLightColor(Color.parseColor("#ff0000"))
Lock Screen Visibility
Sets whether notifications posted to this channel appear on the lockscreen or not, and if so, whether they appear in a redacted form. See e.g.
VISIBILITY_SECRET
.
Java
Kotlin
pushChannelConfiguration.setNotificationChannelLockScreenVisibility(Notification.VISIBILITY_PUBLIC)
pushChannelConfiguration.setNotificationChannelLockScreenVisibility(Notification.VISIBILITY_PUBLIC)
Show Badge
Sets whether notifications posted to this channel can appear as application icon badges in a Launcher.
Java
Kotlin
pushChannelConfiguration.setNotificationChannelShowBadge(true)
pushChannelConfiguration.setNotificationChannelShowBadge(true)
Sound
Sets the sound that should be played for notifications posted to this channel and its audio attributes. Notification channels with an importance of at least
IMPORTANCE_DEFAULT
(3) should have a sound. Set the name of the file without extension through
PushChannelConfiguration
. This file must be in the
resources/raw
folder of your app.
Java
Kotlin
pushChannelConfiguration.setNotificationChannelSound("FILENAME")
pushChannelConfiguration.setNotificationChannelSound("FILENAME")
Vibration
Sets whether notification posted to this channel should vibrate.
Java
Kotlin
pushChannelConfiguration.setNotificationChannelVibration(true)
pushChannelConfiguration.setNotificationChannelVibration(true)
Group
Sets the group this channel belongs to. Group information is only used for presentation on the user's device, not for behavior.
value
is the
group ID
of the group that you want to use.
Java
Kotlin
pushChannelConfiguration.setNotificationChannelGroup("GROUP_ID") //Provide a valid group ID
pushChannelConfiguration.setNotificationChannelGroup("GROUP_ID") //Provide a valid group ID
By default, these properties are assigned the following values.
Property
Value / Status
ID
we_wk_push_channel
Name
Marketing
Description
Not assigned
Importance
IMPORTANCE_DEFAULT
Light color
Light is disabled
Lock screen visibility
VISIBILITY_PUBLIC
Show badge
true
Sound
System default
Vibration
true
Group
Not assigned
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
Customizing push notifications
Copy Page
