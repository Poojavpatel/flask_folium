import time
from celery import Celery

# Celery("task argument(name of the module i.e. task.py)" , broker="specify that we are connecting to RabbitMQ as the guest user")
app = Celery("tasks", broker="amqp://localhost//")

@app.task
def sleep_asynchronously():
    time.sleep(5)

print("Let's begin!")

sleep_asynchronously.delay()
print("... and that's the end of our really short app.")


# to check if rabbitmq is running $ rabbitmq-server
# to run $ celery -A tasks worker --loglevel=info
# -A lets us specify which module to run 