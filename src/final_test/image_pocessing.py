from colorization.colorizers import *
import argparse
import matplotlib.pyplot as plt


def image_colorize(path_to_file):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--img_path", type=str, default=path_to_file)
    parser.add_argument("--use_gpu", action="store_true", help="whether to use GPU")
    parser.add_argument(
        "-o",
        "--save_prefix",
        type=str,
        default=path_to_file.split("/")[
            -2
        ],  # TODO Здесь надо сохранить фотографию в папку соседнюю с оригинальной, но имеющей префикс colored,
        # по запросу файлы из этой папки отправлять пользователю и удалять.
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

    plt.imsave("%s_siggraph17.png" % opt.save_prefix, out_img_siggraph17)
