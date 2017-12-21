# move images which already have bounding box generated
import os
import cv2
import shutil
src_loch_img = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    'annotation_flech_loch',
                                    'flech_loch')


src_loch_annotation = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    'annotation_flech_loch',
                                    'annotations')

dst_loch_img = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    'loch',
                                    'done5_flech_loch')

img_annotation_list = os.listdir(src_loch_annotation)

img_annotation = []
for img in img_annotation_list:
    file_base_name = os.path.basename(img)
    img_annotation.append(os.path.splitext(file_base_name)[0])


bnd_box_generated_img = os.listdir(src_loch_img)
bnd_img = []
for img in bnd_box_generated_img:
    file_base_name = os.path.basename(img)
    bnd_img.append(os.path.splitext(file_base_name)[0])



difference_img = list(set(bnd_img) - set(img_annotation))
# print(len(difference_img))
# print(len(bnd_box_generated_img))
for img in bnd_img:
    if img not in difference_img:
        file_name = src_loch_img + '/' +img + '.jpg'
        shutil.move(file_name, dst_loch_img)




