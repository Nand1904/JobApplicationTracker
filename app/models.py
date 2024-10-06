from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Add this line
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    date_applied = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.Text, nullable=True)

    user = db.relationship('User', backref='applications')  # Add relationship
    def __repr__(self):
        return f'<JobApplication {self.company} - {self.position}>'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)  # Add this line
    password = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        """Hash the password and store it."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password against a provided password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'