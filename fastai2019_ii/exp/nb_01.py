
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/01_matmul.ipynb
from exp.nb_00 import *
import operator

def test(a,b,cmp,cname=None):
    if cname is None: cname=cmp.__name__
    assert cmp(a,b),f"{cname}:\n{a}\n{b}"

def test_eq(a,b): test(a,b,operator.eq,'==')



from pathlib import Path
from IPython.core.debugger import set_trace
import pickle, gzip, math, torch, matplotlib as mpl
import matplotlib.pyplot as plt
from torch import FloatTensor as tensor

MNIST_URL='https://github.com/mnielsen/neural-networks-and-deep-learning/blob/master/data/mnist.pkl.gz'



def shape_mnist(x): return x.view(x.shape[0],x.shape[1]*x.shape[2])

import pandas as pd
def get_minst():
    import mnist
    mnist.temporary_dir = lambda: 'mnist-data'
    def normalize(x, m, s): return (x-m)/s

    x_train, y_train = mnist.train_images(),mnist.train_labels()
    train_mean,train_std = x_train.mean(),x_train.std()
    x_train = normalize(x_train, train_mean, train_std)
    # NB: Use training, not validation mean for validation set
    x_test, y_test = mnist.test_images(),mnist.test_labels()
    x_test = normalize(x_test, train_mean, train_std)
    x_train, x_test = map(torch.FloatTensor,(x_train, x_test))
    y_train, y_test = map(torch.LongTensor,(y_train, y_test))
    return shape_mnist(x_train), y_train,shape_mnist(x_test), y_test

def near(a,b): return torch.allclose(a, b, rtol=1e-3, atol=1e-5)
def test_near(a,b): test(a,b,near)