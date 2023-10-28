import pika
from pika.exchange_type import ExchangeType

# Callback function to handle messages received on queue 'letterbox1'
def on_message1_received(ch, method, properties, body):
    print(f"queue 1 received new message: {body}")

# Callback function to handle messages received on queue 'letterbox2'
def on_message2_received(ch, method, properties, body):
    print(f"queue 2 received new message: {body}")

# Define the connection parameters for RabbitMQ. 
# Change 'localhost' to the appropriate server if needed.
connection_parameters = pika.ConnectionParameters('localhost')

# Establish a connection to the RabbitMQ server
connection = pika.BlockingConnection(connection_parameters)

# Create a channel for communication
channel = connection.channel()

# Declare an exchange named "simplehashing" with the type "x-consistent-hash"
channel.exchange_declare("simplehashing", "x-consistent-hash")

# Declare and bind 'letterbox1' queue with routing_key '1'
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
# Declare and bind 'letterbox2' queue with routing_key '4'
channel.queue_declare(queue='letterbox2')
channel.queue_bind('letterbox2', 'simplehashing', routing_key='4')
channel.basic_consume(queue='letterbox2', auto_ack=True, 
                      on_message_callback=on_message2_received)

# Print a message to indicate the start of message consumption
print("Starting Consuming")

# Start consuming messages from the queues
channel.start_consuming()
