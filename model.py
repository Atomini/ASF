from __future__ import annotations
from pathlib import Path
import sqlite3 as sql
import xlsxwriter
import datetime


class Model:

    def __init__(self):
        way_to_db = Path(__file__).parent / 'flange.db'
        print(way_to_db)
        self.conn = sql.connect(way_to_db)

    def select_from_db(self, *args):
        """
        Выбираем из БД данние для заполнения TableWidget
        :param args: gost           - гост фланца
                     pressure       - Условное давление result_Py
                     Dy             - Значение Ду
                     flange_type    - тип основного фланца
                     answer_flange  - тип ответного фланца
                     number         - количество фланцевых соеденений
                     pipe_length    - длина трубы
                     pipe           - размер трубы
                     name           - обозначение фленцевого соедения
        :return:
        result_Dy               -  Значение Ду
        result_Py               -  Условное давление result_Py
        result_mass             -  масса основного фланца
        result_D                -  наружный диаметр основного фланца
        result_thickness        -  толщина остновного фланца
        result_answer_flange    - ответный фланец ответный/заглушка/нет
        result_type_answer      - тип ответного фланца
        result_mass_answer      - масса ответного фланца
        result_thickness_answer - толщина ответного фланца
        result_bolt             - размер метизов
        result_pin_length       - длина шпильки
        result_pin_number       - Количество шпилек
        result_washer           - количество гаек / шайб
        result_gasket           - размер прокладки
        """

        gost, pressure, Dy, flange_type, answer_flange, number, pipe_length, pipe, name = args[0]

        # конвертируем result_Py из строки в float
        pressure_convert = {"0,1-0,25 МПа": 0.25, "0,6 МПа": 0.6, "1,0 МПа": 1.0, "1,6 МПа": 1.6, "2,5 МПа": 2.5}
        pressure_float = pressure_convert.get(pressure)

        if gost == "12820 (плоский)":
            main_flange = self.get_flange_value_from_db(pressure_float, Dy, "flange_12820")
            # flange GOST = 12821: index  0   1          2   3   4   5   6   7   8   9   10  11    12    13  14  15   16
            #                      param  Dy  pressure   D   D1  D2  D4  D6  d   n   h   h1  h2    bolt  Dy  Py  d1   h4
            #                             17  18   19        20      21
            #                             Dm  Dn   mass_1    mass_2  mass_3

        elif gost == "12821 (сапожковый)":
            main_flange = self.get_flange_value_from_db(pressure_float, Dy, "flange_12821")
            # flange  GOST = 12820: index  0   1          2   3   4   5   6   7   8   9   10  11  12    13  14  15
            #               param          Dy  pressure   D   D1  D2  D4  D6  d   n   h   h1  h2  bolt  Dy  Py  d_in
            #                              16       17      18
            #                              mass_1   mass_2  mass_3

        flange_mass = self.get_flange_mass(flange_type, gost, main_flange)
        flange_thickness = self.get_flange_thickness(flange_type, gost, main_flange)
        flange_answer = self.get_answer_flange(Dy, pressure_float, answer_flange, flange_type, gost, main_flange)
        gasket = self.get_gasket_from_db(Dy, pressure_float, flange_type, answer_flange)
        bolt = main_flange[12]
        metiz = self.get_metiz(bolt, answer_flange, main_flange[8])

        # return block
        result_Dy = main_flange[0]
        result_Py = main_flange[1]
        result_mass = flange_mass
        result_D = main_flange[2]
        result_thickness = flange_thickness
        result_answer_flange = flange_answer[0]
        result_type_answer = flange_answer[1]
        result_mass_answer = flange_answer[2]
        result_thickness_answer = flange_answer[3]
        result_pin_number = metiz[3]
        result_washer = metiz[4]

        if answer_flange == 'Нет':
            result_pin_length = "-"
            result_bolt = "-"
            result_gasket = "-"
            result_gasket_number = "-"
        else:
            result_pin_length = self.pin_legth(result_thickness, result_thickness_answer, metiz)
            result_bolt = main_flange[12]
            result_gasket = gasket[4]
            result_gasket_number = number

        return result_Dy, result_Py, result_mass, result_D, result_thickness, result_answer_flange, result_type_answer,\
               result_mass_answer, result_thickness_answer, result_bolt, result_pin_length, result_pin_number, \
               result_washer, result_gasket, result_gasket_number

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
            if gost == "12820 (плоский)":
                if flange_type == "1":
                    answer_flange_type = "1"
                elif flange_type == "2":
                    answer_flange_type = "3"
                elif flange_type == "3":
                    answer_flange_type = "2"

            elif gost == "12821 (сапожковый)":
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

        if gost == "12820 (плоский)":
            if flange_type == "1":
                mass = flange[17]
            elif flange_type == "2":
                mass = flange[18]
            elif flange_type == "3":
                mass = flange[19]
        elif gost == "12821 (сапожковый)":
            if flange_type == "1":
                mass = flange[19]
            elif flange_type == "2":
                mass = flange[20]
            elif flange_type == "3":
                mass = flange[21]
        return mass

    def get_flange_thickness(self, flange_type, gost, flange):

        if gost == "12820 (плоский)":
            if flange_type == "1" or flange_type == "3":
                thickness = flange[9] + flange[16]
            elif flange_type == "2":
                thickness = flange[10] + flange[16]

        elif gost == "12821 (сапожковый)":
            if flange_type == "1" or flange_type == "3":
                thickness = flange[9] + flange[16]
            elif flange_type == "2":
                thickness = flange[10] + flange[16]
        return thickness

    def pin_legth(self, thickness, thickness_answer, metiz):
        rezult = int(thickness) + int(thickness_answer) + 3 + int(metiz[0]) + int(metiz[2]) + 6
        return rezult

    def save_to_exel(self, data):
        date = datetime.datetime.now().strftime("(%Y_%m_%d__%H.%M.%S)")

        workbook = xlsxwriter.Workbook('фланцы_' + str(date) + '.xlsx')
        worksheet = workbook.add_worksheet()

        table_Horiz_Lable = (
            'Обозначение', 'ГОСТ', 'Ду', 'Py', 'тип', 'масса', 'диаметр', 'толщина', 'ответный', 'тип', 'масса',
            'толщина', 'кол-во', 'крепеж', 'длина шпильки', 'кол-во', 'шайбы кол-во', 'гайка кол-во', 'прокладка',
            'кол-во', 'труба', 'длина трубы')

        position_x = 0
        position_y = 0
        for name in table_Horiz_Lable:
            worksheet.write(position_y, position_x, name)
            position_x += 1
        position_x = 0
        position_y += 1
        for row in data:
            for item in row:
                worksheet.write(position_y, position_x, item)
                position_x += 1
            position_x = 0
            position_y += 1

        workbook.close()


if __name__ == '__main__':
    mod = Model()
    flange = mod.get_flange_value_from_db(1.0, 100, "flange_12820")
    mod.get_gasket_from_db(200, 0.6, 1)
    mod.get_metiz("M10")
    mod.get_flange_mass("2", "flange_12820", flange)
    mod.get_flange_thickness("1", "flange_12820", flange)
    mod.get_answer_flange(100, 2.5, "Ответный", "2", "flange_12820", flange)
