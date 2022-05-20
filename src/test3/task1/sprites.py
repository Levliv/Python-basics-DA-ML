import matplotlib.pyplot as plt
import copy
from random import randint
from math import sqrt, floor


def get_number_of_rows_and_cols(number_of_sprites: int) -> tuple:
    """
    Getting number of rows of columns by total number of sprites.
    All rows must be filled. Number of rows always less than number of columns.
    """
    s_root: int = floor(sqrt(number_of_sprites))
    while s_root > 1:
        if number_of_sprites % s_root == 0:
            break
        s_root -= 1
    return s_root, number_of_sprites // s_root


def create_line(length: int, number_of_colors: int) -> list:
    """
    Generates symmetrical data line using passed number of colors.
    """
    line_raw = [randint(0, number_of_colors - 1) for _ in range(length // 2)]
    line = copy.deepcopy(line_raw)
    if length % 2:
        line.append(randint(0, 1))
    line.extend(list(reversed(line_raw)))
    return line


def generator(rows: int, columns: int, sprite_size: int = 5, number_of_colors: int = 2, save_path: str = ""):
    """
    Creates map of symmetrical sprites.
    If path was not passed, doesn't save the picture.
    """
    fig, axes = plt.subplots(nrows=rows, ncols=columns)
    for ax in axes.flat:
        data = [create_line(sprite_size, number_of_colors) for _ in range(sprite_size)]
        ax.imshow(data)
        ax.axis("off")
    plt.axis("off")
    if len(save_path):
        fig.savefig(save_path)
    else:
        plt.show()
