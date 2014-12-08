TEST TRAINER: a program designed to teach testing techniques and to teach through testing

Project Objectives and Description: The Test Trainer is designed as an “intelligent” test; e.g., as you are answering questions, the test redesigns itself to guide you in the right direction. Sometimes this will take the form of hints, other times the question will be broken down into smaller parts. The Test Trainer is meant as a supplement to traditional education and should be accompanied by regular practice in the subject area. However, use of the Test Trainer alone will make you a better test taker.

Installation: The package can be downloaded by cloning the url:
https://github.com/SamCD/TestTrainer.git

The music component of the program will make use of the Mingus package. Directions for downloading and installing Mingus can be found here:
https://code.google.com/p/mingus/wiki/tutorialSetup

Running the Program:

run_test(subject, category, level) runs the basic testing mechanism. Test data is given and then questions are asked through raw input. A wrong answer will prompt a hint and/or an additional question to help guide towards the right answer.

    Args: subject (string): Ma=Math, Rd=Reading
    category (string): subsection of the subject, e.g. Math has subsections \
    Geo (geometry), Alg (algebra); Reading has subsections Voc (vocabulary), \
    RH (Reading comprehension); Music has subsections KeySig (key signatures), \
    Scl (Scales), Cho (chords and inversions)
    level (integer): 1 is lowest, 3 is highest
    
    Ex:
    
    >>> run_test(Mu, Cho, 1)
    Dominant 7th, low to high: ["B", "D", "F", "G"]
    "What is the root of the chord?" "G"
    Great!

    >>> run_test(Mu, Cho, 1)
    Dominant 7th, low to high: ["B", "D", "F", "G"]
    "What is the root of the chord?" "B"
    Hmmm... A dominant chord in root position has a min 3rd (3 steps) on top.
    "How many steps between the top two notes?" 2
    "What is the root of the chord? "G"
    Great!
    """

After multiple attempts at the same question, the student will be asked for their questions/comments, which are stored as a list and finally written to a text file called “comments.txt”.

Rules, tips and hints used throughout the testing sequence are stored to a file called “review.txt”.

Using the program:
As stated in the “Project Objectives and Description”, the program is meant to be used an a supplement to traditional teaching techniques. The “comments.txt.” file should be used by the teacher to help facilitate communication with the student. The “review.txt” file is for the student, to help guide their studies, including topics for additional review and rules, tips and tricks.

Ex:

>>> run_test(Mu, Cho, 1)
    Dominant 7th, low to high: ["B", "D", "F", "G"]
    "What is the root of the chord?" "B"
    Hmmm... A dominant chord in root position has a min 3rd (3 steps) on top.
    "How many steps between the top two notes?" 2
    "What is the root of the chord? "D”
    Hmmm... A dominant chord in root position has a Maj 3rd (4 steps) on bottom.
    “What is the root of the chord? “F”
    Answer: “G”.
    “What questions do you still have” I dont know what root means

The teacher would have “I dont know what root means” for that students file. The student would have a layout of a dominant 7th chord in all inversions.

Attribution: The Mingus python module, including the tutorial,  was a great influence on this project.

Support: If you have questions about the module, or would like to provide feedback, or add a testing unit to the program, you can contact us by e-mail.


