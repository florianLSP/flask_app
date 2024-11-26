from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    mylist = ["Florian", "Eva", "Théo"]
    return render_template("index.html", mylist=mylist)


@app.route("/other")
def other():
    myvalue = 'Some Text'
    return render_template("other.html", myvalue=myvalue)


if __name__ == "__main__":
    app.run(debug=True)
