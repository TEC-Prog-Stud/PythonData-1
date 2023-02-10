#!/usr/bin/env python3
# import regular expression library
import re
import datetime
# import pprint to make it easier to print nice thing out
import pprint
# import timezone library
import pytz
# import FIT decoding library
import fitdecode
import csv
from geopy.distance import distance
pp = pprint.PrettyPrinter(compact=True, width=60, depth=4)

# import dependencies for date and time
from datetime import datetime, timedelta
# import types for the data structure
from typing import Dict, Union, Optional, Tuple, List
# List of column names for points
POINTS_COLUMN_NAMES = ['latitude', 'longitude','altitude', 'timestamp', 'heart_rate', 'cadence',]
# List of column names for laps
LAPS_COLUMN_NAMES = ['number', 'start_time', 'message_index', 'lap_trigger',]

# Opgave 2 
# Create a function that stores the necessary data from the fit chunk frames
def get_fit_lap_data(frame: fitdecode.records.FitDataMessage) -> Dict[str, Union[float, datetime, timedelta, int]]:
    data: Dict[str, Union[float, datetime, timedelta, int]] = {}
    for field in LAPS_COLUMN_NAMES[1:]:
        if frame.has_field(field):
            data[field] = frame.get_value(field)
    return data
 
# Opgave 2
# Create a function to store necessary data from points
def get_fit_point_data(frame: fitdecode.records.FitDataMessage) -> Optional[Dict[str, Union[float, int, str, datetime]]]:
    data: Dict[str, Union[float, int, str, datetime]] = {}
    if not (frame.has_field('position_lat') and frame.has_field('position_long')):
        return None
    else:
        data['latitude'] = frame.get_value('position_lat') / ((2**32) / 360)
        data['longitude'] = frame.get_value('position_long') / ((2**32) / 360)
    for field in POINTS_COLUMN_NAMES[2:]:
        if frame.has_field(field):
            data[field] = frame.get_value(field)
    if 'timestamp' in data:
        data['timestamp'] = data['timestamp'].astimezone(
            pytz.timezone('Europe/Copenhagen'))
    return data

# Opgave 2
# Read all the laps and points from the FIT file and returns list of line with laps and list of points.
def read_laps_and_points(filename: str):
    points_data = []
    laps_data = []
    lap_no = 1
    # opens FIT file with fitdecode and decribt the file
    with fitdecode.FitReader(filename) as fit:
        # For every frame in the FIT file it loops
        for frame in fit:
            # if frame is a FitDataMessage
            if isinstance(frame, fitdecode.records.FitDataMessage):
                # if the name match 'record'
                if frame.name == 'record': 
                    #Calls get_fit_point_data to put the data from the FIT file in correct format
                    single_point_data = get_fit_point_data(frame)
                    if single_point_data is not None:
                        points_data.append(single_point_data)
                # if the name match 'record'
                if frame.name == 'lap':
                    # Calls get_fit_lap_data to put the data from the FIT file in correct format
                    single_lap_data = get_fit_lap_data(frame)
                    single_lap_data['number'] = lap_no
                    single_lap_data['points'] = points_data
                    laps_data.append(single_lap_data)
                    lap_no += 1
    return laps_data, points_data

