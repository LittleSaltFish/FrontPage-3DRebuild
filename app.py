from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/zone4")
def re4():
    return render_template("第四展区.html")

@app.route("/zone3")
def re3():
    return render_template("第三展区.html")


@app.route("/zone2")
def re2():
    return render_template("第二展区.html")


@app.route("/zone1")
def re1():
    return render_template("第一展区.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5001,debug=True)
