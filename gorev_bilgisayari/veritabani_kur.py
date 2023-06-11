import sqlite3

con = sqlite3.connection("taban.db")
cursor = con.cursor()

sql="Create Table Islev(Id INTEGER PRIMARY KEY AUTOINCREMENT,Yon VARCHAR(100),Durum BOOLEAN)"
cursor.execute(sql)
con.commit()


sql="Insert Into Islev(Yon,Durum) VALUES('ileri',0)"
cursor.execute(sql)
con.commit()

sql="Insert Into Islev(Yon,Durum) VALUES('geri',0)"
cursor.execute(sql)
con.commit()

sql="Insert Into Islev(Yon,Durum) VALUES('sag',0)"
cursor.execute(sql)
con.commit()

sql="Insert Into Islev(Yon,Durum) VALUES('sol',0)"
cursor.execute(sql)
con.commit()

sql="Insert Into Islev(Yon,Durum) VALUES('capala',0)"
cursor.execute(sql)
con.commit()

sql="Insert Into Islev(Yon,Durum) VALUES('durdur',0)"
cursor.execute(sql)
con.commit()

sql="Insert Into Islev(Yon,Durum) VALUES('otonom',0)"
cursor.execute(sql)
con.commit()

