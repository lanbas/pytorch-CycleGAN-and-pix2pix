import cv2
import numpy as np
import os
import argparse 

def main(args):
    fnames = os.listdir(args.res_dirs[0])
    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)

    if len(args.res_dirs) < 2:
        print("Requires more than two result directories for comparison")
        exit(1)

    for fname in fnames:
        fname_pieces = fname.split("_")
        if fname_pieces[1] != 'fake' or fname_pieces[2] != 'B.png':
            continue

        imgs = []
        for res_dir in args.res_dirs:
            img = cv2.imread(os.path.join(res_dir, fname))
            imgs.append(img.copy())

        img_out = np.concatenate(imgs, axis=1)
        cv2.imwrite(os.path.join(args.out_dir, fname), img_out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--res_dirs', nargs='+', type=str, help='directories containing result images')
    parser.add_argument('--out_dir', type=str, help='second directory')
    args = parser.parse_args()

    main(args)