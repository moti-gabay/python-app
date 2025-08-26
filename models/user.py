from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

class User:
    def __init__(self, full_name, tz, email, address, role='user', password=None, _id=None):
        self._id = str(_id) if _id else None
        self.full_name = full_name
        self.tz = tz
        self.email = email
        self.address = address
        self.role = role
        self.password = password  # צריך להיות hashed

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "_id": self._id,
            "full_name": self.full_name,
            "tz": self.tz,
            "email": self.email,
            "address": self.address,
            "role": self.role
        }

    @staticmethod
    def from_mongo(doc):
        """צור אובייקט User ממסמך MongoDB"""
        return User(
            full_name=doc.get('full_name'),
            tz=doc.get('tz'),
            email=doc.get('email'),
            address=doc.get('address'),
            role=doc.get('role', 'user'),
            password=doc.get('password'),
            _id=doc.get('_id')
        )
