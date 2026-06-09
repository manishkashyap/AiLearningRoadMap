# Event Name Updates

- URL: https://docs.webengage.com/docs/system-event-name-updates-complete-reference
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Event Name Updates
System Event Name Updates: Complete Reference
In a recent update, WebEngage has standardized the display names for system events across all engagement channels.
Backend event names are unchanged.
Only what you see in the WebEngage UI has been updated. APIs, webhooks, User Event Stream, and data exports are unaffected.
What changed and why
Event display names were inconsistent in two ways:
Names didn't accurately reflect the delivery lifecycle step. For example, "Email Accepted" (the message was handed to the ESP, not delivered) is now "Email Sent to ESP."
Naming conventions varied across channels. The language is now aligned across Email, SMS, WhatsApp, RCS, Viber, Push, Web Push, On-site, and Inbox.
Naming conventions
Pattern
Old style
New style
Queued internally
Email Queued
Email Queued by WebEngage
Handed to provider
Email Accepted
Email Sent to ESP
Confirmed delivery
WhatsApp Sent
WhatsApp Delivered
Provider rejection
Email Rejected
Email Failed - Rejected
User interaction
Email Click
Email Clicked
On-site widget events
Feedback View
On-site Feedback Viewed
Full event name reference
Email
New Name
Old Name
Backend Name
Email Queued by WebEngage
Email Queued
email_queued
Email Sent to ESP
Email Accepted
email_accepted
Email Sent by ESP
Email Sent
email_sent
Email Failed - Rejected
Email Rejected
email_rejected
Email Failed - Discarded
Email Discarded
email_discarded
Email Failed - Bounced
Email Bounced
email_bounce
Email Delivered
Email Delivered
email_delivered
Email Opened
Email Open
email_open
Email Clicked
Email Click
email_click
Email Unsubscribe
Email Unsubscribe
email_unsubscribe
Email Resubscribe
Email Resubscribe
email_resubscribe
Email Spam Report
Email Spam Report
email_spam
Email Complaint
Email Complaint
email_complaint
Email Control Attempted
Email Control Attempted
email_control_group
SMS
New Name
Old Name
Backend Name
SMS Queued by WebEngage
SMS Queued
sms_queued
SMS Sent to SSP
SMS Accepted
sms_accepted
SMS Delivered
SMS Sent
sms_sent
SMS Failed - Rejected
SMS Rejected
sms_rejected
SMS Failed
SMS Failed
sms_failed
SMS Clicked
SMS Click
sms_click
SMS Control Attempted
SMS Control Attempted
sms_control_group
WhatsApp
New Name
Old Name
Backend Name
WhatsApp Queued by WebEngage
WhatsApp Queued
whatsapp_queued
WhatsApp Sent to WSP
WhatsApp Accepted
whatsapp_accepted
WhatsApp Delivered
WhatsApp Sent
whatsapp_sent
WhatsApp Failed - Rejected
WhatsApp Rejected
whatsapp_rejected
WhatsApp Failed
WhatsApp Failed
whatsapp_failed
WhatsApp Read
WhatsApp Read
whatsapp_read
WhatsApp Clicked
WhatsApp Click
whatsapp_click
WhatsApp Control Attempted
WhatsApp Control Attempted
whatsapp_control_group
RCS
New Name
Old Name
Backend Name
RCS Queued by WebEngage
RCS Queued
rcs_queued
RCS Sent to RSP
RCS Accepted
rcs_accepted
RCS Delivered
RCS Delivered
rcs_delivered
RCS Failed - Rejected
RCS Rejected
rcs_rejected
RCS Failed
RCS Failed
rcs_failed
RCS Read
RCS Read
rcs_read
RCS Clicked
RCS Click
rcs_click
RCS Control Attempted
RCS Control Attempted
rcs_control_group
Viber
New Name
Old Name
Backend Name
Viber Queued by WebEngage
Viber Queued
viber_queued
Viber Sent to Provider
Viber Accepted
viber_accepted
Viber Delivered
Viber Sent
viber_sent
Viber Failed - Rejected
Viber Rejected
viber_rejected
Viber Failed
Viber Failed
viber_failed
Viber Viewed
Viber Seen
viber_read
Viber Clicked
Viber Click
viber_click
Viber Control Attempted
Viber Control Attempted
viber_control_group
Push (Mobile & Web)
New Name
Old Name
Backend Name
Push Queued by WebEngage for FC, DND etc. (Mobile & Web)
Push (Web & Mobile) Queued
push_notification_queued
Push Sent to FCM / APNs (Mobile)
Push (Mobile) Sent
gcm_notification_response
Push Accepted (Web & Mobile)
Push (Web & Mobile) Accepted
push_notification_accepted
Push Failed - Rejected by FCM, Queue Drop etc. (Mobile & Web)
Push (Web & Mobile) Rejected
push_notification_rejected
Push Received (Mobile)
Push (Mobile) Received
push_notification_received
Push Impression (Mobile & Web)
Push (Web & Mobile) Impression
push_notification_view
Push Clicked (Mobile & Web)
Push (Web & Mobile) Click
push_notification_click
Push Dismiss (Web & Mobile)
Push (Web & Mobile) Dismiss
push_notification_close
Push Notification Failed
Push Notification Failed
push_notification_failed
Push Carousel Item Viewed (Mobile)
Push (Mobile) Carousel Item Viewed
push_notification_item_view
Push Rating Submitted (Mobile)
Push (Mobile) Rating Submitted
push_notification_rating_submitted
Push Registered (Mobile)
GCM/APNs Registered
gcm_registered
Push Registered (Web)
Push (Web) Registered
push_notification_registered
Push Unregistered (Web)
Push (Web) UnRegistered
push_notification_unregistered
Push Notification Control Attempted
Push Notification Control Attempted
push_notification_control_group
Web Push
New Name
Old Name
Backend Name
Web Push Subscribe Viewed
Web Push Subscribe Viewed
push_notification_window_view
Web Push Subscribe Denied
Web Push Subscribe Denied
push_notification_window_denied
Web Push Subscribe Successful
Web Push Subscribe Successful
push_notification_window_allowed
Web Push Subscribe Notification Viewed
Web Push Subscribe Notification Viewed
push_notification_prompt_view
Web Push Subscribe Notification Allowed
Web Push Subscribe Notification Allowed
push_notification_prompt_allowed
Web Push Subscribe Notification Denied
Web Push Subscribe Notification Denied
push_notification_prompt_denied
On-site Notifications
New Name
Old Name
Backend Name
Notification Impression (On-site & In-app)
Notification (On-site & In-app) Impression
notification_view
Notification Clicked (On-site & In-app)
Notification (On-site & In-app) Click
notification_click
Notification Closed (On-site & In-app)
Notification (On-site & In-app) Close
notification_close
Notification Control Attempted (On-site)
Notification (On-site) Control Attempted
notification_abs_view
Notification Control Attempted
Notification Control Attempted
notification_control_group
Notification Inbox
New Name
Old Name
Backend Name
Notification Inbox Sent
Notification Inbox Sent
inbox_notification_sent
Notification Inbox Impression
Notification Inbox Impression
inbox_notification_view
Notification Inbox Clicked
Notification Inbox Click
inbox_notification_click
Notification Inbox Read
Notification Inbox Read
inbox_notification_read
Notification Inbox Unread
Notification Inbox Unread
inbox_notification_unread
Notification Inbox Dismissed
Notification Inbox Dismiss
inbox_notification_close
Notification Inbox Deleted
Notification Inbox Delete
inbox_notification_delete
Notification Inbox Control Attempted
Notification Inbox Control Attempted
inbox_notification_control_group
On-site Feedback
New Name
Old Name
Backend Name
On-site Feedback Viewed
On-site Feedback View
feedback_view
On-site Feedback Closed
On-site Feedback Close
feedback_close
On-site Feedback Submitted
On-site Feedback Submit
feedback_submit
On-site Survey
New Name
Old Name
Backend Name
On-site Survey Viewed
On-site Survey View
survey_view
On-site Survey Closed
On-site Survey Close
survey_close
On-site Survey Completed
On-site Survey Complete
survey_complete
On-site Survey Submitted
On-site Survey Submit
survey_submit
Survey Control Attempted (On-site)
Survey (On-site) Control Attempted
survey_abs_view
Web Personalization
New Name
Old Name
Backend Name
Web Personalization Impression
Web Personalization Impression
web_personalization_view
Web Personalization Clicked
Web Personalization Click
web_personalization_click
Web Personalization Control Attempted
Web Personalization Control Attempted
web_personalization_control_group
App In-line
New Name
Old Name
Backend Name
App In-line Impression
App In-line Impression
app_personalization_view
App In-line Clicked
App In-line Click
app_personalization_click
App In-line Failed
App In-line Failed
app_personalization_failed
App In-line Received
App In-line Received
app_personalization_received
App In-line Control Attempted
App-inline Control Attempted
app_personalization_control_group
Frequently asked questions
Will my existing segments break?
No. Existing segments, funnels, journeys, or alerts are unaffected.
What about the API and webhooks?
No change. All API calls, webhook payloads, and data exports are unchanged.
Where are these not changed?
Event Names in following modules remain as they were in those respective modules - Paths, Journeys, Relays and Data Outlets.
Updated
about 1 month ago
Getting Started
Copy Page
