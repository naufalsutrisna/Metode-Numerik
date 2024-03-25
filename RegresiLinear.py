import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# Definisikan dataset
df = pd.DataFrame([[1, 7.03948302],[2, 11.2347113],[3, 15.3418565],[4, 19.1049999],[5, 23.2723955],
                   [6, 27.4985445],[7, 31.6573844],[8, 35.81462],[9, 39.5455326],[10, 43.4423335]])
df.columns = ['x', 'y']
print(df)

X_train = df['x'].values[:, np.newaxis]
y_train = df['y'].values

# Create & train model
lm = LinearRegression()
lm.fit(X_train, y_train)

# Menampilkan nilai coef & intercept
print('Coeficient: ', lm.coef_)
print('Intercept: ', lm.intercept_)

# Data yang akan diprediksi
X_test = [[4.5]]

# Menampilkan hasil prediksi
p = lm.predict(X_test)
print(p)

# Plot data
pb = lm.predict(X_train)
dfc = pd.DataFrame({'x': df['x'],'y':pb})

# plt.scatter(df['x'],df['y'])
# plt.plot(dfc['x'],dfc['y'],color='red',linewidth=1)
# plt.xlabel('Tinggi dalam cm')
# plt.ylabel('Berat dalam Kg')
# plt.grid()
# plt.show()