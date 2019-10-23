import app
import unittest
import flask_socketio

class Socket_io_unit_test(unittest.TestCase):
    def test_on_connect(self):
        client = app.socketio.test_client(app.app)
        received = client.get_received()
        self.assertEquals(len(received), 1)
        message = received[0]
        self.assertEquals(message,'Someone connected!')
    
    def test_disconnect(self):
        socketio = flask_socketio.SocketIO(app.app)
        
        client = app.socketio.test_client(app.app)
        socketio.emit('disconnect')
        recieved = client.get_received()
        print(recieved)
        
    def test_server_relays_message(self):
        client = app.socketio.test_client(app.app)
        client.emit('new_data', {
            'data': 'I am excited!'
        })
        r = client.get_received()
        self.assertEquals(len(r), 1)
        from_server = r[1]
        self.assertEquals(
            from_server['data'],
            'new_data'
        )

if __name__ == '__main__':
    unittest.main()
