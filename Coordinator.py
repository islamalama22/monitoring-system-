import time
import logging
from configparser import ConfigParser
from database import DatabaseManager
from task_queue import TaskQueue

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = ConfigParser()
config.read('config.ini')

DB_HOST = config.get('Database', 'HOST')
DB_USER = config.get('Database', 'USER')
DB_PASSWORD = config.get('Database', 'PASSWORD')
DB_NAME = config.get('Database', 'NAME')

RABBITMQ_HOST = config.get('RabbitMQ', 'HOST')
TASK_QUEUE_NAME = config.get('RabbitMQ', 'TASK_QUEUE_NAME')

def main():
    db_manager = DatabaseManager(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    task_queue = TaskQueue(RABBITMQ_HOST, TASK_QUEUE_NAME)

    try:
        switches = db_manager.get_switch_list()
        oids = db_manager.get_oids_from_file()

        for switch in switches:
            task = db_manager.create_collection_task(switch, oids)
            task_queue.send_task(task)
            time.sleep(2)

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
