# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 08:27:31 2017

@author: luchao96
"""

import math
import pylab as pl
import random
class dilutegas:
    def __init__(self,dt=0.002):
        self.dt=dt
        self.x_curr0=[1,1,1,1,3,3,3,3,5,5,5,5,7,7,7,7]
        self.y_curr0=[1,3,5,7,1,3,5,7,1,3,5,7,1,3,5,7]
        pl.plot(self.x_curr0,self.y_curr0,'o')
        self.x_curr=0
        self.y_curr=0
        self.x_prev=0
        self.y_prev=0
        self.x_new=0
        self.y_new=0
        self.v_x=0
        self.v_y=0
        self.a_x=0
        self.a_y=0
        self.f_x=[]
        self.f_y=[]
        self.t=0
    def calculate(self):
        ax=random.random()
        bx=random.random()
        vx=random.random()
        vy=random.random()
        for i in range(1):
            self.x_curr=self.x_curr0[5]+1+2*(ax-0.5)*0.2*0
            self.y_curr=self.y_curr0[5]+1+2*(bx-0.5)*0.2*0
            self.v_x=2*(vx-0.5)*0+4
            self.v_y=2*(vy-0.5)*0+4
        for i in range(1):
            self.x_prev=self.x_curr-self.v_x*self.dt
            self.y_prev=self.y_curr-self.v_y*self.dt
        while self.t<4000:
            for i in range(1):
                self.f_x=[]
                self.f_y=[]
                for j in range(16):
                    r1=math.pow((self.x_curr-self.x_curr0[j])**2+(self.y_curr-self.y_curr0[j])**2,0.5)
                    r2=math.pow((self.x_curr-self.x_curr0[j]-8)**2+(self.y_curr-self.y_curr0[j])**2,0.5)
                    r3=math.pow((self.x_curr-self.x_curr0[j]+8)**2+(self.y_curr-self.y_curr0[j])**2,0.5)
                    r4=math.pow((self.x_curr-self.x_curr0[j])**2+(self.y_curr-self.y_curr0[j]-8)**2,0.5)
                    r5=math.pow((self.x_curr-self.x_curr0[j])**2+(self.y_curr-self.y_curr0[j]+8)**2,0.5)
                    r=min([r1,r2,r3,r4,r5])
                    if r==0:
                        print self.t,i,j
                    if r<3:
                        fj=24*(2/math.pow(r,13)-1/math.pow(r,7))
                        if r1==r:
                            self.f_x.append(fj*(self.x_curr-self.x_curr0[j])/r)
                            self.f_y.append(fj*(self.y_curr-self.y_curr0[j])/r)
                        if r2==r:
                            self.f_x.append(fj*(self.x_curr-self.x_curr0[j]-8)/r)
                            self.f_y.append(fj*(self.y_curr-self.y_curr0[j])/r)
                        if r3==r:
                            self.f_x.append(fj*(self.x_curr-self.x_curr0[j]+8)/r)
                            self.f_y.append(fj*(self.y_curr-self.y_curr0[j])/r)
                        if r4==r:
                            self.f_x.append(fj*(self.x_curr-self.x_curr0[j])/r)
                            self.f_y.append(fj*(self.y_curr-self.y_curr0[j]-8)/r)
                        if r5==r:
                            self.f_x.append(fj*(self.x_curr-self.x_curr0[j])/r)
                            self.f_y.append(fj*(self.y_curr-self.y_curr0[j]+8)/r)
                self.a_x=sum(self.f_x)
                self.a_y=sum(self.f_y)
            for i in range(1):
                self.x_new=2*self.x_curr-self.x_prev+self.a_x*(self.dt**2)
                self.y_new=2*self.y_curr-self.y_prev+self.a_y*(self.dt**2)
                self.x_new=self.x_new%8
                self.y_new=self.y_new%8
                self.v_x=(self.x_new-self.x_prev)/(2*self.dt)
                self.v_y=(self.y_new-self.y_prev)/(2*self.dt)
            for i in range(1):
                self.x_prev=self.x_curr
                self.x_curr=self.x_new
                self.y_prev=self.y_curr
                self.y_curr=self.y_new
            if self.t%5==0:
                pl.plot(self.x_curr,self.y_curr,'g.')
            self.t=self.t+1
        pl.plot(self.x_curr,self.y_curr,'.')
        pl.show()
a=dilutegas()
a.calculate()
