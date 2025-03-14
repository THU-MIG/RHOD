import os
import json




a=json.load(open('annotations-v4-full-path.json'))
a['categories'] = a['categories'][1:]

with open('annotations-v4-full-path-noentity.json', 'w') as f:
    json.dump(a, f)
    
    

a=json.load(open('annotations-expanded-v4-full-path.json'))
a['categories'] = a['categories'][1:]

with open('annotations-expanded-v4-full-path-noentity.json', 'w') as f:
    json.dump(a, f)
    
    

    