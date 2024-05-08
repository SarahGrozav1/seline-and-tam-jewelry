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

# **3. User Experience (UX)**

### **3.1.1 The Idea**
- The intention of **Seline & Tam Jewelry** site is to be friendly online shop where users can browse variate of products sorted between categories. Besides that, user can read details of each product, see product reviews and comments.

### **3.1.2 The Ideal User**

The target audience are individuals who are seeking luxury jewelry. Those who want to make gifts or to wear a luxury jewelry for themselves.

- Ideal user likes to shop online
- Ideal user likes to explore new trends and ideas in the jewelry field
- Ideal user likes to share their opinion in form of **reviews** and **comments**

### **3.1.3 Site Goals**

- Offer users ability of shopping online without leaving their home
- Offer users ability of reading other people comments on products
- Offer users ability to add items to their **Wishlist** if they want to save the item for later
- Offer users the ability to see details of each item in shop ( price, description, collection etc. ) 
- Provide site visitors with an easy to navigate site to view jewelry products

### **3.1.4 User stories**

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

---

### **3.1.5 Early Development**

At the start of the project, even though I had the wireframes as versions of how I wanted the site to look, I more often than not made early mockup versions of the pages to quickly get the framework of the pages set up and to test whether I might like to do something another way or differently from the wireframes. 

Here is an early example of my index page, mocked up at the very start of the project. 
Key differences here include two more sections about more informations about the jewelry store that I decided to dont include them anymore in my project so that I could focus more on backend. But I want to create them in the future.

![Early Development Index Section](/static/media/documents/more-sections1.png)

![Early Development Index Section](/static/media/documents/more-sections2.png)

I started the project with the home page and nav bar, before installing django allauth and getting the base templates for that. From there, I began working on backend more and didn't focuse on frontend because I wanted to leave it the last, first to make my project work and then add design and fronted details to look better.

Here is an early mockup of my collections page which I decided to don't make it anymore because I did a dropdown button in the navbar from where the user can select easily the collection he wants to see.

![Early Development Collections Page](/static/media/documents/collection-page.png)

---

### **3.1.6 SEO and Web Marketing**

**Who:** I am marketing predominantly towards a jeweler-enthuasiast.
**What:** I am selling jewelry, designed to cater towards this audience. I therefore make it very accessible and clear on my site, so that the audience can go directly towards what they are looking for. I include images of jewelry, designed to excite the site viewer into wondering what it's like to wear them with some sophisticated clothes. It was equally important to make clear titles and key pieces of information available for the site viewers to see on which ever respective page/product they are viewing.
**How:** Based on my B2C model, I decided single payments with Stripe were the best payment option for the products I'm offering. I can update users on new products and general news through an opt-in mailchimp newsletter subscription and I have created a Facebook page which users/clients can view and follow to keep up to date through a social network.


Software developers play a role in making sure their website can be easily found through search engines, including the reviews of Google Search.
Therefore, when implementing SEO (Search Engine Optimisation) tools, the best means available to you are through descriptive and relevant keywords, sitemaps.xml and robots.txt files.

**Keywords and sitemap/robots**

- I included keywords and more tags in my base.html document. This allowed me to define keywords, an author, a site description and a viewport. For the keywords themselves I thought about short and longer words and phrases respectively that might be looked for. 

- I started with fairly obvious short words including: jewelry, gold jewelry, gold bracelet, gold necklace,gold rings,gold earings, luxury jewelry.

- I then expanded in to short phrases, including: golden luxury jewelry

- I have included a sitemap.xml file in the root directory, which allows search engines to crawl through my site and make content more discoverable.

- I have a robots.txt file which provides the location of the sitemap and also defines any folders/files which are prohibited from search engine crawlers.


