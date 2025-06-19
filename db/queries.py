import psycopg2
from psycopg2.extras import RealDictCursor

# Config (move this to config.py later)
DB_CONFIG = {
    'dbname': 'mindpal_db',
    'user': 'ramzi',
    'password': 'password12345',
    'host': 'localhost',
    'port': '5432'
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def insert_user(username, name):
def fetch_user_by_username(connection, username):

def insert_challenge_result():
