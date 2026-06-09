# FAQ

- URL: https://knowledgebase.webengage.com/docs/rcs-faq
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

FAQ
Commonly asked questions related to RCS Messaging
1. Can the URLs in a RCS message have a custom domain?
Yes! Here's how you can go about it:
Step 1:
Create a custom domain that will exclusively be used to add links in your campaigns.
Step 2:
Add a CNAME entry for the custom domain and point it to
weurl.co
with a TTL (
time to live
) of 30 minutes in your DNS (Domain Name System) zone file. Doing so will ensure that your domain name is not replaced with
weurl.co
when the link is shortened.
Step 3:
Add the domain to your dashboard under
Settings > Campaign Custom Domain
And you're all set!
(
Detailed read
)
2. How can I segment opted-in RCS users?
You can easily group all opted-in users through the
Segments section
of your dashboard.
Click to enlarge
As shown above, go to
Users > Reachability
and select
RCS
as the channel.
(Because, Opted-in User = Reachable on RCS)
Add any other
Behavioral
and
Technological
parameters to refine the segment as per your needs and click
Save!
🚧
Detailed Read
Collecting RCS subscriptions & passing opt-in status of a user to your dashboard
Please feel free to drop in a few lines at
[email protected]
in case you have any further queries or feedback. We're always just an email away!
Updated
7 months ago
Rich Communication Service Template Creation
Web Push
Copy Page
