# Getting Started

- URL: https://docs.webengage.com/docs/web-getting-started
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Website
Getting Started
🚧
Looking to Integrate AMP Pages?
Start here.
1. Add Domain to WebEngage Dashboard
Click to enlarge
As shown above:
Log in to your WebEngage dashboard and navigate to
Data Platform> Integrations> SDK Integration Status (Configure).
Add your website's domain name against the field
Domain
under
Integration Steps.
2. Integrate the SDK
At WebEngage, you can choose to host all your data at three data centers - the US, Saudi Arabia or India. By default, all your data is stored in our
US (Global) Data Center.
However, you can choose to host it at our
Saudi Arabia
or
India Data Center
by specifying the same in your contractual agreement.
Depending on your data center, the SDK integration code will vary.
Here's how you can go about it:
For All Websites
(Not applicable to Single-Page Application sites)
If You're Using WebEngage's Global Data Center:
All your data is stored in our
Global Data Center
by default. Thus, if your dashboard URL starts with
dashboard.webengage.com
, then it means you're using our
US Data Center.
Please add the following code at the end
<head>
section of each page you want to track.
HTML
<script id="_webengage_script_tag" type="text/javascript">
 var webengage;
 ! function(w, e, b, n, g) {
 function o(e, t) {
 e[t[t.length - 1]] = function() {
 r.__queue.push([t.join("."), arguments])
 }
 }
 var i, s, r = w[b],
 z = " ",
 l = "init options track screen onReady".split(z),
 a = "feedback survey notification".split(z),
 c = "options render clear abort".split(z),
 p = "Open Close Submit Complete View Click".split(z),
 u = "identify login logout setAttribute".split(z);
 if (!r || !r.__v) {
 for (w[b] = r = {
 __queue: [],
 __v: "6.0",
 user: {}
 }, i = 0; i < l.length; i++) o(r, [l[i]]);
 for (i = 0; i < a.length; i++) {
 for (r[a[i]] = {}, s = 0; s < c.length; s++) o(r[a[i]], [a[i], c[s]]);
 for (s = 0; s < p.length; s++) o(r[a[i]], [a[i], "on" + p[s]])
 }
 for (i = 0; i < u.length; i++) o(r.user, ["user", u[i]]);
 setTimeout(function() {
 var f = e.createElement("script"),
 d = e.getElementById("_webengage_script_tag");
 f.type = "text/javascript",
 f.async = !0,
 f.src = ("https:" == e.location.protocol ? "https://ssl.widgets.webengage.com" : "http://cdn.widgets.webengage.com") + "/js/webengage-min-v-6.0.js",
 d.parentNode.insertBefore(f, d)
 })
 }
 }(window, document, "webengage");

 webengage.init('YOUR_WEBENGAGE_LICENSE_CODE');
</script>
If You're Using WebEngage's India Data Center:
You will need to specifically request for your data to be stored in our India Data Center in your contract with WebEngage. Thus, if your dashboard URL starts with
dashboard.in.webengage.com
, then it means you're using our
India Data Center.
Please add the following code at the end
<head>
section of each page you want to track.
HTML
<script id="_webengage_script_tag" type="text/javascript">
 var webengage;
 ! function(w, e, b, n, g) {
 function o(e, t) {
 e[t[t.length - 1]] = function() {
 r.__queue.push([t.join("."), arguments])
 }
 }
 var i, s, r = w[b],
 z = " ",
 l = "init options track screen onReady".split(z),
 a = "feedback survey notification".split(z),
 c = "options render clear abort".split(z),
 p = "Open Close Submit Complete View Click".split(z),
 u = "identify login logout setAttribute".split(z);
 if (!r || !r.__v) {
 for (w[b] = r = {
 __queue: [],
 __v: "6.0",
 user: {}
 }, i = 0; i < l.length; i++) o(r, [l[i]]);
 for (i = 0; i < a.length; i++) {
 for (r[a[i]] = {}, s = 0; s < c.length; s++) o(r[a[i]], [a[i], c[s]]);
 for (s = 0; s < p.length; s++) o(r[a[i]], [a[i], "on" + p[s]])
 }
 for (i = 0; i < u.length; i++) o(r.user, ["user", u[i]]);
 setTimeout(function() {
 var f = e.createElement("script"),
 d = e.getElementById("_webengage_script_tag");
 f.type = "text/javascript",
 f.async = !0,
 f.src = ("https:" == e.location.protocol ? "https://widgets.in.webengage.com" : "http://widgets.in.webengage.com") + "/js/webengage-min-v-6.0.js",
 d.parentNode.insertBefore(f, d);
 })
 }
 }(window, document, "webengage");

 webengage.init('YOUR_WEBENGAGE_LICENSE_CODE');
