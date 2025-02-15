from db import db


class EducationModel(db.Model):
    
    __tablename__ = "education"
    
    id = db.Column(db.Integer, primary_key=True)
    university_name = db.Column(db.String(50))
    speciality = db.Column(db.String(40),nullable=False)
    start_year = db.Column(db.Integer)
    end_year = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), unique=False, nullable=False)
    user = db.relationship("UserModel",back_populates="educations")
    
