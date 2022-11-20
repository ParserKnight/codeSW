
from event import Event

class Batch():

    def __init__(self, batch:Event):
        self.batch = batch 
 
    @property
    def batch(self):
        return self._batch

    @batch.setter
    def batch(self, value):
        if not all(isinstance(x,Event) for x in value):
            raise TypeError("Batch need to be a list of events")
        self._batch = value

    @property
    def list_ips(self):
        return [element.client_ip for element in self.batch]

    @property
    def list_timestamps(self):
        return [element.timestamp for element in self.batch]

    @property
    def list_by_tes(self):
        return [element.response_size_bytes for element in self.batch]


