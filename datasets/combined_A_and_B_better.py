import cv2 
import os 
import glob
import argparse
import pdb
import numpy as np

def sort_by_index(fname):
    return int(fname.split(".")[0])

def main(args):
    # Assumes dir A and dir B contain same amount and same size images
    img_A_fnames = sorted(os.listdir(args.img_A_dir), key=sort_by_index)
    img_B_fnames = sorted(os.listdir(args.img_B_dir), key=sort_by_index)

    if not os.path.exists(args.img_AB_dir):
        os.makedirs(args.img_AB_dir)
    
    for i, (a_f, b_f) in enumerate(zip(img_A_fnames, img_B_fnames)):
        img_a = cv2.imread(os.path.join(args.img_A_dir, a_f), cv2.IMREAD_COLOR)
        img_b = cv2.imread(os.path.join(args.img_B_dir, b_f), cv2.IMREAD_COLOR)
        img_ab = np.concatenate([img_a, img_b], 1)

        cv2.imwrite(os.path.join(args.img_AB_dir, str(i) + ".jpg"), img_ab)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--img_A_dir", type=str)
    parser.add_argument("--img_B_dir", type=str)
    parser.add_argument("--img_AB_dir", type=str, help="where to save concatenated results")

    args = parser.parse_args()
    main(args)