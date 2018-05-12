# About
Timestretch (as the name implies) takes a .wav file and "stretches" it out, and saves it as a new .wav file. This script is currently being developed. Right now, basic linear interpolation is being used to compute new samples as a means to stretch out the original audio.

# Running the code
Ensure that the scipy and numpy packages are installed with Python 2.7 or above. Simply run
'timestretch.py filename.wav num_samples_to_add'
to see the code in action.

# Motivation
I was interested in implementing a few different interpolation techniques. In addition, I would like to incorporate an algorithm that uses extreme time-stretching to produce interesting and creative results. Stayed tuned!