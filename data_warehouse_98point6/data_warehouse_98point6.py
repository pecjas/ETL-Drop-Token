import time
import pyodbc
import data_warehouse_98point6.seed_database as seed_database

def prompt_for_action():
    pass

def start_application():
    if seed_database.seed():
        input("Database has been seeded. Press any key to quit.")
    else:
        input("An error was encounter while attempting to seed the database.")
