import os
import json




a=json.load(open('annotations-expanded-v4-full-path-noentity-addarea-strid-attr.json'))

hierarchy = json.load(open('label_spaces/hierarchy-v10.json'))



map_super_cat = {}
   
def dfs(root):
    if 'Subcategory' in root.keys() or 'Part' in root.keys():
        children = []
        if 'Subcategory' in root.keys():
            children += root['Subcategory']
        if 'Part' in root.keys():
            children += root['Part']
            
        for child in children:
            map_super_cat[child['LabelName']] = root['LabelName']
            dfs(child)
            
dfs(hierarchy)     


            
for i in range(len(a['categories'])):
    name = a['categories'][i]['name']
    a['categories'][i]['supercategory'] = map_super_cat[name]
    

with open('annotations-expanded-v4-full-path-noentity-addarea-strid-attr-supercat.json', 'w') as f:
    json.dump(a, f)
    
