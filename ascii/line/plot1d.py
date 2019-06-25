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
    print ( "len(%s): %d"%(filename,len(x)) )
    x=np.array(x)  #transform the list x to an array
    return x
#
x=loaddata("./datas/data1d.out",2,0)
y=loaddata("./datas/data1d.out",2,1)

print (x)
print (y)

#plot figure:
fig=plt.figure(figsize=(10,5)) 

ax=fig.add_subplot(121)  # 121 means setting 1 row and 2 column and this is the first plot
ax.plot(x,x+y,color='r',label='$\\rho 1$',lw=1,ls='-') # lw is line width , ls is line style
ax.plot(x,x+y+1,color='b',label='$\\rho 2$',lw=1,ls='--')
ax.plot(x,x+y+2,color='g',label='$\\rho 3$',lw=1,ls=':')
ax.set_xlim(0,6)
ax.set_ylim(0,12)
#ax.set_xlabel('$M_{\odot}$')
ax.set_ylabel('$\eta$')
ax.set_title('x-y 1d plot')
#ax.grid()
legend = ax.legend(loc='upper center', fontsize='x-small') #setting label in 'ax.plot'

ax=fig.add_subplot(122) # 121 means setting 1 row and 2 column and this is the second plot
ax.plot(x/1,x+y,c='k',label='$\\rho 1$',lw=1,ls='-.')
ax.plot(x,x+y+1,color='m',label='$\\rho 2$',lw=1,ls='steps')
ax.plot(x,x+y+2,color='y',label='$\\rho 3$',lw=1)
ax.set_xlim(0,6)
ax.set_ylim(0,12)
ax.set_xlabel('$M_{\odot}$')
ax.set_ylabel('$\eta$')
#ax.set_title('x-y 1d plot')
#ax.grid()
legend = ax.legend(loc='upper center', fontsize='x-small')

fig.savefig("./xy1d.png")
plt.show()

