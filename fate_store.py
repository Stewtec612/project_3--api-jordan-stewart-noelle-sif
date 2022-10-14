import sqlite3
import os

db = os.path.join('database', 'books.db')

class Fate:
    """ Represents one user 'fate'.
    This contains: (tarot card, animal, horoscope)
    """

    def __init__(self, tarot_card, animal, horoscope, id):
        self.tarot_card = tarot_card
        self.animal = animal
        self.horoscope = horoscope
        self.id = id

        self.fate_store = FateStore()


    def save(self):
        """ Saves a generated user fate in the program. """
        self.fate_store._add_fate(self)

    def delete(self):
        self.fate_store._delete_book(self)

    
class FateStore:

    instance = None  # what does this do?

    class __FateStore:

        def __init__(self):
            create_table_sql = 'CREATE TABLE IF NOT EXISTS fates (tarot TEXT, animal TEXT, horoscope TEXT'

            conn = sqlite3.connect(db)

            with conn:
                conn.execute(create_table_sql)

            conn.close()

        
        def _add_fate(self, fate):
            """Adds fate to fate_store (DB)"""

            insert_sql = 'INSERT INTO fates (tarot, animal, horoscope) VALUES (?, ?, ?)'

            try:
                with sqlite3.connect(db) as conn:
                    res = conn.execute(insert_sql, (fate.tarot, fate.animal, fate.horoscope) )
                    new_id = res.lastrowid # figure out a new id based on what the last row in table is
                    fate.id = new_id #set this fate's id

                    exception_error = False # TODO set to False (if no exception, fate successfully added)
                    return exception_error

            except sqlite3.IntegrityError as e:
                exception_error = True # set to True, code reaches the exception
                raise FateError(f'Error - this fate cannot be added.' {fate}) from e

            finally:
                conn.close()
                return exception_error

        
        def get_all_fates(self):
            """ Returns all fate objects stored in DB """
            get_all_fates_sql = 'SELECT rowid, * FROM fates'

            
            conn = sqlite3.connect(db)
            conn.row_factory = sqlite3.Row
            rows = conn.execute(get_all_fates_sql)
            fates = []

            for r in rows:
                fate = Fate(r['title'], r['author'], r['read'], r['rowid'])
                fates.append(fate)

            conn.close()            
            
            return fates


    def __new__(cls):
        """ The __new__ magic method handles object creation. (Compare to __init__ which initializes an object.) 
        If there's already a Bookstore instance, return that. If not, then create a new one
        This way, there can only ever be one __Bookstore, which uses the same database. """
        if not FateStore.instance:
            FateStore.instance = FateStore.__FateStore()
        return FateStore.instance


    def __getattr__(self, name):
        return getattr(self.instance, name)


    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)


    class FateError(Exception):
        """ For BookStore errors. """
        pass