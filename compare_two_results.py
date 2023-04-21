import cv2
import numpy as np
import os
import argparse 

def main(args):
    fnames = os.listdir(args.res_dir_A)
    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)

    for fname in fnames:
        fname_pieces = fname.split("_")
        if fname_pieces[1] != 'fake' or fname_pieces[2] != 'B.png':
            continue

        img_a = cv2.imread(os.path.join(args.res_dir_A, fname))
        img_b = cv2.imread(os.path.join(args.res_dir_B, fname))

        img_ab = np.concatenate([img_a, img_b], axis=1)
        cv2.imwrite(os.path.join(args.out_dir, fname), img_ab)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--res_dir_A', type=str, help='first directory')
    parser.add_argument('--res_dir_B', type=str, help='second directory') 
    parser.add_argument('--out_dir', type=str, help='second directory')
    args = parser.parse_args()

    main(args)