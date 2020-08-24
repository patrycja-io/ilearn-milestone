
# iLearn - learning platform ☕️

<img src="wireframes/AmIResponsive.png"></img>


<p>Welcome to iLearn platform - this e-commerce website developed by Patrycja Tyra as the final milestone project on the Code Institute Full-Stack web developer course. This website is inpired by udemy.com and made for people who would like to learn programming languages . If you would like to reach out to me please use my GitHub contact details.</p>

## Contents: 

- UX 👍
    - Project Goals
    - Target Audience Goals
    - Site Owner Goals
    - User Stories
    - User Requirements and Expectations
- Design Choices 🎨
    - Fonts
    - Icons
    - Colours
    - Styling
    - Images
    - Backgrounds
- Planning✏️
- Wireframes 🔧
    - Website Layout
    - Account Creation Flowchart
    - Database Design
- Features 🎡
    - Features that have been developed
    - Features that will be implemented in the future
- Technologies Used 👨‍💻
- Planning + Testing: ✏️ 🔌
- Bugs 🐞
- Deployment 🚀
	- Deploying to Heroku
    - Locally run this project
- Credits 💳
- Disclaimer

## User Experience: 👍

### Project Goals:
<p></p>

### Target Audience Goals:

* Browse various products and be offered information about that product.
* Purchase products shown on the webstore.
* Create an account to track orders and purchase items on the webstore.
* A visually appealing and intuitive design.
* A website that is navigable on any device (mobile/tablet/desktop).
* Track orders made via profile dashboard.

### Site Owner Goals:

* Provide users with a safe and secure e-commerce platform in order to generate revenue from sales.
* Encourage user sales with promotions and discounts.
* Build awareness for the brand and attract  suppliers.
* Collect user session data for market research purposes.

### User Stories:

<p>Tim Says: "Ive been looking for a website for a while now that works just as well on my phone as it does my laptop, im far too busy to be sitting at my computer all day 
so I need a site that I can use just as well on my phone."</p>

<p>Mark Says: "Im often skeptical of purchasing on online sites, I like to know that I have a line of communication with the company im paying with just incase there would be an issue
at some point down the line with the order."</p>

<p>Gabe Says: "Shopping on an e-commerce website has got to be easy, if you flood the user with too much choice you can cause them to panic and potentially leave the site and go elsewhere,
make it easy for the user to choose which items they want and buy them, simple!"</p>

### User Requirements and Expectations:
<p>When it comes to shopping on the web, users need to feel safe & comfortable in order for them to actually go through with purchases online, therefore providing the best UX, proper authentication
and using secure payment gateways (in this case Stripe) is necessary to offer the best solution.</p>

#### Requirements:

* Interact with a visually appealing and intuitive website.
* Navigate the website on any device, with ease.

* Add products to a shopping cart & update the cart quantities.
* Purchase products in the shopping cart in a safe and secure way.
* View orders in profile dashboard section.
* Can reach out to the business via email if needed.

#### Expectations:

* The Website will ensure safe storage of user details.
* The users payment information will not be stored in the website's database.
* The Website will load with sufficient speed.
* The Content on the website will be dynamic for any device.
* The Website will be navigable with ease.

## Design Choices: 🎨
<p>I wanted the design of this website to reflect the rustic feel of the pastel colours and various brown colours compliment the imagery used across the site.</p>

### Fonts:

<p>I chose to use Montserrat as the main font family for this website as it provides an elegant & clean style for text and titles. In the essence of keeping the layout clean to encourage user sales, I decided to go with this font.</p>

### Icons:

<p>Thanks to the excellent collection of icons over at font-awesome, selecting icons to use for was really simple, I decided to go with typical icons for the 'icon-navigation' section of the navbar, the cart, the user icon and the burger button, as well as using various other intutitive icons across the project. I use icons in place of link text across the site where possible to provide the best UX possible to the user.</p>

### Colours:
<p></p>

<img src="wireframes/iLearn.png"></img>

### Base Styles:

Colours: 

