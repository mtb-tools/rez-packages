name = "boost"

version = "1.73.0"

authors = [
    "Boost community"
]

description = \
    """
    Boost is a set of libraries for the C++ programming language
    that provides support for tasks and structures such as linear
    algebra, pseudorandom number generation, multithreading,
    image processing, regular expressions, and unit testing.
    """

build_requires = [

]

requires = [
    # "python-3.7.10"
    "python-3.7+"
]


@early()
def variants():
    from rez.package_py_utils import expand_requires

    requires = ["platform-**", "arch-**"]  # , "os-**"]
    return [expand_requires(*requires)]

uuid = "libs.boost"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
