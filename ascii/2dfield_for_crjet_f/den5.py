#!/usr/bin/env python
#
#===========================================
# this script is for 2d-color plotting
# 5 plots together 
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

x=loaddata("./datas/xhascii.out5")
y=loaddata("./datas/yhascii.out5")
den_1=loaddata("./datas/denascii.out1")
den_2=loaddata("./datas/denascii.out2")
den_3=loaddata("./datas/denascii.out3")
den_4=loaddata("./datas/denascii.out4")
den_5=loaddata("./datas/denascii.out5")

#data analyzing and ploting:
cmkpc=3.08e21

x=x/cmkpc
y=y/cmkpc

den_1=log10(den_1)
den_2=log10(den_2)
den_3=log10(den_3)
den_4=log10(den_4)
den_5=log10(den_5)

den_1.shape=len(x),len(y) # transform 1d array to 2d array
den_1=transpose(den_1)
den_2.shape=len(x),len(y)
den_2=transpose(den_2)
den_3.shape=len(x),len(y) # transform 1d array to 2d array
den_3=transpose(den_3)
den_4.shape=len(x),len(y)
den_4=transpose(den_4)
den_5.shape=len(x),len(y)
den_5=transpose(den_5)

imax=800
jmax=800
#extract iplot*jplot array data for velocity ploting

xx=np.zeros((imax),dtype=float)
for i in range(0,imax):xx[i]=x[i]
yy=yreflect(y,jmax)
den_1=datareflect(den_1,imax,jmax)
den_2=datareflect(den_2,imax,jmax)
den_3=datareflect(den_3,imax,jmax)
den_4=datareflect(den_4,imax,jmax)
den_5=datareflect(den_5,imax,jmax)

#plotting:
print ("plotting:")
fig=plt.figure(figsize=(4,10))

ax=fig.add_subplot(511)
#ax = plt.axes([0.2, 0.6, 0.7, 0.35]) #[left,bottom,width,height]
pcm=ax.pcolormesh(yy,xx,den_1,vmin=-27.,vmax=-25.,cmap=cm.bwr)
#pcm=ax.contourf(yd,xd,ulg1_1,70,vmin=4.5,vmax=9.0,cmap=cm.jet)
ax.set_xticks([])
ax.set_ylabel('z(kpc)')
#ax.set_title('run R3',loc='left',fontsize=10)
ax.set_title('t= 50Myr',loc='right',fontsize=9)
plt.gca().set_aspect('equal')

ax=fig.add_subplot(512)
#ax = plt.axes([0.2, 0.6, 0.7, 0.35])  #[left,bottom,width,height]
pcm=ax.pcolormesh(yy,xx,den_2,vmin=-27.,vmax=-25.,cmap=cm.bwr)
#pcm=ax.contourf(yd,xd,ulg1_2,70,vmin=4.5,vmax=9.0,cmap=cm.jet)
ax.set_xticks([])
ax.set_ylabel('z(kpc)')
ax.set_title('t=100Myr',loc='right',fontsize=9)
plt.gca().set_aspect('equal')

ax=fig.add_subplot(513)
#ax = plt.axes([0.2, 0.70, 0.7, 0.28])  #[left,bottom,width,height]
pcm=ax.pcolormesh(yy,xx,den_3,vmin=-27.,vmax=-25.,cmap=cm.bwr)
#pcm=ax.contourf(yd,xd,ulg1_3,70,vmin=4.5,vmax=9.0,cmap=cm.jet)
ax.set_xticks([])
ax.set_ylabel('z(kpc)')
ax.set_title('t=200Myr',loc='right',fontsize=9)
plt.gca().set_aspect('equal')

ax=fig.add_subplot(514)
#ax = plt.axes([0.2, 0.41, 0.7, 0.28])  #[left,bottom,width,height]
pcm=ax.pcolormesh(yy,xx,den_4,vmin=-27.,vmax=-25.,cmap=cm.bwr)
#pcm=ax.contourf(yd,xd,ulg1_4,70,vmin=4.5,vmax=9.0,cmap=cm.jet)
ax.set_xticks([])
ax.set_ylabel('z(kpc)')
ax.set_title('t=300Myr',loc='right',fontsize=9)
plt.gca().set_aspect('equal')

ax=fig.add_subplot(515)
#ax = plt.axes([0.2, 0.12, 0.7, 0.28])  #[left,bottom,width,height]
pcm=ax.pcolormesh(yy,xx,den_5,vmin=-27.,vmax=-25.,cmap=cm.bwr)
#pcm=ax.contourf(yd,xd,ulg1_5,70,vmin=4.5,vmax=9.0,cmap=cm.jet)
ax.set_xlabel('x(kpc)')
ax.set_ylabel('z(kpc)')
ax.set_title('t=500Myr',loc='right',fontsize=9)
plt.gca().set_aspect('equal')


#set colorbar:
plt.subplots_adjust(0.2,0.2,0.9,0.9)# (left,bottom,right,top)
cax = plt.axes([0.25, 0.137, 0.6, 0.01])  #[left,bottom,width,height]
cbar=plt.colorbar(pcm,cax=cax,orientation='horizontal')
cbar.set_label('$lg(\\rho/g cm^{-3}) $')
cbar.set_ticks(np.linspace(-27,-25,4))

fig.savefig("./den5.png")
#fig.show()

