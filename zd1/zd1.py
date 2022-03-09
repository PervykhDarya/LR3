# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.read()
    print(text)
    text = text.split(" ")
    text.reverse()
    print(text)