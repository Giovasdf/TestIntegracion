import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('Error recibido: %s' % message)

    def on_message(self, frame):
        print('Mensaje recibido: %s' % frame.body)

conn = stomp.Connection([('localhost', 61613)])
print('Conectando al broker Empresa3...')
conn.set_listener('', MyListener())
conn.connect()

conn.subscribe(destination='/queue/Empresa3', id=1, ack='auto')

while True:
    pass

conn.disconnect()
