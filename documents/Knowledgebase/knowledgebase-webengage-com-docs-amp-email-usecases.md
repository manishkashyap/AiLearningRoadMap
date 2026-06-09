# AMP Email Use Cases

- URL: https://knowledgebase.webengage.com/docs/amp-email-usecases
- Publication Date: Not found
- Scraped At: 2026-06-04T09:16:15.994414+00:00

AMP Email Use Cases
📘
Please Note
Currently, we support AMP email only for
SparkPost
and
SendGrid
at the moment. We'll be adding support for more AMP-enabled ESPs soon!
In this document, we will some potential use cases that can be achieved using AMP emails. To get a basic understanding of AMP emails and how you can create them on WebEngage refer to this document.
AMP Email Use Cases
1. Dynamic Update from the Server
You can directly display the data from the server to the email and take into account the user's input to refresh the server data as well.
AMP for Email uses a combination of
amp-list
and
amp-form
that share the same
amp-mustache
template. The
amp-list
is hidden when the form is submitted for the first time, and the form's response takes its place.
Before you begin, it is important to define a template and give it an id. This allows the id to be used by both
amp-list
and
amp-form
.
amp-list
The
amp-list
component fetches dynamic content from a CORS JSON endpoint. The response from the endpoint contains data, which is rendered in the specified template.
JavaScript
<script async custom-element="amp-list" src="https://cdn.ampproject.org/v0/amp-list-0.1.js"></script>
amp-form
The
amp-form
component allows you to create forms and submit input fields in an AMP document.
JavaScript
<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>
amp-mustache
Before using the
amp-mustache
template, kindly ensure that it is defined and used according to the
AMP Template Spec
.
JavaScript
<script async custom-template="amp-mustache" src="https://cdn.ampproject.org/v0/amp-mustache-0.2.js"></script>
Together these components can be used as:
JavaScript
<template id="id-template" type="amp-mustache">
 <p>Data sent from a server.</p>
 {{#data}}
 <p>Your response {{data}}.</p>
 {{/data}}
</template>
Let's understand this further with the use case:
👍
Use Case: Notifying the User with the Dynamic Update of the Products in their Cart
Let's an example of a hotel reservation website. A user looks for a room for particular dates and adds it to the cart. The user does not pay for the room or makes the reservation.
When the room reservation for the set dates are more, you can send the email to the user and inform them about the number of rooms left to book. You can show them other available room options to choose from and book the room directly from the email.
One of the best ways to drive customers towards checkout is to give them a dynamic update of the products left in the inventory. If the customer gets to know that the product in their cart or wishlist is running short and can go out of stock very soon, they are more likely to purchase the product.
Incorporating the same in email can be done by:
Step- 1:
Using
amp-list
to fetch the list of items in their cart from the server.
Step- 2:
Using
amp-form
to refresh a single item by making a new server request.
Click to enlarge
You can learn more about the example
here
.
This method is helpful for:
Sending time-sensitive content.
Content involving real-time data
Products running out of inventory
2. Send Surveys through AMP emails
🚧
Please Note
Currently WebEngage does not store responses for Survey/Forms sent through AMP emails.
AMP emails can be used to send survey forms through which the customer can directly reply without clicking on any external link. You can add images and descriptions to make the survey form look more attractive.
An
amp-form
with radio button input fields is used to create a survey form. After the user selects a radio button in the form, a
change
event is triggered, which gives the user a free text input space to enter text.
After the survey form is submitted, a confirmation message is displayed to the user using
<div submit-success>
.
JavaScript
<form method="post" action-xhr="https://amp.dev/documentation/examples/api/submit-form-input-text-xhr">
Let's discuss this further with a use case:
👍
Use Case: Sending an Interactive Survey to Customers regarding the Popular Products
Let's take the example of a cosmetics company that wants to discontinue a few of its products and launch new ones.
They decided to take the survey to determine which ones are most loved by their customers, which products are least preferred by customers, and which ones can improve. This, in turn, will also help the company to understand what their customers want.
To accomplish the same, the company decided to send a survey form. The used
amp-form
with check buttons under different categories. They also used a text box to let the user enter their thoughts. The text box only shows up after the user has clicked on rating against the product. When the user rates a product, a
change
event gets triggered.
You can learn more about the example
here
.
This method can be helpful in:
Sending Surveys
Forms
Asking for Reviews
Click to enlarge
3. Adding a GIF to the AMP Email
Adding GIFs or animated images is a great way to make the email look more interesting. You can send newsletters, information regarding new changes, or a new feature with this.
To accomplish this, you can use a combination of
amp-anim
and
amp-img
.
amp-anim
The
amp-anim
component displays a GIF animation with optimized CPU management.
amp-anim
reduces the resources used by the AMP framework when it's off-screen.
JavaScript
<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>
amp-img
The
amp-img
, AMP provides a powerful AMP HTML replacement. AMP can choose to delay or prioritize resource loading based on the viewport position, system resources, connection bandwidth, or other factors. This way, the
amp-img
components effectively manage image resources during runtime.
amp-img
components must be explicitly given the image size (as in width/height) in advance so that the aspect ratio can be known without fetching the image. The
layout
attribute determines the behavior of the actual layout.
JavaScript
<amp-img
 alt="text"
 src="/static/inline-examples/images/example.jpg"
 width="x"
 height="y"
 layout="responsive"
>
</amp-img>
You can add a
Placeholder
element to further optimize the
amp-anim
element.
Together
amp-anim
and
amp-img
works like:
JavaScript
<amp-anim width="x" height="y" src="gif.name">
 <amp-img placeholder width="x" height="y" src="gif-screenshot.jpg">
 </amp-img>
</amp-anim>
Let's explain it with an example:
👍
Use Case: Adding GIF to a product launch AMP Email
Let's assume a clothing company that wants to offer 50% discount to their customers on 4th of July.
Rather than sending a regular email, they decided to send their customers a GIF incorporated in the email highlighting the festive occasion.
Click to enlarge
You can learn more about the example
here
.
This can be used while sending:
Newsletters
Recommendations
4. Updating the Subscription Settings from Email
The benefit of AMP emails is that the customer can do everything from the email. They can even manage their subscription setting. This particular feature is aided by allowing the elements to change with the user's action or data change response.
To achieve this, a combination of
amp-list
,
amp-mustache
,
amp-form
, and
amp-bind
.
amp-bind
The
amp-bind
enables the elements to change based on the response from the user or data change via data binding and simple JS-like expressions.
However, it is necessary to remember that
amp-bind
does not evaluate the expression initially, and the visual elements must be given a default state and should not rely on
amp-bind
for rendering.
JavaScript
<script async custom-element="amp-bind" src="https://cdn.ampproject.org/v0/amp-bind-0.1.js"></script>
Let look into it further with a use case:
👍
Use Case: Managing Subscription settings
Let's assume a streaming platform wants the user to update their subscription details and give them the option to change their subscription status right from the email.
The streaming service provider decided to send the AMP email, personalized for each user.
They used
amp-bind
to enable the stateful interactivity on the AMP pages to accomplish the same.
You can learn more about the example
here
.
This method can be used for:
Subscription emails
Opting out of email list
5. Collapsible Panel (Accordions) in the Email
Accordions
gives the option to add content in the AMP emails that are expandable and collapsible, just like tabs. They give the option to provide more information within limited space.
amp-accordion
helps in viewing the summary of the content and them jumping to any section. This is extremely helpful for mobile devices as scrolling is required after every few lines.
JavaScript
<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>
Let's understand this further with an example:
👍
Use Case: Sending the Course Details to the User
Let's assume a website that provides study material to interested students. After a user signs up for a program, the platform wants to send the user the entire course structure semester-wise that will be covered.
Accordions
or
amp-accordion
help solve this problem statement. You can send the entire course structure and jump to any section with collapsible and expandable tabs, which reduces the user's scrolling if they view the email on an iPad/ tablet or a mobile phone.
You can learn more about the example
here
.
This method is helpful:
Sending details in limited space.
6. Interactive Game
AMP emails can be used to send interactive games and puzzles to the user.
amp-bind
is used for the same purpose.
Let us understand this further with an example:
👍
Use Case: Tic Tac Toe Gameplay
Let's assume a music streaming platform which wants their existing users to start the three-month premium subscription for free. They decide to send their customers a game of tic tac toe. If the user can get three crosses 'XClik to enlarge' in a line, they win a premium subscription. The customer can also play the game as many times as they want till they win the coupon.
This can be accomplished by using the component
amp-bind
and defining the
gamestate
through
amp-state
, which will hold the value of the current move by the customer.
The value of the current player can be 1 or -1, for 'X' and 'O', respectively. The
board
should hold 9 properties of the tiles. Each tile on the board is a button, and when the player moves, the tile's value gets updated.
Click to enlarge
You can learn more about the example
here
.
These can be used to:
Send interactive puzzles for promotions
Sale or new launch offers
Festive offers
7. Adding Carousel in AMP Emails
Carousels allow displaying multiple contents on the horizontal axis. Immediate children of the
amp-carousel
component are treated as an independent item in the horizontal axis. The carousel allows the user to slide forward and backward through the clicks, swipes, or navigational arrows.
JavaScript
<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.2.js"></script>
Let us understand this further with an example:
👍
Use Case: Adding Product Browse Option in the Email
Let's take the example of a news website that wants to send its users the news of their interest with other recommendations in the form of a carousel. They also want the carousel slides to autoplay after 5 seconds.
This can be accomplished by setting up the carousel type as either a slide, button or letting every image change automatically.
type= "slides"
displays the images as slides.
JavaScript
<amp-carousel width="400" height="300" layout="responsive" type="slides" role="region" aria-label="type='slides' carousel">
 <amp-img src="https://amp.dev/static/samples/img/example_image1.jpg" width="400" height="300" layout="responsive" alt="a sample image"></amp-img>
 <amp-img src="https://amp.dev/static/samples/img/example_image2.jpg" width="400" height="300" layout="responsive" alt="another sample image"></amp-img>
</amp-carousel>
autoplay
feature is only applicable to the
type= slides
option where you can enter the time interval after which the slide shall move to the next slide. The
delay=5000
option means that the slide will move to the next slide after 2 seconds.
JavaScript
<amp-carousel width="400" height="300" layout="responsive" type="slides" autoplay delay="5000" role="region" aria-label="Carousel with autoplay">
 <amp-img src="https://amp.dev/static/samples/img/example_image1.jpg" width="400" height="300" layout="responsive" alt="a sample image"></amp-img>
 <amp-img src="https://amp.dev/static/samples/img/example_image2.jpg" width="400" height="300" layout="responsive" alt="another sample image"></amp-img>
</amp-carousel>
type= "carousel"
displays the image as a continuous strip.
JavaScript
<amp-carousel height="300" layout="fixed-height" type="carousel" role="region" aria-label="Basic usage carousel">
 <amp-img src="https://amp.dev/static/samples/img/example_image1.jpg" width="400" height="300" alt="a sample image"></amp-img>
 <amp-img src="https://amp.dev/static/samples/img/example_image2.jpg" width="400" height="300" alt="another sample image"></amp-img>
</amp-carousel>
Click to enlarge
You can learn more about it
here
.
Carousels can be used to:
Send recommendations.
Send news feed.
Industry-wise Application of AMP Emails
Here are some more ideas where AMP can power your marketing campaigns:
AMP Email Idea
Use Case
Industries
AMP Elements
Ecommerce products
In-stock products could show up-to-date in-stock quantities to urge users to buy soon.
E-commerce
Hospitality
Carousels
List
Bookings
Calenders in the AMP Email can help book restaurants, tickets, meetings, and so on.
Hospitality
Travel
Lists
Product sales
Provide discount codes to the users as promotion to drive sales and engagement.
E-commerce
Hospitality
Travel
Fintech
Quiz
List
Upsell
Depending on the previous view history, upsell includes both transactional and promotional emails.
Applicable across all industries
Your preferred element
Recommendations
Tracking user behavior can help get personally tailored email recommendations for the user.
Applicable across all industries
List
Carousel
Referrals
Allow discount or a freebie when your user successfully refers to your platform.
Applicable across all industries
Your preferred element
Reviews
Send the form on the email and ask for reviews directly.
Travel
Hospitality
E-commerce
Form
Newsletters
Keep your customers updated with new launches and features through newsletters. You can also include some handy tips for your website that will be helpful to the customer.
Applicable across all industries
Animations
Interactive images
Abandoned Cart Campaigns
Remind the customer about their cart and allow them to add their most viewed product or their wishlist product to the cart.
Travel
Hospitality
E-commerce
Financial Services
Carousels
List
Status Updates
Shipping status
Loan application updates
Waitlist updates
Insurance claim updates
E-commerce
Financial Services
List
Upsells
Order confirmation email
Applicable across all industries
Carousels, Accordion
Managing app preferences
Manage email subscription settings
Manage content preferences
Manage notification preferences
Downgrade or upgrade
Entertainment
E-commerce
Form
Updated
7 months ago
AMP Emails
Add Brand Logo to Emails
Copy Page
