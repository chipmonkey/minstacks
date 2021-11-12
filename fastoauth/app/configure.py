from dotenv import load_dotenv
import logging
import os

log = logging.getLogger()

envfile = '.env'
log.info(f"loading environment from {envfile}")
load_dotenv(envfile)

psql_host = os.environ['psql_host']
psql_port = os.environ['psql_port']
psql_username = os.environ['psql_username']
psql_password = os.environ['psql_password']
psql_dbname = 'fastoauth'
