import os
import flask
import flask_socketio
import models
import app
import random


class Chatbot():
    def __init__(self):
        return 
    def response(self, message):
        if message == '!! help':
            response = 'EXCITED YOU ASKED!!!! Type in any of these words: !! about, !! say something, !! excited, !! bored, !! encourage, !! bye'
        elif message == '!! about':
            response = 'Welcome to my Happiness chatbot. Feel free to chat with your friends, post images, and post links that you would like to share.'
        elif message == '!! say something':
            response = 'Make youself happy!'
        elif message == '!! bored':
            response = 'me too! But I am happy!!!!!'
        elif message == '!! excited':
            response = ':) I am happy you are excited. We should all be happy'
        elif message == '!! bye':
            response = ':( Thanks for visiting, I love you!'
        elif message == '!! question':
            response = 'What do you like more? food or shopping, type !! food for food or !! shopping for shopping'
        elif message == '!! encourage':
            array = ["You are special", "The best is yet to come", "Relax and do not stress", "Cheer up"]
            r = random.randint(0, len(array))
            response = array[r]
        else:
            response = "Invalid response. Valid responses are !! help, !! about, !! say something, !! bored, !! excited, !! encourage, !! bye"
        return response
        
   
    


