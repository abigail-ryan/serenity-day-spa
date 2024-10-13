# Testing

This is the TESTING file for [Serenity Day Spa](https://serenity-day-spa-c4459ce39df8.herokuapp.com/)

Return to the [README.md](README.md) file.

## Contents

* [HTML Validation](#html-validation)
* [CSS Validation](#css-validation-using-w3c-validation) 
* [Pep8 Validation](#pep8-validation)
* [Lighthouse scores using Chrome Dev Tools](#lighthouse-scores-using-chrome-dev-tools)
* [Manual Testing](#manual-testing)
* [Bugs](#bugs)

____

#### HTML Validation

For testing my HTML for this project, I used the Validate by Direct Input option on W3C Markup Validation. 


![Screenshot of Serenity Day Spa - HTML Validation Home Page](documentation/home-html-check.png) 

I checked all pages of the site in this way and the results are below:

| HTML Page | Errors | Warnings |
| ---- | ------ | -------- | 
| Home | None | None |
| Treatments | None | None |
| Contact | None | None |
| Sign in | None | None |
| Book Now | None | None |
| My Account | None | None |
| Logout | None | None |
| Edit Booking | None | None |
| Delete Booking | None | None |
| Logout | None | None |
| Error 404 | None | None |
| Error 500 | None | None |
| Register | 4 | None |

The Register Page returned 4 errors as show below:

![Screenshot of Serenity Day Spa - HTML Validation Register Page](documentation/register-page-errors.png) 

As this was a standard AllAuth template, I was unable to make adjustments. For future development of this project I will create a custom Register form.

____

#### CSS Validation

My CSS Validation check returned no errors.

![Screenshot of Serenity Day Spa - CSS Validation](documentation/css-validation.png) 
____

#### Pep8 Validation

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files. Some minor line lenght isuues, missing lines, and trailing white space errors were raised and fixed before final deployment.

![Screenshot of Serenity Day Spa - PEP8 Validation - minor errors](documentation/pep8-minor-errors.png) 

![Screenshot of Serenity Day Spa - PEP8 Validation - no errors](documentation/pep8-no-errors.png) 

| App | admin.py | forms.py | models.py | urls.py | views.py |
|---------|----------|----------|-----------|---------|----------|
|  Main Project | N/A | N/A | N/A | no errors | N/A |
| booking | no errors | no errors | no errors | no errors | no errors |
| home | N/A | N/A | N/A | no errors | no errors |
| treatments | no errors | N/A | no errors | no errors | no errors |
| contact | no errors | no errors | no errors | no errors | no errors|
| user_account | N/A | N/A | N/A | no errors | no errors |

____

#### Lighthouse scores using Chrome Dev Tools

My Lighthouse performace Score for the Home Page is lower than I would have liked for both Mobile and Desktop. This is due to the fact that my carousel images in the Hero section are quite large files. I also suspect that they are loading slower due to being hosted on Cloudinary. I had previously compressed the images and placed them as static files, however this lead to lots of noise and blur within the images. For future development I will look furhter into compressing images without losing so much of the quality.

**DESKTOP**

<details>
<summary>Home Page</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - desktop home page](documentation/desktop-lighthouse-score-homepage.png)  
</details>

<details>
<summary>Treatments List</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - desktop treatments list](documentation/desktop-lighthouse-score-treatmentslist.png)  
</details>

<details>
<summary>Treatment Details</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - desktop treatment details](documentation/desktop-lighthouse-score-treatmentdetails.png)  
</details>

<details>
<summary>Contact</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - desktop contact](documentation/desktop-lighthouse-score-contact.png)  
</details>

<details>
<summary>Sign In</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - desktop sign in](documentation/desktop-lighthouse-score-signin.png)  
</details>

<details>
<summary>Register</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - desktop register](documentation/desktop-lighthouse-score-register.png)  
</details>

<details>
<summary>My Account</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - desktop my account](documentation/desktop-lighthouse-score-myaccount.png)  
</details>

<details>
<summary>Book Now</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - desktop book now](documentation/desktop-lighthouse-score-booknow.png)  
</details>

<br> 

**MOBILE**

<details>
<summary>Home Page</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - mobile home page](documentation/mobile-lighthouse-score-homepage.png)  
</details>

<details>
<summary>Treatments List</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - mobile treatments list](documentation/mobile-lighthouse-score-treatmentslist.png)  
</details>

<details>
<summary>Treatment Details</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - mobile treatment details](documentation/mobile-lighthouse-score-treatmentdetails.png)  
</details>

<details>
<summary>Contact</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - mobile contact](documentation/mobile-lighthouse-score-contact.png)  
</details>

<details>
<summary>Sign In</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - mobile sign in](documentation/mobile-lighthouse-score-signin.png)  
</details>

<details>
<summary>Register</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - mobile register](documentation/mobile-lighthouse-score-register.png)  
</details>

<details>
<summary>My Account</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - mobile my account](documentation/mobile-lighthouse-score-myaccount.png)  
</details>

<details>
<summary>Book Now</summary>
<br>

![Screenshot of Serenity Day Spa lighthouse testing - mobile book now](documentation/mobile-lighthouse-score-booknow.png)  
</details>

<br>

The Best Practices Score showed details regarding the Treatmeent Images stating the connection was not secure. This is something I will look into regarding securely loading externally hosted files.
![Screenshot of Serenity Day Spa lighthouse testing - mobile book now](documentation/lighthouse-score-best-practices.png)  

____

#### Manual Testing

____

#### Bugs

____