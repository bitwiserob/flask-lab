from flask import Flask, render_template, request

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


@app.route("/form")
def form():
    return render_template('form.html')


@app.route("/get_request", methods=['GET'])
def get_request():
    name = request.args.get('name', 'Guest')
    age = request.args.get('age', 'Unknown')

    return render_template('display_get.html', name=name, age=age)

@app.route("/post_request", methods=['POST'])
def post_request():
    pass