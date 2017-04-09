import scipy.misc
import matplotlib.pyplot as plt
lena = scipy.misc.face()
plt.gray()
plt.imshow(lena)
plt.colorbar()
plt.show()
