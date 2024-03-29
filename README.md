# Prueba toteat

Prueba "La pikada de la esquina" de toteat

\*\* May take some time to load first time cause of heroku's dyno idling on free tier

**Not live anymore**

~~Live frontend: [https://prueba-toteat-front.herokuapp.com](https://prueba-toteat-front.herokuapp.com)~~

~~Live api docs: [https://prueba-toteat-api.herokuapp.com/docs](https://prueba-toteat-api.herokuapp.com/docs)~~

## Technologies

The backend api is built using fasapi as the main framework and tortoise-orm 
as the orm to interact with the postgres database.

The front is built using vue as the framework and axios to make the api calls.

The project is conteinarized for ease of use in 3 main containers:

 - frontend: to host the frontend applications
 - backend: to host the backend api
 - db: to host the postgre database

## Run development environment

To run for development you can run the following commands

To run the containers:
```bash
docker-compose up -d --build
```
To init-db:
```bash
docker-compose exec backend aerich upgrade
```
```bash
docker-compose exec backend aerich migrate
```
To populate db:
```bash
docker-compose exec db bash
```
Inside the bash terminal of the machine we execute the followeing

```bash
psql postgres://prueba_toteat:prueba_toteat@db:5432/prueba_toteat_dev < data/populate_db
```
And now we can exit the bash terminal with <CTL>+D

## Run production environment

Check readme on `main` branch for details.

## The models and api

There is only one model, Orders, with the following fields
```
Orders:
    id: CharField
    date_opened: DatetimeField
    date_closed: DatetimeField
    total: IntField
    cashier: CharField
    waiter: CharField
    zone: CharField
    table: IntField
    diners: SmallIntField
    products: JSONField
    payments: JSONField
```

The api generates it's own docs, that you can check at `localhost:5000/docs`.
It has the basic crud endponints 

 - GET `localhost:5000/orders`: returns the order instances paginated
   - `?page={page}`: indicates the page requested
   - `?size`: indicates the size of the page, aka the number of objects to get

 - GET `localhost:5000/order/{id}`: returns the order with the requested id or 
a 404 in case it doesn't exist.
 
 - POST `localhost:5000/orders`: creates a new order and returns it

 - POST `localhost:5000/order/{id}`: updates the order with the given id and 
returns it


## The frontend

Intended to create some graphs for the dashboard, but wasn't able to.

 - At `/` you enter the "dashboard" which has currently nothing on it
 - At `/orders` you get a list of orders with pagination
 - At `/order/{id}` you get the detail of an order

 ## The database

 A dataset was given for the test. I imported it into postgres converting it 
 to csv and the using `COPY` inside postgres. A script was made to facilitate 
 doing this in the future.
