# -*- coding: utf-8 -*-

name = 'png'
version = '1.6.37'
authors = ['Guy Eric Schalnat']

variants = [
    # ["platform-linux"],
    ["platform-osx"],
    ]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
