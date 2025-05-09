dev-start:
	python manage.py runserver --noreload --settings=config.settings.dev

dev-install:
	pip install -r requirements/dev.txt

dev-showmigrations:
	python manage.py showmigrations --settings=config.settings.dev

dev-makemigrations:
	python manage.py makemigrations --settings=config.settings.dev

dev-makemigrations-app:
	python manage.py makemigrations $(app) --settings=config.settings.dev

dev-migrate:
	python manage.py migrate --settings=config.settings.dev

dev-createsuperuser:
	python manage.py createsuperuser --settings=config.settings.dev

dev-migrate2:
	python manage.py migrate $(app) $(m) --settings=config.settings.dev

dev-sqlmigrate:
	python manage.py sqlmigrate $(app) $(m) --settings=config.settings.dev

dev-shell:
	python manage.py shell --settings=config.settings.dev

dev-test:
	python manage.py test $(route) --settings=config.settings.dev

dev-dumpdata:
	python manage.py dumpdata -a --settings=config.settings.dev --indent=4 > data.json