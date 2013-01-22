import numpy
import random
import pylab

class motor(object):
    def __init__(self, pas):
        self.pas = pas

    def deplacement(self,x):
        if x > 10:
            return -self.pas
        elif x < - 10:
            return self.pas
        else:
            return 0

class center(object):
    def __init__(self, moteur):
        self.X = 0
        self.Y = 0
        self.moteur = moteur

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def setX(self, X):
        self.X = X

    def setY(self, Y):
        self.Y = Y

    def update(self):
        self.X = self.X + moteur.deplacement(self.X) + random.choice(range(-10,11))
        self.Y = self.Y + moteur.deplacement(self.Y) + random.choice(range(-10,11))

moteur = motor(5)
centre = center(moteur)
for i in range(0,1000):
    centre.update()
print centre.getX()
print centre.getY()
