# Collections

- URL: https://knowledgebase.webengage.com/docs/collections
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Collections
Collections lets you build dynamic data driven criteria from your catalog using flexible filters and logic; powering highly contextual, personalized recommendations
As of now you can create your own strategy by manually selecting events. Keep reading to know how it’s done.
Accessing Collections
Once you’re on the Recommendations page on your dashboard, proceed to click on the 'Add Recommendation' button on the right-hand side of the ‘List of Recommendations’ page.
Now, on the Template Library Page, scroll down or click on the ‘Collections’ button.
‘Create’ card in the 'Collections' section.
How to create Collections?
Begin building your targeted collections strategy by manually building your own filters with our dynamic criteria builder
Once you’re here, you’re introduced to the create recommendation page, from here you can start building your collection.
Firstly, start by choosing the Catalog you want to create this collection for from the dropdown.
Choose a catalog column that you want to sort your criteria by and the sorting order i.e. Ascending or Descending order in which you want your recommendations to be showcased.
Proceed to build the catalog filter criteria.
You can rename your recommendation as by default the name is provided based on the date it is created on.
Build Catalog Filter Criteria
Here’s how to create advanced filtering logic using nested AND/ OR conditions. This feature empowers you to precisely target catalog columns for personalized recommendations and campaigns.
Understanding Nested Logic
Nested logic allows you to combine multiple filtering conditions using AND and OR operators, creating complex criteria for your Collections. This is particularly useful for segmenting your catalog based on intricate user behaviors and attributes.
Steps to Build Nested Logic
Left Side (Catalog Column Selection):
Select the catalog column you wish to filter from the dropdown menu. This column represents the attribute you'll be applying the filter to (e.g., "Product Category," "Price," "User Rating").
Middle Section (Comparison Operators):
Choose the comparison operator that defines the relationship between the selected catalog column and the comparison value. Available operators include:
equals,not equals, greater than, less than, between, contains
and other relevant operators depending on the data type of the catalog column.
Data Type
Operators Available
String
equals to
,
not equals to
,
one of
,
not one of
,
starts with
,
doesnot start with
,
ends with
,
does not end with
,
contain
,
does not contain
,
is not empty
,
is empty
,
contained by
,
not contained by
Numerical
greater than
,
less than
,
greater than or equals to
,
less than or equals to
,
equals to
,
not equals to
,
one of
,
not one of
,
between
,
not between
,
is not empty
,
is empty
Boolean
equals to
,
not equals to
,
is not empty
,
is empty
Date
after
,
before
,
on
,
within
,
present
,
not present
,
before next
,
before last
,
after next
,
after last
,
within next
,
within last
Right Side (Comparison Values):
Define the value against which the selected catalog column will be compared. This value can be sourced from:
Last Event Attributes:
Attributes derived from the user's most recent event (e.g., "Last Viewed Category").
User Attributes:
Pre-existing user data (e.g., "User City," "Purchase History").
Other Catalog Columns:
Compare against values within another column of the same catalog (e.g., "Compare Product Price to Retail Price").
Constants:
Manually entered, static values (e.g., "Red," "100").
Campaign-Supplied Dynamic Values:
Values passed from campaigns, enabling real-time personalization.
Adding Multiple Conditions:
Click the ➕ button to add additional filtering conditions. This allows you to combine multiple criteria using AND and OR operators.
Nesting Conditions:
WebEngage supports up to 3 additional levels of nested AND/OR logic. This enables you to create highly specific and complex filtering rules.
Example:
(Category = "Electronics" AND Price < 500) OR (Category = "Clothing" AND (Size = "Large" OR Color = "Blue"))
Key Considerations:
Data Types:
Ensure that the comparison values and catalog column data types are compatible.
Operator Logic:
Carefully consider the use of AND and OR operators to achieve the desired filtering outcome.
Nesting Complexity:
While 3 levels of nesting are supported, prioritize clarity and maintainability in your filtering logic.
By utilizing nested AND/ OR conditions, you can create highly targeted Collections, enhancing personalization and campaign effectiveness.
👍
Use Cases
👉
E-commerce & Retail:
Personalized Product Suggestions – Show fashion items based on a user's past purchases, preferred brands, and price range, sorted by popularity or discount percentage.
Trending Electronics – Filter the latest mobile phones based on brand preference, budget range, and customer ratings, sorted by newest arrivals.
Grocery Recommendations – Recommend fresh produce or daily essentials based on past purchases and seasonal availability, sorted by best-sellers.
👉
EdTech & Online Learning
Course Suggestions – Recommend courses based on a user’s career interests, past enrollments, and available discounts, sorted by completion rates.
Book Recommendations – Filter books based on user preferences, reading level, and format (audiobook, ebook, paperback), sorted by highest-rated.
👉
Dining and Food Delivery
Restaurant Recommendations - Recommending Restaurants in the users city with the users preferred cuisine, within a certain price range, and sorted by average rating.
Order Recommendations - Filter meal options from restaurants based on dietary preferences (vegan, keto, gluten-free), sorted by calorie count or rating.
Multi level Sorting (Multi sort)
When working with Collections, you may sometimes find that multiple items qualify for the same filter criteria. Multi-Level Sorting helps you decide the order in which these items appear by letting you set up to three sorting levels. You can also consider this as a tie breaker !
Why Use Multi-Sort?
Provides finer control over how results are displayed.
Ensures consistent ordering when multiple items have the same value.
Helps deliver the most relevant results first to your users.
How Does It Work?
Level 1 (Primary Sort, Required): The main sorting rule.
Example: Sort restaurants by Rating (High to Low).
Level 2 (Secondary Sort, Optional): Used only if some items are tied at Level 1.
Example: If multiple restaurants have the same rating, sort them by Number of Reviews.
Level 3 (Tertiary Sort, Optional): Used only if items are still tied after Level 2.
Example: If two restaurants have the same rating and number of reviews, sort them by Distance.
Let us consider this example,
If ten restaurants all have a 5-star rating:
Level 1 (Rating) keeps all 5-star restaurants grouped together.
Level 2 (Number of Reviews) orders them so that restaurants with more reviews appear first.
Level 3 (Distance) is applied only if two or more restaurants still remain tied.
Randomize Results in Collections
When you build a Collection, you usually sort it (for example, highest rating first or most recent first). This means the same items will always appear at the top. Over time, users may only see those same items and ignore the rest, even if the other items are just as relevant this helps keep the experience fresh and engaging for your users.
When to Use Randomize?
Randomization works best when you want to highlight variety and ensure users do not always see the same items. Examples include:
Trending Offers
New Arrivals
Featured Restaurants
How randomize works?
You can apply Randomize at any sorting level.
If Randomize is selected at Level 1, no other sorting rules can be added.
If Randomize is selected at Level 2 or 3, nothing can be added below it.
Each time the Collection is loaded, the items are reshuffled automatically.
Defining Variables within a Campaign
To define variable you have set in the criteria or as code in the html template, you can follow the instructions below. For example:
{{recommend["c_recommendation_1"][xargs(var1=user["custom"]["custom_city"],var2=user["custom"]["custom_boolean"])]["0"]["city1"]}}
Where
"c_recommendation_1"
is the Reference ID you can find in the preview or the recommendation listing page.
While creating your campaigns, in the message creation tab you can use your recommendations as variables for the content to use in your campaign as shown below.
Additionally, for complex use cases where you require values from multiple sources to flow into the campaign, you can use:
{% set Day = "now" | date("dddd") %}
{% set Month = "now" | date("MMMM") %}
{% set DayMonth = Month + " " + Day %}
{{ recommend["c_recommendation_1"][xargs(var1=DayMonth)]["0"]["Order"] }}
Here you can set
DayMonth
as a variable which pulls in two other values, and send it as a variable to the collections query.
For additional support with configuring variable in Campaign for collections, please reach out to your CSM or
[email protected]
.
📘
Examples of Collections
Collections become even more powerful when you combine filters, multi-level sorting, and randomization. Below are some practical examples across industries.
Restaurants
Filter:
(Cuisine = Italian AND Price < 800) OR (Rating ≥ 4.5 AND Location = Mumbai)
Sort:
Level 1: Rating (High to Low)
Level 2: Randomize among equally rated options
Result:
Top-rated restaurants always appear, but the order changes each time for variety.
Ticket Booking
Filter:
(Category = Concert AND City = Delhi) OR (Category = Sports AND Price < 2000)
Sort:
Level 1: Event Date (Sooner to Later)
Level 2: Ticket Availability (High to Low)
Level 3: Randomize if ties remain
Result:
Urgent events show up first, but tied ones rotate to give users a fresh list each time.
E-Commerce
Filter:
(Price < 500 AND Category = Electronics) OR (Category = Clothing AND (Size = Large OR Color = Blue))
Sort:
Level 1: Discount % (High to Low)
Level 2: Randomize among equal discounts
Result:
Biggest discounts lead, while equal discounts shuffle to increase visibility.
Insurance
Filter:
(Premium < 5000 AND Policy Type = Health) OR (Policy Type = Life AND Coverage > 10,00,000)
Sort:
Level 1: Premium Amount (Low to High)
Level 2: Coverage Amount (High to Low)
Result:
Affordable health plans surface first, with life policies ranked by higher coverage.
Randomize Option:
Rotate highlighted policies in campaigns to showcase different options.
Healthcare
Filter:
(Specialty = Dentist AND Location = Bangalore) OR (Specialty = Physician AND Rating ≥ 4)
Sort:
Level 1: Rating (High to Low)
Level 2: Years of Experience (High to Low)
Result:
Best-rated doctors appear first, with experience breaking ties.
Randomize Option:
Randomize tied profiles to help users discover different doctors.
Education
Filter:
(Course Category = Data Science AND Price < 10,000) OR (Mode = Online AND Duration ≤ 6 months)
Sort:
Level 1: Enrollment Count (High to Low)
Level 2: Course Rating (High to Low)
Result:
Popular courses are prioritized, with ratings used for ties.
Randomize Option:
Rotate “Featured Courses” so users see new options on repeat visits.
Updated
7 months ago
Recommendations
Custom Alerts
Copy Page
