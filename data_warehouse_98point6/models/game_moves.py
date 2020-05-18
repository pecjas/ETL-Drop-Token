from data_warehouse_98point6.sql_queries import SqlQueries

class GameMove():
    result_values = list()

    def __init__(self, id):
        self.game_id = id

    def set_trusted_data(self, *, player_id, move_number, column):
        self.player_id = player_id
        self.move_number = move_number
        self.column = column

    def set_results(self, result, cursor):
        if result == "":
            result = None

        try:
            i = GameMove.result_values.index(result)
        except ValueError:
            GameMove.result_values.append(result)
            i = len(GameMove.result_values)-1
            
            cursor.execute(self.get_sql_command_to_update_results(), i, result)

        self.result = i

    def get_sql_command_to_update_results(self):
        return SqlQueries.game_results_insert

    def add_game_move_info_to_cursor(self, cursor):
        cursor.execute(
            SqlQueries.game_data_insert,
            self.game_id,
            self.player_id,
            self.move_number,
            self.column,
            self.result
        )