```scss
$primary-color: #b2e4c8; // primary
$secondary-color: #58493c; // secondary
$tertiary-color: #f1e2d0; // tertiary 
$white-color: #ffffff; // white
$off-white-color: #f2f2f2; // off-white
$black-color: #000; // black
$required-color: #ff0000; // required-red
$error-color: #cc0000; // error-red
$success-color: #25bd2c; // success-green
```

Layout Colours:

```scss
$text-on-white-color: #017735;
$main-nav-color: $secondary-color;
$main-footer-color: $secondary-color;
$main-background-color: $white-color;
$main-panel-color: darken($off-white-color, 5%);
```

Shadows:

```scss
$panel-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);
$text-shadow: 0.5px 0.5px 1px rgba(0, 0, 0, 0.3);
```

Transitions: 
```scss
$fast-transition: 0.25s all ease-in-out;
$slow-transition: 0.5s all ease-in-out;
```

Borders: 

```scss
$default-border-radius: 6px;
```

### Images:
<p>The images used across the website have been sourced from royalty free image website such as <a href="https://unsplash.com/">this</a>. The images are related toin says or  This helps to provide lifestyle imagery to the user and potentially entice them into making a purchase.</p>

## Wireframes/Flowcharts: 🔧
<p>I used Balsamiq</a> to develop the wireframes forthe website, this seemless tool allowed me to easily make a wireframe for each page aswell as a wireframe for each device. I could then easily export them via the tool to .png files in order to save to the project.</p> 

<p>The wireframes for this project can be seen <a href="https://github.com/Geomint/thecofffeeshop/tree/master/wireframes">here</a></p>

### Account Creation Flowchart:

<p>The account creation flowchart for this project can be viewed here <a href="https://github.com/Geomint/thecofffeeshop/tree/master/wireframes/account_auth_flowchart.png">here</a></p>

### Database Design:

* During development oI worked with the standard <strong>sqlite3</strong> database that comes installed with Django.
* In the production version othe database is a <strong>PostgreSQL</strong> database, hosted and provided by Heroku.

### Data Models:

The user model used in this project is that which is provided by Django, click <a href="https://docs.djangoproject.com/en/3.0/ref/contrib/auth/">here</a> to read more about those tables.

#### The Product Model:

The product model within the product app holds the following data for the products .

**Name**|**Key in db**|**Validation**|**Field Type**
:-----:|:-----:|:-----:|:-----:
Name|name|max\_length=254, default=''"|CharField
Grind Size|grind\_size|max\_length=20, choices=GRIND\_OPTIONS, default=FINE,|CharField
Excerpt|excerpt|max\_length=30, default='some string'|TextField
Description|description|default='some string'|TextField
Description2|description2|default='some string'|TextField
Promoted|promoted|default=False|BooleanField
Image|image|upload\_to="static/images"|ImageField
Price|price|max\_digits=6, decimal\_places=2|DecimalField
RRP|recommended\_retail\_price|max\_digits=6, decimal\_places=2, default=0.0|DecimalField

#### The Order Model:

The Order model within the checkout app holds the following data for the orders.

**Name**|**Key in db**|**Validation**|**Field Type**
:-----:|:-----:|:-----:|:-----:
User|user|User, on\_delete=models.PROTECT|ForeignKey
Full Name|full\_name|max\_length=50, blank=False|CharField
Phone Number|phone\_number|max\_length=20, blank=False|CharField
Country|country|max\_length=40, blank=False|CharField
Postcode|postcode|max\_length=40, blank=False|CharField
City|city|max\_length=40, blank=False|CharField
Address Line 1|address\_line\_1|max\_length=40, blank=False|CharField
Address Line 2|address\_line\_2|max\_length=40, blank=False|CharField
Date|date| |DateField

#### The OrderItem Model:

The OrderItem model within the checkout app holds the following data for the OrderItem(s) .

**Name**|**Key in db**|**Validation**|**Field Type**
:-----:|:-----:|:-----:|:-----:
Order|order|Order, null=False|ForeignKey
Product|product|Product, null=False|ForeignKey
Quantity|quantity|blank=False|IntegerField

