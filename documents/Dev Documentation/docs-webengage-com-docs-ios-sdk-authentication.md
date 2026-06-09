# iOS SDK Authentication

- URL: https://docs.webengage.com/docs/ios-sdk-authentication
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS SDK Authentication
SDK authentication is the process of verifying the identity of the SDK that is used to communicate with an external service or platform. In the case of WebEngage, authentication is required to ensure that your application is authorized to access the WebEngage API and interact with the platform.
Prerequisite
Supported on WebEngage Android SDK v6.3.0 or higher
Steps mentioned for
SDK authentication: Prerequisite
are completed
Authenticate
To transmit sensitive user data into WebEngage ecosystem, you can generate a JWT token as part of your application. It is important to note that the JWT token should only be generated for a known user and after they have successfully logged in. By generating the token post-login, you can ensure that the user's identity has been verified. This approach reduces the risk of unauthorized access attempts and helps to maintain the overall security of the system.
Swift
WEGJWTManager.shared.JWTToken = "token";
Invalid Token Callback
If the WebEngage SDK encounters an invalid token error, the client will be given the option to regenerate the JWT token using a callback function. This functionality ensures that the client can maintain secure and uninterrupted access to the WebEngage API even in the event of a token error. The ability to generate a new JWT token on the fly reduces the risk of API requests being rejected and increases the overall security of the system. The client can take advantage of this feature to streamline their workflow and ensure that they always have the most up-to-date JWT token available.
Swift
WEGJWTManager.shared.tokenInvalidatedCallback = {
 print("JWT Token is Invalid.")
}
Updated
7 months ago
Getting Started
Copy Page
