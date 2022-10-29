""" initial set up for Mystic Fate DB, modeled after bookstore from project 2
 """

import sqlite3
import os

db = os.path.join('database', 'fates.db')

class Fate:
    """ Represents one user 'fate'.
    This contains: (zodiac sign, tarot card, animal, horoscope)
    """

    def __init__(self, zodiac_sign, tarot_card, animal, horoscope):
        self.zodiac_sign = zodiac_sign
        self.tarot_card = tarot_card
        self.animal = animal
        self.horoscope = horoscope

        self.fate_store = FateStore()


    def save(self):
        """ Saves a generated user fate in the program. """
        self.fate_store._save_fate(self)

    def view_all_fates(self):
        """ View all the saved Fates in the program. """
        self.fate_store._get_all_fates(self)


class FateStore:

    def __init__(self):
        create_table_sql = 'CREATE TABLE IF NOT EXISTS fates (zodiac_sign text, tarot_card TEXT, animal TEXT, horoscope TEXT'
        conn = sqlite3.connect(db)
        with conn:
            conn.execute(create_table_sql)
        conn.close()


    def _save_fate(self, fate):
        """Adds fate to fate_store (DB)"""
        insert_sql = 'INSERT INTO fates (zodiac_sign, tarot_card, animal, horoscope) VALUES (?, ?, ?, ?)'
        with sqlite3.connect(db) as conn:
            conn.execute(insert_sql, (fate.zodiac_sign, fate.tarot_card, fate.animal, fate.horoscope) )
        conn.close()


    def _get_all_fates(self):
        """ Returns all fate objects stored in DB """
        get_all_fates_sql = 'SELECT rowid, * FROM fates'
        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(get_all_fates_sql)
        fates = []

        for r in rows:
            fate = Fate(r['zodiac_sign'], r['tarot_card'], r['animal'], r['horoscope'])
            fates.append(fate)
        conn.close()

        return fates