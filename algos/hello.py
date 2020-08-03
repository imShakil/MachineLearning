"""
Mobarak Hosen Shakil
ICT, Islamic University
Kushtia - 7003, Bangladesh

File: hello.py
Project: MachineLearning
Created: 11:16 AM, 9/18/2019

"""

import pandas
import numpy
import cv2
import keras
import scipy
import matplotlib
import seaborn
import sklearn
import tensorflow


def version():
    return "Pandas Version: {}" \
           "Numpy Version: {}" \
           "Opencv Version: {}" \
           "Keras Version: {}" \
           "Matplotlib Version: {}" \
           "Scipy Version: {}" \
           "Seaborn Version: {}" \
           "Sklearn Version: {}" \
           "Tensorflow Version: {}".format(pandas.__version__,
                                           numpy.__version__,
                                           cv2.getVersionMinor(),
                                           keras.__version__,
                                           matplotlib.__version__,
                                           scipy.__version__,
                                           seaborn.__version__,
                                           sklearn.__version__,
                                           tensorflow.__version__)
