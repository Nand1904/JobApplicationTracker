import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'e27de455972c1739859612a812cabcee')  # Set a default for development
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///job_applications.db')  # Default to SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False