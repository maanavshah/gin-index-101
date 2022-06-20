import pandas as pd
import psycopg2

TITLE_IDX = 1
YEAR_IDX = 2
METASCORE_IDX = 3

try:
    connection = psycopg2.connect(user="maanav",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()

    df = pd.read_csv('~/Desktop/movies.csv')
    df['Metascore'] = df['Metascore'].fillna(0)

    postgres_insert_query = """ INSERT INTO movies (title, year, metascore) VALUES (%s,%s,%s)"""

    for row in df.itertuples():
        record_to_insert = (row[TITLE_IDX], row[YEAR_IDX], int(row[METASCORE_IDX]))
        print(postgres_insert_query, record_to_insert)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
