from flask import *
import pymysql
connection=pymysql.connect(host="localhost",user="root",password="",database="Kima")
# create an application
app =Flask(__name__)
#create a route
# @app.route("/") 
# def main():
#     return "This is the main route"
app.secret_key="dbsbdbfdfdbvjdbvbjbjvjjbv"
@app.route("/") 
def main():
        # create some code to fetch products
    connection=pymysql.connect(host="localhost",user="root",password="",database="Kima") 
    #  define the sql querry to be executed
    clothessql="select * from products where product_category ='clothes'"
    # sql
    sql_smartphones='select * from products where product_category= "smartphones"'
    sql_detergents='select * from products where product_category= "detergents"'
    sql_laptops='select * from products where product_category= "laptops"'
    # create a cursor for smartphone
    cursor_smartphones=connection.cursor()
    # cursor for clothes
    clothescursor=connection.cursor()
    # cursor for the detergents
    cursor_detergents=connection.cursor()
    cursor_laptops=connection.cursor()
    # execute the querry
    clothescursor.execute(clothessql)
    # execute smartphone sql
    cursor_smartphones.execute(sql_smartphones)
    cursor_detergents.execute(sql_detergents)
    cursor_laptops.execute(sql_laptops)
    # check if there's clithes in the database
    if clothescursor.rowcount==0:
        return render_template("home.html",message="No Products Available")
    else: #you can fetch one, fetch many...
        clothe=clothescursor.fetchall() #create a variable to store clothes in this case ,myvariable
        smartphones=cursor_smartphones.fetchall()
        detergents=cursor_detergents.fetchall()
        laptops=cursor_laptops.fetchall()
        return render_template("home.html",myclothe=clothe,mysmartphones=smartphones,mydetergents=detergents,mylaptops=laptops)
# create a new route
@app.route("/single_item/<product_id>")    
def single_item(product_id):#pass the product id as a parameter
    # create the sqlquerry
    #pass the value of product id as %s placeholder-it will take the actual product_id during querying
    sql_single_item='select * from products where product_id=%s'
    # create a cursor to execute the sql
    cursor_single=connection.cursor()
    # execute the query
    cursor_single.execute(sql_single_item,product_id)
    single=cursor_single.fetchone() #we only need one row

    # code for fetching similar items
    category=single[4]
    sql2='select * from products where product_category=%s LIMIT 4'
    cursor2=connection.cursor()
    cursor2.execute(sql2,category)
    similar=cursor2.fetchall()


    return render_template("single.html",single_item=single,similar_products=similar)
# create a signup route that returns a signup.html template



@app.route("/vendor",methods=['POST','GET'])
def vendor():
#insert into users(firstname,email,lastname,password)
# VALUES(%s,%s,%s,%s)
# get posted details
# check if details have been posted
    if request.method=='POST':
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        town=request.form['town']
        password=request.form['password']
        confirm_password=request.form['confirm_password']
        # validation checks
        if "@" not in email:
            return render_template("vendor.html",error="Email Must Have @")
       
        elif len(password)<8:
            return render_template("vendor.html",error="Password must be atleast 8 characters")
        elif password != confirm_password:
            return render_template("vendor.html",error="Password Mismatch.Please Confirm Password")
        else:
            sql="insert into vendors(firstname,email,lastname,password,town)VALUES(%s,%s,%s,%s,%s)"
            #    create cursor -cursor is used to execute sql querry
            cursor=connection.cursor()

            #execute sql query
            cursor.execute(sql,(firstname,email,lastname,password,town))
            session["firstname"]=firstname
            # commit
            connection.commit()
            # add the sms code
            import sms
            sms.send_sms(lastname,f" Hello {firstname} Thank You For Creating an account with us")
    return render_template("vendor.html")


@app.route("/signup",methods=['POST','GET'])
def signup():
#insert into users(username,email,phone,password)
# VALUES(%s,%s,%s,%s)
# get posted details
# check if details have been posted
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        phone=request.form['phone']
        password=request.form['password']
        confirm_password=request.form['confirm_password']
        # validation checks
        if " " in username:
            return render_template("signup.html",error="username  must have one word")
        elif "@" not in email:
            return render_template("signup.html",error="Email Must Have @")
        elif not phone.startswith("+254"):
            return render_template("signup.html",error="Phone Must start with 254***")
        elif len(password)<8:
            return render_template("signup.html",error="Password must be atleast 8 characters")
        elif password != confirm_password:
            return render_template("signup.html",error="Password Mismatch.Please Confirm Password")
        else:
            sql="insert into users(username,email,phone,password)VALUES(%s,%s,%s,%s)"
            #    create cursor -cursor is used to execute sql querry
            cursor=connection.cursor()

            #execute sql query
            cursor.execute(sql,(username,email,phone,password))
            session["username"]=username
            # commit
            connection.commit()
            # add the sms code
            import sms
            sms.send_sms(phone,f" Hello {username} Thank You For Creating an account with us")
    return render_template("signup.html")
            #create a sign in route that returns signin.html template
@app.route("/signin",methods=['POST','GET'])
def signin():
    if request.method=='POST':
            email=request.form['email']
            password=request.form['password']
            # validation checks
    
            # create sql to select email and password
            sql='select * from users where email=%s and password=%s'
            #    create cursor -cursor is used to execute sql querry
            cursor=connection.cursor()

            #execute sql query
            cursor.execute(sql,(email,password))
            session['password']=password
            session['email']=email
            
            # check if there is a user with the details
            if cursor.rowcount==0:
                 #link session l
                return render_template("signin.html",error="No such user Account.Please Try Again")
            else:
                session['key'] = email
                return redirect("/")
             
                    
    else:

          
        return render_template("signin.html",Success="Welcome back")

    
    # @app.route("/about")
    # def about():
    #     return render_template("about.html")
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/signin')



# create m-pesa route
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/mpesa', methods=['POST', 'GET'])
def mpesa_payment():
    if request.method == 'POST':
        phone = str(request.form['phone'])
        amount = str(request.form['amount'])
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"#test paybill for saf
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return render_template("complete.html")
               

app.run(debug=True)