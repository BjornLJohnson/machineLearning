#!/usr/bin/env python


import argparse
 
parser = argparse.ArgumentParser(description='This is a script used to train a variety of neural networks.')
parser.add_argument('-a','--architecture', help = 'Architecture of neural net, ie basic, recursive, convolutional',required=False, default = 'basic')
parser.add_argument('-s', '--set', help = 'Dataset containing training data', required=False, default='catvnoncat')
parser.add_argument('-i','--iterations', help = 'Number of iterations to train over', required=False, default=2500)
parser.add_argument('-r','--rate', help = 'Learning rate of the algorithm', required=False, default=.009)
parser.add_argument('-d','--dims', help = 'Dimensions of hidden and output layers', required=False, default=[20,7,5,1])
parser.add_argument('-v', '--verbose', help = 'Print information including ', required=False, default=False)
parser.add_argument('-n', '--name', help = 'Nickname for the network', required = False, default = "net")
args = parser.parse_args()

a = str(args.architecture)
data = str(args.set)
iter = int(args.iterations)
rate = float(args.rate)
dims = args.dims

if str(a)=="basic":
    from nn_utils import *
    network = train(dataset = data, num_iterations = iter, learning_rate = rate, layer_dims = dims, print_cost = args.verbose)
    save(network, args.name)

elif(a == convolutional):
        print('cnn')