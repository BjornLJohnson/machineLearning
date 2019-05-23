#!/usr/bin/env python

import sys
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from nn_utils import load, predict
import argparse

parser = argparse.ArgumentParser(description='This is a script used to make a prediction for the content of an image.')
parser.add_argument('-n', '--name', help = 'Name of the network to use', required = True)
parser.add_argument('-i', '--image', help = 'Path to image file', required = True)
parser.add_argument('-l', '--label', help = 'Ground truth label for image', required = True)
args = parser.parse_args()

network = load(args.name)

#print(network)

parameters = network['params']
num_px =  network['image_size']
classes = network['classes']

image_orig = args.image # change this to the name of your image file 
y_label = [args.label] # the true class of your image (1 -> cat, 0 -> non-cat)

image = np.array(ndimage.imread(image_orig, flatten=False))
image_vec = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((num_px*num_px*3,1))
image_vec = image_vec/255.
prediction = predict(image_vec, y_label, parameters)

print ("y = " + str(np.squeeze(y_label)) + ", your L-layer model predicts a \"" + classes[int(np.squeeze(prediction)),].decode("utf-8") +  "\" picture.")

plt.imshow(image)
plt.show()