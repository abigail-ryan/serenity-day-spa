# Serenity Day Spa 
[View my live site here](https://)

Serenity Day Spa is a site for a fictional new business based in the South East coastal town of Tramore, Co. Waterford, Ireland. The Spa is centered around offering treatments to customers looking to book a relaxing appointment to escape and unwind. Serenity Day Spa provides users with a treatment menu, account registration, and booking process.
Unregistered users of this site can access all the information they need to know about Serenity Day Spa treatments, and can contact the site owners with any queries they may have via a contact form. Registered account users can book, edit and cancel their appointments via their user account dashboard, and also contact the site admin via the contact form.

![Screenshot of Serenity Day Spa responsive design through Am I responsive website](documentation/responsive_screenshot.PNG)

## Contents
* [Project Goals](#project-goals)
* [User Stories](#user-stories)
* [Agile Development](#agile-development)
* [UX](#ux)
  * [Strategy](#strategy)
  *	[Scope](#scope)
  * [Structure](#structure)
  * [Skeleton](#skeleton)
    * [Flowchart](#flowchart)
  * [Surface](#surface)
* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
* [Project Features](#project-features)
  * [Home](#home)
  * [Treatments](#treatments)
  * [Contact](#contact)
  * [Login](#login)
  * [Register](#register)
  * [Book Now](#book-now)
  * [My Account - User](#my-account)
  * [Admin Dashboard](#admin-dashboard)
  * [User Feedback](#user-feedback)
* [Future Features](#future-features)
* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries, Technologies and Programs used](#frameworks-libraries-technologies-and-programs-used)
* [Testing](#testing)
  * [Manual Testing](#manual-testing)
  * [HTML Validation](#html-validation)
  * [CSS Validation](#css-validation-using-w3c-validation) 
  * [Lighthouse scores using Chrome Dev Tools](#lighthouse-scores-using-chrome-dev-tools)
  * [Pep8 Validation](#pep8-validation)
  * [Bugs](#bugs)
* [Deployment](#deployment)
  * [Deploying to Heroku](#Deploying-to-heroku)
  * [Forking the GitHub Repository](#forking-the-github-repository)
  * [Clone the GitHub Repository](#clone-the-github-repository)
* [Credits](#credits)
  * [Code References](#code-references)
  * [Content and Media References](#content-and-media-references)
* [Acknowledgements](#acknowledgements)  
         
 
___

### Project Goals

The goal of this project is to create a tranquil and inviting online platform for users where they can easily access information about Serenity Day Spa’s range of relaxation treatments, and encourage visitors to register an account to book appointments.

___

### User Stories

**As a site user:**
* I can view a list of treatments so that I can select which one I want to view. - MUST HAVE
* I can click on a treatment so that I can read the full description - MUST HAVE
* I can register an account so that I can book an appointment - MUST HAVE
* I can fill out a contact form so that I can contact the business with any queries I may have - MUST HAVE


**As a registered user:**
* I can create, view, update, delete bookings so that I can manage my appointments - MUST HAVE
* I can fill out a contact form so that I can contact the business with any queries I may have - MUST HAVE
* I can leave a review so that I can give my feedback to the business and other site users. - COULD HAVE


**As a site admin:**
* I can create, read, update, delete treatments so that I can manage my services options - MUST HAVE
* I can view bookings so that I can manage my schedule - MUST HAVE
* I can store contact form submissions so that I can review them - MUST HAVE
* I can mark contact form submissions as read so that I can see how many I still need to process - MUST HAVE
* I can approve/decline reviews so that I can filter out negative reviews - COULD HAVE

___

### Agile Development

Serenity Day Spa was developed using an Agile approach. I used [Github Projects Board](https://github.com/users/abigail-ryan/projects/3) to manage the development of this project.

___

### UX

#### Strategy

* **User Engagement:** The website will prioritize a user-friendly interface  with simple navigation and clear CTA’s encouraging users to register an account in order to book appointments. Features such as quick access to treatment descriptions and an easy to use sign up form will enhance user interaction and increase booking rates.
* **Brand Positioning:** Serenity Day Spa will be positioned as a tranquil oasis in Tramore, emphasizing its commitment to relaxation and wellness. The website will showcase traditional spa treatments infused with natural elements, creating an emotional connection with potential clients.

#### Scope

* **User Types:** The site will cater to two primary user groups: unregistered users who can explore treatment options and contact the spa for inquiries, and registered users who can book, edit, or cancel appointments through their personalised dashboard.
* **Core Features:** Key functionalities will include a detailed treatment menu with descriptions and pricing, an easy account registration process, a robust booking system that allows users to select services and times, and a contact form for inquiries, ensuring all user needs are met efficiently.

#### Structure

* **Information Hierarchy:** The site’s information architecture will be designed to prioritize essential content. The homepage will feature direct links to the treatment menu, Login/Register options, and contact information, ensuring users can easily find what they need without unnecessary clicks.
* **Content Strategy:** Engaging content will be developed that highlights each treatment’s benefits, including customer testimonials. This approach not only informs users but also helps builds trust and encourages them to book services.

#### Skeleton

Wireframes have been created for each page of the site.

##### Wireframes

<details>
<summary>Home</summary>
<br>
Homepage (featuring popular treatments)

| Mobile View | Desktop View |
| ---| ---|
| ![Screenshot of Serenity Day Spa mobile view wireframe - index page](documentation/mobile-home.png) | ![Screenshot of Serenity Day Spa desktop view wireframe - index page](documentation/desktop-home.png) |
</details>

<details>
<summary>Treatments List</summary>
<br>
Each treatment can be clicked on to view the full description including price and duration.

| Mobile View | Desktop View |
| ---| ---|
| ![Screenshot of Serenity Day Spa mobile view wireframe - treatments list](documentation/mobile-treatments-list.png) | ![Screenshot of Serenity Day Spa desktop view wireframe - treatments list](documentation/desktop-treatments-list.png) |
</details>

<details>
<summary>Treatment Details</summary>
<br>
Each treatment can be clicked on to view the full description including price and duration.

| Mobile View | Desktop View |
| ---| ---|
| ![Screenshot of Serenity Day Spa mobile view wireframe - treatment details](documentation/mobile-treatments-list.png) | ![Screenshot of Serenity Day Spa desktop view wireframe - treatments details](documentation/desktop-treatments-list.png) |
</details>

<details>
<summary>Sign in</summary>
<br>

| Mobile View | Desktop View |
| ---| ---|
| ![Screenshot of Serenity Day Spa mobile view wireframe - index page](documentation/mobile-signin.png) | ![Screenshot of Serenity Day Spa desktop view wireframe - index page](documentation/desktop-signin.png) | 
</details>

<details>
<summary>Registration form</summary>
<br>

| Mobile View | Desktop View |
| ---| ---|
| ![Screenshot of Serenity Day Spa mobile view wireframe - index page](documentation/wf_Mobile_hero_Section.PNG) | ![Screenshot of Serenity Day Spa desktop view wireframe - index page](documentation/wf_Mobile_Navigation_menu.PNG) | 
</details>

<details>
<summary>User dashboard</summary>
<br>

| Mobile View | Desktop View |
| ---| ---|
| ![Screenshot of Serenity Day Spa mobile view wireframe - index page](documentation/wf_Mobile_hero_Section.PNG) | ![Screenshot of Serenity Day Spa desktop view wireframe - index page](documentation/wf_Mobile_Navigation_menu.PNG) | 
</details>

<details>
<summary>Contact page</summary>
<br>

| Mobile View | Desktop View |
| ---| ---|
| ![Screenshot of Serenity Day Spa mobile view wireframe - index page](documentation/wf_Mobile_hero_Section.PNG) | ![Screenshot of Serenity Day Spa desktop view wireframe - index page](documentation/wf_Mobile_Navigation_menu.PNG) | 
</details>


#### Surface

* **Visual Identity:** A calming color palette featuring soft blues and greens will be chosen to evoke tranquility. Typography will be selected for readability while reflecting elegance, ensuring that the visual identity aligns with the spa's mission of relaxation.
* **Responsive Design:** The website design will be fully responsive, ensuring optimal functionality across all devices - smartphones, tablets, and desktops. This adaptability is crucial for users who may wish to book appointments while on-the-go.
* **Accessibility Features:** Features like alt text for images, and screen reader compatibility will ensure that all users can access the site effectively.
* **Feedback Mechanisms:** Visual feedback mechanisms such as confirmation messages upon successful bookings or error notifications during form submissions will be implemented. 

___

### Design
#### Colour Scheme

Given that Serenity Day Spa is situated in a coastal town and offers treatments that incorporate natural elements, I selected a color palette from Canva Colors that features soft sandy tones complemented by shades of blue and green.

**My Chosen Colors:**

**COLOUR PALETTE TO BE ADDED HERE**

* Brown: #daa486 (representing sandy hues)
* Cream: #fafcf0 (evoking a sense of warmth and comfort)
* Teal Green: #13fbe2 (reflecting the tranquility of nature)
* Aquamarine: #008291 (symbolizing the calming essence of the sea)

#### Typography

I chose the following typography for my project:
* Dancing Script - as it’s a lively cursive font with a friendly and inviting feel. It is used for the headings throughout the site.
* Roboto: clean and modern with excellent readability. Used throughout the entire site for all text elements.

**FONTJOY SCREENSHOT TO BE ADDED HERE**

#### Imagery

To create the Spa's interior images for my project, I utilised an AI image generator [DeepAI](https://deepai.org/machine-learning-model/text2img), guided by the color palette I selected. The soft sandy tones, along with the natural blues and greens, inspired the visual elements, ensuring they align with the serene and coastal theme of Serenity Day Spa.

The media used throughout Serenity Day Spa Treatments were sourced from (images sources placed here). Attributions are placed in the Credits section of this README.

____

### Project Features
#### Home
#### Treatments
#### Contact
#### Login
#### Register
#### Book Now
#### My Account - User
#### Admin Dashboard
#### User Feedback

___

### Future Features

___

### Technologies Used
#### Languages
#### Frameworks, Libraries, Technologies and Programs used

___

### Testing
#### Manual Testing
#### HTML Validation
#### CSS Validation
#### Lighthouse scores using Chrome Dev Tools
#### Pep8 Validation
#### Bugs

___

### Deployment
#### Deploying to Heroku
#### Forking the GitHub Repository
#### Clone the GitHub Repository

___

### Credits
#### Code References
#### Content and Media References

___

### Acknowledgements 

___