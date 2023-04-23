import torch.nn.functional as F
import torch
import cv2
import numpy as np 
import os 
import argparse 
import pdb

# Assumes 256x256
def mask_edges(img):
    cut = 33
    img[:cut] = 0
    img[(256 - cut + 3):] = 0
    img[:, :cut] = 0
    img[:, (256 - cut + 5):] = 0
    # cv2.imwrite('test.png', img)
    return img

def sort_by_res_num(fname):
    return int(fname.split("_")[0])

def main(args):
    # img_mask = cv2.imread('results/img_mask.png')

    if args.out_dir is not None and not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)

    # Proces fnames for loading pairs
    res_fnames = os.listdir(args.res_dir)
    res_fnames = sorted(res_fnames, key=sort_by_res_num)
    res_fnames = set([x.split("_")[0] for x in res_fnames])

    correct = 0
    l1_list = []
    for res_num in res_fnames:
        # Load and mask images
        img_fake = cv2.imread(os.path.join(args.res_dir, res_num + "_fake_B.png"))
        img_real = cv2.imread(os.path.join(args.res_dir, res_num + "_real_B.png"))
        img_fake = mask_edges(img_fake)
        img_real = mask_edges(img_real)

        # Compute l1 loss
        l1 = F.l1_loss(torch.Tensor(img_fake), torch.Tensor(img_real)).item()
        l1_list.append(l1)
        print(l1)
        if l1 < 4.5:
            correct += 1

        # Write results
        if args.write:
            img_out = np.concatenate([img_fake, img_real], axis=1)
            cv2.imwrite(os.path.join(args.out_dir, str(round(l1, 3)) + ".png"), img_out)

    print("Estimated accuracy =", correct / len(res_fnames))
    print("Mean L1 loss =", np.mean(l1_list))
    print("Median L1 loss =", np.median(l1_list))

# > 4.5 seems to be good threshold

if __name__ == "__main__":
    # Assumes res_dir is of the format output by pix2pix test.py 
    parser = argparse.ArgumentParser()
    parser.add_argument('--res_dir', type=str, help='directories containing result images')
    parser.add_argument('--out_dir', type=str, help='second directory')
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()

    main(args)
