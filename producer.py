import pika
from pika.exchange_type import ExchangeType

# Define the connection parameters for RabbitMQ. 
# Change 'localhost' to the appropriate server if needed.
connection_parameters = pika.ConnectionParameters('localhost')

# Establish a connection to the RabbitMQ server
connection = pika.BlockingConnection(connection_parameters)

# Create a channel for communication
channel = connection.channel()

# Declare an exchange named "simplehashing" with the type "x-consistent-hash"
channel.exchange_declare("simplehashing", "x-consistent-hash")

# Define the routing key for your message 
routing_key = "Hash me!"

# Define the message you want to send
message = "This is the core message."

# Publish the message to the specified exchange and routing key
channel.basic_publish(
    exchange='simplehashing', 
    routing_key=routing_key, 
    body=message)

# Print the message to confirm a message was sent
print(f"sent message: {message}")

# Close the connection to RabbitMQ 
connection.close()