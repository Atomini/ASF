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
        # конвертируем строку в float
        pressure_convert = {"0,1-0,25 МПа": 0.25, "0,6 МПа": 0.6, "1,0 МПа": 1.0, "1,6 МПа": 1.6, "2,5 МПа": 2.5}
        pressure_float = pressure_convert.get(pressure)

        if gost == "12820 (плоский)":
            flange = self.get_flange_value_from_db(pressure_float, Dy, "flange_12820")
        elif gost == "12821 (сапожковый)":
            flange = self.get_flange_value_from_db(pressure_float, Dy, "flange_12821")
        gasket = self.get_gasket_from_db(Dy, pressure_float, flange_type)
        bolt = flange[12]
        pin = self.get_metiz(bolt=bolt)
        flange_answer = self.get_answer_flange(Dy, pressure_float, answer_flange, flange_type)



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
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(f"""SELECT * FROM flange JOIN {table} f on flange.Dy = f.Dy and flange.pressure = f.pressure 
                            WHERE flange.Dy = {Dy} AND flange.pressure = {pressure}""")
            flange = cur.fetchall()
            return flange[0]

    def get_gasket_from_db(self, Dy, pressure, flange_type):

        if flange_type == 1:
            index = 0
        else:
            index = 1

        with self.conn:
            cur = self.conn.cursor()
            cur.execute(f"""SELECT * FROM gasket WHERE Dy = {Dy} AND pressure = {pressure}""")
            gasket = cur.fetchall()
            return gasket[index]

    def get_metiz(self, bolt):

        with self.conn:
            cur = self.conn.cursor()
            cur.execute("""SELECT thickness FROM nut WHERE bolt = ? """, (bolt,))
            nut = cur.fetchall()
            cur.execute("""SELECT min_length FROM pin WHERE bolt = ? """, (bolt,))
            pin = cur.fetchall()
            cur.execute("""SELECT thickness FROM washer WHERE bolt = ? """, (bolt,))
            washer = cur.fetchall()
            return nut[0][0], pin[0][0], washer[0][0]

    def get_answer_flange(self, Dy, pressure_float, answer_flange, flange_type):

        if answer_flange == "Нет":
            return "-", "-", "-", "-"

        elif answer_flange == "Заглушка":
            with self.conn:
                cur = self.conn.cursor()
                cur.execute(f"""SELECT * FROM flange JOIN plug p on flange.Dy = p.Dy and flange.pressure = p.pressure 
                            WHERE p.Dy = {Dy} AND p.pressure = {pressure_float}""")
                plug = cur.fetchall()

                return "Заглушка", flange_type, plug[0][18], plug[0][15]

        elif answer_flange == "Ответный":
            if flange_type == 1:
                pass





if __name__ == '__main__':
    mod = Model()
    mod.get_flange_value_from_db(1.0, 100, "flange_12821")
    mod.get_gasket_from_db(200, 0.6, 1)
    mod.get_metiz("M10")
