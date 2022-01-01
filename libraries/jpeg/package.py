# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building

name = 'jpeg'
version = '2.1.2'
authors = ['D. R. Commander']

variants = [
    # ["platform-linux"],
    ["platform-osx"]
    ]

uuid = "repository.jpeg"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
