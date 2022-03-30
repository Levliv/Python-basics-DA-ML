import pytest
from os import rmdir, listdir, remove
from src.hw3.image_downloader import downloader


def test_simple():
    directory_name = downloader(4)
    print(directory_name)
    assert len(listdir(directory_name)) == 4
    for file in listdir(directory_name):
        remove(f"{directory_name}/{file}")
    rmdir(directory_name)
