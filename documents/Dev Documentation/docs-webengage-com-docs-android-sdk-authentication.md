# Android SDK Authentication

- URL: https://docs.webengage.com/docs/android-sdk-authentication
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

Android SDK Authentication
SDK authentication is the process of verifying the identity of the SDK that is used to communicate with an external service or platform. In the case of WebEngage, authentication is required to ensure that your application is authorized to access the WebEngage API and interact with the platform.
Prerequisite
WebEngage Android SDK v4.4.1 or higher
Steps mentioned for
SDK authentication: Prerequisite
are completed
Authenticate
You can generate a JWT token as part of your application. The WebEngage SDK will append the current user’s last known JWT to network requests made to WebEngage API. The JWT will be included in the Authorization header of each API request as a bearer token.
Java
Kotlin
WebEngage.get().setSecurityToken(cuid,token);
WebEngage.get().setSecurityToken(cuid,token);
Callbacks
For listening to any errors in the Authentication process, you will have to implement the
onSecurityException
method of the
WESecurityCallback
interface. After implementing this, you will receive the error map in the
onSecurityException
. You can regenerate your JWT token if required and set it again in this method
Java
Kotlin
class WebEngageManager implements WESecurityCallback{
 
 @Override
 public void onSecurityException(Map<String, Object> errorDetails) {
 //callback implementation
 Log.e(TAG, "errorDetails " + errorDetails.get("error"));
 Log.e(TAG, "errorCode " + errorDetails.get("status"));
 }
}
class WebEngageManager : WESecurityCallback {
 override fun onSecurityException(errorDetails: MutableMap<String, Any>) {
 Log.e("TAG", "errorDetails ${errorDetails["error"]}")
 Log.e("TAG", "errorDetails ${errorDetails["status"]}")
 }
}
key
description
sample value
error
Error map with details for the failure.
{response={message=Invalid JWT token passed, status=UID_MISMATCH}}
status
Error code the network request.
401
Updated
7 months ago
Getting Started
Copy Page
