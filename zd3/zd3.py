# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import os


if __name__ == "__main__":
    os.rename("April.png", "March.png")
    os.rename("April(1).png", "April.png")
    os.remove("February.png")
    path = os.getcwd()
    print(path)