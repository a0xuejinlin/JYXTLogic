import sqlite3
import common

import baostock as bs
import pandas as pd


def create_trade_data_table():
    conn = sqlite3.connect(common.db_path_sqlite3)
    cursor = conn.cursor()
    sql = "CREATE TABLE tradeDataMaintenance1 (id INTEGER PRIMARY KEY AUTOINCREMENT, stockName TEXT NOT NULL, stockcode TEXT NOT NULL, tradeTime TEXT NOT NULL, direction TEXT NOT NULL CHECK(direction IN ('buy', 'sell')), volume INTEGER NOT NULL, price REAL NOT NULL, turnover REAL, commissionFee REAL, stampDuty REAL , transferFee REAL, amount REAL, insertTime TEXT DEFAULT (datetime('now','localtime')), IsRevise INTEGER DEFAULT 0, ISdel INTEGER DEFAULT 0, by1 TEXT, by2 TEXT, by3 TEXT, by4 TEXT, by5 TEXT)"
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
create_trade_data_table()

# 表名称：tradeDataMaintenance
# 表字段：
        # id INTEGER PRIMARY KEY AUTOINCREMENT, # 自动增长的唯一ID  
        # stockName TEXT NOT NULL,  # 股票名称
        # stockcode text
        # tradeTime TEXT NOT NULL, # 成交时间
        # direction TEXT NOT NULL CHECK(direction IN ('buy', 'sell')) # 买卖方向  
        # volume INTEGER NOT NULL, # 成交数量
        # price REAL NOT NULL, # 成交价格 
        # turnover REAL, # 成交金额
        # commissionFee REAL, # 手续费 
        # stampDuty REAL,  # 印花税
        # transferFee REAL, # 过户费
        # amount REAL, # 发生金额合计 
        # insertTime TEXT # 插入数据库的时间
        
        # IsRevise（只有两个选项0、1） 是否修改
        # ISdel（只有两个选项0、1） 是否删除

        # by1 备用1
        # by2 备用2
        # by3 备用3
        # by4 备用4
        # by5 备用5
