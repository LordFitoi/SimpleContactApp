SHELL := /bin/bash

build:
	python3 -m venv venv
	. venv/bin/activate && pip3 install -r requirements.txt
	
migrations:
	. venv/bin/activate && python manage.py makemigrations
	. venv/bin/activate && python manage.py migrate

start:
	. venv/bin/activate && python manage.py runserver

build_and_start: build migrations start

vue_dev:
	npm run --prefix vue_frontend/ dev 