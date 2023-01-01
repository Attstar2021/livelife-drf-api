![android-icon-144x144](https://user-images.githubusercontent.com/91749477/210184096-221d145b-3d5d-4359-b665-9d2c480a6550.png)




## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.


### Heroku

1. Log into Heroku and go to the Dashboard, Click “New” then Click “Create new app” then select "create a new app"

2. Give your app a name and select the region closest to you, then click “Create app”.

3. Open the Settings tab and Add a Config Var DATABASE_URLfrom ElephantSQL, SECRET_KEY from env.py file of your repo and CLOUDINARY_URL from Cloudinary.

4. Open the Deploy tab and in the Deployment method section, search for your repo and click Connect

5. You can click  Enable Automatic Deploys or Manual deploy and then click Deploy Branch.

6. when log showing a successful build then your app ready and deployed.

7. Open app button and your back-end API for this project is up and running


------

## heading

** Sub-heading **

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript)
-   [PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [POSTGRESQL](https://en.wikipedia.org/wiki/PostgreSQL)

### Frameworks, Libraries & Programs Used

1. [ReactJS:](https://en.wikipedia.org/wiki/React_(JavaScript_library)) 
 - React was use as a front-end JavaScript library for building user interfaces based on UI components.
2. [Django REST Framework:](https://en.wikipedia.org/wiki/Django_(web_framework))
 - DRF was used for back-end API.
4. [ElephentSQL:](https://www.elephantsql.com/)
 -  Elephant was used for SQL queries to create, read, update and delete data directly from my web browser.
5. [ReactBootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
 - Bootstrap was used to assist with the responsiveness and styling of the website.  
6. [Hover.css:](https://ianlunn.github.io/Hover/)
 - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.    
7. [Google Fonts:](https://fonts.google.com/)
 - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.     
8. [Font Awesome:](https://fontawesome.com/)
 - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.    
9. [Git](https://git-scm.com/)
 - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
10. [GitHub:](https://github.com/)
 - GitHub is used to store the projects code after being pushed from Git
11. [Cloudinary:](https://en.wikipedia.org/wiki/Cloudinary)
 - Cloudinary was used for to upload images and to store, manage, manipulate, and deliver for websites and apps.
12. [JustinMind:](https://en.wikipedia.org/wiki/Justinmind_(software))
 - justinMind was used to make wireframes for this project.
13. [Wix:](https://en.wikipedia.org/wiki/Wix.com)
  - Wix was use to make logo for this website
14. [favicon.io:](https://favicon.io/favicon-converter/)
  -  Favicon.io was used to create favicon for this website.
15. [Pillow:](https://pypi.org/project/Pillow/)
  - This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities


asgiref==3.5.2
cloudinary==1.30.0
dj-database-url==0.5.0
dj-rest-auth==2.2.5
Django==3.2
django-allauth==0.50.0
django-cloudinary-storage==0.3.0
django-cors-headers==3.13.0
django-filter==2.4.0
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
gunicorn==20.1.0
oauthlib==3.2.2
Pillow==9.3.0
psycopg2==2.9.5
PyJWT==2.6.0
python3-openid==3.2.0
pytz==2022.6
requests-oauthlib==1.3.1
sqlparse==0.4.3



---
