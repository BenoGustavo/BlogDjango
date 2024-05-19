
# Projeto Django Blog

This is a Django project that uses Docker for creating a development environment.

## Project Structure

The project directory structure is as follows:

```
.
├── .dockerignore
├── .gitignore
├── data/
│   ├── postgres/
│   │   └── data/
│   └── web/
│       ├── media/
│       └── static/
├── djangoapp/
│   ├── blog/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── static/
│   │   ├── templates/
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── manage.py
│   ├── project/
│   ├── requirements.txt
│   └── site_setup/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── context_processor.py
│       ├── migrations/
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── docker-compose.yml
├── Dockerfile
├── dotenv_files/
│   ├── .env
│   └── .env-example
├── README.md
├── scripts/
│   ├── collectstatic.sh
│   ├── commands.sh
│   ├── makemigrations.sh
│   ├── migrate.sh
│   ├── runserver.sh
│   └── wait_psql.sh
└── venv/
```

## How to Run the Project

1. First, make sure Docker and Docker Compose are installed on your machine.

2. Clone the repository to your local machine.

3. Navigate to the project directory.

4. Create a `.env` file in the [`dotenv_files/`](dotenv_files/) folder based on the provided `.env-example` file.

5. Run the following command to build and start the containers:

```sh
docker-compose up --build
```

6. The Django application will be available at `localhost:8000`.

To access the <b>admin interface</b>, you will need to create a superuser. Here's how you can do it:

7. Run the following command in your terminal:

```sh
python manage.py createsuperuser
```

## Scripts

There are several scripts in the [`scripts/`](scripts/) folder that can be useful during development:

- `collectstatic.sh`: Collects static files to the `static/` folder.
- `commands.sh`: Executes Django commands.
- `makemigrations.sh`: Creates new migrations based on the changes you made to the models.
- `migrate.sh`: Applies the migrations.
- `runserver.sh`: Starts the Django development server.
- `wait_psql.sh`: Waits until PostgreSQL is ready to accept connections.

Here's what they do:

- [`collectstatic.sh`](command:_github.copilot.openSymbolInFile?%5B%22scripts%2Fcollectstatic.sh%22%2C%22collectstatic.sh%22%5D "scripts/collectstatic.sh"): This script collects static files to the `static/` folder. It's useful when you want to gather all your static files in one place for production.

- [`commands.sh`](command:_github.copilot.openSymbolInFile?%5B%22scripts%2Fcommands.sh%22%2C%22commands.sh%22%5D "scripts/commands.sh"): This script executes several Django commands in sequence. It waits for PostgreSQL to be ready, makes migrations, applies them, collects static files, and then starts the Django development server.

- [`makemigrations.sh`](command:_github.copilot.openSymbolInFile?%5B%22scripts%2Fmakemigrations.sh%22%2C%22makemigrations.sh%22%5D "scripts/makemigrations.sh"): This script creates new migrations based on the changes you made to your models. It's useful when you've made changes to your Django models and need to create migrations for them.

- [`migrate.sh`](command:_github.copilot.openSymbolInFile?%5B%22scripts%2Fmigrate.sh%22%2C%22migrate.sh%22%5D "scripts/migrate.sh"): This script applies the migrations. It's useful when you want to apply the migrations you've created to your database.

- [`runserver.sh`](command:_github.copilot.openSymbolInFile?%5B%22scripts%2Frunserver.sh%22%2C%22runserver.sh%22%5D "scripts/runserver.sh"): This script starts the Django development server. It's useful when you want to start your Django application.

- [`wait_psql.sh`](command:_github.copilot.openSymbolInFile?%5B%22scripts%2Fwait_psql.sh%22%2C%22wait_psql.sh%22%5D "scripts/wait_psql.sh"): This script waits until PostgreSQL is ready to accept connections. It's useful when you want to ensure that PostgreSQL is ready before executing other commands that depend on it.

All these scripts are executed at once if you don't specify what to execute. This is done by the [``commands.sh``](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fgustavo%2Fdev_workspace%2FBlogDjango%2Fscripts%2Fcommands.sh%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/gustavo/dev_workspace/BlogDjango/scripts/commands.sh") script.