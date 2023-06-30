import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT")
    client.subscribe(userdata)

def on_message(client, userdata, msg):
    print("Mensaje recibido en el tópico {}: {}".format(msg.topic, msg.payload.decode()))

def receive_messages(broker_url, receive_queue_name):
    client = mqtt.Client()
    client.user_data_set(receive_queue_name)
    client.on_connect = on_connect
    client.on_message = on_message

    print("Conectando al broker MQTT...")
    client.connect(broker_url)
    client.loop_forever()

