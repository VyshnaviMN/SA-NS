import requests
import random
import time
import random
import json
import railway
import networkx as nx

# NS server endpoint and HTTP headers
url = "http://loadbalancer/Scheduler/updateStatus"
headers = {"Content-Type": "application/json", "Connection": "close"}

update_probability = 0.5
update_probability_delay = 0.1



class Train:
    def __init__(self, id, schedule, longitude, latitude, delay):
        self.id = id
        self.schedule = schedule
        self.longitude = longitude
        self.latitude = latitude
        self.delay = delay
    def toJSON(self):
        return dict(id=self.id, schedule=self.schedule, longitude=self.longitude, latitude=self.latitude, delay=self.delay)     


class Schedule:
    def __init__(self):
        self.items = []
    def toJSON(self):
        return dict(items=self.items)     


class StationTimePair:
    def __init__(self, station, time):
        self.station = station
        self.time = time
    def toJSON(self):
        return dict(station=self.station, time=self.time)
    

class Station:
    def __init__(self, id):
        self.id = id
    def toJSON(self):
        return dict(id=self.id)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'toJSON'):
            return obj.toJSON()
        else:
            return json.JSONEncoder.default(self, obj)


"""
Generates a random schedule for a train. We use a
undirectional graph that represents the dutch railway
network to make the results valid and more realistic 
"""
def generate_schedule(G):

    schedule = []
    route = railway.generate_random_route(G, 2, 5)   
    epoch_time = int(time.time())

    for station in route:
        pair = StationTimePair(Station(station), epoch_time)
        schedule.append(pair)
        epoch_time += random.randint(5, 60) * 60
        
    return schedule


"""
Generates a train object with random data
"""
def generate_train(train_id, G):

    longitude = random.uniform(3.0, 7.5)    # limit within Netherlands
    latitude = random.uniform(50.5, 53.5)   # limit within Netherlands
    delay = random.randint(0, 1)            # delay in minutes
    
    schedule = generate_schedule(G)
    train = Train(train_id, schedule, longitude, latitude, delay)
    return train


"""
Updates location data (longitude, latitude) and delay time 
for each train. Each field is updated under a predefined probability
"""
def update_train(train):
    if random.random() < update_probability:
        train.longitude += random.uniform(-0.01, 0.01)
    if random.random() < update_probability:
        train.latitude += random.uniform(-0.01, 0.01)
    if random.random() < update_probability_delay:
        train.delay += random.randint(-1, 1)


"""
Sends a PUT request with the train data to the NS server endpoint
and logs the HTTP response code
"""
def send_train_data(train):

    try:
        train_json = json.dumps(train.toJSON(), cls=ComplexEncoder)
        response = requests.put(url, json=train_json, headers=headers)
        if response.status_code != 200:
            print(f"[ERROR] Error sending train data: {response.status_code}")
            print(f"Tried to send data: {train_json}")
    except Exception as e:
        print(f"Could not send data to server endpoint: {e}")

"""
Main function to generate live data for NS

Creates a list of trains with random schedules and train details.
Sends a PUT request to the NS server endpoint with the train data
which are continuously updated
"""
if __name__ == "__main__":

    # initialize the railway graph
    G = railway.generate_railway_graph()

    # generate a list of train ids in the format 'NS-Sprinter-XXXX' or 'NS-Intercity-XXXX'
    train_ids = ["NS-Sprinter-{}".format(i) for i in range(4000, 4020)] + ["NS-Intercity-{}".format(i) for i in range(1000, 1020)]
    
    time.sleep(10)
    print("[INFO] Iniating live train data generation")

    # generate and send the initial train data
    trains = []
    for train_id in train_ids:
        train = generate_train(train_id, G)
        trains.append(train)
        send_train_data(train)
        print(f"[OK] Sent data for {train_id}")

    print("[INFO] Generating and sending random train data updates..")

    # update periodically the train data and send them to the server endpoint
    while True:
        for train in trains:
            update_train(train)
            send_train_data(train)