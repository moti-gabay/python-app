from datetime import datetime
from bson import ObjectId

class Image:
    """
    מודל עבור תמונה שהועלתה, מאחסן מטא-נתונים וקישורים לקבצים פיזיים.
    תומך בייצוג JSON ובשימוש מול MongoDB.
    """
    def __init__(self, filename, url, uploaded_at=None, uploaded_by=None, _id=None):
        # שמירת _id גם כ-string וגם כ-ObjectId לפעולות MongoDB
        self._id = str(_id) if _id else None
        self._id_obj = _id if isinstance(_id, ObjectId) else ObjectId(_id) if _id else None

        self.filename = filename
        self.url = url
        self.uploaded_at = uploaded_at if isinstance(uploaded_at, datetime) else datetime.utcnow()
        self.uploaded_by = str(uploaded_by) if uploaded_by else None

    def to_dict(self):
        """
        מחזיר ייצוג מילוני של אובייקט התמונה לשימוש בצד לקוח או JSON.
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
        יוצר אובייקט Image ממסמך MongoDB.
        """
        return Image(
            filename=doc.get('filename'),
            url=doc.get('url'),
            uploaded_at=doc.get('uploaded_at') or datetime.utcnow(),
            uploaded_by=doc.get('uploaded_by'),
            _id=doc.get('_id')
        )
