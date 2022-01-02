# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "zlib"

version = "1.2.11"

authors = ["Jean-loup Gailly"]


@early()
def variants():
    from rez.package_py_utils import expand_requires

    requires = ["platform-**", "arch-**"]  # , "os-**"]
    return [expand_requires(*requires)]


def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}")
