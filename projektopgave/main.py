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
        # print(t)
        time.append(t)
        
    st_1 = [p for p in points if p['timestamp'].astimezone() < postkontroller[1]['timestamp'] ]
    # her ses postkontrollens timestamp, og det sidste punkt fra fit filen der er før posten
    postkontroller[1]['timestamp'], st_1[-1]
    b = 0
    for a in st_1:
        # print(f"(Taler: {b}, Latitude: {a['latitude']}, Longtitude {a['longitude']}, TimeStamp: {a['timestamp']})")
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

    walkTime = 0
    runTime = 0
    idleTime = 0
    walkDistance = 0
    runDistance = 0
    idleDistance = 0
    totalTime = 0
    totaldistance = 0
    totalWalk = []
    totalRun = []
    totalIdle = []
    for a in lines:
        # print(f"Delta Time {a['delta_time']}, Delta Distance {a['delta_distance']}, Veloicty {a['veloicty']}")
        if a['veloicty'] < 0.33333:
            idleTime += a['delta_time']
            idleDistance += a['delta_distance']
            print("står stille","\n", "deltatime: ",idleTime, "deltadistance:",idleDistance)
            totalIdle.append((idleTime, idleDistance))
        elif a['veloicty'] < 1.666667:
            walkTime += a['delta_time']
            walkDistance += a['delta_distance']
            print("Går","\n", "deltatime: ",walkTime, "deltadistance:",walkDistance)
            totalWalk.append((walkTime, walkDistance))
        else:
            runTime += a['delta_time']
            runDistance += a['delta_distance']
            print("Løber","\n", "deltatime: ",runTime, "deltadistance:",runDistance)
            totalRun.append((runTime, runDistance))

        totalTime += a['delta_time']
        totaldistance += a['delta_distance']
    print(f"\n\nTotal Time {totalTime}, Total Distance {totaldistance}")

    print(f'\n\n\tmeters, seconds, % of time')
    print(f'Run:\t{runDistance:.1f}\t{runTime}\t{runTime/totalTime:.1%}')
    print(f'Walk:\t{walkDistance:.1f}\t{walkTime}\t{walkTime/totalTime:.1%}')
    print(f'Stand:\t{idleDistance:.1f}\t{idleTime}\t{idleTime/totalTime:.1%}')
    print(f'Total:\t{totaldistance:.1f}\t{totalTime}\t{totalTime/totalTime:.1%}')



def main():
    fname = "projektopgave\data\hok_klubmesterskab_2022\CA8D1347.FIT"
    points = read.read_points(fname)
    # print(len(points))
    # print(points[300])
    print(pace_to_velocity(10))
    # read_csv(points)
    distance_over_time_between_two_points(points)
    pass


if __name__ == "__main__":
    main()
