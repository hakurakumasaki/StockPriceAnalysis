import pandas as pd
import sqlite3

def insert_price_to_DB(ID_list):
    dbpath = '../../DB/stock_price.sqlite3'
    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()

    for ID in ID_list:
        data_file = '../../DB/data_dump/'+ ID + '.T.csv'
        df = pd.read_csv(data_file, skiprows=1,names=["date", "start", "high", "low", "end", "volume", "adjusted_end"] )
        table_name = 'price_raw_' + ID
        print(table_name)
        df.to_sql(table_name, connection, if_exists='replace')


def main():
    ID_list = list(pd.read_csv('../list/stock_list.csv')['code'].astype(str) )
    insert_price_to_DB(ID_list)

if __name__ == "__main__":
    main()