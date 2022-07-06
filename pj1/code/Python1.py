import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,800)
y = np.linspace(-2,2,600)

x_need = []
y_need = []
iter = 0

max_iter = 40 # 最终迭代次数
for a in x:
    for b in y:
        z = 0
        c = complex(a,b)
        for i in range(max_iter):
            z = z**2+c
            if abs(z)>2:
                break # 不加break会报错：OverflowError: complex exponentiation
        if abs(z)<=2:
            plt.scatter(a,b,s=1,c="r")