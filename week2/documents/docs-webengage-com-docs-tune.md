# TUNE

- URL: https://docs.webengage.com/docs/tune
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Partners Integrations
TUNE
This integration allows WebEngage to capture attribution information from TUNE. Here's how you can
configure Webengage as an Internal Partner
in your TUNE dashboard.
Step 1: Select WebEngage as Internal Partner
As highlighted below, click the
Add Postback URL
to get started.
Step 2: Select Mobile App(s)
As shown, select All Mobile Apps against this field to ensure that data flows in for all your apps integrated with WebEngage.
Step 3: Configure Event Type
As highlighted above, select
Install
under the field,
Event Type.
Attribution Option:
As shown below, select the option,
Send all events attributed...
against this field to ensure that all the data tracked for all your apps via TUNE is passed on to your WebEngage account.
Step 4: Add Postback URL
At WebEngage, you can choose to host all your data at three data centers - US, Saudi Arabia or India. By default, all data is stored in our US Data Center. However, you can choose to host it at our Saudi Arabia or India Data Center by specifying the same in your contractual agreement.
🚧
Identifying Your Data Center
If your WebEngage dashboard URL starts with,
dashboard.webengage.com
, then it means that you're using our US data center.
If your WebEngage dashboard link starts with,
dashboard.in.webengage.com
, then it means that you're using our India data center.
If your WebEngage dashboard link starts with,
dashboard.ksa.webengage.com
, then it means that you're using our Saudi Arabia data center.
Depending on your data center, paste the following URL under the field,
Postback URL
in your TUNE dashboard.
Postback URL for US Data Center
https://c.webengage.com/installs/integration?idfa={ios_ifa}&advertiserId={google_aid_alphanumeric_lower}&android-id={android_id}&app-id={package_name}&install-unix-ts={install_datetime}&click-ts={click_timestamp}&campaign={campaign_id}&country-code={country_code}&device-brand={device_brand}&carrier={device_carrier}&ip={device_ip}&device-model={device_model}&language={language}&appsflyer-device-id={mat_id}&app-version-name={package_app_version}&user-agent={user_agent}&idfv={ios_ifv}&os-version-name={os_version}&app-version={app_version}&app-name={package_app_name}&source=tune&http_headers[Authorization]=bearer WEBENGAGE_API_KEY
Postback URL for India Data Center
https://c.in.webengage.com/installs/integration?idfa={ios_ifa}&advertiserId={google_aid_alphanumeric_lower}&android-id={android_id}&app-id={package_name}&install-unix-ts={install_datetime}&click-ts={click_timestamp}&campaign={campaign_id}&country-code={country_code}&device-brand={device_brand}&carrier={device_carrier}&ip={device_ip}&device-model={device_model}&language={language}&appsflyer-device-id={mat_id}&app-version-name={package_app_version}&user-agent={user_agent}&idfv={ios_ifv}&os-version-name={os_version}&app-version={app_version}&app-name={package_app_name}&source=tune&http_headers[Authorization]=bearer WEBENGAGE_API_KEY
Postback URL for Saudi Arabia Data Center
https://c.ksa.webengage.com/installs/integration?idfa={ios_ifa}&advertiserId={google_aid_alphanumeric_lower}&android-id={android_id}&app-id={package_name}&install-unix-ts={install_datetime}&click-ts={click_timestamp}&campaign={campaign_id}&country-code={country_code}&device-brand={device_brand}&carrier={device_carrier}&ip={device_ip}&device-model={device_model}&language={language}&appsflyer-device-id={mat_id}&app-version-name={package_app_version}&user-agent={user_agent}&idfv={ios_ifv}&os-version-name={os_version}&app-version={app_version}&app-name={package_app_name}&source=tune&http_headers[Authorization]=bearer WEBENGAGE_API_KEY
You can use
macros
in these URLs, which are dynamically populated with the appropriate values that
Attribution Analytics
collects from the device (or receives on click, etc.).
Please ensure that you replace
WEBENGAGE_API_KEY
(placed at the end of the URL) with your
WebEngage API Key.
As shown below, it can be found under
Data Platform > Integrations > REST API
in your dashboard.
Click to enlarge
Congratulations! You have successfully integrated TUNE with WebEngage :)
Please feel free to drop in a few lines at
[email protected]
in case you have any queries or feedback. We're always just an email away!
Updated
7 months ago
AppsFlyer
Adjust
Copy Page
