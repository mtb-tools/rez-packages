name = "expat"

version = "2.4.2"

authors = ["James Clark"]

description = """
    Expat is a stream-oriented XML parser.
    """

build_requires = ["cmake"]

requires = ["python-3.7+", "boost-1.7+", "zlib-1.2+"]


@early()
def variants():
    from rez.package_py_utils import expand_requires

    requires = ["platform-**", "arch-**"]  # , "os-**"]
    return [expand_requires(*requires)]


uuid = "libs.expat"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/{name}-{version}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
