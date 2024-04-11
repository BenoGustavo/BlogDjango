#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

wait_psql.sh
makemigrations.sh
migrate.sh
collectstatic.sh
runserver.sh