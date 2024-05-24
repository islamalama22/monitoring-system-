import pika
import logging

logger = logging.getLogger(__name__)

class TaskQueue:
    def __init__(self, host, queue_name):
        self.host = host
        self.queue_name = queue_name

    def send_task(self, task):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
            channel = connection.channel()
            channel.queue_declare(queue=self.queue_name)
            channel.basic_publish(exchange="", routing_key=self.queue_name, body=str(task))
            connection.close()
            logger.info("Task sent to the queue successfully.")
        except Exception as e:
            logger.error(f"Failed to send task to queue: {e}")

    def receive_task(self):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
            channel = connection.channel()
            channel.queue_declare(queue=self.queue_name)

            method_frame, header_frame, body = channel.basic_get(queue=self.queue_name, auto_ack=True)
            if body:
                task = eval(body)
                logger.info("Task received from the queue.")
                return task
            else:
                logger.info("No task in the queue.")
                return None

        except KeyboardInterrupt:
            raise KeyboardInterrupt  # Propagate KeyboardInterrupt to stop the script
        except Exception as e:
            logger.error(f"Failed to receive task from queue: {e}")
            return None
