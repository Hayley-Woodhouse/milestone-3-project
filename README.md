
# Contents
* [1 UX Design](#1-ux-design)
    * [1.1 User Stories](#11-user-stories)
* [2 Strategy](#2-strategy)
    * [2.1 Developers Project](#21-developers-project)
    * [2.2 Business](#22-business)
    * [2.3 Users](#23-users)
* [3 Scope](#3-scope)
    * [3.1 Features](#31-features)
    * [3.2 Future Updates](#32-future-updates)
* [4 Structure](#4-structure)
    * [4.1 Initial Page Structure](#41-initial-page-structure)
* [5 Skelaton](#5-skeleton)
    * [5.1 Wireframes](#51-wireframes)
    * [5.2 The Home Page](#52-the-home-page)
    * [5.3 The Library Page](#53-the-library-page)
    * [5.4 The Sign-up Page](#54-the-sign-up-page)
    * [5.5 The Login Page](#55-the-login-page)
    * [5.6 The Users Profile Page](#56-the-users-profile-page)
* [6 Surface](#6-surface)
    * [6.1 Visual Design](#61-visual-design)
    * [6.2 Colours](#62-colours)
    * [6.3 Typography](#63-typography)
    * [6.4 Images](#64-images)
* [7 Database](#7-database)
    * [7.1 Tables](#71-tables)
        * [7.1.1 Books](#711-books)
        * [7.1.2 Users](#712-users)
        * [7.1.3 Comment](#713-comment)
* [8 Website operations](#8-wesite-operations)
    * [8.1 Home](#81-home)
    * [8.2 Library](#82-library)
    * [8.3 Sign up](#83-sign-up)
    * [8.4 Login](#84-Login)
    * [8.5 Admin](#85-admin)
        * [8.5.1 Edit user](#851-edit-user)
        * [8.5.2 Add book](#852-add-book)
        * [8.5.3 Edit book](#853-edit-book)
    * [8.6 User](#86-user)
        * [8.6.1 Comment](#861-comment)





# 1 Ux design

## 1.1 User Stories

### Consumer user stories

As a user I want to..

1.    Have a clear and straightforward view of the selection of the books, the books information and synopsis and other users comments. 
2.	Manage a personal account allowing me to add, edit and remove content.
3.	View my contributions view my personal account
4.	Navigate the site with easy on all formats.

[Back to top](#contents)

### Business user stories

As a business I want to..

1.	To have a clear interactive layout
2.	Have access to multiple social media links
3.	Have simple colour scheme, representative of the books cover art.
4.	Have the site accessible across all devices. 
5.	Have a admin process to monitor behaviour and manage content.

[Back to top](#contents)

### Developers’ user stories

As a web developer I want to..

1.	provide an easily manageable interactive user experience
2.	have a site that is compliant with W3C guidelines and PEP8 in python
3.	provide well commented code for future updates
4.	have concise use of relational and non-relational databases

[Back to top](#contents)

# 2 Strategy

## 2.1 Developers Project

The aim for this project is to produce a fan site for David Walliams books. Users will be able to register an account for. From there the user can add their own personal comments on the library of books, edit and delete comments and upload new/ additional books to the site. With a simple and readable format, the site will be easy to navigate.

[Back to top](#contents)

## 2.2 Business

To provide a great social media experience enabling users to interact and share comments on their favourite David Walliams books. Giving the users the ability to add content to page managed by an admin account.

[Back to top](#contents)

## 2.3 Users

The aim is to give users a simple and clear user platform to engage in discussions and review the books available. The user can manage their comments with add, edit, and delete options and add new material to the book library page that it added when the administrator of the page enables the new listing.

[Back to top](#contents)

# 3 Scope

## 3.1 Features

The following list of objectives it designed to achieve a well-balanced website that meets the needs and requirements of the business and users strategy outcomes. Within the designated time scale the following criteria will be introduced to the website on initial release.

-	Registration form to sign up for a user profile.
-	A login section
-	Users profile page with logout option
    -	A tally of comments the user has made
    -	An option to add books and information with admin release prompt.
    -	A tally of books added to the library
-	A scrolling library page with book images, information, and comment section
-	A welcome homepage 

[Back to top](#contents)

## 3.2 Future Updates

?? to be added 

[Back to top](#contents)

# 4 Structure

The feature acknowledged from the scope plane will be implemented into the structure of the website.

[Back to top](#contents)

## 4.1 Initial Page Structure

-	The navigation bar will consist of 
-	A home link which will send the user back to the welcome page
-	A library page which palls data from a relation database and displays book information. 
-	A login link which will transfer the user a login field input page
-	A sign up link that will send the user to the sign up field input page
-	The footer will contain links to social media accounts 
-	The home page will have a description about the site. Advise on how to interact with other users and how to registers for an account.
-	The library page will have a list of books, images, information on each book and a comment section for users interact
-	The login link with an email and password fields to access pre-registers users profile page
-	A profile page with a tally chart of comments the user has added and books the user has added to the library
-	The sign up page with input fields for creating a user’s account. 

[Back to top](#contents)

# 5 Skeleton

## 5.1 Wireframes 

The wireframes for the website were created using Balsamiq Wireframes. Using the structure plane the following mock-ups were generated.

[Back to top](#contents)

## 5.2 The Home Page

The opening page has a description about the site, its goals, and its available functionality.   There will also be a link to the sign-up page to encourage and enhance usability. 

![home-page-mod](assets/images-readme/mob_welcome_wire.png)\
*compressed from 43.6 KB to 12.8 KB via [TinyPNG](https://tinypng.com/)*


![home-page-tablet](assets/images-readme/tablet_welcome_wire.png)\
*compressed from 42.8 KB to 14.8 KB via [TinyPNG](https://tinypng.com/)*


![home-page-desk](assets/images-readme/desk_welcome_wire.png)\
*compressed from 44.9 KB to 14.4 KB via [TinyPNG](https://tinypng.com/)*


[Back to top](#contents)

## 5.3 The Library Page

The library page consists of list of book titles, an image of the book and the information associated. Underneath the data there is a comment box enable users to add their views on the books and engage in conversations with other users. The books will be on a continual scroll however the more the data increase a later update for placing the data on multiple pages for easier viewing.

![library-page-mod](assets/images-readme/mob_books_wire.png)\
*compressed from 42.2 KB to 12.5 KB via [TinyPNG](https://tinypng.com/)*


![library-page-tablet](assets/images-readme/tablet_books_wire.png)\
*compressed from 52.4 KB to 17.6 KB via [TinyPNG](https://tinypng.com/)*


![library-page-desk](assets/images-readme/desk_books_wire.png)\
*compressed from 44.9 KB to 14.4 KB via [TinyPNG](https://tinypng.com/)*


[Back to top](#contents)

## 5.4 The Sign-up Page

To register for an account an input form for personal information is provided. The user can access this with a link via the navbar and the home page. This will be a input form.

![sign-up-page-mod](assets/images-readme/mob_signup_wire.png)\
*compressed from 40.7 KB to 11.1 KB via [TinyPNG](https://tinypng.com/)*


![sign-up-page-tablet](assets/images-readme/tablet_signup_wire.png)\
*compressed from 41.4 KB to 13.5 KB via [TinyPNG](https://tinypng.com/)*


![sign-up-page-desk](assets/images-readme/desk_signup_wire.png)\
*compressed from 47.6 KB to 15.6 KB via [TinyPNG](https://tinypng.com/)*


[Back to top](#contents)

## 5.5 The Login Page

The format for this is like the sign-up page for familiarity. The user will use their email address and their password to access their personal account.

![login-page-mod](assets/images-readme/mob_login_wire.png)\
*compressed from 40.7 KB to 11.6 KB via [TinyPNG](https://tinypng.com/)*


![login-page-tablet](assets/images-readme/tablet_login_wire.png)\
*compressed from 41.9 KB to 13.9 KB via [TinyPNG](https://tinypng.com/)*


![login-page-desk](assets/images-readme/desk_login_wire.png)\
*compressed from 47.4 KB to 16.1 KB via [TinyPNG](https://tinypng.com/)*


[Back to top](#contents)

## 5.6 The Users Profile Page

The profile page will have the name an image and a tally of comments the user has made and books the user has uploaded to the library.

![user-page-mod](assets/images-readme/mob_user_wire.png)\
*compressed from 26.9 KB to 6.9 KB via [TinyPNG](https://tinypng.com/)*

![user-page-tablet](assets/images-readme/tablet_user_wire.png)\
*compressed from 28.5 KB to 8.3 KB via [TinyPNG](https://tinypng.com/)*

![user-page-desk](assets/images-readme/desk_user_wire.png)\
*compressed from 40.0 KB to 11.5 KB via [TinyPNG](https://tinypng.com/)*

[Back to top](#contents)

# 6 Surface

## 6.1 Visual Design 

The visual design for the website covers the colours, fonts, effects, and images.

[Back to top](#contents)

## 6.2 Colours

The colours selected for the website where generated from [coolors.com](https://coolors.co/palette/577590-f3ca40-f2a541-f08a4b-d78a76). The colour are set using HEX placement values.

![Palette image of generated colours](assets/images-readme/color_palette_wire.png)\
*compressed from 28.6 KB to 8.3 KB via [TinyPNG](https://tinypng.com/)*

When using the [materialize](https://materializecss.com/) design services the colour generated are not directly hex place accurate to the above sample. However the [coolors.com](https://coolors.co/palette/577590-f3ca40-f2a541-f08a4b-d78a76) website provides a good blue print for colour selection. To regenerate the style above the following colour are to be impemented within the website using [materialize](https://materializecss.com/color.html) availibility. 

![materialize blue colour](assets/images-readme/blue_colour_wire.png)\
*compressed from 4.3 KB to 977 B via [TinyPNG](https://tinypng.com/)*


![materialize dark orange colour](assets/images-readme/dorange_colour_wire.png)\
*compressed from 4.3 KB to 968 B via [TinyPNG](https://tinypng.com/)*


![materialize orange colour](assets/images-readme/orange_colour_wire.png)\
*compressed from 4.2 KB to 968 B via [TinyPNG](https://tinypng.com/)*


![materialize yellow colour](assets/images-readme/yellow_colour_wire.png)\
*compressed from 3.9 KB to 968 B via [TinyPNG](https://tinypng.com/)*


![materialize stone colour](assets/images-readme/stone_colour_wire.png)\
*compressed from 4.6 KB to 1.1 KB via [TinyPNG](https://tinypng.com/)*

[Back to top](#contents)

## 6.3 Typography

The font type used throughout the website is as follows.

Heading and Titles
Caveat regular 400, medium 500, semi-bold 600, bold 700

Paragraphs 

Work sans thin 100, extra light 200, light 300, regular 400.

![typography from google fonts](assets/images-readme/googlefonts_wire.png)\
*compressed from 86.6 KB to 26.0 KB via [TinyPNG](https://tinypng.com/)*

[Back to top](#contents)

## 6.4 Images

Home page image downloaded form [swindon advertiser](https://www.swindonadvertiser.co.uk/news/16103604.comedian-david-walliams-talks-book-gangsta-granny/#gallery0)


![home page image](dw_fan_site/static/images/david_walliams.jpg)


All book images were sourced from [waterstone](https://www.waterstones.com/books/search/term/david+walliams/page/2#p_8764527)


![david walliams books](assets/images-readme/books_1.png)


![david walliams books](assets/images-readme/books_2.png)


![david walliams books](assets/images-readme/books_3.png)


![david walliams books](assets/images-readme/books_4.png)


![david walliams books](assets/images-readme/books_5.png)


![david walliams books](assets/images-readme/books_6.png)


![david walliams books](assets/images-readme/books_7.png)


[Back to top](#contents)


# 7 Database 

postgres was installed locallt to create a database and SQLAlcemy was installed to work with python to add data to tables and query the database.

The database name dw_fan_site



![books model image](assets/images-readme/db_mock_up.png)\
[Back to top](#contents)

## 7.1 Tables

### 7.1.1 Books 

The books model creates the table columns for the database. Frome the routes.py the add_book, edit_book and delete_book enables full CRUD operations. 
From the html pages these operations can be viewed on the add_book(create), books(read), edit_book(update) and books(delete). These are only avalible to the admin user.

The model.py schema 
![books model image](assets/images-readme/books_model_readme.png)\
[Back to top](#contents)


### 7.1.2 Users

The users model creates the table columns for the database. Frome the routes.py the sign_up, edit_user and delete_user enables CRUD operations. 
From the html page these operations can be seen on the sign_up page(create),
profile_html(read), admin.html(update and delete). The edit and delete operations are currently only available to the admin user.

The model.py schema
![users model image](assets/images-readme/user_model_readme.png)\
[Back to top](#contents)

### 7.1.3 Comment

Login - routes.py
![comment model image](assets/images-readme/comment_model_readme.png)\
The comment model creates the table columns for the database. From the routes.py
the comment and delete_comment enables the CRD operations. The update operation is added to the future updates. The html pages for these operations is comment(create), books and profile(read), and profile(delete).

[Back to top](#contents)

# 8 Website operations
The following discribes the operations and functions on the webpage.

[Back to top](#contents)

## 8.1 Home page

The homepage is the opening page. It gives the user the information about the site the what the user needs accomplish in order to get full access to its features. 

![home page](assets/images-readme/home_page.png)\
[Back to top](#contents)

## 8.2 Library

The library page has a list of all books currently in the database. Un-registered users can see comments made by registered users but are prevented from commenting themselves. This is a feature only available to registers users. 

![library page](assets/images-readme/library_page.png)

[Back to top](#contents)

## 8.3 Sign up

The sign-up page is a form with all inputs set to required. The email input will only accept on email on that name to prevent multiple accounts from one user. Once this information is submitted the information will be stored in the database in the table for users.

![sign up page](assets/images-readme/sign_up_page.png)\
[Back to top](#contents)

## 8.4 Login

The login page will prevent users from accessing their profile page if data is inputted incorrectly. Once this is achieved with the correct information the user will be directed to the their profile page.

![login page](assets/images-readme/login_page.png)\
[Back to top](#contents)

## 8.5 Admin

The admin page/account has a lot of functionality. The ability to edit and delete users. The admin account can also add, edit, and delete books. These are not available to any other user.

![admin page](assets/images-readme/admin_page.png)\
[Back to top](#contents)

### 8.5.1 Edit user

The page that renders when editing the user’s informationfrom the admin account. This has the availability to change all fields except passwords. This is a feature for future updates

![edit user info](assets/images-readme/edit_user_page.png)\
[Back to top](#contents)

### 8.5.2 Add book

Adding a book doesn’t require full input fields and again is only accessable from the admin account.

![add book page](assets/images-readme/add_new_book_page.png)\
[Back to top](#contents)

### 8.5.3 Edit book

As with adding a book the edit doesn’t require all fields to be entered and is also a feature only available from the admin account.

![edit book page](assets/images-readme/edit_book_page.png)\
[Back to top](#contents)

## 8.6 User

The user account renders a profile page that displays the users full name and all comments that user has made to books on the library page. From this page the user can delete their comments. The user will remain logged in and can navigate to pages available on the user. The user will need to hit the log out button on the navbar. All previous changes will remain when the user logs in again.

![profile page](assets/images-readme/profile_page.png)\
[Back to top](#contents)

### 8.6.1 Comment

From clicking the comment button, the user can add a comment to the book on the page. the comment will render at the top of the comments section as well as on the users profile page.

![ library comment page](assets/images-readme/library_comment_page.png)\
The comment form will render with the name of the book the user is commenting on.

![comment page](assets/images-readme/comment_page.png)\
[Back to top](#contents)

# 9 Testing

Click the [link](TESTING.md) for testing.

[Back to top](#contents)

# 10 Deployment

 # 11 Technologies used
- [HTML 5](https://en.wikipedia.org/wiki/HTML5) 
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JS](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine))
- [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)
- [Balsamiq](https://balsamiq.com/wireframes/desktop/#)
- [gitpod](https://www.gitpod.io/)
- [github](https://github.com/Hayley-Woodhouse/Milestone-3-project)
- [W3 Schools](https://www.w3schools.com/)
- [Heroku](https://www.heroku.com/)
- [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))


# 12 Credits

- [materialize](https://materializecss.com/)
- [Font awesome](https://fontawesome.com/) was used for all icons.
- [Google fonts](https://fonts.google.com/) was used for the fonts within the website.
- [Favicon](https://favicon.io/emoji-favicons/books) was used for the favicon image.
- [W3S](https://validator.w3.org/) was used to validate the html and css files.

[Back to top](#contents)

# 13 Acknowledgements

This web site was created for my third milestone project for the full stack development diploma with the code instatute and harlow college.

With thanks to 

My fellow class mates for there support and assistance.

Philip Morris for the tuition and guidence.

Richard, Isla and Ben Woodhouse for support and user testing.

[Back to top](#contents)

--->


