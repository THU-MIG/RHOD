source ../set_conda_script.sh
conda activate Detectron2_3
sudo apt-get update 
sudo apt install libgl1-mesa-glx -y --force-yes
python projects/UniDet/train_net.py --config-file projects/UniDet/configs/Unified_learned_OCI_R50_6x_oid_v6_8GPU_4worker.yaml --num-gpus 8
