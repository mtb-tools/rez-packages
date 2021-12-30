from rez.utils.lint_helper import env

name = "arnold"
authors = ["Autodesk"]
description = "advanced Monte Carlo ray tracing renderer"
uuid = "repository.arnold"

tools = ["kick", "oslc", "oslinfo", "maketx"]

build_command = "bash {root}/../common/install.sh"


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
