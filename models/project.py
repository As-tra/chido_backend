from db import db


class ProjectModel(db.Model):
    
    __tablename__ = "projects"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(500),nullable=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    role = db.Column(db.String(50), nullable=True)
    project_url = db.Column(db.String(50),nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), unique=False, nullable=False)
    user = db.relationship("UserModel",back_populates="projects")
