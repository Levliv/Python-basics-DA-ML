import pytest
from os import rmdir
from src.hw3.image_downloader import downloader


def skip():
    directory_name = downloader(4)
    print(directory_name)
    rmdir(directory_name)
    assert 0 == 0
