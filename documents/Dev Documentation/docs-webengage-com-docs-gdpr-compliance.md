# Understanding GDPR

- URL: https://docs.webengage.com/docs/gdpr-compliance
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

GDPR
Understanding GDPR
How WebEngage enables you to comply with EU's GDPR policies (w.e.f May 25, 2018)
The
European Union General Data Protection Regulation (GDPR)
is a comprehensive data protection law that governs how entities operating in the EU, targeting products and services to individuals in the EU or monitoring the behavior of EU citizens, handle personal information. The GDPR is intended to unify and strengthen the protection of personal data of people residing within the member states of the European Union.
GDPR & Your WebEngage Integration
The GDPR defines three primary entities who are involved in the processing of personal data: Data Controllers, Data Subjects, and Data Processors. Each group has different roles and requirements regarding their interactions with customer personal data:
A Data Subject is an end-user whose personal data is being processed by the Data Processor on behalf of the Data Controller.
A Data Controller is the entity that determines the purposes and means of the processing of personal data.
A Data Processor is an entity which processes personal data on behalf and on the instructions of the controller (i.e., a service provider such as WebEngage).
In relation to WebEngage's services:
The Data Subjects are the end-users, customers or other individuals who provide their personal data to you.
You are the Data Controller who decides how and why the personal data of the Data Subjects will be processed.
WebEngage is a Data Processor that processes personal data on your behalf and in accordance with the instructions that we receive from you.
WebEngage is fully GDPR compliant. Let's go over the features that will enable you (as a Data Controller) to comply with your users’ (Data Subjects') requests to exercise their rights.
The Right to Access
Under GDPR, individuals have the right to obtain:
Confirmation that their data is being processed;
Access to their personal data; and
Other supplementary information – this largely corresponds to the information that should be provided in a privacy notice (see
GDPR Article 15
).
WebEngage Compliance
WebEngage enables you to issue a request to
export user profile
containing personal data using REST API. You can export personal data of any of the
Known users
using their
User ID
shown on their respective profile pages on the WebEngage dashboard. You can then provide this personal data to the Data Subject in response to their request to access any personal data being processed by WebEngage as a Data Processor on your behalf.
The Right to Rectification
Individuals are entitled to have personal data rectified if it is inaccurate or incomplete. If you have disclosed the personal data in question to third parties, you must inform them of the rectification where possible.
WebEngage Compliance
If a Data Subject requests that you rectify inaccuracies within the personal data being processed by WebEngage on your behalf, you can use the WebEngage SDKs to send the correct data going ahead, and the WebEngage
/users
REST API to correct existing personal data.
The Right to Erasure
Individuals have the right to get personal data concerning them erased by the controllers. The right to erasure is also known as ‘the right to be forgotten’.
WebEngage Compliance
WebEngage offers APIs to erase personal data if Data Subjects request so. But before deleting user data, you should recommend the Data Subjects to uninstall or log out from all of your applications that use the WebEngage SDK to make sure additional processing of data by WebEngage is stopped.
Once you have halted data collection, you can
create an erasure request
using WebEngage REST API to delete an end-user profile, which will remove all personal data as well as events data records associated with that user from WebEngage data stores.
📘
Deleting an end user from the WebEngage services will permanently delete WebEngage's user profile for that user along with events data stored in WebEngage. As a result, there will be a change in numbers wherever this data is reported on the WebEngage dashboard or in other reports sent by WebEngage or downloaded from WebEngage dashboard.
The Right to Restrict Data Processing
Data Subjects have the right to ‘block’ or suppress the processing of certain subsets of their personal data in the event of inaccurate or improperly obtained data. When processing is restricted, you are permitted to store the personal data, but not further process it. You can retain just enough information about the individual to ensure that the restriction is respected in the future.
WebEngage Compliance
If you have been asked by the Data Subject to restrict the processing of certain subsets of that Data Subject's personal data, WebEngage allows you to mark certain end user profiles as restricted using the
restriction REST API request
. You can only mark the whole user profile as restricted, and not just some subsets of the profile data.
If the end-user allows you to process the restricted subsets of its personal data, you can re-enable the processing using the
re-enable REST API request
.
The Right to Data Portability
The right to data portability allows individuals to obtain and reuse their personal data for their own purposes across different services.
WebEngage Compliance
You may use the WebEngage REST API to
export an end user’s personal data
and furnish it to the Data Subject pursuant to his/her request.
The Right to Object
Individuals have the right to object to:
Processing based on legitimate interests or the performance of a task in the public interest/exercise of official authority (including profiling);
Direct marketing (including profiling); and
Processing for purposes of scientific/historical research and statistics.
WebEngage Compliance
WebEngage provides the ability to mark a user as being unsubscribed from Push, In-app, SMS, Web Push, or Email via our
REST APIs
and via the
iOS
,
Android
, and
Web
SDKs. Customers who receive objections from Data Subjects to receiving such messages can use WebEngage APIs to unsubscribe those end users.
If that is not sufficient, to avoid processing of end-user personal data by WebEngage, the end-user profile should be marked as restricted in the same manner as specified under the ‘Right to Restriction of Processing’ section above.
Rights Related to Automated Decision Making & Profiling
The GDPR prevents automated decision-making without human intervention in certain circumstances, in particular for decisions that “produce a legal effect or a similarly significant effect on the individual.”
WebEngage Compliance
WebEngage does not perform any automated profiling or decision making actions with legal or equivalent ramifications for end users. If you believe that your own usage of the WebEngage platform will have legal or equivalent impacts based upon your own usage, you may choose to delete the User Profile in the same manner as under the “Right to Erasure.”
🚧
Related Reads
To understand how we process the data of our customers' end-users, please read our
Terms of Service
.
To understand how we process our customers' data, please read our
Privacy Policy
.
Updated
7 months ago
Single Sign-On Integration
GDPR Compliance API
Copy Page