## Features: 🎡

### Features that have been developed:

* <p>Sliding latest products carousel that allows users to have a quick look at the list of products available to purchase.</p>
* <p>Account creation, user can login and view orders on profile dashboard.</p>
* <p>User can update their details further from the profile dashboard.</p>
* <p>A search bar that returns a list of products based on the users search query.</p>
* <p>A product list and product detail page so the user can click on individual products and find out more if they so wish.</p>
* <p>An active shopping cart that users can add or remove items from and also update the quantities inside.</p>
* <p>Users can take the cart full of items and checkout using the Stripe API which will process the payment details and place an order.</p>
* <p>Users can send a message via the contact form on the contact page, this utilises the sendgrid API to send the messages via email.</p>

### Features that will be developed in the future:

* <p>A reset password link that will send the user a link to reset their password .</p>
* <p>Products will be filterable by a selection of the properties in the model, e.g grind size or price.</p>
* <p>Full integration of the sendgrid API: there are cname records which need to be set at domain level in order to fully utilise this API, however this was beyond the scope of the requried criteria as I do not have a physical domain for, just that which Heroku provides. Read more about the sendgrid integration in the planning & testing section below.</p>
* <p>Order confirmation emails to be sent to the customer upon placing an order.</p>
* <p>A promoted section where the users can see all of the products that are flagged as 'promoted' in the database.</p>

## Technologies Used: 👨‍💻
#### Languages:
* <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>
* <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a>
* <a href="https://www.w3schools.com/js/">JavaScript</a>
* <a href="https://www.json.org/json-en.html">JSON</a>
* <a href="https://www.python.org/">Python</a>

#### Tools & Libraries: 

* <a href="https://jquery.com/">jQuery</a>
* <a href="https://git-scm.com/">Git</a>
* <a href="https://getbootstrap.com/">Bootstrap</a>
* <a href="https://fontawesome.com/icons?d=gallery">Font-Awesome</a>
* <a href="https://sass-lang.com/">SASS/SCSS</a>
* <a href="https://tinypng.com/">TinyPng (image compression)</a>
* <a href="https://sweetalert2.github.io/">Sweetalert2</a>
* <a href="https://pip.pypa.io/en/stable/installing/">PIP</a>
* <a href="http://whitenoise.evans.io/en/stable/">WhiteNoise</a>
* <a href="https://pypi.org/project/psycopg2/">Psycopg2</a>
* <a href="https://pypi.org/project/gunicorn/">Gunicorn</a>
* <a href="https://stripe.com/">Stripe</a>
* <a href="https://www.djangoproject.com/">Django</a>
* <a href="https://code.visualstudio.com/">Visual Studio Code</a>
* <a href="https://sendgrid.com/">Sendgrid</a>

#### Databases:

* <a href="https://www.postgresql.org/">PostgreSQL - Production</a>
* <a href="https://www.sqlite.org/index.html">SQlite3 - Development</a>

## Planning:  + Testing: ✏️ 🔌

#### Planning: 

<p>Planning for this project was extremely important, using and utilising new technology, frameworks, APIs and other tools can often be a challenge if you lack the correct preperation, continue reading to find out how each feature of was planned, tested, and how the feature works within the scope of the website.</p>

<p>Using the wireframes I built using sketch I was able to quickly build a base layout for the website, utilising component files where possible in order to provide resuable code in multiple areas across the website, thanks to the templating language that comes as standard with Django, this was an easy task.</p>

#### Feature Testing 🎡: 

<strong>Contact Form (using Sendgrid Api)</strong>
- <strong>Plan</strong> 📝: 
I wanted to create a contact form in which users on the website could send messages to the business, I have previously built contact forms which just provide the user with a dummy message to say that the message has been recieved, here however I wanted to take advantage of the excellent service Sendgrid provides and actually allow my users to send messages to an inbox.

