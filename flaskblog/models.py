from flaskblog import db



# Accessed using from flaskblog.models import User, Post

class Util(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    type = db.Column(db.Integer,nullable=False)
    map = db.Column(db.Integer,nullable=False)
    one_way = db.Column(db.Boolean)
    attack = db.Column(db.Boolean)
    lineup_image = db.Column(db.String(20), nullable=False, default ='default.jpg')
    util_image = db.Column(db.String(20), nullable=False, default ='default.jpg')
    pos_image = db.Column(db.String(20), nullable=False, default ='default.jpg')
    player_x = db.Column(db.Integer, nullable=False)
    player_y = db.Column(db.Integer, nullable=False)
    util_x = db.Column(db.Integer)
    util_y = db.Column(db.Integer)
    note = db.Column(db.String(120))

    def __repr__(self):
        return f"Util('{self.title}','{self.id}')"

db.create_all()
