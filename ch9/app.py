from flask import Flask, json
from flask import request
from flask import render_template
from markupsafe import escape

app = Flask(__name__)


# router
@app.route("/")  # localhost:3000/
def index():
    # handler
    # akan menjadi gerbang
    # awal code untuk menerima
    # request
    # ketika kita akses localhost:3000/ => <p>Hello, World!</p>
    print("hello world called")
    return "<p>Hello, World!</p>"


# path variable
@app.route("/users/<greet>/<username>")  # type: ignore
def call_name(greet, username):
    # path variable,
    # dengan passing melalui input function
    print(username, greet)
    return f"{escape(greet)}, {escape(username)}!"


# Challenge:
# membuat API untuk:
# 1 mendapatkan seluruh users (GET /users)
# 2 menambahkan user (POST /users)
# 3 mendapatkan user dengan id (GET /users/:id)
# 4 mengedit user dengan id tertentu
# 5 delete user dengan id tertentu

users_data = []


# router bisa kita beri nama
# API path
@app.route("/users", methods=["GET", "POST"])  # type: ignore
def users():
    if request.method == "GET":
        # dictionary akan mengembalikan
        # data dalam bentuk json
        return users_data
    elif request.method == "POST":
        body = request.get_json()
        users_data.append(body)
        return {"status": "ok"}


@app.route("/users/<int:id>")  # type: ignore
def user_by_id(id):
    return users_data[id]


# templates route
@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    # host => menunjukkan address dari server
    # port => cara mengakses aplikasi yang running
    #
    app.run("0.0.0.0", 3000)
