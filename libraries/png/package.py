# -*- coding: utf-8 -*-

name = 'png'
version = '1.6.37'
authors = ['Guy Eric Schalnat']

@early()
def variants():
    from rez.package_py_utils import expand_requires

    requires = ["platform-**", "arch-**"]  # , "os-**"]
    return [expand_requires(*requires)]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
