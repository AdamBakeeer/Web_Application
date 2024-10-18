from app import db

class Properties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(500), index=True, unique=True)
    duration = db.Column(db.Integer)
    rent = db.Column(db.Float) 