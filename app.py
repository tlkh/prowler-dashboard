import eel
import pika
import ast
import time
from threading import Thread

class ResultsStream:
    """Seperate thread to continously process incoming messages"""
    def __init__(self):
        print("[i] Starting stream reciever")
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='scan_results_exchange',
                                      exchange_type='topic')

        self.result = self.channel.queue_declare(exclusive=True)
        self.queue_name = self.result.method.queue

        self.channel.queue_bind(exchange='scan_results_exchange',
                                queue=self.queue_name,
                                routing_key='scan_results')

        print("[i][Pika] Configured connections")

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        print("[+][Pika] Watching channel (blocking!)")
        self.channel.basic_consume(
            self.callback, queue=self.queue_name, no_ack=True)
        self.channel.start_consuming()

    def callback(self, ch, method, properties, message_body):
        """Callback function to process message"""
        print("\n[R] %r:%r" % (method.routing_key, message_body))
        result = ast.literal_eval(message_body.decode())
        eel.populate_table(result[0], result[1], result[2], result[3])
        print("Append:", result[0], result[1], result[2], result[3])

eel.init('web')
print("[i][Eel] Initialised Eel")
stream = ResultsStream().start()

print("[i][Eel] Serving page...")
eel.start('index.html')
