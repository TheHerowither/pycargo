import json, os


def start_build(path):
    with open(path, "r") as f:
        parsed = json.loads(f.read())
    os.system(f"build {parsed['name']} {os.path.join(os.getcwd(),path)}")