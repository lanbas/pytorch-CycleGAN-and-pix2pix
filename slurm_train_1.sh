#!/bin/bash

#SBATCH --account=eecs598s010w23_class
#SBATCH --partition=spgpu
#SBATCH --time=00-01:20:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=4
#SBATCH --mem-per-gpu=32GB

# set up job
module load python/3.9.12 cuda/11.6.2
source env/bin/activate
module load python/3.9.12 cuda/11.6.2
# pushd /home/kpyu/great-lakes-tutorial


# run job
python train.py --dataroot ./datasets/facades --name maze5x5_1000_pix2pix_global_D --model pix2pix --direction BtoA 