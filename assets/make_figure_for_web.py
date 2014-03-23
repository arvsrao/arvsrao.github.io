
# script for making initial space paritioning plot
# for blog post on k-d tree project
#
#


import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

a= = np.array([[ 6.21829 ,  0.779546,  1.82988 ],
       [ 5.23381 ,  4.69416 ,  4.74723 ],
       [ 9.74655 ,  0.191659,  1.20641 ],
       [ 9.7614  ,  9.8382  ,  0.672512],
       [ 2.8546  ,  7.32662 ,  8.51895 ],
       [ 6.50697 ,  2.70078 ,  1.93852 ],
       [ 8.83612 ,  8.70544 ,  2.40537 ]])



head = np.array([6.50689, 1.3663, 3.43026])
left = np.array([0.113181, 2.22785, 3.46726])
right = np.array([8.40924, 4.11543, 8.10499])
 
xhead = head[0]*np.ones((200,))
yhead = np.linspace(0,10, 200, endpoint=True)
  
xleft = np.linspace(0,head[0], 200, endpoint=True)
xright = np.linspace(head[0],10, 200, endpoint=True)

yleft = left[1]*np.ones((200,))
yright = right[1]*np.ones((200,))

fig = plt.figure(); 
ax1 = fig.add_subplot(111); 
ax1.set_xlabel('x'); ax1.set_ylabel('y'); 
ax1.scatter( a[:,0], a[:,1], s=30,c='r'); 
ax1.scatter( head[0], head[1], color='g', s=40,marker='s', label='root node'); 
ax1.scatter(left[0], left[1], s=40, color='b', marker ='^', label='left node'); 
ax1.scatter(right[0], right[1], color='b', s=40,marker='s', label='right node');


plt.plot(xhead, yhead); 
plt.plot(xleft, yleft, color='r'); 
plt.plot(xright, yright, color='r'); 

plt.title('Initial Space Partitioning');
plt.legend();
plt.show()