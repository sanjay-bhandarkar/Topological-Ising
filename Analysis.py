import numpy as np
import matplotlib.pyplot as plt

numb = 0
fig,ax = plt.subplots(figsize = (8,8))
# for i in range(10):
#     numb = numb + 1
#     a1,b1,c1,d1 = np.loadtxt('Big_Loop1_COM_{}.dat'.format(numb),unpack = True)
#     a2,b2,c2,d2 = np.loadtxt('Small_Loops1_COM_{}.dat'.format(numb),unpack = True)
#     a3,b3,c3,d3 = np.loadtxt('Big_Loop2_COM_{}.dat'.format(numb),unpack = True)
#     a4,b4,c4,d4 = np.loadtxt('Small_Loops2_COM_{}.dat'.format(numb),unpack = True)
#     ax = fig.add_subplot(111, projection='3d')

#     # for i in np.arange(1,20000,10):
#     #     norm = np.sqrt((b2[i]-b1[i])**2 + (c2[i]-c1[i])**2 + (d2[i]-d1[i])**2)
#     #     ax.quiver(0, 0, 0, (b2[i]-b1[i])/norm, (c2[i]-c1[i])/norm, (d2[i]-d1[i])/norm, arrow_length_ratio=0.1)

#     for i in np.arange(1,20000,10):
#         norm = np.sqrt((b4[i]-b3[i])**2 + (c4[i]-c3[i])**2 + (d4[i]-d3[i])**2)
#         ax.quiver(0, 0, 0, (b4[i]-b3[i])/norm, (c4[i]-c3[i])/norm, (d4[i]-d3[i])/norm, arrow_length_ratio=0.1)

#     ax.set_xlim([-1, 1])
#     ax.set_ylim([-1, 1])
#     ax.set_zlim([-1, 1])

#     ax.set_xlabel('X',size = 15,fontweight='bold')
#     ax.set_ylabel('Y',size = 15,fontweight='bold')
#     ax.set_zlabel('Z',size = 15,fontweight='bold')

#     plt.title('Vector Plot of Polymer 1',size = 15,fontweight='bold')
#     plt.savefig('Vec2Plot_{}'.format(numb))
    
for i in range(1,41):
    fig,ax = plt.subplots(figsize = (8,8))
    a1,b1,c1,d1 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent27/Exp{}/Big_Loop1_COM.dat'.format(i),unpack = True)
    a2,b2,c2,d2 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent27/Exp{}/Small_Loops1_COM.dat'.format(i),unpack = True)
    a3,b3,c3,d3 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent27/Exp{}/Big_Loop2_COM.dat'.format(i),unpack = True)
    a4,b4,c4,d4 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent27/Exp{}/Small_Loops2_COM.dat'.format(i),unpack = True)
    plt.plot(a1[::10]/100000000,d1[::10]/25.0,label = 'Subloop-1',linewidth = 3)
    plt.plot(a2[::10]/100000000,d2[::10]/25.0,label = 'Subloop-2',linewidth = 3)
    plt.plot(a3[::10]/100000000,d3[::10]/25.0,label = 'Subloop-3',linewidth = 3)
    plt.plot(a4[::10]/100000000,d4[::10]/25.0,label = 'Subloop-4',linewidth = 3)
    plt.xlabel(r'Iterations ($\mathbf{x10^{8}}$)',size = 25,fontweight='bold')
    plt.ylabel('z\L',size = 25,fontweight='bold')
    plt.xticks([0, 0.5, 1, 1.5, 2],size = 20, fontweight = 'bold')
    plt.yticks(size = 20, fontweight = 'bold')
    # plt.title('Organization of Arc0 Polymer',size = 15,fontweight='bold')
    plt.legend(prop = {'size':20},ncol = 2)
    # plt.grid()
    plt.tight_layout()
    plt.savefig('COM_Arc2_iterations_{}.png'.format(i))
    # plt.show()
    plt.close()



# for i in range(41):
#     a1,b1,c1,d1 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent14/Exp{}/Big_Loop1_COM.dat'.format(i),unpack = True)
#     a2,b2,c2,d2 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent14/Exp{}/Small_Loops1_COM.dat'.format(i),unpack = True)
#     a3,b3,c3,d3 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent14/Exp{}/Big_Loop2_COM.dat'.format(i),unpack = True)
#     a4,b4,c4,d4 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent14/Exp{}/Small_Loops2_COM.dat'.format(i),unpack = True)

    

#     plt.hist(d1,bins='fd',density=True,stacked=True,histtype='step',label = 'Big Loop 1')
#     plt.hist(d2,bins='fd',density=True,stacked=True,histtype='step',label = 'Small Loops 1')
#     plt.hist(d3,bins='fd',density=True,stacked=True,histtype='step',label = 'Big Loop 2')
#     plt.hist(d4,bins='fd',density=True,stacked=True,histtype='step',label = 'Small Loops 2')

#     plt.xlabel('Z-Coordinate of COM',size = 15,fontweight='bold')
#     plt.ylabel('Probability',size = 15,fontweight='bold')
#     plt.ylim((0,0.7))
#     plt.title('Organization of Arc2 Polymer',size = 15,fontweight='bold')
#     plt.legend()
#     plt.grid()
#     plt.savefig('COM_Organization_Arc2_{}.png'.format(i))
#     plt.clf()
#     i = i + 1

# big_loop_dist_mean = []
# small_loop_dist_mean = []
# for i in range(1,41):
#     a1,b1,c1,d1 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent13/Exp{}/Big_Loop1_COM.dat'.format(i),unpack = True)
#     a2,b2,c2,d2 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent13/Exp{}/Small_Loops1_COM.dat'.format(i),unpack = True)
#     a3,b3,c3,d3 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent13/Exp{}/Big_Loop2_COM.dat'.format(i),unpack = True)
#     a4,b4,c4,d4 = np.loadtxt('/home/devanshu/Sanjay/MS_Project/Arc2/200/Independent13/Exp{}/Small_Loops2_COM.dat'.format(i),unpack = True)
    
#     i = i + 1

# #    plt.plot(a1,d3-d1,label = 'Mean = {0:2.3f}'.format(np.mean(d3-d1)))
#     big_loop_dist_mean.append(np.mean(d3-d1))
#     small_loop_dist_mean.append(np.mean(d4-d2))
# #    plt.ylim(0,20)
# #    plt.xlabel('Iterations',size = 15,fontweight='bold')
# #    plt.ylabel('Distance between Z-Coordinate of COM',size = 15,fontweight='bold')
# #    plt.title('Distance between Big Loops',size = 15,fontweight='bold')
# #    plt.legend()
# #    plt.grid()
# #    plt.savefig('Dist_Big_Loops_COM_{}.png'.format(numb))
# #    plt.clf()

# print('Arc0 Big_loop Dist Mean = {0:4.3f}'.format(np.mean(big_loop_dist_mean)))
# print('Arc0 Small_loop Dist Mean = {0:4.3f}'.format(np.mean(small_loop_dist_mean)))