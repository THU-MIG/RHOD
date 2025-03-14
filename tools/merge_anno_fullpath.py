import os
import json
import csv


root_path = '../data'
coco_path = os.path.join(root_path, 'coco/annotations/instances_train2017.json')
objects365_path = os.path.join(root_path, 'objects365/annotations/objects365_train.json')
oid_path = os.path.join(root_path, 'oid/annotations/oid_v6_train.json')

print('loading coco')
coco = json.load(open(coco_path))
print('loading objects365')
obj365 = json.load(open(objects365_path))
print('loading oid')
oid = json.load(open(oid_path))
target_path = os.path.join(root_path, 'hmod_train.json')

print('original dataset loaded!')


f = open('./datasets/label_spaces/mapping_converted_v3_no_entity.json')
mappings = json.load(f)['label_map_dict']

mappings_cat_id = {'coco':{}, 'objects365':{}, 'oid':{}}
for i, cat in enumerate(coco['categories']):
    mappings_cat_id['coco'][cat['id']] = mappings['coco'][str(i)] + 1

for i, cat in enumerate(obj365['categories']):
    mappings_cat_id['objects365'][cat['id']] = mappings['objects365'][str(i)] + 1

for i, cat in enumerate(oid['categories']):
    mappings_cat_id['oid'][cat['id']] = mappings['oid'][str(i)] + 1
    
print('mapping constructed!')



hmod_eval_json = json.load(open('./datasets/annotations-v4-full-path-noentity-addarea-strid_attr.json'))
hmod_categories = hmod_eval_json['categories']
del hmod_eval_json

# check img id, add suffix
hmod_imgs = []
for img in coco['images']:
    img['id'] = 'coco_' + str(img['id']) 
    img['file_name'] = os.path.join('coco', 'train2017', img['file_name']) 
    hmod_imgs.append(img)

for img in obj365['images']:
    img['id'] = 'obj365_' + str(img['id']) 
    img['file_name'] = os.path.join('objects365', 'train', img['file_name']) 
    hmod_imgs.append(img)

for img in oid['images']:
    img['id'] = 'oid_' + img['id'] 
    img['file_name'] = os.path.join('oid', 'images', 'train', img['file_name']) 
    hmod_imgs.append(img)


print('img ok!')
    

hmod_annotations = []
obj_id_start_num = 100000000
oid_id_start_num = 200000000
# obj_id_start_num = 1000000000000
# oid_id_start_num = 2000000000000
# coco max id 903800581884, 1892366, obj 2279761, oid 14610228,
for anno in coco['annotations']: 
    anno['image_id'] = 'coco_' + str(anno['image_id'])
    anno['category_id'] = mappings_cat_id['coco'][anno['category_id']]
    hmod_annotations.append(anno)

for anno in obj365['annotations']:
    anno['image_id'] = 'obj365_' + str(anno['image_id'])
    anno['id'] = anno['id'] + obj_id_start_num
    anno['category_id'] =  mappings_cat_id['objects365'][anno['category_id']]
    hmod_annotations.append(anno)

for anno in oid['annotations']:
    anno['image_id'] = 'oid_' + str(anno['image_id'])
    anno['id'] = anno['id'] + oid_id_start_num 
    anno['category_id'] = mappings_cat_id['oid'][anno['category_id']]
    hmod_annotations.append(anno)


print('annotations ok!')

hmod = {'images': hmod_imgs, 'annotations': hmod_annotations, 'categories':hmod_categories}

print('writing to json')
f = open('hmod_train_fullpath.json', 'w')
json.dump(hmod, f)
    
# 1. check duplicate image id       -- coco and obj365 have overlapped image id, add suffix
# 2. map category id
# 3. 

