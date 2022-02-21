from db_config import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    dependents = db.relationship('Dependent', backref='employee', lazy=True)

    
    def __repr__(self):
        return '<Employee %r>' % self.name