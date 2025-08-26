from datetime import datetime
from bson import ObjectId

class TraditionItem:
    """
    מודל עבור פריטי המסורת היהודית.
    """
    def __init__(self, title, full_content, short_description=None, category=None,
                 image_url=None, created_at=None, updated_at=None, _id=None):
        self._id = str(_id) if _id else None
        self.title = title
        self.short_description = short_description
        self.full_content = full_content
        self.category = category
        self.image_url = image_url
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def to_dict(self):
        """
        מחזיר ייצוג מילוני של אובייקט המסורת.
        """
        return {
            "_id": self._id,
            "title": self.title,
            "short_description": self.short_description,
            "full_content": self.full_content,
            "category": self.category,
            "image_url": self.image_url,
            "created_at": self.created_at.isoformat() + 'Z',
            "updated_at": self.updated_at.isoformat() + 'Z'
        }

    @staticmethod
    def from_mongo(doc):
        """
        יוצר אובייקט TraditionItem ממסמך MongoDB
        """
        return TraditionItem(
            title=doc.get('title'),
            full_content=doc.get('full_content'),
            short_description=doc.get('short_description'),
            category=doc.get('category'),
            image_url=doc.get('image_url'),
            created_at=doc.get('created_at'),
            updated_at=doc.get('updated_at'),
            _id=doc.get('_id')
        )
