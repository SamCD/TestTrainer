#!/usr/bin/env python
# -*- coding: utf-8 -*-

import notelib

class Student(object):

    PassedTests = []
    score = 0

    def __init__(self,name):
        self.name=name


    def take_test(self,subject,level):
        """This command initiates a quiz. You will be asked a few questions. Any that are answered incorrectly
        will prompt a hint and a follow-up question. The follow-up is meant to be considered, but not officially answered.
        You will have two attempts, after which time a study report will be written for you and you will have the
        opportunity to send any feedback or comments to your instructor.
        
        Args: subject (string): the test subject. Options are scale,chord or interval
              level (int): 1 or 2. The test difficulty, in ascending order. ** At this time, level 2 tests are not available
              for interval quizzes. **
        Ex: student_name.take_test("scale", 1)
            > What is this scale (..............)?
        """
        mo = (subject,level)
        answers = []
        anskey = []
        score = 0
        study = []
        tfiles = ["{}questions{}.txt".format(mo[0],mo[1]),
                  "{}answers{}.txt".format(mo[0],mo[1]),
                  "{}hints{}.txt".format(mo[0],mo[1]),
                  "{}followups{}.txt".format(mo[0],mo[1])]
        question = 1
        while question:
            counter = 4
            while counter:
                try:
                    qs = open(tfiles[counter],'r').split("\n")
                except IOError:
                    print "Test subject and/or level not available"
                test = len(qs)
                if counter == 4:
                    while test:
                        ans = raw_input(qs[0])
                        answers.append(ans[i])
                        test -= 1
                    counter -= 1
                    qs.close()
                else:
                    for i in qs:
                        anskey.append(qs[i])
                    counter -= 1
                    for i in answers:
                        if i == anskey[i]:
                            score += 1
                        else:
                            try:
                                ht = open(tfiles[counter],'r')
                                hints = hs.read().split("\n")
                                study.append(hints[i])
                                print hints[i]
                                print tfiles[counter - 1][i]
                                qs.close()
            question -= 1
        self.report(self.name, hints)


    def report(self,name, list_obj):
    """Generates a report for the given subject.
    Args: name (char): the type of report. Options are Comments, Study.
     list (char): the name of the list to be written to the report.
    Ex: > report(Study, study)
    > 
    # writes the list 'study' to the Study.txt file """
    import os
    import time
    fname = os.path.abspath("{}.txt".format(name))
    try:
        fh = open(fname, 'a')
    except IOError:
        fh = open(fname, 'w')
    finally:
        fh.write(time.time())
        for i in list:
            fh.write(list_obj[i])
        fh.close()
        fh.flush()