</script>
If You're Using WebEngage's Saudi Arabia Data Center:
You will need to specifically request for your data to be stored in our Saudi Arabia Data Center in your contract with WebEngage. Thus, if your dashboard URL starts with
dashboard.ksa.webengage.com
, then it means you're using our
Saudi Arabia Data Center.
Please add the following code at the end
<head>
section of each page you want to track.
HTML
<script id="_webengage_script_tag" type="text/javascript">
 var webengage;
 ! function(w, e, b, n, g) {
 function o(e, t) {
 e[t[t.length - 1]] = function() {
 r.__queue.push([t.join("."), arguments])
 }
 }
 var i, s, r = w[b],
 z = " ",
 l = "init options track screen onReady".split(z),
 a = "feedback survey notification".split(z),
 c = "options render clear abort".split(z),
 p = "Open Close Submit Complete View Click".split(z),
 u = "identify login logout setAttribute".split(z);
 if (!r || !r.__v) {
 for (w[b] = r = {
 __queue: [],
 __v: "6.0",
 user: {}
 }, i = 0; i < l.length; i++) o(r, [l[i]]);
 for (i = 0; i < a.length; i++) {
 for (r[a[i]] = {}, s = 0; s < c.length; s++) o(r[a[i]], [a[i], c[s]]);
 for (s = 0; s < p.length; s++) o(r[a[i]], [a[i], "on" + p[s]])
 }
 for (i = 0; i < u.length; i++) o(r.user, ["user", u[i]]);
 setTimeout(function() {
 var f = e.createElement("script"),
 d = e.getElementById("_webengage_script_tag");
 f.type = "text/javascript",
 f.async = !0,
 f.src = ("https:" == e.location.protocol ? "https://widgets.ksa.webengage.com" : "http://widgets.ksa.webengage.com") + "/js/webengage-min-v-6.0.js",
 d.parentNode.insertBefore(f, d);
 })
 }
 }(window, document, "webengage");

 webengage.init('YOUR_WEBENGAGE_LICENSE_CODE');
</script>
For SPA (Single Page Application) Websites
If You're Using WebEngage's Global Data Center:
All your data is stored in our
Global Data Center
by default. Thus, if your dashboard URL starts with
dashboard.webengage.com
, then it means you're using our
Global Data Center.
Please add the following code at the end
<head>
section of each page you want to track.
HTML
<script id='_webengage_script_tag' type='text/javascript'>
 var webengage;
 ! function(w, e, b, n, g) {
 function o(e, t) {
 e[t[t.length - 1]] = function() {
 r.__queue.push([t.join("."), arguments])
 }
 }
 var i, s, r = w[b],
 z = " ",
 l = "init options track screen onReady".split(z),
 a = "feedback survey notification".split(z),
 c = "options render clear abort".split(z),
 p = "Open Close Submit Complete View Click".split(z),
 u = "identify login logout setAttribute".split(z);
 if (!r || !r.__v) {
 for (w[b] = r = {
 __queue: [],
 is_spa: 1, //Change this to 0 if you do not wish to use default SPA behaviour of WebEngage SDK
 __v: "6.0",
 user: {}
 }, i = 0; i < l.length; i++) o(r, [l[i]]);
 for (i = 0; i < a.length; i++) {
 for (r[a[i]] = {}, s = 0; s < c.length; s++) o(r[a[i]], [a[i], c[s]]);
 for (s = 0; s < p.length; s++) o(r[a[i]], [a[i], "on" + p[s]])
 }
 for (i = 0; i < u.length; i++) o(r.user, ["user", u[i]]);
 setTimeout(function() {
 var f = e.createElement("script"),
 d = e.getElementById("_webengage_script_tag");
 f.type = "text/javascript", f.async = !0, f.src = ("https:" == e.location.protocol ? "https://ssl.widgets.webengage.com" : "https://cdn.widgets.webengage.com") + "/js/webengage-min-v-6.0.js", d.parentNode.insertBefore(f, d)
 })
 }
 }(window, document, "webengage");
 webengage.init('YOUR_WEBENGAGE_LICENSE_CODE'); //replace the YOUR_WEBENGAGE_LICENSE_CODE with your WebEngage Account License Code
</script>
If You're Using WebEngage's India Data Center:
You will need to specifically request for your data to be stored in our India Data Center in your contract with WebEngage. Thus, if your dashboard URL starts with
dashboard.in.webengage.com
, then it means you're using our
India Data Center.
Please add the following code at the end
<head>
section of each page you want to track.
HTML
<script id='_webengage_script_tag' type='text/javascript'>
 var webengage;
 ! function(w, e, b, n, g) {
 function o(e, t) {
 e[t[t.length - 1]] = function() {
 r.__queue.push([t.join("."), arguments])
 }
 }
 var i, s, r = w[b],
 z = " ",
 l = "init options track screen onReady".split(z),
 a = "feedback survey notification".split(z),
 c = "options render clear abort".split(z),
 p = "Open Close Submit Complete View Click".split(z),
 u = "identify login logout setAttribute".split(z);
 if (!r || !r.__v) {
 for (w[b] = r = {
 __queue: [],
 is_spa: 1, //Change this to 0 if you do not wish to use default SPA behaviour of WebEngage SDK
 __v: "6.0",
 user: {}
 }, i = 0; i < l.length; i++) o(r, [l[i]]);
 for (i = 0; i < a.length; i++) {
 for (r[a[i]] = {}, s = 0; s < c.length; s++) o(r[a[i]], [a[i], c[s]]);
 for (s = 0; s < p.length; s++) o(r[a[i]], [a[i], "on" + p[s]])
 }
 for (i = 0; i < u.length; i++) o(r.user, ["user", u[i]]);
 setTimeout(function() {
 var f = e.createElement("script"),
 d = e.getElementById("_webengage_script_tag");
 f.type = "text/javascript", f.async = !0, f.src = ("https:" == e.location.protocol ? "https://widgets.in.webengage.com" : "http://widgets.in.webengage.com") + "/js/webengage-min-v-6.0.js", d.parentNode.insertBefore(f, d)
 })
 }
 }(window, document, "webengage");
 webengage.init('YOUR_WEBENGAGE_LICENSE_CODE'); //replace the YOUR_WEBENGAGE_LICENSE_CODE with your WebEngage Account License Code
