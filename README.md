

[![Build Status](https://travis-ci.org/fatukunda/Store-Manager.svg?branch=feature)](https://travis-ci.org/fatukunda/Store-Manager)
[![codecov](https://codecov.io/gh/fatukunda/Store-Manager/branch/feature/graph/badge.svg)](https://codecov.io/gh/fatukunda/Store-Manager)
[![Maintainability](https://api.codeclimate.com/v1/badges/4e9097febebbc2747c2a/maintainability)](https://codeclimate.com/github/fatukunda/Store-Manager/maintainability)

# Store-Manager App

Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. View the application [here](https://fatukunda.github.io/Store-Manager/UI/)

## How to login
 - As a store owner ```username: admin``` and ```password: admin```
 - As a store attendant ```username: user``` and ```password: user```

## The API
### Features
```Admin```
 - Can add a new product
 - Can view a list of all sales made by the attendants
 
 ```Attendant```
 - Can make a sale
 - Can view sales made by him/her
 - Can view a single sale made by him/her
 
The API is hosted on [heroku](https://store-manager-api-heroku.herokuapp.com) and below are the endpoints. Remember to include ```api/v1``` at the end of the heroku url otherwise you will get a page not found error

| Endpoint                        | Functionality       | Notes                           |
| --------------------------------|---------------------|---------------------------------|
| GET /api/v1/products|Fetch all products |Get all available products|
| GET /api/v1/products/id | Fetch a single product record |Get a specific product using the product’s id|
| GET /api/v1/admin/sales|Fetch all sale records|Get all sale records. This endpoint should be accessible to only the store owner/admin|
| POST /api/v1/admin/products | Create a single product | Create a new product record. This endpoint should be accessible to only the store owner/admin.
| GET /api/v1/admin/sales/id |Fetch a single sales record |Get a specific sale record using the sale record Id. This endpoint is accessible to only the store owner/admin |
| GET /api/v1/attendants/username/sales | Get all the sales by a single attendant | Get all sales made by a single attendant. This endpoint is accessible only by the attendant who made the sales|
| Get /api/v1/attendants/username/sales/id | Fetch a single sale item by a specific attendant | Get a single sale made by a specific attendant. This endpoint is only accessible by the attendant who made the sale |
|POST /api/v1/attendants/sales | create a single sales | This endpoint is accessed by only attendants to make sales |


### Prerequisites

 - Python 3.6 or higher
 - Flask 1.0.2 or higher
 - Pytest for running tests
 - Your favorite text editor

### Installing

 ```git clone https://github.com/fatukunda/Store-Manager.git```


## Running the tests

- Run pytest

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Pytest](https://docs.pytest.org/en/latest/) - Test suite used
* [Python](https://www.python.org/) - The development language


## Authors

* **Frank Atukunda** - *Initial work* - [Linkedin](https://www.linkedin.com/in/frank-atukunda/)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## Acknowledgments

* [Andela Uganda](https://andela.com/insights/welcoming-uganda-andela-family/)
* ```This project is part of the Andela bootcamp challenge```


