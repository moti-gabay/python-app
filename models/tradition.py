# models/tradition.py
from extensions import db
from datetime import datetime

class TraditionItem(db.Model):
    """
    מודל עבור פריטי המסורת היהודית.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True) # כותרת הפריט (לדוגמה: "שבת", "פסח", "תפילת שחרית")
    short_description = db.Column(db.Text, nullable=True) # תקציר קצר
    full_content = db.Column(db.Text, nullable=False) # תוכן מלא של הכתבה/הסבר על המסורת
    category = db.Column(db.String(100), nullable=True) # קטגוריה (לדוגמה: "חגים", "תפילות", "מנהגים", "אישים")
    image_url = db.Column(db.String(500), nullable=True) # URL לתמונה קשורה (אופציונלי)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<TraditionItem {self.title}>"

    def to_dict(self):
        """
        מחזיר ייצוג מילוני של אובייקט המסורת.
        """
        return {
            "id": self.id,
            "title": self.title,
            "short_description": self.short_description,
            "full_content": self.full_content,
            "category": self.category,
            "image_url": self.image_url,
            "created_at": self.created_at.isoformat() + 'Z',
            "updated_at": self.updated_at.isoformat() + 'Z'
        }
