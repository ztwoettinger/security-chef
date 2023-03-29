# Security Chef
This is a simple application designed to showcase a few security practices. Here are a few of the things you will find here...
* a docker-compose file that enables a deployment of MySQL with Wordpress
* a simple python application made with the Django web framework
* the yaml file for a Concourse pipeline for continuous integration
* simple unit tests designed to show the basic uses of pytest and pass into our Concourse pipeline

# Running locally
Setting up environment (run this first!)...
* pip install -r requirements.txt

Running django web server (navigate to http://localhost:8000/app after starting)...
* python ./mysite/manage.py runserver

Running unit tests (unit tests can be found at mysite/myapp/views.views.py)...
* ./run-tests.sh

Running Wordpress...
* cd wordpress
* docker-compose up
