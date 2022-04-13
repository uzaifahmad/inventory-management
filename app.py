from flask import Flask,request,render_template
import pyodbc
app = Flask(__name__)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ZIL1180\MSSQLDEV2019;'
                      'Database=inventory;'
                      'Trusted_Connection=yes;')

cursor=conn.cursor()

cursor.execute('SELECT * FROM products')
products=cursor.fetchall()

@app.route('/')
def index():
    return render_template("form.html")
@app.route('/example.html/')
def invenotory(): 
    return render_template("example.html",value=products)
@app.route('/sales.html/')
def sales():

    return render_template("sales.html")

cursor.execute('SELECT * FROM customer')
customers=cursor.fetchall()

@app.route('/customer.html/')
def customer():
    return render_template("customer.html",value=customers)
    
if __name__ == '__main__':
    app.run(debug=True) 



