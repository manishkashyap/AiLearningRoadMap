# UTM Parameters

- URL: https://knowledgebase.webengage.com/docs/utm-parameters
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

UTM Parameters
Urchin Tracking Module(UTM) feature adds tracking tags to campaign links in Email, SMS, Web Push, On-site Notification, Web In-line, and WhatsApp, helping you see where your traffic is coming from. Keep reading to know more about how to set this up for your dashboard.
What is UTM and why do you need it?
UTM parameters are tags added to your URLs to identify traffic sources for analysis, especially in Google Analytics. WebEngage has now introduced the capability to automatically add these UTM parameters to links in your campaigns for channels such as Email, SMS, Web Push, On-site Notification, Web In-line, and WhatsApp.
How to Set it up?
Here’s how you can set up UTM for your campaign links.
Begin by enabling UTM at the global level by following the steps below.
Global Level Set Up (Global Level)
You can enable the automatic addition of UTM parameters in the Navigation Panel under Configurations and clicking on the ‘UTM’ option.
On clicking that, you will see the UTM setup modal page.
You can enable the switch to set up the UTM Parameters
Once enabled, you can see a few predefined UTM parameters, such as
utm_source
,
utm_medium
, that are always enabled and
utm_campaign
,
utm_content
, which can be manually enabled.
You can also add your own custom UTM parameters with specific names.
📘
Note
You can set up to
8 UTM parameters
, out of which 2 are enabled by default.
Campaign Value & Journey Value
You can choose to assign Static or Dynamic values to your UTM parameters.
Static Values
- Alphanumeric values which are hardcoded and used in all campaign links.
Dynamic Values
- Are more personalized values for each Campaign and Journey, you can choose them from the drop-down.
The Campaign Value drop-down has 4 personalized values, they are:
Campaign Channel Name
: The channel name of the campaign appends as a UTM parameter.
Campaign Name
: Campaign name appends as a UTM parameter.
Campaign ID
: Campaign ID appends as a UTM parameter.
Campaign Conversion Event
: Campaign Conversion Event name appends as a UTM parameter. If the conversion event is not added, then ‘Null’ would be passed.
Journey Value
; This column gives values to be passed for the Journey campaign’s UTM parameters. Journey values can also be Static or Dynamic, like Campaign Values.
Journey Values have 6 personalized values:
Journey Name
: Journey name of the campaign appends as a UTM parameter.
Journey ID
: The Journey ID of the campaign appends as a UTM parameter.
Journey Campaign Channel
: The channel name of the Journey campaign appends as a UTM parameter.
Journey Campaign Name
: The campaign name of the Journey campaign appends as a UTM parameter.
Journey Campaign ID
: The campaign ID of the Journey campaign appends as a UTM parameter.
Journey Conversion Event
: The Journey Conversion Event name appends as a UTM parameter. If the conversion event is not added, then ‘Null’ would be passed.
Restrict UTM to Specific Domains
You can control which CTAs have UTM parameters by restricting them to selected domains. This ensures attribution for owned links while keeping external links unaffected.
How does it work?
👍
Use Cases
🔹
Content Publishers
A media company sends newsletters with links to both their website (
newsportal.com
) and external sources. By restricting UTMs to their domain, they get clear insights into reader engagement—without interfering with partner analytics.
🔹
Travel & Hospitality
A travel agency runs a promo campaign with links to both their website (
travelsite.com
) and third-party booking sites. Since they only need to track engagement with their content, they apply UTMs only to their domain, ensuring accurate attribution while leaving external links untouched.
The “Domains to Include for UTM Parameters” field is available in Global and Campaign Setup.
Specify the domains for which UTM parameters should be appended. For multiple domains, separate them with commas. Use domain format only (e.g., example.com, sub.example.com) without https:// or
www
.
Click on save, and you will receive a prompt of confirmation prompt
This is supported for Auto-add UTM channels
Campaign Level Set Up
Once the general UTM setup is complete, UTM parameters are enabled by default for the supported channels. You can edit the UTM parameter for each campaign if you wish to, from the Campaign creation message page.
When navigating to the message tab of the campaign from any channel, scroll down past the message section, and you will find the UTM parameters section for the campaign level setup. You can switch on or off the UTM parameters section by using the toggle switch.
📘
Note
Any updates or edits made to the UTM parameters here will be applicable for this campaign only. You can disable it at the campaign level.
Similar to the global level set-up,
utm_source
,
utm_medium
, which are always enabled and
utm_campaign
,
utm_content
, which can be manually enabled.
Updated
7 months ago
Configure Control Groups
Web Personalization: In-line Content
Copy Page
