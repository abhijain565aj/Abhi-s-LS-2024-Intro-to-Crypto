#!/bin/bash
unzip Riddle.zip
for((i=100;i>0;i--)){
	unzip $i
	echo "unzipped $i"
	rm $i.zip
}



