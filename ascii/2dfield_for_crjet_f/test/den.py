#!/usr/bin/python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
#读取数据
den0=np.loadtxt(fname='./denascii.out2',dtype=float)
#把数据重构成1100*1100的数组
denl=np.swapaxes(np.take(den0,-np.arange(1100**2).reshape([1100,1100])),0,1)
#翻转补齐另一半数据
denr=np.fliplr(denl)
den=np.hstack((denl,denr))


fig, ax1=plt.subplots(figsize=(15,6))
den1=ax1.imshow(den,cmap='jet')
fig.colorbar(den1,ax=ax1)
#fig.savefig("./den.pdf")
plt.show()
