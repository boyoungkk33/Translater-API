from flask import Flask, request, render_template
import openai
openai.api_key = ""

app = Flask(__name__)


@app.route("/translater", methods=["post"])
def translater():
    data = request.json
    language = data["language"]
    text = data["text"]

    prompt = f"{text}\n\nTranslate this sentence into {language}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "you are a translater"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=500,
    )
    return response["choices"][0]["message"]["content"]


@app.route("/web")
def web():
    return render_template("index.html")


@app.route("/")
def index():
    return "Hello World"


app.run(host="0.0.0.0", port=80)
