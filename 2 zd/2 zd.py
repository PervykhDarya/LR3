#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys


def linux_tail(file=None):
    if file:
        with open(file, 'r') as f:
            for line in (f.readlines()[-10:]):
                print(line, end="")
    else:
        print("Файл не получен для обработки!", file=sys.stderr)


if __name__ == "__main__":
    filename = input("Введите имя файла для обработки: ")
    if os.path.isfile(filename):
        linux_tail(filename)
    else:
        print(f"Файла {filename} не существует", file=sys.stderr)
