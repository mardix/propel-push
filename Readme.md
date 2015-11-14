#Propel-Push

## About

A [Propel](https://github.com/mardix/propel) extension that allows you to push to 
git remotes specified in `propel.yml`, which is also the config file to deploy with Propel.

## Install

    pip install propel-push
    
## Setup

Add the following in the `propel.yml`

    git-remotes:
      origin:
        - git@github.com:mardix/propel-push.git

Where  `git-remotes` is a dict of dict of remote name and hosts. It can contain
multiple remotes, and each remote contains a dict of hosts.

                
## How to use

Given a config like the one below in the `propel.yml`

    git-remotes:
      origin:
        - git@github.com:mardix/propel-push.git
      production:
        - ssh://user@host:/home/path.git
        - ssh://user@host1:/home/path.git
        - ssh://user@host2:/home/path.git
      staging:
        - ssh://user@host:/home/path.git

### propel-push -r | --remote $name

To push to a remote by name. In this instance `production`

    propel-push -r production 

### propel-push -a | --all

To push to all remotes. `origin`, `production` and `staging` will be used.

    propel-push -a


### propel-push -l

To list remotes that are on the `propel.yml`

    propel-push -l
    
### propel-push --reset-git-remote

To reset the `git remote` to the ones int propel file.   

---

#### Requirements:

    Git

### License:
    
    MIT