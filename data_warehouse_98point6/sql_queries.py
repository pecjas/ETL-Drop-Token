class SqlQueries():
    title_values_select = ('''
        SELECT id, value
        FROM [dbo].player_titles
    ''')

    title_values_insert = ('''
        INSERT INTO [dbo].player_titles (id, value)
        VALUES (?, ?)
    ''')

    gender_values_select = ('''
        SELECT id, value
        FROM [dbo].player_genders
    ''')

    gender_values_insert = ('''
        INSERT INTO [dbo].player_genders (id, value)
        VALUES (?, ?)
    ''')

    city_values_select = ('''
        SELECT id, value
        FROM [dbo].player_cities
    ''')

    city_values_insert = ('''
        INSERT INTO [dbo].player_cities (id, value)
        VALUES (?, ?)
    ''')

    state_values_select = ('''
        SELECT id, value
        FROM [dbo].player_states
    ''')

    state_values_insert = ('''
        INSERT INTO [dbo].player_states (id, value)
        VALUES (?, ?)
    ''')

    country_values_select = ('''
        SELECT id, value
        FROM [dbo].player_countries
    ''')

    country_values_insert = ('''
        INSERT INTO [dbo].player_countries (id, value)
        VALUES (?, ?)
    ''')

    player_select = ('''
        SELECT id, title_id, name_first, name_last, email, date_of_birth, registration_time, gender_id,
        phone_main, phone_cell
        FROM [dbo].players
    ''')

    player_insert = ('''
        INSERT INTO [dbo].players (id, title_id, name_first, name_last, email, date_of_birth, registration_time, gender_id,
        phone_main, phone_cell)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''')

    player_addresses_select = ('''
        SELECT player_id, street, city_id, state_id, postal_code, country_id
        FROM [dbo].player_addresses
    ''')

    player_addresses_insert = ('''
        INSERT INTO [dbo].player_addresses (player_id, street, city_id, state_id, postal_code, country_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''')

    player_logins_select = ('''
        SELECT player_id, username, salt, password_hashed
        FROM [dbo].player_logins
    ''')

    player_logins_insert = ('''
        INSERT INTO [dbo].player_logins (player_id, username, salt, password_hashed)
        VALUES (?, ?, ?, ?)
    ''')

    player_internal_ids_select = ('''
        SELECT player_id, internal_id_name, internal_id_value
        FROM [dbo].player_internal_ids
    ''')

    player_internal_ids_insert = ('''
        INSERT INTO [dbo].player_internal_ids (player_id, internal_id_name, internal_id_value)
        VALUES (?, ?, ?)
    ''')

    player_images_select = ('''
        SELECT player_id, thumbnail, medium, large
        FROM [dbo].player_images
    ''')

    player_images_insert = ('''
        INSERT INTO [dbo].player_images (player_id, thumbnail, medium, large)
        VALUES (?, ?, ?, ?)
    ''')

    game_data_select = ('''
        SELECT game_id, player_id, move_number, [column], result
        FROM [dbo].game_data
    ''')

    game_data_insert = ('''
        INSERT INTO [dbo].game_data (game_id, player_id, move_number, [column], result)
        VALUES (?, ?, ?, ?, ?)
    ''')

    game_results_select = ('''
        SELECT id, value
        FROM [dbo].game_results
    ''')

    game_results_insert = ('''
        INSERT INTO [dbo].game_results (id, value)
        VALUES (?, ?)
    ''')
