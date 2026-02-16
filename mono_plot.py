import matplotlib.pyplot as plt
import numpy as np

plt.style.use("/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent27/Plots/Apratim_Style.mplstyle")

a = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Plots/BL1.dat')
print('A done')
b = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Plots/SL1.dat')
print('A done')
c = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Plots/BL2.dat')
print('A done')
d = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Plots/SL2.dat')

n_bins = 200
length = 25

Y = [[],[],[],[]]

# f = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent27/Plots/mon1.dat')
# g = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent27/Plots/mon2.dat')
# a1 = []
# b1 = []
# c1 = []
# d1 = []

e = np.concatenate((a,b,c,d))

a = a/25.0
b = b/25.0
c = c/25.0
d = d/25.0
e = e/25.0
																																																																																																																																				

fig,ax = plt.subplots(figsize = (8,8))

def Hist_Apr(data,bins = 10,label = None,linewidth = 2,markersize = 10,x_range = None,color = None,marker = '--o'):
    if(x_range == None):
        x_range = [data.min(),data.max()]
    p = np.histogram(data,weights = np.ones_like(data)/len(data),bins = bins,range = x_range)
    x = (p[1][:-1]+p[1][1:])/2
    y = p[0]
    ax.plot(x,y,marker,label = label,linewidth = linewidth,markersize = markersize,color = color)
    print(len(y))
    Y.append(y)
    

Hist_Apr(a,bins = n_bins, label = 'Big Subloop-P1')
#y1 = y.copy()
Hist_Apr(b,bins = n_bins, label = 'Small Subloops-P1')
#y2 = y.copy()
Hist_Apr(c,bins = n_bins, label = 'Big Subloop-P2')
#y3 = y.copy()
Hist_Apr(d,bins = n_bins, label = 'Small Subloops-P2')
#y4 = y.copy()
Hist_Apr(e,bins = n_bins, label = 'Total')

#print(Y)

plt.xlabel('z/L')
plt.ylabel(r'$\varrho$')

plt.xticks(fontweight = 'bold', size = 20)
plt.yticks(fontweight = 'bold', size = 20)

plt.ylim((0,0.016))

plt.legend(prop={'size':20, 'weight':'bold'})
# # plt.grid()                                      
plt.tight_layout()
plt.savefig('Mono_Arc2_v1.png')
plt.show()

# plt.hist(f-g, bins = 1000, histtype = 'step', density = True, label = '50')
# plt.hist(g, bins = 1000, histtype = 'step', density = True, label = '150')


