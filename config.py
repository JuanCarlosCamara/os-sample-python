import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_HOST = '172.30.48.216'
DB_DATABASE = 'postgres'
DB_PORT = '5432'