- <strong>Implementation</strong> 🏭: 
Using the documentation provided by Django and Sendgrid, setting up the contact form was relatively simple, adding the following settings to my 'settings.py' 
```python
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
EMAIL_HOST = '<sendgrid_host_here>'
EMAIL_HOST_USER = 'apikey'  # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = <ports_here>
EMAIL_USE_TLS = True
``` 
- in order to access the sendgrid API. From within the dashboard of sendgrid I had to set up a verified sender in order to allow messages to be sent in from the form. There are 3 cname records that need to be set at the Domain level in order to allow any sender email to be inputted into the contact form, this exceeded the scope of the requirements for the project as I dont have access to a domain fo, just what heroku provided, therefore the only sender email currently available to use on the contact form is "george.pyott@googlemail.com".

- <strong>Test</strong> 🧪: 
To test this feature I had to ensure that the above settings were correct in the settings.py file, and input a dummy message into the contact form making sure that the email is 'george.pyott@googlemail.com'.

- <strong>Result</strong> 🏆: 
Using the dashboard that SendGrid provides, I could see that the email had been sent using their services, and within the inbox specified I could see the message sent from the contact form within 

- <strong>Verdict</strong> ✅: 
Whilst this feature works in the scope of the project criteria, In the future if  were deployed to a none Heroku domain, I would add the necessary records to the DNS so that any email could be used as a registered sender.

<strong>Product List Page</strong>
- <strong>Plan</strong> 📝: 
An e-commerce site always needs a product list page so that the users can browse through the selection of products the business has to offer, therefore a large portion of planning went into this page in terms of have the correct layout in order to provide the best user experience possible. I wanted to include a level of pagination to this page so that the site could have a vast array of products without making the main product list page load times too long.

- <strong>Implementation</strong> 🏭: 
Once I had setup the product model and migrate the table into the database, I could then create the view within the products app that sends a GET request to the database and returns all the products into the products variable, making this available to the front end via the context in the return statement meant that I could loop through each product from the database and render the details using Djangos template language in the HTML. Using the paginator tool from django I was able to simply set how many products I wanted to show per page and render the pagination buttons in the HTML.

- <strong>Test</strong> 🧪: 
To test that this feature worked, I navigated to the 'products.html' page and looked to see if all the products in the database had been rendered into the HTML, I added enough products so that the paginator would fire, 7 to be precise as the paginator will only show 6 per page.

- <strong>Result</strong> 🏆: 
All products within the database were correctly rendered to the 'products.html' page, and the paginator correctly takes the user to the next page showing the 7th product.

- <strong>Verdict</strong> ✅: 
This test has passed based on the above information and criteria.

<strong>Product View Page (detailed view)</strong>
- <strong>Plan</strong> 📝: 
Aswell as having a product list view where the user can see a list of all the products currently in the database, I wanted to include a product detail page, that ther user could navigate to and read more information about the clicked product, further on in production this would allow the business to include more detail about the product, the brand and any other information on this page too. This would be the page that the user makes the final decision, and add to the cart a specified quantity.

- <strong>Implementation</strong> 🏭: 
Passing in the primary Key of the product (primary key in the database), via the URL meant that I could select the product from the database when the product is clicked by the user, this allowed me to build up a page with ONLY the product the user had clicked on.

- <strong>Test</strong> 🧪: 
To test this feature I had to navigate to the product list page and click on any of the products available, once the page had loaded and the product information was there, I checked the url to see what ID the website had taken to me, comparing this to what information was in the database.

- <strong>Result</strong> 🏆: 
The page rendered accuratley with the previously clicked product information, I could then interact with the elements on the page to find out more about the product and add the item to a cart.

- <strong>Verdict</strong> ✅: 
This test passed based on the above criteria and information.


<strong>Cart (add-to, edit-cart, view-cart)</strong>
- <strong>Plan</strong> 📝: 
You can't have an e-commerce website without a functioning shopping cart, therefore planning and testing for this feature was important. I wanted to cart to be available to any user, not just those signed in as in business terms this would mean that there is a higher chance people would buy items due to not having to enter contact details to browse, also gathering session information is an important part of e-commerce research.

