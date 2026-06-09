# Custom Recommendation API

- URL: https://docs.webengage.com/docs/custom-recommendation-api
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

REST API
Custom Recommendation API
WebEngage used to generate recommendations based on three categories: static, personalization, and relevant. Now, you can create and send your own recommendations via API.
Manual or Custom Recommendation is a strategy where the recommendations are determined entirely by the client’s input through a file (currently only CSV format is supported), without any involvement from WebEngage’s AI-powered recommendation engine. Clients are asked to ensure the accuracy, quality, and proper formatting as specified. Please note that 'manual' and 'custom' recommendations refer to the same process and will be used interchangeably throughout the documentation.
Currently WE supports 3 types of Custom Recommendation
:
Static Recommendation
Personalized Recommendation
Relevant Recommendation
CSV Input Format
Keep in mind that, in all the following the Recommended IDs are the catalog’s primary key column’s values. So, those catalog items will be provided as the recommendations.
Static Custom input format
User Item (Personalized) Custom Input Format
User ID is the
cuid
of the user.
Item Item (Relevant) Custom Input Format
Item IDs will be catalog’s primary key column’s values.
API
There are two scenarios: uploading for the first time, which involves creating a new recommendation, and re-uploading data for an existing recommendation. Here are the steps:
First Time Upload
Use the following curl to form the request
cURL
curl --location '{{baseUrl}}/api/v1/accounts/{{licenseCode}}/recommendation/manual/upload' \
--header 'Authorization: Bearer {{authorizationToken}}' \
--header 'Cookie: _we_rf=; _we_rf=' \
--form 'recommendationMeta="{
 \"type\": \"{{recommendationType}}\",
 \"name\": \"{{recommendationName}}\",
 \"catalogSlug\": \"{{catalogID}}\",
 \"createdBy\": \"{{createdBy}}\"
}"' \
--form 'file=@"/path/to/file"'
Fill in the placeholders in the headers and the key recommendationMeta in the Body (form-data) section:
{{recommendationType}} - choose the prototype befitting your strategy, fill with
STATIC_MANUAL (for custom static recommendations)
ITEM_ITEM_MANUAL (for custom relevant recommendations)
USER_ITEM_MANUAL (for custom personalized recommendations)
{{recommendationName}} - Desired name of your recommendation which will be shown on the UI.
{{catalogSlug}} - catalogID can be seen on the UI, once you click on the catalog on the main page.
{{createdBy}} - Mail ID of the creator for audit.
Fill your Authorization token in the headers.
Head on to the
Body
section and proceed to the
form-data
sub-section, add the csv file against the key named
file
.
Re-upload Recommendation Data for an Existing Strategy
Use the following curl to form the request
cURL
curl --location '{{baseUrl}}/api/v1/accounts/{{licenseCode}}/recommendation/manual/upload' \
--header 'Authorization: Bearer {{authorizationToken}}' \
--header 'Cookie: _we_rf=; _we_rf=' \
--form 'recommendationMeta="{
 \"type\": \"{{recommendationType}}\",
 \"name\": \"{{recommendationName}}\",
 \"catalogSlug\": \"{{catalogID}}\",
 \"createdBy\": \"{{createdBy}}\",
 \"recommendationSlug\": \"{{recommendationSlug}}\"
}"' \
--form 'file=@"/path/to/file"'
Follow steps 2 and 3 of the first upload steps.
Additionally in this case we need to fill the {{recommendationSlug}} to point to the desired recommendation strategy.
How to obtain the recommendation slug?
To obtain the {{recommendation slug}}, use the following steps.
Navigate to the Recommendation section of your WebEngage dashboard.
Right-click on the page and select 'Inspect,' then go to the Network tab.
Click on the three dots next to the recommendation for which you need the slug on your WebEngage dashboard, enter the User ID, and click on 'Preview Recommendations.'
You'll see several requests appear in the Inspect panel. Look for the 'preview' request, where you'll find the recommendation slug within the Request URL field, that usually begins with either of these
s_recommendation , i_recommendation or u_recommendation
followed by a number.
📘
Limitations of Recommendations
User can add a maximum of 5 recommendations per item or user ID
file size for uploading is restricted to 200mb
XML file format is not supported
WebEngage's custom recommendation feature allows clients to control their recommendation strategies by creating and sending tailored suggestions via API. Supporting static, personalized, and relevant recommendation types, clients can ensure precise and aligned recommendations. The process involves creating and uploading CSV files and is managed through straightforward API steps. This flexibility enhances personalized user experiences, driving engagement and conversions.
👍
Use Case: Custom Recommendation for E-commerce
An e-commerce platform can leverage WebEngage’s custom recommendation feature to offer tailored product suggestions.
Static Recommendations
: A new collection launch can use static recommendations to highlight specific products to all users.
Personalized Recommendations
: Based on a specific segment, we can target recommendations to users according to their location, history, or any user attribute. This allows you to deliver tailored recommendations to each target group.
Relevant Recommendations
: We provide specific recommendations for particular item IDs based on your insights. For example, a product like a cricket bat could have tailored recommendations such as a ball, stumps, and gloves etc.
By creating and uploading their custom CSV files, the platform ensures that the recommendations are aligned with their specific marketing and sales strategies, providing a more targeted and effective user experience.
Updated
7 months ago
Catalog Upload via REST API
Multi-Campaign Transaction API & User Profile Upsert
Copy Page
