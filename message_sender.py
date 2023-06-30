import paho.mqtt.client as mqtt

def send_message(broker_url, send_queue_name, message_text):
    client = mqtt.Client()
    client.connect(broker_url, 1883, 60)
    client.publish(send_queue_name, message_text)
    print("Mensaje enviado al tópico {}: {}".format(send_queue_name, message_text))

    client.disconnect()