- <strong>Implementation</strong> 🏭: 
I had to build a context.py file within the cart app and include this within the context processors section within templates in the settings.py file, this is to tell the app what the cart should look like by default and what information should be available to it. This is also required as the cart is not stored in the database, but rather in the session. Once this was done, I could write the view function for Adding to the cart, Editing the quantity in the cart, and Viewing the cart contents.

- <strong>Test</strong> 🧪: 
To test these cart features I had to do the following:
* * 1: Navigate to the product list page and click through to a product detail view page, then I attempted to add 2 of the item to the cart.
* * 2: Wait to see if the returned page was the cart.html page with 2 lots of the product I had just added.
* * 3: Edit the quantity of the items in the cart to 1 and update the cart.

- <strong>Result</strong> 🏆: 
The website correctly added 2 of the clicked products to the cart session, and the cart.html page was rendered with those items in. Upon editing the quantity of the item to 1 and hitting submit, the cart page was reloaded with just 1 of the item not remaining in the cart.

- <strong>Verdict</strong> ✅: 
This test passed based on the above criteria and information.

<strong>Checkout (using the STRIPE API)</strong>
- <strong>Plan</strong> 📝: 
Being able to checkout products on an e-commerce is also a must, infact its a requirement, and users have a full expectation that the website they are using will handle their sensitive information with care and conform to the legal guidelines. This feature needed to work seemlessly so that the user is informed as much as possible during the payment process.

- <strong>Implementation</strong> 🏭: 
Using the course material supplied by <a href="https://codeinstitute.net/">Code Institute</a> aswell as the Django & stripe documentation, I first constructed the Order and OrderItem models in the checkout app and peformed the migrations to setup the tables in the database. From there I could create the views and forms needed to allow the customer to input their details and process and order. Once these had been built, I setup the validation required by STRIPE in the stripe.js file to handle the creation of the stripe_id, which is required in order to process a payment with the API.

- <strong>Test</strong> 🧪: 
To test the checkout feature, I first needed to add a selection of products to the cart and head over to the checkout.html page, I then entered dummy contact information and used stripe test card details (which can be found <a href="https://stripe.com/docs/testing">here</a>) to attempt to create a purchase, I also tested this feature with incorrect payment information in order to check that the error messages were visible, clear and in a good place for the user to see so that they are informed throughout the process.

- <strong>Result</strong> 🏆: 
The payment was processed and using the stripe dashboard I could see that stripe had processed a dummy payment for the products that were in the cart.

- <strong>Verdict</strong> ✅: 
This test passed based on the above criteria and information.

<strong>'Latest Products' Carousel</strong>
- <strong>Plan</strong> 📝: 
As an added extra for the website I wanted to construct a sliding 'latest-products' carousel using the slick.js library, whilst this isnt actually displaying the 'latest-products' it is showing a list of products in a 'quick-look' fashion as an added extra to use across the website. Being familiar with the slick.js library this wasn't going to be that much of a challenge.

- <strong>Implementation</strong> 🏭: 
To implement this feature I had to make sure that the products from the database were available within the view where I wanted to render the carousel, I setup the slick.js file and included the code for the carousel, making sure to vary the amount of products shown on different device types.

- <strong>Test</strong> 🧪: 
To test this feature I navigated to the home page, (one of the places where this feature is rendered), and looked to see if the products were rendered with the settings specified in the slick.js file.

- <strong>Result</strong> 🏆: 
The products were rendered in a sliding carousel with the settings specified in the slick.js file.

- <strong>Verdict</strong> ✅: 
This test passed based on the above criteria and information.

<strong>Profile Dashboard (orders & edit account information)</strong>
- <strong>Plan</strong> 📝: 
I wanted to develop a profile dashboard in which a user could access information about the items they had purchased, and the orders they had made. Also this would be the place in which the user could edit information about themselves.

- <strong>Implementation</strong> 🏭: 
To implement this feature I had to interact with the Order and OrderItem model in the checkout app, looping through each order in the database and pulling out the orders that match the current logged in users id, then within the template looping over each order.item to render the order in the dashboard. In terms of editing the user details, I had to create a form that would update the user details in the User table based on the information inputted.

