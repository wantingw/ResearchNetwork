from app import db 
from app.Controller.auth_routes import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


'''
User: 
    username, password,

Student:
    contact information (name, last name, WSU ID, email, phone) 
    Enter additional information (major, cumulative GPA, expected graduation date, 
    etc. ) 
    Enter the technical elective courses they completed and the grades they 
    received. 
    Select the research topics they are interested in.  
    Select the programming languages they have experience with.  
    Describe their prior research experience if there is any.  

faculty: 
    Enter contact information (name, last name, WSU ID, email, phone) 
'''

# @login.user_loader
# def load_user(id):
#     role = db.session.get('role')
#     return role_mapping[role].query.get(int(id))


class User(db.Model, UserMixin):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    wsuid = db.Column(db.Integer, unique = True)
    email = db.Column(db.String(128))
    firstname = db.Column(db.String(128))
    lastname = db.Column(db.String(128))
    level = db.Column(db.Integer, default = 1)  #Use this column determine this account belong to student or faculty, 1 - student; 2 - faculty, default on 1
    
    # student = db.relationship('Student', backref ='student_user',lazy = 'dynamic')
    # faculty = db.relationship('Faculty', backref ='faculty_user',lazy = 'dynamic')

    def __repr__(self):
        return '<User {}, {}>'.format(self.id,self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password) 
    
    def get_password(self, password):
        return check_password_hash(self.password_hash, password)

# class Student(User):
#     role = db.Column(db.Integer, default=0)

# class Faculty(User):
#     role = db.Column(db.Integer, default=1)

# role_mapping = {
#     'student': Student,
#     'teacher': Faculty
# }

class Position(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(2048))
    desc = db.Column(db.String(2048))
    start_date = db.Column(db.String(128))
    end_date = db.Column(db.String(128))
    time_commitment = db.Column(db.String(128))
    research_field = db.Column(db.String(128))
    applicant_qualification = db.Column(db.String(1024))
