import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///job_applications.db'  # Use SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
