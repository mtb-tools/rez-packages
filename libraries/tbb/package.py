name = "tbb"

version = "2021.2.0"

authors = [
    "James Reinders",
    "Rafael Asenjo",
    "Michael J. Voss"
]

description = \
    """
    Intel® Threading Building Blocks (Intel® TBB) is a library that
    supports scalable parallel programming using standard ISO C++ code.
    """

build_requires = [
    "cmake"
]

requires = []

@early()
def variants():
    from rez.package_py_utils import expand_requires

    requires = ["platform-**", "arch-**"]  # , "os-**"]
    return [expand_requires(*requires)]


uuid = "libs.tbb"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/TBB")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
