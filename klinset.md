- A detergent making and producing company that need an online presence and also an ecommerce platform integration
 
# 1. Landing page

## a. Navbar
- *`Add a mini top navbar for some basic static items`*
- A logo to show the company name and take user to homepage
- A list of links for navigation to:
    - `products`, `about-us`, `cart`, `profile`, `contact-us` 
- A search bar to allow for product lookup

## b. heros section
- A large banner spanning the width of the webpage
- Slogan/title representing the company with a small call to action sentence and button
- Call-To-Action feature for: ``Shop Now``, ``Learn More``, ``get started``

## c. Featured products
- Show a list of the top selling, most popular, featured products, new products etc.

## d. About us section
- what the company is about in a brief 
- Short description of the company
- Where they serve
- Some of the products they sell

## e. blogs section
- Some few blog posts about the companies mission and products
    - Cleaningn tips and product usage or sustainaiblity practices
    - Company news and updates.
    - Tutorails and DIYs guide on related cleaning products?
 
## f. Testimonials section
- Some of the customers we have served 
- Our big clients that use our products

## g. footer section
- **Newsletter**
    - email enter form
    - subscribe button

 - **Shop by category**
    - Antiseptics
    - Detergents
    - Disinfectants
    - Handwash

- **about the company**
    - Gallery
    - Company Blogs
    - Band story
    - Careers

- **social links**
    - link/logo for X, FB, IG, Yt etc.
    - Location, contact information,
    - Google map integration

- **Help links**
    - FAQSs
    - Terms of service
    - privacy policy
    - Shipping and refund information


# 2. products page
- **Show all the products unless a filter is added to the items**
- **Section to filter out products based on:**
     - category of the detegent product
     - price of the item
- **The products card should:**
    - should have a button to add to cart,
    - clickable to learn more about it
    - Nice hover effect

# 3. Single product page
- Show the selected product in details:
    - multiple images of the items
    - how to use the product
    - Rating of the product
    - price of the product
    - dangers/side effects of the comodity
    - Related products to the selected product


# 4. Contact Us page
- Location of where the offices are
- Contact details: `email`,`phone-number`,
- Input form for the following data: 
    - Name- (full name)
    - email address
    - country fo residence
    - phone number
    - Enquiry
- Google map integration

# 5. About Us page
- Show the companies mission, vision and beliefs
- what the company has achieved so far
- what they are doing/do/produce
- Companies background and story statement
- photos of the teams and technologies used
- Any certfications or awards

# 6. profiles page
- Details/data we have on the user in our DB
- Update a user's information: `address`, `userData`
- View all their orders and filter them 
- 

# 7. Cart
- **Items in the cart**
    - user can edit the items in his cart
    - proceed to the checkout
- **checkout**
    - Key in the pickup address 
    - If `loggedIn=true` use the users info else prompt for details 
    - Get the total amount (taxes + shipping charges + discounts)
    - Add payment details and charge the customer
    - Then place the order once payment is successful    

# 8. Auth pages
- **Login page**
    - Form input to enter the following: 
        `email/username/phone_number`, `password`, 
    - Navigation to take user to forgot password page, New user page 
- **Register page**
    - Form inputs to enter basic user registration details: 
        `email`, `full name`, `username`, `passwords`, `password-confirm`, `phone number`
    - Navigation to take the user to login
- **Forgot password page**
    - User enter the email to get the access token
    - Use the token or link to enter a new password and confirmation
    - if all passes are successful then redirect and send a confirmation email
- 
