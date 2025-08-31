from datetime import datetime
from bson import ObjectId

class UploadedFile:
    def __init__(self, filename, uploaded_by=None, category=None, year=None, upload_date=None, _id=None):
        self._id = str(_id) if _id else None
        self.filename = filename
        self.upload_date = upload_date or datetime.utcnow()
        self.uploaded_by = uploaded_by  # user_id או str(ObjectId)
        self.category = category
        self.year = year

    def to_dict(self):
        return {
            "_id": self._id,
            "filename": self.filename,
            "upload_date": self.upload_date.isoformat(),
            "uploaded_by": self.uploaded_by,
            "category": self.category,
            "year": self.year
        }

    @staticmethod
    def from_mongo(doc):
        """
        יוצר אובייקט UploadedFile ממסמך MongoDB
        """
        return UploadedFile(
            filename=doc.get('filename'),
            uploaded_by=doc.get('uploaded_by'),
            category=doc.get('category'),
            year=doc.get('year'),
            upload_date=doc.get('upload_date'),
            _id=doc.get('_id')
        )
