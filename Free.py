import numpy as np
import matplotlib.pyplot as plt 
 
a5 = []
a6 = []
a7 = []
a8 = []

fig,ax = plt.subplots(figsize = (8,8))
cylinder_length = 21.5

for i in range(1,41):
    a1,b1,c1,d1 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/500/Independent5/Exp{}/Big_Loop1_COM.dat'.format(i),unpack = True)
    a2,b2,c2,d2 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/500/Independent5/Exp{}/Small_Loops1_COM.dat'.format(i),unpack = True)
    a3,b3,c3,d3 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/500/Independent5/Exp{}/Big_Loop2_COM.dat'.format(i),unpack = True)
    a4,b4,c4,d4 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/500/Independent5/Exp{}/Small_Loops2_COM.dat'.format(i),unpack = True)

    for j in range(len(a1)):
        a5.append(abs(d1[j]-d3[j]))
        a6.append(abs(d2[j]-d4[j]))
        # a7.append(d3[j])
        # a8.append(d4[j])

bin_Edges = np.linspace(0,cylinder_length,100)
bin_Edges2 = np.linspace(0,cylinder_length,100)

y1, bin_Edges = np.histogram(a5, bins = 100)
y1 = y1/(40*len(a1))

print(sum(y1),len(y1))
y1 = -np.emath.log(y1)

y2, bin_Edges = np.histogram(a6, bins = 100)
y2 = y2/800040

y2 = -np.emath.log(y2)

plt.xlabel(r'z$_{COM}$',fontweight = 'bold', size = 20)
plt.ylabel(r'F[$X_i$]',fontweight = 'bold', size = 20)
plt.xticks(fontweight = 'bold', size = 20)
plt.yticks(fontweight = 'bold', size = 20)
# plt.title('Free Energy Landscape',size = 20,fontweight = 'bold')
plt.plot(bin_Edges2,y1,'-o',label='Big Loops')
plt.plot(bin_Edges2,y2,'-o',label = 'Small Loops')
# plt.hist(a5,density=True,bins = 'fd', label = 'Big Loops')
# plt.grid()
plt.legend(prop={'size':20,'weight':'bold'})
plt.savefig('Free_Energy_A10_v_500.png')
plt.show()
