#!/usr/bin/env python3

import os 
import subprocess
import re

# branches = subprocess.Popen('git branch --list \'release/*\' ' , shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# print(branches.stdout.readlines())
# squared = list(map(lambda x: x**2, branches))
branches_flow = ['release/3.1','release/3.2', 'release/3.3']

def automatic_merge(current_branch, branches_flow):
    print('Auto-merging through: %s' % branches_flow)
    branch_index = branches_flow.index(current_branch)
    if branch_index < (len(branches_flow)-1):
        print ('git checkout %s ' % (branches_flow[branch_index+1]))
        process = subprocess.Popen('git checkout %s ' % (branches_flow[branch_index+1]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print('git merge %s ' % (current_branch))
        print(process.stdout.readlines())
        process1 = subprocess.Popen('git merge %s -m \"auto merge\"' % (current_branch), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(process1.stdout.readlines())
        process1.communicate()[0]
        return (process1.returncode)

current_branch = ((os.popen("git rev-parse --abbrev-ref HEAD")).read()).rstrip()
status = automatic_merge(current_branch, branches_flow)