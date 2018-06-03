import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import Counter
plt.style.use('ggplot')
np.seterr(over='ignore')


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


def what_number(file_path):

    matchedArray = []
    data_set = open('dataset.txt', 'r').read()
    data_set = data_set.split('\n')

    image = np.array(Image.open(file_path))
    #image = threshold(np.array(image))
    image = image.tolist()
    #print image
    for row in image:
        for col in row:
            if len(col)<4:
                col.append(255)
        #print row
    imageInQ = str(image)

    image = imageInQ.split('],')
    #image = str([[[255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255]], [[255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[255, 255, 255, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 255]], [[255, 255, 255, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255]]]).split('],')


    #print imageInQ

    for data in data_set:
        #print data
        dataX = data.split('::')
        #print dataX
        number = dataX[0]
        #print number
        pixels = dataX[1].split('],')
        #print pixels

        x = 0
        while x < len(pixels):
            if image[x] == pixels[x]:
                matchedArray.append(int(number))
            x += 1

    x = Counter(matchedArray)
    print x
    print 'The digit is ', x.most_common()[0][0]
    return x.most_common()[0][0]

accuracy = 0

for i in range(0,9):
    for j in range(1,9):
        image = str(i) + "." + str(j)
        result = what_number('../images/numbers/' + image + '.png')
        if result == i:
            accuracy += 1

print "Accuracy is", float(accuracy/90.0)*100
