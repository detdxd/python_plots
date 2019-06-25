#!/usr/bin/env python
#
#===========================================
# this script is for 2d-color(modulus of velocity) overlaid by velocity plotting
# five plots together! 
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

def xextract(x,idd,iplot):
    x0=np.zeros((iplot),dtype=float)
    i1=0
    for i in range(0,iplot):
        x0[i]=x[i1]
        i1=i1+idd
    return x0
def vecextract(u,idd,jdd,iplot,jplot):
    u0=np.zeros((iplot,jplot),dtype=float)
    i1=0
    for i in range(0,iplot):
        j1=0
        for j in range(0,jplot):
            u0[i,j]=u[i1,j1]
            j1=j1+jdd
        i1=i1+idd
    return u0


x=loaddata("./datas/xhascii.out5")
y=loaddata("./datas/yhascii.out5")
ux_1=loaddata("./datas/uxascii.out1")
uy_1=loaddata("./datas/uyascii.out1")

ux_2=loaddata("./datas/uxascii.out2")
uy_2=loaddata("./datas/uyascii.out2")

ux_3=loaddata("./datas/uxascii.out3")
uy_3=loaddata("./datas/uyascii.out3")

ux_4=loaddata("./datas/uxascii.out4")
uy_4=loaddata("./datas/uyascii.out4")

ux_5=loaddata("./datas/uxascii.out5")
uy_5=loaddata("./datas/uyascii.out5")
#data analyzing and ploting:
cmkpc=3.08e21

x=x/cmkpc
y=y/cmkpc

ux_1.shape=len(x),len(y)
uy_1.shape=len(x),len(y)
ux_1=transpose(ux_1) 
uy_1=transpose(uy_1)
ulg_1=np.log10(np.sqrt(ux_1**2+uy_1**2))

ux_2.shape=len(x),len(y)
uy_2.shape=len(x),len(y)
ux_2=transpose(ux_2)
uy_2=transpose(uy_2)
ulg_2=np.log10(np.sqrt(ux_2**2+uy_2**2))

ux_3.shape=len(x),len(y)
uy_3.shape=len(x),len(y)
ux_3=transpose(ux_3)
uy_3=transpose(uy_3)
ulg_3=np.log10(np.sqrt(ux_3**2+uy_3**2))

ux_4.shape=len(x),len(y)
uy_4.shape=len(x),len(y)
ux_4=transpose(ux_4)
uy_4=transpose(uy_4)
ulg_4=np.log10(np.sqrt(ux_4**2+uy_4**2))

ux_5.shape=len(x),len(y)
uy_5.shape=len(x),len(y)
ux_5=transpose(ux_5)
uy_5=transpose(uy_5)
ulg_5=np.log10(np.sqrt(ux_5**2+uy_5**2))
#extract data from len(x)*len(y) array data 
imax=800
jmax=800
#extract iplot*jplot array data for velocity ploting
iplot=16
jplot=16
idd=int(imax/iplot)
jdd=int(jmax/jplot)

x0=xextract(x,idd,iplot)
y0=xextract(y,jdd,jplot)
ux0_1=vecextract(ux_1,idd,jdd,iplot,jplot)
uy0_1=vecextract(uy_1,idd,jdd,iplot,jplot)
x1=x0
y1=yreflect(y0,jplot)
ux1_1=datareflect(ux0_1,iplot,jplot)
uy1_1=vecyreflect(uy0_1,iplot,jplot)

ux0_2=vecextract(ux_2,idd,jdd,iplot,jplot)
uy0_2=vecextract(uy_2,idd,jdd,iplot,jplot)
ux1_2=datareflect(ux0_2,iplot,jplot)
uy1_2=vecyreflect(uy0_2,iplot,jplot)

ux0_3=vecextract(ux_3,idd,jdd,iplot,jplot)
uy0_3=vecextract(uy_3,idd,jdd,iplot,jplot)
ux1_3=datareflect(ux0_3,iplot,jplot)
uy1_3=vecyreflect(uy0_3,iplot,jplot)

ux0_4=vecextract(ux_4,idd,jdd,iplot,jplot)
uy0_4=vecextract(uy_4,idd,jdd,iplot,jplot)
ux1_4=datareflect(ux0_4,iplot,jplot)
uy1_4=vecyreflect(uy0_4,iplot,jplot)

ux0_5=vecextract(ux_5,idd,jdd,iplot,jplot)
uy0_5=vecextract(uy_5,idd,jdd,iplot,jplot)
ux1_5=datareflect(ux0_5,iplot,jplot)
uy1_5=vecyreflect(uy0_5,iplot,jplot)
#extract imax*jmax density from len(x)*len(y) density and transform it to imax*2jmax:
xd=np.zeros((imax),dtype=float)
for i in range(0,imax):xd[i]=x[i]
yd=yreflect(y,jmax)

ulg1_1=datareflect(ulg_1,imax,jmax)
ulg1_2=datareflect(ulg_2,imax,jmax)
ulg1_3=datareflect(ulg_3,imax,jmax)
ulg1_4=datareflect(ulg_4,imax,jmax)
ulg1_5=datareflect(ulg_5,imax,jmax)

