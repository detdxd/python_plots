#!/usr/bin/env python
#
#===========================================
# this script is for 2d-color overlaid by velocity plotting 
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
den=loaddata("./datas/denascii.out5")
ux=loaddata("./datas/uxascii.out5")
uy=loaddata("./datas/uyascii.out5")

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

#extract data from len(x)*len(y) array data 
imax=800
jmax=800

#extract iplot*jplot array data for velocity ploting
iplot=20
jplot=20
idd=int(imax/iplot) #use "int" function in python3
jdd=int(jmax/jplot)
x0=np.zeros((iplot),dtype=float)
y0=np.zeros((jplot),dtype=float)
ux0=np.zeros((iplot,jplot),dtype=float)
uy0=np.zeros((iplot,jplot),dtype=float)

i1=0
for i in range(0,iplot):
    x0[i]=x[i1]
    y0[i]=y[i1]
    j1=0
    for j in range(0,jplot):
        ux0[i,j]=ux[i1,j1]
        uy0[i,j]=uy[i1,j1]
        j1=j1+jdd
    i1=i1+idd

x1=np.zeros((iplot),dtype=float)
ulg=np.zeros((iplot,jplot*2-1),dtype=float)

x1=x0
y1=yreflect(y0,jplot)
ux1=datareflect(ux0,iplot,jplot)
uy1=vecyreflect(uy0,iplot,jplot)
ulg=np.log10(np.sqrt(ux1**2+uy1**2))

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

pcm=ax.pcolormesh(yd,xd,den1,vmin=-27.,vmax=-25.,cmap=cm.jet)
Q = plt.quiver(y1,x1,uy1,ux1,color='r',
               pivot='mid', units='width') #velocity plotting
qk = plt.quiverkey(Q, 0.7, 0.3, 1e7, r'$100km/s$', labelpos='E',
                   coordinates='figure')
plt.gca().set_aspect('equal')

#set colorbar:
plt.subplots_adjust(0.1,0.25,0.8,0.95)# (left,bottom,right,top)
cax = plt.axes([0.1, 0.15, 0.7, 0.02])  #[left,bottom,width,height]
cbar=plt.colorbar(pcm,cax=cax,orientation='horizontal')
cbar.set_label('$lg(\\rho/g$ $cm^{-3})$')
cbar.set_ticks(np.linspace(-27,-25,5))

del x,y,x1,y1,xd,yd,den,den1,ux,uy,ux1,uy1,ux0,uy0
fig.savefig("./denvec.png")
#fig.show()

