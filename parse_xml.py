# get the center of the bounding box and
# crop the patch size of crop_size * crop_size
# adjust the new boundning box for each croped image
import os
from xml.dom.minidom import parse
# Open XML document using minidom parser
crop_size = 224
half_crop_size = int(crop_size / 2) # from the center of bounding box
one_third_crop_size = int(crop_size/3)

# file to be written when the hole size is > 170
length = 170
src_file_greater_length = os.path.join(os.path.expanduser('~'),
                        'dev',
                        'fabrics',
                        'data_processing',
                        'larger_bounding_box_file.txt')

def parse_xml_file(source, img_name):

    # Open XML document using minidom parser
    DOMTree = parse(os.path.join(source, img_name + '.xml'))

    collection = DOMTree.documentElement

    # Get all the objects in the collection
    objects = collection.getElementsByTagName("object")

    bnd_boxes = []
    bnd_boxes_crop = []
    # detail of each object.
    for object in objects:
        type = object.getElementsByTagName('name')[0]
        defect = '1'

        xmin = object.getElementsByTagName('xmin')[0]
        xmin = int(xmin.childNodes[0].data)

        ymin = object.getElementsByTagName('ymin')[0]
        ymin = int(ymin.childNodes[0].data)

        xmax = object.getElementsByTagName('xmax')[0]
        xmax = int(xmax.childNodes[0].data)

        ymax = object.getElementsByTagName('ymax')[0]
        ymax = int(ymax.childNodes[0].data)

        height = ymax - ymin
        width  = xmax - xmin

        # check if it exceeds the threshold of the length
        if height <= length or width <= length:

            y_lenth_half = int((height) / 2)
            x_length_half = int((width) / 2)

            # calculate the center of bounding box
            yc = int((ymin + y_lenth_half))
            xc = int((xmin + x_length_half))

            # crop the patch of crop_size *2 on the image from the defects(hole or cuts)
            ymin = yc - half_crop_size
            xmin = xc - half_crop_size

            ymax = yc + half_crop_size
            xmax = xc + half_crop_size

            if xmin < 0 or ymin < 0 or xmax > 960 or ymax > 768:
                print('greater')
            else:
                # generate bounding box co-ordinates for the cropped image
                xmin_bnd_box = half_crop_size - x_length_half
                ymin_bnd_box = half_crop_size - y_lenth_half
                xmax_bnd_box = half_crop_size + x_length_half
                ymax_bnd_box = half_crop_size + y_lenth_half
                if xmin_bnd_box < 0 or ymin_bnd_box < 0 or xmax_bnd_box > 224 or ymax_bnd_box > 224:
                    print(img_name)
                else:
                    # add it to the list
                    bnd_boxes.append([(ymin, ymax), (xmin, xmax)])
                    bnd_boxes_crop.append([xmin_bnd_box, ymin_bnd_box, xmax_bnd_box, ymax_bnd_box, defect])


            # crop the patch of crop_size * 3 on the image from the defects(hole or cuts)
            ymin = yc - 2 * one_third_crop_size
            xmin = xc - 2 * one_third_crop_size

            ymax = yc + one_third_crop_size
            xmax = xc + one_third_crop_size

            if xmin < 0 or ymin < 0 or xmax > 960 or ymax > 768:
                print('greater')
            else:
                # generate bounding box co-ordinates for one third of the cropped image
                xmin_bnd_box = 2*one_third_crop_size - x_length_half
                ymin_bnd_box = 2*one_third_crop_size - y_lenth_half
                xmax_bnd_box = 2*one_third_crop_size + x_length_half
                ymax_bnd_box = 2*one_third_crop_size + y_lenth_half
                if xmin_bnd_box < 0 or ymin_bnd_box < 0 or xmax_bnd_box > 222 or ymax_bnd_box > 222:
                    print(img_name)
                else:
                    # add it to the list
                    bnd_boxes.append([(ymin, ymax), (xmin, xmax)])
                    bnd_boxes_crop.append([xmin_bnd_box, ymin_bnd_box, xmax_bnd_box, ymax_bnd_box, defect])





        else :
            with open(src_file_greater_length, mode='a', encoding='utf-8') as f:
                f.writelines(img_name+'\n')

    return bnd_boxes, bnd_boxes_crop