from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
import sqlite3

con = sqlite3.connection("taban.db")
cursor = con.cursor()


app = Flask(__name__) 

app.secret_key="Kıyafet Sayar"

#stream yapma
#video yayınlama
#https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00



@app.route("/")
def index():
    return "Aktif"

@app.route("/setileri")
def setileri():
    sql="Update Islev Durum=1 Where Yon='ileri'"
    cursor.execute(sql)
    con.commit()

@app.route("/setgeri")
def setgeri():
    sql="Update Islev Durum=1 Where Yon='geri'"
    cursor.execute(sql)
    con.commit()

@app.route("/setsag")
def setsag():
    sql="Update Islev Durum=1 Where Yon='sag'"
    cursor.execute(sql)
    con.commit()

@app.route("/setsol")
def setsol():
    sql="Update Islev Durum=1 Where Yon='sol'"
    cursor.execute(sql)
    con.commit()

@app.route("/setcapala")
def setcapala():
    sql="Update Islev Durum=1 Where Yon='capala'"
    cursor.execute(sql)
    con.commit()


@app.route("/setdurdur")
def setdurdur():
    sql="Update Islev Durum=1 Where Yon='durdur'"
    cursor.execute(sql)
    con.commit()


@app.route("/setotonom")
def setotonom():
    sql="Update Islev Durum=1 Where Yon='otonom'"
    cursor.execute()
    con.commit()



@app.route("/getileri")
def getileri():
    sql="Select Drurum From Islev Where Yon='ileri'"
    cursor.execute(sql)
    veri=cursor.fetchone(sql)
    veri= veri[0]
    
    sql="Update Islev Durum=0 Where Yon='ileri'"
    cursor.execute(sql)
    con.commit()

    if(veri):
        return "True"
    else:
        return "False"

@app.route("/getgeri")
def getgeri():

    sql="Select Drurum From Islev Where Yon='geri'"
    cursor.execute(sql)
    veri=cursor.fetchone(sql)
    veri= veri[0]
    
    sql="Update Islev Durum=0 Where Yon='geri'"
    cursor.execute(sql)
    con.commit()

    if(veri):
        return "True"
    else:
        return "False"

@app.route("/getsag")
def getsag():
    sql="Select Drurum From Islev Where Yon='sag'"
    cursor.execute(sql)
    veri=cursor.fetchone(sql)
    veri= veri[0]
    
    sql="Update Islev Durum=0 Where Yon='sag'"
    cursor.execute(sql)
    con.commit()

    if(veri):
        return "True"
    else:
        return "False"

@app.route("/getsol")
def getsol():

    sql="Select Drurum From Islev Where Yon='sol'"
    cursor.execute(sql)
    veri=cursor.fetchone(sql)
    veri= veri[0]
    
    sql="Update Islev Durum=0 Where Yon='sol'"
    cursor.execute(sql)
    con.commit()

    if(veri):
        return "True"
    else:
        return "False"

@app.route("/getcapala")
def getcapala():

    sql="Select Drurum From Islev Where Yon='capala'"
    cursor.execute(sql)
    veri=cursor.fetchone(sql)
    veri= veri[0]
    
    sql="Update Islev Durum=0 Where Yon='capala'"
    cursor.execute(sql)
    con.commit()

    if(veri):
        return "True"
    else:
        return "False"


@app.route("/getdurdur")
def getdurdur():

    sql="Select Drurum From Islev Where Yon='durdur'"
    cursor.execute(sql)
    veri=cursor.fetchone(sql)
    veri= veri[0]
    
    sql="Update Islev Durum=0 Where Yon='durdur'"
    cursor.execute(sql)
    con.commit()

    if(veri):
        return "True"
    else:
        return "False"

@app.route("/getotonom")
def getotonom():

    sql="Select Drurum From Islev Where Yon='otonom'"
    cursor.execute(sql)
    veri=cursor.fetchone(sql)
    veri= veri[0]
    
    sql="Update Islev Durum=0 Where Yon='otonom'"
    cursor.execute(sql)
    con.commit()

    if(veri):
        return "True"
    else:
        return "False"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
