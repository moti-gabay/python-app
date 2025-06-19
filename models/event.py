from extensions import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    needed_volunteers = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    registered_count = db.Column(db.Integer, default=0)
    is_approved = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date.isoformat() if self.date else None,  # ✅ תיקון כאן
            "time": self.time.strftime('%H:%M:%S') if self.time else None,
            "location": self.location,
            "needed_volunteers": self.needed_volunteers,
            "registered_count": self.registered_count,
            "description": self.description,
            "is_approved": self.is_approved,
            "created_by": self.created_by
        }
