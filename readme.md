## Overview

This is a sample REST Django Application that makes calls to the Microsoft Graph API (https://developer.microsoft.com/en-us/graph)


## Reference

Much of the code was based off of this github repo: https://github.com/jasonjoh/pythoncontacts

For deployment to Azure most of the information was pulled from here: https://docs.microsoft.com/en-us/azure/app-service/web-sites-python-configure

## Configuration

Following are the steps that you need to complete in order to see this application working:
- in the Azure  Portal (https://portal.azure.com):
  - go to Azure Active Directory (AAD)
  - create a new AAD web application
  - copy the web application's **Client Id** and **Secret Key** 
  - grant the application the following permissions:
    - Windows Azure Active Directory
      - Sign in and read user profile
    - Microsoft Graph
      - Access directory as the signed in user
      - Read all groups
- Create a Group in the AAD and copy the **Id**
- Add Users you want to give access to that group
- clone this repo
- in the **clientreg.py** file paste the  web application's **Client Id** and **Secret Key** 
- in the **views.py** file paste the groups's **Id** into the code 
- 

- in the command line:
```
$ virtualenv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```
- in your web browser navigate to http://127.0.0.1:8000/
- You can now call the 2 endpoints:

## Endpoints

There are 2 endpoints 

/echo/
- GET
    - Response: Json message that you are hitting the Echo API
- PUT
    - Response: Json message echoing back what was in the body of the Request

/access/
- GET
    - Response: Json message with Repsonse field of either true or false that indicate whether or not you have access to the application (i.e. whether or not the user who is signed in is in the group you set up)
    - If not Auth token is supplied it will respond with a 401
* This endpoint is expecting a token for the Graph API 
