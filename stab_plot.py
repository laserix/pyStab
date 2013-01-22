import numpy
import random
import pylab
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse
from matplotlib import cm

class motor(object):
    def __init__(self, pas):
        self.pas = pas

    def deplacement(self,x):
        if x > 3:
            return -self.pas
        elif x < - 3:
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

# loop on step 
r_mean = numpy.array((0))
r_std = numpy.array((0))
ratio = []

for pas in range(1,25,1):
	moteur = motor(pas)
	centre = center(moteur)
	accept=0
	point_x = []
	point_y = []
	maxiter = 100
	for i in range(0,maxiter):
		centre.update()
		point_x.append(centre.getX())
		point_y.append(centre.getY())
		if (centre.getX()**2+centre.getY()**2)**0.5<10:
			accept +=1.0
	# create array of positions		
	point_x=numpy.array((point_x))
	point_y=numpy.array((point_y))
	ratio.append(accept/maxiter)
	# graphics
	ax1 = pylab.subplot(111,aspect='equal')
	r = (point_x**2+point_y**2)**0.5
	area = 100./(1+0.5*r)
	colors=r/(max(point_x)**2+max(point_y)**2)**0.5
	
	# plot of scatter centroid points
	sc = pylab.scatter(point_x, point_y,c=colors, s=area, cmap=cm.hsv,hold='on')
	ax1.set_xlabel('X')
	ax1.set_xlim(-80,80)
	ax1.set_ylabel('Y')
	ax1.set_ylim(-80,80)
	sc.set_alpha(0.35)
	
	print 'for R<10:', 'pas=',pas,'ratio=',ratio[-1]	

	r_mean = numpy.append(r_mean,numpy.mean(r))
	r_std = numpy.append(r_std,numpy.std(r))
pylab.show()

# mean and std of delta r and ratio R<10/maxiter

fig2 =plt.figure()	
ax2 = fig2.add_subplot(111)
ax2.plot(r_mean[1:],'bo-',label = r'mean')
ax2.plot(r_std[1:],'b*--',label = r'std')
ax2.set_xlabel('motor step length')
ax2.set_ylabel('$\delta r$', color='b')
for tl in ax2.get_yticklabels():
    tl.set_color('b')
    
ax3=ax2.twinx()
ax3.plot(ratio,'r*-',label = 'ratio' )
ax3.set_ylabel('ratio', color='r')
for tl in ax3.get_yticklabels():
    tl.set_color('r')
#fig2.legend(loc='upper left')

plt.show()