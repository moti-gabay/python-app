# models/image.py
from extensions import db
from datetime import datetime

class Image(db.Model):
    """
    מודל עבור תמונה שהועלתה, מאחסן מטא-נתונים וקישורים לקבצים פיזיים.
    """
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), unique=True, nullable=False) # שם קובץ מקורי או מאובטח
    url = db.Column(db.String(255), unique=True, nullable=False)      # ה-URL הציבורי של התמונה (לדוגמה, /images/my_pic.jpg)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # קישור למשתמש שהעלה את התמונה (אופציונלי, ניתן להסיר אם לא רוצים)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) 
    uploader = db.relationship('User', backref='uploaded_images', lazy=True)

    def __repr__(self):
        return f"<Image {self.filename}>"

    def to_dict(self):
        """
        מחזיר ייצוג מילוני של אובייקט התמונה.
        """
        return {
            "id": self.id,
            "filename": self.filename,
            "url": self.url,
            "uploaded_at": self.uploaded_at.isoformat() + 'Z', # פורמט ISO 8601
            "uploaded_by": self.uploaded_by
        }
