# Online-Schedule-Maker
##(This Project used Heroku Django Starter Template and Google sheet)
This Online-Schedule-Maker allow employees and department manager to fill in and collect work schedules online for next quarter efficiently. I wrote three functions "Get Dates", "Get Summaries", "Clear Sheets" in javascript. "Get Dates" allows manger to get new dates for the next quarter. "Get Summaries" allows manger to get a list of each class's name and its corresponding date and total number of classes each instructor will deliver for the next quarter. "Clear Sheets" will clear the contents and sheets. 
## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
