# Test Task
#### Creator: Muhammad Umair Sabir
#### Overview
This is just a small RESTful API, available via HTTP shopping basket 

#### Available Endpoints

## For Products
* POST /Products/ To add new product
* PUT /Products/ To update a product
* GET /Products/ To get all products
* GET /Products/{id} To get product by id
* DELETE /Products/{id}  To delete product by id

## For Basket
* POST /Basket/ To add new item in basket
* PUT /Basket/ To update a basket item
* GET /Basket/ To get all basket items
* GET /Basket/{id} To get basket item by id
* GET /Basket/userid/{id} To get basket item for specific user
* DELETE /Basket/{id}  To delete item by id

#### Tools used:
1) Flask
2) Docker
3) Mariadb

#### How to run:
  * Make sure you have python and Docker installed.
  1) clone this repo 
  2) run dokcer-compose build
  3) run docker-compose up -d (to start the services)
  4) run docker-compose down (to stop the services)
  4) run pytest test_api.py (to run the tests)
