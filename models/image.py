from datetime import datetime
from bson import ObjectId

class Image:
    """
    מודל עבור תמונה שהועלתה, מאחסן מטא-נתונים וקישורים לקבצים פיזיים.
    """
    def __init__(self, filename, url, uploaded_at=None, uploaded_by=None, _id=None):
        self._id = str(_id) if _id else None
        self.filename = filename
        self.url = url
        self.uploaded_at = uploaded_at or datetime.utcnow()
        self.uploaded_by = uploaded_by  # user_id או str(ObjectId)

    def to_dict(self):
        """
        מחזיר ייצוג מילוני של אובייקט התמונה.
        """
        return {
            "_id": self._id,
            "filename": self.filename,
            "url": self.url,
            "uploaded_at": self.uploaded_at.isoformat() + 'Z',
            "uploaded_by": self.uploaded_by
        }

    @staticmethod
    def from_mongo(doc):
        """
        יוצר אובייקט Image ממסמך MongoDB
        """
        return Image(
            filename=doc.get('filename'),
            url=doc.get('url'),
            uploaded_at=doc.get('uploaded_at'),
            uploaded_by=doc.get('uploaded_by'),
            _id=doc.get('_id')
        )
