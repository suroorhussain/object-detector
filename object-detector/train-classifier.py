# Import the required modules
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
import glob
import os
from config import *

def train_classifier():
    fds = []
    labels = []
    # Load the positive features
    for feat_path in glob.glob(os.path.join(pos_feat_path,"*.feat")):
        fd = joblib.load(feat_path)
        fds.append(fd)
        labels.append(1)

    # Load the negative features
    for feat_path in glob.glob(os.path.join(neg_feat_path,"*.feat")):
        fd = joblib.load(feat_path)
        fds.append(fd)
        labels.append(0)

    clf = LinearSVC()
    print "Training a Linear SVM Classifier"
    clf.fit(fds, labels)
    # If feature directories don't exist, create them
    if not os.path.isdir(os.path.split(model_path)[0]):
        os.makedirs(os.path.split(model_path)[0])
    joblib.dump(clf, model_path)
    print "Classifier saved to {}".format(model_path)
if __name__ == "__main__":
    train_classifier()
