import platform

name = "openssl"

version = "1.1.1"

authors = [
    "Mark Cox",
    "Ralf Engelschall",
    "Stephen Henson",
    "Ben Laurie",
    "Paul Sutton"
]

description = \
    """
    OpenSSL is a software library for applications that secure
    communications over computer networks against eavesdropping
    or need to identify the party at the other end. It is widely
    used by Internet servers, including the majority of HTTPS
    websites.
    """

build_requires = []

requires = []

@early()
def variants():
    from rez.package_py_utils import expand_requires

    requires = ["platform-**", "arch-**"]  # , "os-**"]
    return [expand_requires(*requires)]

uuid = "libs.openssl"

if platform.system() == "Windows":
    build_requires.append("python-3")
    build_requires.append("winenv-0.0.1")
    build_command = "python {root}/build.py {install}"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.OPENSSL_ROOT_DIR.append("{root}")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
