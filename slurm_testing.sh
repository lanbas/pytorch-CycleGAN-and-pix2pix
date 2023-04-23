#!/bin/bash

#SBATCH --account=eecs598s010w23_class
#SBATCH --partition=gpu
#SBATCH --time=00-00:05:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=20
#SBATCH --mem-per-gpu=90GB

# set up job
module load python/3.9.12 cuda/11.6.2
source env/bin/activate
module load python/3.9.12 cuda/11.6.2
# pushd /home/kpyu/great-lakes-tutorial


# run job
python test.py --dataroot ./datasets/thick_8x8 --name maze8x8_5000_thick_L120_D0_1 --model pix2pix --direction AtoB --epoch 100 --num_test 1000

