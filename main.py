import os
from flask import Flask, render_template, request
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.json.get('prompt')  # Get input from frontend

    # ✅ Use environment variable
    openai_key = os.environ.get("OPENAI_API_KEY")
    if not openai_key:
        return "OPENAI_API_KEY is not set", 500

    # Setup prompt and chain
    prompt = PromptTemplate.from_template("Generate a blog on title {title}?")
    llm = OpenAI(temperature=0.4, api_key=openai_key)
    chain = LLMChain(llm=llm, prompt=prompt)
    output = chain.run({'title': user_input})

    return output


app.run(host='0.0.0.0', port=81)
