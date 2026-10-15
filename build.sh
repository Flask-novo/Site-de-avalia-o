#!/usr/bin/env bash
# Sair imediatamente se ocorrer um erro
set -o errexit

# 1. Instalar as dependências do Python
pip install -r requirements.txt

# 2. Juntar todos os arquivos estáticos (CSS, etc) numa pasta só para o Render ler
python manage.py collectstatic --no-input

# 3. Aplicar as configurações do banco de dados (SQLite)
python manage.py migrate