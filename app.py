# app.py

from flask import Flask
from routes import inventario_routes

def create_app():
    """Cria e configura uma instância da aplicação Flask."""
    app = Flask(__name__)
    app.register_blueprint(inventario_routes)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)