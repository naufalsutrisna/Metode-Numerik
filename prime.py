# Study Kasus Regresi:
import numpy as np
import matplotlib.pyplot as plt

dataset = np.array([[41,1250],
                   [54,1380],
                   [63,1425],
                   [54,1425],
                  [48,1450],
                  [46,1300],
                  [62,1400],
                  [61,1510],
                  [64,1575],
                  [71,1650]])
print(dataset)

# No X Y
# 1 41 1250
# 2 54 1380
# 3 63 1425
# 4 54 1425
# 5 48 1450
# 6 46 1300
# 7 62 1400
# 8 61 1510
# 9 64 1575
# 10 71 1650

# Solusi dengan Gradient Descent 2D::
alpha=0.00001 #learning rate
[byk_data,dim]=dataset.shape

# inisialisasi b0 dan b1
b0=0.0
b1=0.0

byk_iter=1000;
for j in range(1,byk_iter+1):
  sum_error=0.0
  for i in range(0,byk_data):
    x=dataset[i,0]
    y=dataset[i,1]
    y_topi=b0 + b1*x
    error=(y_topi-y)
    sum_error=sum_error+(error**2)
    # update nilai b0 dan b1
    b0=b0-alpha*error
    b1=b1-alpha*error*x

print()
print('b0 =',b0)
print('b1 =',b1)
print('Y = b0 + b1*X = ', b0,' + ',b1,'*X')

# ploting
plt.title('Regresi Linier:')
plt.xlabel('Ukuran Rumah')
plt.ylabel('Harga Rumah (x 50K)')
#plt.plot(dataset)
plt.scatter(dataset[:,0], dataset[:,1])

# plot garis regresi
x = np.arange(40,80)
y = b0 + b1*x
plt.plot(x, y, color='red')
plt.show()