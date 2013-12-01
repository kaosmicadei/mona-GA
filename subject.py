import cairo
from numpy import *
from itertools import *
from gene import *


class Subject:
  def __init__(self, num_genes, num_vertices, width, height):
    self.width = width
    self.height = height
    self.dna = []

    for _ in xrange(num_genes):
      self.dna.append(Gene(num_vertices, width, height))


  def mutate(self, sigma):
    for i,_ in enumerate(self.dna):
      self.dna[i].mutate_rgba(sigma) if random.random() < 0.5 else self.dna[i].mutate_shape(sigma)


  def fitness(self, goal):
    length = 4.0 * self.width * self.height
    
    individual = map(ord, self.draw().get_data())

    diff = list(imap(lambda x,y: abs(x-y)/255.0, individual, goal))

    return 1 - sum(diff) / length


  def draw(self):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, self.width, self.height)
    context = cairo.Context(surface)
    context.set_source_rgb(1, 1, 1)
    context.rectangle(0, 0, self.width, self.height)
    context.fill()
    
    for gene in self.dna:
      context.set_source_rgba(*gene.rgba)
      context.set_line_width(0)
      context.move_to(*gene.vertices[0])

      for vertex in gene.vertices[1:]:
        context.line_to(*vertex)

      context.fill()

    return surface