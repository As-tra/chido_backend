from db import db
from enums import EmploymentType


class ExperienceModel(db.Model):
    
    __tablename__ = "experience"
    
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(50))
    job_description = db.Column(db.String(500))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    company = db.Column(db.String(50))
    company_url = db.Column(db.String(50),nullable=True)
    location = db.Column(db.String(50),nullable=True)
    type = db.Column(db.Enum(EmploymentType),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), unique=False, nullable=False)
    user = db.relationship("UserModel",back_populates="experience")
