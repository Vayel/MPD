# -*- coding: utf-8 -*-
# Python 2
# OpenCV required

import os
import sys
import numpy as np
import cv2
from cv_functions import loadImg
from global_functions import ensureDir

def main(path):
  src = loadImg(path)
  gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  thresh = cv2.threshold(gray, 127, 255, 0)[1]
  
  contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  cv2.drawContours(src, contours, -1, (255,0,0), 2)
  cv2.imshow("Contours", src)
  print str(len(contours)) + " contours."
  
  cv2.waitKey()
  cv2.destroyAllWindows()


def printUsage():
  print """
  USAGE:
  python contours.py <img-path>
  e.g.: python contours.py bar/foo.jpg
  """
  
    
if __name__ == "__main__":
  if len(sys.argv) > 1:
    src = sys.argv[1]
    main(src)
  else:
    printUsage()
