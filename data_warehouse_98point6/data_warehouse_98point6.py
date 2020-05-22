import pyodbc
from menu import Menu
import data_warehouse_98point6.seed_database as seed_database

def start_application():
    menu = Menu(title="Select Execution Mode",
        options=[
        ("Update All Data", seed_database.seed),
        ("Request Failed Player Pages", seed_database.request_failed_player_pages),
        ("Exit Utility", Menu.CLOSE)
    ])

    menu.open()
