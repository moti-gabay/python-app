from extensions import db
from datetime import datetime

class UploadedFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'))  # אם רוצים לשייך למשתמש
    category = db.Column(db.String(100))  # הוספת שדה קטגוריה
    year = db.Column(db.Integer)  # הוספת שדה שנה

    def to_dict(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "upload_date": self.upload_date.isoformat(),
            "uploaded_by": self.uploaded_by,
            "category": self.category,  # הוספת קטגוריה ל-dict
            "year": self.year,  # הוספת שנה ל-dict
        }