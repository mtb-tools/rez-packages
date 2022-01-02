from rez.utils.lint_helper import this, env

name = "python"


@early()
def version():
    import json
    import argparse

    with open("./versions.json", "r") as versions:
        POSSIBLE_VERSIONS = json.load(versions)
    parser = argparse.ArgumentParser(description="catch version argument")

    parser.add_argument(
        "--version",
        default=POSSIBLE_VERSIONS[0],
        choices=POSSIBLE_VERSIONS,
        help="Version to install",
    )

    args, unknown = parser.parse_known_args()
    return args.version


authors = ["Guido van Rossum"]

description = """
    The Python programming language.
    """

requires = [
    "zlib-1.2.11",
    "openssl-1+"
]
private_build_requires = [
    "gcc",
    "cmake-3",
]


@early()
def pyver():
    maj, mnr = this.version.split(".")[:2]
    return ".".join([maj, mnr])
    # pylibvers = {'2.7': '2.7', '3.6': '3.6m', '3.7': '3.7m', '3.8': '3.8', '3.9':'3.9'}
    # return pylibvers[
    #     ".".join(str(version).split(".")[0:2])
    # ]
    # # [str(i) for i in [this.version.major, this.version.minor]])]


@early()
def variants():
    from rez.package_py_utils import expand_requires

    requires = ["platform-**", "arch-**"]  # , "os-**"]
    return [expand_requires(*requires)]


@early()
def tools():
    # conditionally enumerate python 2 / 3 tools
    maj, mnr = this.version.split(".")[:2]
    pyver = ".".join([maj, mnr])
    all_vers = ["python{0}", "python{0}-config", "pydoc{0}", "pip{0}"]
    py2_only = ["smtpd.py"]
    py3_only = ["pyenv", "idle3"]
    tools = py2_only if int(maj) < 3 else py3_only + ["idle"]
    variants = ["", maj, pyver]
    for tool in all_vers:
        for variant in variants:
            tools.append(tool.format(variant))
    return tools + ["2to3", "idle"]


@early()
def uuid():
    import uuid

    return str(uuid.uuid5(uuid.NAMESPACE_DNS, name))


def pre_build_commands():
    # pyver = ".".join([str(i) for i in [this.version.major, this.version.minor, this.version.patch]])
    pyver = str(this.version)
    url = "http://www.python.org/ftp/python/%s/Python-%s.tgz" % (pyver, pyver)
    env.CFLAGS = " ".join(
        [
            "-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2",
            "-fexceptions -fstack-protector-strong",
            "--param=ssp-buffer-size=4 -grecord-gcc-switches",
            "-m64 -mtune=generic -D_GNU_SOURCE",
            "-fPIC -fwrapv $CFLAGS",
        ]
    )
    env.LDFLAGS = "-Wl,-rpath,$REZ_BUILD_INSTALL_PATH/lib $LDFLAGS"
    config_opt = " ".join(
        [
            "--prefix=$REZ_BUILD_INSTALL_PATH",
            "--enable-ipv6",
            "--enable-shared",
            "--enable-unicode=ucs4",
            "--with-dbmliborder=gdbm:ndbm:bdb",
            "--with-system-expat",
            "--with-system-ffi",
            "--with-ensurepip",
            "--with-computed-gotos=yes",
            "--enable-optimizations",
            # "--enable-loadable-sqlite-extensions",
            # "--with-dtrace",
            # "--with-valgrind",
            # "--build=x86-64-redhat-linux-gnu ",
            # "--host=x86_64-redhat-linux-gnu ",
            # "--without-ensurepip ",
            # "--enable-universalsdk",
        ]
    )
    prefix = "$REZ_BUILD_INSTALL_PATH"
    config_cmd = "./configure %s" % config_opt
    link_cmd_cfg = "ln -sfv python%s-config %s/bin/python-config" % (
        pyver.split(".")[0],
        prefix,
    )
    download_cmd = "wget %s" % url

    def link_cmd(exe):
        return (
            "ln -sfv {0}%s %s/bin/{0}".format(exe)
            % (pyver.split(".")[0], prefix)
            if int(pyver.split(".")[0]) > 2
            else ""
        )

    env.REZ_BUILD_DOWNLOAD_CMD = download_cmd
    env.REZ_BUILD_UNPACK_CMD = "tar -xvf Python*.tgz --strip 1"

    env.REZ_BUILD_CONFIGURE_CMD = config_cmd
    env.REZ_BUILD_MAKE_CMD = "make install -j$REZ_BUILD_THREAD_COUNT VERBOSE=1"
    env.REZ_BUILD_LINK_CMD_0 = link_cmd("python")
    env.REZ_BUILD_LINK_CMD_1 = link_cmd("idle")
    env.REZ_BUILD_LINK_CMD_2 = link_cmd("pydoc")
    env.REZ_BUILD_LINK_CMD_3 = link_cmd("pip")
    env.REZ_BUILD_LINK_CMD_4 = link_cmd_cfg


build_command = """
$REZ_BUILD_DOWNLOAD_CMD
$REZ_BUILD_UNPACK_CMD
$REZ_BUILD_CONFIGURE_CMD
$REZ_BUILD_MAKE_CMD
$REZ_BUILD_LINK_CMD_0
$REZ_BUILD_LINK_CMD_1
$REZ_BUILD_LINK_CMD_2
$REZ_BUILD_LINK_CMD_3
#mkdir $REZ_BUILD_INSTALL_PATH/cmake
#cp {root}/python.cmake $REZ_BUILD_INSTALL_PATH/cmake
"""


def pre_commands():
    env.PYTHONHOME.unset()


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if system.platform in ["osx"]:
        env.DYLD_LIBRARY_PATH.prepend("{root}/lib")
        py_config = "config-%s-%s" % (this.pyver, "darwin")
        py_lib = "{root}/lib/lib%s.dylib" % this.pyver

    elif system.platform in ["linux"]:
        py_config = "config-%s-%s" % (this.pyver, "x86_64-linux-gnu")
        py_lib = "{root}/lib/lib%s.so.1.0" % this.pyver

    else:
        if building:  # todo: support windows
            echo(
                "python rez package - unsupported platform: %s"
                % system.platform
            )
            py_lib = None
            py_config = None

    if building:
        maj_min = ".".join(
            [str(i) for i in [this.version.major, this.version.minor]]
        )
        env.PYTHONUSERBASE = "$REZ_BUILD_INSTALL_PATH"
        env.PYTHON_INCLUDE_DIRS = "{root}/include/python%s" % this.pyver
        env.PYTHON_EXECUTABLE = "{root}/bin/python%s" % this.pyver
        env.PYTHONEXECUTABLE = "{root}/bin/python%s" % this.pyver
        env.CMAKE_MODULE_PATH.prepend("{root}/cmake")
        env.PKG_CONFIG_PATH.prepend("{root}/include/pkgconfig")
        env.LDFLAGS = "-L{root}/lib -Wl,-rpath,{root}/lib $LDFLAGS"
        env.CFLAGS = "-I{root}/include/python%s $CFLAGS" % this.pyver
        env.CXXFLAGS = "-I{root}/include/python%s $CXXFLAGS" % this.pyver
        env.CPPFLAGS = "-I{root}/include/python%s $CPPFLAGS" % this.pyver
        if py_lib:
            env.PYTHON_LIBRARY = py_lib
            env.PYTHON_LIBRARIES = "{root}/lib/python%s/%s/libpython%s.a" % (
                maj_min,
                py_config,
                this.pyver,
            )
