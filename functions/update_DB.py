import csv
import pandas as pd
import os
import sqlite3
from datetime import datetime, date, time


def get_latest_date_from_database(id):
    # DBから最新のデータの日付を取得
    dbpath = '../../DB/stock_price.sqlite3'
    connection = sqlite3.connect(dbpath)

    # id = 'price_raw_1301'
    sql_command = "SELECT date FROM {} ORDER BY date DESC;".format(id)
    df = pd.read_sql(sql_command, connection)
    latest_date = df['date'][0]
    print('latest date in database:', latest_date)
    return latest_date

def read_new_data(start_date):
    # 最新のファイルから追加すべきデータ部分を抽出し、DBにアップデート
    tmp_dir = os.path.abspath(os.getcwd() + "/../../download_tmp/")
    data = pd.read_csv(tmp_dir + '/' + '1301.T.csv', skiprows=1, names=["date", "start", "high", "low", "end", "volume", "adjusted_end"], parse_dates=['date'])
    data['date'] = data['date'].dt.strftime('%Y-%m-%d')
    df = data.query('date > @start_date')
    return df


def append_new_data_to_database(code, df):

    dbpath = '../../DB/stock_price.sqlite3'
    connection = sqlite3.connect(dbpath)

    table_name = code
    df.to_sql(table_name, connection, if_exists='append')


def main():
    id_list = list(pd.read_csv('../list/stock_list.csv')['code'].astype(str) )
    for id in id_list:
        code = 'price_raw_' + id
        print('table name:', code)
        latest_date = get_latest_date_from_database(code)
        new_data = read_new_data(latest_date)
        append_new_data_to_database(code, new_data)


if __name__ == '__main__':
    main()