# convert image into the pascal voc format
import os
from xml.dom.minidom import parse
import shutil
# Open XML document using minidom parser

src_annotations = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    'loch',
                                    'merged_latest1',
                                    'annotations')

dst_annotations = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'tf-Faster-RCNN',
                                    'Data',
                                    'full_image_fabrics',
                                    'Annotations')

src_images = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    'loch',
                                    'merged_latest1'
                                     )

dst_images = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'tf-Faster-RCNN',
                                    'Data',
                                    'full_image_fabrics',
                                    'Images')

dst_set_image = dst_train_image = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'tf-Faster-RCNN',
                                    'Data',
                                    'full_image_fabrics',
                                    'Names',
                                    'image_set.txt')

dst_train_image = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'tf-Faster-RCNN',
                                    'Data',
                                    'full_image_fabrics',
                                    'Names',
                                    'train.txt')


dst_test_image = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'tf-Faster-RCNN',
                                    'Data',
                                    'full_image_fabrics',
                                    'Names',
                                    'test.txt')

dst_valid_image = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'tf-Faster-RCNN',
                                    'Data',
                                    'full_image_fabrics',
                                    'Names',
                                    'valid.txt')

def parse_xml_file(source, img_name):
    # check if it has been already processed src_images+ '/' + img_name + '.jpg'

    #print(dst_images + '/' + img_name + '.jpg')
    if not os.path.exists(dst_images + '/' + img_name + '.jpg'):

        if  os.path.exists(src_images + '/' + img_name + '.jpg'):


            # Open XML document using minidom parser
            DOMTree = parse(source)
            collection = DOMTree.documentElement

            # Get all the objects in the collection
            objects = collection.getElementsByTagName("object")

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

                bnd_boxes_label = (str(xmin), str(ymin), str(xmax), str(ymax), defect)

                # write bounding box cordiantes and label to the txt file
                # create file with the same name
                with open(dst_annotations + '/' + img_name + '.txt',
                          mode='a',
                          encoding='utf-8') as f:
                    f.writelines(' '.join(bnd_boxes_label) + '\n')

            shutil.copy(src_images+ '/' + img_name + '.jpg', dst_images)
            with open(dst_set_image, mode='a', encoding='utf-8') as f:
                f.writelines(img_name +'\n')
        else:
            print(img_name)



annotations = os.listdir(src_annotations)
#print(annotations)
for anno in annotations:
    file_name = os.path.join(src_annotations, anno)
    file_base_name = os.path.basename(file_name)
    img_name = os.path.splitext(file_base_name)[0]
    extension = os.path.splitext(file_base_name)[1]

    if os.path.isfile(file_name) and extension == '.xml':
        #print('yes')
        parse_xml_file(file_name, img_name)

# divide into the train , test and validation sets
# from the train sets. 4:1 ratio train:test
with open(dst_set_image) as processed_img_name:
    dst_train_img_list = [line.strip() for line in processed_img_name.readlines()]
    #print(dst_train_img_list)
    total_set = len(dst_train_img_list)
    start_slice = int((len(dst_train_img_list) * 10 )/ 100)
    # print(len(dst_train_img_list))
    end_slice = int((len(dst_train_img_list) * 20) / 100)

    valid_set = dst_train_img_list[0:start_slice]

    test_set = dst_train_img_list[(total_set - end_slice):]
    train_set = dst_train_img_list[start_slice:(total_set - end_slice)]

    open(dst_train_image, 'w').close()

    for train in train_set:
        with open(dst_train_image, mode='a', encoding='utf-8') as f:
            f.writelines(train + '\n')

    open(dst_test_image, 'w').close()
    for test in test_set:
        with open(dst_test_image, mode='a', encoding='utf-8') as f:

            f.writelines(test + '\n')

    open(dst_valid_image, 'w').close()
    for valid in valid_set:
        with open(dst_valid_image, mode='a', encoding='utf-8') as f:
            f.writelines(valid + '\n')

    # print(len(valid_set))
    # print('---')
    # print(len(test_set))
    # print('---')
    # print(len(train_set))
    # print(total_set - end_slice)



