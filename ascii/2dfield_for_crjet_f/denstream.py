#!/usr/bin/env python
#
#===========================================
# this script is for 2d-color overlaid by streamline plotting 
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


x=loaddata("./datas/xhascii.out4")
y=loaddata("./datas/yhascii.out4")
den=loaddata("./datas/denascii.out4")
ux=loaddata("./datas/uxascii.out4")
uy=loaddata("./datas/uyascii.out4")

#data analyzing and ploting:
cmkpc=3.08e21

x=x/cmkpc
y=y/cmkpc
den=log10(den)

den.shape=len(x),len(y) # transform 1d array to 2d array 
ux.shape=len(x),len(y)
uy.shape=len(x),len(y)
den=transpose(den)
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
#extract imax*jmax density from len(x)*len(y) density and transform it to imax*2jmax:
xd=np.zeros((imax),dtype=float)
for i in range(0,imax):xd[i]=x[i]
yd=yreflect(y,jmax)
den1=datareflect(den,imax,jmax)

print ("x1.shape:",x1.shape)
print ("y1.shape:",y1.shape)
print ("ux1.shape:",ux1.shape)
print ("uy1.shape:",uy1.shape)

print ("xd.shape:",xd.shape)
print ("yd.shape:",yd.shape)
print ("den1.shape:",den1.shape)

#plotting:
print ("plotting:")
fig=plt.figure(figsize=(8,4))
ax=fig.add_subplot(111) # 111 means setting 1 row and 1 column and this is the first plot

pcm=ax.pcolormesh(yd,xd,den1,vmin=-27.,vmax=-25.,cmap='bwr')
strm = ax.streamplot(y1, x1, uy1, ux1, color=ulg,
                     density=[4,2],linewidth=1.0, cmap='brg') #streamline plotting
ax.set_xlim(-200.,200.)
ax.set_ylim(0.,200.)
plt.gca().set_aspect('equal')

plt.subplots_adjust(0.1,0.25,0.9,0.95)# (left,bottom,right,top)
#set colorbar:
cax1 = plt.axes([0.86, 0.25, 0.015, 0.7])
cbar=fig.colorbar(strm.lines,cax=cax1,orientation='vertical')
cbar.set_label('$lg v(cm/s)$')
cax2 = plt.axes([0.15, 0.15, 0.7, 0.02])  #[left,bottom,width,height]
cbar=plt.colorbar(pcm,cax=cax2,orientation='horizontal')
cbar.set_label('$lg(\\rho/g$ $cm^{-3})$')
cbar.set_ticks(np.linspace(-27,-25,5))

fig.savefig("./denstream.png")
#fig.show()

