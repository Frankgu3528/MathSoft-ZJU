import numpy as np
import matplotlib.pyplot as plt
# 需要用到上面两个包，c 的值从倒数第六行输入。
def julia(x, y, c, k):
    x, y = np.meshgrid(x, y)
    z = x + y * 1j
    count = np.zeros(z.shape)
    for i in range(k):
        z = z**4 + c
        count[np.abs(z) < 2] += 1
    return count

x = np.linspace(-2, 2, 2000)
y = np.linspace(-2, 2, 2000)
c = 0.273+0.7j # 这就是一开始的c
plt.figure().add_subplot(111).imshow(julia(x, y, c, 100),cmap="turbo")
# plt.title("Julia set with $c = {0}+{1}i$".format(c.real,c.imag))
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)
plt.show()
