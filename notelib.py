#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Note library"""

all_notes = ['A','A#','Bb','B','C','C#','Db','E','Fb',
             'E','E#','F','F#','Gb','G','G#','Ab']

enharmonics = {'C#':'Db','D#':'Eb','A#':'Bb','Bb':'A#',
               'Fb':'E','F#':'Gb','G#':'Ab','E#':'F',
               'Db':'C#','Gb':'F#','Ab':'G#'}
Major = {
'C':['C','D','E','F','G','A','B'],
'F':['F','G','A','Bb','C','D','E'],
'Bb':['Bb','C','D','Eb','F','G','A'],
'Eb':['Eb','F','G','Ab','Bb','C','D'],
'Ab':['Ab','Bb','C','Db','Eb','F','G'],
'Db':['Db','Eb','F','Gb','Ab','Bb','C'],
'Gb':['Gb','Ab','Bb','Cb','Db','Eb','F'],
'G':['G','A','B','C','D','E','F#'],
'D':['D','E','F#','G','A','B','C#'],
'A':['A','B','C#','D','E','F#','G#'],
'E':['E','F#','G#','A','B','C#','D#'],
'B':['B','C#','D#','E','F#','G#','A#'],
'F#':['F#','G#','A#','B#','C#','D#','E']
}

Minor = {
'C':['C','D','Eb','F','G','Ab','Bb'],
'F':['F','G','Ab','Bb','C','Db','Eb'],
'Bb':['Bb','C','Dd','Eb','F','Gb','Ab'],
'Eb':['Eb','F','Gb','Ab','Bb','Cb','Db'],
'G#':['G#','A#','B','C#','D#','E','F#'],
'C#':['C#','D#','E','F#','G#','A','B'],
'F#':['F#','G#','A','B','C#','D#','E'],
'G':['G','A','Bb','C','D','Eb','F'],
'D':['D','E','F','G','A','Bb','C'],
'A':['A','B','C','D','E','F','G'],
'E':['E','F#','G','A','B','C','D'],
'B':['B','C#','D','E','F#','G']
}
