from colorization.colorizers import *
import argparse
import os
import matplotlib.pyplot as plt


def image_colorize(path_to_file):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--img_path", type=str, default=path_to_file)
    parser.add_argument("--use_gpu", action="store_true", help="whether to use GPU")
    split_path = path_to_file.split("/")
    colored_dir_path = '/'.join([split_path[0], 'colored_' + split_path[1]])
    if not os.path.exists(colored_dir_path):
        os.mkdir(colored_dir_path)
    parser.add_argument(
        "-o",
        "--save_prefix",
        type=str,
        default='/'.join([split_path[0], 'colored_' + split_path[1], split_path[2]]),
        help="will save into this file with {siggraph17.png} suffix",
    )
    opt = parser.parse_args()
    # load colorizer
    colorizer_siggraph17 = siggraph17(pretrained=True).eval()
    if opt.use_gpu:
        colorizer_siggraph17.cuda()
    # default size to process images is 256x256
    # grab L channel in both original ("orig") and resized ("rs") resolutions
    img = load_img(opt.img_path)
    (tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256, 256))
    if opt.use_gpu:
        tens_l_rs = tens_l_rs.cuda()
    # colorizer outputs 256x256 ab map
    # resize and concatenate to original L channel
    out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())
    plt.imsave("%s" % opt.save_prefix, out_img_siggraph17)
    return opt.save_prefix
