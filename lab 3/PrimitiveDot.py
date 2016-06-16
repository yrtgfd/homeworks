class Dot(object):

  def __init__(self, *args):
    self.point = list(args)

  def __str__(self):
    return ','.join(map(str, self.point))

  def distance(self, other):
    if len(self.point) != len(other.point):
      raise ValueError
    return sum(map(lambda x, y: (x - y)**2, self.point, other.point))**0.5

  def middle(self, other):
    if len(self.point) != len(other.point):
      raise ValueError
    return Dot(*list(map(lambda x, y: (x + y) / 2.0, self.point, other.point)))