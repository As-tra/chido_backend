from db import db
from enums import GenderEnum
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, primary_key=True)
    created_At = db.Column(db.Date, nullable=False,default=datetime.now())
    full_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.Enum(GenderEnum),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    phone = db.Column(db.String(50),nullable=False)
    country = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    portfolio_url = db.Column(db.String(50))
    github_url = db.Column(db.String(50))
    linkedin_url = db.Column(db.String(50))
    title = db.Column(db.String(50))
    
    educations = db.relationship("EducationModel",back_populates="user",lazy="dynamic")
    projects = db.relationship("ProjectModel",back_populates="user",lazy="dynamic")
    experience = db.relationship("ExperienceModel",back_populates="user",lazy="dynamic")
    # Here skills will stored in json objectd
    skills = db.Column(db.JSON)
    languages = db.Column(db.JSON)
    activities = db.Column(db.JSON)
    