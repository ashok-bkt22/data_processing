# crop the image based on pre-defined bounding box
import argparse
import cv2
import os
from data_processing import parse_xml


# get the images from the directory
src_loch_bnd_box_img = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    #'data_processing',
                                    'loch',
                                    'done')


dst_loch_bnd_box_crop_img = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    #'data_processing',
                                    'loch',
                                    'done',
                                    'crop')
src_loch_bnd_box_annotation = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    #'data_processing',
                                    'loch',
                                    'done',
                                    'annotation1')
# print(src_loch_bnd_box_annotation)
dst_loch_bnd_box_xml = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    #'data_processing',
                                    'loch',
                                    'done',
                                    'annotation1',
                                    'text')
file_cropped_img = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    'loch',
                                    'done',
                                    'files',
                                    'croped.txt')
file_cropped_img_name = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    'loch',
                                    'done',
                                    'files',
                                    'croped_image_name.txt')
src_bounding_box_larger_than_threshold = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    'loch',
                                     'done',
                                    'files',
                                    'larger_bounding_box_file.txt')

# read the already cropped images first
# if it exists pass it through
with open(file_cropped_img) as f:
    file_already_cropped = [line.strip() for line in f.readlines()]
# print(file_already_cropped)
with open(src_bounding_box_larger_than_threshold) as f:
    bounding_box_larger_than_threshold_list = [line.strip() for line in f.readlines()]
# print(bounding_box_larger_than_threshold_list)

# get the file that has bounding box
img_with_bnd_box = os.listdir(src_loch_bnd_box_annotation)
# print(img_with_bnd_box)
img_bnd_box_name = [os.path.splitext(os.path.basename(img_with_bnd))[0] for img_with_bnd in img_with_bnd_box]
# print(img_bnd_box_name)
# get the images for bounding box
source_files_img = os.listdir(src_loch_bnd_box_img)
for img_name in source_files_img:

    file_name = os.path.join(src_loch_bnd_box_img, img_name)
    file_base_name = os.path.basename(file_name)
    img_name = os.path.splitext(file_base_name)[0]
    
    if img_name  in img_bnd_box_name and img_name not in file_already_cropped and img_name not in bounding_box_larger_than_threshold_list :
        # join source and file name

        if os.path.isfile(file_name):

            img_name_xml = img_name + '.xml'
            #print(img_name_xml)
            # initialize the list of reference points and boolean indicating
            refPt, bnd_box_crop = parse_xml.parse_xml_file(src_loch_bnd_box_annotation, img_name)

            #
            # print(bnd_box_crop)
            # print(refPt)
            # exit()

            if len(refPt) > 0 :
                for i, lines in enumerate(bnd_box_crop):
                    with open(dst_loch_bnd_box_xml + '/' + img_name + '_' + str(i) + '.txt',
                              mode='wt',
                              encoding='utf-8') as f:
                        f.write(' '.join(str(line) for line in lines))
                        # f.write('\n')

                # load the image, clone it
                image = cv2.imread(file_name)
                clone = image.copy()

                if len(refPt) > 0:
                    for i,rfp in enumerate(refPt):
                        roi = clone[refPt[i][0][0]:refPt[i][0][1],refPt[i][1][0]:refPt[i][1][1]]
                        # Crop from x, y, w, h -> 100, 200, 300, 400
                        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
                        print(os.path.join(dst_loch_bnd_box_crop_img, img_name + '_' + str(i) + '.jpg'))

                        cv2.imwrite(os.path.join(dst_loch_bnd_box_crop_img, img_name + '_' + str(i)+'.jpg'), roi)
                        with open(file_cropped_img, mode='a', encoding='utf-8') as f:
                            f.writelines(img_name+'\n')

                        with open(file_cropped_img_name, mode='a', encoding='utf-8') as f:
                            f.writelines(img_name + '_' + str(i) + '\n')



