# TRAI's Mandate for CTA Whitelisting

- URL: https://docs.webengage.com/docs/sms-cta-whitelisting-guidelines-trai-mandate
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
SMS
TRAI DLT Regulations (India)
TRAI's Mandate for CTA Whitelisting
❗️
Important
SMS CTA Whitelisting Guidelines are applicable to all who send
DLT based SMSs in India
. If you do not send DLT based messages in India, you can safely ignore this.
The Telecom Regulatory Authority of India (TRAI) has recently released guidelines to restrict misuse of SMS messages. Certain changes are required to comply with the new regulations around the use of URL shortening services in SMS campaigns. The new regulation specifically states:
"Senders shall not use any URL shortening service or short URLs unless the shortened URL clearly indicates that it has a relation with the Sender."
This means that any shortened URL in your SMS communication must indicate the business sending the message. To ensure compliance with this regulation, we are offering two solutions for the URL shortening in your SMS campaigns.
Note:
This is a developing guideline. TRAI is working with operators and other stakeholders to come up with guidelines acceptable to all parties. Solutions proposed here are as per current visibility, subject to change as mandate evolves.
Solution
To adhere with TRAI guidelines, WebEngage will automatically switch to dynamic path in format,
https://weurl.co/{SenderID}/{UniqueID}
.
For example, for Sender ID ACMENX, URL path to whitelist would be,
https://weurl.co/ACMENX/
New URL format results in increase of 15 characters, may result in increased SMS counts.
The CTAs will follow the format above for the DLT based SMS's only. CTAs in RCS and WhatsApp messages will remain unaffected.
Note: With reference to previous communication URL format is changed to accommodate a variety of formats used by service providers.
Using Custom Domain
We allow you to specify your own custom domain for URL shortening. This means that instead of using our default shortened domain (weurl.co), you can configure your own domain for shortening links. For this you will require to set up a
Custom Domain
Sender ID will be auto appended to the custom domain. For example. if domain is acme.com and Sender ID is ACMENX, URL will be generated in format
https://acme.com/ACMENX/{UniqueID}
or
http://acme.com/ACMENX/{UniqueID}
the URL path to whitelist would be
https://acme.com/ACMENX/
or
http://acme.com/ACMENX/
Do consider variable limit of 30 char limit when choosing your custom domain. To be specific, custom domain should not be more than 8-9 chars. Limit of 8 chars for HTTPS and 9 chars in case of HTTP.
Your custom domain will also apply to shortened URLs in WhatsApp and RCS campaigns. As a result, you will need to update your RCS / WhatsApp templates where weurl.co had been whitelisted.
Important Note
It is advised to whitelist shortened domains with all of the SenderIDs individually in the DLT platform. For example if you have 2 SenderIDs ACMENX and CCMENY then you would have to whitelist
https://weurl.co/ACMENX/
and
https://weurl.co/CCMENY/
. Same goes for custom domains as well.
If your URL contains a query parameter ‘
?
’ then along with the short domain you may need to whitelist the long URL (depends on SP guidelines). For example if your destination URL is
https://example.com/page?parameter1=x&parameter2=y
then you may have to whitelist
https://example.com/page?
as long URL as well.
Implementation Timeline
The TRAI has set a deadline of
Tuesday, 1 October 2024
for compliance with the new guidelines. Solution described above is implemented for your campaigns from Thursday, 26 September 2024.
Impact on Existing Templates
The changes will not affect your existing message templates directly, as URLs in templates are passed as variables. However,
you must ensure that the domain (custom or dynamic) being used is whitelisted with the operator
to avoid any issues once scrubbing starts from the operator's end.
📘
References
Important Guidelines for sending commercial communication using telecom resources through Voice Calls or SMS – Circulation of the same among Principal Entities for compliance – regarding.
Link
letter dated 18-Jun-2024
Direction under section 13, read with subclauses (i) and (v) of clause (b) of sub section (1) of section 11, of the Telecom Regulatory Authority of India Act, 1997 (24 of 1997) regarding measures to curb misuse of Headers and Content Templates under Telecom Commercial Communications Customer Preference Regulations, 2018 (6 of 2018)
Direction
dated 30-Aug-2024
Direction
dated 20-Aug-2204
Updated
7 months ago
TRAI DLT Regulations (India)
Guidelines on PE-TM Chain Binding on DLT
Copy Page
