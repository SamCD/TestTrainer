#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the student module. This is where the student takes graded tests\
and writes reports."""

import testlib as tl
import time
import os


class Student(object):
    """initializes a student. Takes no arguments; you will be asked for info.
    Ex: me = Student()"""


    def __init__(self):

        self.name=raw_input("What is your name? ")
        print "Hi, {}.".format(self.name)
        intro = open("intro",'r')
        print intro.read()
        intro.close()

        self.tests = {}


    def take_test(self,subj,lvl):
        """This command initiates a quiz. You will be asked a few questions.
        Any that are answered incorrectly will prompt a hint and a follow-up
        question. The follow-up is meant to be considered, but not officially
        answered.

        Args: subj (string): the test subject. Options are scale or chord
        level (int): 1 or 2. The test difficulty, in ascending order.

        Ex: Student.take_test("scale", 1)
            > What is this scale (..............)?"""
        
        print ("You will have two attempts, after which time a study report "
        "will be written for you and you will have the opportunity to send"
        "any feedback or comments to your instructor. "
        "Quizzes will count towards your score. "
        "\n"
        "You can always practice by taking a true_or_false() test!")

        mo = (subj,lvl)
        strt = time.time()
        score = 0
        study = []
        tfiles = ["{}questions{}".format(mo[0],mo[1]),
                  "{}answers{}".format(mo[0],mo[1]),
                  "{}hints".format(mo[0]),
                  "{}followups".format(mo[0])]
        question = 2
        while question > 0:
            answers = []
            anskey = []
            count = 0
            while count < 2:
                try:
                    qs = open(tfiles[count],'r')
                except IOError:
                    print "Test subject and/or level not available"
                ques = qs.read().split("\n")
                test = len(ques)
                if count == 0:
                    for i in range(test):
                        answers.append("")
                    quest = 0
                    while test > 1:
                        ans = raw_input(ques[quest])
                        answers[quest] = ans
                        quest += 1
                        test -= 1
                    count += 1
                    qs.close()
                else:
                    for i in ques:
                        anskey.append(i)
                    print "\n"
                    count += 1
                    for i,j in enumerate(answers):
                        if j == anskey[i]:
                            score += 1
                        elif question == 2:
                            print "Q" + str((i + 1))
                            ht = open(tfiles[count],'r')
                            fl = open(tfiles[count + 1],'r')
                            hints = ht.read().split("\n")
                            fups = fl.read().split("\n")
                            hint = hints[tl.hints[subj][lvl][i+1][0] - 1]
                            study.append(hint)
                            print hint
                            print fups[tl.hints[subj][lvl][i+1][1] - 1]
                            ht.close()
                            qs.close()
                        else:
                            continue
            if (score / len(ques)) < 0.7:
                question -= 1
            else:
                print "Nice job!"
                question -= 2
        fin = time.time()
        self.tests[subj + str(lvl)] = score * (1 + (1 / (fin - strt)))
        comm = raw_input("Comments or feedback for your instructor: ")
        self.report(self.name, self.tests, study, comm)


    def report(self,name, tests, study, comm):
        """Generates a report for the given subject.
        Args: name (char): the student name.
        tests (dict): The tests taken, with grades
        study (list): items to be added to the study file.
        comm (string): feedback from the student.
        Ex: > report('Sam', me.tests, me.study, 'Q3 was hard')
        > 
        # writes the list 'study' to the (your name).txt file """
        import os
        import time
        fname = os.path.abspath("{}.txt".format(name))
        report = [study, (comm,)]
        try:
            fh = open(fname, 'a')
        except IOError:
            fh = open(fname, 'w')
        finally:
            fh.write(str(time.time()) + "\n")
            for k, v in tests.iteritems():
                fh.write(k + " : " +str(v) + "\n")
            for i in report:
                for item in range(len(i)):
                    fh.write(i[item] + "\n")
            fh.flush()
            fh.close()
