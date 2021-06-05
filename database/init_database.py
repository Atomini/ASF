import sqlite3 as sql

# создание БД
conn = sql.connect("flange.db")

with conn:
    cur = conn.cursor()
    # Значения переменных из ГОСТ 12815
    cur.execute(""" CREATE TABLE IF NOT EXISTS flange(
                    Dy          TEXT,
                    pressure    FLOAT,
                    D_          INTEGER,
                    D1          INTEGER,
                    D2          INTEGER,
                    D4          INTEGER, 
                    D6          INTEGER,
                    d           INTEGER,
                    n           INTEGER,
                    h           INTEGER,
                    h1          INTEGER,
                    h2          INTEGER,
                    bolt        TEXT
                )""")
    # Значения переменных из ГОСТ 12820
    cur.execute(""" CREATE TABLE IF NOT EXISTS flange_12820(
                    Dy          TEXT,
                    pressure    FLOAT,
                    d_inside    TEXT,
                    b           INTEGER,
                    mass_1      FLOAT,
                    mass_2      FLOAT,
                    mass_3      FLOAT,
            FOREIGN KEY (Dy, pressure) REFERENCES flange(Dy, pressure)
                )""")
    # Значения переменных из ГОСТ 12821
    cur.execute(""" CREATE TABLE IF NOT EXISTS flange_12821(
                    Dy          TEXT,
                    pressure    FLOAT,
                    d1          INTEGER,
                    h4          INTEGER,
                    Dm          INTEGER,
                    Dn          INTEGER,
                    mass_1      FLOAT,
                    mass_2      FLOAT,
                    mass_3      FLOAT,
                    FOREIGN KEY (Dy, pressure) REFERENCES flange(Dy, pressure)
                )""")
    # Заглушка заначение параметров по ГОСТ
    cur.execute(""" CREATE TABLE IF NOT EXISTS plug(
                    Dy          TEXT,
                    pressure    FLOAT,
                    b           INTEGER,
                    h1          INTEGER,
                    d2          INTEGER,
                    m           FLOAT,
                    FOREIGN KEY (Dy, pressure) REFERENCES flange(Dy, pressure)
                )""")
    # Гайка
    cur.execute(""" CREATE TABLE IF NOT EXISTS nut(
                    bolt        TEXT,
                    thickness   INTEGER,
                    FOREIGN KEY (bolt) REFERENCES flange(bolt)
                )""")
    # Шайба
    cur.execute(""" CREATE TABLE IF NOT EXISTS washer(
                    bolt        TEXT,
                    thickness   FLOAT,
                    FOREIGN KEY (bolt) REFERENCES flange(bolt)
                )""")
    # Шпилька
    cur.execute(""" CREATE TABLE IF NOT EXISTS pin(
                    bolt        TEXT,
                    min_length  INTEGER,
                    FOREIGN KEY (bolt) REFERENCES flange(bolt)
                )""")
    # Прокладка
    cur.execute(""" CREATE TABLE IF NOT EXISTS gasket(
                    Dy          TEXT,
                    pressure    FLOAT,
                    type        TEXT,
                    thickness   INTEGER,
                    size        TEXT,
                    FOREIGN KEY (Dy, pressure) REFERENCES flange(Dy, pressure)
                )""")
    # Труба
    cur.execute(""" CREATE TABLE IF NOT EXISTS pipe(
                    Dy       TEXT,
                    size     TEXT,
                    FOREIGN KEY (Dy) REFERENCES flange(Dy)
                )""")
