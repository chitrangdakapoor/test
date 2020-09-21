#!/usr/bin/env python3

import os 
import subprocess

branches_flow = ['release/3.1','release/3.2', 'release/3.3']

def automatic_merge(current_branch, branches_flow):
    print('Auto-merging through: %s' % branches_flow)
    branch_index = branches_flow.index(current_branch)
    print (branch_index)
    print(len(branches_flow)-1)
    if branch_index < (len(branches_flow)-1):
        process = subprocess.Popen('git checkout %s ' % (branches_flow[branch_index+1]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(process.stdout.readlines())
    # for index  in range(branch_index+1,len(branches_flow)):
    #     process = subprocess.Popen('git checkout %s ' % (branches_flow[index]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #     print(process.stdout.readlines())
    #     process = subprocess.Popen('git merge %s ' % (current_branch), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #     print(process.stdout.readlines())
    #     if(not process.returncode):
    #         process = subprocess.Popen('git push', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        


current_branch = ((os.popen("git rev-parse --abbrev-ref HEAD")).read()).rstrip()
automatic_merge(current_branch, branches_flow)