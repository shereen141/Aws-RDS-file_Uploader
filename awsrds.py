import os
import csv
import pymysql
from flask import Flask, render_template, request

app = Flask(__name__)

load_file =app.root_path+'/boat.sql'
@app.route('/connection',methods =['POST','GET'])
def connection():
    conn = pymysql.connect(host= ,
                      port= ,
                      user= ,
                      password= ,
                      db= 
                      )
    return conn
##diplay whole data table

@app.route('/testingdb',methods =['POST','GET'])
def testingdb():
    conn = connection()
    cur = conn.cursor()
    #m=request.files['file']
    #n=request.form.get('numb')/request.form['numb']
    sql_statement = 'select * from boat'
    cur.execute(sql_statement)
    results = cur.fetchall()
    list=[]
    for row in results:
        tuple=(row[0],row[1],row[2],row[4],row[5])
        list.append(tuple)
    conn.commit()
    cur.close()
    conn.close()
    return render_template('result.html',list=list) 

#display data
@app.route('/result',methods =['POST','GET'])
def dbcount():
    print('hi')
    conn = connection()
    cur = conn.cursor()
    quer = 'select count(*) from boat'
    cur.execute(quer)
    res = cur.fetchone()
    print(res[0])
    conn.commit()
    cur.close()
    conn.close()
    return render_template('display.html', )


## query html
@app.route('/result',methods =['POST','GET'])
def query():
    conn = connection()
    cur = conn.cursor()
    if request.method == 'POST':
        mytext = request.form['text1']
        mytext1 = request.form['text2']
        sql = 'select * from boat where place like "%'+mytext+'" and "%+mytext1';
        cur.execute(sql)
        r = cur.fetchall()

    return render_template('result.html')

@app.route('/result',methods =['POST','GET'])
def query():
    conn = connection()
    cur = conn.cursor()
    if request.method == 'POST':
        mytext = request.form['text1']
        mytext1 = request.form['text2']
        sql = 'select * from boat ';

        cur.execute(sql)
        r = cur.fetchall()

    return render_template('result.html')

### CLEAR DB### CLEAR DB
def clearDb():
    conn = connection()
    cur = conn.cursor()
    sql_statement= 'delete from boat where latitude is NULL or longitude is null or magNst is null'
    cur.execute(sql_statement)
    quer= 'select count(*) from boat'
    cur.execute(quer)
    res=cur.fetchone()
    print(res[0])
    conn.commit()
    cur.close()
    conn.close()






@app.route('/')
def hello_world():
    dbcount()

    return render_template('main.html')

if __name__ == '__main__':

    app.run()
