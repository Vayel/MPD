# -*- coding: utf-8 -*-
# Python 2
# OpenCV required

# http://www.tech-faq.com/hsv.html

import sys
import numpy as np
import cv2
from cv_functions import loadImg


TB_WIN_LABEL = "Trackbars"

MIN_HUE_TB_LABEL = "min Hue"
MIN_SAT_TB_LABEL = "min Sat"
MIN_VAL_TB_LABEL = "min Val"

MAX_HUE_TB_LABEL = "max Hue"
MAX_SAT_TB_LABEL = "max Sat"
MAX_VAL_TB_LABEL = "max Val"

MIN_HUE_VALUE = 0
MIN_SAT_VALUE = 0
MIN_VAL_VALUE = 0

MAX_HUE_VALUE = 180
MAX_SAT_VALUE = 255
MAX_VAL_VALUE = 255

MIN_GREEN_HUE = 45
MAX_GREEN_HUE = 77
MIN_GREEN_SAT = 19
MAX_GREEN_SAT = 255
MIN_GREEN_VAL = 164
MAX_GREEN_VAL = 255

KERNEL_SIZE_TB_LABEL = "kernel size"
DEFAULT_KERNEL_SIZE = 2
MAX_KERNEL_SIZE = 10

ERODE_ITERATIONS_TB_LABEL = "erode"
DEFAULT_ERODE_ITERATIONS = 2
MAX_ERODE_ITERATIONS = 10

DILATE_ITERATIONS_TB_LABEL = "dilate"
DEFAULT_DILATE_ITERATIONS = 4
MAX_DILATE_ITERATIONS = 10

ESCAPE_KEY = 27

def nothing(x):
  pass

def createTrackbars():
  cv2.namedWindow(TB_WIN_LABEL)
  cv2.createTrackbar(MIN_HUE_TB_LABEL, TB_WIN_LABEL, MIN_GREEN_HUE, MAX_HUE_VALUE, nothing)
  cv2.createTrackbar(MIN_SAT_TB_LABEL, TB_WIN_LABEL, MIN_GREEN_SAT, MAX_SAT_VALUE, nothing)
  cv2.createTrackbar(MIN_VAL_TB_LABEL, TB_WIN_LABEL, MIN_GREEN_VAL, MAX_VAL_VALUE, nothing)
  cv2.createTrackbar(MAX_HUE_TB_LABEL, TB_WIN_LABEL, MAX_GREEN_HUE, MAX_HUE_VALUE, nothing)
  cv2.createTrackbar(MAX_SAT_TB_LABEL, TB_WIN_LABEL, MAX_GREEN_SAT, MAX_SAT_VALUE, nothing)
  cv2.createTrackbar(MAX_VAL_TB_LABEL, TB_WIN_LABEL, MAX_GREEN_VAL, MAX_VAL_VALUE, nothing)
  cv2.createTrackbar(KERNEL_SIZE_TB_LABEL, TB_WIN_LABEL, DEFAULT_KERNEL_SIZE, MAX_KERNEL_SIZE, nothing)
  cv2.createTrackbar(ERODE_ITERATIONS_TB_LABEL, TB_WIN_LABEL, DEFAULT_ERODE_ITERATIONS, MAX_ERODE_ITERATIONS, nothing)
  cv2.createTrackbar(DILATE_ITERATIONS_TB_LABEL, TB_WIN_LABEL, DEFAULT_DILATE_ITERATIONS, MAX_DILATE_ITERATIONS, nothing)

def main(path):
  src = loadImg(path)
  src = cv2.resize(src, (0,0), fx=0.3, fy=0.3)
  gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
  
  createTrackbars()
  cv2.imshow("Source", src)
  print "Press Escape to quit."
  
  while True:
    k = cv2.waitKey(1) & 0xFF
    if k == ESCAPE_KEY:
      break
        
    minHue = cv2.getTrackbarPos(MIN_HUE_TB_LABEL, TB_WIN_LABEL)
    minSat = cv2.getTrackbarPos(MIN_SAT_TB_LABEL, TB_WIN_LABEL)
    minVal = cv2.getTrackbarPos(MIN_VAL_TB_LABEL, TB_WIN_LABEL)
    
    maxHue = cv2.getTrackbarPos(MAX_HUE_TB_LABEL, TB_WIN_LABEL)
    maxSat = cv2.getTrackbarPos(MAX_SAT_TB_LABEL, TB_WIN_LABEL)
    maxVal = cv2.getTrackbarPos(MAX_VAL_TB_LABEL, TB_WIN_LABEL)
    
    kernelSize = cv2.getTrackbarPos(KERNEL_SIZE_TB_LABEL, TB_WIN_LABEL)
    dilateIterations = cv2.getTrackbarPos(DILATE_ITERATIONS_TB_LABEL, TB_WIN_LABEL)
    erodeIterations = cv2.getTrackbarPos(ERODE_ITERATIONS_TB_LABEL, TB_WIN_LABEL)
    
    lower = np.array([minHue, minSat, minVal])
    upper = np.array([maxHue, maxSat, maxVal])
    mask = cv2.inRange(hsv, lower, upper)
    
    kernel = np.ones((kernelSize, kernelSize), np.uint8)
    
    masked = cv2.bitwise_and(gray, gray, mask=mask)
    masked = cv2.threshold(masked, 5, 255, cv2.THRESH_BINARY)[1]
    masked = cv2.erode(masked, kernel, iterations = erodeIterations)
    masked = cv2.dilate(masked, kernel, iterations = dilateIterations)
    
    cv2.imshow("Masked", masked)
    
  
  cv2.destroyAllWindows()

def printUsage():
  print """
  USAGE:
  python hue.py <img-path>
  e.g.: python hue.py --src foo/bar.jpg
  """
  
if __name__ == "__main__":
  if len(sys.argv) > 1:
    main(sys.argv[1])
  else:
    printUsage()
