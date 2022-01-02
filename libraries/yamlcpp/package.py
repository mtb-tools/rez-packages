import platform

name = "yamlcpp"

version = "0.7.0"

authors = ["Jesse Beder"]

description = """
    yaml-cpp is a YAML parser and emitter in C++ matching the YAML 1.2 spec.
    """

build_requires = ["cmake"]

requires = ["python-3.7+", "boost-1.7+", "zlib-1.2+"]


@early()
def variants():
    from rez.package_py_utils import expand_requires

    requires = ["platform-**", "arch-**"]  # , "os-**"]
    return [expand_requires(*requires)]


uuid = "libs.yamlcpp"


def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake/yaml-cpp")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
