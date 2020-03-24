import base64
import sqlite3
import pickle
import random


def main():
    conn = sqlite3.connect('flags.db')
    cur = conn.cursor()

    # create tables
    cur.execute('''
        CREATE TABLE fakeflags
        (name text, flag text)
    ''')
    cur.execute('''
        CREATE TABLE flags
        (name text, flag text)
    ''')

    # fill with fake data
    data = {
        'demo': 'DEMO{sample_flag}',
        'test': 'TEST{sample_flag}',
        'random': 'RAND{sample_flag}'
    }
    for key, value in data.items():
        cur.execute('''
            INSERT INTO fakeflags
            VALUES (?, ?)
        ''', (key, value))

    # fill with real data
    data = {
        'wtctf': 'AFNOM{7h3_oNly_R3aL_aC7uaL_fLA9}',
    }
    for key, value in data.items():
        cur.execute('''
            INSERT INTO flags
            VALUES (?, ?)
        ''', (key, value))

    # commit and close
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
