from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

i = Image.open('../customImages/test.png')
iar = np.array(i)

print iar
plt.imshow(iar)
plt.show()