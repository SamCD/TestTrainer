def chord_query(note):
"""Asks the first question of ChordTest1
  Args: note can be any note between A and G. MUST be surrounded by quotes.
  """
    import mingus.core.intervals as it
    import mingus.core.diatonic as dt
    import mingus.core.notes as nt
    import mingus.core.chords as crd
    chord =  crd.first_inversion(crd.V7(note))
    print chord
    fh = "ChordTest1.txt"
    ques1 = raw_input("{}").format(fh.readline())
    counter = 2
    while counter:
        if ques1 == dt.get_notes(note)[4]:
            print "Great!"
        elif ques1 not in chord:
            print "Remember, " + testtrainer.chordtips.chord5
            counter -= 1
            chord_query(note)
        else: ques1 in chord and ques1 != dt.get_notes(note)[4]:
            if ques1 == chord[1]:
                print "Hmmm... " + testtrainer.chordtips.chord6
                counter -= 1
                chord_query(note)
