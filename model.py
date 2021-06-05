from pathlib import Path
import sqlite3 as sql


class Model:

    def __init__(self):
        way_to_db = Path(__file__).parent / 'flange.db'
        print(way_to_db)
        self.conn = sql.connect(way_to_db)

    def select_from_db(self, *args):
        print(*args)

    def select_recomend_pipe(self, pipes) -> str:
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(f"""SELECT size FROM pipe WHERE Dy = {pipes}""")
            pipe = cur.fetchone()
        return pipe[0]
