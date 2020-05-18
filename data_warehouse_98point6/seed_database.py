import pyodbc
import requests
import json
import csv
from collections import namedtuple
from data_warehouse_98point6.db_connection import get_connection
from data_warehouse_98point6.models.players import Player
from data_warehouse_98point6.models.game_moves import GameMove

DATASOURCE = {
    'game_data': r"https://s3-us-west-2.amazonaws.com/98point6-homework-assets/game_data.csv",
    'players': r"https://x37sv76kth.execute-api.us-west-1.amazonaws.com/prod/users"
}

MAIN_TABLES = {
    'game_data': "[dbo].game_data",
    'players': "[dbo].players"
}

def seed() -> bool:
    connection = get_connection()
    seeded_successfully = True

    if not seed_players(connection):
        seeded_successfully = False
        print("Failed to seed players.")

    if not seed_game_data(connection):
        seeded_successfully = False
        print("Failed to seed game data")

    connection.close()
    return True

def seed_players(connection) -> bool:
    if database_has_data(connection, MAIN_TABLES["players"]):
        print(data_not_seeded_string("Player"))
        return

    try:
        retrieved_all_players = True
        page = 0
        while retrieved_all_players is True:
            response = requests.get(
                DATASOURCE['players'],
                params={'page': page}
            )
            if response.status_code != requests.codes.ok:
                return False

            players = response.json()
            if players == []:
                retrieved_all_players = False
            else:
                save_players_to_database(players, connection)
            
            page += 1

    except Exception as e:
        print(f"Exception: {e}")
        return False
    
    return True

def database_has_data(connection, table: str) -> bool:
    cursor = connection.cursor()
    cursor.execute(f"SELECT Count(*) as 'count' FROM {table}")

    return cursor.fetchval() > 0

def data_not_seeded_string(data_type) -> str:
    return f"{data_type} data not seeded because data already exists in the table."

def save_players_to_database(players, connection):
    cursor = connection.cursor()

    for player in players:
        player_obj = Player(player['id'])

        player_obj.set_trusted_data(
            name_first=player['data']['name']['first'],
            name_last=player['data']['name']['last'],
            street=player['data']['location']['street'], #TODO: Potentially split this
            email=player['data']['email'],
            username=player['data']['login']['username'],
            salt=player['data']['login']['salt'],
            pass_hashed=player['data']['login']['sha256'],
            thumbnail=player['data']['picture']['thumbnail'],
            img_med=player['data']['picture']['medium'],
            img_large=player['data']['picture']['large']
        )

        player_obj.normalize_and_set_basic_tracked_strings({
            'gender': player['data']['gender'],
            'title': player['data']['name']['title'],
            'city': player['data']['location']['city'],
            'state': player['data']['location']['state'],
        }, cursor)

        player_obj.normalize_and_set_postal_code(player['data']['location']['postcode'])

        player_obj.normalize_and_set_dob(player['data']['dob'])
        player_obj.normalize_and_set_registration(player['data']['registered'])

        player_obj.normalize_and_set_phone_number(player['data']['phone'], 'phone_main', player['data']['nat'])
        player_obj.normalize_and_set_phone_number(player['data']['cell'], 'phone_cell', player['data']['nat'])

        player_obj.set_internal_id(player['data']['id']['name'], player['data']['id']['value'])
        player_obj.normalize_and_set_nationality(player['data']['nat'], cursor)

        player_obj.add_player_info_to_cursor(cursor)
    
    connection.commit()
    cursor.close()
            

def seed_game_data(connection):
    if database_has_data(connection, MAIN_TABLES["game_data"]):
        print(data_not_seeded_string("Game"))
        return False

    try:
        response = requests.get(DATASOURCE['game_data'],)
        if response.status_code != requests.codes.ok:
            return False

        save_game_to_database(response.content.decode('UTF-8'), connection)

    except Exception as e:
        print(f"Exception: {e}")
        return False

    return True

def save_game_to_database(csv_data, connection):
    cursor = connection.cursor()
    csvreader = csv.reader(csv_data.splitlines())
    next(csvreader)

    rowcount = 0
    for row in csvreader:
        game_move = GameMove(row[0])

        game_move.set_trusted_data(
            player_id=row[1],
            move_number=row[2],
            column=row[3]
        )

        game_move.set_results(row[4], cursor)
        game_move.add_game_move_info_to_cursor(cursor)

        rowcount += 1
        if rowcount % 25 == 0:
            connection.commit()

    connection.commit()
    cursor.close()
