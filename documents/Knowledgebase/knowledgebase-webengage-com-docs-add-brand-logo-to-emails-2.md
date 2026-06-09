# Add Brand Logo to Emails

- URL: https://knowledgebase.webengage.com/docs/add-brand-logo-to-emails
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Add Brand Logo to Emails
With phishing, spoofing, and fraudulent emails on the rise, recipients are increasingly suspicious of messages in their inboxes. To build brand visibility, email senders can jump on a new standard known as
BIMI
.
BIMI stands for
Brand Indicators for Message Identification
.
What is BIMI?
BIMI is an emerging email specification that enables the use of brand-controlled logos within supporting email clients. With this simple, visual verification, receivers can recognise and trust the messages you send.
Prerequisite for BIMI
Before implementing BIMI it is necessary to authenticate your organisation’s emails with certain pre-requisites that have been described below:
SPF (Sender Policy Framework)
: Authenticates your email to identify the mail servers allowed to send emails from a particular domain.
DKIM (Domain Keys Identified Mail)
: Adds a digital signature to emails to verify to inbox providers that your domain sent the message and that you’re responsible for the contents of the message.
DMARC (Domain-based Message Authentication, Reporting & Conformance)
: DMARC allows the domain owner to specify how unauthenticated messages should be treated in end user's mail box.
Once all 3 are configured you can move to configure BIMI.
👍
Please Note
SPF and DKIM are primary authentication protocols for validating email sender domains and are usually configured for by brand's tech teams.
Implementing BIMI
BIMI is a text record that lives on your sending servers— in your Domain Name System (DNS) records. After your message is delivered, your recipient’s inbox provider retrieves your BIMI text record using a DNS lookup. This BIMI text record contains the location of your company’s logo. Follow the detailed
implementation guide
here.
🚧
Please Note
The implementation of BIMI has to be done by your tech team and WebEngage cannot help in this process.
Image specifications
The logo you'd like to display for your emails needs to be
The image should be a square aspect ratio.
For optimal display, the image should be centered as it may be displayed as a circle or square with rounded corners depending on the implementation.
The SVG document should be as small as possible and should not exceed 32 kilobytes.
The background should be a solid color, as transparent backgrounds may not display as expected.
BIMI’s Impact on Deliverability
Adding a BIMI record to your email program won’t promise 100% deliverability rates. But it can help. For mailbox providers who support BIMI (including Google and Yahoo!), this will add an extra layer of authenticity to your messages. In addition, subscribers will be more likely to recognise the size of your brand, decreasing the chances of marking it as spam.
Updated
7 months ago
AMP Email Use Cases
WhatsApp
Copy Page
