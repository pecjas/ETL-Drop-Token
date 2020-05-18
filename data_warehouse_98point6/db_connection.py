import pyodbc
import configparser
import os

def get_connection():
    config = configparser.ConfigParser()
    config.read(get_config_file_location())

    return pyodbc.connect(
        f"Driver={{{config['CONNECTION']['Driver']}}};"
        f"Server={config['CONNECTION']['Server']};"
        f"Database={config['CONNECTION']['Database']};"
        "Trusted_connection=yes;"
    )

def get_config_file_location():
    base_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    return os.path.join(base_directory, "config", "db_connection.ini")
