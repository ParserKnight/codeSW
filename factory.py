

from event import Event
from batch import Batch
import re
import logging

class Factory():

    def __init__(self):
        pass

    @staticmethod
    def gather_events(path:list) -> list[Event]:
        """To produce list of event from different sources"""
        events = list()
        for p in path:
            with open(p) as file:
                for line in file:
                    values = re.sub(' +', ' ',line).split(' ')
                    try:
                        event= Event(*values)
                        events.append(event)
                    except ValueError as e:
                        logging.error("Couldnt create event {} - {}".format(values, e))
                        pass
                    except TypeError as e:
                        logging.error("Couldnt create event {} - {}".format(values, e))
                        pass

        return events

    @staticmethod
    def create_batch(events:Event) -> list[Batch]:
        """To produce batch object"""
        try:
            batch = Batch(events)
        except ValueError as e:
            logging.error("Couldnt create event {} - {}".format(events, e))
            pass
        
        return batch