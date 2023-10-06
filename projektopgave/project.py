from geopy.distance import distance 
from handout import indlaes_fra_fit

def distanceCal(punkter): 
    res = {}
    for i, p in enumerate(punkter[1:]):
        # previus point
        pp = punkter[i]

        dt = (p['timestamp'] - pp['timestamp']).seconds
        dd = distance( (pp['latitude'], pp['longitude']), (p['latitude'], p['longitude'])).meters
        v = dd/dt
        res[i]=((dt, float(f'{dd:.4f}'), float(f'{v:.4f}')))
    
    return res


def main():
  punkter = indlaes_fra_fit()
  print(distanceCal(punkter))

if __name__ == "__main__":
    main()
