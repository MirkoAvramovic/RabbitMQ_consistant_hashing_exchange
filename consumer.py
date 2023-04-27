import pika
from pika.exchange_type import ExchangeType

def on_message1_received(ch, method, properties, body):
    print(f"queue 1 received new message: {body}")

def on_message2_received(ch, method, properties, body):
    print(f"queue 2 received new message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare("simplehashing", "x-consistent-hash")

channel.queue_declare(queue='letterbox1')
channel.queue_bind('letterbox1', 'simplehashing', routing_key='1')
channel.basic_consume(queue='letterbox1', auto_ack=True, 
                      on_message_callback=on_message1_received)
'''
    Routing_key = 4 means that the letterbox2 has a greater chance to receive four times more messages than 
    letterbox1 (routing_key=1). 
    
    While the producer's routing key remains the same, the queue which received the message first will continue 
    to receive all the other messages. Every other change to producer's routing_key will create a greater 
    chance for other queues with smaller consumer's routing_key to receive messages. 
    When another queue receives the message for the first time, it will continue to receive messages while the 
    producer's routing_key remains the same.
'''
channel.queue_declare(queue='letterbox2')
channel.queue_bind('letterbox2', 'simplehashing', routing_key='4')
channel.basic_consume(queue='letterbox2', auto_ack=True, 
                      on_message_callback=on_message2_received)

print("Starting Consuming")

channel.start_consuming()