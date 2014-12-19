#!/usr/bin/env python
# -*- coding: utf-8 -*-

import notelib

class Student(object):

    PassedTests = []
    score = 0

    def __init__(self,name):
        self.name=name

    def take_test(self,subject,level):
        mo = (subject,level)
        tfiles = ["{}questions.txt{}".format(mo[0],mo[1]),
                  "{}answers.txt{}".format(mo[0],mo[1]),
                  "{}hints.txt{}".format(mo[0],mo[1]),
                  "{}followups.txt{}".format(mo[0],mo[1])]
        counter = 0
        question = 0
        qs = open(tfiles[counter],'r').split()
        ans = raw_input(qs[0])
