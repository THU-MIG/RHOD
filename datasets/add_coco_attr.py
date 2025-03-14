import os
import json




a=json.load(open('annotations-v4-full-path-noentity-addarea-strid.json'))

for i in range(len(a['annotations'])):
    a['annotations'][i]['iscrowd'] = int(a['annotations'][i]['IsGroupOf']) 
    a['annotations'][i]['isfake'] = int(a['annotations'][i]['IsFake']) 
#     a['annotations'][i]['isreflected'] = str(a['annotations'][i]['IsFake']) 


with open('annotations-v4-full-path-noentity-addarea-strid-attr.json', 'w') as f:
    json.dump(a, f)
    


a=json.load(open('annotations-expanded-v4-full-path-noentity-addarea-strid.json'))

for i in range(len(a['annotations'])):
    a['annotations'][i]['iscrowd'] = int(a['annotations'][i]['IsGroupOf']) 
    a['annotations'][i]['isfake'] = int(a['annotations'][i]['IsFake']) 
    

with open('annotations-expanded-v4-full-path-noentity-addarea-strid-attr.json', 'w') as f:
    json.dump(a, f)
    
