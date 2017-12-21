# resize image into desired size maintaining aspect ratio
import cv2
import argparse
import os
# default path to the folder
src_path = os.path.join(os.path.expanduser('~'),
                        'datasets',
                        'flech_loch')

destination_path = os.path.join(os.path.expanduser('~'),
                        'dev',
                        'fabrics',
                        'flech_loch')



def image_resize(image,
                 width = None,
                 height = None,
                 inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized


if __name__ == "__main__":

    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-l", "--src_path", required=True, help = "folder path to the image")

    args = vars(ap.parse_args())

    src_path = args['src_path']
    if not os.path.isdir(destination_path):
        print('Destination path not found.')

    try:
        print(src_path)
        src_files = os.listdir(src_path)
    except:
        print('The specified path does not exist.')

    for f_name in src_files:
        full_path_name = os.path.join(src_path, f_name)
        #print(full_path_name)
        if os.path.isfile(full_path_name):
            img = cv2.imread(full_path_name)
            clone = img.copy()
            roi = image_resize(clone, width=960)
            file_base_name = os.path.basename(f_name)
            img_name = os.path.splitext(file_base_name)[0]
            cv2.imwrite(os.path.join(destination_path, img_name + '.jpg'), roi)

