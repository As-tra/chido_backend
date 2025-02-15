from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import *
from schema import *

blp = Blueprint("cv", __name__, description="Operations on cv")

@blp.route("/cv")
class CVList(MethodView):
    
    @blp.arguments(CVSchema)
    @blp.response(201)
    def post(self,cv_data):
        user = UserModel(**cv_data["user"])
        try:
            # add the user
            db.session.add(user)
            db.session.commit()
            # add his related info
            user_id = user.user_id
            educations = [EducationModel(user_id=user_id, **edu) for edu in cv_data.get("educations", [])]
            projects = [ProjectModel(user_id=user_id, **proj) for proj in cv_data.get("projects", [])]
            experiences = [ExperienceModel(user_id=user_id, **exp) for exp in cv_data.get("experience", [])]
            # Add all objects to the session
            db.session.add_all(educations)
            db.session.add_all(projects)
            db.session.add_all(experiences)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while adding the data.")

        return {"message":"data added"}
    
    # @blp.response(200)
    # def get(self):
    #     users = []
    #     for user in  UserModel.query.all():
    #         educations = user.educations.all()
    #         projects = user.projects.all()
    #         experience = user.experience.all()
    #         print(user)
    #         users.append({
    #             'user': UserSchema().dumps(user),
    #             'educations': [EducationSchema().dumps(edu) for edu in educations],
    #             'projects': [ProjectSchema().dumps(proj) for proj in projects],
    #             'experience': [ExperienceSchema().dumps(exp) for exp in experience]
    #         })
    #     return {"users":users}