# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 11:53:13 2017

@author: luchao96
"""

#import random
#a=[random.uniform(0,2) for i in range(3)]
#x=a[0]-1
#y=a[0]+1
#z=a[0]
#print x,y,z,a
import math
import pylab as pl
import random
class dilutegas:
    def __init__(self,dt=0.004):
        self.dt=dt
        self.x_curr=[1,1,1,1,3,3,3,3,5,5,5,5,7,7,7,7]
        self.y_curr=[1,3,5,7,1,3,5,7,1,3,5,7,1,3,5,7]
        #pl.plot(self.x_curr,self.y_curr,'o')
        self.x_prev=[0 for i in range(16)]
        self.y_prev=[0 for i in range(16)]
        self.x_new=[0 for i in range(16)]
        self.y_new=[0 for i in range(16)]
        self.v_x=[0 for i in range(16)]
        self.v_y=[0 for i in range(16)]
        self.a_x=[0 for i in range(16)]
        self.a_y=[0 for i in range(16)]
        self.f_x=[]
        self.f_y=[]
        self.t=[0]
        self.potential=[0 for i in range(16)]
        self.energy=[0 for i in range(16)]
        self.temperature=[]
    def calculate(self):
        ax=[random.random() for i in range(16)]
        bx=[random.random() for i in range(16)]
        vx=[random.random() for i in range(16)]
        vy=[random.random() for i in range(16)]
        speed=[]
        sx=[]
        total=[]
        t=[]
        count=[0 for i in range(20)]
        count1=count
        count2=count
        speeds=[0 for i in range(16)]
        for i in range(16):
            self.x_curr[i]=self.x_curr[i]+2*(ax[i]-0.5)*0.2
            self.y_curr[i]=self.y_curr[i]+2*(bx[i]-0.5)*0.2
            self.v_x[i]=2*(vx[i]-0.5)*3
            self.v_y[i]=2*(vy[i]-0.5)*3
        #pl.plot(self.x_curr,self.y_curr,'.')
        for i in range(16):
            self.x_prev[i]=self.x_curr[i]-self.v_x[i]*self.dt
            self.y_prev[i]=self.y_curr[i]-self.v_y[i]*self.dt
        while self.t[-1]<3000:
            for i in range(16):
                self.f_x=[]
                self.f_y=[]
                self.potential[i]=0
                for j in range(16):
                    if j!=i:
                        r1=math.pow((self.x_curr[i]-self.x_curr[j])**2+(self.y_curr[i]-self.y_curr[j])**2,0.5)
                        r2=math.pow((self.x_curr[i]-self.x_curr[j]-8)**2+(self.y_curr[i]-self.y_curr[j])**2,0.5)
                        r3=math.pow((self.x_curr[i]-self.x_curr[j]+8)**2+(self.y_curr[i]-self.y_curr[j])**2,0.5)
                        r4=math.pow((self.x_curr[i]-self.x_curr[j])**2+(self.y_curr[i]-self.y_curr[j]-8)**2,0.5)
                        r5=math.pow((self.x_curr[i]-self.x_curr[j])**2+(self.y_curr[i]-self.y_curr[j]+8)**2,0.5)
                        r=min([r1,r2,r3,r4,r5])
                        if r==0:
                            print self.t[-1],i,j
                        if r<3:
                            fj=24*(2/math.pow(r,13)-1/math.pow(r,7))
                            pj=4*(1/math.pow(r,12)-1/math.pow(r,6))
                            self.potential[i]=self.potential[i]+pj
                            if r1==r:
                                self.f_x.append(fj*(self.x_curr[i]-self.x_curr[j])/r)
                                self.f_y.append(fj*(self.y_curr[i]-self.y_curr[j])/r)
                            if r2==r:
                                self.f_x.append(fj*(self.x_curr[i]-self.x_curr[j]-8)/r)
                                self.f_y.append(fj*(self.y_curr[i]-self.y_curr[j])/r)
                            if r3==r:
                                self.f_x.append(fj*(self.x_curr[i]-self.x_curr[j]+8)/r)
                                self.f_y.append(fj*(self.y_curr[i]-self.y_curr[j])/r)
                            if r4==r:
                                self.f_x.append(fj*(self.x_curr[i]-self.x_curr[j])/r)
                                self.f_y.append(fj*(self.y_curr[i]-self.y_curr[j]-8)/r)
                            if r5==r:
                                self.f_x.append(fj*(self.x_curr[i]-self.x_curr[j])/r)
                                self.f_y.append(fj*(self.y_curr[i]-self.y_curr[j]+8)/r)
                if abs(self.v_x[0])<10 and abs(self.v_y[0])<10:
                    speed0=math.pow(self.v_x[i]**2+self.v_y[i]**2,0.5)
                    self.energy[i]=self.potential[i]+speed0*speed0/2
                    sx.append(math.pow(self.v_x[i]**2+self.v_y[i]**2,1)/2)
                self.a_x[i]=sum(self.f_x)
                self.a_y[i]=sum(self.f_y)
                
                if self.t[-1]>0 and self.t[-1]<2000:
                    if speed0<4:
                        count[int(speed0//0.2)]=count[int(speed0//0.2)]+1
                if self.t[-1]>2000 and self.t[-1]<4000:
                    if speed0<4:
                        count1[int(speed0//0.2)]=count1[int(speed0//0.2)]+1
                if self.t[-1]>4000 and self.t[-1]<6000:
                    if speed0<4:
                        count2[int(speed0//0.2)]=count2[int(speed0//0.2)]+1
            if self.t[-1]==1000:
                print count
                sum0=sum(count)*1.0
                print sum0
                for p in range(20):
                    count[p]=count[p]/sum0
                print count
                #pl.plot([0.1+i*0.2 for i in range(20)],count,'o-',label=str('t=0-10'))
            if self.t[-1]==4000:
                print count1
                sum0=sum(count1)*1.0
                print sum0
                for p in range(20):
                    count[p]=count[p]/sum0
                print count1
                #pl.plot([0.1+i*0.2 for i in range(20)],count1,'o-',label=str('t=10-20'))
            if self.t[-1]==6000:
                print count2
                sum0=sum(count1)*1.0
                print sum0
                for p in range(20):
                    count[p]=count[p]/sum0
                print count2
                #pl.plot([0.1+i*0.2 for i in range(20)],count2,'o-',label=str('t=20-30'))  
            for i in range(16):
                self.x_new[i]=2*self.x_curr[i]-self.x_prev[i]+self.a_x[i]*(self.dt**2)
                self.y_new[i]=2*self.y_curr[i]-self.y_prev[i]+self.a_y[i]*(self.dt**2)
                self.x_new[i]=self.x_new[i]%8
                self.y_new[i]=self.y_new[i]%8
                self.v_x[i]=(self.x_new[i]-self.x_prev[i])/(2*self.dt)
                self.v_y[i]=(self.y_new[i]-self.y_prev[i])/(2*self.dt)
            for i in range(16):
                self.x_prev[i]=self.x_curr[i]
                self.x_curr[i]=self.x_new[i]
                self.y_prev[i]=self.y_curr[i]
                self.y_curr[i]=self.y_new[i]
            #if self.t[-1]%10==0:
             #   pl.plot(self.x_curr[0],self.y_curr[0],'g.')
            if abs(self.v_x[0])<100 and abs(self.v_y[0])<100:
                speed.append(self.dt*self.t[-1])
                
            for i in range(16):
                if abs(self.v_x[i])<10 and abs(self.v_y[i])<10:
                    speeds[i]=speeds[i]+math.pow(self.v_x[i]**2+self.v_y[i]**2,1)/2
          
            e=[sum(self.energy)]
            tt=sum(sx)
            b=[abs(max(self.v_x)),abs(min(self.v_x)),abs(max(self.v_y)),abs(min(self.v_y))]
            if max(b)<10 and e[0]<64:
                self.temperature.append(sum(sx)/len(sx))
                total.append(e[0])
                t.append(self.t[-1]*self.dt+self.dt)
            self.t.append(self.t[-1]+1)
        #print max(self.x_curr),max(self.y_curr)
        #pl.plot(self.x_curr,self.y_curr,'ro')
        pl.plot(t,self.temperature)
        #pl.plot(speed,self.energy)
        #pl.plot(t,total)
        #pl.ylim(-10,10)
        
        speeds=[speeds[i]/len(speed) for i in range(16)]
        vc=sum(speeds)/len(speeds)
        print max(speeds),speeds,vc
        #pl.show()
        pl.xlabel('time')
        pl.ylabel('Temperature')
        pl.title('Temperature versus time')
        #pl.legend(loc='best')
        pl.show()

a=dilutegas()
a.calculate()