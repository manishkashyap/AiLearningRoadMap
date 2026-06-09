# Catalog Based Relays

- URL: https://knowledgebase.webengage.com/docs/catalog-based-relays
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

Catalog Based Relays
Introducing new capabilities to relays that automates business event triggers by uploading them to the catalog. Additionally, it identifies common use cases such as back in stock, low stock, and price drop.
When will these relays be triggered?
Upon refreshing the catalog, we'll assess users and catalog items to identify those that qualify for scenarios such as back in stock, low stock, or price drop.
The triggers will function similarly to batched relays, where a user may qualify for multiple items. These items can be used in personalization as an array of variables.
Event Mapping
To use this feature, ensure you have mapped your catalog appropriately. You need to link a catalog's unique identifier with the event attribute to connect them.
Additionally, for the Price Drop feature, map the event attribute indicating the price to the catalog column containing the current price.
Similarly, for the Low on Stock feature, you just need to indicate “Low Stock Threshold” & "Stock quantity" in the catalog mapping tab.
How to create batched relays?
Step 1
: Navigate to the Relays section of your WE dashboard, and click on the ➕ icon, which then opens to your relays canvas.
Step 2
: From the Triggers option on the left, drag the ‘When catalog refreshes’ block option onto the canvas.
Step 3
: Now click on the block to configure your trigger option.
You are now presented with a new tab, where you can configure your options. The options are as follows.
Campaign type
: This option provides you with 3 options, i.e. Back in stock, Price drop, and Low on Stock.
Back in stock
: If some of your products ran Out of Stock, so some users could not purchase. Now, those products are Back in Stock and you'll like to notify users who could not purchase.
Price Drop
: If the prices have reduced for some products, that's a good opportunity to entice your users who were close to, but didn't purchase.
Low on Stock
: If some of your products are low on stock and you want to clear that stock soon. You can target only those users who showed interest in the product, rather than targeting the general audience.
Step 4
: Select a catalog from the dropdown.
If you choose Back in Stock as campaign type
Once you’ve chosen ‘Back in Stock’ as a campaign type, you can proceed to fill in the following information.
Catalog: From this dropdown choose which Catalog will provide product and stock information and define conditions using this column to identify Products are Back In Stock.
Once you’ve chosen a catalog, proceed to set up the ‘back in stock criteria’, based on this criteria, the system will identify the items from catalog that are back in stock.
Now continue to choose the target audience from the users who did a particular event. For example a user who has added the items to the cart.
You can also choose to exclude users who did a particular event. Like, the User who has already made the purchase.
Look back Period: Choose how long in the past the system should look back to identify target users i.e. 7, 30, 60, or 90 days.
Note
: For the same number of days a user is not allowed to re-enter the relays. So, if the look back period is 7 days, once a user enters the relay he will not be able to re-enter the relay for next 7 days.
👍
Use Case: Back in Stock
You run an online store, and recently several popular items went out of stock, preventing interested users from making purchases. Now that these items are back in stock, you want to notify the users who showed interest but couldn't complete their purchases due to stock unavailability.
By targeting these users and informing them about the restocked products, you increase the likelihood of converting potential customers into buyers. This approach helps recover lost sales opportunities and enhances customer satisfaction by addressing their previous unmet needs.
Keep note that for all users, there will be a re-entry period, which is the same as the look-back period. For example, if the look-back period is 7 days, a user who enters the relay will not be able to re-enter for the next 7 days.
📘
For Shopify Customers Back in Stock criteria should be as below
tracksInventory = true
inventoryQuantity > 0
inventoryPolicy = DENY
If you choose Price Drop as campaign type
🚧
Keep in Mind
To use this feature, you need to specify which column in the catalog indicates the product price.
You also need to map the event's price attribute to show which event attribute captures the price when the event occurs.
Catalog: Select the catalog that will provide price drop information. The system will use the catalog configurations to determine the source of price data.
Choose the target audience from the users who did a particular event.
You can also choose to exclude users who did a particular event. Like, the User who has already made the purchase
Look back Period: Choose how long in the past the system should look back to identify target users i.e. 7, 30, 60, or 90 days.
Note
: For the same number of days a user is not allowed to re-enter the relays. So, if the look back period is 7 days, once a user enters the relay he will not be able to re-enter the relay for next 7 days.
👍
Use case: Price Drop
For example, you manage an online store and have recently reduced prices on several popular products. You want to notify users who showed interest in these products but did not complete their purchase, encouraging them to take advantage of the new lower prices.
By reaching out to users who demonstrated significant interest but didn't buy, and informing them about the price reduction, you increase the chances of converting these potential customers into buyers, thereby boosting sales and enhancing customer satisfaction.
Keep note that for all users, there will be a re-entry period, which is the same as the look-back period. For example, if the look-back period is 7 days, a user who enters the relay will not be able to re-enter for the next 7 days.
If you choose Low on Stock as campaign type
📘
Note
To use this feature, you need to specify which column in the catalog indicates the product quantity.
Catalog: Select the catalog that will provide Low in stock information. The system will use the catalog configurations to determine the source of price data.
Proceed by choosing a low on stock threshold either by choosing ‘Use "Low on stock threshold" from catalog’ that can be enabled if it was set up while mapping your catalog or choose the ‘Indicate threshold manually’ option.
Choose the target audience from the users who did a particular event.
You can also choose to exclude users who did a particular event. Like, the User who has already made the purchase.
📘
Exclusion of an Event
When you apply an exclusion event, the user is excluded entirely. For instance, if a user views two items like "
Nike - Men's Dunk Low Retro
" and "
Nike - Men's Blazer Mid 77 Vintage
" and the inclusion event is "
Product_Viewed
" the user qualifies with both items.
However, if you then apply an exclusion event as "
Product_Purchased
" and the user purchases "Nike - Men's Revolution 6 Road Running" they will be excluded from the relay, regardless of which item they purchased. We are working on refining this behavior.
Look back Period: Choose how long in the past the system should look back to identify target users i.e. 7, 30, 60, or 90 days.
👍
Use Case: Low in Stock
For example, you manage an online e-commerce store and have several products that are low on stock. To clear this inventory quickly, you decide to target users who have shown interest in these products rather than a general audience, as this is likely to be more effective.
By focusing on users who have shown interest in low stock products and informing them about the limited availability, you increase the chances of quickly clearing out your inventory. This approach is more effective than targeting the general population, as it focuses on users who are more likely to make a purchase, thereby boosting sales and customer satisfaction.
Keep note that for all users, there will be a re-entry period, which is the same as the look-back period. For example, if the look-back period is 7 days, a user who enters the relay will not be able to re-enter for the next 7 days.
If you choose Custom Campaign type
This option provides greater flexibility by allowing you to use catalog data to create your own unique notifications for any catalog-triggered events.
Catalog: Choose a catalog with the relevant information for your use case.
Set up rules based on catalog columns to identify items you want to track (e.g., products now eligible for EMI).
Use catalog columns to identify related users.
Specify the look-back period to target users based on past activity.
Combine multiple events with AND/ OR logic to broaden or narrow the targeting criteria.
👍
Use Case: Custom
For example, a business could use catalog relays to notify users about updates to service packages or subscription plans. For instance, if new benefits or add-ons are added to a service, catalog relays can identify users subscribed to that service and send them notifications about the enhanced features.
Similarly, if pricing for a specific service plan changes, users who previously considered or subscribed to that plan can be notified. This approach keeps users informed of relevant changes, improving engagement and retention.
Updated
7 months ago
Getting Started
Reports
Copy Page
