from extensions import db
import json

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    needed_volunteers = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    registered_users = db.Column(db.Text, default='[]')  # ואז תעבוד עם json.loads ו-json.dumps
    is_approved = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date.isoformat() if self.date else None,
            "time": self.time.strftime('%H:%M:%S') if self.time else None,
            "location": self.location,
            "needed_volunteers": self.needed_volunteers,
            "registered_users": json.loads(self.registered_users) if self.registered_users else [],
            "description": self.description,
            "is_approved": self.is_approved,
            "created_by": self.created_by
        }
