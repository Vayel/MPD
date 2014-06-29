# -*- coding: utf-8 -*-
# Python 2
# OpenCV required

import sys
import numpy as np
import cv2

def loadImg(path):
  img = cv2.imread(path)
  if img != None:
    return img
  else:
    print "Unable to load " + path + "."
    sys.exit()
