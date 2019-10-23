# import os
# import flask
# import flask_socketio
# import models
 
# app = flask.Flask(__name__)

# import models
# socketio = flask_socketio.SocketIO(app)

# @app.route('/')
# def hello():
#     return flask.render_template('index.html')
    
# #When someone connects, load up all the contents of my database and send them to my client
# @socketio.on('connect')
# def on_connect():
#     print('Someone connected!')
    
#     messages = models.Message.query.all()
#     array = list(messages)
#     for i in array:
#         print(i)
#     array = [ m.text + ' '  for m in messages]
#     print(array)
    
#     socketio.emit('data received',{
#      'data': array
#     },broaadcast=True)
    
# #When someone adds a new message, receive from client, and then add to the database, and query the database
# @socketio.on('new_data')
# def on_new_message(message):
#     info = models.Message(message['data'])
#     models.db.session.add(info)
#     models.db.session.commit()
#     return on_connect()
   
# @socketio.on('disconnect')
# def on_disconnect():
#     print('Someone disconnected!')
    
# if __name__ == '__main__':  
#     socketio.run(
#         app,
#         host=os.getenv('IP', '0.0.0.0'),
#         port=int(os.getenv('PORT', 8080)),
#         debug=True
#     )
    























import os
import flask
import flask_socketio
from models import db

app = flask.Flask(__name__)

import models
socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
    return flask.render_template('index.html')
    
#When someone connects, load up all the contents of my database and send them to my client
@socketio.on('connect')
def on_connect():
    print('Someone connected!')
    # messages = models.Message.query.all()
    # array = list(messages)
    # print(array)
    # socketio.emit('data received',{
    #  'data': 
    #  'username'
    # },broaadcast=True)
    
#When someone adds a new message, receive from client, and then add to the database, and query the database
@socketio.on('new_data')
def on_new_message(message):
    print(message['data'])
    print(message['username'])
    socketio.emit('data received',{
     'data': message['data'],
     'username': message['username']
    },broaadcast=True)
    
    # info = models.Message(message['username'], message['data'])
    # models.db.session.add(info)
    # models.db.session.commit()
    # return on_connect()
   
@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')
    
if __name__ == '__main__':  
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
    
    
    
    
    
    
    
    
    