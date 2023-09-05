import hashlib
from random import randint
from flask import Flask,redirect, request, session,url_for,render_template
from flask_mysqldb import MySQL

from flask_mail import *

from user import user_operation

app=Flask(__name__)
app.secret_key="super secret key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='sabarishofficial2004@gmail.com'
app.config['MAIL_PASSWORD']='sjnhzenunefsdlbv'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)

otp=randint(0000,9999) 
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/submit',methods=['POST','GET'])   
def submit():
    msg=''
    f=0
    if request.method=='POST':
        try:
            email=str(request.form['email'])
            username=str(request.form['username'])
            password=str(request.form['password'])
            cursor = mysql.connection.cursor()

            
            cursor.execute('Select * from customer_details')
            c=cursor.fetchall()
            for i in c:

                if(i[3]==email):
                    if(i[2]==username):
                        if(i[5]==password):
                            return redirect(url_for('first'))
                        else:
                            msg='Invalid password'
                            break
                            
                    else:
                         msg='Invalid username'
                         break
                else:
                     msg='Invalid Email'



        except:
            return render_template('index.html',msg=msg)
    return render_template('index.html',msg=msg)
        
name=''  
username=''
password=''   
email=''
dob=''  
otp=randint(0000,9999) 


@app.route('/signup',methods=['POST','GET'])
def signup():
     
    if request.method=='POST':
        msg=''
        try:
        
            name=str(request.form['name'])
            username=str(request.form['Username'])
            password=str(request.form['password'])
            email=str(request.form['email'])
            dob=str(request.form['dob'])
            
            cursor = mysql.connection.cursor()

            cursor.execute('Select * from customer_details')
            c=cursor.fetchall()
            for i in c:
                if(i[2]==username):
                    msg='Invalid username'
                    return render_template('index.html',msg1=msg)
                elif(i[3]==email):
                    msg='Invalid email'
                    return render_template('index.html',msg1=msg)
                
            msg=Message('OTP',sender='santhoshdhana88@gmail.com',recipients=[email])
            msg.body=str(otp) 
            
            mail.send(msg)

            # op = user_operation()
            # op.user_signup_insert(name,username,email,password,dob)
            
            return render_template('verify.html',email=email,username=username,name=name,password=password,dob=dob)



        except Exception as e:
            print(e)
            msg='Invalid username or email'
            return render_template('index.html',msg1=msg)
    else:
        return render_template('first.html')
    



@app.route('/verify',methods=['POST'])
def verify():
    try:
        if request.method=='POST':
            
            userotp1=(request.form['otp1'])
            userotp2=(request.form['otp2'])
            userotp3=(request.form['otp3'])
            userotp4=(request.form['otp4'])
       
            userotp=((int)(userotp1)*1000+(int)(userotp2)*100+(int)(userotp3)*10+(int)(userotp4))


            name=str(request.form['name'])
            username=str(request.form['username'])
            password=str(request.form['password'])
            email=str(request.form['email'])
            dob=str(request.form['dob'])
            
            
            if otp == int(userotp):
                print("hiii")
                op = user_operation()
                op.user_signup_insert(name,username,email,password,dob)
                return redirect(url_for('first'))
            else:
                msg='Invalid otp'
                return render_template('verify.html',msg=msg,email=email,username=username,name=name,password=password,dob=dob)

    except Exception as e:
         msg='Invalid otp'
         return render_template('verify.html',msg=msg,email=email,username=username,name=name,password=password,dob=dob)



@app.route('/fertilizer')
def fertilizer():
   return render_template("fertilizer.html")

@app.route('/about')
def about():
   return render_template("about.html")

@app.route('/crop')
def crop():
   return render_template("crop.html")

@app.route('/season')
def season():
   return render_template("season.html")

@app.route('/contact')
def contact():
   return render_template("contact.html")

if __name__=='__main__':
    app.run(debug=True)