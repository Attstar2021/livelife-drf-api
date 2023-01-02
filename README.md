![android-icon-144x144](https://user-images.githubusercontent.com/91749477/210184096-221d145b-3d5d-4359-b665-9d2c480a6550.png)



## Deployment

### Deployment steps
#### set the following environment variables in env.py and setting.py:
1. CLIENT_ORIGIN
2. CLOUDINARY_URL
3. DATABASE_URL
4. DISABLE_COLLECTSTATIC
5. SECRET_KEY

#### Installed the following libraries to handle database connection:
- psycopg2
- dj-database-url
- 
#### Then,
- configured dj-rest-auth library for JWTs
- set allowed hosts
- configured CORS (set allowed_origins)
- set default renderer to JSON
- added Procfile with release and web commands
- gitignored the env.py file
- generated requirements.txt
- deployed to Heroku (Please see the steps given below)

### Heroku

1. Log into Heroku and go to the Dashboard, Click “New” then Click “Create new app” then select "create a new app"

2. Give your app a name and select the region closest to you, then click “Create app”.

3. Open the Settings tab and Add a Config Var DATABASE_URLfrom ElephantSQL, SECRET_KEY from env.py file of your repo and CLOUDINARY_URL from Cloudinary.

4. Open the Deploy tab and in the Deployment method section, search for your repo and click Connect

5. You can click  Enable Automatic Deploys or Manual deploy and then click Deploy Branch.

6. when log showing a successful build then your app ready and deployed.

7. Open app button and your back-end API for this project is up and running


------

## Manual Testing

** Sub-heading **

## Technologies Used

### Languages Used

-   [PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [POSTGRESQL](https://en.wikipedia.org/wiki/PostgreSQL)

### Frameworks, Libraries & Programs Used

1. [Django REST Framework:](https://en.wikipedia.org/wiki/Django_(web_framework))
 - DRF was used for back-end API.
2. [ElephentSQL:](https://www.elephantsql.com/)
 -  Elephant was used for SQL queries to create, read, update and delete data directly from my web browser.    
3. [Git](https://git-scm.com/)
 - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
4. [GitHub:](https://github.com/)
 - GitHub is used to store the projects code after being pushed from Git
5. [Cloudinary:](https://en.wikipedia.org/wiki/Cloudinary)
 - Cloudinary was used for to upload images and to store, manage, manipulate, and deliver for websites and apps.
6. [JustinMind:](https://en.wikipedia.org/wiki/Justinmind_(software))
 - justinMind was used to make wireframes for this project.
7. [Wix:](https://en.wikipedia.org/wiki/Wix.com)
  - Wix was use to make logo for this website
8. [Pillow:](https://pypi.org/project/Pillow/)
  - This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities
9. [dj-database-url:](https://pypi.org/project/django-database-url/)
  - a supporting libraries for postreSQL
10. [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/introduction.html)
  - a set of REST API endpoints to handle User Registration and Authentication tasks.
11. [django-allauth:](https://django-allauth.readthedocs.io/en/latest/)
  - an integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication
12. [django-cors-headers:](https://pypi.org/project/django-cors-headers/)
  - a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS). A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.
13. [gunicorn:](https://docs.gunicorn.org/en/stable)
    - is the server that we use to run django on heroku
14. [psycopg2:](https://pypi.org/project/psycopg2/)
    - Psycopg is the most popular PostgreSQL database adapter for the Python programming language which is use to connect with postgresSQL




---
