"""
CVE-2023-30861 触发代码
Flask < 2.3.2 在设置 session cookie 时未正确限制 path，
导致同域其他路径下的恶意页面可窃取 session cookie。
此文件中显式调用 session.permanent = True 以触发可达性分析。
"""
from flask import Flask, session

app = Flask(__name__)
app.secret_key = "eval-fixture-secret-key"


@app.route("/login")
def login():
    # 这一行是 analyze_reachability 需要匹配的关键证据
    session.permanent = True
    session["user"] = "eval_user"
    return "logged in"


if __name__ == "__main__":
    app.run(debug=True)