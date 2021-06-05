import sqlite3 as sql
from pathlib import Path
import xlrd

#  для подключения к локальной базе данных
way_to_db = Path(__file__).parent / 'flange.db'
print(way_to_db)
conn = sql.connect(way_to_db)

# открываем файл exel
way_to_exel = Path(__file__).parent / 'Data_flange.xls'
print(way_to_exel)
rb = xlrd.open_workbook(way_to_exel, formatting_info=True, on_demand=True)


# Добавляем фланцы и заглушки
def add_flange():
    pressure = {0: 0.6, 1: 1.0, 2: 1.6, 3: 2.5}
    for i in range(0, 5):
        # выбираем активный лист
        sheet = rb.sheet_by_index(i)
        vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

        pressure_value = pressure.get(i)
        print(pressure_value)
        for row in vals:
            Dy = int(row[0])
            D = int(row[1])
            D1 = int(row[2])
            D2 = int(row[3])
            D4 = int(row[4])
            D6 = int(row[5])
            d = int(row[6])
            n = int(row[7])
            h = int(row[8])
            h1 = int(row[9])
            h2 = int(row[10])
            Bolt = str(row[11])
            # - ---
            d_inside = str(row[13])
            b_20 = int(row[14])
            m_20_1 = float(row[15])
            m_20_2 = float(row[16])
            m_20_3 = float(row[17])
            # - ---
            d1 = int(row[19])
            b_21 = int(row[20])
            h4 = int(row[21])
            Dm = int(row[22])
            Dn = int(row[23])
            m_21_1 = float(row[24])
            m_21_2 = float(row[25])
            m_21_3 = float(row[26])
            # - ---
            Z_b = int(row[28])
            Z_h1 = int(row[29])
            Z_d2 = int(row[30])
            Z_m = float(row[31])
            # - --------
            flange = (Dy, pressure_value, D, D1, D2, D4, D6, d, n, h, h1, h2, Bolt)
            conn.execute("""INSERT INTO  flange (Dy, pressure, D_, D1, D2, D4, D6, d, n, h, h1, h2, bolt) 
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""", flange)
            flange_12820 = (Dy, pressure_value, d_inside, b_20, m_20_1, m_20_2, m_20_3)
            conn.execute("""INSERT INTO flange_12820(Dy, pressure, d_inside, b, mass_1, mass_2, mass_3)
                            VALUES (?,?,?,?,?,?,?)""", flange_12820)
            flange_12821 = (Dy, pressure_value, d1, h4, Dm, Dn, m_21_1, m_21_2, m_21_3)
            conn.execute("""INSERT INTO flange_12821(Dy, pressure, d1, h4, Dm, Dn, mass_1, mass_2, mass_3) 
                            VALUES (?,?,?,?,?,?,?,?,?)""", flange_12821)
            plug = (Dy, pressure_value, Z_b, Z_h1, Z_d2, Z_m)
            conn.execute("""INSERT INTO plug(Dy, pressure, b, h1, d2, m) VALUES (?,?,?,?,?,?)""", plug)
            conn.commit()


if __name__ == '__main__':
    # add_flange() # готово
    conn.close()
    rb.release_resources()
    del rb


