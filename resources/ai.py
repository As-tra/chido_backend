from flask.views import MethodView
import google.generativeai as genai
from flask_smorest import Blueprint, abort
import os
import ast
from schema import AiSchema,SkillsSchema
from dotenv import load_dotenv

blp = Blueprint("ai", __name__, description="generate content for cv")


@blp.route("/ai/<string:title>")
class Skills(MethodView):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    @blp.response(200, SkillsSchema)
    def get(self, title):
        try:
            prompt = f"""
            Analyze the following input provided by the user: {title}. 
            1. If the input is a clear job title or role (e.g., "Software Engineer," "Graphic Designer"), extract and suggest a comprehensive list of relevant skills for that job title to help the user build their CV. 
            2. If the input is random text (e.g., hobbies, interests, or general knowledge), or areas of expertise mentioned by the user.
            3. In both cases, suggest additional relevant or related skills that align with the context of the input to enhance the user's CV.

            Format the output as a Python array, like this: ['skill1', 'skill2', 'skill3', ...].
            Ensure the skills are relevant to the input provided and minimum of 8 skills.
            """
            response = self.model.generate_content(prompt)
            skills = ast.literal_eval(response.text)
            return {"skills": skills}
        except Exception as e:
            abort(500, message=f"An error occurred: {str(e)}")
            
@blp.route("/ai")
class CVList(MethodView):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro') 
    @blp.arguments(AiSchema)
    @blp.response(200, AiSchema)
    def get(self, data):
        try:
            prompt_prefix = f"make a better version of this {data['type'].value} description that it will be added to my cv"
            if data.get('job_title'):
                prompt_prefix += f" for the role of {data['job_title']}"
            prompt_prefix += " to make it clearer, more consistent, and engaging."

            full_prompt = f"{prompt_prefix}\n\nHere is the description:\n{data['content']}\nProvide only the reformatted version without any additional text or introductions."
            response = self.model.generate_content(full_prompt)
            data["content"] = response.text
            return data
        except genai.GenAIError as e:
            abort(500, message=f"Gemini API error: {str(e)}")
        except Exception as e:
            abort(500, message=f"An unexpected error occurred: {str(e)}")