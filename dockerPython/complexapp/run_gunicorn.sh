# gunicorn --bind=127.0.0.1:8001 app:server --daemon # This one doesn't actually work
gunicorn --bind=127.0.0.1:8002 app2:server --daemon
gunicorn --bind=127.0.0.1:8003 basicapp:server --daemon
