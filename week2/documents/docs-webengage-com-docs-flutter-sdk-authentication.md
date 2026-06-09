# Flutter SDK Authentication

- URL: https://docs.webengage.com/docs/flutter-sdk-authentication
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Flutter SDK Authentication
SDK authentication is the process of verifying the identity of the SDK that is used to communicate with an external service or platform. In the case of WebEngage, authentication is required to ensure that your application is authorized to access the WebEngage API and interact with the platform.
If SDK security is enabled then the application must provide an authorization /JWT token with all the request to WebEngage API in order to access it's user’s data in WebEngage.
Initialization
To begin using the WebEngage plugin, initialize it using the following line of code:
Swift
_webEngagePlugin = new WebEngagePlugin();
User Login
To log in a user, use one of the following methods depending on whether JWT token security is enabled:
With JWT Token:
swift
_webEngagePlugin.userLogin(userName, jwtToken);
This method requires both the
userName
and
jwtToken
to be passed.
Without JWT Token:
swift
_webEngagePlugin.userLogin(userName);
This method is used when JWT token security is not enabled, and only the
userName
needs to be passed.
Token Invalidated Callback
If the JWT token expires or becomes invalid, you can set a callback function to handle this scenario:
Swift
_webEngagePlugin.tokenInvalidatedCallback(_onTokenInvalidated);
Update Secure Token
To update the JWT token for a user, especially in cases where the token is invalid or expired, use the following method:
swift
_webEngagePlugin.setSecureToken(userName, jwtToken);
This method updates the
jwtToken
for the specified
userName
.
Updated
5 months ago
Getting Started
Copy Page
