import numpy as np
import matplotlib.pyplot as plt

plt.style.use("/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent27/Plots/Apratim_Style.mplstyle")

a5 = []
a6 = []
a7 = []
a8 = []

n_bins = 50

# Bin1 = np.zeros(bin_size)
# Bin2 = np.zeros(bin_size)
# Bin3 = np.zeros(bin_size)
# Bin4 = np.zeros(bin_size)

fig,ax = plt.subplots(figsize = (8,8))

for i in range(1,41):
    a1,b1,c1,d1 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Exp{}/Big_Loop1_COM.dat'.format(i),unpack = True)
    a2,b2,c2,d2 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Exp{}/Small_Loops1_COM.dat'.format(i),unpack = True)
    a3,b3,c3,d3 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Exp{}/Big_Loop2_COM.dat'.format(i),unpack = True)
    a4,b4,c4,d4 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent41/Exp{}/Small_Loops2_COM.dat'.format(i),unpack = True)

    d1 = d1/25.0
    d2 = d2/25.0
    d3 = d3/25.0
    d4 = d4/25.0

    for j in range(len(a1)):
        a5.append(d1[j])
        a6.append(d2[j])
        a7.append(d3[j])
        a8.append(d4[j])

def Hist_Apr(data,bins = 10,label = None,linewidth = 2,markersize = 10,x_range = None,color = None,marker = '--o'):
    if(x_range == None):
        x_range = [0,1]
    b = np.histogram(data,weights = np.ones_like(data)/len(data),bins = bins,range = x_range)
    x = (b[1][:-1]+b[1][1:])/2
    y = b[0]
    ax.plot(x,y,marker,label = label,linewidth = linewidth,markersize = markersize,color = color)

# y1, bin1 = np.histogram(a5,bins = bin_size,density = True)
# y2, bin2 = np.histogram(a6,bins = bin_size,density = True)
# y3, bin3 = np.histogram(a7,bins = bin_size,density = True)
# y4, bin4 = np.histogram(a8,bins = bin_size,density = True)

# # y4 = np.delete(y4,167)
# # bin4 = np.delete(bin4,167)

# for i in range(bin_size-1):
#     Bin1[i] = 0.5*(bin1[i] + bin1[i+1])
#     Bin2[i] = 0.5*(bin2[i] + bin2[i+1])
#     Bin3[i] = 0.5*(bin3[i] + bin3[i+1])
#     Bin4[i] = 0.5*(bin4[i] + bin4[i+1])
    
# plt.plot(Bin1,y1)
# plt.plot(Bin1,y1,'o',markersize = 10,label = 'Big-Loop 1')
# plt.plot(Bin2,y2)
# plt.plot(Bin2,y2,'*',markersize = 10,label = 'Small-Loops 1')
# plt.plot(Bin3,y3)
# plt.plot(Bin3,y3,'s',markersize = 10,label = 'Big-Loop 2')
# plt.plot(Bin4,y4)
# plt.plot(Bin4,y4,'+',markersize = 10,label = 'Small-Loops 2')


# # plt.hist(a5,bins='fd',density=True,stacked=True,histtype='step',label = 'Big Loop 1')
# # plt.hist(a6,bins='fd',density=True,stacked=True,histtype='step',label = 'Small Loops 1')
# # plt.hist(a7,bins='fd',density=True,stacked=True,histtype='step',label = 'Big Loop 2')
# # plt.hist(a8,bins='fd',density=True,stacked=True,histtype='step',label = 'Small Loops 2')

Hist_Apr(np.array(a5),bins = n_bins, label = 'Big Subloop-P1')
Hist_Apr(np.array(a6),bins = n_bins, label = 'Small Subloops-P1')
Hist_Apr(np.array(a7),bins = n_bins, label = 'Big Subloop-P2')
Hist_Apr(np.array(a8),bins = n_bins, label = 'Small Subloops-P2')

# plt.xlabel('Z-Coordinate of COM',size = 25,fontweight='bold')
# plt.ylabel('Probability',size = 25,fontweight='bold')
plt.xlabel('z/L')
plt.ylabel('P(z/L)')

plt.xticks(fontweight = 'bold', size = 20)
plt.yticks(fontweight = 'bold', size = 20)

# plt.yticks([round(i, 2) for i in plt.yticks()[0]],5)
# plt.xlim((2.3,22.7))
plt.ylim((0,0.22))

# plt.title('COM Organization along z axis')
plt.legend(prop={'size':20,'weight':'bold'})
# # plt.grid()
plt.tight_layout()
plt.savefig('Average_Organization_Arc-2_25.png')
plt.show()

