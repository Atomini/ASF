from pathlib import Path
import sqlite3 as sql


class Model:

    def __init__(self):
        way_to_db = Path(__file__).parent / 'flange.db'
        print(way_to_db)
        self.conn = sql.connect(way_to_db)

    def select_from_db(self, *args):
        """Выбираем из БД данние"""
        gost, pressure, Dy, flange_type, answer_flange, number, pipe_length, pipe, name = args[0]
        print(pressure)
        if gost == "12820 (плоский)":
            flange = self.get_flange_value_from_db(pressure, Dy, "flange_12820")
            # print(flange) # for test
        elif gost == "12821 (сапожковый)":
            flange = self.get_flange_value_from_db(pressure, Dy, "flange_12821")
            # print(flange) # for test

    def select_recomend_pipe(self, pipes) -> str:
        """Получает из БД размер трубы по Ду"""
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(f"""SELECT size FROM pipe WHERE Dy = {pipes}""")
            pipe = cur.fetchone()
        return pipe[0]

    def get_flange_value_from_db(self, pressure, Dy, table):
        """Получем из БД размеры для фланца 12820
        в table нередается имя таблици flange_12820 или flange_12821"""
        pressure_convert = {"0,1-0,25 МПа": 0.25, "0,6 МПа": 0.6, "1,0 МПа": 1.0, "1,6 МПа": 1.6, "2,5 МПа": 2.5}
        pressure_float = pressure_convert.get(pressure)
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(f"""SELECT * FROM flange JOIN {table} f on flange.Dy = f.Dy 
                        and flange.pressure = f.pressure WHERE f.Dy = {Dy} AND f.pressure = {pressure_float} """)
            flange = cur.fetchall()
            return flange[0]




if __name__ == '__main__':
    mod = Model()
    mod.get_flange_value_from_db(1.0, 50, "flange_12821")