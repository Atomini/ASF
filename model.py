from __future__ import annotations
from pathlib import Path
import sqlite3 as sql


class Model:

    def __init__(self):
        way_to_db = Path(__file__).parent / 'flange.db'
        print(way_to_db)
        self.conn = sql.connect(way_to_db)

    def select_from_db(self, *args):
        """
        Выбираем из БД данние
        :param args: gost           - гост фланца
                     pressure       - Условное давление Py
                     Dy             - Значение Ду
                     flange_type    - тип основного фланца
                     answer_flange  - тип ответного фланца
                     number         - количество фланцевых соеденений
                     pipe_length    - длина трубы
                     pipe           - размер трубы
                     name           - обозначение фленцевого соедения
        :return:
        ret_Dy              -  Значение Ду
        Py                  -  Условное давление Py
        mass                -  масса основного фланца
        D                   -  наружный диаметр основного фланца
        thickness           -  толщина остновного фланца
        ret_answer_flange   - ответный фланец ответный/заглушка/нет
        ret_type_answer     - тип ответного фланца
        mass_answer         - масса ответного фланца
        thickness_answer    - толщина ответного фланца
        ret_bolt            - размер метизов
        pin_length          - длина шпильки
        pin_number          - Количество шпилек
        washer              - количество гаек / шайб
        ret_gasket          - размер прокладки
        """

        gost, pressure, Dy, flange_type, answer_flange, number, pipe_length, pipe, name = args[0]

        # конвертируем Py из строки в float
        pressure_convert = {"0,1-0,25 МПа": 0.25, "0,6 МПа": 0.6, "1,0 МПа": 1.0, "1,6 МПа": 1.6, "2,5 МПа": 2.5}
        pressure_float = pressure_convert.get(pressure)

        if gost == "12820 (плоский)":
            flange = self.get_flange_value_from_db(pressure_float, Dy, "flange_12820")
            flange_mass = self.get_flange_mass(flange_type, "flange_12820", flange)
            flange_thickness = self.get_flange_thickness(flange_type, "flange_12820", flange)
            flange_answer = self.get_answer_flange(Dy, pressure_float, answer_flange, flange_type,
                                                   "flange_12820", flange)

        elif gost == "12821 (сапожковый)":
            flange = self.get_flange_value_from_db(pressure_float, Dy, "flange_12821")
            flange_mass = self.get_flange_mass(flange_type, "flange_12821", flange)
            flange_thickness = self.get_flange_thickness(flange_type, "flange_12821", flange)
            flange_answer = self.get_answer_flange(Dy, pressure_float, answer_flange, flange_type,
                                                   "flange_12821", flange)

        gasket = self.get_gasket_from_db(Dy, pressure_float, flange_type, answer_flange)
        bolt = flange[12]
        metiz = self.get_metiz(bolt, answer_flange, flange[8])

        # return block
        ret_Dy = flange[0]
        Py = flange[1]
        mass = flange_mass
        D = flange[2]
        thickness = flange_thickness
        ret_answer_flange = flange_answer[0]
        ret_type_answer = flange_answer[1]
        mass_answer = flange_answer[2]
        thickness_answer = flange_answer[3]
        pin_number = metiz[3]
        washer = metiz[4]

        if answer_flange == 'Нет':
            ret_pin_length = "-"
            ret_bolt = "-"
            ret_gasket = "-"
            ret_gasket_number = "-"
        else:
            ret_pin_length = self.pin_legth(thickness, thickness_answer, metiz)
            ret_bolt = flange[12]
            ret_gasket = gasket[4]
            ret_gasket_number = number

        return ret_Dy, Py, mass, D, thickness, ret_answer_flange, ret_type_answer, mass_answer, thickness_answer, \
               ret_bolt, ret_pin_length, pin_number, washer, ret_gasket, ret_gasket_number

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

    def get_gasket_from_db(self, Dy, pressure, flange_type, answer_flange):
        """Получем из БД размеры для прокладки в зависимости от Ду, давления, типа фланца"""
        if answer_flange == "Нет":
            return '-', '-', '-', '-', '-'

        if flange_type == 1:
            index = 0
        else:
            index = 1

        with self.conn:
            cur = self.conn.cursor()
            cur.execute(f"""SELECT * FROM gasket WHERE Dy = {Dy} AND pressure = {pressure}""")
            gasket = cur.fetchall()
            return gasket[index]

    def get_metiz(self, bolt, answer_flange, number):

        if answer_flange == "Нет":
            return "-", "-", "-", "-", "-"

        with self.conn:
            cur = self.conn.cursor()
            cur.execute("""SELECT thickness FROM nut WHERE bolt = ? """, (bolt,))
            nut = cur.fetchall()
            cur.execute("""SELECT min_length FROM pin WHERE bolt = ? """, (bolt,))
            pin = cur.fetchall()
            cur.execute("""SELECT thickness FROM washer WHERE bolt = ? """, (bolt,))
            washer = cur.fetchall()
            pin_number = number
            nut_number = number * 2
            return nut[0][0], pin[0][0], washer[0][0], pin_number, nut_number

    def get_answer_flange(self, Dy, pressure_float, answer_flange, flange_type, gost, flange):

        if answer_flange == "Нет":
            return "-", "-", "-", "-"

        elif answer_flange == "Заглушка":
            with self.conn:
                cur = self.conn.cursor()
                cur.execute(f"""SELECT * FROM flange JOIN plug p on flange.Dy = p.Dy and flange.pressure = p.pressure 
                            WHERE p.Dy = {Dy} AND p.pressure = {pressure_float}""")
                plug = cur.fetchall()

                return answer_flange, flange_type, plug[0][18], plug[0][15]

        elif answer_flange == "Ответный":
            if gost == "flange_12820":
                if flange_type == "1":
                    answer_flange_type = "1"
                elif flange_type == "2":
                    answer_flange_type = "3"
                elif flange_type == "3":
                    answer_flange_type = "2"

            elif gost == "flange_12821":
                if flange_type == "1":
                    answer_flange_type = "1"
                elif flange_type == "2":
                    answer_flange_type = "3"
                elif flange_type == "3":
                    answer_flange_type = "2"

            answer_flange_mass = self.get_flange_mass(answer_flange_type, gost, flange)
            answer_flange_thickness = self.get_flange_thickness(answer_flange_type, gost, flange)
            return answer_flange, answer_flange_type, answer_flange_mass, answer_flange_thickness

    def get_flange_mass(self, flange_type, gost, flange):

        if gost == "flange_12820":
            if flange_type == "1":
                mass = flange[17]
            elif flange_type == "2":
                mass = flange[18]
            elif flange_type == "3":
                mass = flange[19]
        elif gost == "flange_12821":
            if flange_type == "1":
                mass = flange[19]
            elif flange_type == "2":
                mass = flange[20]
            elif flange_type == "3":
                mass = flange[21]
        return mass

    def get_flange_thickness(self, flange_type, gost, flange):

        if gost == "flange_12820":
            if flange_type == "1" or flange_type == "3":
                thickness = flange[9] + flange[16]
            elif flange_type == "2":
                thickness = flange[10] + flange[16]

        elif gost == "flange_12821":
            if flange_type == "1" or flange_type == "3":
                thickness = flange[9] + flange[16]
            elif flange_type == "2":
                thickness = flange[10] + flange[16]
        return thickness


    def pin_legth(self, thickness, thickness_answer, metiz):
        rezult = int(thickness)+int(thickness_answer)+3+int(metiz[0])+int(metiz[2])+6
        return rezult


if __name__ == '__main__':
    mod = Model()
    flange = mod.get_flange_value_from_db(1.0, 100, "flange_12820")
    mod.get_gasket_from_db(200, 0.6, 1)
    mod.get_metiz("M10")
    mod.get_flange_mass("2", "flange_12820", flange)
    mod.get_flange_thickness("1", "flange_12820", flange)
    mod.get_answer_flange(100, 2.5, "Ответный", "2", "flange_12820", flange)
