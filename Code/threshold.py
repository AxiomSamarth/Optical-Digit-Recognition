from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def threshold(imageArray):
    balanceArray = []
    newImage = imageArray

    for eachrow in imageArray:
        for eachpix in eachrow:
            average = reduce(lambda x,y: x+y, eachpix[:3])/(len(eachpix[:3]))
            balanceArray.append(average)
    balance = reduce(lambda x,y: x+y, balanceArray)/len(balanceArray)

    for eachrow in newImage:
        for eachpix in eachrow:
            if reduce(lambda x,y: x+y, eachpix[:3])/len(eachpix[:3]) > balance:
                eachpix[0] = 255
                eachpix[1] = 255
                eachpix[2] = 255
                try:
                    eachpix[3] = 255
                except Exception as e:
                    pass

            else:
                eachpix[0] = 0
                eachpix[1] = 0
                eachpix[2] = 0
                try:
                    eachpix[3] = 255
                except Exception as e:
                    pass

    return newImage
'''
i = Image.open('../images/numbers/0.1.png')
iar = np.array(i)
iar1 = threshold(iar)
plt.imshow(iar1)
plt.show()

i1 = Image.open('../images/numbers/y0.3.png')
iar2 = np.array(i1)
plt.imshow(iar2)
plt.show()

iar2 = threshold(iar2)
plt.imshow(iar2)
plt.show()
'''

i1 = Image.open('../images/numbers/0.1.png')
i2 = Image.open('../images/numbers/y0.3.png')
i3 = Image.open('../images/numbers/y0.4.png')
i4 = Image.open('../customImages/test.png')

iar1 = threshold(np.array(i1))
iar2 = threshold(np.array(i2))
iar3 = threshold(np.array(i3))
iar4 = threshold(np.array(i4))

fig = plt.figure()
ax1 = plt.subplot2grid((8,8),(4,4),rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,8),(4,0),rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,8),(0,4),rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,8),(0,0),rowspan=4, colspan=3)

ax1.imshow(iar1)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)
plt.show()