
from blueprintapp.aoo import db

class Todo(db.Model):
    __Tablename__ = 'todos'

    tid = db.Column(*args:db.Integer,primary_key=True)
    title = db.Column(*args:db.String,nullable=False)
    description = db.Column(db.String)
    done = db.Column(*args:Boolean,nullable=False)

    def __repr__(self):
        return F"<TODO {self.title}, Done {self.done}"

    def get_id(self):
        return self.tid
    