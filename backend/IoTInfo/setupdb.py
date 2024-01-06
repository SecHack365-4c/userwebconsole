import mysql.connector

# データベースに接続
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              )
# カーソルを作成
cursor = cnx.cursor()

cursor.execute("CREATE DATABASE iotdb")

# テーブルを作成

cursor.execute("""
USE iotdb;
CREATE TABLE IF NOT EXISTS iot_devices(
  id INT AUTO_INCREMENT PRIMARY KEY,
  MACaddress VARCHAR(20) NOT NULL UNIQUE,
  iotname VARCHAR(20) NOT NULL UNIQUE,
  username VARCHAR(20) NOT NULL,
  password VARCHAR(20) NOT NULL
)
""")
#UNIQUEで一意制約をつけることで、同じMACadress/iotnameを登録できないようにする

# データベース接続を閉じる
cnx.close()
