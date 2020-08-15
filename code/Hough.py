import numpy as np
import math
class Hough(object):
    def __init__(self,n_edges,theta_min = -90,theta_max = 90,pix_threshold=10):
        self.thetas = [i for i in range(theta_min, theta_max+1)] # angles
        self.n_edges = n_edges # max n_edges to draw
        self.pix_threshold = pix_threshold # consider pixels whose value is over this
    def vote(self,img):
        self.rmax = int(math.hypot(img.shape[0],img.shape[1])) # the maximum value rho can get.
        self.hough_space = np.zeros((len(self.thetas), 2 * self.rmax + 1)) # This is the hough space that we will vote.

        for x in range(img.shape[1]): # the X and Y coordinates in an image is different thats why x == img.shape[1]
            for y in range(img.shape[0]):
                if img[y, x] > self.pix_threshold:
                    for i, theta in enumerate(self.thetas): # rotate the line
                        th = math.radians(theta)
                        ro = round(x * math.cos(th) + y * math.sin(th)) + self.rmax # we add r_max to get rid of negative values for indexing.
                        if ro <= 2 * self.rmax:
                            self.hough_space[i, ro] += 1 # vote
    def get_lines(self): # This method simply returns top n_edges in the hough space.
        return self.topk(self.hough_space,k=self.n_edges)
    def topk(self,a, k):
        idx = np.argpartition(a.ravel(), a.size - k)[-k:]
        return np.column_stack(np.unravel_index(idx, a.shape))
    def reset(self): # reset if needed
        self.hough_space = np.zeros((len(self.thetas), 2 * self.rmax + 1))
