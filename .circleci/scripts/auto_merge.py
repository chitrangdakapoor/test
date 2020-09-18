#!/usr/bin/env python3

import os 

branches_flow = ['release/3.1','release/3.2']

def automatic_merge(current_branch, branches_flow):
    print('Auto-merging through: %s' % branches_flow)
    branch_index = branches_flow.index(current_branch)
    print (branch_index)
    for index  in range(branch_index+1,len(branches_flow)):
        process = os.popen('git checkout %s ; git merge %s' % (branches_flow[index], current_branch))
        print(process.read())


current_branch = ((os.popen("git rev-parse --abbrev-ref HEAD")).read()).rstrip()
automatic_merge(current_branch, branches_flow)