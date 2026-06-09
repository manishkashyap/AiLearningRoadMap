# AWS S3

- URL: https://docs.webengage.com/docs/aws-s3
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Partners Integrations
AWS S3
AWS S3 offers industry-leading scalability, data availability, security, and performance.
Recognizing the importance of seamless data transfer between systems to support various data-driven operations, we have initiated efforts to develop data streaming capabilities. These capabilities will facilitate the export of data from WebEngage to AWS S3.
How to export Events from WebEngage to AWS S3?
On your WE dashboard navigate to the Data Platform tab, and Integrations sub-tab, and locate Data Destinations.
Choose AWS S3 and click on Configure.
Once you’ve been redirected to this page, click on the ➕ button, and create your connection by providing the following details.
Connection Name
: A unique name to identify your connection. This helps you distinguish between different connections you may have set up.
Bucket Name
: The name of the storage bucket where your data will be stored. This typically refers to a cloud storage service like AWS S3, where a bucket is a container for data.
Region Name
: The geographical region where your bucket is hosted. This is important for latency and compliance with regional data storage regulations.
Access Key
: A unique identifier assigned to you by your cloud service provider, used to authenticate your requests to access your bucket.
Secret Access Key
: A secret key paired with your access key, used to securely authenticate your requests. This key should be kept confidential.
File Path
: The specific location within your bucket where the data files will be stored or retrieved. This could be a directory path or a file name.
You can also edit your connection details by clicking on the action button adjacent to the connection on the listing page.
Once the connection is established you can now start exporting the events using this connection.
Navigate to the Data Platform tab, and Data Management sub-tab, and locate Data exports.
Click on the ➕ , and provide the following information to establish the connection between WebEngage and AWS S3.
Export Name
: A name to identify the export.
Using Connection
: In this drop down, you get to choose which partner’s connection you wish to use.
Export Events
: You are provided with 3 options i.e. All Events, All Campaign Events, Selected Events Only,
Cadence
: Choose a time span between ‘Near Real Time’, ‘Every 15, 30mins, 1, 6, 12, 24 hours’.
File Format
File generated would have new-line delimited JSON format - Each exported record’s JSON will occupy a single line and separated using a new line.
Attributes with null values will not be exported. No option to include null values.
At a high level, schema will be:
Key
What It Means
user_id
System-generated unique ID assigned to a known user
anonymous_id
System-generated unique ID assigned to anonymous/unknown users.
event_name
Name of the event
category
Specifies whether the event is a
system
event (
System Events
) or an
application
event (
custom-events
).
license_code
Your WebEngage License Code
event_time
The timestamp of the event, recorded in Epoch (Unix) time.
system_data
Map of event's
System Attributes
and their values
event_data
Map of event's
Custom Attributes
and their values
For example,
System Event: Push (Mobile) Received
JSON
{
 "user_id": "1519021150",
 "anonymous_id": "c2c605d7fb04594475d216f9139c362a",
 "event_name": "push_notification_received",
 "category": "system",
 "license_code": "stg~aa133b83",
 "event_time": "2023-01-11T11:35:28+0000",
 "system_data": {
 "app_version": "3.14.0",
 "release": "12",
 "language": "English",
 "device_type": "Mobile",
 "locale": "en_IN",
 "manufacturer": "Xiaomi",
 "viewport_height": 2179,
 "app_version_code": 20,
 "scope": "null_6cdd49fd-9c87-4e02-8b20-f13a77dac0a0#2:1673436926571",
 "sdk_version": 40000,
 "model": "M2007J20CI",
 "variation_id": "h156f5",
 "brand": "POCO",
 "screen_title": "Staging",
 "id": "20hmsco",
 "os_version": "12",
 "ip": "43.231.236.166",
 "api_version": 31,
 "sdk": "ANDROID",
 "viewport_width": 1080,
 "screen_path": "com.webengage.test.views.HomeActivity",
 "os_name": "Android",
 "device": "karna"
 },
 "event_data": {
 "provider": "FCM",
 "amplified": false
 }
}
System Event: SMS Queued
JSON
{
 "user_id": "1519021150",
 "anonymous_id": "c2c605d7fb04594475d216f9139c362a",
 "event_name": "sms_queued",
 "category": "system",
 "license_code": "stg~aa133b83",
 "event_time": "2023-03-20T05:15:28+0000",
 "system_data": {
 "id": "3e48iq5",
 "variation_id": "12m7sbb",
 "ip": "192.168.124.7",
 "scope": "~1afeac1g7gi3ifi_fc_d466dbd9-5916-4953-a63c-f0bd705f581b:1673600979748"
 },
 "event_data": {
 "reason": "CAMPAIGN_DAILY_LIMIT",
 "qc": 1,
 "bucket_value": 54,
 "new_time_to_live": 223780,
 "send_next": "2023-01-13T19:00:00+0000"
 }
}
System Event: App Installed
JSON
{
 "user_id": "1519021150",
 "anonymous_id": "c2c605d7fb04594475d216f9139c362a",
 "event_name": "app_installed",
 "category": "system",
 "license_code": "stg~aa133b83",
 "event_time": "2023-05-29T02:06:28+0000",
 "interface_id": "com.test.app|0179B18A887EACF1686D6612B8BA40CB",
 "system_data": {
 "country": "India",
 "app_version": "1.11.79",
 "city": "Kanpur",
 "release": "13",
 "device_type": "Mobile",
 "language": "Hindi",
 "locale": "hi",
 "manufacturer": "Motorola",
 "viewport_height": 2174,
 "app_version_code": 210011179,
 "sdk_version": 40900,
 "model": "moto g42",
 "brand": "Motorola",
 "campaign_source": "google-play",
 "campaign_medium": "organic",
 "screen_title": "Test",
 "ip": "127.0.0.1",
 "os_version": "13",
 "api_version": 33,
 "viewport_width": 1080,
 "screen_path": "com.test.app.SplashActivity",
 "os_name": "Android",
 "sdk": "ANDROID",
 "region": "Uttar Pradesh",
 "device": "Mobile"
 }
}
Custom Event: Bill Payment
JSON
{
 "user_id": "1519021150",
 "anonymous_id": "c2c605d7fb04594475d216f9139c362a",
 "event_name": "Bill Payment",
 "category": "application",
 "license_code": "stg~aa133b83",
 "event_time": "2023-08-25T04:15:12+0000",
 "interface_id": "mobile_app_android_v1",
 "system_data": {
 "country": "USA",
 "region": "California",
 "city": "San Francisco",
 "locality": "Downtown",
 "postal_code": "94103",
 "ip": "192.168.1.1",
 "latitude": "37.7749",
 "longitude": "-122.4194",
 "app_version": "1.2.3",
 "app_version_code": "123",
 "release": "10.0",
 "sdk_version": "30",
 "api_version": "3.1",
 "os_version": "14.2",
 "os_name": "Android",
 "browser_name": "Chrome",
 "browser_version_code": "86",
 "browser_version": "86.0.4240.111",
 "device_type": "Smartphone",
 "device": "Pixel 4",
 "language": "en-US",
 "locale": "en_US",
 "manufacturer": "Google",
 "model": "Pixel 4 XL",
 "brand": "Google",
 "viewport_height": "640",
 "viewport_width": "360",
 "screen_name": "MainScreen",
 "screen_title": "Main",
 "screen_path": "/main",
 "page_url": "https://example.com",
 "push_notification_content": "You have a new message",
 "scope": "global",
 "journey_id": "journey_123",
 "id": "exp_456",
 "variation_id": "event_789",
 "referrer_type": "organic",
 "campaign_source": "google",
 "campaign_medium": "cpc",
 "campaign_id": "cmp_12345",
 "sdk": "ANDROID"
 },
 "event_data": {
 "Account Id": "26576576125381",
 "Amount": "5000",
 "Status": "Sucess"
 }
}
Updated
7 months ago
Amplitude
Getting Started
Copy Page
