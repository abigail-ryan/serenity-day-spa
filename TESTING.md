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

____

#### Lighthouse scores using Chrome Dev Tools

____

#### Manual Testing

____

#### Bugs

____