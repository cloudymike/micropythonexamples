#!/bin/bash
if [ "$1" != "" ]
then
	DIRS=$1
else
	DIRS=*
fi

for d in $DIRS
do
	if [[ -d $d ]]
	then
		if [[ -f "$d/test.py" ]]
		then
			echo Testing $d
			pushd $d &> /dev/null
			timeout 120 ./RUN.sh &>/dev/null
			timeout 60 ampy --port /dev/ttyUSB0 run test.py | grep TESTOK
			OK=$?
			if [ "$OK" != "0" ]
			then
				echo "Test Failed"
			fi
			popd &> /dev/null
		fi
	fi
done
