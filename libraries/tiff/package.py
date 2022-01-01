# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building


name = 'tiff'

version = '4.3.0'

authors = ["Sam Leffler", "Silicon Graphics"]

variants = [
    # ["platform-linux"],
    ["platform-osx"],
]

private_build_requires = [
    "jpeg-2+"
]

uuid = 'repository.tiff'


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
