# RabbitMQ Consistent Hashing Exchange Application

This is a sample application that demonstrates how to use RabbitMQ with consistent hashing exchange to route messages to specific queues based on a consistent hash of the message's routing key.

## Prerequisites

Before running this application, ensure you have the following prerequisites installed:

- [RabbitMQ](https://www.rabbitmq.com/download.html)
- Python (for running the provided Python scripts)

## Getting Started

1. Clone this repository to your local machine
2. Install the necessary Python dependencies
3. Run the producer and consumer scripts to send and receive messages using the consistent hashing exchange.

## Usage
### Producer
The producer script (producer.py) sends messages to the consistent hashing exchange. You can customize the routing keys and messages within the script to see how the messages are routed to different queues.

### Consumer
The consumer script (consumer.py) receives messages from the queues based on the routing keys and demonstrates how consistent hashing works.

## Explanation
In this application, we use a RabbitMQ exchange with the type "x-consistent-hash" to distribute messages to queues. The producer.py script sends messages with routing keys, and the exchange uses consistent hashing to determine which queue should receive the message.

### Routing Keys and Queues
- letterbox1 with routing key 1:
This queue will receive messages with a routing key of 1.
- letterbox2 with routing key 4
The comments within the scripts provide additional details about how the consistent hashing exchange works.

## Acknowledgments
- RabbitMQ
- pika
