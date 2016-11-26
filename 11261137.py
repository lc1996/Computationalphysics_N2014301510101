# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 10:50:13 2016

@author: luchao96
"""

import pylab as pl
import math
class solar_system:
    def __init__(self,time_step=0.0001,beta=2.0,i=0,radius=[0.39,0.72,1.00,1.52,5.20,9.54,19.19,30.06,39.53],e=[0.206,0.007,0.017,0.093,0.048,0.056,0.046,0.01,0.248],v_x=0,v_y=2*math.pi,planet=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']):
        self.x=[radius[i]*(1-e[i])]
        self.y=[0]
        self.v_x=[v_x]
        self.v_y=[v_y*math.pow((1+e[i])/(radius[i]*(1-e[i])),0.5)]
        self.dt=time_step
        self.beta=beta
        self.r=radius[i]
        self.e=e[i]
        self.side=[radius[i]]
        self.area=[]
        self.t=0
        self.planet=planet[i]
    def calculate(self):
        while(1):
            A=4*math.pow(math.pi,2)/math.pow(self.x[-1]**2+self.y[-1]**2,self.beta/2+0.5)
            self.v_x.append(self.v_x[-1]-A*self.x[-1]*self.dt)
            self.x.append(self.x[-1]+self.v_x[-1]*self.dt)
            self.v_y.append(self.v_y[-1]-A*self.y[-1]*self.dt)
            self.y.append(self.y[-1]+self.v_y[-1]*self.dt)
            self.t=self.t+self.dt
            self.side.append(math.pow(self.x[-1]**2+self.y[-1]**2,0.5))
            side3=math.pow((self.x[-1]-self.x[-2])**2+(self.y[-1]-self.y[-2])**2,0.5)
            p=(self.side[-1]+self.side[-2]+side3)/2            
            #self.area.append(math.pow(p*(p-self.side[-1])*(p-self.side[-2])*(p-side3),0.5))
            if self.t>2:            
                if self.r*(1-self.e)-self.x[-1]<0.01:
                    if self.y[-1]>=0:
                        print 'T=',self.t
                        break
    def plot(self):
        d=math.pow(self.t,2)/math.pow(0.5*(max(self.x)-min(self.x)),3)
        r=33
        pl.plot(self.x,self.y,label='$T^2/a^3=$'+str(d)+',T='+str(self.t)+'yr')
        pl.plot(0,0,'.')
        pl.title(self.planet+' orbiting the Sun')
        pl.legend(loc='best',prop={'size':12})
        pl.xlabel('x(AU)')
        pl.ylabel('y(AU)')
        pl.xlim(-r,r)
        pl.ylim(-r,r)

j=2
while j<3:
    a=solar_system(i=7)
    a.calculate()
    a.plot()
    #b=max(a.x)
    #c=min(a.x)
    #print b,c
    #d=math.pow(a.t,2)/math.pow(0.5*(b-c),3)
    #print '$T^2/a^3=$',d,'i=',j
    #area=sum(a.area)
    #print 'the total area=',area
    j=j+1
pl.show()
