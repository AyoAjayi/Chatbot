import os
import flask
import flask_socketio
import models  
from models import db
from models import *
app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
    return flask.render_template('index.html')
#delete from
@socketio.on('connect')
def on_connect():
    print('Someone connected!')

@socketio.on('new_data')
def on_new_data(message):
    info = message['data']
    messages = models.Message.query.all()
    db.session.add(info)
    db.session.commit(messages)
    print(messages)
    # html = ['<li>' + m.text + '</li>' for m in all_messages]
    # return html
    socketio.emit('data received',{
     'data'
#     },broaadcast=True)
    
    
    
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

# #Whenever someone adds something new
# @socketio.on('new_data')
# def on_new_data(message):
#     #call the function
#     send_to_database(message)
#     socketio.emit('data received',{
     
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
    
    
    
    
