#!/usr/bin/bash/python3

import os

def generate_negative_desc_file():
    with open("neg.txt", "w") as f:
        for filename in os.listdir('neg'):
            f.write('neg/' + filename + '\n')

