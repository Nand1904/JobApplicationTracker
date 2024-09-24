from . import db

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    date_applied = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(50), default='Applied')
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<JobApplication {self.company} - {self.position}>'