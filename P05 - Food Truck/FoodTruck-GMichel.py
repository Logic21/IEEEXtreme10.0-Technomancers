import sys
import datetime
import math
import re

class Coordinates:
    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)

# Haversine formula
def geo_distance(latitude1,longitude1, latitude2,longitude2):
    lat1 = math.radians(latitude1)
    long1 = math.radians(longitude1)
    lat2 = math.radians(latitude2)
    long2 = math.radians(longitude2)
    r = 6378.137
    return 2.0*r*math.asin(math.sqrt(math.sin((lat1-lat2)/2.0)**2+math.cos(lat1)*math.cos(lat2)*math.sin((long1-long2)/2.0)**2))

#All Stdin at once!
input_data = sys.stdin.readlines()

# Static Data
client_location = input_data[0].rstrip().split(',')
client_location = [float(client_location[0]),float(client_location[1])]
message_radius = float(input_data[1].rstrip())

# Config Data Order
headers = input_data[2].rstrip().split(',')
i_timestamp = headers.index('Date&Time')
i_latitude = headers.index('Latitude')
i_longitude = headers.index('Longitude')
i_number = headers.index('PhoneNumber')

input_data = input_data[3:] # Remove static data from input

numbers_seen = []
customers = []

for line in input_data:
    # Parse Data
    list_c_data = line.rstrip().split(',')

    # Customer Data
    number = int(list_c_data[i_number])

    try:
        timestamp = datetime.datetime.strptime(list_c_data[i_timestamp].rstrip(), '%m/%d/%Y %H:%M')
    except ValueError:
        raw_search = re.search('(\d\d).+?(\d\d).+?(\d\d\d\d).+?(\d\d).+?(\d\d)',list_c_data[i_timestamp].rstrip())
        if raw_search == None:
            timestamp = datetime.datetime.now()
        else:
            try:
                timestamp = datetime.datetime(int(raw_search.group(3)),int(raw_search.group(5)),int(raw_search.group(4)),int(raw_search.group(1)),int(raw_search.group(2)))
            except ValueError:
                raise ValueError('Not Correct')


    distance = geo_distance(client_location[0], client_location[1], float(list_c_data[i_latitude]),float(list_c_data[i_longitude]))

    if number in numbers_seen:
        index = numbers_seen.index(number)
        if timestamp > customers[index][1]:
            customers[index][1] = timestamp
            customers[index][2] = distance
    else:
        customers.append([number,timestamp,distance])
        numbers_seen.append(number)

if len(customers):
    in_range = [val for idx, val in enumerate(numbers_seen) if customers[idx][2] <= message_radius]
    in_range.sort()
    print ",".join(str(number) for number in in_range)
