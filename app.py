from flask import Flask, render_template
from config import Config
from controllers.auth_controller import auth_bp
from controllers.main_controller import main_bp
from controllers.user_controller import user_bp
from controllers.admin_controller import admin_bp

app = Flask(__name__)
app.config.from_object(Config)

# Middleware para rodar antes de cada requisição
@app.before_request
def before_request_middleware():
    print("Middleware: requisição recebida!")

# Registra os Blueprints dos controladores
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

# Páginas de erros personalizadas
@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404

@app.errorhandler(401)
def unauthorized(e):
    return render_template("errors/401.html"), 401

@app.errorhandler(403)
def forbidden(e):
    return render_template("errors/403.html"), 403

if __name__ == "__main__":
    app.run(debug=True)
