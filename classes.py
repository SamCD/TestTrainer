#!/usr/bin/env python
# -*- coding: utf-8 -*-

import notelib
import testfiles
import time
import os


class Student(object):
    """Begin by entering your name
    Ex: me = Student("Sam")"""


    def __init__(self):
        
        intro = open("intro",'r')
        print intro.read()
        intro.close()
        try:
            self.name=raw_input("What is your name? ")
        except NameError:
            self.name = "'" + name + "'"
        print "Hi, {}.".format(self.name)

        self.points = 0


    def take_test(self,subject,level):
        """This command initiates a quiz. You will be asked a few questions. Any that are answered incorrectly
        will prompt a hint and a follow-up question. The follow-up is meant to be considered, but not officially answered.
        You will have two attempts, after which time a study report will be written for you and you will have the
        opportunity to send any feedback or comments to your instructor.
        
        Quizzes will count towards your score. You can always practice by taking a true_or_false() test!
        
        Args: subject (string): the test subject. Options are scale,chord or interval
              level (int): 1 or 2. The test difficulty, in ascending order. ** At this time, level 2 tests are not available
              for interval quizzes. **
        Ex: student_name.take_test("scale", 1)
            > What is this scale (..............)?
        """

        mo = (subject,level)
        strt = time.time()
        answers = []
        anskey = []
        score = 0
        study = []
        tfiles = ["{}questions{}".format(mo[0],mo[1]),
                  "{}answers{}".format(mo[0],mo[1]),
                  "{}hints{}".format(mo[0],mo[1]),
                  "{}followups{}".format(mo[0],mo[1])]
        question = 2
        while question:
            counter = 0
            while counter < 4:
                try:
                    qs = open(tfiles[counter],'r')
                except IOError:
                    print "Test subject and/or level not available"
                ques = qs.read().split("\n")
                test = len(ques)
                if counter == 0:
                    quest = 0
                    while test > 0:
                        ans = raw_input(ques[quest])
                        answers.append(ans)
                        quest += 1
                        test -= 1
                    counter += 1
                    qs.close()
                else:
                    for i,j in enumerate(ques):
                        anskey.append(ques[i])
                    counter += 1
                    for i,j in enumerate(answers):
                        if j == anskey[i]:
                            score += 1
                        else:
                            ht = open(tfiles[counter],'r')
                            hints = ht.read().split("\n")
                            study.append(hints[i])
                            print hints[i]
                            print tfiles[counter + 1][i]
                            qs.close()
            if (score / len(ques)) > 0.6:
                print "Nice job!"
                break
            else:
                question -= 1
        fin = time.time()
        self.points += score * (1 + (1 / (fin - strt)))
        self.report(self.name, hints)


