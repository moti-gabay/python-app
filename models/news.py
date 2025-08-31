from datetime import datetime, timedelta
from bson import ObjectId

class NewsItem:
    def __init__(self, title, description=None, full_content=None, image_url=None,
                 published_at=None, _id=None):
        self._id = str(_id) if _id else None
        self.title = title
        self.description = description
        self.full_content = full_content
        self.image_url = image_url
        self.published_at = published_at or datetime.utcnow()

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
            "_id": self._id,
            "title": self.title,
            "description": self.description,
            "full_content": self.full_content,
            "image_url": self.image_url,
            "published_at": self.published_at.isoformat() + 'Z',
            "timeAgo": self._calculate_time_ago()
        }

    @staticmethod
    def from_mongo(doc):
        """
        יוצר אובייקט NewsItem ממסמך MongoDB
        """
        return NewsItem(
            title=doc.get('title'),
            description=doc.get('description'),
            full_content=doc.get('full_content'),
            image_url=doc.get('image_url'),
            published_at=doc.get('published_at'),
            _id=doc.get('_id')
        )
