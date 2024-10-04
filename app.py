from flask import Flask, render_template, request
import google.generativeai as genai
from google.generativeai import GenerationConfig
import os
import json 

genai.configure(api_key="AIzaSyAFDb8vis8Ze8laQfFbwBTd0RRq-0eceTM")
model = genai.GenerativeModel("gemini-1.5-flash")



app = Flask(__name__)

# Basic Route
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hi")
def hi_world():
    return "<p>hi, World!</p>"

@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/form", methods=["GET"])
def form():
    return render_template('form.html')


@app.route("/get_request", methods=['GET'])
def get_request():
    name = request.args.get('name', 'Guest')
    age = request.args.get('age', 'Unknown')
    return render_template('display_get.html', name=name, age=age)



@app.route("/movie_review", methods=['GET'])
def review_movie():
    movie_name = request.args.get("movie_name",'Nan')
    response_schema = {
   "type": "ARRAY",
        "items": {
            "type": "OBJECT",
            "properties": {
                "movie_name": {"type": "STRING"},
                "movie_review": {"type": "STRING"},
            },
        },
    }
    
    prompt = f"review {movie_name}"
    response=model.generate_content(
        prompt,
        generation_config=GenerationConfig(
            response_mime_type="application/json", response_schema=response_schema
        )
    
    )
    json_obj = json.loads(response.text) 
    
    return render_template("movie_review.html",movie_review=json_obj)



@app.route("/post_request", methods=['POST'])
def post_request():
    pass