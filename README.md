# Python Engineer Test

## Project’s Structure

It's a django app integrated with postgres. 


## Directions to running the code

It is required that you have installed on your machine:
-   docker
-   docker-compose

In the work space folder run:

0.  make build
1.	make run

In a new terminar run:

0.	Go to the work space folder
1.	make shell

Once you are inside the docker instance run:

0.	python manage.py makemigrations
1.	python manage.py migrate


Open the browser or postman with the following url:

Create an user account
-   http://0.0.0.0:8000/api/signup/

Loggued in with "email" and "password" 
-   http://0.0.0.0:8000/api/token/

Copy the returned access token and set it in the Header in the parameter Authorization

Call the api
-   http://0.0.0.0:8000/api/market/?symbol=IBM

Logs will be show in:
-   request.info.log