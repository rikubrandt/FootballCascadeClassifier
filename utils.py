#!/usr/bin/bash/python3

import os

def generate_negative_desc_file():
    with open("neg.txt", "w") as f:
        for filename in os.listdir('neg'):
            f.write('neg/' + filename + '\n')


# opencv_createsamples -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec

# opencv_traincascade -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 100 -numNeg 100 -numStages 10

# opencv_annotations --annotations=pos.txt --images=pos
