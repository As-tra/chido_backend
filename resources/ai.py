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
            prompt =f"Analyze the following description provided by the user: '{title}'. Identify and extract all relevant skills, knowledge, or areas of expertise mentioned by the user. Format the output as a Python array, like this: ['skill1', 'skill2', 'skill3', ...]. Ensure the skills are specific, clear, and directly derived from the user's description."
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