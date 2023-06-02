# Her udleveres kode til løsning af opgave 1

def pace2velocity(p):
    return (1000/60)/p

assert pace2velocity(10) == 1.666666666666666666

def v2p(v):
    return (1000/60)/v

def percentage(some, total):
  return 100 * some/total

assert v2p(1.666666666666666666) == 10

# Her udleveres kode til at løse opgave 2
# virker med stien når du har mappen `projektopgave` aktiv`

def indlaes_fra_fit(fname = "data/hok_klubmesterskab_2022/CA8D1347.FIT"):
    from fit_file import read
    points = read.read_points(fname)
    return points

punkter = indlaes_fra_fit()

distancetime = []

print(f"Der er indlæst {len(punkter)} punkter fra filen")
print(punkter[300])

## -----------------------------------------------------------------

from geopy.distance import distance 

# afstand mellem punkter

# Ved at bruge enumarate får jeg både hvert element (`p`), og et index for hvert element (`i`), altid startende med 0 
# Jeg itereret over listen `punkter[1:]` hvor første element er slicet væk
#   inde i løkken henter jeg forrige punkt med index'et i 
#     Da i starter på nul, for jeg hvert punkt fra 0 til nedstsidste,
#     punktet p er hvert af punkterne fra andet til sidste
def DistanceUdregning(punkter):
    for i, p in enumerate(punkter[1:]):
        # previus point
        pp = punkter[i]

        dt = (p['timestamp'] - pp['timestamp']).seconds
        dd = distance( (pp['latitude'], pp['longitude']), (p['latitude'], p['longitude'])).meters
        v = dd/dt
        #print(f"p: {p}")
        #print(f"pp: {pp}")
        #print(f"dt: {dt}")
        #print(f"dd: {dd}")
        distancetime.append([dt,dd,v])
        #distancetime[dd] = distancetime.get(dd, dt, v)

def MovementCalc(distancetime):
    sumDisRun = 0
    sumDisWalk = 0
    sumDisIdle = 0
    sumTimeRun = 0
    sumTimeWalk = 0
    sumTimeIdle = 0
    for time, distance, hastighed in distancetime:
        if (hastighed >= 1.666667):
            sumDisRun += distance
            sumTimeRun += time
        elif (hastighed >= 0.333333):
            sumDisWalk += distance
            sumTimeWalk += time
        elif (hastighed < 0.333333):
            sumDisIdle += distance
            sumTimeIdle += time
    
    sumDisTotal = sumDisRun + sumDisWalk + sumDisIdle
    sumTimeTotal = sumTimeRun + sumTimeWalk + sumTimeIdle
    # print (sumDisRun,sumDisWalk,sumDisIdle)
    # print (sumTimeRun,sumTimeWalk,sumTimeIdle)
    # print (sumDisTotal,sumTimeTotal)
    # print(percentage(sumTimeRun,sumTimeTotal))
    # print(percentage(sumTimeWalk,sumTimeTotal))
    # print(percentage(sumTimeIdle,sumTimeTotal))
    # print(percentage(sumTimeRun,sumTimeTotal) + percentage(sumTimeWalk,sumTimeTotal) + percentage(sumTimeIdle,sumTimeTotal))

    print(f'\t meters \t seconds \t percentage \nRun: \t {sumDisRun: .1f} \t {sumTimeRun} \t\t {percentage(sumTimeRun,sumTimeTotal): .1f} \nWalk: \t {sumDisWalk: .1f} \t {sumTimeWalk} \t\t {percentage(sumTimeWalk,sumTimeTotal): .1f} \nIdle: \t {sumDisIdle: .1f} \t\t {sumTimeIdle} \t\t {percentage(sumTimeIdle,sumTimeTotal): .1f} \nTotal: \t {sumDisTotal: .1f} \t {sumTimeTotal} \t\t {percentage(sumTimeTotal, sumTimeTotal): .1f}')

            

DistanceUdregning(punkter)
MovementCalc(distancetime)
     
# for time, distance, hastighed in distancetime:
#     print(f"Afstand: {distance: .1f} \t Tid: {time} \t Hastighed: {hastighed: .2f}")
