# ***Seline & Tam Jewelry - Portfolio Project 5 Ecommerce***
---
# **1. Key project information**

- **Description :** This Portfolio Project 5 website called **Seline & Tam Jewelry** is a site of imaginary online shop that sells jewelry like bracelets, earings, necklaces and rings. User can easily browse through the shop items, **add/delete** items from their **Wishlist**, express their opinion by leaving a **review** and **comment** on items and most importantly order their selected items for home delivery including online payment.
- **Key project goal :** To offer all visitors of **Seline & Tam Jewelry** site the option to buy their chosen products, select delivery option and finish payment online without the need of leaving the house.
- **Audience :** The audience age of this website is for 18 years and up.
- **Live version :** Live version of **Seline & Tam Jewelry** e-shop page can be viewed [here](https://seline-and-tam-jewelry-ef3ef903eb25.herokuapp.com/).
- **Developer :** [Grozav Sarah Ligia](https://github.com/tomik-z-cech/)

![Mockup](static/media/documents/mockup.png)

---

# **2. Table of Contents**


---

# **3. Wireframes and Planning**

### Canva wireframes/mockups

I used Canva to make mockups for the website and design how I initially imagined the site would look. 

<details><summary>Desktop Wireframes</summary>

### Desktop

**Note!** It should be mentioned at this point that during development, I decided to change a few things in my design.

Also missing here is the contact page. I originally intended this to be in the navbar but now I included a button in Contact section at the bottom of the home page.

#### Home 
![Home](/static/media/documents/home.png)

#### Clock
![Clock](/static/media/documents//clock.png)

#### Collection 
![Collection](/static/media/documents/collection.png)

#### Promise
![Promise](/static/media/documents/promise.png)

#### Contact
![ontact](/static/media/documents/contact-section.png)

#### Products
![Products](/static/media/documents/products.png)

#### Product Detail
![Product-detail](/static/media/documents/product.png)

#### Shopping Bag
![Shopping-bag](/static/media/documents/bag.png)

#### Checkout
![Checkout](/static/media/documents/checkout.png)

#### Profile
![Profile](/static/media/documents/profile.png)

</details>

---

### Early Development

At the start of the project, even though I had the wireframes as versions of how I wanted the site to look, I more often than not made early mockup versions of the pages to quickly get the framework of the pages set up and to test whether I might like to do something another way or differently from the wireframes. 

Here is an early example of my index page, mocked up at the very start of the project. 
Key differences here include two more sections about more informations about the jewelry store that I decided to dont include them anymore in my project so that I could focus more on backend. But I want to create them in the future.

![Early Development Index Section](/static/media/documents/more-sections1.png)

![Early Development Index Section](/static/media/documents/more-sections2.png)

I started the project with the home page and nav bar, before installing django allauth and getting the base templates for that. From there, I began working on backend more and didn't focuse on frontend because I wanted to leave it the last, first to make my project work and then add design and fronted details to look better.

Here is an early mockup of my collections page which I decided to don't make it anymore because I did a dropdown button in the navbar from where the user can select easily the collection he wants to see.

![Early Development Collections Page](/static/media/documents/collection-page.png)

---

# **4. User Experience (UX)**

### **4.1.1 The Idea**
- The intention of **Seline & Tam Jewelry** site is to be friendly online shop where users can browse variate of products sorted between categories. Besides that, user can read details of each product, see product reviews and comments.

### **4.1.2 The Ideal User**

The target audience are individuals who are seeking luxury jewelry. Those who want to make gifts or to wear a luxury jewelry for themselves.

- Ideal user likes to shop online
- Ideal user likes to explore new trends and ideas in the jewelry field
- Ideal user likes to share their opinion in form of **reviews** and **comments**

### **4.1.3 Site Goals**

- Offer users ability of shopping online without leaving their home
- Offer users ability of reading other people comments on products
- Offer users ability to add items to their **Wishlist** if they want to save the item for later
- Offer users the ability to see details of each item in shop ( price, description, collection etc. ) 
- Provide site visitors with an easy to navigate site to view jewelry products

### **4.1.4 SEO and Web Marketing**

**Who:** I am marketing predominantly towards a jeweler-enthuasiast.
**What:** I am selling jewelry, designed to cater towards this audience. I therefore make it very accessible and clear on my site, so that the audience can go directly towards what they are looking for. I include images of jewelry, designed to excite the site viewer into wondering what it's like to wear them with some sophisticated clothes. It was equally important to make clear titles and key pieces of information available for the site viewers to see on which ever respective page/product they are viewing.
**How:** Based on my B2C model, I decided single payments with Stripe were the best payment option for the products I'm offering. I can update users on new products and general news through an opt-in mailchimp newsletter subscription and I have created a Facebook page which users/clients can view and follow to keep up to date through a social network.


Software developers play a role in making sure their website can be easily found through search engines, including the reviews of Google Search.
Therefore, when implementing SEO (Search Engine Optimisation) tools, the best means available to you are through descriptive and relevant keywords, sitemaps.xml and robots.txt files.

### **4.1.5 Keywords and sitemap/robots**

- I included keywords and more tags in my base.html document. This allowed me to define keywords, an author, a site description and a viewport. For the keywords themselves I thought about short and longer words and phrases respectively that might be looked for. 

- I started with fairly obvious short words including: jewelry, gold jewelry, gold bracelet, gold necklace,gold rings,gold earings, luxury jewelry.

- I then expanded in to short phrases, including: golden luxury jewelry

- I have included a sitemap.xml file in the root directory, which allows search engines to crawl through my site and make content more discoverable.

- I have a robots.txt file which provides the location of the sitemap and also defines any folders/files which are prohibited from search engine crawlers.

### **4.1.6 Agile Methodologies**

To plan tasks to implement for my website, I used Github Projects, which is a Kanban style board to track your project progress. You can track user stories, epics, ideas, to-do items and you can all see what tasks have been completed.

You can see my project board [here](https://github.com/users/SarahGrozav1/projects/8)

### **4.1.7 User stories**

- [User Story: Products Page]([#1](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/1))
    - As a Site User I want to be able to view a list of products so that I can select some to purchase.

- [User Story: Detail Product Page]([#2](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/2))
    - As a Site User I want to be able to view individual product details so that I can see the price, description, rating, product image and collection.

- [User Story: Shopping Bag]([#3](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/3))
    - As a Site User I want to be able to easily see the total of my purchases at any time so that I can avoiding spending to much.

- [User Story: Register]([#4](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/4))
    - As a Site User I want to be able to easily register for an account so that I can have a personal account and be able to view my profile with orders I have made.

- [User Story: Log in/ Log Out page]([#5](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/5))
    - As a Site User I want to be able to easily login and logout so that I can access my personal account information.

- [User Story: Success message]([#6](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/6))
    - As a  User I want to receive an email confirmation after registering so that I can verify that my account registration was successful.

- [User Story: Profile Page]([#7](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/7))
    - As a User I want to be able to have a perosnalized user profile so that I can view my personal order history and order confirmations and save my payment information.

- [User Story: Navbar]([#8](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/8))
    - As a Site User I want to be able to sort the list of available products so that I can easily identify the best rated, best prices and sorted products.

- [User Story: Navbar collections dropdown button]([#9](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/9))
    - As a Site User I want to be able to see every product from witch collection it is so that I can find it easier.

- [User Story: Product Management Page]([#10](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/10))
    - As a Store Owner I want to be able to add a product so that I can add new items to my store

- [User Story: Edit product button]([#11](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/11))
    - As a Store Owner I want to be able to Edit a product so that I can change product prices, descriptions, images and other product criteria

- [User Story: Delete product button]([#12](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/12))
    - As a Store Owner I want to be able to Delete a product so that I can remove items that are no longer for sale.

- [User Story: Contact Page]([#13](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/13))
    - As a Site User I want to be able to contact the store owner so that I can ask if I have questions.

- [User Story: Product Reviews]([#14](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/14))
    - As a User I want to be able to see others reviews so that I can decide if I want to purchase that product

- [User Story: Edit review button]([#15](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/15))
    - As a User I want to be able to edit my reviews so that I can update them when I want or when I made a mistake.

- [User Story: Delete review button]([#16](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/16))
    - As a Site User I want to be able to have a button for delete so that I can delete my review

- [User Story: Error message]([#17](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/17))
    - As a Site User I want to be receive error messages so that I know what I did wrong

- [User Story: Google Map]([#18](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/18))
    - As a Site User I want to see a Google Map so that I can find the store easier

- [User Story: Wishlist Page]([#19](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/19))
    - As a Site User I want to have a wishlist page so that I can see my favourite products

- [User Story: Add to wishlist button]([#20](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/20))
    - As a Site User I want to see an 'add to wishlist' button so that I can add my favourite product to wishlist page.

- [User Story: Remove button from wishlist Page]([#21](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/21))
    - As a Site User I want to have a 'remove' button for every product adde in wishlist so that I can remove it when I dont want it to be there anymore.

- [User Story: Admin Panel messages]([#22](https://github.com/SarahGrozav1/seline-and-tam-jewelry/issues/22))
    - As a Store Owner I want to be able to see mesages from users so that I know their concern about the website


### **4.1.8 Epics**

- Epic: Install Django
    - As a Developer I would like to install Django so that I can begin working on my project.
    
- Epic: Initial Deploy to Heroku
    - As a Developer I would like to deploy to heroku early so that I can confirm my configuration is wired up correctly.

- Epic: AWS
    - As a Developer I would like to create an AWS S3 bucket so that I can store my static files and media.

- Epic: Login/Logout
    - As a Site User I would like to Login and Logout so that I can keep my account secure.
- Epic: Basket
    - As a Site User I would like to View a Basket so that I can check my orders before checking out.
- Epic: Stripe Checkout
    - As a Site User I would like to checkout so that I can purchase the items I came to buy.
- Epic: Mailchimp Newsletter
    - As a Site User I would like to Sign up to a mailing list so that I can get new information from the business, including new products or promotions.
- Epic: Testing
    - As a Software Developer I would like to Create Manual tests so that I can check the quality and functionality of my code.

---

# **5. Features**

Below is a comprehensive list of the site features and their relations to the user stories:

1. A Nav Bar/Header that:
    - is split in two with a top nav where the user can find company logo that redirects to the   home page when clicked on, account icon when it is clicked on the user can find register or log in functionalities and if it logged the user will see my profile, wishlist and logout functionalities and the last is the basket icon
    - has a middle nav which serves as the main navigation of the site where the user can find a house icon and see products by category by rating , by price or by collections

 - Acceptance Criteria:
        - A Responsive fixed-top header that contains a logo, user icon and basket icon on desktop and a triple line menu icon user icon basket icon and a basket icon on mobile/tablet
        - Nav bar is clean and consistent with the theme and overall design scheme

    ![Navbar](/static/media/documents/navbar.png)


2. A Home Page that:
    - Contains more sections
    - Contains a background image
    - Contains a title and subtitle and a button
    - serves as the entry page 

    ![Home Page](/static/media/documents/home-page.png)

    - Acceptance Criteria:
        - Home Page features a Nav Bar, Main body with Hero image
        - Has a consistent theme and colour scheme
        - Most Pages can be navigated to directly from this one point
        - Theme of site and target audience easily identifiable from the home page alone

  - About Section:

      - Contains three cards with images and text
      - Contains a background with shape divider

    ![About Section](/static/media/documents/about.png)

    - Acceptance Criteria:
        - About section features three cards with details about the company jewelry
        - Has a consistent theme and colour scheme

  - Countdown Section:

      - Contains a background image
      - Contains a header 
      - Contains a digital clock made with js
    
    ![Countdown Section](/static/media/documents/countdown.png)

    - Acceptance Criteria:

      - Countdown Section features a text header with the date of upcoming collection
      - Has a real countdown clock until the date of upcoming new collection
      - Has a consistent theme and colour scheme

  - New/Last Collection Section:

      - Contains a header with the name of the new collection
      - Contains a paragraph with key words
      - Contains three cards with images
      - Contains name and price of the products showed in the image above
      - Contains a see more button
    
    ![New Collection Section](/static/media/documents/new-collections.png)

    - Acceptance Criteria:

      - Countdown Section features a text header with the date of upcoming collection
      - Has a real countdown clock until the date of upcoming new collection
      - Has a see more button for the user to see more products of that new collection
      - Has a consistent theme and colour scheme


  - Our Promise Section:

      - Contains a header with the title of the section
      - Contains a shape divider for the top of the section
      - Contains four icons 
      - Contains text for each icon
    
    ![Our Promise Section](/static/media/documents/our-promise.png)

    - Acceptance Criteria:

      - Have four icons for more informations 
      - Have a text under each icon for the user to understand the icons for more informations
      - Has a consistent theme and colour scheme
      
  - Contact Section:

      - Contains a shape divider for the top of the section
      - Contains a background image only on the half of screen
      - Contains the names of the website managers
      - Contains a button
      - Contains location , email address and phone number
    
    ![Contact Section](/static/media/documents/contact.png)

    - Acceptance Criteria:

      - Have a "Send a message" button for users to contact the seller 
      - Have contact information for users to find them easily
      - Has a consistent theme and colour scheme

  - Map Section:

      - Contains a API Map
    
    ![Contact Section](/static/media/documents/map.png)

    - Acceptance Criteria:

      - Have a map for users so that they can find easily the store

  - Footer:

      - Contains a hr to separate the page from footer
      - Contains five social media icons
      - Contains a copyright text
    
    ![Contact Section](/static/media/documents/footer.png)

    - Acceptance Criteria:

      - Have social media links inclusive business facebook page for users to find more informations about store and products such as new collections, reviews and owners story.

3. A Contact Page that:
    - Contains navbar
    - Contains a contact form
    - Contains a button
    - Contains a paragraph 
    - Contains footer

    ![Contact Page](/static/media/documents/contact-page.png)

    - Acceptance Criteria:
        - Contact Page features a navbar so that the user can easily navigate trough the pages
        - Has a consistent theme and colour scheme
        - Have a form so that the user can send easily a message to store owners
        - Have a submit button so that the user can submit the form
        - Have a paragraph with facebook link to invite the users to join the bussiness facebook page


4. A Products Page that:
    - Contains navbar
    - Contains a heading
    - Contains a paragraph
    - Contains all products
    - Contains footer 

    ![Products Page](/static/media/documents/products-page.png)

    - Acceptance Criteria:
        - Products Page features a navbar so that the user can easily navigate trough the pages
        - Has a consistent theme and colour scheme
        - Have a title so that the user know on what page is and in what category
        - Have all products so that the user can see them and buy if wants
        - Have a paragraph where it writes how many products are in the category

  - If user wants to see products from one collection or by category:

      - Contains a different heading for each collection or category
    
    ![Collections Heading](/static/media/documents/collections-category.png)
    ![Category Heading](/static/media/documents/products-by-category.png)

    - Acceptance Criteria:

      - Heading changes on every collection or category so that it would be easier for the user to know in what category or collections he is 

5. A Detail Product Page that:
    - Contains navbar
    - Contains image of the product
    - Contains informations about product
    - Contains quantity field
    - Contains add to bag button
    - Contains wishlist button
    - Contains keep shopping button
    - Contains review section
    - Contains footer 

    ![Detail Product Page](/static/media/documents/detail_product.png)

    - Acceptance Criteria:
        -Detail Product Page features a navbar so that the user can easily navigate trough the pages
        - Has a consistent theme and colour scheme
        - Have an image to see how the product look
        - Have informations about product so that the user can read and know more about product
        - Have a wishlist button so that the user can add to the wishlist the product if he wants
        - Have a keep shopping button so that the user can return to all products if he want to see more
        - Have a add to bag button so that the user can add to bag the product if he wants to buy
        - Have a review section where user cand add a review and see others reviews


6. A Bag Page that:
    - Contains navbar
    - Contains a heading
    - Contains image of the product
    - Contains informations about product
    - Contains quantity field
    - Contains total of the bag
    - Contains button to go to checkout
    - Contains keep shopping button
    - Contains footer 

    ![Bag Page](/static/media/documents/bag-page.png)

    - Acceptance Criteria:
        - Shopping Bag Page features a navbar so that the user can easily navigate trough the pages
        - Has a consistent theme and colour scheme
        - Have an image to see how the product look
        - Have informations about product so that the user know the name and price of the product
        - Have a quantity field so that the user can add or delete the quantity of the product
        - Have a grand total so that the user can see how much it will cost all the products in total
        - Have a checkout button so that the user can go for the next step to finish the order
        - Have a keep shopping button so that the user can return to all products if he want to see more


7. A Checkout Page that:
    - Contains navbar
    - Contains a heading
    - Contains a form 
    - Contains image of the product
    - Contains informations about product
    - Contains total of the bag
    - Contains complete order button 
    - Contains adjust bag button
    - Contains footer 

    ![Checkout Page](/static/media/documents/checkout-page.png)

    - Acceptance Criteria:
        -Checkout Bag Page features a navbar so that the user can easily navigate trough the pages
        - Has a consistent theme and colour scheme
        - Have an image to see how the product look
        - Have informations about product so that the user know the name and price of the product
        - Have a grand total so that the user can see how much it will cost all the products in total
        - Have a complete order button so that the user can finish the order
        - Have a adjust bag button so that the user can return to bag page if he want to change something in his order


8. A Success checkout Page that:
    - Contains navbar
    - Contains a heading
    - Contains informations about order
    - Contains keep shopping button
    - Contains footer 

    ![Success Checkout Page](/static/media/documents/checkout-success-page.png)

    - Acceptance Criteria:
        - Success Checkout Page features a navbar so that the user can easily navigate trough the pages
        - Has a consistent theme and colour scheme
        - Have informations about the order so that the user know informations about his order
        - Have a keep shopping button so that the user can return to all products if he want to see more


9. A Profile Page that:
    - Contains navbar
    - Contains a heading
    - Contains a form for users address
    - Contains button for updating informations
    - Contains saved orders of the user
    - Contains footer 

    ![Profile Page](/static/media/documents/profile-page.png)

    - Acceptance Criteria:
        - Profile Page features a navbar so that the user can easily navigate trough the pages
        - Has a consistent theme and colour scheme
        - Have informations about users address
        - Have a button for updating informations so that the user can update his address informations
        - Have all his orders saved with details so that the user know everything about his old orders

10. A Wishlist Page that:
    - Contains navbar
    - Contains a heading
    - Contains a paragraph
    - Contains all products added to wishlist
    - Contains footer 

    ![Wishlist Page](/static/media/documents/wishlist.png)

    - Acceptance Criteria:
        - Shopping Bag Page features a navbar so that the user can easily navigate trough the pages
        - Has a consistent theme and colour scheme
        - Have a title so that the user know on what page is
        - Have all saved products so that the user can see them and buy if wants
        - Have a paragraph where it writes how many products are in the wishlist

11. An Admin-only management page that:
    - is accessed through a superuser exclusive link
    - opens a page for admins to add new products

    ![Management Page](/static/media/documents/add-product.png)

    - Acceptance Criteria:
        - Superuser/Admin only access
        - Products can be added to the database from a form on the page

12. A custom error 404 page that:
    - will appear if the user looks for a page that doesn't exist
    - will encourage the user to return to the home page through a home page button clearly displayed

    ![Custom Error 404 Page](/static/media/documents/404-page.png)

---

# **5. Design**

Seline & Tam Jewelry's Site features neutral designs.
I use a lot of beige color and added white and black to it. 

`#f1eee9` is the main background colour you see on the site, followed by `#dfdad3` for the main nav bar.
The colors from the website is my personal choice I have looked on pinterest for colors combinations and I choose this colors based on the home page backgorund image. I have always liked neutral colors.

See the main colour palette below:

![Colour Palette](/static/media/documents/colors.png)

I have used a lot of standard Bootstrap colors as well for many buttons and toasts on the site. 
The usual Success Green, Warning Yellow, Primary Blue, Info Blue and Danger Red colours are implemented all across the site.
They give great visual feedback to users and so I think they are a fantastic out-of-the-box solution to add relevant colour quickly.

The structure of the site is based around 2 navigation menus. A top nav, where users access account or authentication related content and basket/checkout functionalities (+ the site logo, which also returns users to the home page), and a middle nav which serves as the main point of reference for the rest of the site. Both nav bars can be found on all pages.

A lot of the other content contains some form of bootstrap card type design, such as the products page and some pages with forms. I made use of 3 separate card-like containers in the basket page to house and separate different info, where I would ideally like users to focus on different info separate from each other. 

The main fonts across the website are ` 'Playfair Display', sans-serif; `

I used diamond icon as my favicon for the site:

![Favicon](/static/media/documents/favicon.png)
 
---

# **6. Facebook**

Seline & Tam Jewelry has a Facebook page, where users can follow and like the page, interact with posts to keep up to date with the latest news at Seline & Tam Jewelry store.

As a part of the business marketing strategy and a key foundation of any website's online marketing, a Facebook page provides the means to update users on a popular social media platform with the latest news relating to the business, store. 

In time, engagement will increase with followers gained and interactions through comments, reviews, likes and shares. 
It serves the site/business goals of growing the business and shining a positive light on motorsports and promoting motorsports in the UK.
The Facebook page will increase the reach of the business to new potential customers and engage with existing clients.


![Facebook page](/static/media/documents/facebook.png)

---

# **7. Future Implementations**

- Add a button to the detail product page for choosing the size of the jewelries the user need.
- Add a CUSTOMIZE button for the user to choose their own suitable size to make the order according to the size they want. By clicking the CUSTOMIZE button will appear as a popup form where the user can put his desired size or simply have a field where the user can write the desired size. 
- Add fotos in the login/register pages to attract the user. Below is an example of how I made in another project.

![Future implementation](/static/media/documents/future-implementation.png)

- Add more informations about products in detail product page
- Change the design of 404 error page
- Change the design of products card where the user will have one button for add to bag and two icons. One for wishlist and one eye icon to redirect user to detail product page. See example below from another project made by me.

![Future implementation- Cards](/static/media/documents/cards-future-implementation.gif)

---

# **8. Database Schema**


I used **DBeaver** to map out an ER Diagram for my Database Schema:

![DB Schema](/static/media/documents/dbeaver-1.png)
![DB Schema](/static/media/documents/dbaver-2.png)


---

# **8. Technologies Used**

Full list of technology implemented below:

- HTML
- CSS 
- Bootstrap - A styling framework used to speed up layout and styles. 
- Django Framework - Main, Python based framework on which this project is based.
- Python 3.8 - Version of Python installed on Gitpod
- Javascript 
- Stripe - APIs that handles the payments on the project
- AWS S3 - for storing static files such as media
- HEROKU - used to host my website
- Github - used to host the code from my repository
- VSCode - used to write and store code on a local machine
- ElephantSQL (Hosted my PostgreSQL database)
- PostgreSQL (RDBMS) - The Regional Database Management System used for the data/backend of the project
- Django Summernote - for styling the text boxes in the admin page with a WYSIWYG (what you see is what you get) editor.
- Django Crispy Forms - for neatly styling form layouts
- Pillow - A PIL (Python Imaging Library)
- GMail - for sending real email from gmail to users in production
- Mailchimp - also for sending real newsletters
- DBeaver - for importing data and mapping out ER diagrams from connected databases
- VEED.IO - for creating boomerang for README file
- UNSPLASH - for downloading HD images for this project

---

# **9. Python Packages Installed**


- asgiref==3.7.2
- boto3==1.34.88
- botocore==1.34.88
- dj-database-url==0.5.0
- Django==3.2.24
- django-allauth==0.41.0
- django-countries==7.2.1
- django-crispy-forms==1.14.0
- django-storages==1.14.2
- gunicorn==22.0.0
- jmespath==1.0.1
- oauthlib==3.2.2
- pillow==10.2.0
- psycopg2==2.9.9
- python3-openid==3.2.0
- pytz==2024.1
- requests-oauthlib==1.3.1
- s3transfer==0.10.1
- sqlparse==0.4.4
- stripe==9.0.0
- urllib3==1.26.18

---

# **10. The Mailchimp**

- [Mailchimp Site](https://mailchimp.com/)


### What is Mailchimp?
- For mailing purposes, we need to use for newsletters. 
- Mailchimp allows you to send emails. With Mailchimp, you also have the advantage of managing all your marketing channels, including email and SMS*, from one unified platform - **Definition from Mailchimp itself.**

### Why use Mailchimp?
- Mailchimp is a free mailing server.
- It provides 1,000 emails per month included in the free account.
- It's very easy to use and fast.
- It has a automations tool

### How does Mailchimp work?
- After creating an account, and following the documentation, Mailchimp provides an API key to use in our env.py file.
- We create email design and text. 
- Mailchimp is able to send automated emails to every new user. And if it's new user will be send automated email welcome message.

---

# **11. Testing**

# Manual Testing

This section of the documentation comprises of various manual tests and online validators to check the quality of my code and also to check the functionality of the project.

---

## Manual Testing

### Stripe

To test the checkout payments with card details in test mode, I used the following long card numbers:

- 4242424242424242: for successful card payments (Visa)

I used the above to successfully test Stripe and I am happy to say it is working as expected.

<br></br>

### Home/Index
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Logo/Home Link | Click on Logo at top of Page | Redirect to the home page | PASS |
| All Products Link | Click on middle nav link | Opens Products Page | PASS |
| Bracelet Link | Click on middle nav link  | Opens category bracelet Page | PASS |
| Necklaces Link | Click on middle nav link  | Opens category necklaces Page | PASS |
| Earings Link | Click on middle nav link  | Opens category earings Page | PASS |
| Rings Link | Click on middle nav link  | Opens category rings Page | PASS |
| Collections Click | Click on middle nav link | Opens dropdown with each collections links | PASS |
| My account Icon | Click on nav link | Opens dropdown with other links | PASS |
| Shopping bag Icon | Click on nav link | Opens Bag Page | PASS |
| Shop Now Button | Click on index main section button | Opens Products Page | PASS |

### Lisa Collection Section
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| See More Button | Click on index lisa Collection Section button | Redirect to the Lisa Collection page | PASS |

### Contact Section
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Send Message Button | Click on index Contact Section button | Redirect to the Contact page | PASS |

### Footer
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Media links | Click on link | Open blank page to the clicked link | PASS |

### Contact
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Submit Form | Attempt to submit blank form with nothing filled in | Form validation will prevent form from sending and alert user to which input needs filling in | PASS |
| Submit Form | Attempt to submit with just one input filled in  | Form validation will prevent form from sending and alert user to which input needs filling in | PASS |
| Email input | Try to enter an invalid email address or random numbers, words etc.  | Form will not send and user will be informed to enter a valid email address | PASS |
| Submit Valid Form | Submit a complete and valid contact form | Page redirects to  the same page and receive a success message | PASS |
| Admin Panel | Check output of submission in the Admin Panel | All filled out information should be strored correctly in the database | PASS |

### Profile
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Profile Link | Check appearance when logged out | Profile page is not accessible to users not logged in | PASS |
| Profile Link | Check appearance and click on link when logged in | User will be redirected to their profile page | PASS |
| Update Button | Click Update Button | The form will update and save | PASS |
| Input fields | Enter invalid inputs for fields | User will get an error message | PASS |
| Input fields | Enter Valid input for fields | User will be informed that it saved successfully | PASS |


### Authentication
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Sign Up | Create an account | You will be asked to wait until the admin will check your email and confirm it | PASS |
| Login | Login with a registered account | Redirected to homepage and informed you are logged in | PASS |
| Remember me checkbox | Click on remember me checkbox button before loggin in | You will not need to login next time you visit the site | PASS |
| Forgot Password | Click on Forget Password and submit email | Link to set new password sent to email address supplied by user | PASS |


### Basket and Bag
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Basket Icon | Click on Basket icon in top nav | Redirects to bag page | PASS |
| Basket Page with no items | Click on basket page with nothing in the basket | Item counter reads as 0 and user is informed that there are no items in the basket, summary is blank | PASS |
| Item in Basket | Add item to basket and check that it appears in the items table | Chosen product will appear in the basket | PASS |
| Multiple items in Basket | Add more than one item to the basket (both quantity and different products) | Quantities are implemented and counted and you are able to add all 3 different products to basket in any order | PASS |
| Delete Item in basket | Click 'Delete button | Item is deleted from the basket | PASS |
| Update Item in basket | Click 'Update' button | Item is updated from the basket | PASS |
| Summary total Calculator | Add items to basket, change quantities, delete items from basket | total will adjust accordingly | PASS |
| Summary VAT calculator | Add items to basket and check VAT calculation | 20% VAT applied automatically | PASS |
| Checkout Button (Basket Page) | Add item to basket and click on the checkout button in the basket page | redirect to the stripe checkout | PASS |
| Checkout validation | Attempt to submit checkout with inclomplete input fields | Checkout will not proceed until you have filled in all required fields | PASS |
| Checkout Success | Visit checkout, fill in required fields and click 'Complete Order' | On successfull payment, you are redirected to the success page | PASS |
| Checkout Fail | Attempt a failed checkout | Redirected to the same page, user is not charged, and receive erro message | PASS |
| Order History Added/Updated | Checkout and visit order history page | Order is added to order history table in profile page | PASS |

### Management
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Management Link | Login as Admin/Superuser and open profile dropdown | Management link visible and when clicked, redirect to the management add products page | PASS |
| Submit Form | Complete valid form and click "Add Product" | Product is added to list of products on the products page and superuser receive a success mesage | PASS |
| Image upload to AWS | On form submit, check new products detail | image on product detail is available due to automated image storage to AWS | PASS |
| Superuser Access only | Try to access url as a non-admin | Receive a message saying you are not allowed to view this page | PASS |
| Product list | Check Products list has new Product added post submission | new Product is visible with all data inputs added visible | PASS |
| Form validation | Attempt to add invalid entries or incomplete form and submit | Form validation prevents submission until correctly filled out | PASS |

### Product Cards
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Edit and Delete Buttons | Login as Admin/Superuser and open products page | Superuser can see edit and delete buttons for each product | PASS |
| Edit Button (Product Card) | Click on edit button | Superuser is redirected to edit page and receive an alert message | PASS |
| Delete Button | Click on edit button | Product is deleted after superuser confirms again that he want to delete | PASS |
| Wishlist | Click on wishlist button | Product is added to wishlist page and user receive a succes message | PASS |
| Product Card image | Click on product image | User/superuser is redirected to the detail product page | PASS |




### Other
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Order History Link | click on link in Nav | Opens user order history page | PASS |
| Order History Table | Make orders and view order history page | Orders will render in a table automatically and in chronological order | PASS |
| Stripe Receipt Link | Click receipt link in the table | Redirects to Stripe receipt | PASS |


---

## HTML Validation

All HTML validation was done using https://validator.w3.org/nu/


### /templates 

| File | Result |
| -------- | ------ |
| base.html | PASS |
| main-nav.html  | PASS |
| includes/base.html | PASS |
| includes/toast_error.html  | PASS |
| includes/toast_info.html  | PASS |
| includes/toast_success.html  | PASS |
| includes/toast_warning.html | PASS |

### /trackdays

| File | Result |
| -------- | ------ |
|  experience-detail.html | PASS |
|  experiences.html | PASS |
|  trackday-detail.html | PASS |
|  trackday-list.html | PASS |
|  trackday-request.html | PASS |
|  tuition-detail.html | PASS |
|  tuition.html | PASS |
|  includes/increment_decrement.html | PASS |

### /profiles

| File | Result |
| -------- | ------ |
| profile.html  | PASS |

### /home

| File | Result |
| -------- | ------ |
| about.html  | PASS |
| contact.html  | PASS |
| faqs.html  | PASS |
| index.html  | PASS |
| policies.html  | PASS |
| management.html  | PASS |
| error404.html | PASS |
| newsletter.html | PASS |

### /checkout

| File | Result |
| -------- | ------ |
| basket.html  | PASS |
| cancel.html | PASS |
| error.html | PASS |
| success.html | PASS |
| history.html | PASS |


### /cars

| File | Result |
| -------- | ------ |
| car-hire.html  | PASS |

<br/><br/> 

<details><summary> Main HTML Validation Screenshots</summary>

#### Base.html, Main-nav.html and  Index.html
![Base Template Validation](/static/images/readme-images/validation-images/base-index.html-val.png)

#### experience-detail.html
![Experience Detail Validation](/static/images/readme-images/validation-images/experience-detail.html-val.png)

#### experiences.html
![Experiences Validation](/static/images/readme-images/validation-images/experiences.html-val.png)

#### trackday-detail.html
![Trackday Detail Validation](/static/images/readme-images/validation-images/trackday-detail.html-val.png)

#### trackday-list.html
![Trackday List Validation](/static/images/readme-images/validation-images/trackday-list.html-val.png)

#### trackday-request.html
![Trackday Request Validation](/static/images//readme-images/validation-images/trackday-request.html-val.png)

#### tuition-detail.html
![Tuition Detail Validation](/static/images//readme-images/validation-images/tuition-detail.html-val.png)

#### tuition.html
![Tuition Validation](/static/images//readme-images/validation-images/tuition.html-val.png)

#### profile.html
![Profile Validation](/static/images//readme-images/validation-images/profile.html-val.png)

#### about.html
![About Validation](/static/images//readme-images/validation-images/about.html-val.png)

#### contact.html
![Contact Validation](/static/images//readme-images/validation-images/contact.html-val.png)

#### faqs.html 
![FAQS Validation](/static/images//readme-images/validation-images/faqs.html-val.png)


#### policies.html
![Policies Validation](/static/images//readme-images/validation-images/policies.html-val.png)

#### management.html
![Management Validation](/static/images//readme-images/validation-images/management.html-val.png)

#### error404.html
![Error 404 Validation](/static/images//readme-images/validation-images/error404-page-val.png)

#### newsletter.html
![Newsletter Validation](/static/images//readme-images/validation-images/newsletter.html-val.png)

#### basket.html
![Empty Basket Validation](/static/images//readme-images/validation-images/basket.html-empty-val.png)
![Full Basket Validation](/static/images//readme-images/validation-images/basket.html-with-items-val.png)

#### history.html
![Order History Validation](/static/images//readme-images/validation-images/history.html-val.png)

#### success.html
![Checkout Success Validation](/static/images//readme-images/validation-images/success.html-val.png)

#### cancel.html
![Cancel Checkout Validation](/static/images//readme-images/validation-images/cancel.html-val.png)

#### car-hire.html
![Car Hire Page Validation](/static/images//readme-images/validation-images/car-hire.html-val.png)


</details>

<br/><br/> 

### Current HTML Errors/Issues/Explanations:

- Mostly just warnings for script tags having the ` type="text/javascript" ` attribute in them. This can be ignored.

---

## CSS Validation

All CSS validation was done using https://jigsaw.w3.org/css-validator/

### /static/css

| File | Result |
| -------- | ------ |
| base.css  | PASS |


### /trackdays/css

| File | Result |
| -------- | ------ |
| booking-detail.css  | PASS  |
| exp_detail.css  | PASS  |
| experiences.css  | PASS  |
| trackday-request.css  | PASS  |
| trackdays.css  | PASS  |
| tuition.css  | PASS  |

### /profiles/css

| File | Result |
| -------- | ------ |
| profiles.css  | PASS |

### /home/css

| File | Result |
| -------- | ------ |
| about.css  | PASS |
| contact.css  | PASS |
| index.css  | PASS |
| management.css  | PASS |
| newsletter.css  | PASS |

### /basket/css

| File | Result |
| -------- | ------ |
| basket.css  | PASS |
| history.css  | PASS |

### cars/css

| File | Result |
| -------- | ------ |
| cars.css  | PASS |


<br/><br/> 

<details><summary>CSS Validation Screenshots</summary>

#### base.css
![Base CSS Validation](/static/images//readme-images/validation-images/base.css-val.png)

#### booking-detail.css
![Booking Detail CSS Validation](/static/images//readme-images/validation-images/booking-detail.css-val.png)

#### exp_detail.css
![Experience Detail CSS Validation](/static/images//readme-images/validation-images/exp_detail.css-val.png)

#### experiences.css
![Experiences CSS Validation](/static/images//readme-images/validation-images/experiences.css-val.png)

#### trackday-request.css
![Trackday Request CSS Validation](/static/images//readme-images/validation-images/trackday-request.css-val.png)

#### trackdays.css
![Trackdays CSS Validation](/static/images//readme-images/validation-images/trackdays.css-val.png)

#### tuition.css
![Tuition CSS Validation](/static/images//readme-images/validation-images/tuition.css-val.png)

#### profiles.css
![Profiles CSS Validation](/static/images//readme-images/validation-images/profiles.css-val.png)

#### about.css 
![About CSS Validation](/static/images//readme-images/validation-images/about.css-val.png)

#### contact.css
![Contact CSS Validation](/static/images//readme-images/validation-images/contact.css-val.png)

#### index.css 
![Index CSS Validation](/static/images//readme-images/validation-images/index.css-val.png)

#### management.css
![Management CSS Validation](/static/images//readme-images/validation-images/management.css-val.png)

#### newsletter.css
![Newsletter CSS Validation](/static/images//readme-images/validation-images/newsletter.css-val.png)

#### basket.css 
![Basket CSS Validation](/static/images//readme-images/validation-images/basket.css-val.png)

#### history.css
![History CSS Validation](/static/images//readme-images/validation-images/history.css-val.png)

#### cars.css
![Cars CSS Validation](/static/images//readme-images/validation-images/cars.css-val.png)

</details>

<br/><br/> 

### Current CSS Errors/Issues/Explanations:

- No issues at all to report.

---

## JS Validation

I cross-referenced JS Validation using two different Validation services:
- https://jshint.com/
- https://jsvalidator.com/

I did find this particularly useful as some files generated warnings on one validator (perhaps due to over-sensitivity) and passed with zero errors on another.
I have included different screenshots to demonstrate this and show that the JS is valid and working.


### profiles/js

| File | Result |
| -------- | ------ |
| profile.js | PASS |

### home/js

| File | Result |
| -------- | ------ |
| base.js  | PASS |

<br/><br/> 

<details><summary>JS Validation Screenshots</summary>

#### profile.js
![Profile Page JS](/static/images/readme-images/validation-images/profiles.js-val.png)

#### base.js
![Base JS](/static/images//readme-images/validation-images/base.js-val.png)
![Base JS](/static/images//readme-images/validation-images/base.js-js-val.png)

#### increment-decrement js
![Increment and Decrement JS](/static/images/readme-images/validation-images/increment-decrement-script-js-val.png)

#### basket js
![Basket JS](/static/images/readme-images/validation-images/basket-js-script-val.png)

#### Management js
![Management JS](/static/images/readme-images/validation-images/management-js-script-val.png)

#### Trackday Detail js
![Trackday Detail JS](/static/images/readme-images/validation-images/trackday-detail-js-script-val.png)

#### Bootstrap Toast js
![Bootstrap Toast JS](/static/images/readme-images/validation-images/bootstrap-toasts-js-val.png)
![Bootstrao Toast JS](/static/images/readme-images/validation-images/bootstrap-toasts-js-js-val.png)

Extra JS in includes/toasts html files:
![Extra JS](/static/images/readme-images/validation-images/extra-toast-js.png)


</details>

<br/><br/> 

### Current JS Errors/Issues/Explanations:

- As you can see from the screen shots, the same code on one js linter can be more sensitive towards things than others. I have included cases like this above for transparency and to prove I have tested across more than one JS linter.


---

## Python Validation

All Python validation was checked through Code Institute's PEP8 Python Linter. You can find it via this link: https://pep8ci.herokuapp.com/

### /django_raceway


| File | Result |
| -------- | ------ |
| settings.py | PASS |
| urls.py | PASS |


### /trackdays

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS |
| tests.py | PASS |



### /profiles

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS |
| tests.py | PASS |



### /home

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS |



### /checkout

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| contexts.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS* |
| helpers.py | PASS |
| tests.py | PASS |

* Line 313 in views.py reads as too long, however, for reliability I have opted to leave this
in as it can cause issues in deployment when concatenated as it is an image url. I believe this is
a sensible and reasonable precaution to take for site reliability in conjunction with stripe.
See further explanation below.


### /cars

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS |
| tests.py | PASS |

<br/><br/> 

<details><summary>Python Validation Screenshots</summary>

#### /django_raceway

![settings.py](/static/images/readme-images/validation-images/django_raceway-settings.py-val.png)
![urls.py](/static/images/readme-images/validation-images/django_raceway-urls.py-val.png)


#### /trackdays

![admin.py](/static/images/readme-images/validation-images/trackdays-admin.py-val.png)
![models.py](/static/images/readme-images/validation-images/trackdays-models.py-val.png)
![urls.py](/static/images/readme-images/validation-images/trackdays-urls.py-val.png)
![views.py](/static/images/readme-images/validation-images/trackdays-views.py-val.png)


#### /home

![admin.py](/static/images/readme-images/validation-images/home-admin.py-val.png)
![models.py](/static/images/readme-images/validation-images/home-models.py-val.png)
![urls.py](/static/images/readme-images/validation-images/home-urls.py-val.png)
![views.py](/static/images/readme-images/validation-images/home-views.py-val.png)


#### /profiles

![admin.py](/static/images/readme-images/validation-images/profiles-admin.py-val.png)
![models.py](/static/images/readme-images/validation-images/profiles-models.py-val.png)
![urls.py](/static/images/readme-images/validation-images/profiles-urls.py-val.png)
![views.py](/static/images/readme-images/validation-images/profiles-views.py-val.png)

#### /checkout

![admin.py](/static/images/readme-images/validation-images/checkout-admin.py-val.png)
![models.py](/static/images/readme-images/validation-images/checkout-models.py-val.png)
![urls.py](/static/images/readme-images/validation-images/checkout-urls.py-val.png)
![views.py](/static/images/readme-images/validation-images/checkout-views.py-val.png)
![views.py 2](/static/images/readme-images/validation-images/checkout-views.py-line-too-long.png)
![contexts.py](/static/images/readme-images/validation-images/checkout-contexts.py-val.png)
![helpers.py](/static/images/readme-images/validation-images/checkout-helpers.py-val.png)


#### /cars

![admin.py](/static/images/readme-images/validation-images)
![models.py](/static/images/readme-images/validation-images)
![urls.py](/static/images/readme-images/validation-images)
![views.py](/static/images/readme-images/validation-images)
![tests.py](/static/images/readme-images/validation-images)


</details>

<br/><br/> 

### Current Python Errors/Issues/Explanations:

- Only 1 known python linting issue across the entire workspace, being that of line 313 in /checkout/views.py where a line is too long.
Due to this being a url, and a pretty specific one from Stripe as well, I opted to follow best practice and to leave it as is for this one exception in order 
to ensure reliability of the checkout on the site. I believe reliability takes priority over anything else.
I am very much following [this Principal](https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds)


---

## Lighthouse Performance Testing

- Lighthouse Testing was performed in an incognito tab to ensure no external chrome add-ons were affecting the test.
- I did the test 3 times to see how consistent the tests were.
- Results of the Lighthouse Performance testing below:

**Test 1**
![Test 1](/static/images/readme-images/validation-images/lighthouse-testing.png)
**Test 2**
![Test 2](/static/images/readme-images/validation-images/lighthouse-testing-2.png)
**Test 3**
![Test 3](/static/images/readme-images/validation-images/lighthouse-testing-3.png)

- As you can see, there is quite a bit of variation in the test results. However, taking an average of the scores from the 3 tests, I am fairly happy with the performance of the site overall.

---

## Device and Browser Testing

- Browsers Tested:
    - Google Chrome
    - Safari

- Devices Tested:
    - MacBook Pro
    - Apple iPhone 12 Pro
    - iPhone 14 Pro
    - iPhone X
    - iPad Pro



### Responsiveness

- The site has been tested down to screen widths of 320px and up to screen widths of 2560px
- The site is fully responsive between these viewport widths

---


## Current known and unresolved issues

- As documented in the outstanding bugs section in the readme, there is an (as of writing) unresolved bug where when you sign in or log out, the sign in and log out buttons can appear to not be clickable. This is always able to be fixed by either refreshing the page or clicking on to another link/page. Alternatively, click on the site logo (which redirects to the home page anyway) to clear this bug. This may not happen to you at all or it may happen to you randomly.
- My Trackday Constraint in my Trackday model appears to not work realiably. I have tried various combinations of the code, tried to reformat it countless times and tried to use it in conjunction with adding ` unique=True` in the fields that are supposed to work with it. I have yet to resolve this issue and will aim to do so in a future update.
- If you visit the site too often, you may find you need to hard refresh or clear the cache on some pages, especially the checkout page I find. This can be avoided entirely by using an incognito tab in your browser.


--- 

[Return to Top](#manual-and-automated-testing)








    