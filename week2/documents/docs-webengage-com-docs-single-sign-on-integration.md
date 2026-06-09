# Single Sign-On Integration

- URL: https://docs.webengage.com/docs/single-sign-on-integration
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

SSO Integration
Single Sign-On Integration
Integrate your WebEngage dashboard with SSO
Single Sign-On (SSO)
is a user authentication process that enables individuals to securely access multiple applications and systems using a single set of login credentials. SSO streamlines the authentication process by allowing them to authenticate once and gain access to various resources seamlessly. SSO is commonly used across various environments, including enterprise systems, cloud applications, and online services, providing a seamless and secure user authentication experience.
Some of the benefits of SSO are,
Improve user experience:
Since there’s no need to hop between multiple login URLs, or reset passwords, you save between 5 to 15 seconds per login.
Alleviating the Cognitive Burden of Multiple User names and Passwords with SSO:
Your team members can be heavily burdened by the need to remember multiple usernames and passwords for each app, which can cause confusion and havoc. The implementation of single sign-on alleviates this cognitive load.
Strengthening Enterprise Security:
SSO reduces attack surfaces by enabling users to login once a day with a single set of credentials. Enhancing enterprise security is possible through the use of a unified login system. Typically, employees avoid using separate passwords for each application, which increases the risk of security breaches.
WebEngage supports SSO using the SAML2 protocol. The setup process involves adding additional configuration on both WebEngage and your system (IdP).
Getting Started
Once the SSO is enabled, users cannot log in using their username/password and must be added to the IdP.
If you would like WE to test your login process first, you can create a test user on your idp and share the login credentials with WE to test. It may be necessary to disable two-factor authentication temporarily.
Step 1: Exchanging Details
The process primarily starts with exchanging details between you and WE.
(i) Configuration on your IDP
Your IT team can help set up the WebEngage application on your IdP. They will require the following details from WebEngage:
Item
Value
App name
WebEngage
Sign-on URL
https://dashboard.webengage.com/sso/saml/login?action=viewLogin
Issuer URL
https://webengage-sso.com/
Reply URL
https://dashboard.webengage.com/sso/saml/verify
SAML NameID
Use the email address which will be used for logging in
You also need to add attribute mapping for email. Make sure the name field contains the word email (lowercase). For example:
email
,
emailAddress
,
login_email
, etc. Note: 2-Factor Authentication and other security settings should be configured per your internal security policies.
(ii) Configuration on WebEngage
Additionally you also need to configure the following 3 mandatory details on your WebEngage’s SAML/SSO integration page, they are:
IDP’s Login URL (post-binding)
IDP’s Entity ID
And, upload IDPs certificate (after the 2 above mentioned details have been saved)
You can also include your SP entity ID name; if it's not necessary, you can leave it blank.
Step 2: Send WebEngage the IDP Metadata, Certificate, and Test Login Details
Once your IDP is configured, you will need to send the following items to WebEngage:
Item
Comment
metadata.xml
The IDP metadata that WebEngage will import into the system. The filename can be different.
certificate.cer
The certificate file that WebEngage will import into the system. The filename can be different.
Test credentials (optional)
Minor misconfigurations in SAML2 might result in login not working. If you would like WebEngage to test the login flow before it is handed over to you, supply test credentials for login. Note that two-factor authentication may need to be temporarily disabled for this.
Once WebEngage receives these details, your metadata settings will be imported and SSO will be enabled for your account.
Step 3: SSO confirmation mail for existing users
Once the first step is completed the existing users should get a SSO confirmation email.
To log in to the dashboard use the following steps.,
Visit the URL provided by WebEngage and type your email address as configured for SSO in your IdP. You should be redirected to your system for logging in, and then back to WebEngage.
In case you would like to grant access to a new user via SSO, then use the following steps.
Create a user within your system (IdP).
Once the user is configured on your system, they will be allowed to log in.
However, you still need to add the user to WebEngage so that you can set their access control and privileges.
The "Add Another Admin" button can be used to add a new admin in the admin panel.
The email should be the same as the SSO email address which will be used.
The new admin is sent an invite via email. While creating an admin, you can choose privileges that should be assigned to them.
👍
Note
Minor misconfigurations in SAML2 might result in the login not working. We do not support two-way certificates at this point.
Please refer the flow diagram below for general understanding of how SAML flow works between IDP and SP.
Step 4: Logging In
To log in, visit the following URL:
https://dashboard.webengage.com/sso/saml/login?action=viewLogin
,
Type your email address as configured for SSO in your Identity Provider (IDP). You will be redirected to your system for login, and then back to WebEngage.
Updated
12 days ago
RCS Service Provider
Understanding GDPR
Copy Page
