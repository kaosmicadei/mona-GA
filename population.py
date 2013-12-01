import cairo
from subject import *


class Population:
  num_genes = 50
  num_vertices = 6
  sigma = 0.1
  
  def __init__(self, original_image, num_individuals):
    self.num_individuals = num_individuals
    
    image = cairo.ImageSurface.create_from_png(original_image)
    self.width = image.get_width()
    self.height = image.get_height()

    self.goal = map(ord, image.get_data())

    self.population = []

    for _ in xrange(self.num_individuals):
      self.population.append(Subject(self.num_genes, self.num_vertices, self.width, self.height))


  def pop_fitness(self):
    fitness = {}

    for i in xrange(self.num_individuals):
      fitness[i] = self.population[i].fitness(self.goal)

    return fitness


  def evolve(self):
    pass


  def cross(self, partner):
    pass