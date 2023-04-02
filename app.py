from flask import Flask, request, render_template
#import pickle 
from rsmodel import *
import pymysql as pms
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("login_page.html")

@app.route("/check", methods=['Post'])
def check():
    username = request.form['username']
    password = request.form['password']
    #return "Success!"
    f=open('ps.txt','rb')
    conn=pms.connect(host="localhost",port=3306,user="root",password="Ms03#shrusps",db="employees")
    cur=conn.cursor() #object for accessing queries
    cur.execute("select * from login")
    for i in cur.fetchall():
        if i[0]==username and i[1]==password:
            return render_template("success.html")
    return render_template("login_page.html",data="INVALID USER CREDENTIALS")

@app.route("/recommend", methods=['Post'])
def recommend():
#    model = pickle.load(open(r'C:\Users\Shruthi Mohan\OneDrive\Desktop\College_Stuff\Sem4\ML\CIA2- FLASK\Solution1\model.pkl','rb'))
    input_series = request.form['series']
    rec = get_recommendations_new(input_series)
    return render_template("result.html",data=rec)

if __name__=='__main__':
    app.run(host='localhost',port=5000)