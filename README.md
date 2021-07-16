# Restaurant
Restaurant API for reservation and create table for restaurant

# Requirments
1. Python 3: https://www.python.org/downloads/
2. Postgres DB: https://www.postgresql.org/download/
3. PgAdmin: https://www.pgadmin.org/download/

# Getting Started
1. Clone the Project: https://github.com/Hamza-abughazaleh/Restaurant.git
2. Create Python Enviroment:
   - Open Terminal
   - sudo apt install virtualenv
   - virtualenv "env name" --python=/usr/bin/python3
3. Activate Your Enviroment:
   - Open Terminal
   - source "env name"/bin/activate
4. Go to project Directory and Install requirements file by Terminal: pip install -r requirements.txt
5. Create Your DB from pgadmin
6. Go to settings.py and edit this code:
   ```python
   - DATABASES = {
    	'default': {
       		'ENGINE': 'django.db.backends.postgresql_psycopg2',
       		'NAME': 'restaurants', #add your db name you created
       		'USER': 'postgres', #add your db authentication
       		'PASSWORD': 'postgres',
       		'HOST': '127.0.0.1',
       		'PORT': '5432',
    		}
   	}
7. Go to project Directory and do this Commands by Terminal: 
   - python manage.py makemigrations
   - python manage.py createsuperuser #to create super user (admin)
   - python manage.py runserver

8. if you Need to Access All Api:
   - Login as Super User (Admin)

9. Go to localhost:8000/api-v1/

# What's included
1. Django 3.2.5: https://docs.djangoproject.com/en/3.2/
2. Django Rest Framework 3.12.4: https://www.django-rest-framework.org/
3. Django Rest Framework Simplejwt 4.7.2: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

