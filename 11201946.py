# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:41:36 2016

@author: luchao96
"""

import math
import pylab as pl
import numpy as np
class circul:
    def __init__(self,dt1=0.01,dt2=0.001,x=0,y=0.5,angle=1,alpha=0):
        self.dt1=dt1
        self.dt2=dt2
        self.x=[x]
        self.y=[y]
        self.angle=angle
        self.v=1
        self.t=[0]
        self.alpha0=alpha
    def calculate(self):
        self.x0=[math.cos(math.pi*i/100) for i in range(101)]
        self.y0=[math.sin(math.pi*i/100)+self.alpha0 for i in range(101)]
        self.x3=[math.cos(math.pi*i/100) for i in range(101,201)]
        self.y3=[math.sin(math.pi*i/100)-self.alpha0 for i in range(101,201)]
        self.x1=[]
        self.vx1=[]
        i=0
        while i<15000:
            self.vx=self.v*math.cos(self.angle)
            self.vy=self.v*math.sin(self.angle)
            self.x.append(self.x[-1]+self.vx*self.dt1)
            self.y.append(self.y[-1]+self.vy*self.dt1)
            self.t.append(self.t[-1]+0.01)
            #if abs(self.y[-1])<0.0005:
                #self.x1.append(self.x[-1])
                #self.vx1.append(self.vy)
            if self.y[-1]>self.alpha0:
                if math.pow(self.x[-1],2)+math.pow(self.y[-1]-self.alpha0,2)>1:
                    self.x[-1]=self.x[-2]+self.vx*self.dt2
                    self.y[-1]=self.y[-2]+self.vy*self.dt2
                    while(1):
                        self.x.append(self.x[-1]+self.vx*self.dt2)
                        self.y.append(self.y[-1]+self.vy*self.dt2)
                        self.t.append(self.t[-1]+0.01)
                        if math.pow(self.x[-1],2)+math.pow(self.y[-1]-self.alpha0,2)>1:
                            self.x[-1]=(self.x[-1]+self.x[-2])*0.5
                            self.y[-1]=(self.y[-1]+self.y[-2])*0.5
                            self.alpha=math.atan((self.y[-1]-self.y[-2])/(self.x[-1]-self.x[-2]))
                            if self.alpha<0:
                                self.alpha=self.alpha+math.pi
                            self.beta=math.atan((self.y[-1]-self.alpha0)/self.x[-1])
                            if self.beta<0:
                                self.beta=self.beta+math.pi
                            self.angle=2*self.beta-self.alpha
                            if self.angle>0:
                                self.angle=self.angle+math.pi
                            break
                        else:
                            continue
            elif self.y[-1]+self.alpha0<0:
                if math.pow(self.x[-1],2)+math.pow(self.y[-1]+self.alpha0,2)>1:
                    self.x[-1]=self.x[-2]+self.vx*self.dt2
                    self.y[-1]=self.y[-2]+self.vy*self.dt2
                    while(1):
                        self.x.append(self.x[-1]+self.vx*self.dt2)
                        self.y.append(self.y[-1]+self.vy*self.dt2)
                        self.t.append(self.t[-1]+0.01)
                        if math.pow(self.x[-1],2)+math.pow(self.y[-1]+self.alpha0,2)>1:
                            self.x[-1]=(self.x[-1]+self.x[-2])*0.5
                            self.y[-1]=(self.y[-1]+self.y[-2])*0.5
                            self.alpha=math.atan((self.y[-1]-self.y[-2])/(self.x[-1]-self.x[-2]))
                            if self.alpha<0:
                                self.alpha=self.alpha+math.pi
                            self.beta=math.atan((self.y[-1]+self.alpha0)/self.x[-1])
                            if self.beta<0:
                                self.beta=self.beta+math.pi
                            self.angle=2*self.beta-self.alpha
                            if self.angle<0:
                                self.angle=self.angle+math.pi
                            break
                        else:
                            continue
            else:
                if abs(self.x[-1])>1:
                    self.x[-1]=(self.x[-1]+self.x[-2])*0.5
                    self.y[-1]=(self.y[-1]+self.y[-2])*0.5
                    while(1):
                        self.x.append(self.x[-1]+self.vx*self.dt2)
                        self.y.append(self.y[-1]+self.vy*self.dt2)
                        self.t.append(self.t[-1]+0.01)
                        if abs(self.x[-1])>1:    
                            self.angle=math.pi-self.angle
                            break
                        else:
                            continue
            i=i+1
    def plot(self):
        pl.plot(self.x[::1],self.y[::1])
        pl.plot([0,0,0],[0,self.alpha0,-self.alpha0],'.')
        pl.plot(self.x0,self.y0,'g.')
        pl.plot(self.x3,self.y3,'g.')
        #pl.plot(self.x1,self.vx1,'.')
        pl.title('Circular stadium - trajectory')
        pl.xlabel('x')
        pl.ylabel('y')
        pl.xlim(-1,1)
        pl.ylim(-1-self.alpha0,1+self.alpha0)
        
        
class sepration(circul):
    def __init__(self,dt1=0.01,dt2=0.001,x=0,y=0.50001,angle=1,alpha=0):
        self.dt1=dt1
        self.dt2=dt2
        self.x=[x]
        self.y=[y]
        self.angle=angle
        self.v=1
        self.t=[0]
        self.alpha0=alpha
Alpha=0.900002       
a=circul(alpha=Alpha)
a.calculate()
b=sepration(alpha=Alpha)
b.calculate()
i=[math.pow((a.x[j]-b.x[j])**2+(a.y[j]-b.y[j])**2,0.5) for j in range(len(a.x))]
t=a.t
#print len(i)==1e-5

l = np.arange(0.000001, 1, 0.000001)
pl.semilogy(l, np.exp(-l/5.0))

pl.plot(t,i)
pl.xlabel('time')
pl.ylabel('sepration')
pl.title('Stadium with alpha='+str(Alpha)+'-divergence of two trajectory')
pl.show()
