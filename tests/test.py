import unittest
import app
import Chatbot


class ChatBotTest(unittest.TestCase):
    def chatbot_test(self):
        response = Chatbot.get_response('!! help')
        self.assertEquals(response, 'EXCITED YOU ASKED!!!! Type in any of these words: !! about, !! say something, !! excited, !! bored, !! encourage, !! bye')
    
    def chatbot_test_about(self):
        response = Chatbot.get_response('!! about')
        self.assertEquals(response, 'Welcome to my Happiness chatbot. Feel free to chat with your friends, post images, and post links that you would like to share.')
    
    def chatbot_test_bored(self):
        response = Chatbot.get_response('!! bored')
        self.assertEquals(response, 'me too! But I am happy!!!!!')
    
    def chatbot_test_invalid_response(self):
        response = Chatbot.get_response('!! heyyy')
        self.assertEquals(response, "Invalid response. Valid responses are !! help, !! about, !! say something, !! bored, !! excited, !! encourage, !! bye")
        
    def chatbot_test_say_something(self):
        response = Chatbot.get_response('!! say something')
        self.assertEquals(response, "Make youself happy!")
    
    def chatbot_test_excited(self):
        response = Chatbot.get_response('!! excited')
        self.assertEquals(response, ":) I am happy you are excited. We should all be happy!")
    
    def chatbot_test_bye(self):
        response = Chatbot.get_response('!! bye')
        self.assertEquals(response,':( Thanks for visiting, I love you!')
        
    def chatbot_test_encourage(self):
        response = Chatbot.get_response('!! encourage')
        self.assertEquals(response, "You are special" or "The best is yet to come" or "Relax and do not stress" or "Cheer up")
    
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    
