# Bring Your Own Key (BYOK)

- URL: https://knowledgebase.webengage.com/docs/bring-your-own-key
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Bring Your Own Key (BYOK)
This is WebEngage's way of giving you full control over your users data. With BYOK, you can use your own encryption keys to secure any fields marked as PII (such as email addresses and phone numbers). WebEngage handles the encryption and decryption as part of our infrastructure, but the keys are always in your control. We never store or see raw PII.
How it works?
WebEngage’s encryption layer kicks in the moment data hits our system. When user events or profiles come in, any user fields(custom or system) marked as PII are encrypted immediately before they’re stored or processed further.
We use a two-layer encryption method, a temporary data key labelled 'encryption key' encrypts the actual PII, and this key is then encrypted by your 'master key' managed via KMS. The encrypted PII and the encrypted data key are stored together, but the plain text and the encryption key are discarded. When it’s time to send a campaign, WebEngage fetches this encrypted data along with the encrypted data key, decrypts it in memory by calling your key, personalizes the message, and discards it right after. At no point do we store or access the raw PII or your master key.
Encryption Process
For ingested data WE identifies fields marked as PII (any user fields(custom or system) marked as PII).
WE reaches out to you KMS to fetch Data Key and its encrypted form.
This temporary data key would be used to encrypt PII. Each data key would be valid for 30 minutes (or as communicated by your KMS).
Encrypted data would then be stored with WE.
The original PII and the raw data key are discarded immediately.
Decryption Process
While sending campaigns, WebEngage fetches the encrypted PII.
We request the relevant data key from the KMS to decrypt it and get back the data key for decryption.
Using this key, we decrypt the PII temporarily in memory.
The decrypted PII is used to personalize the message.
Once the message is sent, the decrypted PII is discarded and not stored anywhere.
What you need to set up?
A master key hosted in your own KMS.
Provide WebEngage with the access required to encrypt and decrypt using that key.
Decide upfront which fields should be treated as PII.
Be responsible for key rotation, expiration, and access control.
Key Highlights
Feature
What it means
Customer-managed keys
You generate and control the keys, not us
No PII access
WebEngage never stores or sees plaintext PII.
Stateless decryption
Decryption happens only at send-time, and decrypted values are discarded immediately.
Compliance-friendly
Aligns with privacy-focused policies and enterprise data governance requirements.
Transparent audit
Every decrypt request is visible in your KMS audit logs
📘
Things to Know
Clients own the keys - If you revoke access or rotate them, we can no longer decrypt the data. Ingestion will still work, but campaign sends may fail until keys are restored.
This isn't a full data export system - You can’t pull out decrypted data via WebEngage, this system is strictly for send-time personalization.
Key rotation isn’t automated (yet). You’ll need to re-encrypt existing data or provide WebEngage with the updated key details when you rotate.
With increasing focus on privacy, security, and compliance, BYOK helps you meet regulatory requirements while still using WebEngage to engage your users. The goal is to build trust, reduce risk, and give clients complete control over their most sensitive data without compromising on product capabilities.
Updated
28 days ago
Personally Identifiable Information (PII)
Conversion Card Setting
Copy Page
