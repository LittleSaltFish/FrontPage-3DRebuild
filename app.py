from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/zone3")
def re3():
    return render_template("introduction-第三展区.html")


@app.route("/zone2")
def re2():
    return render_template("introduction-武汉工业大学部分讲解.html")


@app.route("/zone1")
def re1():
    return render_template("introduction-理工大部分讲解稿.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5001,debug=True)
