# Catalogs and Recommendations

- URL: https://knowledgebase.webengage.com/docs/catalogs-and-recommendations
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Catalogs and Recommendations
📘
This feature is only available for selected customers. Please get in touch with your Customer Success Manager or
[email protected]
to get access.
Overview
You can create and use multiple catalogs and recommendation strategies to enrich the personalization of your campaigns across various engagement channels, here are some examples:
Recommend products to users depending on their events (added to cart, product viewed, purchased, etc.)
Use the latest data from the catalog for personalization (price, quantity, image, etc.)
Show trending products
For more examples and use cases, you can go through
this deck
.
Prerequisites
Your catalog file must be in a CSV format less than 200 MB in size or XML(RSS) file format less than 200 MB.
Ensure that your catalog has all the data needed to personalize your campaigns -
image, name, price, link, etc.
. Your image links must be publicly accessible. It's advised to use the same image dimensions for all products so that there are no alignment issues in your campaign.
If you want to automate the process of syncing your catalog data, keep your Amazon S3 credentials handy. Our system can import the latest catalog file from your Amazon S3 bucket on a daily basis.
To effectively utilize our recommendation engine:
Ensure that the item ID in your event is the same as the item ID in your catalog.
Pass item IDs in a comma-separated string if there are multiple items associated with that event (example:
Purchase
event)
Ensure that all item IDs are present in your catalog file. A good way to check this would be to use
Events
to check the top item IDs for a particular event (example: check occurrences of
Product Viewed
over
item_id
- convert to table view).
Upload catalogs
Uploading a catalog involves 3 steps - Configuration of basic inputs, Mapping of known fields, Preview and selection of data types.
1. Configuration
Specify a name for your catalog and select your project's industry.
Select
Direct File Upload
as your upload method if you want to do a one-time upload of your catalog file. You will have the option to re-upload a new version of the file manually at a later stage if needed.
Select
Periodic Upload
as your upload method if you want our system to automatically import the latest catalog file daily from your Amazon S3 bucket. Keep the following information handy to integrate Amazon S3 -
bucket name, region name, access key and secret access key
.
Note: our system will replace the entire catalog with the latest file.
Upload a CSV file (max size: 200MB) or XML(RSS) file (max size 200 MB). Field names must follow these rules: i) contain only letters, numbers, and underscores ii) start with a letter or underscore and iii) have a maximum of 300 characters.
2. Mapping
Depending on the industry you selected, you will be asked to map the columns of your catalog with certain recommended attributes.
Note:
item_id
is a mandatory field to be mapped.
3. Preview and data type selection
Preview the values in your file and select the data type of each field in your file.
👍
Pro tip
Think beyond the traditional boundaries of a product catalog.
Treat your catalog as a dynamic data source that can drive powerful, personalized experiences across multiple channels.
For example, when a user enters their pin code on a product detail page, you could instantly fetch and display real-time details of the nearest store manager, including their name, photo, and contact number through an on-site notification or inline content campaign.
View and verify data
View the list page of Catalogs to check the basic info of your catalogs -
status of upload, upload frequency, number of items, etc.
If a catalog's status is marked as
Error
, hover on its status to view more details of the error.
View the list of items to quickly glance through the uploaded data. You can use filters on this page to check specific items (example: price > 1000).
Map events to a catalog
This is a crucial step for using our recommendation engine. Mapping events essentially means stitching the item ID between your catalog and your event data. Map events like
Added To Cart, Product Viewed, Checkout Completed, etc.
so that you can utilize those events to create your recommendation strategies.
Deleting a Catalog
If Catalog DOESN'T have any dependencies
simply click on the three dots adjacent to the particular catalog you'd like to discard and click on the 'Delete' option. Once that's done, you will be presented with a confirmation tab for the same, once you've confirmed that, your catalog will be deleted. Reference in the image below.
If the catalog DOES have dependencies
: You can’t delete a catalog if it’s being used somewhere else, like in recommendations or campaigns. First, you’ll need to remove those linked items. Once there are no active dependencies, the catalog can be deleted. This helps avoid breaking anything that relies on the catalog.
Updated
4 months ago
Multi-Campaign Transaction API
Recommendations
Copy Page
