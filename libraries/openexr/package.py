# -*- coding: utf-8 -*-

name = "openexr"
version = "3.1.3"

description = \
"""
The professional-grade image storage format of the motion picture industry
"""

authors = [
    "Academy Software Foundation"
]

@early()
def variants():
    from rez.package_py_utils import expand_requires

    requires = ["platform-**", "arch-**"]  # , "os-**"]
    return [expand_requires(*requires)]

uuid = "repository.%s" % name


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/lib/cmake")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
