# Company Data Collection
A Django web application to collect the company meta data and list it down.

## Description
Created a project to collect the metadata about the company from the basic form and appending the data to the existing csv file and listing the data in the webpage.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### Setup
The first thing to do is to clone the repository:
```
$ git clone https://github.com/shrutiwd/treety.git
$ cd treety
```
Install the dependencies:
``` 
$ pip install -r requirements.txt
```
Once ```pip``` has finished downloading the dependencies:
```
$ python manage.py runserver
```
And navigate to ```http://127.0.0.1:8000/``` to enter the company data.

After submitting the data, it will redirect to the company details page ```http://127.0.0.1:8000/company-details/```.
From the company details page, there is a button to create a new company.
