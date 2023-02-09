import csv
import datetime
from fit_file import read
from geopy.distance import distance

# This function takes a pace value as an argument and returns the corresponding velocity as an output
def pace_to_velocity(pace):
    # Calculate velocity in meters per second
    v = (1000/60)/pace
    # Return the result
    return v


def read_csv(points):
    # regexTime = r'\s(\d+):(\d+):(\d+)'
    time = []
    l0 = 0
    l1 = 1
    with open('projektopgave\data\hok_klubmesterskab_2022\kontroltider.csv', 'r',
              encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        postkontroller = [{'nr': row['nr'],
                       'timestamp': datetime.datetime.fromisoformat(row['timestamp'])}
                      for row in reader]
    while l1 < len(postkontroller):
        t = postkontroller[l1]['timestamp'] - postkontroller[l0]['timestamp']
        l0 += 1
        l1 += 1
        print(t)
        time.append(t)
        
    st_1 = [p for p in points if p['timestamp'].astimezone() < postkontroller[1]['timestamp'] ]
    # her ses postkontrollens timestamp, og det sidste punkt fra fit filen der er før posten
    postkontroller[1]['timestamp'], st_1[-1]
    b = 0
    for a in st_1:
        print(f"(Taler: {b}, Latitude: {a['latitude']}, Longtitude {a['longitude']}, TimeStamp: {a['timestamp']})")
        b += 1
    # print(st_1)



def distance_over_time_between_two_points(points):
    lines = []
    for i, p in enumerate(points[1:]):
    # bemærk at i starter på 0 selv om vi slicer med [1:]
        pp = points[i]                # previous_point
        dt = (p['timestamp'] - pp['timestamp']).seconds
        dd = distance( (pp['latitude'], pp['longitude']), (p['latitude'], p['longitude'])).meters
        v = dd/dt
        line = {
            'start'             : pp,
            'end'               : p,
            'delta_time'        : dt,
            'delta_distance'    : dd,
            'veloicty'          : v,
        }
        lines.append(line)
    print(lines)

    for a in lines:
        print(f"start: {a['start']}, end: {a['end']}, dt: {a['delta_time']}, dd: {a['delta_distance']}, Veolicty: {a['veloicty']}")


def main():
    fname = "projektopgave\data\hok_klubmesterskab_2022\CA8D1347.FIT"
    points = read.read_points(fname)
    print(len(points))
    print(points[300])
    print(pace_to_velocity(10))
    read_csv(points)
    pass


if __name__ == "__main__":
    main()