- <strong>Test</strong> 🧪: 
To test the orders section of the profile dashboard, I first had to place a dummy order through the website so that there was information stored in the database to render in the HTML. I then navigated to the orders section in the dashboard. To test editing the user information I filled in the form with a new 'Name' and 'Surname' on the account information section and hit the edit details button.

- <strong>Result</strong> 🏆: 
When I navigated to the orders section, I could see that the order I had previously placed was rendered with all the relevant information, to check that this was only viewable by my account, I created a test account to check to see if the order was visible and it wasnt. Upon submitting the user details form, I checked the details rendered in the HTML and could see that the values in the database had been updated.

- <strong>Verdict</strong> ✅: 
This test passed based on the above criteria and information.

<strong>Search Bar</strong>
- <strong>Plan</strong> 📝: 
I wanted to develop an intuitive search feature for the website, so that the user could search for products based on a custom string. This is often an expected feature in e-commerce sites in the modern day so was quite high in terms of importance on my list of features to develop. 

- <strong>Implementation</strong> 🏭: 
I developed a view in the search app that fetches a product based on the query that is collected by the search form. The product(s) if there are multiple are then returned to the HTML so that the user can see what items are returned on their query, I used an if statement to return a 'no-results' page with the passed query so that the user can see there were no products returned for that query.

- <strong>Test</strong> 🧪: 
To test the search function I had to input various search queries into the search bar and hit enter, I intentionally searched for products I knew existed and also typed in queries that would not return products.

- <strong>Result</strong> 🏆: 
When searching for all 7 products returned as at the time of performing this test all the products in the database had the name value of (number)". When searching for "Lion" or "Gazelle", the 'no-results.html' page was rendered and I could see that the website was not able to serve any products based on those queries.

- <strong>Verdict</strong> ✅: 
This test passed based on the above criteria and information.

<strong>User Authentication (register, login, logout)</strong>
- <strong>Plan</strong> 📝: 
Its important on any e-commerce website to allow users to create an account, login and logout, so that they can view relevant information to do with their account and any orders they may have placed. Using the django.auth settings this feature would be heavily supported by the existing functionality that comes with django out of the box.

- <strong>Implementation</strong> 🏭: 
The user table exists in django as standard, So all I had to do was construct the forms and views in order to allow the user to register an account, login to their account and logout from their account.

- <strong>Test</strong> 🧪: 
To test the User features I had to perform each view step by step, First I Created a 'test-account' and checked that the records had been added to the database, Then I attempted a login to the website using those details, after that I logged out of the account using the logout view.

- <strong>Result</strong> 🏆: 
The 'test-account' I had created was visible in the database, and when I attempted to login to the account I was redirected to the profile page where I was greeted by a personalized welcome back message. Finally logging out cleared my session and meant that I would have to log back into the test-account to return to the profile page.

- <strong>Verdict</strong> ✅: 
This test passed based on the above criteria and information.


## Bugs 🐞

#### Bugs During Development: 

<p>Stripe Integration</p>

- <strong>Bug</strong> 🐞: During development of the stripe integration I had ran into an issue in which I could not get the website to process the order using a test card, in debugging mode I was being told that the 'stripe_id' is required to perform a purchase.
 
- <strong>Fix</strong> 🔧: The fix for this bug was irritatingly simple, because the Stripe JS code relies on the jQuery library I had to reorder the order in which I import the scripts in scripts.html so that jQuery was rendered before the stripe.js file.

- <strong>Verdict</strong> ✅: The bug was squashed and orders could now be processed!


## Deployment 🚀


### Running this project locally:

To run locally please follow the steps below!

Before starting make sure you have the following:

* An IDE (interactive development environment) such as <a href="https://code.visualstudio.com/">Visual Studio Code</a>.
* You <strong>MUST</strong> have the following installed on your machine>
* * <a href="https://pip.pypa.io/en/stable/installing/">PIP</a>
* * <a href="https://www.python.org/">Python3</a>
* * <a href="https://git-scm.com/">Git</a>
* You will <strong>need to</strong> create accounts with the following online services in order to run this project.
* * <a href="https://sendgrid.com/">Sendgrid</a>
* * <a href="https://stripe.com/">Stripe</a>

