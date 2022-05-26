from sprites import generator, get_number_of_rows_and_cols


def sprites_CLI():
    """
    CLI for sprites
    """
    print(
        "Enter in the following order using spaces only:\nnumber_of_sprites, size of the sprite, number_of_colors, "
        "path to save the sprite\nExample:'20 5 2 test.png'\n"
        "NB: if you don't enter path to save the file it will be shown, but not saved"
    )
    inp = input()
    data: list = inp.split(" ")
    try:
        map_size: tuple = get_number_of_rows_and_cols(int(data[0]))
        sprite_size: int = int(data[1])
        number_of_colors: int = int(data[2])
    except IndexError:
        print("Please, enter the data in the prescribed way")
    path: str = ""
    try:
        path = data[3]
    except IndexError:
        pass
    generator(*map_size, sprite_size, number_of_colors, path)


if __name__ == "__main__":
    sprites_CLI()
