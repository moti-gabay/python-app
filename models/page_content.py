import json
from bson import ObjectId

class PageContent:
    def __init__(self, slug, title, body, images=None, _id=None):
        self._id = str(_id) if _id else None
        self.slug = slug
        self.title = title
        self.body = body
        self.images = images or []  # רשימה של URL או מידע נוסף

    def to_dict(self):
        return {
            "_id": self._id,
            "slug": self.slug,
            "title": self.title,
            "body": self.body,
            "images": self.images
        }

    @staticmethod
    def from_mongo(doc):
        """
        יוצר אובייקט PageContent ממסמך MongoDB
        """
        return PageContent(
            slug=doc.get('slug'),
            title=doc.get('title'),
            body=doc.get('body'),
            images=doc.get('images', []),
            _id=doc.get('_id')
        )
