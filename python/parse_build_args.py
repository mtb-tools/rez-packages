import json

with open("./versions.json", "r") as versions:
    POSSIBLE_VERSIONS = json.load(versions)


parser.add_argument('--version', default=POSSIBLE_VERSIONS[0], choices=POSSIBLE_VERSIONS, help='Version to install')
