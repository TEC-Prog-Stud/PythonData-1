class p2p:
  def __init__(self, dt, dd, v, tempo) -> None:
    """Point To Point or vetice between to points on a map

    Args:
        dt (number): Delta Time, time it took to treverse
        dd (number): Delta Distance distance of vertice
        v (number): Velocity
        tempo (Enum): Tempo, calculated by velocity and distance
    """
    self.deltatime = dt
    self.deltadistance = dd
    self.velocity = v
    self.tempo = tempo
