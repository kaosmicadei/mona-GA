from numpy import *


class Gene:
  def __init__(self, num_vertices, width, height):
    self.width = width
    self.height = height
    self.rgba = list(random.rand(4))
    self.vertices = []
    
    for _ in xrange(num_vertices):
      x = random.random_integers(0, self.width)
      y = random.random_integers(0, self.height)
      self.vertices.append((x, y))


  def mutate_rgba(self, sigma):
    self.rgba += sigma * sigma * random.randn(4)

    self.rgba = map(lambda x: max(0, min(1, x)), self.rgba)

    
  def mutate_shape(self, sigma):
    for i,_ in enumerate(self.vertices):
      x = self.vertices[i][0] + sigma * random.randn() * self.width
      x = max(0, min(self.width, x))

      y = self.vertices[i][1] + sigma * random.randn() * self.height
      y = max(0, min(self.height, y))

      self.vertices[i] = (x,y)