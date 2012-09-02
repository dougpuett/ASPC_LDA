#!/bin/bash 
echo "Checking for LDA implementation..."
if [ -a LDA.tar.gz ];
	then 
		echo "DONE"
	else
		echo "Downloading LDA..."
		curl -L http://sourceforge.net/projects/gibbslda/files/latest/download -o "LDA.tar.gz"
		echo "DONE"
fi
echo "Checking for LDA installation..."
if [ -a GibbsLDA++-0.2 ];
	then 
		echo "DONE"
	else		
		echo "Extracting LDA..."
		tar xvzf LDA.tar.gz
		echo "DONE"
		echo "Installing LDA..."
		cd GibbsLDA++-0.2
		make clean
		make all
		cd ..
		echo "DONE"
fi
echo "Checking for poems..."
if [ -s poems1 ];
	then 
		echo "DONE"
	else
		echo "Downloading poems"
		python ascorpus.py 
		echo "DONE"
fi
path="$PWD/poems1"
path2="$PWD/lda.m"
echo "Checking for LDA output..."
if [ -s model-final.theta ];
	then 
		echo "DONE"
	else
		echo "Running LDA..."
		./GibbsLDA++-0.2/src/lda -est -ntopics 50 -niters 1000 -savestep 1000 -twords 25 -dfile $path
		echo "DONE"
fi

echo "Checking for Clustergram Data..."
if [ -s lda.csv ];
	then 
		echo "DONE"
	else
		echo "Formatting Data..."
		python tocsv.py
		echo "DONE"
fi
echo "Creating Clustergram..."
cd /Applications/MATLAB_R2011a.app/bin/
./matlab -nodesktop -r "run $path2"
echo "DONE"