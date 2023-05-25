from flask_sqlalchemy import SQLAlchemy
from config.default import config

from datetime import datetime
import uuid

db = SQLAlchemy()
database_path = config['DATABASE_URI']

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    db.app = app
    db.init_app(app)
    db.create_all()

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text('uuid_generate_v4()'))
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    job_title = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text('now()'))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, onupdate=datetime.utcnow, server_default=db.text('now()'))
    image_path = db.Column(db.String(500), nullable=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    department_id = db.Column(db.String(36), db.ForeignKey('departments.id'), nullable=False)

    def __init__(self, first_name, last_name, job_title, department_id):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.created_at = datetime.utcnow()
        self.department_id = department_id
        self.is_active = True

    def __repr__(self):
        return '<Employee %r %r>' % (self.first_name, self.last_name)
    

    def serialize(self):
        created_at_str = datetime.strftime(self.created_at, "%B %d of %Y at %I:%M %p")
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'job_title': self.job_title,
            'created_at': created_at_str,
            'image_path': self.image_path
        }
    

class Department(db.Model):
    __tablename__ = 'departments' 
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text('uuid_generate_v4()'))
    name = db.Column(db.String(120), nullable=False)
    short_name = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text('now()'))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, onupdate=datetime.utcnow, server_default=db.text('now()'))
    employees = db.relationship('Employee', backref='department', lazy=True)

    def __init__(self, name, short_name):
        self.name = name
        self.short_name = short_name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'short_name': self.short_name,
            'created_at': self.created_at,
        }