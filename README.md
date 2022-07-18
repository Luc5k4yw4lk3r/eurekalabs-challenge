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

Open the browser or postman with the following url:

Create an user account
-   http://0.0.0.0:8000/api/signup/

Loggin with "email" and "password" 
-   http://0.0.0.0:8000/api/token/

Copy the returned access token and set it in the Header in the parameter Authorization
-   Bearer \<access_token\>

Call the api
-   http://0.0.0.0:8000/api/market/?symbol=IBM

Logs will be show in:
-   request.info.log