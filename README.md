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

- [***Seline & Tam Jewelry - Portfolio Project 5 Ecommerce***](#---seline---tam-jewelry---portfolio-project-5-ecommerce---)
- [**1. Key project information**](#--1-key-project-information--)
- [**2. Table of Contents**](#--2-table-of-contents--)
- [**3. Wireframes and Planning**](#--3-wireframes-and-planning--)
    + [Canva wireframes/mockups](#canva-wireframes-mockups)
    + [Desktop](#desktop)
      - [Home](#home)
      - [Clock](#clock)
      - [Collection](#collection)
      - [Promise](#promise)
      - [Contact](#contact)
      - [Products](#products)
      - [Product Detail](#product-detail)
      - [Shopping Bag](#shopping-bag)
      - [Checkout](#checkout)
      - [Profile](#profile)
    + [Early Development](#early-development)
- [**4. User Experience (UX)**](#--4-user-experience--ux---)
    + [The Idea](#the-idea)
    + [The Ideal User](#the-ideal-user)
    + [Site Goals](#site-goals)
    + [SEO and Web Marketing](#seo-and-web-marketing)
    + [Keywords and sitemap/robots](#keywords-and-sitemap-robots)
    + [Agile Methodologies](#agile-methodologies)
    + [User stories](#user-stories)
    + [Epics](#epics)
- [**5. Features**](#--5-features--)
- [**5. Design**](#--5-design--)
- [**6. Facebook**](#--6-facebook--)
- [**7. Future Implementations**](#--7-future-implementations--)
- [**8. Database Schema**](#--8-database-schema--)
- [**8. Technologies Used**](#--8-technologies-used--)
- [**9. Python Packages Installed**](#--9-python-packages-installed--)
- [**10. The Mailchimp**](#--10-the-mailchimp--)
    + [What is Mailchimp?](#what-is-mailchimp-)
    + [Why use Mailchimp?](#why-use-mailchimp-)
    + [How does Mailchimp work?](#how-does-mailchimp-work-)
- [**11. Testing**](#--11-testing--)
  * [Manual Testing](#manual-testing)
    + [Stripe](#stripe)
    + [Home/Index](#home-index)
    + [Lisa Collection Section](#lisa-collection-section)
    + [Contact Section](#contact-section)
    + [Footer](#footer)
    + [Contact](#contact-1)
    + [Profile](#profile-1)
    + [Authentication](#authentication)
    + [Basket and Bag](#basket-and-bag)
    + [Management](#management)
    + [Product Cards](#product-cards)
    + [Product Detail](#product-detail-1)
    + [Wishlist](#wishlist)
  * [HTML Validation](#html-validation)
    + [/templates](#-templates)
    + [/home](#-home)
    + [/products](#-products)
    + [/profiles](#-profiles)
    + [/shpbag](#-shpbag)
    + [/checkout](#-checkout)
      - [Base.html, Main-nav.html, Index.html](#basehtml--main-navhtml--indexhtml)
      - [products.html](#productshtml)
      - [detail_product.html](#detail-producthtml)
      - [profile.html](#profilehtml)
      - [wishlist.html](#wishlisthtml)
      - [bag.html](#baghtml)
      - [checkout.html](#checkouthtml)
      - [contact.html](#contacthtml)
    + [Current HTML Errors/Issues/Explanations:](#current-html-errors-issues-explanations-)
  * [CSS Validation](#css-validation)
    + [/static/css](#-static-css)
      - [style.css](#stylecss)
      - [profile.css](#profilecss)
    + [Current CSS Errors/Issues/Explanations:](#current-css-errors-issues-explanations-)
  * [JS Validation](#js-validation)
    + [clock/js](#clock-js)
    + [cards/js](#cards-js)
    + [stripe/js](#stripe-js)
      - [clock.js](#clockjs)
      - [cards.js](#cardsjs)
      - [stripe_elements.js](#stripe-elementsjs)
      - [increment-decrement js](#increment-decrement-js)
    + [Current JS Errors/Issues/Explanations:](#current-js-errors-issues-explanations-)
    + [Current JS Errors/Issues/Explanations:](#current-js-errors-issues-explanations--1)
  * [Python Validation](#python-validation)
    + [/jewelry](#-jewelry)
    + [/home](#-home-1)
    + [/products](#-products-1)
    + [/profiles](#-profiles-1)
    + [/shpbag](#-shpbag-1)
    + [/usercheckout](#-usercheckout)
      - [/jewelry](#-jewelry-1)
      - [/home](#-home-2)
      - [/products](#-products-2)
      - [/profiles](#-profiles-2)
      - [/shpbag](#-shpbag-2)
      - [/usercheckout](#-usercheckout-1)
    + [Current Python Errors/Issues/Explanations:](#current-python-errors-issues-explanations-)
  * [Lighthouse Performance Testing](#lighthouse-performance-testing)
  * [Browser Testing](#browser-testing)
    + [Responsiveness](#responsiveness)
  * [Bugs and Issues](#bugs-and-issues)
    + [Current Unresolved Bugs](#current-unresolved-bugs)
- [**12. Deployment**](#--12-deployment--)
    + [Pre-flight checks before starting:](#pre-flight-checks-before-starting-)
    + [Version Control:](#version-control-)
    + [Forking a Github Repository:](#forking-a-github-repository-)
    + [Locally Cloning a Github Repository:](#locally-cloning-a-github-repository-)
      - [Github docs:](#github-docs-)
    + [Deployment through Heroku:](#deployment-through-heroku-)
- [**13. Peer Reviews**](#--13-peer-reviews--)
- [**14. Credits**](#--14-credits--)
    + [Code Help:](#code-help-)
  * [Personal Credits](#personal-credits)
  * [Media/Images:](#media-images-)
- [**15. Final Thoughts**](#--15-final-thoughts--)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

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

### The Idea
- The intention of **Seline & Tam Jewelry** site is to be friendly online shop where users can browse variate of products sorted between categories. Besides that, user can read details of each product, see product reviews and comments.

### The Ideal User

The target audience are individuals who are seeking luxury jewelry. Those who want to make gifts or to wear a luxury jewelry for themselves.

- Ideal user likes to shop online
- Ideal user likes to explore new trends and ideas in the jewelry field
- Ideal user likes to share their opinion in form of **reviews** and **comments**

### Site Goals

- Offer users ability of shopping online without leaving their home
- Offer users ability of reading other people comments on products
- Offer users ability to add items to their **Wishlist** if they want to save the item for later
- Offer users the ability to see details of each item in shop ( price, description, collection etc. ) 
- Provide site visitors with an easy to navigate site to view jewelry products

### SEO and Web Marketing

**Who:** I am marketing predominantly towards a jeweler-enthuasiast.
**What:** I am selling jewelry, designed to cater towards this audience. I therefore make it very accessible and clear on my site, so that the audience can go directly towards what they are looking for. I include images of jewelry, designed to excite the site viewer into wondering what it's like to wear them with some sophisticated clothes. It was equally important to make clear titles and key pieces of information available for the site viewers to see on which ever respective page/product they are viewing.
**How:** Based on my B2C model, I decided single payments with Stripe were the best payment option for the products I'm offering. I can update users on new products and general news through an opt-in mailchimp newsletter subscription and I have created a Facebook page which users/clients can view and follow to keep up to date through a social network.


Software developers play a role in making sure their website can be easily found through search engines, including the reviews of Google Search.
Therefore, when implementing SEO (Search Engine Optimisation) tools, the best means available to you are through descriptive and relevant keywords, sitemaps.xml and robots.txt files.

### Keywords and sitemap/robots

- I included keywords and more tags in my base.html document. This allowed me to define keywords, an author, a site description and a viewport. For the keywords themselves I thought about short and longer words and phrases respectively that might be looked for. 

- I started with fairly obvious short words including: jewelry, gold jewelry, gold bracelet, gold necklace,gold rings,gold earings, luxury jewelry.

- I then expanded in to short phrases, including: golden luxury jewelry

- I have included a sitemap.xml file in the root directory, which allows search engines to crawl through my site and make content more discoverable.

- I have a robots.txt file which provides the location of the sitemap and also defines any folders/files which are prohibited from search engine crawlers.

### Agile Methodologies

To plan tasks to implement for my website, I used Github Projects, which is a Kanban style board to track your project progress. You can track user stories, epics, ideas, to-do items and you can all see what tasks have been completed.

You can see my project board [here](https://github.com/users/SarahGrozav1/projects/8)

### User stories

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


### Epics

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

# **9. Technologies Used**

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

# **10. Python Packages Installed**


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

# **11. The Mailchimp**

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

# **12. Testing**

## Manual Testing

This section of the documentation comprises of various manual tests and online validators to check the quality of my code and also to check the functionality of the project.

---

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

### Product Detail
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Edit and Delete Buttons | Login as Admin/Superuser and open products page | Superuser can see edit and delete buttons for each product | PASS |
| Edit Button (Product Card) | Click on edit button | Superuser is redirected to edit page and receive an alert message | PASS |
| Delete Button | Click on edit button | Product is deleted after superuser confirms again that he want to delete | PASS |
| Wishlist | Click on wishlist button | Product is added to wishlist page and user receive a succes message | PASS |
| Quantity | Click on + or - | Quantity increase or decrease | PASS |
| Keep Shopping button | Click on Keep Shopping button | Redirect to the products page | PASS |
| Add to Bag button | Click on Add to Bag button | Success message with Product added to bag | PASS |
| Add Review | Click on stars and write a subject | Review saved and user can see it in the right side | PASS |
| Edit Review Button | Click on edit button | Redirected to the edit review page | PASS |
| Delete Review Button | Click on delete button | Review deleted | PASS |
| Edit Review Page | Edit the review and click on edit review button | Redirected to the detail product with a success message page | PASS |


### Wishlist 
| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Wishlist Page | The user can see products added to wishlist  | PASS |
| Trash Icon Button | Click on Trash Icon Button | Product will be removed from wishlist page | PASS |
| Card Image | Click on Image | The user will be redirected to the detail product page | PASS |


---

## HTML Validation

All HTML validation was done using https://validator.w3.org/nu/

### /templates 

| File | Result |
| -------- | ------ |
| base.html | PASS |
| main-nav.html  | PASS |
| mobile-top-header.html  | PASS |
| includes/toast_error.html  | PASS |
| includes/toast_info.html  | PASS |
| includes/toast_success.html  | PASS |
| includes/toast_warning.html | PASS |
| 404.html | PASS |

### /home

| File | Result |
| -------- | ------ |
| index.html | PASS |
| contact.html | PASS |

### /products

| File | Result |
| -------- | ------ |
|  add_product.html | PASS |
|  detail_product.html | PASS |
|  edit_product.html | PASS |
|  editreview.html | PASS |
|  products.html | PASS |
|  wishlist.html | PASS |
|  custom_clearable_file_inputquantity_script.html | PASS |
|  includes/increment_decrement.html | PASS |

### /profiles

| File | Result |
| -------- | ------ |
| profile.html  | PASS |

### /shpbag

| File | Result |
| -------- | ------ |
| bag-total.html  | PASS |
| bag.html  | PASS |
| checkout-buttons.html  | PASS |
| product-image.html  | PASS |
| product-info.html  | PASS |
| quantity-form.html  | PASS |

### /checkout

| File | Result |
| -------- | ------ |
| checkout_success.html  | PASS |
| checkout.html | PASS |


<br/><br/> 

<details><summary> Main HTML Validation Screenshots</summary>

#### Base.html, Main-nav.html, Index.html
![Base Template Validation]()

#### products.html
![Products Template Validation]()

#### detail_product.html
![Detail Product Template Validation]()

#### profile.html
![Profile Template Validation]()

#### wishlist.html
![Wishlist Template Validation]()

#### bag.html
![Bag Template Validation]()

#### checkout.html
![Checkout Template Validation]()

#### contact.html
![Contact Template Validation]()

</details>

<br/><br/> 

### Current HTML Errors/Issues/Explanations:

- Mostly just warnings for script tags having the ` type="text/javascript" ` attribute in them. This can be ignored.

---

## CSS Validation

CSS validation was done using https://jigsaw.w3.org/css-validator/

### /static/css

| File | Result |
| -------- | ------ |
| style.css  | PASS |

<details><summary>CSS Validation Screenshots</summary>

#### style.css
![Base CSS Validation](/static/media/documents/css-val.png)

#### profile.css
![Profile CSS Validation](/static/media/documents/profile-css-val.png)

</details>


### Current CSS Errors/Issues/Explanations:

- No issues at all to report.
<br/><br/> 

---

## JS Validation

I cross-referenced JS Validation using two different Validation services:
- https://jshint.com/
- https://jsvalidator.com/

I did find this particularly useful as some files generated warnings on one validator (perhaps due to over-sensitivity) and passed with zero errors on another.


### clock/js

| File | Result |
| -------- | ------ |
| clock.js | PASS |

### cards/js

| File | Result |
| -------- | ------ |
| cards.js  | PASS |

### stripe/js

| File | Result |
| -------- | ------ |
| stripe_elements.js  | PASS |

<br/><br/> 

<details><summary>JS Validation Screenshots</summary>

#### clock.js
![Clock JS](/static/media/documents/clock-js.png)

#### cards.js
![Cards JS](/static/media/documents/cards-js.png)

#### stripe_elements.js
![Stripe JS](/static/media/documents/stripe-val.png)
- With error
![Stripe JS](/static/media/documents/stripe-val-error.png)

#### increment-decrement js
![Increment and Decrement JS](/static/media/documents/increment-decrement-val.png)
- With error
![Increment and Decrement JS](/static/media/documents/increment-decrement-val-error.png)

### Current JS Errors/Issues/Explanations:

- As you can see from the screen shots, the same code on one js linter can be more sensitive towards things than others. I have included cases like this above for transparency and to prove I have tested across more than one JS linter.

---

</details>

<br/><br/> 

### Current JS Errors/Issues/Explanations:

- As you can see from the screen shots, the same code on one js linter can be more sensitive towards things than others. I have included cases like this above for transparency and to prove I have tested across more than one JS linter.


---

## Python Validation

All Python validation was checked through Code Institute's PEP8 Python Linter. You can find it via this link: https://pep8ci.herokuapp.com/

### /jewelry

| File | Result |
| -------- | ------ |
| settings.py | PASS |
| urls.py | PASS |


### /home

| File | Result |
| -------- | ------ |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS |

### /products

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| forms.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS |


### /profiles

| File | Result |
| -------- | ------ |
| forms.py | PASS |
| models.py | PASS |
| urls.py | PASS |
| views.py | PASS |

### /shpbag

| File | Result |
| -------- | ------ |
| apps.py | PASS |
| bag-items.py | PASS |
| contexts.py | PASS |
| urls.py | PASS |
| views.py | PASS |


### /usercheckout

| File | Result |
| -------- | ------ |
| admin.py | PASS |
| apps.py | PASS |
| forms.py | PASS |
| models.py | PASS |
| signals.py | PASS |
| urls.py | PASS |
| views.py | PASS* |
| webhook_handler.py | PASS* |
| webhooks.py | PASS* |



* Line 313 in views.py reads as too long, however, for reliability I have opted to leave this
in as it can cause issues in deployment when concatenated as it is an image url. I believe this is
a sensible and reasonable precaution to take for site reliability in conjunction with stripe.
See further explanation below.

<br/><br/> 

<details><summary>Python Validation Screenshots</summary>

#### /jewelry

![settings.py](/static/media/documents/settings-val.png)
![urls.py](/static/media/documents/settings-url-val.png)


#### /home

![models.py](/static/media/documents/home-models.png)
![urls.py](/static/media/documents/home-urls.png)
![views.py](/static/media/documents/home-views.png)


#### /products

![admin.py](/static/media/documents/products-admin.png)
![forms.py](/static/media/documents/products-form.png)
![models.py](/static/media/documents/products-models.png)
![urls.py](/static/media/documents/products-urls.png)
![views.py](/static/media/documents/products-views.png)
![widgets.py](/static/media/documents/products-widget.png)


#### /profiles

![forms.py](/static/media/documents/profiles-forms.png)
![models.py](/static/media/documents/profiles-models.png)
![urls.py](/static/media/documents/profiles-urls.png)
![views.py](/static/media/documents/profiles-views.png)


#### /shpbag

![apps.py](/static/media/documents/shpbag-apps.png)
![bag-items.py](/static/media/documents/shpbag-bag-items.png)
![contexts.py](/static/media/documents/shpbag-context.png)
![urls.py](/static/media/documents/shpbag-urls.png)
![views.py](/static/media/documents/shpbag-views.png)


#### /usercheckout

![admin.py](/static/media/documents/usercheckout-admin.png)
![apps.py](/static/media/documents/usercheckout-apps.png)
![forms.py](/static/media/documents/usercheckout-forms.png)
![models.py](/static/media/documents/usercheckout-mdoels.png)
![signals.py 2](/static/media/documents/usercheckout-signals.png)
![urls.py](/static/media/documents/usercheckout-urls.png)
![views.py](/static/media/documents/usercheckout-views.png)
![webhook_handler.py](/static/media/documents/usercheckout-webhook-handler.png)
![webhooks.py](/static/media/documents/usercheckout-webhooks.png)


</details>

<br/><br/> 

### Current Python Errors/Issues/Explanations:

In the urls, I opted to follow best practice and to leave it as is for this one exception in order to ensure reliability of the checkout on the site. I believe reliability takes priority over anything else.
I am very much following [this Principal](https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds)


---

## Lighthouse Performance Testing

- Lighthouse Testing was performed in an incognito tab to ensure no external chrome add-ons were affecting the test.
- Results of the Lighthouse Performance testing below:

**Test 1**
![Test 1](/static/media/documents/lighhouse.png)

- As you can see, the results of performance are only 70 because of the images. However, I am fairly happy with the performance of the site overall.

---

## Browser Testing

- Browsers Tested:
    - Google Chrome


### Responsiveness

- The site has been tested down to screen widths of 320px and up to screen widths of 2560px
- The site is fully responsive between these viewport widths

---

## Bugs and Issues

- I haved some design issue in wishlist page the cards didn't align how I wanted

- In the detail product page the reviews was one on top of another and not one under another how I wanted

- I haved some problems with images when i uploaded them in AWS Amazon , the images didn't want to appear in products page and detail product page my website

- My order didn't want to save

- Checkout Success page didn't work 

### Current Unresolved Bugs

- Sometimes you may need to clear your cache to access frequently visited pages, especially the checkout page, I have found.
This can be mitigated entirely by using an incognito tab in your browser.

---

# **13. Deployment**

### Pre-flight checks before starting:
- Please make sure you have **all** of the following before beginning with the below steps:
    - A **Github** account and configure either Gitpod or VSCode (Or both)
    - A **Heroku** account
    - An **AWS** account
    - A **Stripe** account
    - An **ElephantSQL** account
    - A **Mailchimp Account**
    - Another Email Account, such as GMail

### Version Control:

- Version control was done through the Gitpod in VSCode, using the following key commands to push updated code to Github:
    - `git add ,` - to add all new files or file changes in preparation to commit in next step.
    - `git commit -m ""` - add your commit message inbetween the two quoatation marks, this explains the changes of your lastest version.
    - `git push` - this is the command that pushed your code up to your github repository.

### Forking a Github Repository:

- Instructions for forking a respositoty:
    - To fork a chosen repository, look towards the top right of the page, between the watch/unwatch tab and the star tab, and select the "Fork" tab.
    - By default, forks are named the same as the parent repository, however, you can change this as you see fit. You are also able to add an optional description.
    - Choose which branch you want to copy if you need to. Only the default branch is copied by default setting.
    - Click the green "Create Fork" button, and you will now have a forked repository to use.

### Locally Cloning a Github Repository:

- Instructions for cloning a repository:
    - To clone a repository, first you will need to select your chosen repository and look for the green "Code" button (located next to the "Go to file" and "Add file" buttons).
    - Next, copy the URL for the repository. By default this is a HTTPS link, however, you can copy an SSH key or by using the Github CLI.
    - After you have the URL, you are going to want to go to the terminal of your machine and cd (change directory) to the folder where you want to save your working directory to be.
    - In the terminal, type `git clone` followed by the url link you copied earlier.
    - Press enter and hopfully you will have successfully cloned the repository locally.
    - You will also need to make sure you have installed all the required packaged of the project. To do this, paste this code in to the terminal once your workspace is set up: `pip install -r requirements.txt`
    - You will also need to make an env.py file to run the project. Populate it with the required information, though make sure you include this file in the .gitignore file. The contents of the env.py file should NOT be made public.


#### Github docs:
- For further reading, I would highly suggest the Github Docs: [Github Docs Link](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

### Deployment through Heroku:

- Make sure you have a Heroku account before beginning with these steps.
- You should also make sure you have an AWS account with S3, and a Stripe Account for payments. These should then be configured for your project.

- Once logged in to Heroku, navigate to the personal dashboard and look for the 'New' dropdown button at top right hand corner of the page.
- In the drop down, select "Create new app - you will be taken to a page where you will be able to name the app and select a region. Once you have filled this information in, click the "Create app" button. Your app is now created.
- To pair an ElephantSQL (PostgreSQL) Database to your project, as I did to mine, see steps for this in the next section below. Alternatively, you can use a Heroku Postgres database.
- Next, you should navigate to the Settings tab to set up the config vars. Scroll down slightly to the button that reads "Reveal Config Vars" and click it to open it. We are going to need to add/remove the following information: 
    - DATABASE_URL: this should have been automatically generated by Heroku for you, but make sure it is populated already.
    If you are using another service such as ElephantSQL, simply place that database url in here instead. Click add.
    - USE_AWS: should be set to True. Click add.
    - AWS_ACCESS_KEY_ID: should be set to your AWS access key, click add.
    - AWS_SECRET_ACCESS_KEY: should be set to your AWS secret key, click add.
    - EMAIL_HOST_PASS: In conjuntion with whichever email app provider you use. In my case, GMail and they provide you with a unique pass code to enter in to your config. Click add.
    - SEND_GRID_API: Should be set to your SendGrid API Key. Click add.
    - EMAIL_HOST_USER: this will be your email address. Click add.
    - SECRET_KEY: This should be a secret password, do not publish this anywhere. Click add.
    - STRIPE_SECRET_KEY: Set to your Stripe Secret Key. Click add.
    - STRIPE_PUBLISHABLE_KEY: Set to your Stripe Publishable key. Click add.
    - API_KEY: insert your stripe api key here. Click add.
    - DISABLE_COLLECTSTATIC: Should have been set to 1 during development. You will REMOVE this for full deployment. Click the 'x' to remove it. However, if you set up a dynamic DEBUG variable in settings.py, like so: `DEBUG = 'DEVELOPMENT' in os.environ`, you can remove it earlier.

- After this, head to the Deploy tab and scroll down to the Deployment Method section and select "Github"
- Next, in the "App connected to GitHub" section, look up your account and repo to pair it to the heroku app (click connect).
- Head to the bottom of the page where you will see a section called "Manual Deploy". Select the 'main' branch in the drop down and click the 'Deploy Branch' button.
- Wait for the deployment to complete, and when prompted, click the "View/Open App" button to see the launched site.

---

# **14. Peer Reviews**

- The site has been shared with friends and family to get feedback and constructive criticism. 
- I have also had my project reviewed by my course mentor in 3 stages of the development cycle. 

---

# **15. Credits**

### Code Help:

The preliminary set up and an assisting walkthrough came in the form of following Code Institute's Boutique Ado walkthrough e-commerce project. Repository can be found here: [Boutique Ado - Code Institute](https://github.com/Code-Institute-Solutions/boutique_ado_v1)

I used the Bootstrap 4 framework. 
The following from the documentation helped me:
- Navigation:
    - [Bootstrap Navbar docs](https://getbootstrap.com/docs/4.0/components/navbar/)
- Cards: 
    - [Bootstrap Cards](https://getbootstrap.com/docs/4.0/components/card/)


For general Bootstrap tips and information, I frequently referred to the [GetBootstrap](https://getbootstrap.com/) documentation, the [mdbootstrap](https://mdbootstrap.com/docs/) documentation and the [W3Schools](https://www.w3schools.com/bootstrap5/index.php) bootstrap documentation.

Favicons were generated on [Favicon.io](https://favicon.io) - I choosed one icon from there.

I made use of Icons from [Font Awesome](https://fontawesome.com/) using their free student plan. 
All icons used in this project have come from here.

Some of the logic for my increment/decrement buttons on the track day detail page were inspired by answers from this stackoverflow thread: [Stackoverflow js +/-](https://stackoverflow.com/questions/9186346/javascript-onclick-increment-number)

Very useful tips and instructions for reseting DB migrations and faking initial migrations to prevent issues: [Simpleisbetterthancomplex migrations reset](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)

I have used shape dividers in my project from here: [Shape Divider](https://www.shapedivider.app/)

I used this very helpful guide for importing the data from my ElephantSQL database into DBeaver to map out my database Schema: [Amis Technology Blog](https://technology.amis.nl/database/quick-start-with-free-managed-postgresql-database-on-elephantsql/)

I generated my sitemap.xml using the steps from Boutique Ado Project from [this site](http://www.check-domains.com/sitemap/index.php)

I generated my robots.txt file using the steps from Boutique Ado Project from [this site](https://www.seoptimer.com/robots-txt-generator)
    
## Personal Credits

- Many Thanks to my C.I Mentor Daisy McGirr, who has been guiding me and advising me through this project as well as all projects since PP2 - Her input in our mentor sessions has been instrumental in getting me this far and so I have to say I massive thank you to her for that!

- Thanks to Matt Boden, who has guided me and explained me about database and how it works.

- Tutor support - helped me work out an issue with my AWS configuration where I was stuck and sat in front of my screen for over 3 hours! They are so patient, understanding and methodical and they also helped me to debug an issue I was having with my database.

- I would like to thank to my husband and family for their support through all this course, without them I couldn't be here.

## Media/Images:

I have downloaded my images from [Unsplash](https://unsplash.com/).
I used Canva for designing my project and there I have made a color pallete. The colors are from the home background image.

---

# **16. Final Thoughts**

This is my fifth and final project with Code Institute. A Full-Stack E-commerce jewelry business, selling jewelries and developed using the Django Framework, AWS, Heroku and Stripe. Written with HTML, CSS, Python and Javascript (JQuery).

This marks the end of a year long journey with C.I, from someone with zero background in software development to someone who has created a Github portfolio of 5 graded projects to proudly display the development in my own learning and new-found abilities. 

I thoroughly look forward to continuing to practice, grow and develop existing coding skills as well as learn new languages in due course.
I'd like to thank everyone who has helped me along the way, because it certainly would not have been possible without your support, teaching and encouragement.

---


