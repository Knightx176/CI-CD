from flask import Flask, request, render_template, redirect, url_for
import pymysql
import os
app = Flask(__name__)

#Retreiving the DB credentials
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
db = os.environ.get("DB")

# Database configuration
db_config = {
    'host': 'mysql-service',  # The name of your MySQL service in Kubernetes
    'user': username,
    'password': password,
    'db': db
}

# Initialize database connection
def get_db_connection():
    return