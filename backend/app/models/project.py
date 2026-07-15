from datetime import datetime
from app import db


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)

    project_name = db.Column(db.String(200), nullable=False)

    github_url = db.Column(db.String(500))

    uploaded_file = db.Column(db.String(500))

    status = db.Column(db.String(50), default="Pending")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)