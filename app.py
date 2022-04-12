from flask import Flask, render_template
import pyodbc
app = Flask(__name__)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ZIL1180\MSSQLDEV2019;'
                      'Database=ASSIGNMENT;'
                      'Trusted_Connection=yes;')

cursor=conn.cursor()
cursor.execute("select * from inventory") 
data = cursor.fetchall() #data from database
cursor.execute("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'inventory'") 
content = cursor.fetchall() #data from database
@app.route('/')
def index():
    return render_template("form.html")
@app.route('/example.html/')
def invenotory(): 
    return render_template("example.html",value=data,value1=content)
@app.route('/sales.html/')
def sales():
    return render_template("sales.html")
    
if __name__ == '__main__':
    app.run(debug=True) 



