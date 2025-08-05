import os
import flask
import random

password = os.getenv("password")
app = flask.Flask(__name__)

def return_random_key():
    "返回随机 API Key"
    with open("config/key", "r", encoding="utf-8") as f:
        keys = f.readlines()
    return random.choice(keys).strip()
def return_all_key():
    """返回所有 API Key"""
    with open("config/key", "r", encoding="utf-8") as f:
        keys = f.readlines()
        keys = [ i.strip() for i in keys ]
    return keys # Keys Not Kiss (^_^)

@app.route("/")
def index():
    return flask.Response(status=404)

@app.route("/api/random", methods=["GET", "POST"])
def random_key():
    if password is None:
        """无密码设置"""
        return flask.Response(status=403)
    elif flask.request.method == "POST" and flask.request.form.get("password") == password:
        """处理 POST 请求"""
        return return_random_key()
    elif flask.request.method == "GET" and flask.request.args.get("password") == password:
        """处理 GET 请求"""
        return return_random_key()
    else:
        """啥也不是"""
        return flask.Response(status=403)

@app.route("/api/all", methods=["GET", "POST"])
def all_key():
    if password is None:
        """无密码设置"""
        return flask.Response(status=403)
    elif flask.request.method == "POST" and flask.request.form.get("password") == password:
        """处理 POST 请求"""
        return return_all_key()
    elif flask.request.method == "GET" and flask.request.args.get("password") == password:
        """处理 GET 请求"""
        return return_all_key()
    else:
        """啥也不是"""
        return flask.Response(status=403)

@app.route("/api/")
def no_content():
    return flask.Response(status=404)

if __name__ == "__main__":
    app.run()