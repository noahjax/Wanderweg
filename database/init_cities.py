
# imports
import json
import sqlite3
from sqlite3 import Error
from db_utils import create_connection

'''
This file initializes the cities table in the Wanderweg database
'''

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_cities_table(database):

    # create a database connection                               
    conn = create_connection(database)

    #Create table for city features 
    sql_create_cities_table = """ CREATE TABLE IF NOT EXISTS cities (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        country text NOT NULL,
                                        hostel_url text,
                                        hostelworld_pic text,
                                        population integer,
                                        latitude real,
                                        longitude real,
                                        weather text,
                                        trainline_id text
                                    ); """

    if conn is not None:
        # create cities table
        create_table(conn, sql_create_cities_table)
    else:
        print("Error! cannot create the database connection.")

    return conn


def create_city(conn, city):
    sql = "insert into cities values(?,?,?,?,?,?,?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, city)
    return cur.lastrowid


def readFromFile(filename):
    ret = {}
    with open(filename) as f:
        data = json.load(f)
        for key in sorted(list(data.keys())):
            ret[key] = data[key]
    return ret


def load_cities_data(conn):
    countries = ["Italy", "Croatia", "Slovenia"] #, "France", "Germany", "Switzerland", "Austria"]
    count = 1
    for country in countries:
        filename = 'countries/' + country.lower() + 'Data.txt'
        cities = readFromFile(filename)
        for city, info in cities.items():
            create_city(conn, (count, city, info[0], info[1], info[2], info[3], info[4], info[5], str(info[6]), '0'))
            count += 1


def main():
    database = 'wanderweg.db'
    conn = create_cities_table(database)
    load_cities_data(conn)
    conn.commit()
    conn.close()


if __name__ == '__main__':  
    main()