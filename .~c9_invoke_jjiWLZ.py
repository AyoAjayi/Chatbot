import os
import flask
import flask_socketio
import models  
from models import db

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
    return flask.render_template('index.html')


@socketio.on('new message')
def on_new_message(data):
   
    message = data['message']
    username = data['username']
    server_message = Message(message, username)
    database.session.add(server_message)
    database.session.commit()

    #send the messages
    send_messages()

def send_messages():
    global messages
    messages = Message.query.all()
    messages = list(messages)
    socketio.emit('retrieved messages', {
        'messages': messages
    })





























@socketio.on('connect')
def on_connect():
    print('Someone connected!')
    messages = models.Message.query.all()
    html = ['<li>' + m.text + '</li>' for m in messages]
    return '<ul>' + ''.join(html) + '</ul>'
    # socketio.emit('data received',{
    #  'data': info
    # },broaadcast=True)

@socketio.on('new_data')
def on_new_data(message):
    print(message['data'])
    info = models.Message(message['data'])
    models.db.session.add(info)
    models.db.session.commit()
   
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
    
    
    
    
    
        
# import os
# import flask
# import psycopg2
# #You have to import everything from models.py
# from models import *

# @app.route('/')
# def hello():
#     return flask.render_template('index.html')

# @socketio.on('connect')
# def on_connect():
#     print('Someone connected!')

# #Whenever someone connects to my server, I want to store what they write to my database
# @socketio.on('new_data')
# def on_new_data(message):
#     #call the function
#     send_to_database(message)
#     socketio.emit('data received',{ 'data': message
#     },broaadcast=True)
    
# #I want to send the data I receive to my database
# def send_to_database(info):
#     message = Message(info['data'])
#     db.session.add(message)
#     db.session.commit()
#     all_messages = Message.query.all()
#     html = ['<li>' + m.text + '</li>' for m in all_messages]
#     return html


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
        


    
    
    
    
    
    
    
    
    
    
 # import os, flask, flask_socketio  

# app = flask.Flask(__name__)
# socketio = flask_socketio.SocketIO(app) 

# @app.route('/')
# def hello():
#     return flask.render_template('index.html')

# @socketio.on('connect') 
# def on_connect():
#     print ('Someone connected!')
    
# socketio.run(
#     app,
#     host=os.getenv('IP', '0.0.0.0'),
#     port=int(os.getenv('PORT', 8080)),
#     debug=True
# )
    
    
    
    