U_1=ux1_1/np.sqrt(ux1_1**2+uy1_1**2)
V_1=uy1_1/np.sqrt(ux1_1**2+uy1_1**2)

U_2=ux1_2/np.sqrt(ux1_2**2+uy1_2**2)
V_2=uy1_2/np.sqrt(ux1_2**2+uy1_2**2)

U_3=ux1_3/np.sqrt(ux1_3**2+uy1_3**2)
V_3=uy1_3/np.sqrt(ux1_3**2+uy1_3**2)

U_4=ux1_4/np.sqrt(ux1_4**2+uy1_4**2)
V_4=uy1_4/np.sqrt(ux1_4**2+uy1_4**2)

U_5=ux1_5/np.sqrt(ux1_5**2+uy1_5**2)
V_5=uy1_5/np.sqrt(ux1_5**2+uy1_5**2)

#plotting:
print ("plotting:")
fig=plt.figure(figsize=(4,10))

ax=fig.add_subplot(511)
#ax = plt.axes([0.2, 0.6, 0.7, 0.35]) #[left,bottom,width,height]
pcm=ax.pcolormesh(yd,xd,ulg1_1,vmin=4.5,vmax=9.0,cmap=cm.jet)
#pcm=ax.contourf(yd,xd,ulg1_1,70,vmin=4.5,vmax=9.0,cmap=cm.jet)
Q = plt.quiver(y1,x1,V_1,U_1,color='black',headwidth=6,headlength=4,
               pivot='mid', units='width') #velocity plotting
ax.set_xticks([])
ax.set_ylabel('z(kpc)')
ax.set_title('run R3',loc='left',fontsize=10)
ax.set_title('t=5Myr',loc='right',fontsize=9)
plt.gca().set_aspect('equal')

ax=fig.add_subplot(512)
#ax = plt.axes([0.2, 0.6, 0.7, 0.35])  #[left,bottom,width,height]
pcm=ax.pcolormesh(yd,xd,ulg1_2,vmin=4.5,vmax=9.0,cmap=cm.jet)
#pcm=ax.contourf(yd,xd,ulg1_2,70,vmin=4.5,vmax=9.0,cmap=cm.jet)
Q = plt.quiver(y1,x1,V_2,U_2,color='black',headwidth=6,headlength=4,
               pivot='mid', units='width') #velocity plotting
ax.set_xticks([])
ax.set_ylabel('z(kpc)')
ax.set_title('t=250Myr',loc='right',fontsize=9)
plt.gca().set_aspect('equal')

ax=fig.add_subplot(513)
#ax = plt.axes([0.2, 0.70, 0.7, 0.28])  #[left,bottom,width,height]
pcm=ax.pcolormesh(yd,xd,ulg1_3,vmin=4.5,vmax=9.0,cmap=cm.jet)
#pcm=ax.contourf(yd,xd,ulg1_3,70,vmin=4.5,vmax=9.0,cmap=cm.jet)
Q = plt.quiver(y1,x1,V_3,U_3,color='black',headwidth=6,headlength=4,
               pivot='mid', units='width') #velocity plotting
ax.set_xticks([])
ax.set_ylabel('z(kpc)')
ax.set_title('t=350Myr',loc='right',fontsize=9)
plt.gca().set_aspect('equal')

ax=fig.add_subplot(514)
#ax = plt.axes([0.2, 0.41, 0.7, 0.28])  #[left,bottom,width,height]
pcm=ax.pcolormesh(yd,xd,ulg1_4,vmin=4.5,vmax=9.0,cmap=cm.jet)
#pcm=ax.contourf(yd,xd,ulg1_4,70,vmin=4.5,vmax=9.0,cmap=cm.jet)
Q = plt.quiver(y1,x1,V_4,U_4,color='black',headwidth=6,headlength=4,
               pivot='mid', units='width') #velocity plotting
ax.set_xticks([])
ax.set_ylabel('z(kpc)')
ax.set_title('t=500Myr',loc='right',fontsize=9)
plt.gca().set_aspect('equal')

ax=fig.add_subplot(515)
#ax = plt.axes([0.2, 0.12, 0.7, 0.28])  #[left,bottom,width,height]
pcm=ax.pcolormesh(yd,xd,ulg1_5,vmin=4.5,vmax=9.0,cmap=cm.jet)
#pcm=ax.contourf(yd,xd,ulg1_5,70,vmin=4.5,vmax=9.0,cmap=cm.jet)
Q = plt.quiver(y1,x1,V_5,U_5,color='black',headwidth=6,headlength=4,
               pivot='mid', units='width') #velocity plotting
ax.set_xlabel('x(kpc)')
ax.set_ylabel('z(kpc)')
ax.set_title('t=900Myr',loc='right',fontsize=9)
plt.gca().set_aspect('equal')


#set colorbar:
plt.subplots_adjust(0.2,0.2,0.9,0.9)# (left,bottom,right,top)
cax = plt.axes([0.25, 0.137, 0.6, 0.01])  #[left,bottom,width,height]
cbar=plt.colorbar(pcm,cax=cax,orientation='horizontal')
cbar.set_label('lg(v/cm $s^{-1}$)')
cbar.set_ticks(np.linspace(3.0,9.0,7))

fig.savefig("./vmod_v5.png")
#fig.show()

