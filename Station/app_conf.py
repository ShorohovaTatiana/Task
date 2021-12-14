from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Tatisha2001@localhost/postgres"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # ??? Если не прописать, то будет Warning
    ##SECRET_KEY = 'we4fh%gC_za:*8G5v=fbv' # для дебага как я понял


app = Flask(__name__)
engine = create_engine("postgresql://localhost:5432/postgres")
app.config.from_object(Config())
##db = SQLAlchemy(app)
db = SQLAlchemy(app=app, session_options={'autoflush': False})
##jdbc:postgresql://localhost:5432/postgres