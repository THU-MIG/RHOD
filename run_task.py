import os
config = 'Partitioned_COI_R50_2x_oid_v6_8GPU.yaml'
# scripts = ['source ../set_conda_script.sh', 'conda activate Detectron2_3', \
#         'python projects/UniDet/train_net.py config-file projects/UniDet/configs/{} num-gpus 8'.format(config)]

os.execl("/bin/bash", "../set_conda_env.sh")

scripts = ['conda activate Detectron2_3']

for script in scripts:
    print(script)
    os.system(script)

