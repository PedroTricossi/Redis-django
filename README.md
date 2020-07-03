# Redis-django
This project was created in order to continue my studies in APIrest.

To make it real I decided to create a very simple stock system, the client can add and update products using the admin interface. The endpoint return the product (with price, descriptions, etc)
for some frontend application consume it. As a way of making it faster i decide to make it use redis as a cache store(in this application the difference is very little, however it can 
easily start making huge difference if it grows).

You can se the difference here:

## Time response without redis

![Alt text](./images/APIsem.png?raw=true "without")

## Time response with redis

![Alt text](./images/APIsem.png?raw=true "with")

## Technologies used
To build this project I have used:
Django and its API lib Rest_framework.

SQLite3 as DB.

Redis to store cache.
