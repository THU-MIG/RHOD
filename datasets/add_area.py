import os
import json




a=json.load(open('annotations-v4-full-path-noentity.json'))

for i in range(len(a['annotations'])):
    bbox = a['annotations'][i]['bbox']
    a['annotations'][i]['area'] = bbox[-1] * bbox[-2]


with open('annotations-v4-full-path-noentity-addarea.json', 'w') as f:
    json.dump(a, f)
    


a=json.load(open('annotations-expanded-v4-full-path-noentity.json'))

for i in range(len(a['annotations'])):
    bbox = a['annotations'][i]['bbox']
    a['annotations'][i]['area'] = bbox[-1] * bbox[-2]


with open('annotations-expanded-v4-full-path-noentity-addarea.json', 'w') as f:
    json.dump(a, f)
    
