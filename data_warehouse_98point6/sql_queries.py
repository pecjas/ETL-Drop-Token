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
    MERGE [dbo].players as T
    USING (VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)) as S(COL1,COL2,COL3,COL4,COL5,COL6,COL7,COL8,COL9,COL10)
    ON (T.id = COL1)
    WHEN MATCHED
        THEN UPDATE SET T.title_id = S.COL2,
                        T.name_first = S.COL3,
                        T.name_last = S.COL4,
                        T.email = S.COL5,
                        T.date_of_birth = S.COL6,
                        T.registration_time = S.COL7,
                        T.gender_id = S.COL8,
                        T.phone_main = S.COL9,
                        T.phone_cell = S.COL10
    WHEN NOT MATCHED BY TARGET
        THEN INSERT (id, title_id, name_first, name_last, email, date_of_birth, registration_time, gender_id,
                    phone_main, phone_cell)
            VALUES(COL1,COL2,COL3,COL4,COL5,COL6,COL7,COL8,COL9,COL10);
    ''')

    player_addresses_select = ('''
        SELECT player_id, street, city_id, state_id, postal_code, country_id
        FROM [dbo].player_addresses
    ''')

    player_addresses_insert = ('''
        MERGE [dbo].player_addresses as T
        USING (VALUES(?, ?, ?, ?, ?, ?)) as S(COL1,COL2,COL3,COL4,COL5,COL6)
        ON (T.player_id = COL1)
        WHEN MATCHED
            THEN UPDATE SET T.street = S.COL2,
                            T.city_id = S.COL3,
                            T.state_id = S.COL4,
                            T.postal_code = S.COL5,
                            T.country_id = S.COL6
        WHEN NOT MATCHED BY TARGET
            THEN INSERT (player_id, street, city_id, state_id, postal_code, country_id)
                VALUES(COL1,COL2,COL3,COL4,COL5,COL6);
    ''')

    player_logins_select = ('''
        SELECT player_id, username, salt, password_hashed
        FROM [dbo].player_logins
    ''')

    player_logins_insert = ('''
        MERGE [dbo].player_logins as T
        USING (VALUES(?, ?, ?, ?)) as S(COL1,COL2,COL3,COL4)
        ON (T.player_id = COL1)
        WHEN MATCHED
            THEN UPDATE SET T.username = S.COL2,
                            T.salt = S.COL3,
                            T.password_hashed = S.COL4
        WHEN NOT MATCHED BY TARGET
            THEN INSERT (player_id, username, salt, password_hashed)
                VALUES(COL1,COL2,COL3,COL4);
    ''')

    player_images_select = ('''
        SELECT player_id, thumbnail, medium, large
        FROM [dbo].player_images
    ''')

    player_images_insert = ('''
        MERGE [dbo].player_images as T
        USING (VALUES(?, ?, ?, ?)) as S(COL1,COL2,COL3,COL4)
        ON (T.player_id = COL1)
        WHEN MATCHED
            THEN UPDATE SET T.thumbnail = S.COL2,
                            T.medium = S.COL3,
                            T.large = S.COL4
        WHEN NOT MATCHED BY TARGET
            THEN INSERT (player_id, thumbnail, medium, large)
                VALUES(COL1,COL2,COL3,COL4);
    ''')

    game_data_select = ('''
        SELECT game_id, player_id, move_number, [column], result
        FROM [dbo].game_data
    ''')

    game_data_insert = ('''
        MERGE [dbo].game_data as T
        USING (VALUES(?, ?, ?, ?, ?)) as S(COL1, COL2, COL3, COL4, COL5)
        ON (T.game_id = S.COL1 AND T.move_number = COL3)
        WHEN MATCHED
            THEN UPDATE SET T.player_id = S.COL2,
                            T.[column] = S.COL4,
                            T.result = S.COL5
        WHEN NOT MATCHED BY TARGET
            THEN INSERT(game_id, player_id, move_number, [column], result)
                VALUES(COL1, COL2, COL3, COL4, COL5);
    ''')

    game_results_select = ('''
        SELECT id, value
        FROM [dbo].game_results
    ''')

    game_results_insert = ('''
        INSERT INTO [dbo].game_results (id, value)
        VALUES (?, ?)
    ''')
