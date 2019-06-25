#!/usr/bin/env python
#
#===========================================
# script for line-plotting using ascii data
# Det, May 17,2018
#===========================================
#

import numpy as np
from pylab import *
import matplotlib.pyplot as plt

# define a function for loading data from column-ascii data
# istart is the data starting row number, jdata is the column number
def loaddata(filename,istart,jdata):
    fo=open(filename,'r')
    data=fo.readlines()
    fo.close()
    x=[]
    for line in data[istart:]:
        line=line.split()
        x.append(float(line[jdata]))
    del data
    print ("len(%s): %d"%(filename,len(x)))
    x=np.array(x)  #transform the list x to an array
    return x

tyr=loaddata("./datas/energyc.out",7,1)
eth=loaddata("./datas/energyc.out",7,3)
ek=loaddata("./datas/energyc.out",7,4)
epot=loaddata("./datas/energyc.out",7,6)

tMyr=tyr/1.e6
eth60=eth/1.e4
ek60=ek/1.e4
epot60=epot/1.e4

#plot figure:
fig=plt.figure(figsize=(6,6))

ax=fig.add_subplot(111) # 111 means setting 1 row and 1 column and this is the first plot
ax.plot(tMyr,eth60,color='r',label='$\Delta E_{th}$',lw=1,ls='-') # lw is line width , ls is line style
ax.plot(tMyr,ek60,color='b',label='$\Delta E_{k}$',lw=1,ls='--')
ax.plot(tMyr,epot60,color='g',label='$\Delta E_{pot}$',lw=1,ls=':')
ax.set_xlim(0,500)
ax.set_ylim(-9,2)
ax.set_xlabel('$t(Myr)$')
ax.set_ylabel('$E(10^{60}ergs)$')
ax.set_title('evolution of energy in AGN feedback')
#ax.grid()
legend = ax.legend(loc='best', fontsize='x-small') #setting label in 'ax.plot'

fig.savefig("./energy.pdf")
plt.show()

