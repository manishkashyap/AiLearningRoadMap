# Shield

- URL: https://knowledgebase.webengage.com/docs/shield
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Shield
Shield is WebEngage's enterprise-grade security framework designed to protect sensitive data, control access, and ensure secure platform operations across the entire lifecycle of customer engagement.
It brings together encryption, identity and access controls, secure credential management, auditability, and advanced privacy capabilities into a unified security layer.
Why you need Shield?
Shield helps organizations:
Protect sensitive customer data through encryption and masking
Control who can access data and platform resources
Secure SDK, API, and webhook communication
Maintain visibility and traceability with audit logs and SIEM integrations
Enable advanced privacy models such as ZeroPII and BYOK
Meet enterprise security and compliance requirements
By combining these capabilities under a single framework, Shield ensures that data is protected at rest, in transit, and during processing, while giving enterprises flexibility and control over how their security infrastructure is managed.
Let's learn about various features Shield has on offer.
Data Masking / Encryption
Shield offers a sophisticated framework that merges Data Masking, Auto/Self-Encryption, and ZeroPII.
Data Masking
PII protection requiring specific "View PII" permissions for access
Learn more
Data Encryption
Auto Encryption: Auto Encryption is a procedure wherein WebEngage automatically encrypts the PII fields.
Client Encrypted Data: Client encryption (or Self Hashing), refers to the process where data is encrypted on the client i.e. your side. In this approach, you encrypt the data, the Personally Identifiable Information (PII), before passing it to WebEngage.
Learn more
Single Sign On (SSO)
Single Sign On simplifies access management by integrating directly with your corporate Identity Provider (IDP) through SAML 2.0. This centralized approach allows your team to use their existing enterprise credentials for secure, one-click access to the WebEngage dashboard while enabling centralized identity management
Learn more
.
SDK Authentication
To prevent "spoofing" or unauthorized data injection, Shield requires a secure handshake between your frontend platforms and the WebEngage servers. By enabling SDK Authentication, every request from your App or Website is signed with a unique token and verified on ingestion, ensuring that only legitimate user events are processed
Learn more
.
WebEngage Vault & Credential Decoupling
The WebEngage Vault serves as the centralized security hub, providing a hardened layer for managing the lifecycle of all sensitive integration data. By moving away from local storage within individual feature settings, the Vault significantly reduces the potential attack surface of your marketing operations.
How Credential Decoupling Works
Traditionally, API keys or certificates might be stored within the specific module that uses them (e.g., inside the Email or SMS settings). With Shield, WebEngage introduces Credential Decoupling:
Secret Objects: Sensitive credentials—such as those for ESPs (SendGrid, AWS SES), SMS gateways, APNS certificates, and Storage Spaces—are converted into "Secret Objects".
Pointer-Based Referencing: These secrets are stored exclusively within the Vault. Other platform features only interact with "pointers" to these secrets rather than the raw data itself.
Centralized Encryption: All credentials held within the Vault are encrypted at rest, ensuring that even in the event of a system-level breach, the raw keys remain protected.
Advanced Key Management (KMS)
The Vault offers two distinct modes for managing the master keys used to encrypt your secrets:
Native Mode (Default): This utilizes WebEngage's internal Key Management Service for standard, high-security encryption and is included in the Free plan.
BYOK Mode (Advanced): Available in the Pro plan, this allows enterprises to extend the Vault to their own cloud KMS, such as AWS KMS, Google Cloud KMS, or Azure Key Vault. This ensures your organization retains absolute control over the master keys; if you revoke access in your cloud console, the data becomes unreadable to WebEngage.
Governance and Visibility
To ensure total transparency, the Vault is deeply integrated with Shield’s governance tools:
Rotation: The service is responsible for the secure, automated rotation of sensitive credentials to prevent long-term exposure.
SIEM Auditing: Every time a system process "calls" a credential via its pointer, the action is logged and can be tracked via SIEM integration. This allows security teams to monitor exactly when and how secrets are being utilized across the platform.
Extensible Audit Log Retention
While standard logs may have shorter lifecycles, the Advanced plan extends this storage to a default period of 6 months, providing your security team with a historical lookback window necessary for deep-dive forensic analysis and compliance auditing.
Audit Logs to SIEM Integration
WebEngage DLP system logs are exported in real time to SIEM (Security Information and Event Management) system enabling monitoring, analysis, and alerting for sensitive data activities.
IP-Based Restriction
Control who can access your sensitive marketing data by limiting connections to known, trusted networks.
Dashboard Access:
Restrict login capabilities solely to your organization’s office IPs or authorized VPNs, preventing unauthorized access from public or external networks.
Service Accounts:
Hardened security for your API integrations by whitelisting the specific IP addresses of your backend servers, ensuring that your Service Account credentials cannot be used from an unrecognized source.
User-Level Restriction:
IP restriction at the user level allows you to control access for individual team members by restricting which IP addresses they can use to log in.
How to access it ?
Navigate to
Settings > Teams
from your left navigation pan
On this Team members page, click the three-dot menu next to the user's name
Select IP Whitelisting once that's done, you can add/remove allowed IP addresses or ranges for individual users, and restrict a user to a specific network (e.g. office only).
📘
Note:
Unlike account-level restriction (which applies globally), this only affects the selected user.
You can whitelist individual IP addresses (e.g., 192.168.1.1) or IP ranges using CIDR notation (e.g., 192.168.1.0/24). Maximum 10 entries allowed.
mTLS (Mutual TLS)
For organizations requiring the highest level of transport security, WebEngage introduces mTLS to ensure that both the client and the server verify each other's digital certificates before a connection is established. This "double-handshake" mechanism provides cryptographically backed identity verification, effectively preventing man-in-the-middle attacks for critical data flows, including Webhooks, ZeroPII engagements, and API Data Ingestion.
Dedicated Data Plane
The Dedicated Data Plane is designed for organizations with the most stringent data residency and isolation requirements. Storing end-user data on a dedicated instance, ensures your most sensitive information is siloed from other platform clients, even though the underlying infrastructure is shared. This architecture provides the performance and security benefits of a private environment with the scalability of the WebEngage platform.
ZeroPII
For organizations requiring the highest level of privacy, ZeroPII allows for engagement and segmentation without the platform ever handling raw PII.
Some of the features may not be available for you dpending on your plan. To activate, get in touch with your CSM, or
[email protected]
Updated
15 days ago
Custom Alerts
Key Concepts
Copy Page
