# models/news.py
from extensions import db
from datetime import datetime, timedelta # ייבוא timedelta לחישוב זמן

class NewsItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True) # תקציר
    full_content = db.Column(db.Text, nullable=True) # תוכן מלא
    image_url = db.Column(db.String(500), nullable=True) # URL לתמונה (השם ב-DB)
    published_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f"<NewsItem {self.title}>"

    def _calculate_time_ago(self):
        """
        מחשב את הזמן שחלף מאז הפרסום ומחזיר מחרוזת ידידותית למשתמש.
        """
        now = datetime.utcnow()
        diff = now - self.published_at
        
        if diff.days > 365:
            years = diff.days // 365
            return f"לפני {years} שנה" if years == 1 else f"לפני {years} שנים"
        elif diff.days > 30:
            months = diff.days // 30
            return f"לפני {months} חודש" if months == 1 else f"לפני {months} חודשים"
        elif diff.days > 7:
            weeks = diff.days // 7
            return f"לפני {weeks} שבוע" if weeks == 1 else f"לפני {weeks} שבועות"
        elif diff.days > 0:
            return f"לפני {diff.days} יום" if diff.days == 1 else f"לפני {diff.days} ימים"
        elif diff.seconds > 3600:
            hours = diff.seconds // 3600
            return f"לפני {hours} שעה" if hours == 1 else f"לפני {hours} שעות"
        elif diff.seconds > 60:
            minutes = diff.seconds // 60
            return f"לפני {minutes} דקה" if minutes == 1 else f"לפני {minutes} דקות"
        else:
            return "לפני רגע"

    def to_dict(self):
        """
        מחזיר ייצוג מילוני של אובייקט החדשות, כולל שדות מחושבים.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "full_content": self.full_content, # עבור דף הכתבה המלאה
            "image_url": self.image_url, # <--- שם שדה ב-JSON כפי שביקש המשתמש
            "published_at": self.published_at.isoformat() + 'Z', # עדיין מחזירים את זה ליתר ביטחון
            "timeAgo": self._calculate_time_ago() # <--- שדה מחושב כפי שביקש המשתמש
        }
