#!/bin/bash

#SBATCH --account=eecs598s010w23_class
#SBATCH --partition=spgpu
#SBATCH --time=00-04:00:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=4
#SBATCH --mem-per-gpu=47GB

# set up job
module load python/3.9.12 cuda/11.6.2
source env/bin/activate
module load python/3.9.12 cuda/11.6.2


# run job
python train.py --dataroot ./datasets/thick_10x10 --name maze10x10_5000_multiscaleG6_L120_D0_1 --model pix2pix --direction AtoB --netG multiscale

