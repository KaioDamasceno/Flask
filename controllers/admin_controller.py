from flask import Blueprint, render_template, session, abort

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin")
def admin_page():
    if session.get("role") != "admin":
        abort(403)  # Redireciona para a página de erro 403 se o usuário não for 'admin'
    return render_template("admin_page.html")
