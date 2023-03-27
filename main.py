from flask import Flask,render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from flask_mail import Mail
from flask_mail import Message
import os
from werkzeug.utils import secure_filename
import json
import math
import datetime
nondate=datetime.date.today()
with open ('config.json','r') as e:
    file=json.load(e)['params']
local_server=True
today=date.today()
app=Flask(__name__)
app.config.update(
    MAIL_SERVER ='smtp.gmail.com',
    MAIL_PORT =  '465',
    MAIL_USE_SSL = 'True',
    MAIL_USERNAME = file["gmail_user"],
    MAIL_PASSWORD = file["gmail_pass"]
)

app.config["Upload"]=file["upload_loacton"]
mail=Mail(app)

if local_server==True:
    app.config['SQLALCHEMY_DATABASE_URI']=file['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI']=file['local_uri']

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask1'
db=SQLAlchemy()
db.init_app(app)

class contacts(db.Model):
    s_no = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer)
    message = db.Column(db.String)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.String)
    email = db.Column(db.String)

class Post(db.Model):
    s_no = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String)
    content = db.Column(db.String)
    date = db.Column(db.String)
    title = db.Column(db.String)
    img_file = db.Column(db.String)
app.secret_key = 'super secret key'
name=file["admin"]
@app.route('/')
@app.route('/index')
def home():
    posts=Post.query.filter_by().all()
    last=math.ceil(len(posts)/int(file['no_of_post']))

    page=(request.args.get('page'))
    if(not str(page).isnumeric()):
        page=1
    page=int(page)
    posts=posts[(page-1)*int(file['no_of_post']):(page-1)*int(file['no_of_post'])+int(file['no_of_post'])]
    if page==1:
        prev="javascript:void(0)"
        next="/?page="+str(page+1)
    elif(page==last):
        next="javascript:void(0)"
        prev="/?page="+str(page-1)
    else:
        next="/?page="+str(page+1)
        prev="/?page="+str(page-1)  
    return render_template('index.html',param=file,posts=posts,dates=nondate,name=name,prev=prev,next=next)

@app.route('/about')
def about():
    return render_template('about.html',param=file)

@app.route('/uploader',methods=["GET","POST"])

def uploader():
    if ('user' in session and session['user']==file['admin_user']):
        if request.method=="POST":
            r=request.files['file1']
            r.save(os.path.join(app.config["Upload"],secure_filename(r.filename)))
            return "Upload Successfully"
    # return render_template('about.html',param=file)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')
@app.route('/post/<string:post_slug>',methods=['GET'])
def post_route(post_slug): 
    post=Post.query.filter_by(slug=post_slug).first()
    if post.date==None:
        post.date=nondate
    return render_template('post.html',param=file,post=post,name=name)

# @app.route('/post',methods=['GET'])
# def all_post():
#     post=Post.query.filter_by().all().firs
#     print(post.img_file)
#     return render_template('post.html',param=file,post=post,name=name)

@app.route('/contact',methods=['GET','POST'])

def contact():
    if request.method=="POST":
        user = contacts(
            name=request.form["name"],
            email=request.form["email"],
            phone=request.form['phone'],
            message=request.form['message'],
            date=today
        )
        db.session.add(user)
        db.session.commit()
        msg = Message("Hello",
                  sender=user.email,
                  recipients=[file["gmail_user"]])
        msg.body = F"{user.message} AND \n Number: {user.phone}" 
        mail.send(msg)
    return render_template('contact.html',param=file)

@app.route('/dashboard',methods=['GET','POST'])
def sing_in():
    post=Post.query.filter_by().all()
    for i in post:
        if i.date==None:
            i.date=nondate
    
    if ('user' in session and session['user']==file['admin_user']):
        return render_template("/dashboard.html",post=post,param=file)
    
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        if username==file["admin_user"] and password==file["admin_pass"]:
            session['user']=username
            return render_template('/dashboard.html',post=post,param=file)
        else:
            return render_template("/sign_in.html")
    else:
        return render_template('/sign_in.html')


@app.route('/delete/<string:s_no>',methods=["GET","POST"])
def delete(s_no):
    if ('user' in session and session['user']==file['admin_user']):
        post=Post.query.filter_by(s_no=s_no).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')

@app.route('/name/<name>')
def getname(name):
    if ('user' in session and session['user']==file['admin_user']):
        if name=="shivam":
            return render_template('/about.html')
        else:
            return redirect('/contact')
    else:
        #  return redirect('post/first-blog')
        return render_template('/sign_in.html')

@app.route('/edit/<string:s_no>',methods=["GET","POST"])
def edit(s_no):
    if ('user' in session and session['user']==file['admin_user']):
        if request.method=="POST":
            title=request.form['title']
            slug=request.form['slug']
            img_file=request.form['img_file']
            content=request.form['content']
            date=today
            print(s_no)
            # post=Post.query.filter_by().all()
            if s_no=='0':
                post=Post(slug=slug,content=content,date=date,title=title,img_file=img_file)
                db.session.add(post)
                db.session.commit()
            else:
                post=Post.query.filter_by(s_no=s_no).first()
                post.title=title
                post.content=content
                post.img_file=img_file
                post.slug=slug
                post.date=date
                db.session.commit()
                return redirect('/edit/'+s_no)
        post=Post.query.filter_by(s_no=s_no).first()
        return render_template('/edit.html',param=file,post=post,s_no=s_no)
    else:
        return render_template('/sign_in.html')
            # return "hello word"
app.run(debug=True)