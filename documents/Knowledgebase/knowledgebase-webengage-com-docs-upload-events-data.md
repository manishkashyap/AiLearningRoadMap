# Upload Events Data

- URL: https://knowledgebase.webengage.com/docs/upload-events-data
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Upload Events Data
WebEngage enables you to consolidate your events data or your historic events data by uploading it manually. You can convert your events data in the excel sheet in the form of a CSV file and upload it.
Understanding Events Data
Events in WebEngage are of the following types. Please refer to
Events
for more details.
System Events
: These events are automatically captured by WebEngage as soon as the SDK integration is done, such as
App Install, App Uninstall
, etc.
Campaign Events
: These events are automatically captured by WebEngage, based on the actions your users perform on the campaigns they receive through WebEngage such as
Email Open, Email Click
, etc.
Custom Events
: These events are sent by you to WebEngage, based on the actions performed by your users on your mobile app and/or website. Some examples of these events are:
Purchased, Searched, Added to Wishlist
, and so on. You can check the various custom events you are already sending to WebEngage under the
Data Management > Events
section of your dashboard.
📘
Only CSV Files with Custom Events Can Be Uploaded
Please note that you can upload the Events CSV file for
Custom Events
only. The file can contain data about an already existing custom event or a new custom event. Any new custom events created through CSV files will be visible on your list of events section in the WebEngage dashboard under the
Data Management > Events list
section.
A custom event has attributes that describe the event's details - who did the event, where the event happened, what time the event happened, etc. Just like
User
attributes, attributes of a
Custom Event
are of two types:
System Attributes
: WebEngage predefines these, and they automatically capture specific details about the event such as time of the event, who did the event, the location where the event happened, etc.
Custom Attributes
: You define these attributes and their data types. For example, a Purchase event could have custom attributes like
Item ID, Item Price, Item Category
, etc.
Any Events CSV file you upload on WebEngage will have a mix of system and custom attributes that define each custom event. Let’s look at a tabular representation of a sample Events CSV file. If you notice the first row in the table below, you will see that this CSV file has a mix of system attributes (
event_name,
user_id,
event_time
) and custom attributes (
product
,
price
,
category
).
event_name
user_id
event_time
product
add_to_cart
223451
2018-01-21 10:23:21
Samsung S10
wishlist
654324
2018-05-18 22:20:00
Wireless Charger
In addition to defining specific event attributes as system attributes, WebEngage has also assigned the relevant data types to these system attributes (e.g., system attribute
event_name
is of
String
data type). When you prepare your Events CSV file, you need to ensure that you use these same attribute names and data types to represent your data.
📘
Important
You cannot change the name of the system attributes or the corresponding data types.
You can find the list of System Attributes for Events CSV File Upload
here
.
Pre-requisite of CSV file
While preparing your CSV file, it is important to remember that all the attribute names must be in the first row and each user's data in the subsequent rows.
Format required for preparing Events CSV file:
The first row should contain the names of the attributes. The three system attributes (
event_name,
user_id,
event_time
) are mandatorily required in each CSV file.
The name and data type of the three system attributes must match the name and data type defined
here
. You are not required to use all the custom event attributes in each CSV file you create. However, if any of the subsequent rows contain data about an attribute, the corresponding attribute name is required in the first row. In other words, the first row cannot have any blank/empty values.
If you are using an existing custom attribute, then the name and data type of the attribute must match the data type you have already defined for this attribute in WebEngage. You can check the custom event attributes and the corresponding data types you have defined on your WebEngage dashboard under the
Data Management > Events list
section.
When defining a new custom attribute, kindly note that you will not be allowed to change its name once an attribute is set. Therefore, it is necessary to be careful when creating new custom attributes.
If you’re defining a new custom attribute, please note that the attribute name's maximum length is 50 characters.
event_name,
user_id
and
event_time
must be the first three data points on each row (or in other words,
event_name,
user_id
and
event_time
need to be the first three columns).
One Event CSV file can have details of only one custom event. You will not be able to include more than one custom event on different rows in the same file.
When defining a new custom event, please note that the maximum length of the event name is 50 characters.
The name of your event or custom attribute should not begin with
we_
.
The maximum length of a
String
data type for an attribute is 1000 characters.
Values of the attribute can only be of the following data types:
Boolean,
Number,
Strings,
and
Dates.
If you want a certain attribute to have a blank/empty value, kindly refrain from entering a
NULL
as a value for those attributes. Instead, leave the value blank/empty.
There can be instances where the attribute may not hold any value for a certain user. For example, if a user hasn't updated their age compared to the one who did, it must be left empty. An empty cell indicates that there is no value for the attribute for the 'Age'. Entering a `NULL' will take it as a string.
Attribute
Data Type
user_id
Age
25
223451
Age
656783
A custom event can have a maximum of 25 custom attributes per data type (i.e., 25 custom attributes of
Number
data type, 25 custom attributes of
String
data type, etc.).
The maximum file size allowed is 200MB. This should be more than sufficient for millions and millions of rows of data.
Please take note of the following limitations for any historical events data uploaded manually through a CSV file:
Historical events data (e.g.
event_time
more than 31 days from now) will be available for creating segments only 15 minutes after the CSV file has been uploaded.
Historical events data will be visible in event analytics, funnels, cohorts after 12.30 am UTC on the same day or the next day, whichever is earliest.
Historical events data will be readily available for creating triggered campaigns, journeys and adding event-based personalization in messages.
Uploading Events Data
How to Access
As shown below, you can access
User Profile Attributes
through
Data Platform > Data Management
or
Data Platform > Upload Data.
Click to enlarge
Overview
Here you will be able to upload the events data file or access any previously uploaded
Events Data
file and download it for future references.
Click to enlarge
On the
Upload Events Data
page, you will see two different sections on the screen:
Upload File:
Here the user can click the Select File button to choose a CSV file to upload. To understand the CSV file format, you can download the sample document in the CSV format. The format required for CSV files is covered in detail in the section below.
History:
History shows the list of uploads in the past and the details of the file. IT also allows you to search the previously uploaded file with the file name and even download the file.
Step 1: Uploading the CSV file
Click on the
Data Management
section in your WebEngage dashboard to upload your file.
Click to enlarge
From the tabs shows on the page, click on the
Upload events Data
tab.
Click to enlarge
You will see two subsections on the screen that will allow you to upload the CSV file:
Upload
subsection where you can upload your CSV file.
Previous Uploads
subsection where you can see the following details of the CSV files you had previously uploaded - file name of the CSV file that was uploaded, who uploaded it and when, the number of records found in the CSV file, the status of the upload (in progress, successful or failure). You may even download any of the CSV files you had previously uploaded by clicking on the download icon.
To begin the upload process, click the
Select File
button in the
Upload
subsection.
Step 2: CSV File Validation
Once you select your file and start the upload process, WebEngage will validate the CSV file before it is uploaded, and if validation is successful, the records will be saved in WebEngage.
There are two levels of validation as described below.
2.1. First Level of Validation
The first level of validation works on the first two rows of your CSV file, i.e., the first row containing the attribute name and the second row containing the value of the first user attributes.
If the first level of validation fails, then the file will not be uploaded, and the records will not be saved in WebEngage.
The first level of validation can fail if any of the conditions described above for
Events
is not followed. When the validation fails, the relevant message will be displayed on the dashboard.
Click to enlarge
When the first level of validation is successful, you will be asked to verify the data before the file gets uploaded and goes for the second level of validation.
Click to enlarge
2.2. Second Level of Validation
In the second level of validation, WebEngage will go through each row of data to ensure that the conditions mentioned under
Events
are met.
You can see the status of the second level of validation under the subsection called
History
.
Status of Second Level of Data Validation
Under
History
, the second-last column denotes the status of the second level of validation. It can be one of the following:
In Progress:
The second level of data validation might take a few minutes to a few hours, depending on the number of records in your CSV file. When the validation is in progress, the status will be
In Progress
.
Failure:
If the second level of validation fails, then the status will show
Failure
. You can click the
Fix
link to understand why the upload failed. On the
Fix
page, you will be able to download a new CSV file. This new CSV file contains your original data-points appended with a data-point at the end that denotes the error on that row (if an error exists on that row). You can then correct the errors and upload the file again.
Success:
If the second level of validation is successful, then your data is processed and will appear on WebEngage in a few minutes to a few hours, depending on the volume of data in your CSV file.
Step 3: View Your Uploaded Data (History)
Click to enlarge
Once the second level of validation is successful, you will be able to view the data on your dashboard in a few minutes to a few hours, depending on the volume of data in your CSV file.
Column Name
Description
File Name
Name of the file that has been previously uploaded.
Uploaded By
Name of the team member who uploaded the file.
Number of Records
The total number of rows in the CSV file.
Uploaded On
The date when the marketer initiated the upload. It can be different from the Completion Date.
Search Bar
If you want to search for a previously uploaded file, you can search by entering the
filename
into the search bar.
Download Symbol
Let's you download the CSV file that was uploaded.
Status
The
Status
in the
History
section helps you understand the status of the document that has been uploaded. Broadly there can be three different status of the document:
Completed-
This shows that the file upload was completed successfully.
Failed-
This Shows that the file upload failed. You can see the details of the failure by clicking on it. You can re-upload the file after fixing the error(s) if any.
In Progress-
Shows the progress of the upload completion. Given the size of the file, the upload time can vary.
We hope this has enabled you to understand the process of uploading User Data. Please feel free to drop in a few lines at
[email protected]
if you have any queries or feedback. We're always just an email away!
Updated
7 months ago
Upload User Data
Engagement Score
Copy Page
