#プログラムの初回実行時に必要なDB作成等を実施
'''
1. DB作成（DB名：stock_price.sqlite3）
2. 株価テーブルの作成（security_code.csvの各銘柄を、テーブル名"stock_price_xxxxT"として作成）
3. コーポレートアクションの履歴を格納するDB/テーブルを作成
'''
import sqlite3
import pandas as pd


def createDB():
    #データベースに接続
    dbpath = '../../DB/stock_price.sqlite3'
    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()

def create_table(ID_list):
    dbpath = '../../DB/stock_price.sqlite3'
    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()

    for ID in ID_list:
        table_name = ('price_raw_' + ID)
        #銘柄ごとにテーブルを作成（作成済みならスキップ）
        print("table_name:", table_name)
        try:
            create_table = 'CREATE TABLE IF NOT EXISTS {} (date date primary key not NULL, start_price float, high_price float, low_price float, end_price float, volume float, adjusted_end_price float)'.format(table_name)

            cursor.execute(create_table)

        except sqlite3.Error as e:
            print(e)

    connection.commit()

def main():
    # 株価を格納するDB作成
    createDB()

    # 株価を格納するテーブルを作成
    ID_list = list(pd.read_csv('../list/stock_list.csv')['code'].astype(str) )
    create_table(ID_list)

if __name__ == "__main__":
    main()