import os
import subprocess
import argparse
try:
    import yaml
except ImportError as ex:
    print("PyYaml is missing. pip install pyyaml")

__version__ = "0.1.1"
__NAME__ = "Propel-Push"

CWD = os.getcwd()
conf_file = CWD + "/propel.yml"

def run(cmd):
    subprocess.call(cmd.strip(), shell=True)

def git_remotes_conf(f):
    """
    Return the dict of the git-remotes
    :param f: file path
    :return: dict
    """
    with open(f) as yfile:
        conf = yaml.load(yfile)
        return conf["git-remotes"] if "git-remotes" in conf else {}

def gen_git_push_remote(name, force=False):
    force = " -f" if force else ""
    return "git push %s %s master;" % (force, name)

def gen_git_remove_remote(name):
    return "git remote remove %s;" % name

def gen_git_remote_command(name, remotes):
    """
    Generate the push command for a remote
    :param name (str): the remote name
    :param remotes (list): list of  
    :return str: 
    """
    if not isinstance(remotes, list):
        raise TypeError("'remotes' must be of list type")
    
    cmd = gen_git_remove_remote(name)
    cmd += "git remote add %s %s;" % (name, remotes[0])
    if len(remotes) > 1:
        for h in remotes:
            cmd += "git remote set-url %s --push --add %s;" % (name, h)
    return cmd


def cli():
    """
    Main application
    :return:
    """
    try:
        parser = argparse.ArgumentParser(description="%s %s"
                                                     % (__NAME__, __version__))
        parser.add_argument("-r", "--remote",
                            help="To push to a single remote name. "
                                 "ie: [ propel-push -r origin ]")
        parser.add_argument("-a", "--all",
                            help="The push to all the remotes. "
                                 "ie: [ propel-push -a ]",
                            action="store_true")
        parser.add_argument("-l", "--list",
                            help="List remotes in the file. "
                                 "ie: [ propel-push -l ]",
                            action="store_true")
        parser.add_argument("--reset-git-remote",
                            help="Persist the remotes into the git config. "
                                 "ie: [ propel-push --reset ]",
                            action="store_true")
        parser.add_argument("-f", "--force",
                            help="To force the push "
                                 "ie: [ propel-push -a -f ]",
                            action="store_true")
        arg = parser.parse_args()

        print("%s %s" % (__NAME__, __version__))

        force = arg.force
        if arg.all:
            print("Push to all remotes")
            conf = git_remotes_conf(conf_file)
            l = []
            [l.extend(h) for k, h in conf.items()]
            remotes = list(set(l))
            name = "propel_push__all"
            cmd = gen_git_remote_command(name, remotes)
            cmd += gen_git_push_remote(name, force)
            cmd += gen_git_remove_remote(name)
            run("cd %s; %s" % (CWD, cmd))
        
        elif arg.remote:
            name = arg.remote
            print("Push to remote: %s" % name)
            conf = git_remotes_conf(conf_file)
            remotes = conf[name]
            name = "propel_push__%s" % name
            cmd = gen_git_remote_command(name, remotes)
            cmd += gen_git_push_remote(name, force)
            cmd += gen_git_remove_remote(name)
            run("cd %s; %s" % (CWD, cmd))

        elif arg.list:
            print("List Remotes")
            conf_dict = git_remotes_conf(conf_file)
            for k, hosts in conf_dict.items():
                print("%s :" % k)
                print("\n".join([("\t%s" % h) for h in hosts]))

        elif arg.reset_git_remote:
            print("Reset Git Remotes")
            d = git_remotes_conf(conf_file)
            cmd = ""
            for k, values in d.items():
                cmd += gen_git_remote_command(k, values)
            run("cd %s; %s" % (CWD, cmd))

    except Exception as ex:
        print("Exception: %s" % ex.__repr__())

