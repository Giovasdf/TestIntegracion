import threading
import message_receiver
import message_sender

def main():
    broker_url = "localhost"
    send_queue_name = "Empresa2"
    receive_queue_name = "Empresa1"

    # Envío de mensajes
    print("== Envío de mensajes ==")
    print("Ingrese el contenido del mensaje (escriba 'fin' para salir):")
    message_content = input()

    while message_content != "fin":
        message_sender.send_message(broker_url, send_queue_name, message_content)
        print("Mensaje enviado:", message_content)

        print("Ingrese el contenido del mensaje (escriba 'fin' para salir):")
        message_content = input()

    # Recepción de mensajes
    print("\n== Recepción de mensajes ==")

    receiver_thread = threading.Thread(target=message_receiver.receive_messages, args=(broker_url, receive_queue_name))
    receiver_thread.start()

    print("Presione enter para detener la recepción de mensajes.")
    input()

    # Detener la recepción de mensajes
    message_receiver.stop_receiving()

    # Esperar a que el hilo de recepción termine
    receiver_thread.join()

if __name__ == "__main__":
    main()
