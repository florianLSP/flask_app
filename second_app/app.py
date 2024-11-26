from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    mylist = ["Florian", "Eva", "Théo"]
    return render_template("index.html", mylist=mylist)


@app.route("/other")
def other():
    myvalue = 'Some Text'
    return render_template("other.html", myvalue=myvalue)


@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]


if __name__ == "__main__":
    app.run(debug=True)
