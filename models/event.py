import json
from bson import ObjectId

class Event:
    def __init__(self, title, date, time, location, needed_volunteers, description=None,
                 registered_users=None, is_approved=False, created_by=None, _id=None):
        self._id = str(_id) if _id else None
        self.title = title
        self.date = date          # מחרוזת ISO או datetime.date
        self.time = time          # מחרוזת HH:MM:SS או datetime.time
        self.location = location
        self.needed_volunteers = needed_volunteers
        self.description = description
        self.registered_users = registered_users or []  # רשימה של user_ids
        self.is_approved = is_approved
        self.created_by = created_by  # יכול להיות user_id או str(ObjectId)

    def to_dict(self):
        return {
            "_id": self._id,
            "title": self.title,
            "date": self.date.isoformat() if hasattr(self.date, 'isoformat') else self.date,
            "time": self.time.strftime('%H:%M:%S') if hasattr(self.time, 'strftime') else self.time,
            "location": self.location,
            "needed_volunteers": self.needed_volunteers,
            "registered_users": self.registered_users,
            "description": self.description,
            "is_approved": self.is_approved,
            "created_by": self.created_by
        }

    @staticmethod
    def from_mongo(doc):
        """צור אובייקט Event ממסמך MongoDB"""
        return Event(
            title=doc.get('title'),
            date=doc.get('date'),
            time=doc.get('time'),
            location=doc.get('location'),
            needed_volunteers=doc.get('needed_volunteers'),
            description=doc.get('description'),
            registered_users=doc.get('registered_users', []),
            is_approved=doc.get('is_approved', False),
            created_by=doc.get('created_by'),
            _id=doc.get('_id')
        )
