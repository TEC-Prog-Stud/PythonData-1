#importing modules
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


# this is a function to get all the data from the file and making it easier to read
def distance_over_time_between_two_points(points):

    lines = []
    for i, p in enumerate(points[1:]):
            # Get previous point
        pp = points[i]
            # Calculate time difference     
        dt = (p['timestamp'] - pp['timestamp']).seconds
            # Calculate distance
        dd = distance( (pp['latitude'], pp['longitude']), (p['latitude'], p['longitude'])).meters
            # Calculate velocity
        v = dd/dt
            # Store data in line dictionary
        line = {
            'start'             : pp,
            'end'               : p,
            'delta_time'        : dt,
            'delta_distance'    : dd,
            'veloicty'          : v,
        }
        lines.append(line)
        # Print results
    print(lines)

    # Variables
    walkTime = 0
    runTime = 0
    idleTime = 0
    walkDistance = 0
    runDistance = 0
    idleDistance = 0
    totalTime = 0
    totaldistance = 0
    # for loop
    for a in lines:
        # if statements for what his velocity is
        #this is idle
        if a['veloicty'] < 0.33333:
            # takes the varibale idleTime  and adds delta_time to it
            idleTime += a['delta_time']
            # takes the varibale idleDistance and adds delta_distance to it
            idleDistance += a['delta_distance']
            print("står stille","\n", "deltatime: ",idleTime, "deltadistance:",idleDistance)
        #this is walk
        elif a['veloicty'] < 1.666667:
            walkTime += a['delta_time']
            walkDistance += a['delta_distance']
            print("Går","\n", "deltatime: ",walkTime, "deltadistance:",walkDistance)
        # this is run
        else:
            runTime += a['delta_time']
            runDistance += a['delta_distance']
            print("Løber","\n", "deltatime: ",runTime, "deltadistance:",runDistance)

        totalTime += a['delta_time']
        totaldistance += a['delta_distance']
    print(f"\n\nTotal Time {totalTime}, Total Distance {totaldistance}")

    # formates the info like the assignment said, and adding some of the variables as procent 
    print(f'\n\n\tmeters, seconds, % of time')
    print(f'Run:\t{runDistance:.1f}\t{runTime}\t{runTime/totalTime:.1%}')
    print(f'Walk:\t{walkDistance:.1f}\t{walkTime}\t{walkTime/totalTime:.1%}')
    print(f'Stand:\t{idleDistance:.1f}\t{idleTime}\t{idleTime/totalTime:.1%}')
    print(f'Total:\t{totaldistance:.1f}\t{totalTime}\t{totalTime/totalTime:.0%}')



def main():
    #variable with the relative file path to a .FIT file
    fname = "projektopgave\data\hok_klubmesterskab_2022\CA8D1347.FIT"
    #Reading the FIT file
    points = read.read_points(fname)
    #priting the length of points
    print(len(points))
    #printing the number 300 of the list of points
    print(points[300])

    ## calling my functions
    print(pace_to_velocity(10))
    distance_over_time_between_two_points(points)

# if name is main execute main function
if __name__ == "__main__":
    main()
