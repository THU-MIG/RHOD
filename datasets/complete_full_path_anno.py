import os
import json




def get_ob365_all_paths(path='objects365/annotations/objects365_val.json'):
    ob_anno = json.load(open(path))
    ob_images = ob_anno['images']
    path_map = {}
    for img in ob_images:
        file_name = img['file_name']
        img_name = file_name.split('/')[-1]
        path_map[img_name] = os.path.join('objects365', 'val', file_name)
    
    return path_map

        
        

def process(json_file, ob_path_map):
    
    anno = json.load(open(json_file))
    images = anno['images']
    for i, img in enumerate(images):
        if 'object' in img['file_name']:
            anno['images'][i]['file_name'] = ob_path_map[img['file_name']]
        else:
            anno['images'][i]['file_name'] = os.path.join('oid', 'images', 'validation', img['file_name'])
    
    json_file_new = json_file.split('.')[0] + '-full-path.json'
    with open(json_file_new, 'w') as f:
        json.dump(anno, f)
        

        
a = get_ob365_all_paths()
# process('annotations-v4.json', a)
process('annotations-expanded-v4.json', a)
    
    
    