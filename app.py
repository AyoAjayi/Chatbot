import os
import flask
import flask_socketio
import models
import chatbot
from rfc3987 import parse
from google.oauth2 import id_token
from google.auth.transport import requests
# import requests_oauthlib, requests, oauthlib.oauth2
import requests
# import json

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
    messages = models.Message.query.all()
    array = []
    for message in messages:
        array.append(
            [message.username, message.text,message.image
            ]
        )
    #Send the data to the client
    # print(array)
    socketio.emit('data received',{
     'data': array
    }, broaadcast=True)
    

#When a user logs in, send username and image to my server
@socketio.on('login')
def signIn(response):
    global name
    global image
    image = response['username']['profileObj']['imageUrl']
    name = response['username']['profileObj']['name']

    
#When someone adds a new message, receive from client, and then add to the database, and query the database
@socketio.on('new_data')
def on_new_message(message):
    current_message = message['data']

    #If it is a url, send data to the client 
    if uri_validator(current_message) == True:
        socketio.emit('url received', {'data': current_message})
        info = models.Message(message['data'], name, image)
        models.db.session.add(info)
        models.db.session.commit()
    
    # if current_message == "!! food":
    #     yelp()
    #If the message the user writes starts with !!, then call the Chatbot class in chatbot.py
    elif current_message[:2] == '!!':
        called_class = chatbot.Chatbot()
        final_response = called_class.response(current_message)
        new_message = models.Message(final_response, name, image)
        models.db.session.add(new_message)
        models.db.session.commit()
   
    else:
        info = models.Message(message['data'], name, image)
        models.db.session.add(info)
        models.db.session.commit()
    return on_connect()
    
@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')


def uri_validator(string):
    try:
        result = parse(string, rule='URI')
        print('Received a URL')
        url = True
        return url
    except:
        return False

# request = requests.Request()
# print(request)

if __name__ == '__main__':  
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )


# def yelp():
#     api_key='txrxgJJET6AJinDvE-Nw_G3Q63pTzEKCa4KWgDP4dENnyUhMaedcp5JrFQD7j8fWmDA9NWTqE5PZ3cfcZn31xQ5Lf7YW37CXwB-Onn5weapsnKtWiUhw_rDEBkypXXYx'
#     headers = {'Authorization': 'Bearer %s' % api_key}
#     url='https://api.yelp.com/v3/businesses/search'
#     params = {'term':'food','location':'Baltimore'}
#     req=requests.get(url, params=params, headers=headers)
#     parsed = json.loads(req.text)
#     json_string = json.dumps(parsed, indent=4)
#     print(json_string)
    