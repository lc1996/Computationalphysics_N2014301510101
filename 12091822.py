# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 18:13:55 2016

@author: luchao96
"""

import math
import pylab as pl
x=[1.38,2.71,4.06,5.41,6.79,8.10]
y=[0.67,1.30,1.94,2.57,3.22,3.82]
x1=[1.30,2.56,3.83,5.12,6.44,7.69]
y1=[0.75,1.45,2.16,2.87,3.57,4.24]
x2=[1.44,2.83,4.24,5.65,7.10,8.47]
y2=[0.60,1.18,1.76,2.33,2.91,3.45]
pl.plot(x,y,'.-',label='20lx')
pl.plot(x1,y1,'.-',label='30lx')
pl.plot(x2,y2,'.-',label='62lx')
pl.legend(loc='best')
pl.xlim(1.25,8.50)
pl.ylim(0.55,4.27)
pl.xlabel('I(mA)')
pl.ylabel('U(V)')
pl.title('Plot of U-I')
pl.show()