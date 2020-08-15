from __future__ import print_function
import cv2 as cv
class CannyMethod(object):
    def __init__(self,max_lowThreshold=100, ratio=3, kernel_size=3):
        self.max_lowThreshold = max_lowThreshold # hysterisis thresholding
        self.ratio = ratio
        self.kernel_size = kernel_size # gaussian filter size
    def getEdgeMap(self,src,src_gray,threshold):
        low_threshold = threshold
        img_blur = cv.blur(src_gray, (3, 3)) # clear noise
        detected_edges = cv.Canny(img_blur, low_threshold, low_threshold * self.ratio, self.kernel_size) # get edge map
        mask = detected_edges != 0
        dst = src * (mask[:, :, None].astype(src.dtype))
        return detected_edges, dst # return edge_map along with original image
