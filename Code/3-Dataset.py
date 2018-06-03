from PIL import Image
import numpy as np

file = open('dataset.txt', 'w')

for i in range(0, 10):
    for j in range(1, 10):

        img = Image.open('../images/numbers/' + str(i) + '.' + str(j) + '.png')
        iar = np.array(img)
        file.write(str(i) + '::' + str(iar.tolist()) + '\n')

file.close()
