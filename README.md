# Django custom users example

## Tech Stack

- Programming Language: [Python](https://www.python.org/)

- Dependency Manager: [uv](https://docs.astral.sh/uv/)

- Lint & Formatting: [ruff](https://docs.astral.sh/ruff/)

- Web Framework: [Django](https://www.djangoproject.com/)

## Usage

```sh
cp example.env .env
uv sync
cd src
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 
```
