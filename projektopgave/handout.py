# Her udleveres kode til løsning af opgave 1

def pace2velocity(p):
    return (1000/60)/p

assert pace2velocity(10) == 1.666666666666666666

def v2p(v):
    return (1000/60)/v

assert v2p(1.666666666666666666) == 10

# Her udleveres kode til at løse opgave 2
# virker med stien når du har mappen `projektopgave` aktiv`

def indlaes_fra_fit(fname = "data/hok_klubmesterskab_2022/CA8D1347.FIT"):
    from fit_file import read
    points = read.read_points(fname)
    return points

punkter = indlaes_fra_fit()

print(f"Der er indlæst {len(punkter)} punkter fra filen")
# print(punkter[300])

## -----------------------------------------------------------------

from geopy.distance import distance 

# afstand mellem punkter

# Ved at bruge enumarate får jeg både hvert element (`p`), og et index for hvert element (`i`), altid startende med 0 
# Jeg itereret over listen `punkter[1:]` hvor første element er slicet væk
#   inde i løkken henter jeg forrige punkt med index'et i 
#     Da i starter på nul, for jeg hvert punkt fra 0 til nedstsidste,
#     punktet p er hvert af punkterne fra andet til sidste

# Opgave 3: Skriv en funktion som beregner distance og tid mellem hvert målepunkt,
# i en ny liste af linjestykker
def timeanddistance():
    global lines
    # Creating a new list for lines
    lines = []
    for i, p in enumerate(punkter[1:]):
        pp = punkter[i]
        dt = (p['timestamp'] - pp ['timestamp']).seconds
        dd = distance( (pp['latitude'], pp['longitude']), (p['latitude'], p['longitude'])).meters
        # Creating a list with delta time and delta distance in it, and add it into the list called lines
        line = {
            # Time between the two consecutives
            'Delta Time'        : dt,
            # Distance between the two consecutives
            'Delta Distance'    : dd,
        }
        lines.append(line)

timeanddistance()

# def velocityeverypoint():
#     global velocity
#     velocity = []
#     for d in lines:
#         v = d["Delta Distance"]/d["Delta Time"]
#         velocity.append({}) 

# velocityeverypoint()

# Opgave 4 A.: I en funktion som beregner hastighed mellem hvert målepunkt.
# Egentlig i listen med linjestykker
def velocityeverypoint():
    # Making the 3 lists to global, it means that you will be able to use these lists outside this funktion
    global ll, lg, ls
    # ll stands for ListLøb
    ll = []
    # ll stands for ListGang
    lg = []
    # ll stands for ListStå
    ls = []
    for d in lines:
        v = d["Delta Distance"]/d["Delta Time"]
        # If velocity(hastighed) is not 0, then it doesn't belong to the tempo "Stå"
        if v != 0:
           p = v2p(v)
           # Løb: If tempo is less than 10 min/km
           if p < 10:
              ll.append({"Delta Distance": d["Delta Distance"], "Delta Time": d["Delta Time"], 'v': v, 'p': p})
           # Gang: If tempo is greater than 10 min/km and less than 50 min/km
           elif p > 10 and p < 50:
              lg.append({"Delta Distance": d["Delta Distance"], "Delta Time": d["Delta Time"], 'v': v, 'p': p})
           # Stå: If tempo is greater than 50 min/km
           else:
              ls.append({"Delta Distance": d["Delta Distance"], "Delta Time": d["Delta Time"], 'v': v, 'p': p})
        # Else if velocity(hastighed) actually is 0, then it belongs to the tempo "Stå"
        else:
          ls.append({"Delta Distance": d["Delta Distance"], "Delta Time": d["Delta Time"], 'v': v, 'p': p}) 


velocityeverypoint()

# Opgave 4 B. a.
# I en funktion som
# a. beregner sum af afstand og sum af tid i hver af de tre tempo-zoner; løb, gang og stå
def sum(l):
 global d, t
 # d stands for distance
 d = 0
 # d stands for time
 t = 0
 for i in l:
  # Adding numbers into the 2 ints
  d = d + i["Delta Distance"]
  t = t + i["Delta Time"]
 # print(d, t)

# Calling the function with paramter (ll = ListLøb, lg = ListGang, ls = ListStå) in it
# ll, lg and ls are already created as lists in the function called velocityeverypoint()
sum(ll)
sum(lg)
sum(ls)

# Opgave 4 B. b
# Beregn hvor mange procent af tiden, der samlet foregår hver tempo-zone
def procent():
   tp = 0
   sum(ll)
   # tl stands for timeløb
   tl = t
   sum(lg)
   # tg stands for timegang
   tg = t
   sum(ls)
   # ts stands for timestå
   ts = t

   # Adding all the procents to procenttotal
   tt = tl + tg + ts
   print("Løb: " + str((tl/tt)*100) + "%")
   print("Gang: " + str((tg/tt)*100) + "%")
   print("Stå: " + str((ts/tt)*100) + "%")

procent()