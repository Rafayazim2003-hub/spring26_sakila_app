# Name: Rafay Azim
# Date: 2026-04-24
# Purpose: Combined config after merge conflict resolution
import os

class Config:
    "Configuration class including database, timeout, and health check settings"
    
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey123')
    
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))