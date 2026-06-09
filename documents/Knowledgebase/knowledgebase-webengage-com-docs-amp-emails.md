# AMP Emails

- URL: https://knowledgebase.webengage.com/docs/amp-emails
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

AMP Emails
🚧
Please Note
We support AMP email only for
Infobip
,
SparkPost
and
SendGrid
at the moment. We'll be adding support for more AMP-enabled ESPs soon!
Currently WebEngage does not store responses for Survey/Forms sent through AMP emails.
What is AMP for Email?
AMP for Email is redefining transactional and marketing email campaigns. Instead of static experiences, AMP for emails allows you to serve live, interactive email content like carousels, accordions, confirmation, purchase buttons, etc., in an email without needing to open a new tab to visit a website. Imagine a website like experience — just, in an email. That's AMP.
Inboxes that support AMP for Email:
Currently AMP is supported these email clients:
Gmail
Yahoo! Mail
FairEmail
Mail.ru
Benefits of AMP Email?
AMP provide a seamless experience to the customer with graphics, images, buttons etc. within an email. They are designed to increase customer engagement and help in shortening the funnel. One of the major benefits of AMP emails is the higher engagement and low drop-offs.
With interactive AMP emails, you can send:
Emails that require immediate attention, like changing the subscription or opting out of the email list.
Forms for surveys or user preferences.
Emails that have complex content with multiple links. You can send them in the form of
Carousels
making it more interactive for the user to reply to the email without leaving the email page.
Emails that have products with real-time pricing or are time-sensitive.
Calendar invites which can be accepted or rejected from the email.
Quizzes or puzzles to make the user engagement on the email more interactive and fun.
Details of multiple products/ services in the form of
Accordion
.
Prerequisite for sending AMP Emails
Before starting to send AMP emails, you will have to ensure that you have SPF (Sender Policy Framework) and DKIM (DomainKeys Identified Mail) set up for the domain you’re sending from.
After setting up your domain, you have to send a test email to
[email protected]
and follow the [Bulk Senders Guidelines] (
https://support.google.com/mail/answer/81126
) from Gmail.
The last step is to use their
registration form
to list yourself as a sender.
Other criteria to be fulfilled:
The recipient should have enabled dynamic emails through the inbox settings.
A non-AMP fallback email must also be sent along with AMP version. This is to make sure that an email is rendered in non AMP supporting mailboxes or AMP disabled mailboxes.
Read this
to understand the need for adding Fallback message.
Creating AMP Emails in WebEngage
📘
Please Note
Please go through the basic steps of creating an email campaign
here
.
Once you land on the
Message
tab of email campaign creation, follow the process mentioned below for creating an AMP Email campaign.
Add AMP and Fallback Content
Once you land on the Message tab, select your ESP and add the details required in this
From
card
If you have selected an ESP, you will see an
AMP Email
toggle in the Message card. Switch it on
In the Body field, you will now find 2 tabs:
AMP
and
Fallback
. You need to add content in both fields. For AMP HTML, you need to add content in AMP HTML format, while for Fallback you can either add Rich Text or Raw HTML
📘
Please Note
Drag and Drop editor is currently not supported while sending AMP campaigns.
Validate your AMP for Email Markup
It is very important to send a valid AMP HTML or else the fallback email will sent to the client. To validate your markup, you can do it
here
.
Preview your Email
You can check Raw or User previews of your emails for both AMP and Fallback content. For AMP emails you can test your interactive elements within these previews as well. There is capability to preview as Mobile or Desktop mode.
Final steps
Once you are satisfied with the campaign preview, add
conversion tracking
and
test the campaign
. Finally
review the campaign details
and launch.
👍
Congratulations!
You have now successfully sent your AMP Email campaign 👍
You can check out some of the use cases that AMP email can help you achieve
here
.
Fallback for AMP Emails
To ensure that every email recipient has a seamless inbox experience, it is necessary to create a fallback for AMP emails. When you add videos or images to the email, it is a good practice to add the HTML fallback so that the users who cannot view it due to limited email client functionality can still have a good email experience.
Fallback message comes in play when:
The AMP email expires after 30 days, and if the user tries to access the AMP email after it has expired
If a user wants to forward an AMP email. In this case the recipient will only see the fallback.
The recipient does not use the email service provider to support the AMP functionality.
In such scenarios, the HTML fallback lets the recipient have an enjoyable experience and successfully impart necessary information.
Updated
7 months ago
FAQ
AMP Email Use Cases
Copy Page