## Instructions:

<em>WARNING: You may need to follow a different guide based on the OS you are using, read more <a href="https://python.readthedocs.io/en/latest/library/venv.html">here.</a></em>


* 1: <strong>Clone</strong> repository by either downloading from <a href="https://github.com/shop">here</a> or type the following command into your terminal.
```bash
git clone https://github.com/

* 2: <strong>Navigate</strong> to this folder in your terminal.
* 3: <strong>Enter</strong> the following command into your terminal.
```bash
python3 -m .venv venv
```
* 4: <strong>Initialize</strong> the environment by using the following command.
```bash
.venv\bin\activate
```

* 5: <strong>Install</strong> the requirements and dependancies from the requirements.txt file
```bash
pip3 -r requirements.txt
```

* 6: Within your IDE now <strong>create</strong> a file where you can store your secret information for the app, I used vscodes settings.json however you can just create an env.py file if you wish.

```bash
{
    "python.pythonPath": "/usr/local/bin/python3",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "files.autoSave": "onFocusChange",
    "files.useExperimentalFileWatcher": true,
    "terminal.integrated.env.osx": {
      "SECRET_KEY": "<your_secret_key_here>",
      "DEV": "1",
      "SENDGRID_API_KEY": "<your_sendgrid_api_key_here>",
      "STRIPE_PUBLISHABLE": "<your_stripe_publishable_key_here>",
      "STRIPE_SECRET": "<your_stripe_secret_key_here>",
      "DATABASE_URL": "<your_database_url_here>",
}
```

* 7: <strong>Enter</strong> the following command into the terminal to migrate models into database.
```bash
python3 manage.py migrate
```

* 8: Then you need to <strong>Create</strong> a 'superuser' for the project using the terminal, enter the following command.
```bash
python3 manage.py createsuperuser
```

* 9: The app can now be ran locally using the following command.
```bash
python3 manage.py runserver
```

Congratulations,is now running locally on your machine! Happy Coding!

### Deploying  to Heroku:

* 1: <strong>Create</strong> a requirements.txt file using the following command.
```bash
pip3 freeze > requirements.txt
```

* 2: <strong>Create</strong> a procfile with the following command.
```bash
echo web: python3 app.py > Procfile
```
* 3: Push these newly created files to your repository.
* 4: Create a new app for this project on the Heroku Dashboard.
* 5: Select your deployment method by clicking on the deployment method button and select GitHub.
* 6: On the dashboard, set the following config variables:

**Key**|**Value**
:-----:|:-----:
DATABASE\_URL|<your\_database\_url>
SECRET\_KEY|<your\_secret\_key>
SENDGRID\_API\_KEY|<your\_sendgrid\_api\_key>
STRIPE\_PUBLISHABLE|<your\_stripe\_publishable\_key>
STRIPE\_SECRET|<your\_stripe\_secret\_key>

* 7: <strong>Click</strong> the deploy button on the heroku Dashboard.
* 8: Wait for the build to finish and click the view project link once it has!

Congratulations, is now hosted on Heroku and is live!

## Credits 💳

* <a href="https://medium.com/developing-with-sass/creating-a-dead-simple-sass-mixin-to-handle-responsive-breakpoints-889927b37740">Mixin For Breakpoints</a>
* <a href="https://www.favicon-generator.org/">Favicon Generator</a>  
* <a href="https://coolors.co/">Coolors.co</a>
* <a href="https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB">Unicorn Revealer</a>
* <a href="https://hatchful.shopify.com/">Logo Design</a>
* <a href="https://unsplash.com/">Unsplash - Royalty Free Images</a>
* <a href="https://www.sh.co.uk/"> Images & Content</a>
* <a href="https://ironandfire.co.uk/"> Images & Content</a>

## Disclaimer
The contents of this website are for educational purposes only.