</script>
If You're Using WebEngage's Saudi Arabia Data Center:
You will need to specifically request for your data to be stored in our Saudi Arabia Data Center in your contract with WebEngage. Thus, if your dashboard URL starts with
dashboard.ksa.webengage.com
, then it means you're using our
Saudi Arabia Data Center.
Please add the following code at the end
<head>
section of each page you want to track.
HTML
<script id='_webengage_script_tag' type='text/javascript'>
 var webengage;
 ! function(w, e, b, n, g) {
 function o(e, t) {
 e[t[t.length - 1]] = function() {
 r.__queue.push([t.join("."), arguments])
 }
 }
 var i, s, r = w[b],
 z = " ",
 l = "init options track screen onReady".split(z),
 a = "feedback survey notification".split(z),
 c = "options render clear abort".split(z),
 p = "Open Close Submit Complete View Click".split(z),
 u = "identify login logout setAttribute".split(z);
 if (!r || !r.__v) {
 for (w[b] = r = {
 __queue: [],
 is_spa: 1, //Change this to 0 if you do not wish to use default SPA behaviour of WebEngage SDK
 __v: "6.0",
 user: {}
 }, i = 0; i < l.length; i++) o(r, [l[i]]);
 for (i = 0; i < a.length; i++) {
 for (r[a[i]] = {}, s = 0; s < c.length; s++) o(r[a[i]], [a[i], c[s]]);
 for (s = 0; s < p.length; s++) o(r[a[i]], [a[i], "on" + p[s]])
 }
 for (i = 0; i < u.length; i++) o(r.user, ["user", u[i]]);
 setTimeout(function() {
 var f = e.createElement("script"),
 d = e.getElementById("_webengage_script_tag");
 f.type = "text/javascript", f.async = !0, f.src = ("https:" == e.location.protocol ? "https://widgets.ksa.webengage.com" : "http://widgets.ksa.webengage.com") + "/js/webengage-min-v-6.0.js", d.parentNode.insertBefore(f, d)
 })
 }
 }(window, document, "webengage");
 webengage.init('YOUR_WEBENGAGE_LICENSE_CODE'); //replace the YOUR_WEBENGAGE_LICENSE_CODE with your WebEngage Account License Code
</script>
Guidelines
(Applicable to all the integration code snippets provided above)
Please replace
YOUR_WEBENGAGE_LICENSE_CODE
with your WebEngage license code which can be found under Account Setup in your dashboard (as shown below). Your License Code might start with tilde (
~
).
Locating license code in your WebEngage dashboard
The integration code loads and initializes WebEngage SDK asynchronously, so that it does not affect the page load time of your website.
During initialization, this code waits for event,
DOMContentLoaded
to occur before modifying the
DOM
for loading further resources, ensuring it doesn't delay readiness of the
DOM
.
The script URLs in the integration code are protocol relative. All our resources are loaded over the same protocol (
HTTP
or
HTTPS
) as the containing page, which prevents "Insecure Content" warnings.
Session Lifecycle
The WebEngage SDK automatically starts tracking user data (e.g., Browser, OS version, Country) and engagement with the basic setup above.
WebEngage SDK also starts tracking user sessions with this basic setup. Upon leaving the web page, the SDK marks the current time. If the user returns to the web page after more than 30 minutes since the user had last left the page, the SDK will close the previous session. If the user returns to the web page within 30 minutes of leaving, the previous session is resumed as if the user did not leave the web page at all. Please note that this behaviour is recorded only if the resumed session is in the same web browser (can be a different browser window). In case the resumed session is in a different web browser on the same device, WebEngage SDK will record it as a separate session.
🚧
Congratulations!
You have now successfully integrated WebEngage with your website and are now sending user session data to your dashboard. Please note that it may take upto a few minutes for your data to show up on the WebEngage dashboard.
Please feel free to drop in a few lines at
[email protected]
or get in touch with your
Onboarding Manager
in case you have any further queries. We're always just an email away!
Updated
7 months ago
So, what's next?
Let's show you how you can:
Track User Properties as User Attributes
Track User Actions as Events
Integrate Web Push
Integrate On-site Notification
Integrate On-site Survey
Integrate On-site Feedback
Copy Page
