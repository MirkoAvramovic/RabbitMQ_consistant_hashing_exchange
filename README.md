# RabbitMQ_consistant_hashing_exchange
Producer.py send the message with specific routing_key and uses "x-consistant-hash" exchange type. <br>
Consumer.py consumes the message. Depending of queue's routing_key, message will be dilivered to a particular queue.
