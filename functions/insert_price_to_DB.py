import pandas as pd
import sqlite3


def insert_price_to_database(id_list):
    dbpath = '../../DB/stock_price.sqlite3'
    connection = sqlite3.connect(dbpath)

    for ID in id_list:
        data_file = '../../DB/data_dump/' + ID + '.T.csv'
        df = pd.read_csv(data_file, skiprows=1, names=["date", "start", "high", "low", "end", "volume", "adjusted_end"],
                         parse_dates=['date'])
        df['date'] = df['date'].dt.strftime('%Y-%m-%d')  # 月、日を2桁とした文字列に変換（sqliteは日付型を持てないため
        table_name = 'price_raw_' + ID
        print(table_name)
        df.to_sql(table_name, connection, if_exists='replace')


def main():
    id_list = list(pd.read_csv('../list/stock_list.csv')['code'].astype(str))
    insert_price_to_database(id_list)


if __name__ == "__main__":
    main()
