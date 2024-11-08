class User:
    @staticmethod
    def validate_login(username, password):
        # Simulação de validação do usuário
        return username == "admin" and password == "password" or username == "user" and password == "password"

    @staticmethod
    def get_user_role(username):
        # Simula o papel do usuário: 'admin' ou 'user'
        return "admin" if username == "admin" else "user"
