# Copyright 2015 Sun Jingyun
#
# Python version: 2.7.8
#
# An GIT post-commit hook for posting to Lesschat. Using it with following steps.
#  
# Step 1:
#       Setup the channel and integration first, then get the url for the new service of GIT.
# Step 2:
#       rename the post-receive.sample (under the [git repository folder]\.git\hooks) with the new name as it say.
#       add your code to excute the git.py
#       NOTE: 1. The names of hooks are different in the different version of git, please use the most similar one if there isn't post-receive.sample
#             2. Please give the executable permissions to the post-receive and the git.py
#             3. When you excute git.py in post-receive, please use the full path of git_34.py, because git run the hooks in others path.
# Step 3: 
#       replace the specail url with the one come from Lesschat.
# Step 4:
#       try to commit something and check your channel.


# POST https://hook.lesschat.com/git/xxxxxxxxxxxxxxxx
# Content-Type: application/json
# Body: {"payload": {"committer": "xxxx", "sha_id": "xxxx", "log": "xxxx", "repo_name": "xxxx"}}

import sys
import os
import urllib
import urllib2
import json

def get_content():
        repo_name = get_repo_name()
        committer = get_committer()
        log = get_log()
        sha_id = get_id()
        content = {'repo_name': repo_name, 'committer': committer, 'log': log, 'sha_id': sha_id}
        return content
def get_repo_name():
# the repository name 
        return "xxxx"
def get_committer():
        cmd = 'git log --pretty=format:"%cn" -1'
        output = os.popen(cmd).read()
        return output
def get_log():
        cmd = 'git log --pretty=format:"%s" -1'
        output = os.popen(cmd).read()
        return output
def get_id():
        cmd = 'git log --pretty=format:"%h" -1'
        output = os.popen(cmd).read()
        return output
def post(content):
        url = "https://hook.lesschat.com/git/xxxxxxxxxxxxxxxx"
        data = {'payload': content}
        headers = {'Content-Type': 'application/json'}
        req = urllib2.Request(url = url, data = json.dumps(data), headers = headers)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        return

# switch the work path to repository path
# for example, your repository path is \usr\bin\myrepository, then switch to the path of \usr\bin\myrepository
os.chdir("xxxxxxxxxxxxx")

content = get_content()
post(content)
