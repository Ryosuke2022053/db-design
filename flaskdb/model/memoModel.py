from flaskdb import db

class Memo(db.Model):
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    share = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Memo %r>" % self.id