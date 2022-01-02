# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building

name = 'jpeg'
version = '2.1.2'
authors = ['D. R. Commander']

@early()
def variants():
    from rez.package_py_utils import expand_requires

    requires = ["platform-**", "arch-**"]  # , "os-**"]
    return [expand_requires(*requires)]

uuid = "repository.jpeg"

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
