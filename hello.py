from flask import Flask
from flask import request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import re
app = Flask(__name__)



class RegistrationForm(Form):
    username = StringField('username', [validators.Length(min=4, max=25),
    validators.Regexp('^[a-zA-Z]+$',message=('Failure: only characters allowed in username'))
    ])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.Length(min=6,max=25,message=('Failure:password should be of length 6')),
        validators.Regexp('.*[0-9].*',message=('Failure:password to have 1 character and 1 number')),
    ])

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login',methods=['POST','GET'])
def login():
    data = {}
    password = request.form['password']
    # if request.method =='POST':
    #     if(request.form['username']=='vaibhav'):
    #         password = request.form['password']
    #         if(len(password)<6):
    #             return {"status": 201,
    #                     "msg": "Failure: password should be of length 6" },201
    #         elif()
    #         return {
    #             'msg': 'Success'
    #         }
    #     else:
    #         data['error']="Invalid username/password"
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        if(not(form.validate())):
            umessage = form.username.errors
            pmessage = form.password.errors
            if(len(umessage)==0 and len(pmessage)>2):
                data['msg']= pmessage[0]
                return data,201
            elif len(umessage)>0:
                data['msg']=umessage[0]
                return data,203
            elif len(pmessage)==1:
                print('202 present')
                data['msg']= pmessage[0]
                return data,202
        elif(password=='abcd12'):
                data['msg']='Success'
                return data,200
        # elif (len(form.password.errors)>1):
        #     print("202 present")
        #     pmessage= form.password.errors



    data['msg']= 'Failure:password should be of length 6'
    return data,201