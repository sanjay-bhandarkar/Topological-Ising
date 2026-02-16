import matplotlib.pyplot as plt
import numpy as np

n_runs = 40
n_snapshots = 2000
n_bins = 20

fig,ax = plt.subplots(figsize = (8,8))

dot = np.zeros((n_runs,n_snapshots))
dot2 = []

dot_1 = np.zeros((n_runs,n_snapshots))
dot2_1 = []

dot_2 = np.zeros((n_runs,n_snapshots))
dot2_2 = []

error = np.zeros((n_runs,n_bins))
error_1 = np.zeros((n_runs,n_bins))
error_2 = np.zeros((n_runs,n_bins))


for i in range(n_runs):
# Dumbbell = 26,34,27
    a,b = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent5/Exp{}/DotProd_Arc2.dat'.format(i+1),unpack = True)
    c,d = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent3/Exp{}/DotProd_Arc2.dat'.format(i+1),unpack = True)
    e,f = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent14/Exp{}/DotProd_Arc2.dat'.format(i+1),unpack = True)
    for j in range(len(b)):
        dot[i][j] = b[j]
        dot2.append(b[j])
    for k in range(len(d)):
        dot_1[i][k] = d[k]
        dot2_1.append(d[k])
    for l in range(len(f)):
        dot_2[i][l] = f[l]
        dot2_2.append(f[l])


binEdges2 = np.linspace(-0.95,0.95,20)
# print(binEdges2)

for i in range(n_runs):
    y, binEdges = np.histogram(dot[i], bins = n_bins)
    error[i] = y/2000
    y = 0

for i in range(n_runs):
    y_1, binEdges_1 = np.histogram(dot_1[i], bins = n_bins)
    error_1[i] = y_1/2000
    y_1 = 0

for i in range(n_runs):
    y_2, binEdges_2 = np.histogram(dot_2[i], bins = n_bins)
    error_2[i] = y_2/2000
    y_2 = 0

xticks = np.linspace(-1,1,5)
minor_xticks = np.arange(-1,1,0.1)
averages = np.mean(error,axis = 0)
errors = np.std(error,axis = 0)

averages_1 = np.mean(error_1,axis = 0)
errors_1 = np.std(error_1,axis = 0)

averages_2 = np.mean(error_2,axis = 0)
errors_2 = np.std(error_2,axis = 0)


yticks = np.linspace(0,0.25,6)
minor_yticks = np.arange(0,0.2,0.05)
# plt.bar(binEdges2,averages,yerr = errors,width = 0.1,capsize = 5,label = 'L=25a',fill = True)
#plt.errorbar(binEdges2,averages,yerr = errors,fmt= 'o',capsize = 8,markersize = 10,label = 'L = 15a',color =   'blue')
#plt.errorbar(binEdges2,averages_1,yerr = errors_1,fmt= 'o',capsize = 8,markersize = 10,label = 'L = 20a',color = 'red')
plt.errorbar(binEdges2,averages_2,yerr = errors_2,fmt= 'o',capsize = 8,markersize = 10,label = 'L = 15a')

plt.xlabel(r'cos$(\theta)$',size = 25,fontweight='bold')
plt.ylabel(r'p(cos$\theta$)',size = 25,fontweight='bold')
plt.xticks(xticks,size = 20,fontweight = 'bold')
plt.xticks(minor_xticks,minor = True,size = 20)
plt.yticks(yticks,size = 20,fontweight = 'bold')
plt.yticks(minor_yticks,minor = True,size = 20)
# plt.title(r'cos$\theta$ Distribution with Two Dumbbell Polymers',size = 20,fontweight='bold')
# plt.grid()
plt.legend(prop = {'size':25, 'weight':'bold'})
plt.tight_layout()
plt.savefig('DotProduct_Arc-1-10_Final.png')
plt.show()


# c = np.zeros(40)

# dot_Arc10 = np.zeros((40,2000))
# dot2_Arc10 = []

# error_Arc10 = np.zeros((40,20))
# # fig,ax = plt.subplots(figsize = (6,6))

# for i in range(40):
#     a1,b1 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent4/Exp{}/DotProd_Arc2.dat'.format(i+1),unpack = True)
#     for j in range(len(b1)):
#         dot_Arc10[i][j] = b1[j]
#         dot2_Arc10.append(b1[j])

# for i in range(40):
#     y_Arc10, binEdges_Arc10 = np.histogram(dot_Arc10[i], bins = 20)
#     error_Arc10[i] = y_Arc10/2000
#     y_Arc10 = 0

# averages_Arc10 = np.mean(error_Arc10,axis = 0)
# errors_Arc10 = np.std(error_Arc10,axis = 0)
# plt.bar(binEdges2,averages_Arc10,yerr = errors_Arc10,width = 0.1,fill = True)
# # plt.errorbar(binEdges2,averages_Arc10,yerr = errors_Arc10,fmt= '*',capsize = 2,markersize = 10)

# # plt.xlabel(r'cos$\theta$',size = 15,fontweight='bold')
# # plt.ylabel(r'P(cos$\theta$)',size = 15,fontweight='bold')
# # plt.xticks(xticks)
# # plt.xticks(minor_xticks,minor = True)
# # plt.title('Distribution of Dot Products',size = 15,fontweight='bold')
# # plt.grid()
# plt.savefig('DotProduct_plot1.png')
# plt.show()
