# TRAI DLT Regulations (India)

- URL: https://docs.webengage.com/docs/trai-sms-dlt-regulations-india
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Channel Configuration
SMS
TRAI DLT Regulations (India)
Applicable only if you are sending messages to users located in India via domestic messaging pipeline. International messaging routes remain unaffected
👍
Highlights
Whitelisting templates for all messages.
Registering the business entities and Sender IDs used for SMS marketing.
Registering user consent or SMS opt-in status.
In an effort to control promotional spam, SMS fraud, and unsolicited messaging, the
Telephone Regulatory Authority of India (TRAI) has enforced new guidelines
for SMS marketing. It
mandates the whitelisting of all SMS templates and registration of your company's entities, Sender IDs (Headers), and user consent
in a centralized DLT portal provided by Indian mobile operators.
This is applicable for sending both
Transactional and Promotional campaigns.
Additionally, a third campaign type has been introduced by TRAI - Service (Implicit & Explicit). You can find more details on the respective DLT portals while
whitelisting message templates
.
November 19, 2020, is the tentative deadline for registration. Failing to do so will cause mobile operators to cease delivering all your messages to their end-users.
Additionally, TRAI also prohibits all kinds of SMS marketing between DND hours from 21:00 Hrs. to 10:00 Hrs. Bank/ Financial Transaction OTPs are the only exception that can be conveyed via SMS during these hours.
Emphasis on Customer Consent & Preferences:
The new regulations grant complete control to your customers over multiple aspects (in addition to existing DND regulations). This includes:
Opting-out of receiving SMSes from your brand.
Opting-in to receiving promotional SMSes from your brand even if a user is registered in the national DND list.
Specify a time window, in a day, for receiving promotional messages. (Messages sent outside this window will fail to get delivered due to
DLT Scrubbing
).
DLT Registration
Here's a quick overview of the process:
Step 1
:
Register your Business to get a
Unique PE ID
Step 2
:
Register your
Sender IDs
Step 3
:
Whitelist all SMS templates to get
DLT Template ID
for each one
Step 4:
Register your
PE ID
and
DLT Template ID
with SSP to comply with
DLT Scrubbing Rules
(WebEngage simplifies this process for select SSPs!)
Step 1: Register Business Entity to Generate Unique PE ID
🚧
You Can Register on the Following DLT Portals
Airtel
Jio
Vodafone-Idea
BSNL
Videocon
Tata Tele Services
Once registered, you will be assigned a
Principal Entity ID (PE ID)
which must be used for registering your
Sender IDs
and
Message Templates
.
Please get in touch with your
SMS Service Provider
to understand if you need to register with all the aforementioned operators.
Attaching
PE ID
to each SMS sent by you:
As per TRAI's regulations, your
PE ID
must be passed in the message payload of each SMS sent to your users. Failing to do so will cause delivery failure owing to
DLT Scrubbing
by the mobile network provider. Here's how you can go about it:
Option 1:
Update your API integration with the SSP to include
PE ID
in the SMS message payload.
Option 2:
Add
PE ID
to WebEngage dashboard.
At WebEngage, you can easily add your PE ID while configuring the following SSPs in your dashboard. We'll ensure that it's relayed to your SSP for each SMS campaign sent by you:
Exotel
,
Gupshup
,
Infobip
,
Kaleyra
,
MSG91
,
ValueFirst
If you are using an SSP other than the ones listed above, please get in touch with your account manager asap to obtain more clarity!
Step 2: Register Sender ID
Depending on your use-case, you can choose to register your custom
Sender Name/ Sender ID/ Headers
as
Transactional
or
Promotional
directly with the mobile network providers. Please check the respective definitions on the DLT portals before you begin the process.
Step 3: Whitelist Message Templates to Generate Template ID
(Here's a template creation guide to help you get started)
Your SMS templates can be whitelisted on the
DLT portals mentioned above
under any of the following categories:
Transactional
(Reserved only for bank OTPs.)
Service-Implicit / Service-Inferred
(To be used for all other transactional campaigns.)
Promotional
(Requires proof of user consent & includes messages that sell products/services.)
Service-Explicit
(Requires proof of user consent & includes messages that recommend products/services.)
You will receive a unique
DLT Template ID
for each SMS template approved by the portals.
👍
Including Personalization Variables in SMS Templates for Whitelisting
All details such as
name, date, account number, OTP, codes, transaction ID, a/c numbers, URLs,
and so on are considered personalization variables during the whitelisting process.
Each variable can be replaced by the placeholder,
{#var#}
in your message. A maximum of 5-6 variables is allowed in a content template.
While it's mandatory for
Transactional
and
Service-Implicit
messages to include personalization variables, these can be excluded from
Promotional
and
Service-Explicit
messages.
Attaching
DLT Template ID
to each SMS sent by you:
As per TRAI's regulations, w.e.f Feb 1, 20201 the
Template ID
must be passed in the message payload of each SMS sent to your users. Failing to do so will cause delivery failure owing to
DLT Scrubbing
by the mobile network provider. Here's how you can go about it:
Option 1:
Register all your approved SMS templates manually with your SSP. (Depending on your SSP, you may need to update your APIs too.)
Option 2:
Add
DLT Template ID
to WebEngage dashboard
We have partnered with
Exotel
,
Gupshup
,
Infobip
,
Kaleyra
,
MSG91
and
ValueFirst
to help you manage template registration. You can simply add the
DLT Template ID
while creating an SMS campaign, we'll ensure that the parameter is passed to your SSP for each SMS.
If you are using an SSP other than the ones listed above, then please get in touch with your account manager asap to obtain further clarity!
DLT Scrubbing
TRAI has deemed it mandatory for all SMS marketers to provide their
PE ID (w.e.f Nov 1, 2020)
and
DLT Template ID (w.e.f Feb 1, 2021)
in the message payload for each SMS sent to a user. All SMSes will be subject to DLT scrubbing at the mobile network provider's end. This means that if either parameter is missing from the message payload, then the SMS will fail to get delivered.
At WebEngage, we have partnered with
Exotel
,
Gupshup
,
Infobip
,
Kaleyra
,
MSG91
and
ValueFirst
to help you pass these parameters in the message payload of each SMS, directly through your dashboard.
(So that you continue all your SMS marketing activities unhindered!)
PE ID
can be added while integrating any of the aforementioned SSPs.
DLT Template ID
can be added while creating an SMS campaign (only if any of the aforementioned SSPs are selected at
Step 3: Message
).
🚧
Please Note
Owing to TRAI's regulations, you may incur an additional DLT scrubbing charge of Rs. 0.25 per SMS. Please get in touch with your SSP for more details on their revised bulk SMS/ Promotional and transactional messaging rates.
Frequenty Asked Questions
1. Is the Content Template Registration mandatory on the DLT platform?
Yes, Content Template Registration is mandatory, and passing an approved Template Id, and the SMS will soon be a mandatory parameter.
Also, all kinds of SMS content, i.e., OTPs, Transactional, and Promotional, have to be registered on your respective DLT platform.
2. What is the format of Variable while applying Content Template on DLT platform?
On every DLT platform, each Variable should be written as {#var#}. If you use any other variable format, it will not be considered a variable, and your SMS delivery will be impacted.
3. What is the character limit in Variable {#var#} while sending SMS?
The variable's actual value while sending an SMS will be a maximum of 30 characters for both English and Unicode.
4. Is there any limit on the number of variables allowed in a single Content Template?
A maximum of 5-6 variables is allowed in one Content Template.
5. Is Brand Name mandatory in every SMS Template while applying on the DLT platform?
Yes, it is necessary to include your Brand Name in every SMS Content Template.
6. How many Headers (Sender Id) can be associated with a Content Template?
Multiple Headers can be mapped against the same Content Template during registration. This might be different on different DLT platforms.
7. How long does it take to get the approval of the Content Template from the DLT platform?
Due to a large number of requests, you may face some delay in approval. However, a minimum of 2-4 business days wait is expected.
8. Is adding a Brand Name compulsory for all kinds of content templates?
Brand Name is compulsory in all kinds of SMS content: Promotional, Transactional, and OTPs.
9. Getting rejection on a template with an error
Wrong Content-Type Selected
?
Please note, your SMS content should be applied under service implicit or explicit category only. Do not apply under promotional or transactional categories.
10. Getting rejection on a template with an error
Brand Name not Added
.
Adding Brand name in an SMS content template is mandatory and should be explicitly mentioned in the SMS body.
👍
Example of SMS Body
Hello {#Var#},
Your order with Id {#Var#} has been dispatched for delivery.
Team XYZ.
11. Getting rejection on a template with an error
No header associated with the brand name
.
This implies that you do not have a Header/ Sender Id of the brand name you wish to have a template of, and hence no- correlation can be built.
If you want to add a template with the brand name MSG91, you should have a header related to MSG91 in your DLT account first, say, MSGIND.
📘
Please Note
You cannot apply for a template with your customer’s brand name in your DLT account. A new entity registration should be carried out for your customers first.
12. Having confusion while applying content in service implicit and explicit?
If you are confused in deciding the SMS content category as
Service Implicit
or
Service Explicit
while applying on the DLT platform, it is highly recommended that you apply the Content Template twice, once with Implicit and once with Explicit.
Later, if your Content Template is approved from both categories, kindly use the Template Id of
Service Implicit
only.
13. I have got my Header/Sender Id approved from DLT. What should I do next?
Once the Header is approved on the DLT platform, it will be synced on the Global Platform in around 24 hrs, and you will then be able to use your Header for sending SMS.
If your SMSes are not getting delivered from your Header even after 24 hrs from Header approval time, kindly get in touch with this contact:
[email protected]
.
14. What should I do if my Sender Id does not match with my Company Name applied on DLT?
In such a case, kindly upload a document to prove the co-relation between Company Name and Header.
If Alphabet Inc. needs Sender ID as Google, they need to prove co-relation between Sender Id GOOGLE and Alphabet.
If the Operator is not satisfied with co-relation proof, your Header may not be approved.
15. What should I do if the template requests not getting approved on Ping Connect?
If your template request is not approved even after 3 days of minimum wait, kindly share the below details registered on Telecom Operator (DLT platform) to request the Telecom Operator to approve your request.
Organization Name
DLT Platform Name
Entity Id
Template Request number
Date of Submission
MSG91 Username
16. Getting this error "Organization with this POI has been already registered"?
This means that you have either tried to register before or are already registered. In this case, kindly try to log in and click on the forgot password. If it still doesn’t work, kindly write on
[email protected]
and share your issues with them and support screenshots.
Please feel free to drop in a few lines at
[email protected]
if you have any further queries. We're always just an email away!
Updated
7 months ago
SMS
TRAI's Mandate for CTA Whitelisting
Copy Page
