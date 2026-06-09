# Web SDK Authentication

- URL: https://docs.webengage.com/docs/web-sdk-authentication
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Web SDK Authentication
SDK authentication is the process of verifying the identity of the SDK that is used to communicate with an external service or platform. In the case of WebEngage, authentication is required to ensure that your application is authorized to access the WebEngage API and interact with the platform.
Prerequisite
Update WebEngage Web SDK integration snippet (mentioned below).
Steps mentioned for
SDK authentication: Prerequisite
are completed.
Update Web SDK Integration Snippet
Add the below script in your web SDK:
JavaScript
webengage.options("httpFetch",true);
Authenticate
You can generate a JWT token as part of your application. The WebEngage SDK will append the current user’s last known JWT to network requests made to WebEngage API. The JWT will be included in the Authorization header of each API request as a token.
JavaScript
webengage.user.login("<CUID>","<AUTH_TOKEN>");
Invalid Token Callback
If the WebEngage SDK encounters an invalid token error, the client will be given the option to regenerate the JWT token using a callback function. This functionality ensures that the client can maintain secure and uninterrupted access to the WebEngage API even in the event of a token error. The ability to generate a new JWT token on the fly reduces the risk of API requests being rejected and increases the overall security of the system. The client can take advantage of this feature to streamline their workflow and ensure that they always have the most up to date JWT token available.
JavaScript
webengage.options('auth.tokenInvalidatedCallback','<CALLBACK>')
Updated
7 months ago
Getting Started
Copy Page
