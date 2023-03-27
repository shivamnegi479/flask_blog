ay=date.today()
# app=Flask(__name__)
# if local_server==True:
#     app.config['SQLALCHEMY_DATABASE_URI']=file['local_uri']
# else:
#     app.config['SQLALCHEMY_DATABASE_URI']=file['server_uri']
# db=SQLAlchemy()
# db.init_app(app)

# class contacts(db.Model):
#     s_no = db.Column(db.Integer, primary_key=True)
#     phone = db.Column(db.Integer)
#     message = db.Column(db.String)
#     name = db.Column(db.String, nullable=False)
#     date = db.Column(db.String)
#     email = db.Column(db.String)
# @app.route('/')
# def method_name():
#     return {
#         "name":"shivam"
#     }

# @app.route('/index')
# def home():
#     return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/post')
# def post():
#     return render_template('post.html')
# @app.route('/contact',methods=['GET','POST'])
# def contact():
#     if request.method=="POST":
#         user = contacts(
#             name=request.form["name"],
#             email=request.form["email"],
#             phone=request.form['phone'],
#             message=request.form['message'],
#             date=today
#         )
#         db.session.add(user)
#         db.session.commit()
#     return render_t