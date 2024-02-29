# Django and MongoDB example

## About

A very simple example of django and MongoDB implementation.
I must say django is not maybe a correct example for this
since we will not have use of **django ORM**, **django Admin**, etc.

Then seems like django is not fully used and maybe this is more a good option for some
microservice - maybe with FastAPI, Flask or any other small framework.

Why I did this?

I was just curious!

Of course this could be a nice use case for storing some data, besides some relation DB
that integrates with django.

In this example for communicating to MongoDB I used [PyMongo](https://pypi.org/project/pymongo/) package.

## Requirements

1. Python 3.11+
2. Poetry

## How

1. Install requirements:
    ```shell
    poetry install
    ```
2. Create .env file in root of your project (same level as manage.py)
3. Update .env with your values (check .env.example file)
4. Run server

## Be free to contact me if you have any questions!
