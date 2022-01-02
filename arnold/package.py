# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env
import argparse
import json

name = "arnold"
authors = ["Autodesk"]
description = "advanced Monte Carlo ray tracing renderer"
uuid = "repository.arnold"

tools = ["kick", "oslc", "oslinfo", "maketx"]

build_command = "bash {root}/install.sh"

@early()
def version():
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


def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
    env.solidangle_LICENSE = "5053@localhost"
