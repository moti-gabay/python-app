from extensions import db

class PageContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)  
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    images_json = db.Column(db.Text, nullable=True)  # כאן נשמור מערך JSON כטקסט

    def to_dict(self):
        return {
            "id": self.id,
            "slug": self.slug,
            "title": self.title,
            "body": self.body,
            "images": json.loads(self.images_json) if self.images_json else []            
        }
