# simple-blog

## Introduction
**Simplbe-Blog** is a fullstack application where users can register, log in and add some simple blogs. Users have their profiles created on sin up and can edit their profile. Use are also capable of retrieveing lost password via email. You can add, edit, delete and view posts. You can also filter posts based on users.
## __Application Link__
https://dukeblog.herokuapp.com/

## Key Application features  
* Users can create account and log in
* Users can view posts submitted by other users
* Authenticated uses can view details of a post
* Authenticated user can edit and delete their posts
* Authenticated user can manage his profile
* Authenticated user can log out
* Users can retrieve lost/forgotten password

## Technologies used
* Python: A fast growing programming language
* Postgres DBMS: An open-source RDBMS for storing data
* Django web framework: A fullstack Python web application framework
* <a href ="https://jwt.io/">JSON Web Token: </a> A JSON-based standard for creating access tokens.
* AWS S3: A cloud based file storage system from Amazon Web Services


## Installing the application 

* Clone the application to your local system
```Sh
> $ `git clone https://github.com/Victoradukwu/simple-blog.git`
```
* Change the directory on your local system
```Sh
> $ `cd /simple-blog`
```
* Install all dependencies
```Sh
> $ `pip install -r requirements.txt`
```
* create a .env file at you app root and populate it withb the encironment variables such as:
```Sh
DEBUG=True
EMAIL_HOST_USER=you_gmail_account
EMAIL_HOST_PASSWORD=your_gmail_password
SECRET_KEY=your_secret_key
AWS_ACCESS_KEY_ID=your_AWS_access_key_id
AWS_SECRET_ACCESS_KEY=your_AWS_secret_access_key
AWS_STORAGE_BUCKET_NAME=your_AWS_S3_bucket
```
* Export Environment variables
```Sh
> $ `export $(cat .env)`
```
* Migrate the application
```Sh
> $ `python manage.py migrate`
```
* Start the application
```sh
> $ python manage.py runserver
```
## Testing
* Create a test database and name it `Testdb`
* Run Test `$ python manage.py test`
