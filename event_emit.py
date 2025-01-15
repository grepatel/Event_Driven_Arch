import pika

def emit_event(event_data):

	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	
	channel.queue_declare(queue='events')
	
	channel.basic_publish(exchange='',routing_key='events',body=event_data)
	
	print(f"Sent event: {event_data}")

	connection.close()

emit_event("User signed up")
