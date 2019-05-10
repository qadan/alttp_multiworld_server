'''
Hangs onto a database connection, provides functionality.
'''
class db:
    db = None;

    def __init__(self, db_source):
        db = sqlite.connect(db_source)

    def get_db(self):
        return db

    def query_db(self, query, args=(), one=True):
        cur = self.db.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv
