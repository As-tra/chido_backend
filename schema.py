from marshmallow import Schema, fields
from enums import GenderEnum,EmploymentType,GenerationTypes


class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    created_At = fields.DateTime(dump_only=True)
    full_name = fields.Str(required=True)
    title = fields.Str(required=True)
    gender = fields.Enum(GenderEnum,required=True)
    age = fields.Int(required=True)
    phone = fields.Str(required=True)
    country = fields.Str(required=True)
    email = fields.Str(required=True)
    portfolio_url = fields.Str()
    github_url = fields.Str()
    linkedin_url = fields.Str()
    skills = fields.List(fields.Str())
    languages = fields.List(fields.Str())
    activities = fields.List(fields.Str())
    
class EducationSchema(Schema):
    id = fields.Int(dump_only=True)  
    user_id = fields.Int(dump_only=True)
    university_name = fields.Str(required=True)
    speciality = fields.Str(required=True)
    start_year = fields.Int(required=True)
    end_year = fields.Int(required=True)
    

# Schema for the 'projects' table
class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)  
    user_id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    role = fields.Str()
    project_url = fields.Str()

# Schema for the 'experience' table
class ExperienceSchema(Schema):
    id = fields.Int(dump_only=True) 
    user_id = fields.Int(dump_only=True)
    company = fields.Str(required=True)
    company_url = fields.Str()
    location = fields.Str(required=True)
    job_title = fields.Str(required=True)
    job_description = fields.Str(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    type = fields.Enum(EmploymentType,required=True)    

class CVSchema(Schema):
    user = fields.Nested(UserSchema, required=True)
    educations = fields.List(fields.Nested(EducationSchema))
    projects = fields.List(fields.Nested(ProjectSchema))
    experience = fields.List(fields.Nested(ExperienceSchema))
    

class AiSchema(Schema):
    type = fields.Enum(GenerationTypes,required=True)
    title = fields.Str()
    content = fields.Str(required=True)


class SkillsSchema(Schema):
    skills = fields.List(fields.Str)
    
