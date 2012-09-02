By Doug Puett, 9/1/2012

To run, open the terminal, CD into this directory and run:
$ bash run.sh

To run on OSX, you'll need to download mac's xcode command line tools from here: 
https://developer.apple.com/downloads/index.action#
(THIS TAKES SO LONG! UGH. STUPID MAC)

You'll also need MATLAB, and I assume it is in the same place on your computers as it is mine. If not, you'll have to edit the path in the run.sh file. I wanted to get the clustergram to run in Python, but couldn't for the life of me figure it out. 

NOTE:
The clustergram is a little different than before:
This time, the rows are the LDA cluster values, and only the columns represent the actual poems. Each column is represented by a number at the bottom of the clustergram (it is much bigger this time, so you'll have to zoom in). The numbers correspond to the poems in the file names.csv

Manual for the LDA implementation is here: http://gibbslda.sourceforge.net/

I have made no attempt to adjust parameters, iterations, number of clusters, etc. Doing so will, I'm sure, yield interesting results.

I have also made no attempt at any sort of interpretation or analysis.

I'll probably be putting this up on GITHUB soon, so that we can all mutually edit the program(s)
