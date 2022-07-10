# Prueba toteat

Prueba "La pikada de la esquina" de toteat

\*\* May take some time to load first time cause of heroku's dyno idling on free tier

Live frontend: [https://prueba-toteat-front.herokuapp.com](https://prueba-toteat-front.herokuapp.com)

Live api docs: [https://prueba-toteat-api.herokuapp.com/docs](https://prueba-toteat-api.herokuapp.com/docs)

## Technologies

The backend api is built using fasapi as the main framework and tortoise-orm 
as the orm to interact with the postgres database.

The front is built using vue as the framework and axios to make the api calls.

The project is conteinarized for ease of use in 3 main containers:

 - frontend: to host the frontend applications
 - backend: to host the backend api
 - db: to host the postgre database

## Deploy to heroku

To deploy to heroku, create 2 apps one for the frontend, and one for the backend.

The frontend app and the backend app are containerized and can be pushed easily 
to heroku.

First you have to download the heroku cli and log in using `heroku login`, then 
login into container with `heroku container:login` and push each app to the it's 
respective heroku app. Finally, release each app.

```bash
cd services/backend
heroku container:push web -a <heroku-backend-app-name>
heroku container:release web -a <heroku-backend-app-name>
```

```bash
cd services/frontend
heroku container:push web -a <heroku-frontend-app-name>
heroku container:release web -a <heroku-frontend-app-name>
```
The frontend app `Dockerfile` exports `VUE_APP_API_URL` as an env variable, 
you should change this to be the url of the backend api app.

The backend app `Dockerfile` exports `FRONTEND_URL` as an env variable, you 
should change this to be the url of the frontend app.


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
