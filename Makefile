SHELL := /bin/bash

build:
	python3 -m venv venv
	. venv/bin/activate && pip3 install -r requirements.txt
	
migrations:
	. venv/bin/activate && python manage.py makemigrations
	. venv/bin/activate && python manage.py migrate

start:
	. venv/bin/activate && python manage.py runserver

vue_build:
	npm run --prefix vue_frontend/ dev

build_and_start:
	build
	migrations
	start

vue_dev:
	npm run --prefix vue_frontend/ dev

sass_compile:
	. venv/bin/activate && python manage.py sass zero_note/static/scss/style.scss zero_note/static/css/style.min.css --watch -t compressed
