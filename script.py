
from service_functions import digest_path
from factory import Factory
from service_functions import mflip
from service_functions import efip
from service_functions import eps
from service_functions import bytes_
import sys
import json
import logging 

def run(path: str, output: str, argv: list) -> dict:

    path = digest_path(path)
    events = Factory().gather_events(path)
    batch = Factory().create_batch(events)
    
    response=dict()
    for options in argv:
        if "--mflip" in options:
            response.update({"common ip": mflip(batch.list_ips)})

        elif "--efip" in options:
            response.update({"uncommon ip": efip(batch.list_ips)})

        elif "--eps" in options:
            response.update({"events/s": eps(batch.list_timestamps)})

        elif "--bytes" in options:
            response.update({"bytes sum": bytes_(batch.list_by_tes)})
        
        else:
            raise ValueError("Not a valid option provided")

    with open(output, 'w') as f:
        json.dump(response, f)

    print("Output -> {}".format(response))
    print("Saved in {} inside the container, just sudo docker cp <containerid>:<path> <local_path> to retrieve .json output.".format(output))

    return response
    
if __name__=="__main__":
    logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG)
    logging.info("Running...")
    print("Running...")
    path = sys.argv[1]
    output = sys.argv[2]
    argv = sys.argv[3:]
    run(path, output, argv)