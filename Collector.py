import logging
import random
from task_queue import TaskQueue

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

RABBITMQ_HOST = "localhost"
TASK_QUEUE_NAME = "switch_data_collection"

def main():
    task_queue = TaskQueue(RABBITMQ_HOST, TASK_QUEUE_NAME)

    try:
        while True:
            task = task_queue.receive_task()
            if task:
                process_task(task)
    except KeyboardInterrupt:
        logger.info("Collector stopped.")

def process_task(task):
    # Simulate temperature data collection
    temperature = random.randint(18, 25)
    logger.info(f"Collected temperature for switch {task['switch_id']} ({task['location']}): {temperature}°C")

if __name__ == "__main__":
    main()
