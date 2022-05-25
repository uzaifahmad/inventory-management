import connection
from flask import Flask,request,render_template

app = Flask(__name__)


cursor=connection.conn.cursor()

cursor.execute('SELECT * FROM product')
products=cursor.fetchall()

def calculate(productid,quantity,products):
    for i in products:
        if i[0]==productid:
            return i[0],i[1],quantity,i[4],i[4]*quantity

def inventory():
    cursor.execute("SELECT * FROM Product")
    products=[list(i) for i in cursor.fetchall()]
    return products

@app.route('/')
def home():
    return render_template("form.html")
@app.route('/inventory/')
def invenotory(): 
    return render_template("example.html",value=products)
def init_cart():
    global cart
    cart=[]
init_cart()
@app.route('/sales/',methods=['POST','GET'])
def sales():
    if request.method=='POST':
        obj=[int(i) for i in request.form.values()]
        cart.append(list(calculate(obj[0],obj[1],products)))
        print(cart)
        return render_template('sales.html',temp=cart)

    return render_template('sales.html')

cursor.execute('SELECT * FROM customer')
customers=cursor.fetchall()

@app.route('/customer/')
def customer():
    return render_template("customer.html",value=customers)

@app.route('/orders/')
def orders():
    cursor.execute('EXEC DisplayOrders')
    orders=[list(i) for i in cursor.fetchall()]
    return render_template("orders.html",order=orders)
@app.route('/outofstock/')
def outofstock():
    cursor.execute('EXEC out_of_stock')
    out=[list(i) for i in cursor.fetchall()]
    return render_template("outofstock.html",outofstock=out)
if __name__ == '__main__':
    app.run(debug=True) 