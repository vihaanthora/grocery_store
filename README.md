# Grocery Store Backend - A Rest API
This project consists of a rest API that is designed to simluate the working of a grocery store. 
## Tech Stacks
1. Python 3.8- Programming language
2. Django 3.2 - Python based web framework
3. Django-REST Framework 3.12 - A powerful toolkit to create web APIs
## Assumptions
1. Every item present in the grocery store has a unique code, i.e., no two distinct items have the same code in the system. Hence, the item code is used as primary key in the items table. This code can be a barcode or any other coding convention followed by the store such as category code followed by a serial number, etc.
2. Every user is identified by his/her phone number. This is a valid assumption as this system is followed by major retail giants all over the world. Hence, the phone number is used as a primary key in the users table.
## ER Diagram
https://drawsql.app/personal-284/diagrams/grocery-store#
## Instructions
After cloning the repository in your code editor, type the following commands in the terminal to run the server:
1. $ cd GroceryStore
2. $ python manage.py makemigrations
3. $ python manage.py migrate
4. $ python manage.py runserver     
   
After this, the server should be successfully running on your local machine.
## Admin Access
To create a super user, i.e., to have admin rights provided by Django, you can run the following command:
1. $ python manage.py createsuperuser   
         
When prompted, enter a username and a password for Django admin page. The admin can be accessed by clicking the URL http://localhost:8000/admin/. Here, you can enter the credentials that were entered before while creating the superuser. After logging in successfully, you will have a dashboard showing you all the admin rights provided by Django in this project. 
## API Documentation
For using the different features offered by the API, you can simply go to the URLs present in the documentation of the API, which can be seen by opening https://documenter.getpostman.com/view/17859944/UV5RnfnY
