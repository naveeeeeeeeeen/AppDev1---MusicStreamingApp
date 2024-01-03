from flask import Flask
from models import db
import secrets

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.sqlite3'
    app.secret_key = secrets.token_hex(16)
    db.init_app(app)
    with app.app_context():
        import routes
        import app_data
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    
