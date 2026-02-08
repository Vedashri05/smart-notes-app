import os
import pickle
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

load_dotenv()
db=SQLAlchemy()

def create_app():

    app=Flask(__name__)

    #---------- LOAD ML FILES --------
    base_dir=os.path.dirname(os.path.dirname(__file__))

    app.model=pickle.load(open(os.path.join(base_dir,"ml/lr_model.pkl"),"rb"))
    app.vectorizer=pickle.load(open(os.path.join(base_dir,"ml/vectorizer.pkl"),"rb"))
    app.label_encoder=pickle.load(open(os.path.join(base_dir,"ml/label_encoder.pkl"),"rb"))

    app.config["SECRET_KEY"]=os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"]=(
        f"mysql+pymysql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}/"
        f"{os.getenv('DB_NAME')}"
    )
    app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"]=False

    #remember me session duration - 7 days
    app.permanent_session_lifetime=timedelta(days=7)

    db.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.notes import notes_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp)
    return app