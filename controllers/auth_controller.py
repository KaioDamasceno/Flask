from flask import Blueprint, render_template, request, redirect, url_for, session, flash, make_response
from models.user_model import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if User.validate_login(username, password):
            session["username"] = username
            session["role"] = User.get_user_role(username)
            resp = make_response(redirect(url_for("main.index")))
            resp.set_cookie("username", username)
            flash("Login realizado com sucesso!", "success")
            return resp
        else:
            flash("Nome de usuário ou senha incorretos", "error")
            return redirect(url_for("auth.login"))
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("role", None)
    resp = make_response(redirect(url_for("main.index")))
    resp.set_cookie("username", "", expires=0)
    flash("Logout realizado com sucesso!", "info")
    return resp
