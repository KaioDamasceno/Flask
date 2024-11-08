from flask import Blueprint, render_template, request

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    username = request.cookies.get("username")
    return render_template("index.html", username=username)
