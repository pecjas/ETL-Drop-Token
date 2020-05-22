from collections import namedtuple
import datetime
import dateutil.parser as dateparser
import phonenumbers
import pycountry
from data_warehouse_98point6.sql_queries import SqlQueries

class Player():
    gender_values = list()
    title_values = list()
    city_values = list()
    state_values = list()
    country_values = list()

    date_formats = {
        'dob': "%Y-%m-%d",
        'registration': "%Y-%m-%d %H:%M:%S"
    }

    def __init__(self, player_id:int):
        self.id = player_id

    def set_trusted_data(self, *, name_first, name_last, street, email, username, salt, pass_hashed, thumbnail, img_med, img_large):
        self.name_first = name_first
        self.name_last = name_last

        self.street = street

        self.email = email
        self.username = username
        self.salt = salt
        self.pass_hashed = pass_hashed

        self.thumbnail = thumbnail
        self.img_med = img_med
        self.img_large = img_large
    
    def normalize_and_set_basic_tracked_strings(self, att_to_value:dict, cursor):
        for key, value in att_to_value.items():
            value = value.lower()
            setattr(self, key, Player._get_class_index(f"{key}_values", value, cursor))

    @classmethod
    def _get_class_index(cls, cls_attr, value, cursor):
        try:
            i = getattr(cls, cls_attr).index(value)

        except ValueError:
            getattr(cls, cls_attr).append(value)
            i = len(getattr(cls, cls_attr))-1
            
            cursor.execute(Player.get_sql_command_to_update_tracked_string(cls_attr), i, value)

        return i

    @classmethod
    def get_sql_command_to_update_tracked_string(cls, cls_attr):
        return getattr(SqlQueries, f"{cls_attr}_insert".lower())

    def normalize_and_set_postal_code(self, postal_code:int):
        self.postal_code = str(postal_code)

    def normalize_and_set_dob(self, value:str):
        dob = dateparser.parse(value)
        self.dob = dob.strftime(Player.date_formats.get('dob'))

    def normalize_and_set_registration(self, value:str):
        registration = dateparser.parse(value)
        self.registration = registration.strftime(Player.date_formats.get('registration'))

    def normalize_and_set_phone_number(self, number:str, phone_type:str, nation:str = None):
        try:
            number = phonenumbers.parse(number, nation)
            setattr(
                self,
                phone_type,
                phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164))

        except phonenumbers.NumberParseException:
            setattr(self, phone_type, None)

    def normalize_and_set_nationality(self, nationality, cursor):
        country = pycountry.countries.lookup(nationality).alpha_2
        self.country = Player._get_class_index("country_values", country, cursor)

    def add_player_info_to_cursor(self, cursor):
        cursor.execute(
            SqlQueries.player_insert,
            self.id,
            self.title,
            self.name_first,
            self.name_last,
            self.email,
            self.dob,
            self.registration,
            self.gender,
            self.phone_main,
            self.phone_cell
        )

        cursor.execute(
            SqlQueries.player_addresses_insert,
            self.id,
            self.street,
            self.city,
            self.state,
            self.postal_code,
            self.country
        )

        cursor.execute(
            SqlQueries.player_logins_insert,
            self.id,
            self.username,
            self.salt,
            self.pass_hashed
        )

        cursor.execute(
            SqlQueries.player_images_insert,
            self.id,
            self.thumbnail,
            self.img_med,
            self.img_large
        )
    
    def add_player_info_to_dict(self, sql_data):
        sql_data.get('player').append(
            (self.id,
            self.title,
            self.name_first,
            self.name_last,
            self.email,
            self.dob,
            self.registration,
            self.gender,
            self.phone_main,
            self.phone_cell)
        )

        sql_data.get('address').append(
            (self.id,
            self.street,
            self.city,
            self.state,
            self.postal_code,
            self.country)
        )

        sql_data.get('logins').append(
            (self.id,
            self.username,
            self.salt,
            self.pass_hashed)
        )

        sql_data.get('images').append(
            (self.id,
            self.thumbnail,
            self.img_med,
            self.img_large)
        )
