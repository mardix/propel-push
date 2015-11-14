import os
import subprocess
import argparse
try:
    import yaml
except ImportError as ex:
    print("PyYaml is missing. pip install pyyaml")

__version__ = "0.1.0"
__NAME__ = "GitRemote"

CWD = os.getcwd()
conf_file = CWD + "/gitremote.yml"

def run(cmd):
    subprocess.call(cmd.strip(), shell=True)

conf_file_template = """
#
# GitRemote
# Dict of remote name and host for all remote
#

origin:
  - git@github.com:{REPO-USENAME}/{REPO-NAME}.git

"""

def create_config_file(f):
    if not os.path.isfile(f):
        with open(conf_file, "w+") as f:
            f.write(conf_file_template)

def read_config_file(f):
    with open(f) as yfile:
        return yaml.load(yfile)

def to_git_config(f):
    d = read_config_file(f)
    lines = ""
    if d:
        for k, values in d.items():
            lines += "git remote remove %s;" % k
            lines += "git remote add %s %s;" % (k, values[0])
            if len(values) > 1:
                for h in values:
                    lines += "git remote set-url %s --push --add %s;" % (k, h)
    return lines


def cli():
    """
    Main application
    :return:
    """
    try:
        parser = argparse.ArgumentParser(description="%s %s" % (__NAME__, __version__))
        parser.add_argument("-l", "--list",
                            help="List remotes",
                            action="store_true")
        parser.add_argument("-r", "--reset",
                            help="Reset remotes",
                            action="store_true")
        parser.add_argument("-v", "--verbose",
                            help="List all set remotes",
                            action="store_true")
        parser.add_argument("-i", "--init",
                            help="Git init with gitremote.yml",
                            action="store_true")
        arg = parser.parse_args()

        print("%s %s" % (__NAME__, __version__))

        if arg.init:
            print("Git Init...")
            run("cd %s; git init" % CWD)
            create_config_file(conf_file)

        if arg.list:
            print("List Remotes")
            conf_dict = read_config_file(conf_file)
            for k, hosts in conf_dict.items():
                print("%s :" % k)
                print "\n".join([("\t%s" % h) for h in hosts])

        elif arg.reset:
            print("Reset Remotes")
            s = to_git_config(conf_file)
            run("cd %s; %s" % (CWD, s))

        elif arg.verbose:
            run("cd %s; git remote -v" % CWD)

    except Exception as ex:
        print("Exception: %s" % ex.message)

