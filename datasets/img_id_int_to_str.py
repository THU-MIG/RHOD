import os
import json




a=json.load(open('annotations-v4-full-path-noentity-addarea.json'))

for i in range(len(a['annotations'])):
    a['annotations'][i]['image_id'] = str(a['annotations'][i]['image_id']) 


for i in range(len(a['images'])):
    a['images'][i]['id'] = str(a['images'][i]['id'])

with open('annotations-v4-full-path-noentity-addarea-strid.json', 'w') as f:
    json.dump(a, f)
    


a=json.load(open('annotations-expanded-v4-full-path-noentity-addarea.json'))

for i in range(len(a['annotations'])):
    a['annotations'][i]['image_id'] = str(a['annotations'][i]['image_id']) 

    
for i in range(len(a['images'])):
    a['images'][i]['id'] = str(a['images'][i]['id'])

with open('annotations-expanded-v4-full-path-noentity-addarea-strid.json', 'w') as f:
    json.dump(a, f)
    
