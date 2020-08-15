from Hough import *
from canny import *
import cv2 as cv
import os
import matplotlib.pyplot as plt

class ExtractLines(object):
    def __init__(self,seg_path,src_path):
        self.Hough = Hough(20)
        self.Canny = CannyMethod()
        self.seg_path = seg_path
        self.src_path =src_path
    def start(self):
        for file in os.listdir(self.src_path):
            orig_image = cv.imread(self.src_path + file)
            seg_image = cv.imread(self.seg_path + file)
            src_gray = cv.cvtColor(orig_image, cv.COLOR_BGR2GRAY)
            img, rgbimg = self.Canny.getEdgeMap(orig_image,src_gray,100)
            self.Hough.vote(img)
            lines = self.Hough.get_lines()
            f = plt.figure(figsize=(20, 10))
            f.add_subplot(1, 4, 1)
            plt.imshow(orig_image, interpolation='nearest')
            plt.axis("off")
            f.add_subplot(1, 4, 2)
            plt.imshow(img, cmap=plt.cm.gray, interpolation='nearest')
            plt.axis("off")
            #plt.savefig(fname="hello.png")
            lined_orig,lined_seg = self.draw_lines(lines,orig_image,seg_image)
            f.add_subplot(1, 4, 3)
            plt.imshow(lined_orig, interpolation='nearest')
            plt.axis("off")
            f.add_subplot(1, 4, 4)
            plt.imshow(lined_seg, interpolation='nearest')
            plt.axis("off")
            plt.show()
            self.Hough.reset()
    def draw_lines(self,lines,orig,seg):
        for line in lines:
            th = math.radians(self.Hough.thetas[line[0]])
            ro = line[1] - self.Hough.rmax # we extract rmax since we added it on the preprocessing phase.
            a = math.cos(th)
            b = math.sin(th)
            x0 = a * ro
            y0 = b * ro
            x1 = int(round(x0 + 1000 * (-b)))
            y1 = int(round(y0 + 1000 * (a)))
            x2 = int(round(x0 - 1000 * (-b)))
            y2 = int(round(y0 - 1000 * (a)))
            cv.line(orig, (x1, y1), (x2, y2), (255, 0, 0), 3, 8)
            cv.line(seg, (x1, y1), (x2, y2), (255, 0, 0), 3, 8)
        return orig,seg





