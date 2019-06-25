#!/usr/bin/env python
#
#===========================================
# this script is a streamline-plotting code 
# from a files like: 'uxasciiout1','uyasciiout2'
# Det, May 17,2018
#===========================================
#

import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pylab import *

#define a function for loading data 
def loaddata(filename):
    fo=open(filename,'r')
    data=fo.readlines()
    fo.close()
    x=[]
    for line in data:
        line=line.split()
        x.append(float(line[0]))
    del data
    print ("len(%s): %d"%(filename,len(x)))
    x=np.array(x)
    return x
#define functions to reflect y and data for axisymmetric plotting:
def yreflect(y,jend):
    y1=np.zeros((jend*2-1),dtype=float)
    for j in range(0,jend*2-1):
        if j<=jend-1 :
            y1[j]=-y[jend-1-j]
        else:
            y1[j]=y[j-jend+1]
    return y1

def datareflect(data,iend,jend):
    data1=np.zeros((iend,jend*2-1),dtype=float)
    for i in range(0,iend):
        for j in range(0,jend*2-1):
            if j<=jend-1 :
                data1[i,j]=data[i,jend-1-j]
            else:
                data1[i,j]=data[i,j-jend+1]
    return data1
def vecyreflect(vecy,iend,jend):
    data1=np.zeros((iend,jend*2-1),dtype=float)
    for i in range(0,iend):
        for j in range(0,jend*2-1):
            if j<=jend-1 :
                data1[i,j]=-vecy[i,jend-1-j]
            else:
                data1[i,j]=vecy[i,j-jend+1]
    return data1


x=loaddata("./datas/xhascii.out5")
y=loaddata("./datas/yhascii.out5")
ux=loaddata("./datas/uxascii.out5")
uy=loaddata("./datas/uyascii.out5")

#data analyzing and ploting:
cmkpc=3.08e21

x=x/cmkpc
y=y/cmkpc

ux.shape=len(x),len(y) # transform 1d array to 2d array 
uy.shape=len(x),len(y)
ux=transpose(ux)
uy=transpose(uy)
print ("ux.shape",ux.shape)

#extract imax*jmax array data from len(x)*len(y) array data and transform it to imax*2jmax:
imax=800
jmax=800
x1=np.zeros((imax),dtype=float) # define zero array x1
ulg=np.zeros((imax,jmax*2-1),dtype=float)

for i in range(0,imax): x1[i]=x[i]
y1=yreflect(y,jmax)
ux1=datareflect(ux,imax,jmax)
uy1=vecyreflect(uy,imax,jmax)

ulg=np.log10(np.sqrt(ux1**2+uy1**2))
print ("x1.shape:",x1.shape)
print ("y1.shape:",y1.shape)
print ("ux1.shape:",ux1.shape)
print ("uy1.shape:",uy1.shape)

#plotting:
print ("plotting:")
fig=plt.figure(figsize=(8,5))
ax=fig.add_subplot(111) # 111 means setting 1 row and 1 column and this is the first plot
strm = ax.streamplot(y1, x1, uy1, ux1, color=ulg, 
                     density=[8,4],linewidth=0.5, cmap='jet') #streamline plotting
ax.set_xlim(-200.,200.)
plt.gca().set_aspect('equal')

#set colorbar:
plt.subplots_adjust(0.1,0.15,0.9,0.95)# (left,bottom,right,top)
cax = plt.axes([0.1, 0.12, 0.8, 0.02])  #[left,bottom,width,height]
cbar=fig.colorbar(strm.lines,cax=cax,orientation='horizontal')
cbar.set_label('$lg v(cm/s)$')
#cbar.set_ticks(np.linspace(4,7,4))

del x,y,x1,y1,ux,uy,ux1,uy1
fig.savefig("./stream.png")
#fig.show()

