#!/usr/bin/env bash
# build.sh
# Instala dependencias
pip install -r requirements.txt

# Aplica migraciones
python manage.py migrate

# Recolecta archivos estáticos
python manage.py collectstatic --noinput