# SDK Authentication Prerequisite

- URL: https://docs.webengage.com/docs/sdk-authentication-prerequisite
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

SDK Authentication Prerequisite
In this guide, we'll explain how authentication works with the WebEngage SDK using JSON Web Tokens (JWT), and what you need to do to ensure that your application is properly authorized to interact with the WebEngage platform, particularly in the context of server-side integration.
Implementing SDK Authentication
To implement the authentication workflow, the client must update the WebEngage SDK. Enabling this feature will cause the WebEngage SDK to add the most recent JWT of the current user to any network requests sent to the WebEngage API.
To offer backward compatibility with previous SDK versions, WebEngage offers 3 configuration modes to authorize/validate the token:
Modes
Description
OFF
This is the default setting
; WebEngage will not verify the JWT supplied for a user.
Optional
WebEngage will verify requests for logged-in users, but will not reject invalid requests.
ON
In this mode, WebEngage will verify requests for logged-in users and reject invalid JWT.
Please Note:
If the ON mode is enabled, any API call that does not contain a JWT token for a user will be rejected by the server. Therefore, it is important to exercise caution while enabling the ON mode.
Getting Started
To implement server side authentication, following steps are to be followed:
Generate a public/private key
Generate JWT token
Reach out to us on
[email protected]
to enable the feature once SDK side integration is completed. You will also need to specify the authorization mode you will like to configure (as shown in this section).
Generate a Public/Private Key
Step 1: Generate an RSA public/private key-pair
To generate the RSA keys, you can follow the steps mentioned below:
Generate an RSA private key, of size 2048, and output it to a file named
private_key.pem
:
Shell
openssl genrsa -out private_key.pem 2048
Extract the public key from the key pair, which can be used in a certificate:
Shell
openssl rsa -in private_key.pem -outform PEM -pubout -out public_key.pem
Verify that the key pair has been generated successfully. You can view the contents of the private/public key by executing the following command:
Shell
cat private_key.pem
cat public_key.pem
Step2: Share the public key with WebEngage
Currently the key cannot be shared via dashboard and you will be required to mail it to us on
[email protected]
while requesting to enable this feature and after implementing SDK side changed.
Make sure to keep the private key secured and do not share it with WebEngage while requesting to enable the feature.
Generate JWT Token
JSON Web Tokens (JWT) are a widely used standard for authenticating securely between two parties. Once the private/public key have been generated, the client can use the private key to generate JSON web token on their server and would send the JWT to WebEngage API as part of the API payload. To know more about JSON Web Token, kindly refer
jwt.io
When generating the JWT, the following fields are expected:
JWT Header :
FIELD
REQUIRED
DESCRIPTION
alg
Yes
RS256
typ
Yes
The type should equal
JWT
.
JWT Payload:
Field
Description
cuid
User ID of the logged in user for validation.
exp
(optional)
Token expiration time.
JWT Example :
JSON
Header :
{
 "alg" : "RS256",
 "typ" : "JWT"
}

Payload :

{
 "cuid": "cuid",
 "exp": 1657561941
}

Output : 

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJ1aWQiOiJjdWlkT3JsdWlkIiwiZXhwaXJlIjoxNjU3NTYxOTQxfQ.
1Kuo259BaDA4Q32iJmSYw_s9YCW9Ano8N5KdMMSsLkw
Select Configuration Mode
Once JWT tokens are implemented, reach out to us on
[email protected]
to enable SDK authentication with the configuration setting that you would like (as mentioned in
this
section).
Next step: SDK Side Implementation
Implement SDK authentication for:
Web
Android
iOS
Updated
7 months ago
Getting Started
Copy Page
