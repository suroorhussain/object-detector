# Import the functions to calculate feature descriptors
from skimage.feature import hog
from skimage.io import imread
from sklearn.externals import joblib
# To read file names
import glob
import os
from config import *

def create_feature_files():
    # If feature directories don't exist, create them
    if not os.path.isdir(pos_feat_path):
        os.makedirs(pos_feat_path)

    # If feature directories don't exist, create them
    if not os.path.isdir(neg_feat_path):
        os.makedirs(neg_feat_path)

    print "Calculating the descriptors for the positive samples and saving them"
    for im_path in glob.glob(os.path.join(pos_im_path, "*")):
        im = imread(im_path, as_grey=True)
        fd = hog(im, orientations, pixels_per_cell, cells_per_block, visualize, normalize)
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(pos_feat_path, fd_name)
        joblib.dump(fd, fd_path)
    print "Positive features saved in {}".format(pos_feat_path)

    print "Calculating the descriptors for the negative samples and saving them"
    for im_path in glob.glob(os.path.join(neg_im_path, "*")):
        im = imread(im_path, as_grey=True)
        fd = hog(im,  orientations, pixels_per_cell, cells_per_block, visualize, normalize)
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(neg_feat_path, fd_name)
        joblib.dump(fd, fd_path)
    print "Negative features saved in {}".format(neg_feat_path)

    print "Completed calculating features from training images"

if __name__ == "__main__":
    create_feature_files()
