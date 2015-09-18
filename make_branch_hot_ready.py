#!/usr/bin/env python
# coding: utf-8

import subprocess
import time
from datetime import datetime

class PrintProgress():
    def __init__(self, taskName):
        self.taskName = taskName
        self.beginTime = datetime.now()

    def printSpendingTime(self):
        self.endTime = datetime.now()
        print '%s Begins at :%s' % (self.taskName, self.beginTime)
        print '%s Ends at   :%s' % (self.taskName, self.endTime)
        print 'Spend time: %s \n'%(self.endTime - self.beginTime)
        print 'Finish!'

def main():
    gclientSynStr = "gclient sync --with_branch_heads -j 1 --nohooks --reset"
    gclientSync = gclientSynStr.split()
    progress = PrintProgress("gclient sync")
    subprocess.check_call(gclientSync)
    progress.printSpendingTime()

    generateProjectStr = "python wow_project.py"
    generateProject = generateProjectStr.split()
    progress = PrintProgress("Generate project")
    subprocess.check_call(generateProject)
    progress.printSpendingTime()

    buildWithNinjaStr = "ninja -C out\debug chrome"
    buildWithNinja = buildWithNinjaStr.split()
    progress = PrintProgress("build chrome with ninja")
    subprocess.check_call(buildWithNinja)
    progress.printSpendingTime()

if __name__ == '__main__':
    main()
