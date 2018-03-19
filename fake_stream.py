import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='scan_results')

i = 0

while True:
    i += 1
    fake_ip = (str(i) + ".")*3 + str(i)
    message = [fake_ip, "Linux/3.4", ["22/ssh", "5900/vnc"], "Unknown"]
    print("[i][pika] Sending message", message)
    channel.basic_publish(exchange='scan_results_exchange', routing_key='scan_results', body=str(message))
    time.sleep(1)

print("Closing connection...")
connection.close()