def KontrolTider():
    with open('PythonData-1\projektopgave\data\hok_klubmesterskab_2022\kontroltider.csv', 'r',
        encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        postkontroller = [{'nr': row['nr'],'timestamp': datetime.fromisoformat(row['timestamp'])}for row in reader]
    return postkontroller

def delstrækning(postkontroller, points):
    strærkninger = []
    point = points
    print(len(point))
    print(len(postkontroller))
    totaldd = 0

    for i, time in enumerate(postkontroller[:-1]):
        strærkninger = ([p for p in point 
                         if p['timestamp'].astimezone() > postkontroller[i]['timestamp'] 
                         and p['timestamp'].astimezone() < postkontroller[i+1]['timestamp']])
        print("længde af stærkninger", len(strærkninger))
        for længde in strærkninger:
            længdep = strærkninger[-1]                # previous_pointd
            dd = distance((længde['latitude'], længde['longitude']),
                          (længdep['latitude'], længdep['longitude'])).meters
            print("dd", dd)
            totaldd += dd

    print("totaldd", totaldd)
    return strærkninger

# Opgave 1
def pace2velocity():
    # tager input fra brugeren til hvor langt han har løbet og hvor lang tid de har løbet
    min = input("Hvor langt tid har du bevæget dig?:")
    km = input("Hvor langt her du bevæget dig?:")
    
    #konvter string to int
    min = int(min)
    km = int(km)
    meter = km * 1000
    sec = min * 60
    tempoikilometer = min / km
    tempoimeter = meter / sec
    
    #tjeker hvor hurtig du bevæger dig
    if tempoikilometer <= 10:
        print("Du Løber med", {tempoimeter}, "meter i sek")
    elif tempoikilometer > 10 and tempoikilometer <= 50:
        print("Du Gå med", {tempoimeter}, "meter i sek")
    elif tempoikilometer > 50:
        print("Du stå med",{tempoimeter}, "meter i sek")

def længdeoghastigheder(points):
    lines = []
    # used later in opgave 5
    runmeter = 0
    runsec = 0
    walkmeter = 0
    walksec = 0
    idlemeter = 0
    idlesec = 0
    totaltime = 0
    totalmeter = 0
    print(len(points))
    for i, p in enumerate(points[1:]):
        # bemærk at i starter på 0 selv om vi slicer med [1:]
        pp = points[i]                # previous_pointd
        dt = (p['timestamp'] - pp['timestamp']).seconds
        dd = distance((pp['latitude'], pp['longitude']),(p['latitude'], p['longitude'])).meters
        v = dd/dt
        # Addes start, end time distance and speed of every point
        line = {
            'start': pp,
            'end': p,
            'delta_time': dt,
            'delta_distance': dd,
            'hastighed': v
        }
        
        lines.append(line)
        
        # Check at what speed you are moving
        if v > 1.6666667:
            runmeter += dd
            runsec += dt
        elif v < 1.666667 and v > 0.333333:
            walkmeter += dd
            walksec += dt
        else:
            idlemeter += dd
            idlesec += dt
        totaltime += dt
        totalmeter += dd
    totalruntime = runsec/totaltime *100
    totalwalktime = walksec/totaltime * 100
    totalideltime = idlesec/totaltime * 100
    totaltimeprecent = totalruntime + totalwalktime + totalideltime 
    pp = pprint.PrettyPrinter(compact=True, width=60, depth=2)
    pp = pprint.PrettyPrinter(compact=True, width=60, depth=4)
    pp.pprint(f"Run: {runmeter} {runsec} {totalruntime}", "%")
    pp.pprint(f"walk: {walkmeter} {walksec} {totalwalktime}","%")
    pp.pprint(f"idle: {idlemeter} {idlesec} {totalideltime}","%")
    pp.pprint(f"Total: {totalmeter} {totaltime} {totaltimeprecent}"," %")
    return lines

# initialize main program which it used to call other functions.
def main():
    #Make a var which stores the route to the FIT file
    filename = 'PythonData-1\projektopgave\data\hok_klubmesterskab_2022\CA8D1347.FIT'
    # Calls the method read_laps_and_points to get 2 list which conntains the decribt FIT file
    laps, points = read_laps_and_points(filename)
    postkontroller = KontrolTider()
    strærkninger = delstrækning(postkontroller, points)
    længderoghastigheder = længdeoghastigheder(strærkninger, points)
    # pp.pprint(len(laps))
    # pp.pprint(len(points))
    # pp.pprint(len(strærkninger))
    # pp.pprint(len(længderoghastigheder))
    # pp.pprint(laps)
    # pp.pprint(points)
    # pp.pprint(strærkninger[1])
    # pp.pprint(strærkninger[-1])
    # pp.pprint(længderoghastigheder)
    pace2velocity()
if __name__ == "__main__":
    main()
