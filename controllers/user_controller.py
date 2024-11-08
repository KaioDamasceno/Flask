from flask import Blueprint, render_template, session, abort

user_bp = Blueprint("user", __name__)

@user_bp.route("/user")
def user_page():
    if session.get("role") != "user":
        abort(403)  # Redireciona para a página de erro 403 se o usuário não for 'user'
    return render_template("user_page.html")
