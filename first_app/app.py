from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return "flask_app"


@app.route("/hello", methods=["GET", "POST"])
def hello():
    return "Hello\n", 201


@app.route("/hello2", methods=["GET", "POST"])
def hello2():
    if request.method == "GET":
        return "You made a GET request\n"
    elif request.method == "POST":
        return "You made a POST request\n"


@app.route("/hello3", methods=["GET", "POST"])
def hello3():
    response = make_response("Hello\n")
    response.status_code = 202
    response.headers["content-type"] = "text/plain"
    return response


@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"


@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    return f"{number1} + {number2} = {number1+number2}"


@app.route("/handle_url_params")
def handle_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        greeting = request.args["greeting"]
        name = request.args.get("name")
        return f"{greeting}, {name}"
    else:
        return "Some parameters are missing"


if __name__ == "__main__":
    app.run(debug=True)