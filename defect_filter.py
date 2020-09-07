import sys
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import gaussian
from scipy.ndimage import gaussian_laplace
from skimage.io import imread

def highlight_defects(image_path, sigmas=[2,4,5]):
    """ Find defects in the image """
    img = imread(image_path) / 255.
    h, w = img.shape

    fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True, figsize=(10, 10))
    ax = axes.ravel()

    ax[0].imshow(img, cmap=plt.cm.gray)
    ax[0].set_title('Original Image')

    # gaussian laplace and zero crossing
    idx = 1
    for sigma in sigmas:
        res = gaussian_laplace(img, sigma=sigma)
        res[res > 0] = 1
        ax[idx].imshow(res, cmap=plt.cm.gray)
        ax[idx].set_title('Result with sigma %d' % sigma)
        idx = idx + 1

    # plot images
    fig.tight_layout()
    plt.show()

# Make sure code is executed directly from the shell
if __name__ == '__main__':

    # check number of argument passed to the program
    if len(sys.argv) < 2:
        # if less than 2, then it is incorrect.
        # print help and exit
        print('Usage:\n\tpython %s <image_path>' % sys.argv[0])
        exit(0)

    # get image path from program arguments
    image_path = sys.argv[1]

    # apply various filters
    highlight_defects(image_path)
