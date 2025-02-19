from database.__init__ import db


class Ingredients(db.Document):
    category = db.StringField(required=True)
    name = db.StringField(required=True)
    icon_url = db.URLField(required=True)
    

class Refrigerator(db.Document):
    rfg_name = db.StringField(required=True)
    rfg_img_url = db.URLField(required=True)
    rfg_memo = db.StringField(required=True)