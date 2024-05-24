import random
import logging

logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname

    def get_switch_list(self):
        # Database interaction to fetch switch list
        # Simulating fetching switch data
        switches = [{"id": 1, "location": "r1"}, {"id": 2, "location": "r2"}]
        return switches

    def get_oids_from_file(self):
        # Read OIDs from file and return as list
        oids = [".1.3.6.1.2.1.1.5.0", ".1.3.6.1.2.1.2.2.1.2", ".1.3.6.1.2.1.4.20.1.1"]
        return oids

    def create_collection_task(self, switch, oids):
        task = {"switch_id": switch["id"], "location": switch["location"], "oids": oids}
        return task
