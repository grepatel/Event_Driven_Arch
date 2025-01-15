from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def process_event(event_data)
	print(f"Processing event: {event_data}")
