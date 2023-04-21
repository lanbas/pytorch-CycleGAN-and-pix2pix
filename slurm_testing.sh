#!/bin/bash

#SBATCH --account=eecs598s010w23_class
#SBATCH --partition=spgpu
#SBATCH --time=00-00:00:30
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=4
#SBATCH --mem-per-gpu=32GB

# set up job
module load python/3.9.12 cuda/11.6.2
source env/bin/activate
module load python/3.9.12 cuda/11.6.2
# pushd /home/kpyu/great-lakes-tutorial


# run job
python test.py --dataroot ./datasets/mazes_thick --name maze5x5_5000_thick_multiscaleG_L120_D0_1 --model pix2pix --direction AtoB --epoch 65

