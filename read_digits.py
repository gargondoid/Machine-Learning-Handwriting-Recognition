#Library for processing images
import imageio
#Library for scaling images
from skimage.transform import resize
#Library for processing the numbers
import numpy as np
#Library to show the images
from matplotlib import pyplot as plt
#Library to get all the images in the folder
import os

import random

path = "./Samples"
files = os.listdir(path)

#Import the images
ims=[]

#Add each file to a list of images
for file in files:
    ims.append(imageio.imread("./Samples/"+file))

#Test show the image
#plt.figure(i+1)
#plt.imshow(im, cmap = plt.get_cmap('gray'))
#plt.show()


def invert(im):
    for i in range(0,len(im[0])):
        for j in range(0,len(im[i])):
            im[i][j]=255-(255*im[i][j])
    return im
         
def crop(im,w,h,sx,sy):
    #Array to hold the cropped image
    cropped=[]
    #Crop the image in the y direction
    im=im[sy:sy+h]
    #Crop the image in the x direction
    for i in im: cropped.append(i[sx:sx+w])
    #Return the cropped image
    return cropped

def resizeNumbers(im):
    im=resize(np.asarray(im, dtype=np.uint8), (28,28))
    return im

#Function to get the numbers from 0-9 in a given image
#im = the image of the numbers 0-9
def getNumbers(im):
    #Variable to hold the images of the numbers 0-9 on the given image
    nums=[]
    
    #im = the image of the numbers 0-9, w = the width of the section, h = the height of the section, sx = the part where the section starts on the x axis, sy = the part where the section starts on the y axis
    
    #Get the number 0
    temp=crop(im, 135, 145, 18, 20)
    temp = resizeNumbers(temp)
    nums.append(invert(temp))    
    
    #Get the number 1
    temp=crop(im, 135, 145, 170, 20)
    temp = resizeNumbers(temp)
    nums.append(invert(temp))
    
    #Get the number 2
    temp=crop(im, 135, 145, 18, 180)
    temp = resizeNumbers(temp)
    nums.append(invert(temp))
    
    #Get the number 3
    temp=crop(im, 135, 145, 170, 180)
    temp = resizeNumbers(temp)
    nums.append(invert(temp))
    
    #Get the number 4
    temp=crop(im, 135, 145, 18, 340)
    temp = resizeNumbers(temp)
    nums.append(invert(temp))
    
    #Get the number 5
    temp=crop(im, 135, 145, 170, 340)
    temp = resizeNumbers(temp)
    nums.append(invert(temp))
    
    #Get the number 6
    temp=crop(im, 135, 145, 18, 500)
    temp = resizeNumbers(temp)
    nums.append(invert(temp))
    
    #Get the number 7
    temp=crop(im, 135, 145, 170, 500)
    temp = resizeNumbers(temp)
    nums.append(invert(temp))
    
    #Get the number 8
    temp=crop(im, 135, 145, 18, 660)
    temp = resizeNumbers(temp)
    nums.append(invert(temp))
    
    #Get the number 9
    temp=crop(im, 135, 145, 170, 660)
    temp = resizeNumbers(temp)
    nums.append(invert(temp))
    
    #Return the numbers 0-9 in the given image
    return nums



def prepareImage(im):
    gotten=getNumbers(im)
    nums=[]
    for i in gotten:
        num=resizeNumbers(gotten[i])
        num=invert(num)
        nums.append(num)
    return nums




def showOneInNum(n):    
    imNum=0
    for im in ims:
        digits = getNumbers(im)
        for i in range(0, 10):
            
            willPrint=random.randint(1,n)
            
            if willPrint==1:
                plt.figure((imNum*10)+(i+1))                
                #Prepare the image
                plt.imshow(digits[i], cmap = plt.get_cmap('gray'))
                #Show the image
                plt.show()
        imNum+=1

#showOneInNum(10)

imNum=0
for im in ims:
#    digits = getNumbers(im)
    for i in range(0, 10):
#        plt.figure((imNum*10)+(i+1))
        #Prepare the image
#        plt.imshow(digits[i], cmap = plt.get_cmap('gray'))
        #Show the image
#        plt.show()
        pass
    imNum+=1
    

def getAllNums():
    allNums=[]
    for im in ims:
        tmp=getNumbers(im)
        for i in tmp:
            allNums.append(i)
    return allNums

def prepareForMnistConvnet():
    #List to hold all of the images
    im_x=[]
    im_y=[]
    #List to hold the images' "values"
    im_y_element=[0,1,2,3,4,5,6,7,8,9]
    
    #List to hold all of the images
    im_x=getAllNums()
    
    for i in range(len(im_x)//10):
        #Add the image's "value" to im_y
        im_y.extend(im_y_element)
    
    #Returns in following format:
    #[im_x, im_y]
    return im_x, im_y

x_train, y_train = prepareForMnistConvnet()

x_train=np.asarray(x_train)
y_train=np.asarray(y_train)


#Index 138 is an amazing 8

#Show all the 8s
#for g in range(231):
#    if str(g)[-1]=="8":
#        plt.figure(g)
#        plt.imshow((x_train[g]), cmap = plt.get_cmap('gray'))
#        plt.show()

#Show all stages of the funny 8 at index 138
#plt.figure(1)
#plt.imshow((crop(ims[11], 135, 145, 18, 340)), cmap = plt.get_cmap('gray'))
#plt.show()

#plt.figure(2)
#plt.imshow((resizeNumbers(crop(ims[11], 135, 145, 18, 340))), cmap = plt.get_cmap('gray'))
#plt.show()

#plt.figure(3)
#plt.imshow((invert(resizeNumbers(crop(ims[11], 135, 145, 18, 340)))), cmap = plt.get_cmap('gray'))
#plt.show()
