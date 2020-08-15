# Line-Detection-Using-Hough-Space
The program can be simply run with ; 
python run.py ./Dataset/Original_Subset/ ./Dataset/Detection_Subset/

The run.py creates an Extraction object that traverses all the images in the given paths. In Extraction object a canny method object and hough transformation object is created. These are the core implementations of this assignment. First the image is read and Canny's method applied on the image and we extract the edge map. And than we applied voting on Hough Space by simply calling the vote function in Hough.py. And than we get the top n edges from the Hough object by calling get_lines. Than we draw these lines on the images and plot it by calling draw_lines function. Note that this is a course assignment, but you can adapt it to your own datasets.
