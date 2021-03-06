import matplotlib.pyplot as plt
import particle
import numpy as np

class Molecule:
    
     '''A class that represents a molecule made out of two particles'''
    
    def __init__(self, pos1, pos2, m1, m2, k, L0):
        self.p1=particle.Particle(pos1, m1)
        self.p2=particle.Particle(pos2, m2)
        self.k=k
        self.L0=L0

    def get_displ(self):
        return np.array(self.p1.pos)-np.array(self.p2.pos)

    def get_force(self):
        displacement=Molecule.get_displ(self)
        distance=np.linalg.norm(displacement)
        return self.k*(distance-self.L0)/displacement
        '''A function that finds the force between two particles'''


