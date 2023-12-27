# 本页面的内容主要用于维护交易系统中的数据（插删改查）

import sqlite3

from . import commonjx

# 新增tradeDataMaintenance表的交易记录
# 参数data:为字典类型,包含表所有字段如下:
# stockCode:股票代码 
# stockName:股票名称
# tradeTime:成交时间
# direction:买卖方向 
# volume:成交数量
# price:成交价格
# turnover:成交金额
# commissionFee:手续费
# stampDuty:印花税
# transferFee:过户费
# amount:发生金额合计
def create_record(stockcode, stockName, tradeTime, direction, volume,price, turnover, commissionFee, stampDuty,transferFee, amount):
    try:
        conn = sqlite3.connect(commonjx.db_path_sqlite3)
        sql = """INSERT INTO tradeDataMaintenance 
                  (stockCode, stockName, tradeTime, direction, volume, 
                  price, turnover, commissionFee, stampDuty,  
                  transferFee, amount) 
                  VALUES(?,?,?,?,?,?,?,?,?,?,?)"""
        cursor = conn.execute(sql, (stockcode, stockName, tradeTime, direction, volume,price, turnover, commissionFee, stampDuty,transferFee, amount,))
        conn.commit()
    except Exception as e:
        print("Insert error:", e)
    finally:
        conn.close()



# 返回表中id字段的最大值
def get_max_id():
    try:
        conn = sqlite3.connect(commonjx.db_path_sqlite3)
        sql = "SELECT MAX(id) FROM tradeDataMaintenance where IsRevise = 0 AND ISdel = 0"
        cursor = conn.execute(sql)
        max_id = cursor.fetchone()[0]
        print("Max id:", max_id)
        return max_id
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

#返回表中所有的去重股票名称
def get_distinct_stocknames():
    try:
        conn = sqlite3.connect(commonjx.db_path_sqlite3)
        sql = "SELECT DISTINCT stockName FROM tradeDataMaintenance where IsRevise = 0 AND ISdel = 0"
        cursor = conn.execute(sql)
        stock_names = [row[0] for row in cursor.fetchall()]
        return stock_names
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()


#通过id查询指定的交易记录的股票号码
def read_record_by_id(id):
    try:
        conn = sqlite3.connect(commonjx.db_path_sqlite3)
        sql = "SELECT stockcode FROM tradeDataMaintenance WHERE id = ? and IsRevise = 0 AND ISdel = 0"
        cursor = conn.execute(sql, (id,))
        row = cursor.fetchone()[0]
        if row:
            print(row)
        else:
            print("Record with id {} not found".format(id))
        return row
    except Exception as e:
        print("Read error:", e)
    finally:
        conn.close()

    
# 查询tradeDataMaintenance表的所有交易记录
# 参数:无
# 返回:记录列表,每条记录为元组  
def read_records(codestock,num):
    try:
        conn = sqlite3.connect(commonjx.db_path_sqlite3)
        sql = "SELECT id,stockCode, stockName, tradeTime, direction, volume, price, turnover, commissionFee, stampDuty, transferFee, amount, insertTime FROM tradeDataMaintenance where IsRevise = 0 AND ISdel = 0 and stockcode == ? order by id asc limit ?"
        cursor = conn.execute(sql,(codestock,num,))
        rows=cursor.fetchall()
        for row in rows:
            print(row)
        
        return rows
    except Exception as e:  
        print("Read error:", e)
    finally:
        conn.close()
        

# 更新tradeDataMaintenance表的交易记录
# 参数id:记录的id
# 参数data:更新后的记录数据,字典类型,包含所有字段        
def update_record(stockcode, stockName, tradeTime, direction, volume,price, turnover, commissionFee, stampDuty,transferFee, amount,id):
    try: 
        conn = sqlite3.connect(commonjx.db_path_sqlite3)
        sql = """UPDATE tradeDataMaintenance SET stockCode=?, stockName=?,  
                  tradeTime=?, direction=?, volume=?, price=?, turnover=?,
                  commissionFee=?, stampDuty=?, transferFee=?, amount=? 
                  WHERE IsRevise = 0 AND ISdel = 0 and id=?"""
        cursor = conn.execute(sql, (stockcode, stockName, tradeTime, direction, volume,price, turnover, commissionFee, stampDuty,transferFee, amount,id))
        conn.commit()
    except Exception as e:   
        print("Update error:", e)
    finally:
        conn.close()   

# 删除tradeDataMaintenance表的交易记录
# 参数id:交易记录的id  
def delete_record(id):
    try:
        conn = sqlite3.connect(commonjx.db_path_sqlite3)
        sql = "UPDATE tradeDataMaintenance SET IsRevise = 1 WHERE id = ?;"  
        cursor = conn.execute(sql, (id,))
        print(":这条数据已经被删除"+str(id))
        conn.commit() 
    except Exception as e:
        print("Delete error:", e)
    finally:
        conn.close()

#通过stockname获取本条股票的所有交易记录
def stockdata_bysname(stockname,num):
    try:
        conn = sqlite3.connect(commonjx.db_path_sqlite3)
        sql = "SELECT id,stockCode, stockName, tradeTime, direction, volume, price, turnover, commissionFee, stampDuty, transferFee, amount, insertTime FROM tradeDataMaintenance where IsRevise = 0 AND ISdel = 0 and stockname == ? order by id asc limit ?"  
        cursor = conn.execute(sql, (stockname,num))
        rows=cursor.fetchall()
        print(":已通过"+str(stockname)+"找到所有数据并反馈")
        
        for row in rows:
            print(row)        
        return rows

    except Exception as e:
        print("Delete error:", e)
    finally:
        conn.close()
        
