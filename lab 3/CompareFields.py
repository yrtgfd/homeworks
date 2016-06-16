class Comparator(object):
  def __init__(self, x):
    self.value = x

  def compare(self, v):
    if hasattr(v, 'value'):
      return int(self.value) - int(v.value)
    else:
      return 1

C = Comparator(123)
class Test: pass
T = Test()
T.value = 124
print(C.compare(T))