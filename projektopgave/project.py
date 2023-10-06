from geopy.distance import distance 
from handout import indlaes_fra_fit, v2p, pace2velocity
from tempo import Tempo
from distance import p2p
import pandas
import csv
import datetime
import numpy as np

def distanceCal(punkter): #3
  """Calculate the distance between two points and return a list of vertices as P2p classes

  Args:
      punkter (list[geolocation]): list of consecutive geolocations

  Returns:
      list[p2p]: List of vertices
  """
  res = {}
  for i, p in enumerate(punkter[1:]):
      # previus point
      pp = punkter[i]

      dt = (p['timestamp'] - pp['timestamp']).seconds
      dd = distance( (pp['latitude'], pp['longitude']), (p['latitude'], p['longitude'])).meters
      v = dd/dt
      tempo = getTempo(v)
      newp2p = p2p(dt, dd, v, tempo)
      res[i]=(newp2p)
  
  return res


def getTempo(v):
  """Get the tempo by giving velocity
  turns v into pace and returns tempo
  run: pace < 10 min/km
  walk 10 min/km <= pace < 50 min/km
  still pace >= 50 min/km

  Args:
      v (velocity): float

  Returns:
      Enum: Tempo
  """
  if v == 0:
    return Tempo.STILL
  else:
    p = v2p(v) #min/km
  if p < 10:
    return Tempo.RUN
  elif 10 <= p and p < 50:
    return Tempo.WALK
  else:
    return Tempo.STILL


def legcalc(p2pDict : dict[int, p2p]): #Opgave 4
  """Generate a dictionary of tuples with calculated vertice data.
  each leg consists of one or more vertices (p2p) this methods devides each vertice between tempos 

  Args:
      p2pDict (dict[int, p2p]): dictionary of legs, a leg is a list of vertices

  Returns:
      dict: A dictionary of tuples divided in Run/Walk/Still/Total with values of (Distance, Time, %of total distance, %of total time)
  """
  still = [0, 0]
  walk = [0, 0]
  run = [0, 0]
  for pp in p2pDict.values():
    if pp.tempo == Tempo.STILL:
        still[0] += pp.deltadistance
        still[1] += pp.deltatime
    elif pp.tempo == Tempo.WALK:
        walk[0] += pp.deltadistance
        walk[1] += pp.deltatime
    else:
        run[0] += pp.deltadistance
        run[1] += pp.deltatime
  totalDist = still[0] + walk[0] + run[0]
  totalTime = still[1] + walk[1] + run[1]
  res = {}
  res["Run"] = (run[0],run[1],run[0]/totalDist*100,run[1]/totalTime*100)
  res["Walk"] = (walk[0],walk[1],walk[0]/totalDist*100,walk[1]/totalTime*100)
  res["Still"] = (still[0],still[1],still[0]/totalDist*100,still[1]/totalTime*100)
  res["Total"] = (totalDist,totalTime,100,100)
  return res
  

def prettyPrintRun(x : dict): #Opgave 5
  """Prettely prints a dictionary, arg must be the return of legcalc()

  Args:
      x (dict): A dictionary of tuples divided in Run/Walk/Still/Total with values of (Distance, Time, %of total distance, %of total time)
  """
  table = [[round(x["Run"][0],2), x["Run"][1], round(x["Run"][2], 2), round(x["Run"][3], 2)],
          [round(x["Walk"][0],2), x["Walk"][1], round(x["Walk"][2], 2), round(x["Walk"][3], 2)], 
          [round(x["Still"][0],2), x["Still"][1], round(x["Still"][2], 2), round(x["Still"][3], 2)], 
          [round(x["Total"][0],2), x["Total"][1], round(x["Total"][2], 2), round(x["Total"][3], 2)]]
  df = pandas.DataFrame(table, columns= ["distance", "time", f"%distance", f"%time"], index=["Run", "Walk", "Still", "Total"])
  
  print(df)
   

