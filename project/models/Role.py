from project import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    rolename = db.Column(db.String(255), unique=True)