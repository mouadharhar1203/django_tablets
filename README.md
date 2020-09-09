# django_tablets
Django Postgres Docker Project


## Setup

build and up containers

```
docker-compose up
```

run migrations

```
docker-compose run web python3 manage.py migrate
```

create a user for admin

```
docker-compose run web python manage.py createsuperuser
```

#### features implemented:
A page containing 2 tables:
 * 1 table listing all the french tablets released between 2015 and 2020
 * 1 table listing all the others