def readControlTimes():
  """Reads control times of post in a csv file

  Returns:
      list[dict[str, any]]: list of dictionarys of string keys and geoloc values
  """
  with open('data/hok_klubmesterskab_2022/kontroltider.csv', 'r', 
          encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    postkontroller = [{ 'nr':row['nr'], 
            'timestamp': datetime.datetime.fromisoformat(row['timestamp']) } 
          for row in reader]
    return postkontroller


def getLegs(punkter): #Opgave 6.1
  """Devides a list of geolocs into lists of "legs", a leg is all the points bewteen two control points

  Args:
      punkter (list[geolocation]): A list of GeoLocations

  Returns:
      dict[int, list[geolocs]]: return a dictionary of legs, with leg 1 being points between first and second control points
  """
  postkontroller = readControlTimes()
  postLeg = {}
  lastPost = postkontroller[0]["timestamp"].astimezone()
  for pk in postkontroller[1:]:
    postLeg[pk['nr']] = [p for p in punkter if (p['timestamp'].astimezone() < pk['timestamp'] and p['timestamp'].astimezone() >= lastPost) ]
    lastPost = postLeg[pk['nr']][-1]["timestamp"]

  return postLeg


def getBirdp2p(legPoints): #Opgave 6.2
  """Calculate birdflight distance between beginning of legs

  Args:
      postLeg (a dictionnary of legs): Takes the return type of legs()  

  Returns:
      dict: A dictionary of bird path p2p
  """
  cloestPunktToPost = []
  start = True
  for point in legPoints:
    if start:
      cloestPunktToPost.append(legPoints[point][0]) # because these are vertices, the "first" post should be the start of the first vertice
      start = False
    cloestPunktToPost.append(legPoints[point][-1])
  birdFlightDist = distanceCal(cloestPunktToPost)

  return birdFlightDist


def distancesBetweenLegs(legPoints : dict): #OPgave 6.3
  """Calculate total distance of each leg

  Args:
      postLeg (a dictionary of legs): a dict of legs containing points in that leg

  Returns:
      dict: A dictionary of the total distance covered by each leg
  """
  res = {}
  i = 1
  totalDist = 0
  for posts in legPoints.values():
    postDists = distanceCal(posts)
    legDist = legcalc(postDists)
    res[i] = legDist["Total"][0]
    i += 1
    totalDist += legDist["Total"][0]
  return res


def printLegs(legPoints : dict): #Opgave 7
  """Prints tempo of each leg

  Args:
      legPoints (dict): a dict of legs containing points in that leg
  """
  total = 0
  legTitle = "Start"
  for leg in legPoints:
    print(f"\nFrom {legTitle} to {leg}")
    res = distanceCal(legPoints[leg])
    legres = legcalc(res)
    prettyPrintRun(legres)
    total += legres["Total"][0]
    legTitle = leg
  print(f"\nTotal: {total:.2f} meters from start to finish") 
  

def getRelations(legP2P, legPoints): #Opgave 8
  """Calculates relations of each consecutive leg compared to all legs

  Args:
      legP2P (dict): dict of leg vertices
      legPoints (dict): a dict of legs containing points in that leg

  Returns:
      dict: relational tuple containing info of each leg(leg distance, leg distance / distance of all legs)
  """
  res = {}  
  for points in legPoints:
    punktDists = distanceCal(legPoints[points])
    totalegdist = sum([p2p.deltadistance for p2p in punktDists.values()])
    res[points] = (totalegdist, totalegdist/legP2P["Total"][0])
  return res


def getLegAverage(legPoints : dict[p2p, int]): #Opgave 9
  """Calculate the average velocity of each leg

  Args:
      legPoints (dict[p2p, int]): a dictionary of legs containin all points in leg

  Returns:
      dict: Dictionary for each leg, with tuples containg average velocity and corrosponding tempo enum 
  """
  res = {}
  i = 1
  for leg in legPoints.values():
    postDists = distanceCal(leg)  
    totalTime = sum([p2p.deltatime for p2p in postDists.values()])
    totalVelocities = sum([p2p.velocity*p2p.deltatime for p2p in postDists.values()])
    v = totalVelocities/totalTime
    tempo = getTempo(v)
    #print(f"Stræk {i} ̅v = {v:.2f}m/s; {tempo}")
    res[i]=(v,tempo)
    i+=1
  return res

 
def getBirdLegAverage(birdp2p : dict[p2p, int]): #Opgave 10
  """Get only the bird average velocity and tempo

  Args:
      birdp2p (dict[p2p, int]): return type of postBirds
  """
  res = {}
  i = 1
  for p2p in birdp2p.values():
    #print(f"Fugle flugt stræk {i} ̅v = {p2p.velocity:.2f}m/s {p2p.tempo} afstand {p2p.deltadistance:.2f}")
    res[i]=(p2p.velocity,p2p.tempo)
    i+=1
  return res

 
def getRelationofRealandBirdVelocity(legsPoints, birdp2p): #Opgave 11
  """Calculates relation of two different lists of velocities

  Args:
      legPoints (dict[p2p, int]): a dictionary of legs containin all points in leg
      birdp2p (dict[p2p, int]): return type of postBirds

  Returns:
      dict: relation of real velocity and flight velocity
  """
  res = {}
  realV =[]
  for leg in legsPoints.values():
    postDists = distanceCal(leg)  
    totalTime = sum([p2p.deltatime for p2p in postDists.values()])
    totalVelocities = sum([p2p.velocity*p2p.deltatime for p2p in postDists.values()])
    realV.append(totalVelocities/totalTime)
  birdV = [p2p.velocity for p2p in birdp2p.values()]
  for i in range(len(birdV)):
    #print(f"leg {i} realV {realV[i]:.2f}, birdV {birdV[i]:.2f} realV/birdV = {realV[i]/birdV[i]:.2f}")
    res[i] = realV[i] / birdV[i]
  return res


def printLegRelation(legp2p, legPoints, birdp2p): #Opgave 12
  """Prints the relations

  Args:
      legp2p (_type_): _description_
      legPoints (_type_): _description_
      birdp2p (_type_): _description_
  """
  distRel = getRelations(legp2p, legPoints)
  realV = getLegAverage(legPoints)
  birdV = getBirdLegAverage(birdp2p)
  Vrel = getRelationofRealandBirdVelocity(legPoints, birdp2p)
  
  dist = list(np.cumsum(list(round(rel[1]*100,2) for rel in distRel.values())))
  realV = list(round(realv[0],2) for realv in realV.values())
  birdV = list(round(birdv[0],2) for birdv in birdV.values())
  vrel = list(round(vrel,2) for vrel in Vrel.values())
  
  df = pandas.DataFrame({f"%of total distance":dist, 
                         "Average velocity" : realV, 
                         "Bird velocity": birdV, 
                         "Average compared to velocity of unladen swallow": vrel}, 
                        index=list(range(1, len(distRel)+1)))
  print(df)
  

def main():
  #Opgaver 3-5
  punkter = indlaes_fra_fit()
  p2pDict = distanceCal(punkter)
  legs = legcalc(p2pDict)
  print(f"\nTotal Running Adventure")
  prettyPrintRun(legs)
  
  #Opgave 6-7
  legPoints = getLegs(punkter)
  print(f"\nRunning Adventure divided by legs")
  printLegs(legPoints) 
  
  #opgave 8-12
  birdp2p = getBirdp2p(legPoints)
  print(f"\nRunning Adventure legs relations to birds")
  printLegRelation(legs, legPoints, birdp2p)

if __name__ == "__main__":
    main()

