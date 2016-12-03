# -*- coding: utf-8 -*-
"""
Created on Sat Dec 03 09:56:15 2016

@author: luchao96
"""
import numpy as np
import pylab as pl
import math
class hyperion:
    def __init__(self,time_step=0.0001,zero=0,theta=0):
        self.dt=time_step
        self.x=[1]
        self.y=[0]
        self.v_x=[0]
        self.v_y=[5]
        self.t=[zero]
        self.nt=10/time_step
        self.theta=[theta]
        self.omega=[zero]
    def calculate(self):
        i=0
        while i<self.nt:
            A=4*(math.pi**2)/math.pow(self.x[-1]**2+self.y[-1]**2,1.5)
            self.v_x.append(self.v_x[-1]-A*self.x[-1]*self.dt)
            self.x.append(self.x[-1]+self.v_x[-1]*self.dt)
            self.v_y.append(self.v_y[-1]-A*self.y[-1]*self.dt)
            self.y.append(self.y[-1]+self.v_y[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            B=12*(math.pi**2)/math.pow(self.x[-1]**2+self.y[-1]**2,2.5)
            C=self.x[-1]*math.sin(self.theta[-1])-self.y[-1]*math.cos(self.theta[-1])
            D=self.x[-1]*math.cos(self.theta[-1])+self.y[-1]*math.sin(self.theta[-1])
            self.omega.append(self.omega[-1]-B*C*D*self.dt)
            self.theta.append(self.theta[-1]+self.omega[-1]*self.dt)
            #if abs(self.theta[-1])>math.pi:
             #   if abs(self.theta[-1]+2*math.pi)<math.pi:
              #      self.theta[-1]=self.theta[-1]+2*math.pi
               # else:
                #    self.theta[-1]=self.theta[-1]-2*math.pi
            i=i+1
    def plot(self):
        pl.plot(self.x,self.y)
        pl.title('trajectory of Hyperion')
        pl.xlabel('time(yr)')
        pl.ylabel('theta(radians)')
        
        
class delta(hyperion):
    def __init__(self,time_step=0.0001,zero=0,theta=0.01):
        self.dt=time_step
        self.x=[1]
        self.y=[0]
        self.v_x=[0]
        self.v_y=[5]
        self.t=[zero]
        self.nt=10/time_step
        self.theta=[theta]
        self.omega=[zero]
        
a=hyperion()
a.calculate()
b=delta()
b.calculate()
dtheta=[abs(a.theta[i]-b.theta[i]) for i in range(len(a.t))]
l = np.arange(0.000001, 0.0001, 0.000001)
pl.semilogy(l, np.exp(-l/5.0))
pl.plot(a.t,dtheta)
pl.title('Hyperion:$\Delta theta$ versus time')
pl.xlabel('time(yr)')
pl.show()
pl.ylabel('d theta(radians)')
pl.xlim(0,10)
pl.show()
