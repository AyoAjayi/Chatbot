import flask_sqlalchemy,app
import flask
import flask_socketio
import os

app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ayo:ayo@localhost/postgres'
# app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = flask_sqlalchemy.SQLAlchemy(app.app)
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key
    text = db.Column(db.String(200))
    username = db.Column(db.String(200))
    image = db.Column(db.String(200))
    
    def __init__(self, t,username,image): 
        self.text = t
        self.username = username
        self.image = image

    def __repr__(self):
        return "<Message text:'%s text, %s name, %s image : >" % (self.text , self.username, self.image)



